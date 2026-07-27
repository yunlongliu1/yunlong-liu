# .claude — 项目级 Claude Code 配置

## claude-seo（SEO 技能套件）

本目录 vendored 了开源 SEO 技能套件 **claude-seo**，供 NOZLOO / SANIKB 站点的 SEO 工作使用。

| 项目 | 值 |
|---|---|
| 上游仓库 | https://github.com/AgriciDaniel/claude-seo |
| 版本 | v2.2.4 |
| 锁定 commit | `09d37c7b66ed3ca9c6efbdb765a805a6c76a8f01`（2026-07-20） |
| 许可证 | MIT（见 `skills/seo/LICENSE`） |
| 装入日期 | 2026-07-27 |

### 目录结构

```
.claude/
├── skills/           25 个子技能（seo, seo-audit, seo-ecommerce, seo-geo …）
│   └── seo/          主技能 + 支撑资源
│       ├── bin/          claude-seo 启动器
│       ├── scripts/      53 个 Python 工具脚本
│       ├── schema/       Schema.org 校验定义
│       ├── extensions/   8 个可选 MCP 扩展（均需自备账号，默认不启用）
│       ├── hooks/        钩子脚本
│       ├── pdf/          PDF 报告模板
│       └── data/         Google 算法更新时间线
└── agents/           18 个专项子代理
```

### 首次使用前的一次性初始化

Python 脚本类命令（性能抓取、Schema 校验、PDF 报告等）依赖一个隔离的 Python 运行时
和 Chromium。执行：

```
/seo setup
```

诊断用：

```
/seo doctor
```

运行时创建在仓库之外（`~/.local/share` / `%LOCALAPPDATA%`），不会污染 git。
纯分析类命令（`/seo plan`、`/seo content-brief` 等）无需 setup 即可用。

### 常用命令

| 命令 | 用途 |
|---|---|
| `/seo audit <url>` | 全站审计，并行调度子代理，输出 0-100 健康分 + 优先级行动计划 |
| `/seo ecommerce <url>` | 电商 SEO：产品 schema、集合页、marketplace 情报 |
| `/seo page <url>` | 单页深度分析 |
| `/seo technical <url>` | 技术 SEO（9 大类：抓取、索引、Core Web Vitals/INP …） |
| `/seo schema <url>` | Schema.org 检测、校验、生成 |
| `/seo content <url>` | E-E-A-T 与内容质量 |
| `/seo content-brief <topic>` | 生成含目标词、大纲、内链的内容简报 |
| `/seo geo <url>` | AI Overviews / ChatGPT / Perplexity 生成式引擎优化 |
| `/seo cluster <seed-keyword>` | 基于 SERP 的语义聚类与内容架构 |
| `/seo images <url>` | 图片 SEO 与 Google 图片 SERP |
| `/seo sitemap <url>` | 站点地图分析或生成 |
| `/seo drift baseline <url>` | 建立基线，后续用 `compare` 追踪变化 |
| `/seo backlinks <url>` | 外链分析（免费源：Moz、Bing、Common Crawl） |

完整清单见 `skills/seo/SKILL.md`。

### 凭据说明

核心功能**不需要**任何第三方密钥。以下均为可选、需自备账号、默认关闭：
Google Search Console / PageSpeed / CrUX / GA4、DataForSEO、Firecrawl、
Ahrefs、SE Ranking、Profound、Bing Webmaster、Unlighthouse。

**不要把任何 API 密钥提交进本仓库。** 凭据走各工具自己的本地配置或环境变量。

### 升级方式

vendored 副本不会自动更新。升级时重新拉取上游对应版本覆盖 `skills/` 与 `agents/`，
并更新本文件顶部的版本与 commit 记录。

本机（Windows / macOS）如果想要自动更新的安装方式，在交互式 Claude Code 里执行：

```
/plugin marketplace add AgriciDaniel/claude-seo
/plugin install claude-seo@agricidaniel-claude-seo
/seo setup
```
