# NOZLOO Google Ads 重启配置清单（2026-07-29）

目标：以最小结构重建账户，让每一美元花在能验证"ROAS 4 是否可达"的地方。执行完本清单后，账户只有两个启用的系列。

## 第 0 步 — 一次性前置（投放前完成）

- [ ] **转化设置**：Google Ads → 目标 → 转化，确认只有 Shopify「购买」（含动态订单价值）标记为**主要**；加购、进结账、页面浏览全部改为**次要**。出价算法只学主要转化。
- [ ] **排除内部流量**：账户设置 → IP 排除，加入办公室/家庭 IP；今后测试单一律在排除 IP 下操作（7 月已有一笔 $0 测试单被归因给 google）。
- [ ] **Merchant Center 核查**：6 个 SKU 全部"已批准"；每个 SKU 确认 `google_product_category`（feed 应用已设 metafield，核对是否同步）、GTIN 或 `identifier_exists=false`、材质/颜色/尺寸属性；标题格式改为 `NOZLOO 33" Fireclay Farmhouse Sink | Smooth Apron Workstation`（搜索词前置）。
- [ ] **Judge.me → Google 评论同步**：开启 Judge.me 的 Google Shopping 评论 feed（Product Ratings），让星级进入购物广告。当前爆款只有 2 条评论——开启购后自动索评邮件（发货后 14–21 天触发，水槽要留安装时间）。
- [ ] **地理**：定位美国，**排除阿拉斯加、夏威夷**（免运费只覆盖本土 48 州）。

## 第 1 步 — 系列结构（只留两个）

### A. 品牌防守（已有，保持）
- 预算 $5/天，尽可能争取点击，**加 CPC 上限 $1.00**
- 品牌词量现在很小（月 20 次展示）属正常，放着即可

### B. Standard Shopping「6SKU逐个出价」（恢复已暂停的系列，保留历史数据）
- 类型：标准购物（不是 PMax）；优先级：中；**搜索合作伙伴：关**
- 预算：**$50/天**（单一系列集中花，别再分散）
- 出价：**人工 CPC**，按 SKU 分产品组：
  | SKU | 起始 Max CPC |
  |---|---|
  | 33" Smooth（爆款，有星级）| $0.85 |
  | 33" Reversible 入门 $479 | $0.85 |
  | 33" Fluted Workstation | $0.75 |
  | 33" Double Bowl | $0.70 |
  | 30" 两款（库存仅 11-12，卖断即暂停该产品组）| $0.65 |
- 调整规则：某 SKU 展示份额 <30% 且 CTR ≥1.5% → 加价 10-15%；CPC 实际均价 >$1.00 → 降价。每次调整间隔 ≥5 天。
- 设备：先不做调整，两周后看数据（高客单常见移动端 CVR 低，届时考虑移动 -20%）。

### C. 全部暂停/保持暂停
- PMax 纯Feed（$80/天那个）——30 转化/30 天门槛前不开
- 核心精确词搜索、7.28 search——CPC $2.54/$33 在当前转化率下无法打平
- 任何"尽可能提高转化价值"出价的新系列

## 第 2 步 — 否定关键词（加在 Shopping 系列上，词组匹配）

```
售后维修类:  repair, crack repair, refinish, refinishing, touch up, replacement parts, scratch remover
二手低价类:  used, second hand, refurbished, craigslist, ebay, facebook marketplace, cheap, discount code, coupon
信息研究类:  how to install, installation instructions, how to clean, dimensions pdf, cad block, spec sheet
渠道错位类:  wholesale, bulk, distributor, dropship, supplier
材质错位类:  stainless steel, copper, granite composite, cast iron, acrylic, quartz
场景错位类:  bathroom, rv, camper, outdoor, laundry room
竞品品牌类:  bocchi, ruvati, kraus, sinkology, kohler, whitehaus, signature hardware, elkay
```
注意：**不要**否定 porcelain / ceramic（消费者常用它们指 fireclay）；"farmhouse sink for 33 inch cabinet" 这类带尺寸词是最高意图，确保没有被误伤。

## 第 3 步 — 每周例行（周一，30 分钟）

1. 搜索词报告 → 新增否定词（Shopping 的搜索词报告是最有价值的关键词研究，免费）
2. 按 SKU 看：展示/点击/CTR/花费；有展示无点击 = 标题/图片/价格问题，修 feed 不是调出价
3. Merchant Center：拒登、价格竞争力报告
4. 库存核对：30" 两款低库存，<5 件即暂停产品组
5. 记录周 blended MER = Shopify 总收入 ÷ 广告总花费

## 升级门槛（不达标不动）

| 条件 | 动作 |
|---|---|
| 30 天内 ≥30 次真实购买转化 | Shopping 切「尽可能提高转化价值」 |
| ≥50 次转化 | 上 tROAS，从近 30 天实际值起步，每 1–2 周 ±10–15% 向 4.5–5.0 拉 |
| tROAS 稳定 ≥4.5 且量稳 | 恢复 PMax（纯 feed 起步，品牌词排除必开），预算 +20%/次 |
| 某系列花满 $400 仍 ROAS <4 且无加购信号 | 先查 feed/落地页原因，无解则砍 |

## 同步进行的转化率工作（决定成败，广告只是放大器）

- 评论数量：目标 90 天内爆款 ≥20 条（购后邮件 + 向老客户补索评）
- 结账流失（26 进结账只有 3-4 真实付款）：自查结账页的运费时效展示、税费呈现、Shop Pay 分期是否出现"$/mo"字样（钱包已启用，确认 Installments 在结账页可见）
- 商品页：描述文案已含"fits a 36\" cabinet / 免运费 / 终身质保"，但确认这三点在**首屏购买按钮附近**有可视化展示，不是埋在正文里
- 促销纪律：不打折（25% 毛利下 9 折 = 保本 ROAS 6.7），送配件代替降价
