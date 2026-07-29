# Google Ecommerce Playbook (D2C / B2C)

Operating rules for consumer ecommerce on Google Ads: feed-first foundations, the build order by spend level, Standard Shopping vs Performance Max, ROAS bidding gates, and the adaptations high-AOV considered purchases need. This is the B2C companion to [google-search-playbook.md](google-search-playbook.md) (B2B lead gen) — shared mechanics (match types, negatives mechanics, the weekly search-terms ritual) live there and are not repeated.

## Contents

- When this playbook applies
- Feed first: Merchant Center is the account
- The ecommerce build order
- Standard Shopping vs Performance Max
- PMax guardrails for ecommerce
- The search layer for ecommerce
- Bidding by conversion volume (ROAS ladder)
- High-AOV considered purchases ($300+)
- Remarketing and Demand Gen
- Measurement: MER over platform ROAS
- Promotions and seasonality
- Kill / keep / scale
- Weekly ecommerce scorecard

## When this playbook applies

Physical products, checkout on your own site (Shopify or similar), consumer purchase decision. If the conversion is a lead, demo, or quote request, use [google-search-playbook.md](google-search-playbook.md) instead — the economics and bidding gates there are built for pipeline, not carts.

## Feed first: Merchant Center is the account

In ecommerce, the product feed does the job keywords do in lead gen. Google matches queries to **feed data** in Shopping and PMax — a mediocre feed with great campaigns loses to a great feed with default campaigns. Audit the feed before spending a dollar:

- **Sync natively, never manually.** Shopify → the Google & YouTube channel app; it keeps price/availability live (mismatches cause disapprovals) and enables enhanced conversions and dynamic remarketing with no extra tagging.
- **Titles are the #1 lever.** Formula: `[Brand] [Size/Spec] [Material] [Product Type] [Differentiator]` — front-load what buyers actually type within the first ~70 characters. A buyer searches "33 inch fireclay farmhouse sink"; a title reading "The Heritage Collection — Classic White" is invisible.
- **Fill every attribute, even optional ones:** `product_type` (your own taxonomy), `google_product_category`, GTIN/MPN (or `identifier_exists: false` if genuinely no GTIN — leaving it blank suppresses serving), `material`, `color`, `size`. Empty attributes = weaker matching = paying more for less relevant traffic.
- **Images:** clean main image (white/neutral background, product fills the frame, no watermarks or overlay text — policy violation), lifestyle shots as additional images. PMax reuses these across placements.
- **Reviews:** enroll in Google Customer Reviews / a syndication partner early. Star ratings need review volume; they move Shopping CTR more than any bid change.
- **Description:** first 160–500 characters carry weight; put searched attributes in prose, not marketing copy.

**Common Shopify gap:** stores that never set `productType`, tags, or category on products ship a thin feed. Fix in Shopify admin (it flows through the app) rather than with feed rules, so every channel benefits.

## The ecommerce build order

Spend opens rung by rung, same discipline as the B2B intent ladder — each tier unlocks after the one below proves unit economics:

1. **Brand search** — always on, own budget, capped. Protects the SERP and catches ready buyers.
2. **Shopping on hero SKUs** — your best sellers only, Standard Shopping at low volume (control + query data) or PMax if the account already has conversion history. This is the profit center.
3. **Non-brand search, high-intent category terms** — spec and category queries ("33 inch farmhouse sink," "fireclay workstation sink"). Phrase + Exact first; match-type gates per the B2B playbook.
4. **PMax expansion** — full catalog, asset groups by category, once conversion volume can feed it (gates below).
5. **Remarketing + Demand Gen** — dynamic remarketing on viewers/carts, Demand Gen for prospecting with lifestyle creative.
6. **YouTube / awareness** — last, with spare budget only.

**Don't skip rungs.** PMax-first on a new account with no conversion history is the ecommerce version of broad-match-first: the algorithm learns on junk and platform-reported ROAS hides it by claiming brand and remarketing conversions.

## Standard Shopping vs Performance Max

| | Standard Shopping | Performance Max |
|---|---|---|
| Query visibility | Full search-terms report | Partial (search categories only) |
| Negative keywords | Campaign-level, full control | Account-level list + limited campaign-level |
| Placements | Shopping surfaces only | Search, Shopping, Display, YouTube, Gmail, Discover |
| Creative control | Feed only | Feed + asset groups (or feed-only mode) |
| Data appetite | Works at low volume with manual bids | Needs ~30 conv/30 days to leave learning reliably |
| Brand traffic | Sculptable with negatives | Claims brand unless excluded — inflates reported ROAS |

