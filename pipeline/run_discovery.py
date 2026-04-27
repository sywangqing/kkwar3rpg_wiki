"""
pipeline/run_discovery.py — 话题自主发现入口
每日调用：爬取四个社区来源 → LLM 评估 → 追加至 topics.json

用法：
    cd pipeline
    python run_discovery.py [--dry-run]
"""
from __future__ import annotations

import argparse
import asyncio
import json
import logging
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

_PIPELINE_DIR = Path(__file__).parent
sys.path.insert(0, str(_PIPELINE_DIR))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

TOPICS_PATH = _PIPELINE_DIR / "cache" / "topics.json"


def _load_topics() -> list[dict]:
    if TOPICS_PATH.exists():
        return json.loads(TOPICS_PATH.read_text(encoding="utf-8"))
    return []


def _save_topics(topics: list[dict]) -> None:
    TOPICS_PATH.parent.mkdir(parents=True, exist_ok=True)
    TOPICS_PATH.write_text(json.dumps(topics, ensure_ascii=False, indent=2), encoding="utf-8")


def _dedup_new_topics(existing: list[dict], new: list[dict]) -> list[dict]:
    """过滤掉 slug 或 title 与已有话题重复的新话题"""
    existing_slugs = {t.get("slug", "") for t in existing}
    existing_titles = {t.get("title", "").lower() for t in existing}
    fresh = []
    for t in new:
        if t.get("slug") in existing_slugs:
            logger.debug(f"  重复 slug，跳过: {t['slug']}")
            continue
        if t.get("title", "").lower() in existing_titles:
            logger.debug(f"  重复标题，跳过: {t['title']}")
            continue
        fresh.append(t)
    return fresh


async def main(dry_run: bool = False) -> None:
    logger.info("🚀 话题发现流水线启动")

    # 1. 并行爬取四个来源
    from discovery.hive_scraper import scrape_hive_workshop
    from discovery.reddit_scraper import scrape_reddit_wc3
    from discovery.forum_nga import scrape_nga

    hive_task = scrape_hive_workshop(max_threads=40)
    nga_task = scrape_nga(max_threads=20)

    hive_candidates, nga_candidates = await asyncio.gather(hive_task, nga_task)

    # Reddit 是同步的（PRAW）
    loop = asyncio.get_event_loop()
    reddit_candidates = await loop.run_in_executor(None, lambda: scrape_reddit_wc3(limit=50))

    all_candidates = hive_candidates + reddit_candidates + nga_candidates
    logger.info(f"📊 总候选话题: {len(all_candidates)} 条")

    if not all_candidates:
        logger.info("无新候选话题，结束")
        return

    # 2. 加载现有话题
    existing_topics = _load_topics()

    # 3. LLM 评估
    from agents.discoverer.agent import DiscovererAgent
    discoverer = DiscovererAgent()
    accepted = await discoverer.evaluate_candidates(all_candidates, existing_topics)

    # 4. 去重
    truly_new = _dedup_new_topics(existing_topics, accepted)
    logger.info(f"✅ 最终新增话题: {len(truly_new)} 条 (从 {len(accepted)} 个接受中去重)")

    if not truly_new:
        logger.info("无新增话题")
        return

    for t in truly_new:
        logger.info(f"  + [{t['source']}] {t['title']} ({t['slug']})")

    # 5. 写回 topics.json
    if dry_run:
        logger.info("🔍 [dry-run] 未写入 topics.json")
        print(json.dumps(truly_new, ensure_ascii=False, indent=2))
    else:
        updated = existing_topics + truly_new
        _save_topics(updated)
        logger.info(f"💾 topics.json 已更新: {len(existing_topics)} → {len(updated)} 条")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="War3 Wiki 话题发现")
    parser.add_argument("--dry-run", action="store_true", help="不写入 topics.json，仅打印结果")
    args = parser.parse_args()
    asyncio.run(main(dry_run=args.dry_run))
