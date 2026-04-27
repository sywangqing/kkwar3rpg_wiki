"""pipeline/agents/discoverer/agent.py — Discoverer Agent：LLM 评估 + 话题接受/拒绝"""
from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from pathlib import Path

from agents.base import BaseAgent, extract_json_from_response
from discovery.hive_scraper import CandidateTopic

logger = logging.getLogger(__name__)

_PROMPT_DIR = Path(__file__).parent


class DiscovererAgent(BaseAgent):
    """
    接收来自各论坛的候选话题列表，调用 LLM 评估相关性/价值/新颖性，
    返回被接受的话题。
    """

    PROMPT_DIR = _PROMPT_DIR

    async def evaluate_candidates(
        self,
        candidates: list[CandidateTopic],
        existing_topics: list[dict],
        batch_size: int = 15,
    ) -> list[dict]:
        """
        批量评估候选话题，返回被接受的话题列表（已格式化为 topics.json 条目）。
        """
        if not candidates:
            return []

        # 构建现有话题标题样本（用于新颖性对比）
        existing_titles = [t.get("title", "") for t in existing_topics[:50]]

        accepted: list[dict] = []

        # 分批处理（防止单次 prompt 过长）
        for i in range(0, len(candidates), batch_size):
            batch = candidates[i: i + batch_size]
            candidates_json = [
                {
                    "title": c.title,
                    "url": c.url,
                    "source": c.source,
                    "popularity_score": c.popularity_score,
                    "replies": c.reply_count,
                }
                for c in batch
            ]

            prompt = self._render_prompt(
                existing_topics_sample=existing_titles,
                candidates_json=candidates_json,
            )

            # 创建伪 context 用于 retry 日志
            from models import ResearchContext
            dummy_ctx = ResearchContext(
                topic_id="discoverer", title="Discoverer", category="discovery", slug="discoverer"
            )

            try:
                raw = await self._call_llm_with_retry(
                    prompt, dummy_ctx, max_tokens=3000, temperature=0.2
                )
                results = json.loads(extract_json_from_response(raw))
            except Exception as e:
                logger.error(f"DiscovererAgent 评估失败（批次 {i}）: {e}")
                continue

            now = datetime.now(timezone.utc).isoformat()
            for item in results:
                if not item.get("accept"):
                    logger.debug(f"❌ 拒绝: {item.get('original_title', '?')} — {item.get('reason', '')}")
                    continue

                # 匹配回原始 CandidateTopic
                original = next(
                    (c for c in batch if c.title == item.get("original_title")), None
                )
                source_urls = [original.url] if original else []

                new_topic = {
                    "topic_id": item["suggested_slug"],
                    "title": item["suggested_wiki_title"],
                    "slug": item["suggested_slug"],
                    "category": item.get("suggested_category", "general"),
                    "status": "pending",
                    "retry_count": 0,
                    "source": original.source if original else "unknown",
                    "source_urls": source_urls,
                    "discovered_at": now,
                    "popularity_score": original.popularity_score if original else 0.0,
                    "discovered_via": original.source if original else "unknown",
                }
                accepted.append(new_topic)
                logger.info(f"✅ 接受新话题: {item['suggested_wiki_title']}")

        logger.info(f"🔍 DiscovererAgent: {len(candidates)} 候选 → {len(accepted)} 接受")
        return accepted
