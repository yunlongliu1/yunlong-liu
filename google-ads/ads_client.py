"""共享的 Google Ads API 客户端构建逻辑。

从同目录下的 .env（或真实环境变量）读取凭据，构建 GoogleAdsClient。
真实环境变量优先级高于 .env 文件。
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

from google.ads.googleads.client import GoogleAdsClient
from google.auth.exceptions import RefreshError

ENV_PATH = Path(__file__).resolve().parent / ".env"

REQUIRED_KEYS = (
    "GOOGLE_ADS_DEVELOPER_TOKEN",
    "GOOGLE_ADS_CLIENT_ID",
    "GOOGLE_ADS_CLIENT_SECRET",
    "GOOGLE_ADS_REFRESH_TOKEN",
)


def load_env(path: Path = ENV_PATH) -> None:
    """把 .env 里的 KEY=VALUE 读进 os.environ，不覆盖已存在的环境变量。"""
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        os.environ.setdefault(key.strip(), value)


def normalize_customer_id(customer_id: str) -> str:
    """把 851-773-3884 这种带横杠的写法规整成 8517733884。"""
    return "".join(ch for ch in customer_id if ch.isdigit())


def build_client() -> GoogleAdsClient:
    """构建 GoogleAdsClient；凭据缺失时给出可操作的报错。"""
    load_env()

    missing = [key for key in REQUIRED_KEYS if not os.environ.get(key, "").strip()]
    if missing:
        sys.exit(
            "缺少以下凭据：\n  "
            + "\n  ".join(missing)
            + f"\n\n请先复制 {ENV_PATH.parent}/.env.example 为 .env 并填写。"
            + "\n刷新令牌（GOOGLE_ADS_REFRESH_TOKEN）可以用 `python oauth_setup.py` 生成。"
        )

    config = {
        "developer_token": os.environ["GOOGLE_ADS_DEVELOPER_TOKEN"].strip(),
        "client_id": os.environ["GOOGLE_ADS_CLIENT_ID"].strip(),
        "client_secret": os.environ["GOOGLE_ADS_CLIENT_SECRET"].strip(),
        "refresh_token": os.environ["GOOGLE_ADS_REFRESH_TOKEN"].strip(),
        "use_proto_plus": True,
    }

    login_customer_id = os.environ.get("GOOGLE_ADS_LOGIN_CUSTOMER_ID", "").strip()
    if login_customer_id:
        config["login_customer_id"] = normalize_customer_id(login_customer_id)

    # load_from_dict 会立刻拿 refresh_token 去换 access_token，
    # 所以 OAuth 凭据不对在这里就会炸，翻译成人话再抛出去。
    try:
        return GoogleAdsClient.load_from_dict(config)
    except RefreshError as error:
        detail = str(error)
        if "invalid_client" in detail:
            hint = "client_id 或 client_secret 不对（去 Google Cloud Console → 凭据 核对）。"
        elif "invalid_grant" in detail:
            hint = (
                "refresh_token 无效或已过期。重新跑 `python oauth_setup.py` 生成；\n"
                "  如果 OAuth 应用还处于「测试中」状态，令牌 7 天就会过期，"
                "把应用发布即可长期有效。"
            )
        else:
            hint = "请检查 .env 里的 OAuth 三件套。"
        sys.exit(f"OAuth 认证失败：{detail}\n\n  {hint}")


def target_customer_id() -> str:
    """返回要操作的广告账号 ID（纯数字）。"""
    load_env()
    raw = os.environ.get("GOOGLE_ADS_CUSTOMER_ID", "").strip()
    if not raw:
        raw = os.environ.get("GOOGLE_ADS_LOGIN_CUSTOMER_ID", "").strip()
    if not raw:
        sys.exit("请在 .env 里设置 GOOGLE_ADS_CUSTOMER_ID（要查询的广告账号 ID）。")
    return normalize_customer_id(raw)


def format_customer_id(customer_id: str) -> str:
    """8517733884 -> 851-773-3884，方便人眼核对。"""
    digits = normalize_customer_id(customer_id)
    if len(digits) != 10:
        return digits
    return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"


def print_google_ads_exception(error) -> None:
    """把 GoogleAdsException 展开成人能看懂的排查信息。"""
    print(f"\n请求失败，request_id = {error.request_id}", file=sys.stderr)
    for failure_error in error.failure.errors:
        print(f"  错误码: {failure_error.error_code}", file=sys.stderr)
        print(f"  说明:   {failure_error.message}", file=sys.stderr)
        for field in failure_error.location.field_path_elements:
            print(f"    字段: {field.field_name}", file=sys.stderr)
