#!/usr/bin/env python3
"""Length + consistency analysis of NOZLOO SEO titles/descriptions (Shopify Admin API data)."""

# (kind, handle, title_tag, meta_description)
DATA = [
 ("product","30-inch-grooved-fireclay-farmhouse-sink",'30" Grooved Apron Fireclay Farmhouse Sink with Workstation Kit | NOZLOO',"30 inch grooved fireclay farmhouse sink in genuine fireclay. Grooved apron front, non-porous glaze, free shipping, Limited Lifetime Warranty."),
 ("product","30-inch-reversible-apron-fireclay-farmhouse-sink",'30" Reversible Apron Fireclay Farmhouse Sink with Workstation Kit | NOZLOO','Shop a 30 inch reversible apron fireclay farmhouse sink with smooth or fluted front, workstation accessories, 33" cabinet fit, and a lifetime warranty.'),
 ("product","33-inch-fireclay-double-bowl-farmhouse-sink",'33" Fireclay Double Bowl Farmhouse Sink with Workstation Kit | NOZLOO','Upgrade your kitchen with a NOZLOO 33" fireclay double bowl farmhouse sink featuring a workstation kit, 50/50 bowls, and reversible apron front.'),
 ("product","33-inch-reversible-apron-fireclay-farmhouse-sink",'33" Glossy White Glaze Reversible Apron Fireclay Farmhouse Sink | NOZLOO',"Shop a 33-inch reversible apron fireclay farmhouse sink with fluted and smooth fronts, glossy white glaze, bottom grid, and drain. Fits 36-inch cabinets."),
 ("product","33-inch-ribbed-fireclay-farmhouse-workstation-sink",'33" Fluted Apron Fireclay Farmhouse Sink with Workstation Kit | NOZLOO',"Shop a 33 inch fluted fireclay farmhouse workstation sink with a reversible apron, built-in ledge, cutting board, drying rack, bottom grid, and drain."),
 ("product","33-inch-smooth-apron-fireclay-farmhouse-sink",'33" Smooth Apron Fireclay Farmhouse Sink with Workstation Kit | NOZLOO','Shop the NOZLOO 33" smooth apron fireclay farmhouse sink with workstation kit, single bowl design, white glazed finish, center drain, and 36" cabinet fit.'),

 ("collection","fireclay-farmhouse-sink",'Fireclay Farmhouse Sinks — Apron-Front, 30" & 33" | NOZLOO','Genuine fireclay farmhouse sinks in 30" and 33" — single or double bowl, workstation or standard models. Free U.S. shipping and a limited lifetime warranty.'),
 ("collection","33-inch-fireclay-farmhouse-sink",'33" Fireclay Farmhouse Sinks — Single and Double | NOZLOO','Four 33-inch fireclay farmhouse sinks for a 36" base cabinet — a $479 standard, a 50/50 double, and fluted or smooth workstation models. Free U.S. shipping.'),
 ("collection","30-inch-fireclay-farmhouse-sink",'30" Fireclay Farmhouse Sink — Fits a 33" Cabinet | NOZLOO','Two 30-inch fireclay farmhouse workstation sinks for a 33" base cabinet — fluted or grooved reversible apron, full prep kit included. Free U.S. shipping.'),
 ("collection","fireclay-workstation-sinks","Fireclay Workstation Sinks — Ledge & 4-Piece Kit | NOZLOO",'Fireclay workstation sinks with a built-in ledge and full 4-piece prep kit — cutting board, drying rack, grid, and drain, in 30" and 33". Free U.S. shipping.'),

 ("article","why-fireclay-is-known-for-durability-in-kitchen-design","Why Is Fireclay So Durable? Vitrification Explained | NOZLOO","Fireclay is durable because it's vitrified at 2,200°F into a dense, low-porosity body that resists chips, stains, and heat. Here's the science."),
 ("article","the-science-behind-fireclay-heat-pressure-and-strength","The Science Behind Fireclay: Heat & Strength | NOZLOO","Learn the science behind fireclay, including heat resistance, kiln firing, and material strength. Discover what makes fireclay durable in daily use."),
 ("article","fireclay-vs-ceramic-sink-differences","Fireclay vs Ceramic Sink: Key Differences | NOZLOO","Fireclay and ceramic sinks look alike but age very differently. We break down how they compare on durability, stains, heat, cost, and daily use."),
 ("article","fireclay-vs-stainless-steel-sink","Fireclay vs Stainless Steel Sink: An Honest Comparison | NOZLOO","Fireclay vs stainless steel sink — weighed fairly on durability, noise, price, install and resale, with independent sources, to help you choose."),
 ("article","what-is-a-fireclay-sink","What Is a Fireclay Sink? Material, Durability & Use","Learn what a fireclay sink is, what it is made of, how durable it is, and what to know before choosing one for a farmhouse-style kitchen."),
 ("article","fireclay-vs-cast-iron-vs-porcelain-sink","Fireclay vs Cast Iron vs Porcelain Sink | NOZLOO","Fireclay vs cast iron vs porcelain — we compare durability, chipping, stain resistance, and maintenance so you can pick the right kitchen sink material."),
 ("article","fireclay-sink-problems","Fireclay Sink Problems: 7 Issues to Know | NOZLOO","Worried about fireclay sink problems? We cover the 7 most common issues — chipping, crazing, stains, weight, cost — and how to avoid each one."),
 ("article","how-to-clean-fireclay-sink","How to Clean a Fireclay Sink Without Damaging the Finish | NOZLOO","White fireclay sinks are easy to keep clean. Daily care, safe cleaners, stain removal, what to avoid — plus how to fix chips and protect the glaze."),
 ("article","best-fireclay-sink-brands","Best Fireclay Sink Brands 2026: Reviews | NOZLOO","Comparing the best fireclay sink brands for 2026 — Rohl, Bocchi, Ruvati, Blanco, NOZLOO. Reviews, pricing, warranty, and which brand fits your kitchen."),
 ("article","fireclay-sink-pros-and-cons","Fireclay Sink Pros and Cons: Honest Buyer's Guide | NOZLOO","Considering a fireclay sink? Learn the real pros and cons—durability, weight, cost, chipping risk, maintenance, and when it's worth buying."),
 ("article","farmhouse-sink-price-guide","Cheap vs Expensive Farmhouse Sinks | NOZLOO","Farmhouse sink prices range from $150 to $1,500. See what you get at each price point: material, construction, durability, and where the markup hides."),
 ("article","fireclay-sink-buying-guide","Fireclay Sink Buying Guide: Size & Quality | NOZLOO","Learn how to choose a fireclay sink by size, bowl style, glaze quality, cabinet fit, drain placement, installation needs, and common buying mistakes."),
 ("article","fireclay-farmhouse-sink-cabinet-size","Fireclay Farmhouse Sink Cabinet Size Guide | NOZLOO",'Learn what size cabinet fits a fireclay farmhouse sink, including 30", 33", and 36" base cabinets, apron cutouts, support frames, and key measurements.'),
 ("article","fireclay-farmhouse-sink-worth-it","Is a Fireclay Farmhouse Sink Worth It? | NOZLOO","Is a fireclay farmhouse sink worth it? Learn when real fireclay makes sense, what to check before install, and how to avoid brand markup."),
 ("article","do-fireclay-sinks-crack-easily","Do Fireclay Sinks Crack Easily? Installation Guide","Do fireclay sinks crack easily? Learn crack causes, installation support needs, thermal shock risks, and prevention steps before installation."),
 ("article","fireclay-vs-granite-composite-sink-surface","Fireclay vs Granite Composite Sink: Surface Guide | NOZLOO","Fireclay vs granite composite sink: compare smooth glaze vs matte stone finish, cleaning, stains, water spots, heat, and kitchen style."),
 ("article","best-kitchen-sink-materials","Best Kitchen Sink Materials: How to Choose | NOZLOO","Compare the best kitchen sink materials: stainless steel, granite composite, fireclay, cast iron, copper, quartz, and stone. Find the right one for you."),
 ("article","can-you-use-garbage-disposal-with-fireclay-sink",None,"Most fireclay sinks can use a garbage disposal. Learn how to check flange depth, cabinet clearance, plumbing, crack risk, and warranty."),
 ("article","good-quality-fireclay-sink","How to Tell If a Fireclay Sink Is Good Quality?","Learn how to judge a good quality fireclay sink by weight, glaze, shape, durability, cabinet support, warranty, and inspection details before buying."),
 ("article","farmhouse-sink-accessories-guide","Farmhouse Sink Accessories Guide | NOZLOO","Learn how farmhouse sink accessories like a sink grid, drying rack, cutting board, and drain kit help protect and organize a fireclay workstation sink."),
 ("article","farmhouse-sink-vs-apron-sink","Farmhouse Sink vs Apron Sink: The Difference | NOZLOO","Confused by farmhouse sink vs apron sink? Learn the real difference, why the terms overlap, and what to check before choosing a kitchen sink."),
 ("article","are-farmhouse-sinks-still-in-style-in-2026",None,"Farmhouse sinks are still in style in 2026, but the look has changed. Learn what feels outdated, what looks modern, and how to make one work."),
 ("article","before-you-buy-a-farmhouse-sink","Before You Buy a Farmhouse Sink: A Checklist | NOZLOO","Before you buy a farmhouse sink, check cabinet readiness, countertop timing, installer approval, delivery, and your return window. Read the checklist."),
 ("article","how-far-should-a-farmhouse-sink-stick-out","How Far Should a Farmhouse Sink Stick Out? | NOZLOO","Learn how far a farm sink should stick out, whether it should sit flush or slightly past cabinets, and what to check before installation."),
 ("article","how-to-install-a-fireclay-farmhouse-sink","How to Install a Fireclay Farmhouse Sink | NOZLOO","A step-by-step guide to installing a fireclay farmhouse sink: support the weight, build the frame, cut the cabinet, level, seal, and know when to call a pro."),
 ("article","farmhouse-sink-reveal",None,"Compare positive, zero, and negative farmhouse sink reveals, including cleaning, countertop templating, workstation clearance, and replacement fit."),
 ("article","farmhouse-sink-plumbing-rough-in","Farmhouse Sink Plumbing Rough-In and Drain Height","Plan farmhouse sink drain height, P-trap placement, shutoff valves, and cabinet clearances for a cleaner, code-aware plumbing rough-in."),
 ("article","farmhouse-sink-depth","Farmhouse Sink Depth: 7, 8, 9 or 10 Inches?","Compare 7, 8, 9, and 10 inch farmhouse sink depths by comfort, bowl capacity, apron height, cabinet fit, and everyday kitchen use."),
 ("article","do-fireclay-farmhouse-sinks-add-resale-value","Do Fireclay Farmhouse Sinks Add Resale Value? | NOZLOO","Honest take on whether a fireclay farmhouse sink helps kitchen resale value, what buyers actually notice, and how to choose one that pays off."),
 ("article","workstation-farmhouse-sinks-upgrades-buyers-notice","Workstation Farmhouse Sinks: Are They Worth It? | NOZLOO","What a workstation ledge and its accessories actually do day to day, which upgrades buyers notice, and how to pick a workstation farmhouse sink."),
 ("article","how-long-do-fireclay-farmhouse-sinks-last","How Long Do Fireclay Farmhouse Sinks Last? | NOZLOO","How long a fireclay farmhouse sink really lasts, what affects its lifespan, and simple habits that keep the glaze looking new for decades."),
 ("article","single-vs-double-bowl-farmhouse-sink","Single vs Double Bowl Farmhouse Sink: Which Is Better?","Compare single vs double bowl farmhouse sinks by cookware, hand-washing, dishwasher use, disposal setup, and daily kitchen habits."),
 ("article","30-vs-33-inch-farmhouse-sink","30 vs 33 Inch Farmhouse Sink: Which Should You Choose? | NOZLOO","Compare 30 vs 33 inch farmhouse sinks by cabinet fit, basin room, counter space, and price — with real interior dimensions and a decision table."),
 ("article","fireclay-vs-porcelain-sink","Fireclay vs Porcelain Sink: Key Differences Explained","Compare fireclay vs porcelain sinks by material, durability, cleaning, cost, weight, kitchen use, and whether fireclay is the same as porcelain."),
 ("article","faucets-for-farmhouse-sinks","Faucets for Farmhouse Sinks: Get the Reach Right","Choosing faucets for farmhouse sinks? A 20-inch sink leaves just four inches of counter for the hole, base and handle. Get the reach right before you buy."),
 ("article","farmhouse-sink-with-butcher-block-countertop","Farmhouse Sink with Butcher Block Counter: Install & Seal","Learn how to support, cut and seal a farmhouse sink with butcher block countertop while protecting the wood from moisture damage."),
 ("article","how-to-measure-for-a-farmhouse-sink","How to Measure for a Farmhouse Sink: New or Replacement","Learn which sink, cabinet, apron, countertop, cutout, and drain measurements to record before a new farmhouse sink installation or replacement."),
 ("article","offset-drain-kitchen-sink","Offset Drain Kitchen Sink: Pros, Cons, Plumbing and Storage","Compare offset and center drain kitchen sinks, including basin space, plumbing, disposal placement, workstation use, and cabinet storage."),
 ("article","functional-farmhouse-kitchen-design","Functional Farmhouse Kitchen Design: Sink, Seating & Storage","Plan a functional farmhouse kitchen with practical advice on sink selection, kitchen clearances, banquette seating, storage and warm materials."),

 ("page","contact","Contact Us | NOZLOO","Contact NOZLOO for product inquiries, order support, shipping questions, and collaboration opportunities. We typically reply within 12 hours."),
 ("page","about","About NOZLOO | Real Fireclay Farmhouse Sinks","Learn about NOZLOO, a modern home brand focused on real fireclay sinks designed for timeless style, durability, and everyday living."),
 ("page","support","Customer Support | NOZLOO","Get support from NOZLOO for order inquiries, shipping updates, product questions, and after-sales assistance. We typically reply within 12 hours."),
 ("page","return-policy","Return Policy | NOZLOO","Read NOZLOO's return policy, including return eligibility, damaged items, refund timelines, and how to start a return request."),
 ("page","warranty","NOZLOO Limited Lifetime Warranty","NOZLOO fireclay sinks are backed by a Limited Lifetime Warranty for eligible residential use. View coverage, exclusions, claims, and return policy."),
 ("page","shipping-policy","NOZLOO Shipping Policy","Learn about NOZLOO shipping timelines, processing, delivery, inspection requirements, and what to do if your fireclay sink arrives damaged."),
 ("page","faq","NOZLOO Sink FAQ | Fireclay Farmhouse Sink Questions","Find answers about NOZLOO fireclay farmhouse sinks including durability, installation, shipping, warranty, and returns."),
 ("page","care-maintenance","NOZLOO Care & Maintenance","Learn how to clean, protect, and maintain your NOZLOO fireclay farmhouse sink for long-lasting performance and appearance."),
 ("page","why-fireclay","Why Choose a Fireclay Sink? | NOZLOO","Learn why fireclay sinks are valued for their durable, non-porous glaze, heat resistance, quiet feel, and timeless farmhouse style—plus what to plan for."),
 ("page","farmhouse-sink-size-calculator","Farmhouse Sink Size Calculator: Find the Right Sink | NOZLOO","Find the right fireclay farmhouse sink in seconds. Match your base cabinet to a 30-inch or 33-inch apron sink, single or double bowl. Free tool by NOZLOO."),
 ("page","farmhouse-sink-accessories","Farmhouse Sinks with Accessories | NOZLOO Fireclay Sinks","Shop NOZLOO farmhouse sinks with cutting boards, drying racks, bottom grids, and drain kits included. Accessories vary by model and are not sold separately."),
 ("page","track-order",None,None),
 ("page","sitemap","Sitemap | NOZLOO","Browse NOZLOO sink collections, individual models, planning guides, support pages, policies, and company information."),
 ("page","data-sharing-opt-out","Your Privacy Choices | NOZLOO","Manage your privacy choices and opt out of the sale or sharing of personal information for targeted advertising where applicable."),
]

