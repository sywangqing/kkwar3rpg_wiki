"""pipeline/search/orchestrator.py — 多源搜索编排器（Tavily 主 + DDG 备 + 去重 + 黑名单）"""
from __future__ import annotations

import logging
import urllib.parse
from pathlib import Path

from models import SearchResult

logger = logging.getLogger(__name__)

_BLACKLIST_PATH = Path(__file__).parent / "domain_blocklist.txt"


def _load_blacklist() -> set[str]:
    if not _BLACKLIST_PATH.exists():
        return set()
    return {
        line.strip().lower()
        for line in _BLACKLIST_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    }


def _extract_domain(url: str) -> str:
    try:
        return urllib.parse.urlparse(url).netloc.lower().lstrip("www.")
    except Exception:
        return ""


def _canonicalize_url(url: str) -> str:
    """去掉尾部斜杠和 fragment，用于去重比较"""
    try:
        p = urllib.parse.urlparse(url)
        return urllib.parse.urlunparse((p.scheme, p.netloc, p.path.rstrip("/"), "", "", ""))
    except Exception:
        return url


class MultiSourceSearch:
    """
    多源搜索编排器：
    1. 先用 Tavily，失败则 fallback 到 DuckDuckGo
    2. 对结果去重（按规范化 URL）
    3. 过滤黑名单域名
    """

    def __init__(self, tavily_api_key: str | None = None):
        self._blacklist = _load_blacklist()
        self._tavily_key = tavily_api_key

        # 懒加载搜索提供者
        self._tavily: "TavilyProvider | None" = None  # type: ignore[name-defined]
        self._ddg: "DuckDuckGoProvider | None" = None  # type: ignore[name-defined]

    def _get_tavily(self):
        if self._tavily is None:
            try:
                from search.tavily_provider import TavilyProvider
                self._tavily = TavilyProvider(api_key=self._tavily_key)
            except (ValueError, ImportError) as e:
                logger.warning(f"Tavily 不可用，将仅使用 DuckDuckGo: {e}")
        return self._tavily

    def _get_ddg(self):
        if self._ddg is None:
            from search.duckduckgo_provider import DuckDuckGoProvider
            self._ddg = DuckDuckGoProvider()
        return self._ddg

    async def search(
        self,
        query: str,
        max_results: int = 5,
        lang: str = "en",
    ) -> list[SearchResult]:
        """
        执行搜索，优先 Tavily，失败自动降级到 DuckDuckGo。
        返回去重 + 过滤后的结果，按 score 降序，最多 max_results 条。
        """
        results: list[SearchResult] = []

        # 1. 尝试 Tavily
        tavily = self._get_tavily()
        if tavily:
            try:
                results = await tavily.search(query, max_results=max_results, lang=lang)
                logger.info(f"🔍 Tavily 搜索成功: {len(results)} 条 | {query[:40]}")
            except RuntimeError as e:
                logger.warning(f"⚠️  Tavily 失败，降级到 DuckDuckGo: {e}")
                results = []

        # 2. Fallback 到 DuckDuckGo
        if not results:
            ddg = self._get_ddg()
            results = await ddg.search(query, max_results=max_results, lang=lang)
            logger.info(f"🔍 DuckDuckGo 搜索: {len(results)} 条 | {query[:40]}")

        # 3. 去重 + 黑名单过滤
        seen_urls: set[str] = set()
        filtered: list[SearchResult] = []
        for r in results:
            canonical = _canonicalize_url(r.url)
            domain = _extract_domain(r.url)
            if canonical in seen_urls:
                continue
            if domain in self._blacklist:
                logger.debug(f"🚫 黑名单过滤: {r.url}")
                continue
            seen_urls.add(canonical)
            filtered.append(r)

        return filtered[:max_results]
