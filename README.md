# 🎮 War3 地图开发者 Wiki

> AI 自动整理的 Warcraft III RPG 地图编辑器知识库，每日持续更新，面向所有开发者免费开放。

**🌐 在线访问：[https://sywangqing.github.io/kkwar3rpg_wiki/](https://sywangqing.github.io/kkwar3rpg_wiki/)**

---

## 📖 直接访问（推荐）

无需任何安装，直接用浏览器打开上面的网址即可。

---

## 💻 本地运行

### 环境要求

- [Node.js](https://nodejs.org/) v18 或以上（下载 LTS 版本）
- [Python](https://www.python.org/) 3.10 或以上（用于 AI 生成管道，可选）

### 步骤

**1. 下载代码**

```bash
git clone https://github.com/sywangqing/kkwar3rpg_wiki.git
cd kkwar3rpg_wiki
```

也可以在 GitHub 页面点击绿色 **Code** → **Download ZIP** 手动下载。

**2. 安装依赖**

```bash
npm install
```

**3. 启动本地预览**

```bash
npm run dev
```

浏览器打开 **http://localhost:5173** 即可预览网站。

**4. 构建静态文件**

```bash
npm run build
```

生成的静态文件在 `docs/.vitepress/dist/` 目录。

---

## 🤖 AI 文章生成管道（可选）

本项目使用 MiniMax 大模型自动生成 War3 知识文章。

### 配置步骤

**1. 创建 `.env` 文件**（复制 `.env.example`）

```bash
cp .env.example .env
```

**2. 填入 API Key**

编辑 `.env` 文件：

```env
OPENAI_API_KEY=你的MiniMax_API_Key
OPENAI_BASE_URL=https://api.minimax.chat/v1
ARTICLE_GEN_MODEL=MiniMax-M2.7-highspeed
```

> 💡 MiniMax API Key 申请地址：[https://platform.minimaxi.com/](https://platform.minimaxi.com/)

**3. 安装 Python 依赖**

```bash
cd pipeline
pip install -r requirements.txt
```

**4. 运行增量更新**（只生成尚未生成的文章）

```bash
python run_incremental.py
```

**5. 运行全量更新**（重新生成所有文章）

```bash
python run_full.py
```

---

## 🔄 自动更新机制

网站通过 GitHub Actions 自动更新，无需手动操作：

| 时间 | 任务 |
|------|------|
| 每天凌晨 2:00 (UTC+8) | 增量生成新文章 |
| 每周日凌晨 3:00 (UTC+8) | 全量重新生成所有文章 |
| 每次 push 到 `main` 分支 | 立即重新部署网站 |

---

## 📁 项目结构

```
kkwar3rpg_wiki/
├── docs/                    # VitePress 文档源文件
│   ├── .vitepress/          # VitePress 配置 & 主题
│   ├── getting-started/     # 快速入门文章
│   ├── triggers/            # 触发器系统文章
│   ├── scripting/           # 脚本编程文章
│   └── ...                  # 其他分类
├── pipeline/                # AI 文章生成管道
│   ├── storm_runner.py      # 核心生成引擎
│   ├── run_incremental.py   # 增量更新脚本
│   ├── topics.json          # 文章主题列表
│   └── requirements.txt     # Python 依赖
├── scripts/                 # 构建辅助脚本
├── .github/workflows/       # GitHub Actions 工作流
└── vercel.json              # Vercel 部署配置（备用）
```

---

## 🤝 贡献指南

欢迎提交 Issue 或 PR！

- **发现错误**：[提交 Issue](https://github.com/sywangqing/kkwar3rpg_wiki/issues/new)
- **补充内容**：直接编辑 `docs/` 下的 Markdown 文件，提交 PR
- **新增主题**：编辑 `pipeline/topics.json`，添加新的文章主题

---

## 📄 许可证

MIT License — 免费使用，欢迎转载，注明出处即可。
