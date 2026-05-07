"""
pipeline/discovery/kk_scraper.py
KK 官方对战平台 + KK 开发者平台 爬虫

抓取范围：
  1. create.kkdzpt.com/help       — 帮助中心（公开）
  2. create.kkdzpt.com/news/      — 开发者新闻资讯（公开）
  3. kkdzpt.com/news/developer     — 开发者公告（需登录）
  4. kkdzpt.com/news/platform      — 平台更新（需登录）

登录凭据通过环境变量 KK_USERNAME / KK_PASSWORD 传入。
"""
from __future__ import annotations

import asyncio
import logging
import os
import time
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)

KK_MAIN = "https://www.kkdzpt.com"
KK_CREATE = "https://create.kkdzpt.com"
KK_LOGIN_API = "https://www.kkdzpt.com/api/user/login"

# 对 Wiki 有价值的新闻分类
NEWS_CATEGORIES = [
    ("developer", "开发者公告"),
    ("platform",  "平台更新"),
]

# 帮助中心 Tab（公开，无需登录）
HELP_TABS = [
    ("function", "功能指南"),
    ("rule",     "规则中心"),
    ("service",  "服务与支持"),
]


@dataclass
class CandidateTopic:
    title: str
    url: str
    source: str = "kk_official"
    popularity_score: float = 0.5
    view_count: int = 0
    reply_count: int = 0
    extra: dict = field(default_factory=dict)


# ---------------------------------------------------------------------------
# 登录工具
# ---------------------------------------------------------------------------

def _get_kk_session() -> "httpx.Client | None":
    """
    用账号密码登录 KK，返回携带 Cookie 的 httpx.Client。
    失败时返回 None（只抓公开内容）。
    """
    import httpx

    username = os.getenv("KK_USERNAME", "")
    password = os.getenv("KK_PASSWORD", "")

    if not username or not password:
        logger.warning("⚠️  KK_USERNAME/KK_PASSWORD 未配置，跳过需登录内容")
        return None

    client = httpx.Client(
        timeout=20,
        follow_redirects=True,
        headers={"User-Agent": "Mozilla/5.0 War3WikiBot/1.0"},
    )
    try:
        # 先访问首页获取基础 Cookie
        client.get(KK_MAIN)

        # 提交登录表单
        resp = client.post(KK_LOGIN_API, json={
            "phone": username,
            "password": password,
            "loginType": 1,
        })
        data = resp.json()
        if data.get("code") == 200 or data.get("success"):
            logger.info("✅ KK 平台登录成功")
            return client
        else:
            logger.warning(f"⚠️  KK 登录失败: {data.get('msg', resp.text[:200])}")
            return None
    except Exception as e:
        logger.warning(f"⚠️  KK 登录异常: {e}")
        return None


# ---------------------------------------------------------------------------
# 公开内容：帮助中心
# ---------------------------------------------------------------------------

async def _scrape_help_center(loop) -> list[CandidateTopic]:
    """抓取 create.kkdzpt.com/help 下的各类文章标题，作为候选话题"""
    import httpx
    from bs4 import BeautifulSoup

    candidates: list[CandidateTopic] = []

    def _fetch():
        with httpx.Client(timeout=15, follow_redirects=True,
                          headers={"User-Agent": "Mozilla/5.0 War3WikiBot/1.0"}) as c:
            # 帮助中心是 SPA，先拿主页 HTML 看能否获取文章列表
            resp = c.get(f"{KK_CREATE}/help")
            return resp.text

    try:
        html = await loop.run_in_executor(None, _fetch)
        soup = BeautifulSoup(html, "html.parser")

        # 尝试提取侧边栏文章链接（不同 SPA 可能需要接口）
        links = soup.select("a[href*='/help']")
        seen = set()
        for a in links:
            title = a.get_text(strip=True)
            href = a.get("href", "")
            if not title or len(title) < 3 or href in seen:
                continue
            # 过滤导航类链接
            if title in ("帮助中心", "开发者平台", "登录"):
                continue
            seen.add(href)
            full_url = href if href.startswith("http") else KK_CREATE + href
            candidates.append(CandidateTopic(
                title=f"KK平台：{title}",
                url=full_url,
                source="kk_help",
                popularity_score=0.8,
                extra={"section": "帮助中心"},
            ))
            logger.debug(f"  帮助中心候选: {title}")

        logger.info(f"📋 帮助中心候选: {len(candidates)} 条")
    except Exception as e:
        logger.warning(f"⚠️  帮助中心爬取失败: {e}")

    return candidates


