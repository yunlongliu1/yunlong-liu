# Product Marketing Context — NOZLOO (C-end / D2C)

Auto-read by the `ads` skill before campaign work. Scope: consumer (C端) advertising for NOZLOO. The SANIKB B2B factory site (`index.html` in this repo) is a separate business — do not mix B2B OEM messaging into NOZLOO consumer campaigns.

## Brand

- **NOZLOO** — nozloo.com, D2C kitchen & bath brand, launched 2025 (Crunchbase)
- Shopify store confirmed live: name NOZLOO, USD, US-based, "Shopify" plan
- Backed by SANIKB, a Foshan kitchen & bath OEM/ODM manufacturer with its own ceramic plant (since 2000) → the core story: **factory-direct genuine fireclay, no middleman markup**
- Positioning: fireclay sink specialist for modern farmhouse kitchens — genuine 2,200°F (1,200°C) fired clay
- Offer stack (per nozloo.com): direct pricing, **free lower-48 US shipping**, **limited lifetime warranty**
- Market: United States (lower 48 primary)

## Live catalog (Shopify Admin, 2026-07-29)

6 active SKUs, all fireclay farmhouse sinks, single-variant, AOV band **$479–$599**:

| Product | Price | SKU | Stock |
|---|---|---|---|
| 33" Reversible Fluted Apron w/ Workstation Kit | $569 | nz103w3320 | 71 |
| 33" Smooth Apron w/ Workstation Kit — tagged `most-popular` | $519 | NZ3320S | 82 |
| 33" Fireclay Double Bowl w/ Workstation Kit | $599 | NZ103w3320d | 12 |
| 33" Reversible Apron (no workstation) — entry price point | $479 | NZ3320T | 60 |
| 30" Grooved Apron w/ Workstation Kit | $549 | NZ105w3020 | 11 |
| 30" Reversible Apron w/ Workstation Kit | $549 | NZ103W3020 | 12 |

- Hero dimension split: 33" (fits 36" cabinet) vs 30" (fits 33" cabinet) — size queries are a primary keyword axis
- Site also lists broader kitchen/bath range (stainless sinks, vanities, faucets) per web presence; the Shopify catalog above is what's actually sellable today — anchor ads on the 6 sinks
- One-purchase category (a sink is bought once) → exclude past purchasers from prospecting; accessories/workstation add-ons are the only cross-sell

## Audience

- **Primary:** US homeowners mid-kitchen-renovation, modern-farmhouse aesthetic, researching sinks by cabinet size and material; multi-week consideration cycle typical of $500+ fixtures
- **Secondary:** contractors, interior designers, builders buying for projects
- Research behaviors to serve: "will it fit my cabinet," fireclay vs cast iron/granite composite, durability/chip concerns (nozloo.com already publishes guides: "What is a fireclay sink," "Fireclay sink problems" — use as remarketing pool builders)

## Competitive set (assumption — verify in auction insights)

Bocchi, Ruvati, Sinkology, Kraus, Signature Hardware, Kohler (Whitehaven) on brand/product terms; Wayfair/Home Depot/Lowe's marketplace listings in Shopping auctions.

## Keyword seeds (C-end)

- Spec: "33 inch farmhouse sink", "30 inch farmhouse sink", "33 inch fireclay sink", "farmhouse sink for 36 inch cabinet"
- Category: "fireclay farmhouse sink", "fireclay workstation sink", "apron front sink", "white farmhouse sink", "reversible apron sink"
- Comparison: "fireclay vs cast iron sink", "fireclay vs granite composite", "best farmhouse sink"
- Informational (content/remarketing only, negative on Search): "how to clean fireclay sink", "fireclay sink problems", "farmhouse sink installation"

## Account state snapshot (2026-07-01 → 07-28, diagnosed 2026-07-29)

Google Ads: $2,277.53 spend, 152k impressions, 1,807 clicks ($1.26 avg CPC), reported 8 conversions / $569 value. Ten campaigns created/paused/removed within the month; active at snapshot: feed-only PMax $80/day on Max Conv Value + brand defense $5/day (only 20 impressions — brand query volume is near zero for the new brand). A "核心精确词" search campaign spent $723 at $2.54 CPC; a broad MCV search campaign bought a single $33 click.