TITLE_MAX = 60      # ~580px SERP truncation threshold
DESC_MIN, DESC_MAX = 120, 160

def bar(n, lo, hi):
    if n is None: return "MISSING"
    if n > hi:  return f"{n:>3}  OVER by {n-hi}"
    if n < lo:  return f"{n:>3}  under by {lo-n}"
    return f"{n:>3}  ok"

print("=" * 96)
print("TITLE TAGS OVER 60 CHARS  (truncated in Google SERP)")
print("=" * 96)
over = [(k,h,t,len(t)) for k,h,t,_ in DATA if t and len(t) > TITLE_MAX]
over.sort(key=lambda r: -r[3])
for k,h,t,n in over:
    print(f"  [{k:10}] {n:>3}  {t}")
print(f"\n  -> {len(over)} of {sum(1 for _,_,t,_ in DATA if t)} title tags exceed {TITLE_MAX} chars")

print()
print("=" * 96)
print("MISSING TITLE TAG / META DESCRIPTION")
print("=" * 96)
for k,h,t,d in DATA:
    miss = [n for n,v in (("title_tag",t),("meta_description",d)) if not v]
    if miss:
        print(f"  [{k:10}] {h:<52} missing: {', '.join(miss)}")

print()
print("=" * 96)
print(f"META DESCRIPTIONS OUTSIDE {DESC_MIN}-{DESC_MAX} CHARS")
print("=" * 96)
bad = [(k,h,d,len(d)) for k,h,_,d in DATA if d and not (DESC_MIN <= len(d) <= DESC_MAX)]
bad.sort(key=lambda r: -r[3])
for k,h,d,n in bad:
    print(f"  [{k:10}] {bar(n, DESC_MIN, DESC_MAX):<18} {h}")
