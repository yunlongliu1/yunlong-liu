# NOZLOO 全站一致性审计报告
店铺: NOZLOO (nozloo.com) · API域: r8hi1q-rx.myshopify.com · API 2024-10
范围: 6 个产品 · 4 个集合 · 15 个页面 · 34 篇博客文章
方式: 直连 Admin GraphQL API 拉取全量数据 → 多角度找茬 → 逐条对抗验证(疑罪从无)
处置: **仅报告,未做任何改动**(等确认)

## 产品对照表
| 代号 | 标题 | handle | SKU | 价 | 库存 | tags |
|---|---|---|---|---|---|---|
| P1 | 33" Reversible **Ribbed** Apron + Workstation | 33-inch-ribbed-fireclay-farmhouse-workstation-sink | nz103w3320 | 569 | 72 | coming-soon, most-popular |
| P2 | 33" **Double Bowl** + Workstation | 33-inch-fireclay-double-bowl-farmhouse-sink | NZ103w3320d | 599 | 12 | coming-soon |
| P3 | 30" **Grooved** Apron + Workstation | 30-inch-grooved-fireclay-farmhouse-sink | NZ105w3020 | 549 | 12 | coming-soon |
| P4 | 33" **Reversible** Apron (无 Workstation) | 33-inch-reversible-apron-fireclay-farmhouse-sink | NZ3320T | 479 | 60 | coming-soon |
| P5 | 33" **Smooth** Apron + Workstation | 33-inch-smooth-apron-fireclay-farmhouse-sink | NZ3320S | 519 | 84 | coming-soon |
| P6 | 30" **Reversible** Apron + Workstation | 30-inch-reversible-apron-fireclay-farmhouse-sink | NZ103W3020 | 549 | 12 | coming-soon |

---

## 🔴 高优先级

### H1. 全站"即将上市 / Ships soon"状态 vs 实际"在售·有货·可下单"
- 6/6 产品都带 `coming-soon` 标签;但全部 status=ACTIVE、有货(12–84 件)、availableForSale=true、可直接购买,且 P1 已有 3 条评价。
- 34 篇博客里嵌入的产品卡片仍显示 **"Ships soon"** 徽标(如 "Ships soon FITS 36-INCH CABINETS NOZLOO 33″…")。
- P1 同时打了 `coming-soon` 和 `most-popular` —— "即将上市"与"最热销"逻辑互斥。
- **影响**:主题可能渲染"即将上市"徽标 / 削弱购买按钮;与真实可售状态矛盾,损害转化与信任。
- **建议**:移除全部 `coming-soon` 标签;清理博客产品卡里的 "Ships soon" 文案;确认 P1 是否保留 `most-popular`。

### H2. "可翻转围裙"纹理术语在同一产品内自相矛盾(核心"描述不同步")
店铺把 **Ribbed(P1)/Grooved(P3)/Fluted(P6)** 当作**不同的产品/SKU** 来卖,但对同一款翻转围裙,标题·正文·SEO·图片Alt·卡片字段用词彼此打架:

- **P4(33" Reversible 标准款)** 最严重:SEO 说 "**grooved** and smooth fronts";而图片 Alt 分别叫它 grooved / **ribbed**(×2)/ **fluted**(×2)/ flat / smooth —— 同一页面对同一围裙出现 4 种纹理名。
- **P6(30" Reversible)** 三重矛盾:标题·正文·card 字段=**Fluted**;SEO meta 描述=**"smooth or ribbed"**;图片 Alt=ribbed+smooth+**fluted**+flat。Google 搜到 "ribbed",落地页却叫 "Fluted"。
- **P2(双盆)**:正文="**ribbed** apron … or a **smooth** apron";但图片 Alt#5="reversible apron front with **flat and fluted** finishes"。
- 对照:P1 全程 "ribbed"、P3 全程 "grooved"、P5 全程 "smooth/flat" —— 这三款内部是一致的,说明问题就出在三款"翻转"产品的文案没对齐。
- **建议**:每款先锁定"纹理侧"的唯一称呼(如 P6=Fluted、P4=按实物定 Grooved 或 Ribbed),再统一刷到标题/正文/SEO/图片Alt/card_* 全字段。

---

## 🟠 中优先级

### M1. 集合 "30 Inch Fireclay Farmhouse Sinks" 描述与实际成员不符
- SEO 描述:"Compare **ribbed and grooved** apron-front workstation sinks…"
- 实际两款成员:Grooved(P3)+ Fluted/Reversible(P6)。**没有 ribbed 款**。
- **建议**:改为 "grooved and fluted"(或 "grooved and reversible")。

### M2. 保修名称词序颠倒:产品页 vs 官方保修页
- 官方《Warranty》页 + 全部博客统一用 "**Limited Lifetime Warranty**"。
- 但 P1 / P4 / P6 产品正文写成 "**Lifetime Limited Warranty**"(词序相反)。
- **建议**:产品页统一改为官方名 "Limited Lifetime Warranty"。

### M3. 博客价格/尺寸口径错误
- 文章 `fireclay-vs-porcelain-sink`:"Nozloo's fireclay lineup **starts at $479 for 30-inch and 33-inch** models"。
- 实际:$479 是 **33"** 标准款(P4);最便宜的 **30"** 是 **$549**(P3/P6)。不存在 $479 的 30" 款。
- **建议**:改为 "starts at $479 for 33-inch, from $549 for 30-inch" 之类的准确表述。

---

## 🟡 低优先级 / 数据卫生

- **L1**. 集合 "Fireclay Workstation Sinks" SEO 描述拼写错误:"**hop** a fireclay workstation sink"(应为 "Shop")。
- **L2**. 规格字段 `custom.installation` 格式不一:P4="Apron Front",其余="Apron-front"。
- **L3**. 标题标点不一:P4 用花引号 `33”`,其余用直引号 `33"`;P4/P6 的 SEO 标题把尺寸拼成 "33 Inch / 30 Inch" 而产品标题用符号。
- **L4**. 描述完整度不一:保修只在 P1/P4/P6 正文出现,P2/P3/P5 正文未提。
- **L5**. `mm-google-shopping.google_product_category`(=2757)仅 P5 设置,其余 5 款缺失 → Google/Feed 结构化数据不齐。
- **L6**. 图文疑似不符:P3 主图 Alt 出现 "black colander tray",但 4 件套配件清单/正文未列该配件 —— 需确认是否随附,或从图/文中去除。

---

## 🔍 需人工核实(当前 token 权限或字段限制,无法程序化确认)

- **V1**. P5 的 `shopify.color-pattern` 含**两个** metaobject 引用(比其余多一个 `252206940397`),但 P5 只描述白色 → 疑似误加了一个颜色。需 `read_metaobjects` 权限确认。
- **V2**. P2 的 `shopify.sink-type`(`246872375533`)与其余 5 款(`238231322861`)不同 → 可能因"双盆"而正常,也可能标错。需确认。
- **V3**. 页面 `first-release` / `why-fireclay` / `farmhouse-sink-size-calculator` / `farmhouse-sink-accessories` 的 `body` 为空,内容存于**主题模板/区块**;需 `read_themes` 拉取主题资源,才能核对这些落地页内嵌的规格文案是否与产品同步。

---

## 全站一致的项(已核查,无问题)
- 烧制温度:全站统一 2,200°F / 1,200°C ✅
- 橱柜适配:30"→33" 橱柜、33"→36" 橱柜,全站一致 ✅
- 配件材质/数量:sapele 木砧板 + 4 件套工作站配件,产品与博客一致 ✅
- 产品卡价格($479/$519/$549/$569/$599)与实际 variant 价一致 ✅
- 集合成员计数(6 / 4 / 2 / 5)与描述文案一致 ✅
