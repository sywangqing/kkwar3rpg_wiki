"""pipeline/agents/writer/agent.py — Writer Agent"""
from __future__ import annotations

import json
import logging
import re
from pathlib import Path

from agents.base import BaseAgent, strip_think_tags
from models import ResearchContext

logger = logging.getLogger(__name__)

_PROMPT_DIR = Path(__file__).parent


class WriterAgent(BaseAgent):
    """
    逐节撰写文章，注入引用标记，生成 ## 参考来源 区块。
    支持 Reviewer 反馈后的重写。
    """

    PROMPT_DIR = _PROMPT_DIR

    async def run(self, context: ResearchContext, reviewer_feedback: str = "") -> ResearchContext:
        logger.info(f"✍️  WriterAgent 开始: {context.title} (loop {context.review_loop_count})")

        source_registry = [
            {"id": s.id, "url": s.url, "title": s.title, "snippet": s.snippet[:300]}
            for s in context.sources
        ]

        section_parts: list[str] = []

        for node in context.outline:
            # 构建该节的提纲文本
            section_outline = f"{'#' * node.level} {node.title}"
            for child in node.children:
                section_outline += f"\n{'#' * child.level} {child.title}"

            prompt = self._render_prompt(
                topic=context.title,
                section_title=node.title,
                section_outline=section_outline,
                source_registry_json=source_registry,
                reviewer_feedback=reviewer_feedback or "无反馈（首次撰写）",
            )

            section_text = await self._call_llm_with_retry(
                prompt, context, max_tokens=1500, temperature=0.4
            )
            section_text = strip_think_tags(section_text)
            section_parts.append(section_text)
            context.section_drafts[node.title] = section_text
            logger.debug(f"  ✓ 节完成: {node.title} ({len(section_text)} 字符)")

        # 拼接全文
        body = "\n\n".join(section_parts)

        # 标记被引用的来源（扫描 [^N] 标记）
        cited_ids = {int(m) for m in re.findall(r"\[\^(\d+)\]", body)}
        for s in context.sources:
            if s.id in cited_ids:
                s.used = True

        # 生成 ## 参考来源 区块
        used_sources = context.get_used_sources()
        if used_sources:
            refs_block = "\n\n## 参考来源\n\n" + "\n".join(s.footnote_def for s in used_sources)
        else:
            refs_block = ""

        context.draft = body + refs_block
        logger.info(
            f"✅ WriterAgent 完成: {len(context.draft)} 字符, "
            f"{len(used_sources)}/{len(context.sources)} 来源被引用"
        )
        return context

    def _build_references_block(self, context: ResearchContext) -> str:
        """（外部可调用）重新生成参考来源区块"""
        used = context.get_used_sources()
        if not used:
            return ""
        return "\n\n## 参考来源\n\n" + "\n".join(s.footnote_def for s in used)
