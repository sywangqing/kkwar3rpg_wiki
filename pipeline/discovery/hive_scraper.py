"""pipeline/discovery/hive_scraper.py — Hive Workshop 论坛话题爬虫（1 req/sec）"""
from __future__ import annotations

import asyncio
import logging
import time
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)

HIVE_BASE = "https://www.hiveworkshop.com"
TARGET_SUBFORUMS = [
    "/forums/jass-ai-scripts-tutorials.279/",
    "/forums/triggers-scripts.102/",
    "/forums/resources.324/",
    "/forums/tutorials.293/",
]


@dataclass
class CandidateTopic:
    title: str
    url: str
    source: str  # "hive" | "reddit" | "9ddota" | "nga"
    popularity_score: float = 0.0
    view_count: int = 0
    reply_count: int = 0


async def scrape_hive_workshop(max_threads: int = 30) -> list[CandidateTopic]:
    """
    爬取 Hive Workshop 多个子版块的最新帖子。
    速率：1 请求/秒。
    """
    import httpx
    from bs4 import BeautifulSoup

    candidates: list[CandidateTopic] = []

    for subforum in TARGET_SUBFORUMS:
        url = HIVE_BASE + subforum
        try:
            await asyncio.sleep(1)  # 1 req/sec 限速

            def _fetch(u=url):
                with httpx.Client(timeout=15, follow_redirects=True, headers={
                    "User-Agent": "War3WikiBot/1.0"
                }) as c:
                    return c.get(u).text

            html = await asyncio.get_event_loop().run_in_executor(None, _fetch)
            soup = BeautifulSoup(html, "html.parser")

            # 解析帖子列表
            for thread in soup.select("div.structItem--thread"):
                title_el = thread.select_one("div.structItem-title a")
                if not title_el:
                    continue
                title = title_el.get_text(strip=True)
                href = title_el.get("href", "")
                if not href:
                    continue
                full_url = HIVE_BASE + href if href.startswith("/") else href

                # 获取回复/浏览数
                replies = 0
                views = 0
                for meta in thread.select("dd"):
                    text = meta.get_text(strip=True).replace(",", "")
                    if text.isdigit():
                        val = int(text)
                        if replies == 0:
                            replies = val
                        else:
                            views = val

                score = min(1.0, (replies * 2 + views / 100) / 200)
                candidates.append(CandidateTopic(
                    title=title,
                    url=full_url,
                    source="hive",
                    popularity_score=score,
                    reply_count=replies,
                    view_count=views,
                ))

                if len(candidates) >= max_threads:
                    break

        except Exception as e:
            logger.warning(f"Hive Workshop 爬取失败 ({subforum}): {e}")

    logger.info(f"🏚️  Hive Workshop: {len(candidates)} 个候选话题")
    return candidates