# ---------------------------------------------------------------------------
# 公开内容：开发者新闻资讯
# ---------------------------------------------------------------------------

async def _scrape_create_news(loop) -> list[CandidateTopic]:
    """抓取 create.kkdzpt.com/news/ 开发者资讯"""
    import httpx
    from bs4 import BeautifulSoup

    candidates: list[CandidateTopic] = []

    def _fetch():
        with httpx.Client(timeout=15, follow_redirects=True,
                          headers={"User-Agent": "Mozilla/5.0 War3WikiBot/1.0"}) as c:
            return c.get(f"{KK_CREATE}/news/").text

    try:
        html = await loop.run_in_executor(None, _fetch)
        soup = BeautifulSoup(html, "html.parser")

        # 通用文章链接选择器
        for a in soup.select("a[href*='/news/'], a[href*='/article/']"):
            title = a.get_text(strip=True)
            href = a.get("href", "")
            if not title or len(title) < 4:
                continue
            # 只保留与 War3/地图开发相关的文章
            keywords = ["地图", "war3", "魔兽", "编辑器", "开发者", "作者", "更新", "公告",
                        "触发", "脚本", "jass", "lua", "rpg", "发布", "审核"]
            if not any(kw in title.lower() for kw in keywords):
                continue
            full_url = href if href.startswith("http") else KK_CREATE + href
            candidates.append(CandidateTopic(
                title=title,
                url=full_url,
                source="kk_news",
                popularity_score=0.7,
                extra={"section": "开发者资讯"},
            ))

        logger.info(f"📋 开发者资讯候选: {len(candidates)} 条")
    except Exception as e:
        logger.warning(f"⚠️  开发者资讯爬取失败: {e}")

    return candidates


# ---------------------------------------------------------------------------
# 需登录：KK 官网新闻（开发者公告 + 平台更新）
# ---------------------------------------------------------------------------

async def _scrape_kk_news_with_login(loop, session) -> list[CandidateTopic]:
    """用已登录的 session 抓取开发者公告和平台更新"""
    from bs4 import BeautifulSoup

    candidates: list[CandidateTopic] = []

    for cat_key, cat_name in NEWS_CATEGORIES:
        url = f"{KK_MAIN}/news/{cat_key}"
        try:
            await asyncio.sleep(1)

            def _fetch(u=url, s=session):
                return s.get(u).text

            html = await loop.run_in_executor(None, _fetch)
            soup = BeautifulSoup(html, "html.parser")

            # KK 官网文章列表选择器
            for a in soup.select("a[href*='/article/']"):
                title = a.get_text(strip=True)
                href = a.get("href", "")
                if not title or len(title) < 4:
                    continue
                # 过滤与地图开发相关的内容
                keywords = ["地图", "war3", "魔兽", "编辑器", "开发者", "作者",
                            "更新", "公告", "审核", "发布", "触发", "脚本", "rpg"]
                if not any(kw in title.lower() for kw in keywords):
                    continue
                full_url = href if href.startswith("http") else KK_MAIN + href
                candidates.append(CandidateTopic(
                    title=title,
                    url=full_url,
                    source="kk_official",
                    popularity_score=0.85,
                    extra={"section": cat_name},
                ))
                logger.debug(f"  [{cat_name}] {title}")

            logger.info(f"📋 {cat_name} 候选: {len([c for c in candidates if c.extra.get('section') == cat_name])} 条")

        except Exception as e:
            logger.warning(f"⚠️  {cat_name} 爬取失败: {e}")

    return candidates


# ---------------------------------------------------------------------------
# 主入口
# ---------------------------------------------------------------------------

async def scrape_kk_official() -> list[CandidateTopic]:
    """
    KK 官网全量爬取入口。
    返回 CandidateTopic 列表供 DiscovererAgent 评估。
    """
    loop = asyncio.get_event_loop()
    all_candidates: list[CandidateTopic] = []

    # 1. 公开内容并行抓取
    help_task = _scrape_help_center(loop)
    news_task = _scrape_create_news(loop)
    help_candidates, news_candidates = await asyncio.gather(help_task, news_task)
    all_candidates.extend(help_candidates)
    all_candidates.extend(news_candidates)

    # 2. 需登录内容
    session = await loop.run_in_executor(None, _get_kk_session)
    if session:
        try:
            login_candidates = await _scrape_kk_news_with_login(loop, session)
            all_candidates.extend(login_candidates)
        finally:
            session.close()

    logger.info(f"✅ KK 官网总候选话题: {len(all_candidates)} 条")
    return all_candidates
