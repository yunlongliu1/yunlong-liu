"""连通性自检：确认凭据能真正打通 Google Ads API。

依次做三件事：
  1. ListAccessibleCustomers —— 验证 开发者令牌 + OAuth 凭据是否有效
  2. 查询目标账号的基本信息（名称/币种/时区/是否经理账号）
  3. 如果目标是经理账号，列出它下面的所有子账号

    python test_connection.py
"""

from __future__ import annotations

import sys

from google.ads.googleads.errors import GoogleAdsException

from ads_client import (
    build_client,
    format_customer_id,
    print_google_ads_exception,
    target_customer_id,
)

CUSTOMER_QUERY = """
    SELECT
      customer.id,
      customer.descriptive_name,
      customer.currency_code,
      customer.time_zone,
      customer.manager,
      customer.test_account
    FROM customer
    LIMIT 1
"""

CHILD_ACCOUNTS_QUERY = """
    SELECT
      customer_client.id,
      customer_client.descriptive_name,
      customer_client.currency_code,
      customer_client.manager,
      customer_client.level,
      customer_client.status
    FROM customer_client
    WHERE customer_client.level <= 1
"""


def step_list_accessible_customers(client) -> list[str]:
    print("[1/3] 验证凭据，拉取可访问的账号列表 ...")
    customer_service = client.get_service("CustomerService")
    response = customer_service.list_accessible_customers()

    ids = [resource.split("/")[-1] for resource in response.resource_names]
    if not ids:
        print("      凭据有效，但这个 Google 账号下没有任何可访问的广告账号。")
        return []

    print(f"      凭据有效，可访问 {len(ids)} 个账号：")
    for customer_id in ids:
        print(f"        - {format_customer_id(customer_id)}")
    return ids


def step_describe_customer(client, customer_id: str) -> bool:
    pretty = format_customer_id(customer_id)
    print(f"\n[2/3] 读取账号 {pretty} 的基本信息 ...")

    googleads_service = client.get_service("GoogleAdsService")
    rows = googleads_service.search(customer_id=customer_id, query=CUSTOMER_QUERY)

    is_manager = False
    for row in rows:
        customer = row.customer
        is_manager = customer.manager
        print(f"      账号名称:   {customer.descriptive_name}")
        print(f"      账号 ID:    {format_customer_id(str(customer.id))}")
        print(f"      币种:       {customer.currency_code}")
        print(f"      时区:       {customer.time_zone}")
        print(f"      经理账号:   {'是' if customer.manager else '否'}")
        print(f"      测试账号:   {'是' if customer.test_account else '否'}")
    return is_manager


def step_list_child_accounts(client, customer_id: str) -> None:
    print(f"\n[3/3] {format_customer_id(customer_id)} 是经理账号，列出旗下账号 ...")

    googleads_service = client.get_service("GoogleAdsService")
    rows = googleads_service.search(customer_id=customer_id, query=CHILD_ACCOUNTS_QUERY)

    children = [row.customer_client for row in rows if not row.customer_client.manager]
    if not children:
        print("      这个经理账号下暂时没有子广告账号。")
        return

    print("      可以投放的子账号（把其中一个填进 .env 的 GOOGLE_ADS_CUSTOMER_ID）：")
    for child in children:
        print(
            f"        - {format_customer_id(str(child.id))}  "
            f"{child.descriptive_name}  [{child.currency_code}] {child.status.name}"
        )


def main() -> None:
    client = build_client()
    customer_id = target_customer_id()

    try:
        accessible = step_list_accessible_customers(client)

        if accessible and customer_id not in accessible:
            print(
                f"\n      注意：.env 里的 GOOGLE_ADS_CUSTOMER_ID"
                f"（{format_customer_id(customer_id)}）不在直接可访问列表里。"
                f"\n      如果它是经理账号下的子账号，这是正常的 ——"
                f" 只要 GOOGLE_ADS_LOGIN_CUSTOMER_ID 填的是对应的经理账号即可。"
            )

        is_manager = step_describe_customer(client, customer_id)

        if is_manager:
            step_list_child_accounts(client, customer_id)
        else:
            print("\n[3/3] 目标不是经理账号，跳过子账号枚举。")

        print("\n连接成功。可以用 `python query.py` 跑真实数据查询了。")

    except GoogleAdsException as error:
        print_google_ads_exception(error)
        print(
            "\n常见原因：\n"
            "  - DEVELOPER_TOKEN_NOT_APPROVED：开发者令牌还没通过审核，只能连测试账号\n"
            "  - USER_PERMISSION_DENIED：登录的 Google 账号对该广告账号没有权限，\n"
            "    或者 GOOGLE_ADS_LOGIN_CUSTOMER_ID 没填对应的经理账号\n"
            "  - CUSTOMER_NOT_FOUND：GOOGLE_ADS_CUSTOMER_ID 填错了",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
