"""pipeline/discovery/forum_nga.py — NGA 魔兽争霸三版块爬虫（1 req/2s）"""
from __future__ import annotations

import asyncio
import logging

logger = logging.getLogger(__name__)

NGA_WC3_URL = "https://bbs.nga.cn/thread.php?fid=242"  # War3 版块


async def scrape_nga(max_threads: int = 20) -> list:
    """爬取 NGA 魔兽争霸三版块最新帖子，速率：1 req/2s"""
    import httpx
    from bs4 import BeautifulSoup
    from discovery.hive_scraper import CandidateTopic

    candidates: list[CandidateTopic] = []

    try:
        await asyncio.sleep(2)

        def _fetch():
            with httpx.Client(timeout=15, follow_redirects=True, headers={
                "User-Agent": "Mozilla/5.0 War3WikiBot/1.0",
                "Accept-Language": "zh-CN,zh;q=0.9",
            }) as c:
                return c.get(NGA_WC3_URL).text

        html = await asyncio.get_event_loop().run_in_executor(None, _fetch)
        soup = BeautifulSoup(html, "html.parser")

        for row in soup.select("tr.topicrow")[:max_threads]:
            title_el = row.select_one("td.c2 a.topic_link")
            if not title_el:
                continue
            title = title_el.get_text(strip=True)
            href = title_el.get("href", "")
            url = "https://bbs.nga.cn/" + href.lstrip("/") if href else ""
            if not url:
                continue

            # 提取回复数
            reply_el = row.select_one("td.c4")
            replies = int(reply_el.get_text(strip=True)) if reply_el else 0

            score = min(1.0, replies / 50)
            candidates.append(CandidateTopic(
                title=title,
                url=url,
                source="nga",
                popularity_score=score,
                reply_count=replies,
            ))

    except Exception as e:
        logger.warning(f"NGA 爬取失败: {e}")

    logger.info(f"🎮 NGA: {len(candidates)} 个候选话题")
    return candidates
