"""pipeline/search/extractor.py — 网页正文提取（httpx + BeautifulSoup）"""
from __future__ import annotations

import asyncio
import logging
import re
from typing import Optional

logger = logging.getLogger(__name__)

# 每个页面最大保留的 token 数估算（1 token ≈ 4 chars）
MAX_CHARS = 2000 * 4
FETCH_TIMEOUT = 10  # 秒

# 常见需要剥离的噪声标签
_NOISE_TAGS = [
    "nav", "header", "footer", "aside", "script", "style",
    "noscript", "iframe", "form", "button", "input", "select",
    "ads", "advertisement", "[document]",
]


async def fetch_page_text(url: str, timeout: int = FETCH_TIMEOUT) -> Optional[str]:
    """
    异步抓取网页，提取正文文本，截断至 MAX_CHARS 字符。
    若抓取失败（404、超时等），返回 None 并记录警告日志。
    """
    import httpx
    from bs4 import BeautifulSoup

    def _sync_fetch():
        with httpx.Client(timeout=timeout, follow_redirects=True, headers={
            "User-Agent": "War3WikiBot/1.0 (+https://github.com/sywangqing/kkwar3rpg_wiki)"
        }) as client:
            resp = client.get(url)
            resp.raise_for_status()
            return resp.text

    try:
        loop = asyncio.get_event_loop()
        html = await loop.run_in_executor(None, _sync_fetch)
    except Exception as exc:
        logger.warning(f"⚠️  抓取失败，已忽略: {url} — {exc}")
        return None

    # BeautifulSoup 解析
    try:
        soup = BeautifulSoup(html, "html.parser")
    except Exception as exc:
        logger.warning(f"⚠️  HTML 解析失败: {url} — {exc}")
        return None

    # 移除噪声标签
    for tag in soup(_NOISE_TAGS):
        tag.decompose()

    # 优先提取 <main>/<article>/<div class="content"> 等语义区域
    main_content = (
        soup.find("main")
        or soup.find("article")
        or soup.find("div", class_=re.compile(r"content|post|entry|article", re.I))
        or soup.body
        or soup
    )

    text = main_content.get_text(separator="\n", strip=True) if main_content else ""

    # 合并多余空行
    text = re.sub(r"\n{3,}", "\n\n", text)

    # 截断
    if len(text) > MAX_CHARS:
        text = text[:MAX_CHARS] + "\n\n[... 内容已截断 ...]"

    return text.strip() or None


async def fetch_pages_batch(
    urls: list[str],
    max_concurrent: int = 3,
    timeout: int = FETCH_TIMEOUT,
) -> dict[str, Optional[str]]:
    """
    并发抓取多个 URL，返回 {url: text_or_None} 字典。
    限制并发数防止被反爬。
    """
    sem = asyncio.Semaphore(max_concurrent)

    async def _limited(url: str):
        async with sem:
            return url, await fetch_page_text(url, timeout=timeout)

    tasks = [_limited(u) for u in urls]
    results = await asyncio.gather(*tasks, return_exceptions=False)
    return dict(results)
