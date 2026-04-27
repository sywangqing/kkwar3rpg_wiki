"""pipeline/agents/planner/agent.py — Planner Agent"""
from __future__ import annotations

import json
import logging
from pathlib import Path

from agents.base import BaseAgent, extract_json_from_response
from models import OutlineNode, ResearchContext

logger = logging.getLogger(__name__)

_PROMPT_DIR = Path(__file__).parent


class PlannerAgent(BaseAgent):
    """
    接收主题信息，输出：
    - 文章大纲（OutlineNode 树）
    - 各节的搜索查询列表
    """

    PROMPT_DIR = _PROMPT_DIR

    async def run(self, context: ResearchContext) -> ResearchContext:
        logger.info(f"📐 PlannerAgent 开始: {context.title}")

        prompt = self._render_prompt(
            topic=context.title,
            category=context.category,
            initial_context="\n".join(context.source_urls) if context.source_urls else "无",
        )

        raw = await self._call_llm_with_retry(prompt, context, max_tokens=2048, temperature=0.3)

        try:
            data = json.loads(extract_json_from_response(raw))
        except json.JSONDecodeError as e:
            logger.error(f"PlannerAgent JSON 解析失败: {e}\n原始输出: {raw[:300]}")
            context.log_error("PlannerAgent", f"JSON 解析失败: {e}")
            # 降级：使用最小大纲继续
            data = {
                "outline": [{"title": "概述", "level": 2, "search_queries": [context.title], "children": []}],
                "global_queries": [context.title, f"Warcraft III {context.title}"],
            }

        # 解析大纲
        context.outline = [OutlineNode(**node) for node in data.get("outline", [])]

        # 汇总所有搜索查询
        all_queries: list[str] = list(data.get("global_queries", []))
        for node in context.outline:
            all_queries.extend(node.search_queries)
        context.search_queries = list(dict.fromkeys(all_queries))  # 去重保序

        logger.info(
            f"✅ PlannerAgent 完成: {len(context.outline)} 节, {len(context.search_queries)} 个查询"
        )
        return context
