"""pipeline/agents/researcher/agent.py — Researcher Agent"""
from __future__ import annotations

import json
import logging
from pathlib import Path

from agents.base import BaseAgent, extract_json_from_response
from models import ResearchContext, SearchResult
from search.bilingual import bilingual_search
from search.extractor import fetch_pages_batch
from search.orchestrator import MultiSourceSearch

logger = logging.getLogger(__name__)

_PROMPT_DIR = Path(__file__).parent
_MIN_SOURCES = 3


class ResearcherAgent(BaseAgent):
    """
    执行搜索查询、抓取页面内容，构建 Source 注册表。
    至少保证 _MIN_SOURCES 个有效来源，否则尝试扩大搜索范围。
    """

    PROMPT_DIR = _PROMPT_DIR

    def __init__(self, model: str | None = None):
        super().__init__(model)
        self._search = MultiSourceSearch()

    async def run(self, context: ResearchContext) -> ResearchContext:
        logger.info(f"🔍 ResearcherAgent 开始: {context.title} ({len(context.search_queries)} 查询)")

        # 1. 执行双语搜索，收集候选结果
        all_results: list[SearchResult] = []
        seen_urls: set[str] = set()

        async def _search_fn(q: str, lang: str) -> list[SearchResult]:
            return await self._search.search(q, max_results=5, lang=lang)

        for query in context.search_queries[:6]:  # 最多使用前 6 个查询
            try:
                results = await bilingual_search(query, _search_fn, max_results_per_lang=4)
                for r in results:
                    if r.url not in seen_urls:
                        seen_urls.add(r.url)
                        all_results.append(r)
            except Exception as e:
                logger.warning(f"查询失败，已跳过: {query} — {e}")

        context.raw_search_results = all_results
        logger.info(f"  搜索阶段：收集到 {len(all_results)} 条候选结果")

        # 2. 取 top N URL，抓取页面正文
        top_urls = [r.url for r in sorted(all_results, key=lambda x: x.score, reverse=True)[:8]]
        page_texts = await fetch_pages_batch(top_urls, max_concurrent=3)

        # 3. 构建包含正文的搜索结果摘要，传给 LLM 评估
        enriched_results = []
        for r in all_results[:8]:
            page_text = page_texts.get(r.url)
            enriched_results.append({
                "url": r.url,
                "title": r.title,
                "snippet": r.snippet,
                "page_text_preview": (page_text or "")[:800],  # 正文预览
                "score": r.score,
                "engine": r.source_engine,
            })

        # 4. 调用 LLM 评估并排序来源
        prompt = self._render_prompt(
            topic=context.title,
            search_results_json=enriched_results,
        )

        raw = await self._call_llm_with_retry(prompt, context, max_tokens=3000, temperature=0.2)

        try:
            ranked_sources = json.loads(extract_json_from_response(raw))
        except json.JSONDecodeError as e:
            logger.error(f"ResearcherAgent JSON 解析失败: {e}")
            # 降级：直接使用 top 5 搜索结果
            ranked_sources = [
                {"url": r.url, "title": r.title, "excerpt": r.snippet, "key_points": []}
                for r in all_results[:5]
            ]

        # 5. 注册来源到 context
        for item in ranked_sources:
            url = item.get("url", "")
            if not url:
                continue
            full_text = page_texts.get(url, "")
            snippet = item.get("excerpt", "") or full_text[:500]
            source = context.add_source(url=url, title=item.get("title", url), snippet=snippet)
            logger.debug(f"  来源 [^{source.id}]: {url[:60]}")

        # 6. 检查来源数量，不足时尝试扩大搜索
        if len(context.sources) < _MIN_SOURCES:
            logger.warning(f"来源不足（{len(context.sources)}/{_MIN_SOURCES}），扩大搜索...")
            fallback_results = await self._search.search(
                f"Warcraft III {context.title} tutorial guide", max_results=5
            )
            for r in fallback_results:
                if r.url not in {s.url for s in context.sources}:
                    context.add_source(url=r.url, title=r.title, snippet=r.snippet)
                    if len(context.sources) >= _MIN_SOURCES:
                        break

        if len(context.sources) < _MIN_SOURCES:
            logger.warning(f"⚠️  仍然不足 {_MIN_SOURCES} 个来源（{len(context.sources)}），继续流水线")

        logger.info(f"✅ ResearcherAgent 完成: {len(context.sources)} 个来源已注册")
        return context