print(f"\n  -> {len(bad)} of {sum(1 for _,_,_,d in DATA if d)} meta descriptions outside range")

print()
print("=" * 96)
print("BRAND SUFFIX CONSISTENCY  (title tags without '| NOZLOO')")
print("=" * 96)
nosuffix = [(k,h,t) for k,h,t,_ in DATA if t and "| NOZLOO" not in t]
for k,h,t in nosuffix:
    print(f"  [{k:10}] {len(t):>3}  {t}")
print(f"\n  -> {len(nosuffix)} of {sum(1 for _,_,t,_ in DATA if t)} lack the '| NOZLOO' suffix")

print()
print("=" * 96)
print("SUMMARY")
print("=" * 96)
tot = len(DATA)
withT = sum(1 for _,_,t,_ in DATA if t)
withD = sum(1 for _,_,_,d in DATA if d)
print(f"  URLs analysed (Admin API objects) : {tot}")
print(f"  title tags set                    : {withT}/{tot}   ({tot-withT} missing)")
print(f"  meta descriptions set             : {withD}/{tot}   ({tot-withD} missing)")
print(f"  titles over {TITLE_MAX} chars                : {len(over)}  ({len(over)/withT*100:.0f}% of set titles)")
print(f"  descriptions outside {DESC_MIN}-{DESC_MAX}       : {len(bad)}  ({len(bad)/withD*100:.0f}% of set descriptions)")
