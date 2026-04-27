"""pipeline/search/duckduckgo_provider.py — DuckDuckGo 搜索引擎适配器（备用）"""
from __future__ import annotations

import asyncio
import logging

from models import SearchResult
from search.base import SearchProvider

logger = logging.getLogger(__name__)


class DuckDuckGoProvider(SearchProvider):
    """
    DuckDuckGo 搜索适配器（免费备用）。
    使用 duckduckgo-search 库的文本搜索接口，规避原 STORM 库中
    对 .message 属性的错误访问。
    """

    @property
    def name(self) -> str:
        return "duckduckgo"

    async def search(
        self,
        query: str,
        max_results: int = 5,
        lang: str = "en",
    ) -> list[SearchResult]:
        """
        调用 DDGS().text()（同步包装为异步），安全处理所有异常。
        region 参数：en-us（英文）/ zh-cn（中文）
        """
        try:
            from ddgs import DDGS  # type: ignore  # 新包名
        except ImportError:
            from duckduckgo_search import DDGS  # type: ignore  # 旧包名兼容

        region = "zh-cn" if lang.startswith("zh") else "en-us"

        def _sync_search():
            results_raw = []
            try:
                with DDGS() as ddgs:
                    for r in ddgs.text(query, region=region, max_results=max_results):
                        results_raw.append(r)
            except Exception as exc:
                logger.warning(f"DuckDuckGo 搜索异常（已忽略）: {exc}")
            return results_raw

        loop = asyncio.get_event_loop()
        raw_list = await loop.run_in_executor(None, _sync_search)

        results: list[SearchResult] = []
        for i, item in enumerate(raw_list):
            results.append(
                SearchResult(
                    title=item.get("title", ""),
                    url=item.get("href", ""),
                    snippet=item.get("body", ""),
                    score=1.0 - i * 0.05,   # DDG 无原生 score，用排名估算
                    source_engine="duckduckgo",
                )
            )

        logger.debug(f"DuckDuckGo 返回 {len(results)} 条结果: {query[:50]}")
        return results
