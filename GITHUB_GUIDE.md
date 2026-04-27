# 🛠️ GitHub 非技术操作指南

> 面向不熟悉编程的运营人员，介绍如何管理 War3 Wiki 的 AI 自动化流程。

---

## 1. 如何添加 Tavily Search API Key

Tavily 提供更高质量的搜索结果（否则回退到 DuckDuckGo）。

### 步骤

1. 前往 [https://tavily.com/](https://tavily.com/) 注册账号
2. 在控制台复制你的 **API Key**（格式：`tvly-xxxxxxxx`）
3. 打开 GitHub 仓库 → **Settings** → **Secrets and variables** → **Actions**
4. 点击 **New repository secret**，填写：
   - Name: `TAVILY_API_KEY`
   - Secret: 你的 API Key
5. 点击 **Add secret** 保存

下次 GitHub Actions 自动运行时，将自动使用 Tavily 搜索。

---

## 2. 如何添加 MiniMax API Key

### 步骤

1. 前往 [https://platform.minimaxi.com/](https://platform.minimaxi.com/) 注册账号
2. 在「API 密钥」页面生成新密钥
3. GitHub 仓库 → **Settings** → **Secrets and variables** → **Actions**
4. 添加：
   - `OPENAI_API_KEY` = 你的 MiniMax API Key

---

## 3. 如何配置 Reddit 发现（可选）

Reddit 发现可以自动扫描 r/WC3 等社区的热帖。

### 创建 Reddit App

1. 前往 [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
2. 点击「create another app」
3. 选择类型：**script**
4. 填写名称（如 `war3-wiki-bot`），redirect uri 填 `http://localhost`
5. 创建后记录：
   - **client_id**（app 名称下方的字符串）
   - **client_secret**（「secret」后面的字符串）

### 添加 Secrets

在 GitHub 仓库 Secrets 中添加：
- `REDDIT_CLIENT_ID` = client_id
- `REDDIT_CLIENT_SECRET` = client_secret
- `REDDIT_USER_AGENT` = `war3-wiki-bot/1.0`

---

## 4. 如何在本地运行主题发现

```bash
# 1. 进入 pipeline 目录
cd pipeline

# 2. 复制并配置环境变量
cp ../.env.example ../.env
# 编辑 .env，填入你的 API keys

# 3. 安装依赖
pip install -r requirements.txt

# 4. 运行发现
python run_discovery.py
```

发现结果会追加到 `pipeline/cache/topics.json`，下次运行 `run_incremental.py` 时自动生成文章。

---

## 5. 如何手动添加新主题

编辑 `pipeline/cache/topics.json`，添加如下格式的条目：

```json
{
  "slug": "my-new-topic",
  "title": "我的新主题标题",
  "category": "JASS 编程",
  "status": "pending",
  "discovered_via": "manual"
}
```

**字段说明：**

| 字段 | 说明 | 必填 |
|------|------|------|
| `slug` | 文章 URL 标识符，英文小写+连字符 | ✅ |
| `title` | 文章标题（中文） | ✅ |
| `category` | 分类（见下方列表） | ✅ |
| `status` | `pending`=待生成，`completed`=已完成 | ✅ |
| `discovered_via` | `manual`=手动添加，或论坛来源 | ✅ |

**可用分类：**
- `JASS 编程`
- `vJASS 编程`
- `Lua 脚本`
- `触发器系统`
- `地形编辑`
- `对象编辑器`
- `工具生态`
- `进阶开发`

---

## 6. 如何手动触发 GitHub Actions

### 触发文章生成

1. 进入 GitHub 仓库 → **Actions** 标签页
2. 在左侧列表找到 **Generate Articles**
3. 点击右侧 **Run workflow** → **Run workflow**
4. 等待约 10-30 分钟（取决于主题数量）

### 触发主题发现

1. Actions → **Discover Topics** → **Run workflow**

### 触发网站部署

每次向 `main` 分支 push 都会自动触发部署。  
也可以在 Actions → **Deploy** → **Run workflow** 手动触发。

---

## 7. 如何查看文章生成报告

每次 GitHub Actions 运行后：

1. Actions 标签页 → 找到最近一次 **Generate Articles** 运行
2. 点击进入，查看 **Job Summary**（页面底部）
3. 报告格式：

```
🌪️ War3 Wiki 自动更新报告
| 处理主题总数 | 10 |
| ✅ 成功生成  | 8  |
| ⏩ 缓存跳过  | 1  |
| ❌ 失败      | 1  |
| ⏱️ 总耗时   | 180.5s (3.0min) |
```

---

## 8. 如何编辑 AI 生成的提示词

提示词存放在 `pipeline/agents/` 各子目录的 `prompt.md` 文件中：

| 文件 | 作用 |
|------|------|
| `agents/planner/prompt.md` | 控制大纲生成和搜索查询 |
| `agents/researcher/prompt.md` | 控制来源筛选和排名 |
| `agents/writer/prompt.md` | 控制文章写作风格和格式 |
| `agents/reviewer/prompt.md` | 控制质量评分标准 |
| `agents/discoverer/prompt.md` | 控制新主题的相关性判断 |

**直接编辑 Markdown 文件即可**，无需修改 Python 代码。  
修改后 commit & push，下次运行时自动生效。

详见 [`pipeline/agents/README.md`](pipeline/agents/README.md)。

---

## 9. 常见问题

### Q: 文章质量分很低（< 0.7）怎么办？

- 检查 `TAVILY_API_KEY` 是否配置（影响搜索质量）
- 在 `pipeline/agents/writer/prompt.md` 中提高写作要求
- 检查 `pipeline/logs/` 中的日志文件，查看具体错误

### Q: 论坛发现没有找到新主题？

- Hive Workshop 每天有新内容，但需要 relevance score ≥ 0.7 才会被接受
- 可以降低 `DISCOVERY_RELEVANCE_THRESHOLD`（默认 0.7）
- 检查 `pipeline/logs/discovery-*.log` 日志

### Q: GitHub Actions 失败了怎么办？

1. 点击失败的 workflow → 展开日志
2. 查找红色 ❌ 的步骤
3. 常见原因：API Key 过期、网络超时、JSON 解析错误
4. 如果看不懂，截图发给技术人员处理
