"""pipeline/search/tavily_provider.py — Tavily 搜索引擎适配器"""
from __future__ import annotations

import asyncio
import logging
import os

from models import SearchResult
from search.base import SearchProvider

logger = logging.getLogger(__name__)


class TavilyProvider(SearchProvider):
    """
    Tavily AI Search 适配器（主力搜索引擎）。
    自动处理 429 / 5xx 错误，超时后抛出以便上层 fallback。
    """

    def __init__(self, api_key: str | None = None):
        self._api_key = api_key or os.getenv("TAVILY_API_KEY", "")
        if not self._api_key:
            raise ValueError("TAVILY_API_KEY 未设置，请在 .env 中配置")

    @property
    def name(self) -> str:
        return "tavily"

    async def search(
        self,
        query: str,
        max_results: int = 5,
        lang: str = "en",
    ) -> list[SearchResult]:
        """
        调用 Tavily Python SDK（同步接口包装为异步）。
        遇到 HTTP 4xx/5xx 会抛出 RuntimeError，由上层 MultiSourceSearch 处理 fallback。
        """
        from tavily import TavilyClient  # type: ignore

        def _sync_search():
            client = TavilyClient(api_key=self._api_key)
            response = client.search(
                query=query,
                max_results=max_results,
                include_raw_content=False,
            )
            return response

        try:
            loop = asyncio.get_event_loop()
            response = await loop.run_in_executor(None, _sync_search)
        except Exception as exc:
            raise RuntimeError(f"Tavily 搜索失败: {exc}") from exc

        results: list[SearchResult] = []
        for item in response.get("results", []):
            results.append(
                SearchResult(
                    title=item.get("title", ""),
                    url=item.get("url", ""),
                    snippet=item.get("content", ""),
                    score=float(item.get("score", 0.0)),
                    source_engine="tavily",
                )
            )

        # 按 score 降序
        results.sort(key=lambda r: r.score, reverse=True)
        logger.debug(f"Tavily 返回 {len(results)} 条结果: {query[:50]}")
        return results
