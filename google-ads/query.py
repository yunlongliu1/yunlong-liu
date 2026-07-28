"""跑任意 GAQL 查询。

    # 默认：最近 7 天各广告系列的花费/展示/点击/转化
    python query.py

    # 自己写 GAQL
    python query.py "SELECT campaign.name, metrics.clicks FROM campaign WHERE segments.date DURING LAST_30_DAYS"

    # 指定账号（覆盖 .env 里的 GOOGLE_ADS_CUSTOMER_ID）
    python query.py --customer-id 123-456-7890

GAQL 字段参考：https://developers.google.com/google-ads/api/fields/v25/overview
"""

from __future__ import annotations

import argparse
import sys

from google.ads.googleads.errors import GoogleAdsException

from ads_client import (
    build_client,
    format_customer_id,
    normalize_customer_id,
    print_google_ads_exception,
    target_customer_id,
)

DEFAULT_QUERY = """
    SELECT
      campaign.id,
      campaign.name,
      campaign.status,
      metrics.impressions,
      metrics.clicks,
      metrics.cost_micros,
      metrics.conversions
    FROM campaign
    WHERE segments.date DURING LAST_7_DAYS
    ORDER BY metrics.cost_micros DESC
"""


def render_default_rows(rows) -> int:
    header = f"{'广告系列':<40} {'状态':<10} {'展示':>10} {'点击':>8} {'花费':>12} {'转化':>8}"
    print(header)
    print("-" * len(header))

    count = 0
    total_cost = total_impressions = total_clicks = 0
    total_conversions = 0.0

    for row in rows:
        count += 1
        cost = row.metrics.cost_micros / 1_000_000
        total_cost += row.metrics.cost_micros
        total_impressions += row.metrics.impressions
        total_clicks += row.metrics.clicks
        total_conversions += row.metrics.conversions

        name = row.campaign.name
        if len(name) > 38:
            name = name[:37] + "…"
        print(
            f"{name:<40} {row.campaign.status.name:<10} "
            f"{row.metrics.impressions:>10,} {row.metrics.clicks:>8,} "
            f"{cost:>12,.2f} {row.metrics.conversions:>8,.1f}"
        )

    if count:
        print("-" * len(header))
        print(
            f"{'合计':<40} {'':<10} {total_impressions:>10,} {total_clicks:>8,} "
            f"{total_cost / 1_000_000:>12,.2f} {total_conversions:>8,.1f}"
        )
    return count


def render_generic_rows(rows) -> int:
    count = 0
    for row in rows:
        count += 1
        print(row)
    return count


def main() -> None:
    parser = argparse.ArgumentParser(description="执行 GAQL 查询")
    parser.add_argument("gaql", nargs="?", help="GAQL 语句；不传则跑默认的广告系列报表")
    parser.add_argument("--customer-id", help="覆盖 .env 里的 GOOGLE_ADS_CUSTOMER_ID")
    args = parser.parse_args()

    client = build_client()
    customer_id = (
        normalize_customer_id(args.customer_id)
        if args.customer_id
        else target_customer_id()
    )
    query = args.gaql or DEFAULT_QUERY
    is_default = args.gaql is None

    print(f"账号: {format_customer_id(customer_id)}")
    print(f"查询: {' '.join(query.split())}\n")

    try:
        googleads_service = client.get_service("GoogleAdsService")
        rows = googleads_service.search(customer_id=customer_id, query=query)
        count = render_default_rows(rows) if is_default else render_generic_rows(rows)
        if not count:
            print("（没有返回任何数据行）")
    except GoogleAdsException as error:
        print_google_ads_exception(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
