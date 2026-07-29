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

## Known gaps / pre-launch action items

1. **Feed quality:** Shopify products have empty `productType` and (mostly) no tags — thin Merchant Center feed signals. Set product type + Google category + material/size attributes in Shopify admin before scaling Shopping/PMax.
2. **GTIN:** confirm whether SKUs have GTINs; if not, set `identifier_exists` properly so serving isn't suppressed.
3. **Inventory-aware ads:** 3 SKUs sit at ~11–12 units — keep low-stock SKUs out of PMax listing groups or set alerts (see ecommerce playbook, inventory discipline).
4. **Reviews:** early-stage brand — enroll Google Customer Reviews / review syndication ASAP; stars gate Shopping CTR.
5. Ad history, pixel/conversion state, and monthly budget: **unknown — ask before building.**

## Working economics (fill in real numbers before setting tROAS)

- Breakeven ROAS = 1 / contribution margin (after COGS, freight — sinks are heavy, oversized-parcel or LTL shipping costs are material — fulfillment, payment fees). Factory-direct margin is the structural advantage; get the real number from the owner before bidding targets are set.
