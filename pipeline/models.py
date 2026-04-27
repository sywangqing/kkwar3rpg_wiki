"""
models.py — 多 Agent 协作的共享数据模型
所有 Agent 通过 ResearchContext 传递状态，使用 Pydantic v2 保证类型安全。
"""
from __future__ import annotations

import hashlib
from datetime import datetime, timezone
from typing import Any, Optional

from pydantic import BaseModel, Field, model_validator


# ---------------------------------------------------------------------------
# 搜索层模型
# ---------------------------------------------------------------------------

class SearchResult(BaseModel):
    """单条搜索结果（来自 Tavily / DuckDuckGo）"""
    title: str
    url: str
    snippet: str
    score: float = 0.0
    source_engine: str = "unknown"  # "tavily" | "duckduckgo"


# ---------------------------------------------------------------------------
# 来源 / 引用模型
# ---------------------------------------------------------------------------

class Source(BaseModel):
    """文章中引用的一个网络来源"""
    id: int                          # 稳定的引用编号 [^id]
    url: str
    title: str
    snippet: str = ""                # 被 Writer 实际使用的摘录片段
    accessed_at: str = Field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
    used: bool = False               # 是否被 Writer 实际引用

    @property
    def footnote_def(self) -> str:
        """生成 Markdown 脚注定义行"""
        date_str = self.accessed_at[:10]
        return f"[^{self.id}]: [{self.title}]({self.url}) — accessed {date_str}"


# ---------------------------------------------------------------------------
# Planner 输出模型
# ---------------------------------------------------------------------------

class OutlineNode(BaseModel):
    """文章大纲节点（递归）"""
    title: str
    level: int = 2                   # Markdown heading level (2 = ##)
    children: list["OutlineNode"] = Field(default_factory=list)
    search_queries: list[str] = Field(default_factory=list)  # 该节点需要搜索的查询


# ---------------------------------------------------------------------------
# Reviewer 输出模型
# ---------------------------------------------------------------------------

class ReviewFeedback(BaseModel):
    """单条 Reviewer 反馈项"""
    category: str   # missing_citation|factual_error|incomplete_section|poor_structure|redundant_content|tone_mismatch
    excerpt: str
    suggestion: str


class ReviewResult(BaseModel):
    """Reviewer Agent 输出的完整评分结果"""
    accuracy: float = Field(ge=0.0, le=1.0)
    completeness: float = Field(ge=0.0, le=1.0)
    readability: float = Field(ge=0.0, le=1.0)
    citation_coverage: float = Field(ge=0.0, le=1.0)
    overall_score: float = Field(ge=0.0, le=1.0)
    feedback: list[ReviewFeedback] = Field(default_factory=list)
    passed: bool = False

    @model_validator(mode="after")
    def compute_overall(self) -> "ReviewResult":
        # 如果 overall_score 为 0 则重新计算
        if self.overall_score == 0.0:
            self.overall_score = round(
                self.accuracy * 0.35
                + self.completeness * 0.30
                + self.readability * 0.20
                + self.citation_coverage * 0.15,
                2,
            )
        self.passed = self.overall_score >= 0.7
        return self


# ---------------------------------------------------------------------------
# 核心共享上下文
# ---------------------------------------------------------------------------

class ResearchContext(BaseModel):
    """
    多 Agent 共享的研究上下文。
    每个 Agent 读取并修改此对象，最终由 Orchestrator 持久化为 Markdown 文章。
    """
    # 基本标识
    topic_id: str
    title: str
    category: str
    slug: str

    # Planner 输出
    outline: list[OutlineNode] = Field(default_factory=list)
    search_queries: list[str] = Field(default_factory=list)

    # Researcher 输出
    sources: list[Source] = Field(default_factory=list)
    raw_search_results: list[SearchResult] = Field(default_factory=list)

    # Writer 输出
    draft: str = ""
    section_drafts: dict[str, str] = Field(default_factory=dict)  # section title → content

    # Reviewer 输出
    review_result: Optional[ReviewResult] = None
    review_history: list[ReviewResult] = Field(default_factory=list)
    review_loop_count: int = 0

    # 最终文章元数据
    quality_score: float = 0.0
    quality_warning: bool = False
    discovered_via: str = "manual"  # "manual" | "hive" | "reddit" | "9ddota" | "nga"
    source_urls: list[str] = Field(default_factory=list)

    # 运行时错误记录
    errors: list[dict[str, Any]] = Field(default_factory=list)

    # ---------------------------------------------------------------------------
    # 工厂方法
    # ---------------------------------------------------------------------------

    @classmethod
    def from_topic_entry(cls, topic: dict[str, Any]) -> "ResearchContext":
        """
        从 topics.json 中的一个条目构建初始 ResearchContext。

        topics.json 字段映射：
          topic_id  → topic_id
          title     → title
          category  → category
          slug      → slug（若无则由 title 生成）
          source    → discovered_via（默认 "manual"）
          source_urls → source_urls（可选）
        """
        slug = topic.get("slug") or _slugify(topic["title"])
        return cls(
            topic_id=str(topic.get("topic_id", slug)),
            title=topic["title"],
            category=topic.get("category", "general"),
            slug=slug,
            discovered_via=topic.get("source", "manual"),
            source_urls=topic.get("source_urls", []),
        )

    # ---------------------------------------------------------------------------
    # 辅助方法
    # ---------------------------------------------------------------------------

    def add_source(self, url: str, title: str, snippet: str = "") -> Source:
        """注册一个新来源，返回带有稳定 id 的 Source 对象（去重）"""
        # 基于 URL 去重
        existing = next((s for s in self.sources if s.url == url), None)
        if existing:
            return existing
        source = Source(id=len(self.sources) + 1, url=url, title=title, snippet=snippet)
        self.sources.append(source)
        return source

    def get_used_sources(self) -> list[Source]:
        """返回 Writer 实际引用的来源列表"""
        return [s for s in self.sources if s.used]

    def best_draft(self) -> str:
        """返回历次重写中质量最高的草稿"""
        return self.draft

    def log_error(self, agent: str, error: str) -> None:
        self.errors.append({"agent": agent, "error": error, "ts": datetime.now(timezone.utc).isoformat()})


# ---------------------------------------------------------------------------
# 工具函数
# ---------------------------------------------------------------------------

def _slugify(text: str) -> str:
    """将中文/英文标题转换为 URL 安全的 slug（基于 MD5 后缀兜底）"""
    import re
    slug = re.sub(r"[^\w\s-]", "", text.lower())
    slug = re.sub(r"[\s_-]+", "-", slug).strip("-")
    if not slug:
        slug = "topic-" + hashlib.md5(text.encode()).hexdigest()[:8]
    return slug
