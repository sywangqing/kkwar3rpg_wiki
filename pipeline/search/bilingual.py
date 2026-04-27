"""pipeline/search/bilingual.py — 中英文双语查询扩展 + 合并去重"""
from __future__ import annotations

import asyncio
import logging
import os

from models import SearchResult

logger = logging.getLogger(__name__)


async def translate_query(query: str, target_lang: str) -> str:
    """
    使用 LLM 将搜索词翻译成目标语言（en/zh）。
    若翻译失败则返回原始 query。
    """
    import litellm  # type: ignore

    model = os.getenv("AGENT_LLM_MODEL", "minimax/abab7-chat-preview")
    prompt = (
        f"Translate the following search query to {'Chinese (Simplified)' if target_lang == 'zh' else 'English'}. "
        f"Return ONLY the translated query, no explanation.\n\nQuery: {query}"
    )

    try:
        resp = await asyncio.get_event_loop().run_in_executor(
            None,
            lambda: litellm.completion(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=100,
                temperature=0.1,
            ),
        )
        translated = resp.choices[0].message.content.strip()
        # 去掉可能存在的 <think> 标签
        import re
        translated = re.sub(r"<think>.*?</think>", "", translated, flags=re.DOTALL).strip()
        return translated or query
    except Exception as exc:
        logger.warning(f"翻译失败，使用原词: {exc}")
        return query


async def bilingual_search(
    query: str,
    search_fn,  # async callable(query, lang) -> list[SearchResult]
    max_results_per_lang: int = 5,
) -> list[SearchResult]:
    """
    对 query 发起中英文双语搜索，合并结果并去重（基于 URL）。

    Args:
        query: 原始查询词（中文或英文均可）
        search_fn: async def search(q: str, lang: str) -> list[SearchResult]
        max_results_per_lang: 每种语言最多返回多少条

    Returns:
        合并去重后的 SearchResult 列表，按 score 降序
    """
    import re

    # 判断原始语言
    has_chinese = bool(re.search(r"[\u4e00-\u9fff]", query))
    if has_chinese:
        zh_query = query
        en_query = await translate_query(query, target_lang="en")
    else:
        en_query = query
        zh_query = await translate_query(query, target_lang="zh")

    logger.info(f"🌐 双语查询: EN='{en_query}' | ZH='{zh_query}'")

    # 并发执行两个查询
    en_task = search_fn(en_query, "en")
    zh_task = search_fn(zh_query, "zh")
    en_results, zh_results = await asyncio.gather(en_task, zh_task, return_exceptions=False)

    # 合并 + URL 去重（保留 score 较高的那条）
    seen: dict[str, SearchResult] = {}
    for r in (*en_results, *zh_results):
        key = r.url.rstrip("/")
        if key not in seen or r.score > seen[key].score:
            seen[key] = r

    merged = sorted(seen.values(), key=lambda r: r.score, reverse=True)
    return merged[: max_results_per_lang * 2]  # 最多返回两倍单语数量
