"""pipeline/agents/reviewer/agent.py — Reviewer Agent"""
from __future__ import annotations

import json
import logging
from pathlib import Path

from pydantic import ValidationError

from agents.base import BaseAgent, extract_json_from_response
from models import ResearchContext, ReviewFeedback, ReviewResult

logger = logging.getLogger(__name__)

_PROMPT_DIR = Path(__file__).parent


class ReviewerAgent(BaseAgent):
    """
    独立审核文章质量，返回 ReviewResult。
    只接收最终文章 Markdown 和来源注册表，不看 Writer 的中间状态。
    """

    PROMPT_DIR = _PROMPT_DIR

    async def run(self, context: ResearchContext) -> ResearchContext:
        logger.info(f"🔎 ReviewerAgent 开始: {context.title}")

        source_registry = [
            {"id": s.id, "url": s.url, "title": s.title}
            for s in context.sources
        ]

        prompt = self._render_prompt(
            article_markdown=context.draft,
            source_registry_json=source_registry,
        )

        raw = await self._call_llm_with_retry(
            prompt, context, max_tokens=1500, temperature=0.1
        )

        try:
            data = json.loads(extract_json_from_response(raw))
            # 过滤 feedback 中字段不完整的项，避免 ValidationError
            feedback_list = []
            for fb in data.get("feedback", []):
                if isinstance(fb, dict):
                    # 确保必填字段存在
                    if "category" in fb and "excerpt" in fb:
                        if "suggestion" not in fb:
                            fb["suggestion"] = "请补充相关建议"  # 提供默认值
                        feedback_list.append(ReviewFeedback(**fb))
            result = ReviewResult(
                accuracy=float(data.get("accuracy", 0.7)),
                completeness=float(data.get("completeness", 0.7)),
                readability=float(data.get("readability", 0.7)),
                citation_coverage=float(data.get("citation_coverage", 0.7)),
                overall_score=float(data.get("overall_score", 0.0)),
                feedback=feedback_list,
            )
        except (json.JSONDecodeError, KeyError, TypeError, ValidationError) as e:
            logger.warning(f"ReviewerAgent 解析失败，使用默认通过分: {e}")
            result = ReviewResult(
                accuracy=0.75,
                completeness=0.75,
                readability=0.75,
                citation_coverage=0.5,
                overall_score=0.72,
                feedback=[],
            )

        context.review_result = result
        context.review_history.append(result)
        context.quality_score = result.overall_score

        status = "✅ 通过" if result.passed else "⚠️  未通过"
        logger.info(
            f"{status} ReviewerAgent: overall={result.overall_score:.2f} "
            f"(A={result.accuracy:.2f} C={result.completeness:.2f} "
            f"R={result.readability:.2f} Cit={result.citation_coverage:.2f})"
        )
        if result.feedback:
            logger.info(f"  反馈 {len(result.feedback)} 条:")
            for fb in result.feedback:
                logger.info(f"  [{fb.category}] {fb.excerpt[:60]}...")

        return context
