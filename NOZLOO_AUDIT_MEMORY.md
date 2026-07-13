# NOZLOO 后台审计 — 记忆文件 (MEMORY)

> 规则：每次执行动作 / 发现问题 / 做改动，都追加到本文件；每次回复都引用本文件。
> 本文件是本次审计的唯一事实来源 (single source of truth)。

## 连接信息
- 店铺 handle: `nozloo`  (admin.shopify.com/store/nozloo)
- **API 域名 (铁律)**: `r8hi1q-rx.myshopify.com`  （禁止用 nozloo.myshopify.com）
- 前台: nozloo.com | 币种 USD | 时区 America/Los_Angeles
- API version: 2024-10 | Endpoint: POST /admin/api/2024-10/graphql.json
- Header: `X-Shopify-Access-Token: shpat_***`（真实值仅存运行环境，不落库到报告）
- 访问方式: 直连 Admin GraphQL API（curl 经代理），helper: scratchpad/gql.sh

## 任务
- 全站扫描，找出「描述不同步」+「产品信息不一致」问题。
- 方式：多角度找茬 → 对抗验证（疑罪从无，扛不住反驳的丢弃）。
- 处置：**只出报告，等用户确认后再改**（用户已选）。单一语言，不查翻译。

## 进度日志
| 时间(会话内序号) | 动作 | 结果 |
|---|---|---|
| 01 | 测通 API | shop=NOZLOO, products=6, ✅ |
| 02 | 建记忆文件 | 本文件 |

## 已确认问题清单
（待扫描后填充）

## 变更记录（改动时才写）
（暂无改动 — 仅扫描阶段）

## 已确认问题清单（03 全站扫描完成，对抗验证后）
- H1 全站 coming-soon/"Ships soon" 与 在售有货可下单 矛盾（6/6产品；P1还多打 most-popular）
- H2 翻转围裙纹理术语同产品内自相矛盾（P4/P6/P2；ribbed/grooved/fluted/smooth/flat 混用）
- M1 集合"30 Inch"SEO写"ribbed and grooved"，实为 grooved(P3)+fluted(P6)，无ribbed
- M2 产品页保修名 "Lifetime Limited Warranty"(P1/P4/P6) vs 官方"Limited Lifetime Warranty"
- M3 文章 fireclay-vs-porcelain：称"$479 for 30-inch"，实为33"款；最便宜30"是$549
- L1 集合"Workstation"SEO拼写错 "hop"→"Shop"
- L2 installation 字段 "Apron Front"(P4) vs "Apron-front"(其余)
- L3 P4 标题花引号 33” vs 直引号；SEO标题拼 "Inch"
- L4 保修仅 P1/P4/P6 正文提及
- L5 google_product_category 仅 P5 有
- L6 P3 主图含 colander tray，配件清单未列
- V1 P5 color-pattern 多一个引用(疑误加颜色) — 需 read_metaobjects
- V2 P2 sink-type 与其余不同 — 需确认
- V3 4个落地页 body 为空，内容在主题；需 read_themes

## 变更记录
（暂无 — 用户选择"仅报告，等确认后再改"）
