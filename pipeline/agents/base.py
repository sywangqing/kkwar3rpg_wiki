"""pipeline/agents/base.py — Agent 基类：prompt 加载、<think> 剥离、重试逻辑"""
from __future__ import annotations

import asyncio
import json
import logging
import os
import re
from pathlib import Path
from typing import Any

from tenacity import (
    AsyncRetrying,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from models import ResearchContext

logger = logging.getLogger(__name__)

_THINK_RE = re.compile(r"<think>.*?</think>", re.DOTALL | re.IGNORECASE)
_JSON_FENCE_RE = re.compile(r"```(?:json)?\s*([\s\S]*?)```", re.IGNORECASE)


def strip_think_tags(text: str) -> str:
    """移除 LLM 输出中的 <think>...</think> 推理标签"""
    return _THINK_RE.sub("", text).strip()


def extract_json_from_response(text: str) -> str:
    """从 LLM 响应中提取 JSON（处理 ```json ... ``` 代码块）"""
    text = strip_think_tags(text)
    match = _JSON_FENCE_RE.search(text)
    if match:
        return match.group(1).strip()
    # 尝试直接解析（有些模型直接输出 JSON）
    return text.strip()


class BaseAgent:
    """
    所有 Agent 的公共基类。
    提供：
    - 从 Markdown 文件加载 prompt 模板
    - 调用 LiteLLM (同步包装为异步)
    - 自动剥离 <think> 标签
    - 指数退避重试（最多 3 次）
    """

    # 子类需要设置此变量为对应的 prompt.md 所在目录
    PROMPT_DIR: Path | None = None

    def __init__(self, model: str | None = None):
        self.model = model or os.getenv("AGENT_LLM_MODEL", "minimax/abab7-chat-preview")
        self._prompt_template: str | None = None

    # ------------------------------------------------------------------
    # Prompt 加载
    # ------------------------------------------------------------------

    def _load_prompt(self) -> str:
        if self._prompt_template:
            return self._prompt_template
        if self.PROMPT_DIR is None:
            raise ValueError(f"{self.__class__.__name__} 未设置 PROMPT_DIR")
        prompt_path = Path(self.PROMPT_DIR) / "prompt.md"
        if not prompt_path.exists():
            raise FileNotFoundError(
                f"Prompt 文件不存在: {prompt_path}\n"
                f"请检查 pipeline/agents/{self.__class__.__name__.lower().replace('agent', '')}/ 目录"
            )
        self._prompt_template = prompt_path.read_text(encoding="utf-8")
        return self._prompt_template

    def _render_prompt(self, **kwargs: Any) -> str:
        """将 {variable} 占位符替换为实际值"""
        template = self._load_prompt()
        for key, value in kwargs.items():
            if isinstance(value, (dict, list)):
                value = json.dumps(value, ensure_ascii=False, indent=2)
            template = template.replace(f"{{{key}}}", str(value))
        return template

    # ------------------------------------------------------------------
    # LLM 调用
    # ------------------------------------------------------------------

    async def _call_llm(
        self,
        prompt: str,
        system: str = "You are a helpful assistant for a Warcraft III Wiki.",
        max_tokens: int = 4096,
        temperature: float = 0.3,
    ) -> str:
        """调用 LiteLLM，返回剥离 <think> 后的文本"""
        import litellm  # type: ignore

        def _sync():
            return litellm.completion(
                model=self.model,
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=max_tokens,
                temperature=temperature,
            )

        loop = asyncio.get_event_loop()
        resp = await loop.run_in_executor(None, _sync)
        raw = resp.choices[0].message.content or ""
        return strip_think_tags(raw)

    # ------------------------------------------------------------------
    # 带重试的 LLM 调用
    # ------------------------------------------------------------------

    async def _call_llm_with_retry(
        self,
        prompt: str,
        context: ResearchContext,
        **llm_kwargs: Any,
    ) -> str:
        """
        带指数退避重试的 LLM 调用（最多 3 次，等待 2/4/8 秒）。
        失败会记录到 context.errors 并重新抛出最后一次异常。
        """
        last_error: Exception | None = None
        async for attempt in AsyncRetrying(
            stop=stop_after_attempt(3),
            wait=wait_exponential(multiplier=1, min=2, max=8),
            retry=retry_if_exception_type(Exception),
            reraise=True,
        ):
            with attempt:
                try:
                    return await self._call_llm(prompt, **llm_kwargs)
                except Exception as e:
                    last_error = e
                    logger.warning(
                        f"⚠️  {self.__class__.__name__} LLM 调用失败 "
                        f"(attempt {attempt.retry_state.attempt_number}/3): {e}"
                    )
                    context.log_error(self.__class__.__name__, str(e))
                    raise  # tenacity 需要异常重新抛出

        raise RuntimeError(f"{self.__class__.__name__} 重试耗尽") from last_error
