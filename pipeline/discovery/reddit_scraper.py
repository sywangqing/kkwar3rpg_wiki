"""pipeline/discovery/reddit_scraper.py — Reddit r/WC3 话题爬虫（PRAW）"""
from __future__ import annotations

import logging
import os

logger = logging.getLogger(__name__)


def scrape_reddit_wc3(limit: int = 50) -> list:
    """
    使用 PRAW 获取 r/WC3 的热门帖子。
    过滤条件：score > 20 AND num_comments > 5。
    需要环境变量：REDDIT_CLIENT_ID / REDDIT_CLIENT_SECRET / REDDIT_USER_AGENT
    """
    from discovery.hive_scraper import CandidateTopic

    client_id = os.getenv("REDDIT_CLIENT_ID", "")
    client_secret = os.getenv("REDDIT_CLIENT_SECRET", "")
    user_agent = os.getenv("REDDIT_USER_AGENT", "war3-wiki-bot/1.0")

    if not client_id or not client_secret:
        logger.warning("Reddit API 凭证未配置，跳过 Reddit 爬取")
        return []

    try:
        import praw  # type: ignore
    except ImportError:
        logger.warning("praw 未安装，跳过 Reddit 爬取 (pip install praw)")
        return []

    try:
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent,
        )

        candidates: list[CandidateTopic] = []
        subreddit = reddit.subreddit("WC3")

        for post in subreddit.hot(limit=limit):
            if post.score <= 20 or post.num_comments <= 5:
                continue
            score = min(1.0, (post.score / 500 + post.num_comments / 100) / 2)
            candidates.append(CandidateTopic(
                title=post.title,
                url=f"https://reddit.com{post.permalink}",
                source="reddit",
                popularity_score=score,
                view_count=0,  # Reddit API 不提供 view 数
                reply_count=post.num_comments,
            ))

        logger.info(f"🔴 Reddit r/WC3: {len(candidates)} 个候选话题")
        return candidates

    except Exception as e:
        logger.warning(f"Reddit 爬取失败: {e}")
        return []
