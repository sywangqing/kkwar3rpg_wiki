"""pipeline/search/base.py — 搜索提供者抽象接口"""
from __future__ import annotations

from abc import ABC, abstractmethod

from models import SearchResult


class SearchProvider(ABC):
    """所有搜索引擎适配器必须实现的接口"""

    @abstractmethod
    async def search(
        self,
        query: str,
        max_results: int = 5,
        lang: str = "en",
    ) -> list[SearchResult]:
        """执行搜索，返回按相关度降序排列的结果列表"""
        ...

    @property
    @abstractmethod
    def name(self) -> str:
        """适配器名称，用于日志和来源标注"""
        ...
