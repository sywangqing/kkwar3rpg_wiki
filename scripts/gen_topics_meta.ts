/**
 * gen_topics_meta.ts
 * 构建时将 pipeline/cache/topics.json 转换为前端可用的 public/topics-meta.json
 *
 * 使用方式：
 *   npx tsx scripts/gen_topics_meta.ts
 *   # 或在 package.json scripts 中调用：
 *   "prebuild": "tsx scripts/gen_topics_meta.ts"
 */
import fs from 'fs'
import path from 'path'

const ROOT = path.resolve(__dirname, '..')
const TOPICS_PATH = path.join(ROOT, 'pipeline', 'cache', 'topics.json')
const OUT_PATH = path.join(ROOT, 'docs', 'public', 'topics-meta.json')

interface TopicRaw {
  slug: string
  title: string
  category: string
  status: string
  discovered_via?: string
  discovered_at?: string
  source_urls?: string[]
  article_path?: string
  quality_score?: number
}

interface TopicMeta {
  slug: string
  title: string
  link: string
  category: string
  discovered_via: string
  discovered_at: string
  quality_score?: number
}

function slugToLink(slug: string, articlePath?: string): string {
  if (articlePath) {
    // article_path 形如 "docs/scripting/jass-basics.md"
    return '/' + articlePath
      .replace(/^docs\//, '')
      .replace(/\.md$/, '')
  }
  return `/${slug}`
}

function main() {
  if (!fs.existsSync(TOPICS_PATH)) {
    console.error(`❌ 找不到 topics.json: ${TOPICS_PATH}`)
    process.exit(1)
  }

  const raw: TopicRaw[] = JSON.parse(fs.readFileSync(TOPICS_PATH, 'utf-8'))

  const meta: TopicMeta[] = raw
    .filter((t) => t.status === 'completed' || t.article_path)
    .map((t) => ({
      slug: t.slug,
      title: t.title,
      link: slugToLink(t.slug, t.article_path),
      category: t.category ?? '',
      discovered_via: t.discovered_via ?? 'manual',
      discovered_at: t.discovered_at ?? '',
      quality_score: t.quality_score,
    }))

  // 确保 public 目录存在
  const outDir = path.dirname(OUT_PATH)
  fs.mkdirSync(outDir, { recursive: true })

  fs.writeFileSync(OUT_PATH, JSON.stringify(meta, null, 2), 'utf-8')
  console.log(`✅ topics-meta.json 已生成: ${meta.length} 条 → ${OUT_PATH}`)
}

main()
