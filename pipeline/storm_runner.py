"""
storm_runner.py — AI 文章生成引擎

直接调用 MiniMax（LiteLLM）生成高质量 War3 地图编辑器知识文章。
不依赖外部搜索引擎，利用 LLM 内置知识 + 结构化 Prompt 生成专业内容。

架构：
  1. 大纲生成（outline）
  2. 分节撰写（section writer）
  3. 整合打磨（polish）
  4. Frontmatter 注入 + 后处理
"""
import logging
import os
import re
from datetime import datetime, timezone
from pathlib import Path

import yaml
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

# ============================================================
# LiteLLM 调用工具（含 <think> 标签过滤）
# ============================================================

def _call_llm(messages: list, max_tokens: int = 3000) -> str:
    """
    调用 MiniMax（或任意 OpenAI 兼容模型），自动剥离 <think> 推理标签。
    """
    import litellm

    api_key = os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("OPENAI_BASE_URL")
    model_name = os.getenv("ARTICLE_GEN_MODEL", "MiniMax-M2.7-highspeed")

    # litellm 需要 openai/ 前缀以使用自定义 base_url
    if base_url and not model_name.startswith("openai/"):
        model_name = f"openai/{model_name}"

    kwargs = dict(
        model=model_name,
        messages=messages,
        max_tokens=max_tokens,
        api_key=api_key,
    )
    if base_url:
        kwargs["api_base"] = base_url

    response = litellm.completion(**kwargs)
    raw = response.choices[0].message.content or ""

    # 剥离推理模型的 <think>...</think> 思维链
    cleaned = re.sub(r"<think>[\s\S]*?</think>", "", raw, flags=re.IGNORECASE).strip()
    return cleaned


# ============================================================
# 系统提示
# ============================================================

SYSTEM_PROMPT = """你是一位专业的 Warcraft III 地图编辑器 (World Editor) 知识库编辑，
同时也是一位经验丰富的 War3 RPG 地图开发者。

你的任务是为社区 Wiki 撰写高质量的中文技术文档，帮助新入门和进阶的 War3 地图开发者。

写作要求：
- 严格使用简体中文
- 结构清晰，使用标题分层（## 二级，### 三级）
- 包含实际可用的代码示例（jass/lua）
- 解释专业术语，对新手友好
- 引用官方编辑器功能的准确名称
- 避免过于笼统，要有具体操作步骤
"""


# ============================================================
# 文章生成：三阶段管道
# ============================================================

def _generate_outline(topic: dict) -> str:
    """阶段 1：生成文章结构大纲"""
    title = topic["title"]
    tags = ", ".join(topic.get("tags", []))
    search_query = topic.get("search_query", "")

    prompt = f"""请为以下 War3 Wiki 文章生成一个详细的章节大纲：

**文章标题**: {title}
**关键词**: {tags}
**搜索意图**: {search_query}

要求：
- 大纲包含 4~7 个主要章节（## 级别）
- 每个章节下列出 2~4 个子话题
- 第一章必须是"简介/概述"，最后一章是"常见问题/注意事项"
- 中间章节覆盖核心知识点、操作步骤、高级用法

只输出大纲结构，格式示例：
## 1. 简介
- 是什么
- 应用场景

## 2. 基本概念
...
"""
    logger.info(f"  📋 生成大纲: {title}")
    return _call_llm([
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt},
    ], max_tokens=800)


def _write_section(title: str, section_header: str, outline: str, prev_sections: str) -> str:
    """阶段 2：逐节撰写文章内容"""
    context = f"\n\n已写内容摘要：\n{prev_sections[:500]}" if prev_sections else ""
    prompt = f"""正在撰写 War3 Wiki 文章《{title}》。

完整大纲：
{outline}

请详细撰写其中的章节：**{section_header}**{context}

要求：
- 详细、专业、实用
- 包含具体操作步骤或代码示例（如适用）
- 中文撰写，代码注释也用中文
- 字数：300~600 字
- 直接输出该章节内容（从 ## 标题开始）
"""
    return _call_llm([
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt},
    ], max_tokens=1000)


