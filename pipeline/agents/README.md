# Agent Prompt 编辑指南

本目录包含 War3 Wiki 多 Agent 系统的所有 Prompt 模板文件。  
**你可以直接编辑 `.md` 文件来调整 AI 的行为，无需修改任何 Python 代码。**

---

## 目录结构

```
pipeline/agents/
├── planner/
│   ├── prompt.md       ← 大纲规划提示词
│   └── agent.py        ← Planner Agent 实现（一般不需要修改）
├── researcher/
│   ├── prompt.md       ← 来源评估提示词
│   └── agent.py
├── writer/
│   ├── prompt.md       ← 文章撰写提示词
│   └── agent.py
├── reviewer/
│   ├── prompt.md       ← 质量审核提示词
│   └── agent.py
├── discoverer/
│   ├── prompt.md       ← 话题发现提示词
│   └── agent.py
├── base.py             ← 公共基类
└── README.md           ← 本文件
```

---

## 如何修改 Prompt

### 1. 找到对应文件
- 想改文章质量？→ 编辑 `writer/prompt.md`
- 想加严质量审核？→ 编辑 `reviewer/prompt.md`
- 想改大纲结构？→ 编辑 `planner/prompt.md`
- 想调整话题过滤标准？→ 编辑 `discoverer/prompt.md`

### 2. 了解变量占位符
每个 prompt.md 中用 `{变量名}` 表示运行时注入的动态内容，例如：
- `{topic}` — 文章主题标题
- `{source_registry_json}` — 来源注册表 JSON
- `{article_markdown}` — 已生成的文章内容

**不要删除这些占位符**，否则 Agent 将无法正常工作。

### 3. 修改示例：让文章更长
打开 `writer/prompt.md`，找到：
```
- Aim for 200–400 Chinese characters per top-level section.
```
改为：
```
- Aim for 400–800 Chinese characters per top-level section.
```
保存后，下次生成的文章每节会更详细。

### 4. 修改示例：降低质量审核标准
打开 `reviewer/prompt.md`，找到质量分权重说明，可以调整：
- 提高 `readability` 权重 → 更注重可读性
- 降低 `citation_coverage` 权重 → 对引用要求更宽松

---

## 变量速查表

| Prompt 文件 | 可用变量 |
|---|---|
| `planner/prompt.md` | `{topic}` `{category}` `{initial_context}` |
| `researcher/prompt.md` | `{topic}` `{search_results_json}` |
| `writer/prompt.md` | `{topic}` `{section_title}` `{section_outline}` `{source_registry_json}` `{reviewer_feedback}` |
| `reviewer/prompt.md` | `{article_markdown}` `{source_registry_json}` |
| `discoverer/prompt.md` | `{existing_topics_sample}` `{candidates_json}` |

---

## 常见问题

**Q: 修改了 prompt 但没有生效？**  
A: Prompt 在每次 Agent 运行时重新读取，无需重启服务。但如果当前有文章正在生成，需要等本次完成后才能看到变化。

**Q: 能否给某类文章使用不同的 Prompt？**  
A: 目前所有文章共用同一套 Prompt。如需按分类定制，需要修改 `agent.py` 中的 `_render_prompt()` 调用，按 `context.category` 加载不同的模板文件。

**Q: 如何测试我的修改？**  
A: 在 `pipeline/` 目录下运行：
```bash
python -c "
import asyncio, sys
sys.path.insert(0, '.')
from agent_orchestrator import Orchestrator
from pathlib import Path

async def test():
    orc = Orchestrator(docs_root=Path('../docs'))
    result = await orc.generate({
        'topic_id': 'test', 'title': 'JASS 触发器入门',
        'category': 'scripting', 'slug': 'jass-trigger-intro', 'status': 'pending'
    })
    print('生成完成:', result)

asyncio.run(test())
"
```