**Rules:**

- **New account or <30 conversions/30 days → Standard Shopping**, hero SKUs, Manual CPC or Max Clicks, weekly query mining. You're buying data and control cheaply.
- **Graduate to PMax when:** 30+ conv/30 days, feed audit passed, conversion values accurate, brand exclusions configured. Not before all four.
- **Feed-only PMax** (no asset-group creative) is the honest middle step: behaves closest to Shopping while gaining PMax inventory. Add asset groups once you have creative worth showing.
- Keep Standard Shopping and PMax off the same SKUs — PMax takes priority in the auction and starves the Shopping campaign's data.

## PMax guardrails for ecommerce

- **Brand exclusions ON, always.** Brand belongs to the brand campaign. Without exclusions PMax buys your cheapest conversions and reports itself a hero; the incrementality is fiction.
- **Asset groups mirror the catalog** — one per category/theme, each with its own listing group, creative, and audience signal. One mega-group = no signal separation.
- **Listing groups exclude** low-margin SKUs, out-of-stock-prone items, and anything you don't want subsidized clicks on.
- **Account-level negative list applied** — universal junk plus category collisions (see search layer below).
- **New-customer goal:** if repeat purchase matters to your economics, set the new-customer-acquisition goal so PMax doesn't farm your existing buyers.
- **Audience signals are advisory, not targeting** — feed them your buyer data (customer lists, converters, high-intent site segments) but judge PMax on output, not on whether it "used" the signal.
- **Monthly:** check the placement report for Display/YouTube junk share, and compare account performance with PMax's claimed conversions removed — that's the honest incrementality read.

## The search layer for ecommerce

Keyword universe, in priority order:

1. **Spec/size queries** — "33 inch farmhouse sink," "30 inch apron front sink." Highest intent after brand; the buyer has measured their cabinet.
2. **Category + material** — "fireclay farmhouse sink," "fireclay workstation sink." The core.
3. **Comparison** — "fireclay vs cast iron sink," "[competitor] alternative." Run selectively with dedicated comparison/guide pages.
4. **Problem/informational** — "how to clean a fireclay sink." Do NOT pay for these on Search; publish content, capture the audience, remarket.

**Ecommerce negative starters** (on top of the universal junk list in the B2B playbook):

- **Aftermarket intent:** repair, crack, refinish, replacement parts, touch up kit, scratch remover
- **Secondhand:** used, second hand, refurbished, clearance (unless you run one), craigslist, ebay, facebook marketplace
- **DIY/trade info:** how to install, installation instructions, dimensions pdf, CAD, spec sheet (route to content instead)
- **Wrong channel:** wholesale, bulk, distributor, dropship (unless you serve them)
- **"Near me" / showroom terms:** test before negativing — for shipped goods these can convert, but if they don't within 2× breakeven CPA, cut them.
- **Your brand as negative in non-brand campaigns**, as always.

Match-type progression, negative mechanics, and the weekly search-terms ritual: identical to the B2B playbook — follow it verbatim.

## Bidding by conversion volume (ROAS ladder)

First compute **breakeven ROAS = 1 / contribution margin** (margin after COGS, shipping, fulfillment, payment fees — before ad spend). At a 40% contribution margin, breakeven ROAS is 2.5. Every target below derives from this number, not from a benchmark.

| Conversions / 30 days | Bid strategy |
|---|---|
| < 30 | Manual CPC or Max Clicks (Shopping), Max Conversions no-target (Search). You're buying data. |
| 30–50 | Max Conversion Value, **no tROAS yet** — let value optimization learn without a constraint. |
| 50+ | tROAS set at your trailing-30-day **actual** ROAS, then move toward target in ±10–15% steps, waiting 1–2 weeks between moves. |

- Setting tROAS above your actual ROAS on day one doesn't raise efficiency — it collapses volume. Ratchet, don't leap.
- Budget increases +20% at a time, 3–5 days apart (learning resets are real).
- If conversion volume is structurally too low for the ladder (high-AOV, low-frequency), add a **micro-conversion as secondary** (add-to-cart, begin-checkout) for signal — but never as the primary optimization target unless you accept that Google will optimize for carts, not cash.

## High-AOV considered purchases ($300+)

Above ~$300 AOV the buyer researches for days to weeks across multiple sessions. The playbook changes:

- **Expect conversion lag.** Judge campaigns on 30-day windows using "Conversions (by conversion time)" and by-time value columns; a 7-day read on a considered purchase always looks like failure.
- **Give spend room before verdicts.** A campaign or SKU gets spend ≈ 3× breakeven CPA before a kill decision, and assisted/micro-conversion signal counts as a stay of execution.
- **Close the objections in the ad and on the page:** shipping cost (free shipping is a top-3 conversion factor at high AOV), warranty, returns, financing (Shop Pay Installments/Affirm — "from $X/mo" in copy), reviews/UGC, and fit/spec certainty ("fits a 36-inch base cabinet").
- **Landing pages:** spec/size queries → PDP. Category queries → collection page. Comparison/research queries → guide or comparison content (which also builds the remarketing pool).
- **Remarketing windows stretch:** PDP viewers 30 days, guide readers 60–90, cart abandoners hit hard for 14. A "cold" 60-day viewer of a $500 product is still in-market.
- **Offer a micro-commitment** for hesitant researchers — sample, swatch, printable sizing template, "will it fit" checker. It converts a bounce into an identified in-market buyer.

## Remarketing and Demand Gen

Segments, each with different message and cap:

| Segment | Window | Message |
|---|---|---|
| Cart / begin-checkout | 1–14 days | Objection handling: shipping, warranty, financing. Restraint on discounts — train buyers to abandon and you pay forever. |
| PDP viewers | 30 days | Dynamic remarketing (feed-driven), reviews/proof |
| Guide/blog readers | 60–90 days | Education → category ad ("what is X" reader gets "why ours") |
| Past purchasers | Exclude in a one-purchase category; retarget only with accessories/cross-sell |

- Dynamic remarketing requires the feed link + remarketing tag — the Shopify app provides both; verify events fire before trusting the audience.
- **Demand Gen** campaigns are the prospecting layer: lifestyle creative, lookalike-style optimized targeting seeded with converter lists. Hold it to the same breakeven math — it's rung 5, not rung 2.
- Frequency caps: hot segments tolerate high frequency; cold segments 1–2×/week or you're paying for annoyance.

## Measurement: MER over platform ROAS

- **Enhanced conversions for web: ON** (native in the Shopify Google app). Recovers conversions browsers hide; without it your smart bidding trains on undercounted data.
- **One primary conversion source.** Google Ads tag OR GA4-imported purchase as primary — never both (double counting). The other stays secondary for diagnosis.
- **Weekly blended MER** = total revenue ÷ total ad spend, all channels. Platform ROAS self-attributes generously (PMax especially); MER is the number that has to clear blended breakeven.
- **Split new vs returning customer revenue.** A "3.5 ROAS" that is 60% repeat buyers who would have bought anyway is a very different business than 3.5 on new customers.
- **The pause test applies to brand** here too (see B2B playbook): if organic owns your brand SERP, test it and watch total brand revenue, not paid.

## Promotions and seasonality

- Run sales through **Merchant Center promotions** and `sale_price` in the feed — you get strikethrough pricing and sale badges in Shopping, worth more than the discount itself.
- For short, sharp events (BFCM), use smart bidding's **seasonality adjustments** to pre-warn the algorithm; do not slash tROAS mid-event and re-trigger learning.
- Q4: uncap budgets on proven winners only; update shipping-cutoff messaging in ads and on PDPs; stock-outs during peak = paused ad groups, not "out of stock" landing pages.
- Inventory discipline year-round: low-stock SKUs come out of listing groups before they burn spend on unsellable clicks.

## Kill / keep / scale

- **Kill:** below breakeven ROAS after spend ≥ 3× breakeven CPA, with no assisted/micro-conversion signal and no fixable feed or landing-page cause. Check the feed before the funeral — a Shopping SKU with impressions but abysmal CTR is a title/image/price problem, not a demand problem.
- **Keep:** clearing breakeven but below target — work Quality/CTR levers (feed titles, reviews, price competitiveness report in Merchant Center) before adding budget.
- **Scale:** above target ROAS at stable volume → +20% budget steps, or loosen tROAS 10–15% to buy volume. Scale toward your breakeven ceiling, not toward a vanity ROAS (net cash > ROAS percentage — see SKILL.md scaling discipline).

## Weekly ecommerce scorecard

- Spend pacing vs budget; blended MER vs breakeven
- ROAS by campaign, new-customer share of revenue
- Search-terms ritual (per B2B playbook) on Search + Standard Shopping; PMax search categories skim
- Merchant Center: disapprovals, price competitiveness, items with impressions/no clicks
- Inventory check against listing groups (anything low-stock still serving?)
- Top-SKU concentration (one hero SKU >70% of revenue = fragility worth fixing with feed/creative work on the rest)