def _polish_article(title: str, raw_article: str) -> str:
    """阶段 3：整合打磨完整文章"""
    prompt = f"""以下是《{title}》的草稿，请进行最终润色：

{raw_article}

润色要求：
1. 确保各章节衔接自然
2. 统一术语（如 World Editor/世界编辑器、Trigger Editor/触发器编辑器）
3. 添加文章开头的摘要段落（2~3 句话概括全文）
4. 检查 Markdown 格式是否正确
5. 不要删减内容，只做优化

直接输出最终文章，从 ## 概述 或第一章标题开始。
"""
    logger.info(f"  ✨ 润色文章")
    return _call_llm([
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt},
    ], max_tokens=6000)


def generate_article(topic: dict, output_dir: Path) -> tuple[str, int]:
    """
    三阶段生成单篇 War3 Wiki 文章。

    Returns:
        (article_content, sources_count)
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    title = topic["title"]

    logger.info(f"🌪️  开始生成文章: {title}")

    # 阶段 1：大纲
    outline = _generate_outline(topic)
    logger.info(f"  ✅ 大纲完成 ({len(outline)} 字符)")

    # 解析大纲中的章节标题
    section_headers = re.findall(r"^##\s+(.+)$", outline, re.MULTILINE)
    if not section_headers:
        # 回退：直接提取数字开头的行
        section_headers = re.findall(r"^\d+[\.、]\s*(.+)$", outline, re.MULTILINE)
    if not section_headers:
        section_headers = ["简介与概述", "核心功能", "使用方法", "注意事项"]

    logger.info(f"  📑 识别到 {len(section_headers)} 个章节: {section_headers}")

    # 阶段 2：逐节撰写
    sections = []
    prev_text = ""
    for i, header in enumerate(section_headers):
        logger.info(f"  ✍️  撰写章节 {i+1}/{len(section_headers)}: {header}")
        content = _write_section(title, header, outline, prev_text)
        sections.append(content)
        prev_text += f"\n{header}: {content[:100]}"

    raw_article = "\n\n".join(sections)

    # 阶段 3：润色
    polished = _polish_article(title, raw_article)

    # 统计参考数（LLM 生成无引用，设为 0）
    sources_count = 0

    return polished, sources_count


# ============================================================
# 文章后处理：Frontmatter 注入
# ============================================================

def strip_think_tags(content: str) -> str:
    """去除 MiniMax 推理模型输出的 <think>...</think> 思维链标签"""
    content = re.sub(r"<think>[\s\S]*?</think>", "", content, flags=re.IGNORECASE)
    return content.strip()


def post_process_article(
    raw_content: str,
    topic: dict,
    sources_count: int = 0,
) -> str:
    """
    为生成的文章注入 YAML frontmatter 元数据。
    """
    raw_content = strip_think_tags(raw_content)

    frontmatter = {
        "title": topic["title"],
        "topic_id": topic["topic_id"],
        "category": topic["category"],
        "category_name": topic.get("category_name", ""),
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "sources_count": sources_count,
        "ai_generated": True,
        "description": f"War3 地图编辑器知识 - {topic['title']}",
    }

    fm_str = "---\n" + yaml.dump(
        frontmatter, allow_unicode=True, default_flow_style=False
    ) + "---\n\n"

    # 去除可能存在的旧 frontmatter
    if raw_content.startswith("---"):
        end = raw_content.find("---", 3)
        if end != -1:
            raw_content = raw_content[end + 3:].lstrip()

    ai_notice = (
        "\n\n---\n\n"
        "> 📝 **本文由 AI 自动生成**，基于 Warcraft III 地图编辑器知识库整理，仅供参考。\n"
        "> 发现错误？欢迎 [提交反馈](https://github.com/your-org/war3-wiki/issues/new)。\n"
    )

    return fm_str + raw_content.strip() + ai_notice


# ============================================================
# 公共入口：单主题完整处理
# ============================================================

def run_topic(topic: dict, docs_root: Path) -> str:
    """
    完整处理单个主题：生成文章 → 后处理 → 写入文件。

    Returns:
        article_path (str): 写入的文件路径
    """
    if topic["output_dir"].startswith("docs/"):
        output_dir = docs_root / Path(topic["output_dir"]).relative_to("docs")
    else:
        output_dir = docs_root / topic["output_dir"]

    raw_content, sources_count = generate_article(topic, output_dir)
    final_content = post_process_article(raw_content, topic, sources_count)

    filename = f"{topic['topic_id']}.md"
    file_path = output_dir / filename
    file_path.write_text(final_content, encoding="utf-8")

    logger.info(f"✅ 文章已写入: {file_path}")
    return str(file_path)