Shopify same period: 6 orders on the books, but **owner-confirmed only 4 are real — 3 organic (~$1,537) + 1 from ads ($419); the other 2 were internal test orders** (fully discounted, ≈$1,138 of the -$1,238 "discounts" — real-customer discounting is only ~5%, i.e. real buyers pay near list price). Sessions 5,085 → 52 add-to-cart (1.0%) → 26 reached checkout → 5 completed incl. tests → **real store CVR ≈ 0.08%; real checkout completion ≈ 15%** (benchmark 40–60%). True paid ROAS ≈ 0.18 (1,807 ad clicks → 1 order).

Diagnosis, in priority order (tracking is NOT broken — owner confirmed):

1. **Store CVR ≈ 0.08%** vs the ~0.7% needed for ROAS 4 at ~$0.93 Shopping CPC (required CVR = 4 × CPC ÷ AOV). Organic converts at ~0.09% too — the bottleneck is the site, not traffic quality. Worst break: checkout completion ~15%.
2. **Trust, not price, is the barrier** — real customers pay near list, so fix reviews/stars, financing (Shop Pay Installments), shipping-time and warranty display at checkout; do NOT discount (at 25% margin a 10%-off promo pushes breakeven ROAS to ~6.7).
3. **Config hygiene in Google Ads:** verify what the 8 reported "conversions" are — keep Purchase as the only primary (bidding signal), micro-events secondary; exclude internal/test traffic (one $0 test order already got attributed to google).
4. Structure thrash and PMax/MCV launched far below the playbook's data gates (30 conv/30d for MCV, 50 for tROAS).

Agreed sequence: consolidate to brand defense $5/day + manual-CPC Standard Shopping "6SKU逐个出价" revived at $40–60/day (CPC cap ~$1), search paused or capped ≤$1.30, PMax paused until gates → CRO on checkout + reviews as the main battlefield → re-enter smart bidding only at the volume gates. Budget ceiling $50–70/day until real CVR clears ~0.5%.

## Known gaps / pre-launch action items

1. **Feed quality:** Shopify products have empty `productType` and (mostly) no tags — thin Merchant Center feed signals. Set product type + Google category + material/size attributes in Shopify admin before scaling Shopping/PMax.
2. **GTIN:** confirm whether SKUs have GTINs; if not, set `identifier_exists` properly so serving isn't suppressed.
3. **Inventory-aware ads:** 3 SKUs sit at ~11–12 units — keep low-stock SKUs out of PMax listing groups or set alerts (see ecommerce playbook, inventory discipline).
4. **Reviews:** early-stage brand — enroll Google Customer Reviews / review syndication ASAP; stars gate Shopping CTR.
5. Ad history, pixel/conversion state, and monthly budget: **unknown — ask before building.**

## Working economics (owner-confirmed 2026-07-29)

- **Breakeven ROAS = 4.0** (owner-provided) → implied contribution margin ≈ 25% after COGS, freight (heavy/oversized parcels), fulfillment, and payment fees
- **Blended MER floor = 4.0** — weekly blended revenue ÷ total ad spend must clear 4 or the account is losing money regardless of what platform ROAS claims

Breakeven CPA by SKU (price ÷ 4):

| SKU | Price | Max CPA at breakeven |
|---|---|---|
| 33" Reversible no-workstation (entry) | $479 | ~$120 |
| 33" Smooth Apron (most-popular) | $519 | ~$130 |
| 30" models | $549 | ~$137 |
| 33" Fluted Workstation | $569 | ~$142 |
| 33" Double Bowl | $599 | ~$150 |

Operational translation (per the ecommerce playbook):

- **tROAS targets:** breakeven 4.0 is the ceiling, not the goal. Once tROAS-eligible (50+ conv/30d), start at trailing-30d actual and ratchet toward an operating target of **4.5–5.0** so each sale carries real profit; only relax toward 4.0 deliberately, to buy volume when scaling.
- **Kill rule instantiated:** a campaign/SKU below ROAS 4 after ~**$400 spend** (≈3× breakeven CPA) with no assisted/micro-conversion signal and no fixable feed cause → kill.
- **Max CPC sanity check:** max CPC = breakeven CPA × CVR. At ~$130 CPA: 1.0% CVR → $1.30 max CPC; 0.7% → ~$0.90; 1.5% (warm/brand) → ~$1.95. Cold-traffic CVR on a $500 considered purchase typically runs under 1% — expect non-brand CPCs to need tight keyword selection to pencil, and lean on remarketing (much higher CVR) to lift the blend.
- 25% margin means **no discount-led promos without re-doing this math** — a 10% discount drops breakeven ROAS to ~6.7. Prefer value adds (free accessories/workstation kit) over price cuts.
