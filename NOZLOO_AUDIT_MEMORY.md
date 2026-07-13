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

## H2 修订（04 — 关键词视角，用户提示后补强）
根因：H1(coming-soon未清) 与 H2(纹理漂移) 同源 = 上线前模板文案未最终对齐。
纹理漂移 = 关键词互相抢(cannibalization)，非随机：
- 核心词(handle/card)：P1=ribbed, P3=grooved, P5=smooth, P6=fluted, P4=reversible标准, P2=double bowl
- P6 SEO 打 "ribbed" → 抢 P1 的词，自己 "fluted" 在SEO中缺席
- P4 SEO 打 "grooved" → 抢 P3 的词
修复原则（重要）：不是全店统一，而是"每款回归自己核心词 + 停止抢别人的词"，
保留 ribbed/grooved/fluted 的差异化，勿砸关键词策略。
- P6: SEO/Alt "ribbed"→"fluted"（夺回 fluted，不再抢 P1）
- P4: SEO 去 "grooved"（P3的词）；实物纹理待用户确认后定
- P2: 正文 vs 图Alt 统一到实物那一对（ribbed/smooth 或 fluted/smooth）
- P1/P3/P5: 已对齐，不动
待用户确认：P4 实物纹理（grooved+smooth ？其他？）→ 确认后 P4/P6/P2 一次刷全字段

## H2 深层修订（05 — 抓线上渲染页实证，纠正 04 的错误判断）
方法补强：Admin API 的 descriptionHtml 只是开头短介绍；产品页深层内容（"Drag to compare"
对比滑块 + 规格表 + 特性区块）由主题区块渲染，须抓 nozloo.com 线上 HTML 才看得到。
已抓 6 个线上产品页(200 OK)扫描。

店铺自定义的分类学（来自页面原话）：
- grooved = "a single horizontal groove"（横向凹槽）→ 真独立面（仅 P3）
- ribbed = fluted = "vertical ridges/flutes"（竖棱）→ 同一面两名（P6原话:"a ribbed, also called fluted, front"）
- smooth = flat = 光面（滑块标 Flat，正文/规格表标 Smooth）

纠正 04：ribbed 与 fluted 不是不同产品，是同义。→ P1(33"Ribbed) 与 P6(30"Fluted) 很可能同款竖棱面，按尺寸起了两名（命名不一致）。

实锤（页面自相矛盾）：
- P4：正文+规格表="Grooved + Smooth"，但对比滑块(实拍图)="Fluted Side / vertical ridges"。
  grooved≠fluted（店铺自定义）→ 文字/ SEO 的"grooved"是从 P3 模板抄串行；实拍图为准 → P4 实为 fluted/ribbed(竖棱)+光面。
  → 已用图片回答上轮"P4纹理"疑问：P4 = 竖棱(fluted/ribbed)，非 grooved。
- 全站 smooth↔flat 命名漂移：滑块统一叫"Flat"，正文/规格表叫"Smooth"（P1/P2/P3/P4/P6 都有）。
- ribbed↔fluted 标签未统一：P1规格"Ribbed"、P4滑块"Fluted"、P6"Ribbed/Fluted"。

修复原则（修订版）：
1. 同义面统一命名：光面统一"Smooth"（弃"Flat"标签）；竖棱面全店选定一个词(Ribbed 或 Fluted)统一，或像P6显式写"Ribbed/Fluted"。
2. 真独立面保留：grooved(横槽)保持独立，勿并入竖棱。
3. 修 P4 事实错误：正文+规格表+SEO 的"grooved"→改"fluted/ribbed"以匹配实拍图（同时消除对 P3 的抢词）。
4. 每款三处(正文/滑块/规格表)+SEO+Alt+card 对齐到同一命名。
待确认：P4 实拍图是否即最终实物（若是，则文字改 fluted）。

## P4 修复定位（06 — 用户确认 P4=竖向纹路+光面 → 竖向=fluted，"grooved"是错的）
用户确认：P4 一面竖向凹槽/棱纹、一面光滑 → 按店铺分类学 = fluted(竖) + smooth。故 P4 所有 "grooved" 均错。
内容源：不在 descriptionHtml，在主题 MAIN="Updated copy of Horizon"(gid 158269538541)
模板文件：templates/product.nz3320t.json（P4 专属；各产品独立模板）
"grooved" 5 处（偏移量）：720 / 5311 / 8887(spec_row "Reversible (Grooved + Smooth)") / 16503 / 21259
滑块 side_b_name 已=“Fluted Side”, side_b_desc=“Vertical ridges…” → 图正确，仅文字错。
side_a_name=“Flat Side”（光面被标 Flat，属 smooth↔flat 全站漂移，可选统一为 Smooth）。
SEO：seo.description/global.description_tag = “…grooved and smooth fronts…” 待改 fluted。
拟改：模板5处 grooved→fluted；SEO 1处；图片Alt 可选统一。
状态：等用户明确 go（改的是 MAIN 已发布主题，属线上可见改动）。未改。
其他产品模板后缀：P1=nz103w3320 P2=nz103w3320d P3=105w3020 P5=nz3320s P6=nozloo-30
