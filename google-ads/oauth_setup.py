"""一次性脚本：走一遍 Google OAuth 授权，拿到 refresh_token。

两种模式：

  python oauth_setup.py
      在本机自动开浏览器 + 起本地回调服务器。有图形界面的电脑用这个。

  python oauth_setup.py --manual
      打印授权链接，你在任意浏览器里打开，授权后把地址栏的整条 URL 粘回来。
      服务器 / 无图形界面 / 远程环境用这个。

拿到 refresh_token 后填进 .env 的 GOOGLE_ADS_REFRESH_TOKEN。
"""

from __future__ import annotations

import argparse
import os
import sys

from google_auth_oauthlib.flow import Flow, InstalledAppFlow

from ads_client import ENV_PATH, load_env

SCOPES = ["https://www.googleapis.com/auth/adwords"]
REDIRECT_URI = "http://localhost:8080/"


def client_config(client_id: str, client_secret: str) -> dict:
    return {
        "installed": {
            "client_id": client_id,
            "client_secret": client_secret,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "redirect_uris": [REDIRECT_URI],
        }
    }


def read_credentials() -> tuple[str, str]:
    """从 .env 读 client_id / client_secret，没有就当场问。"""
    load_env()
    client_id = os.environ.get("GOOGLE_ADS_CLIENT_ID", "").strip()
    client_secret = os.environ.get("GOOGLE_ADS_CLIENT_SECRET", "").strip()

    if not client_id:
        client_id = input("OAuth client_id: ").strip()
    if not client_secret:
        client_secret = input("OAuth client_secret: ").strip()

    if not client_id or not client_secret:
        sys.exit(
            "client_id / client_secret 不能为空。\n"
            "去 Google Cloud Console → API 和服务 → 凭据 → 创建 OAuth 客户端 ID"
            "（应用类型选「桌面应用」）。"
        )
    return client_id, client_secret


def run_local_server_flow(client_id: str, client_secret: str):
    """在本机开浏览器授权。prompt="consent" 必须带上，
    否则重复授权时 Google 不会再下发 refresh_token。"""
    flow = InstalledAppFlow.from_client_config(
        client_config(client_id, client_secret), scopes=SCOPES
    )
    flow.run_local_server(port=8080, access_type="offline", prompt="consent")
    return flow.credentials


def run_manual_flow(client_id: str, client_secret: str):
    flow = Flow.from_client_config(
        client_config(client_id, client_secret), scopes=SCOPES
    )
    flow.redirect_uri = REDIRECT_URI

    auth_url, _ = flow.authorization_url(
        access_type="offline", prompt="consent", include_granted_scopes="true"
    )

    print("\n1) 在浏览器里打开下面这个链接并完成授权：\n")
    print(auth_url)
    print(
        "\n2) 授权后浏览器会跳到 http://localhost:8080/?code=... 并显示「无法访问」，"
        "\n   这是正常的 —— 直接把地址栏里那一整条 URL 复制下来。\n"
    )

    pasted = input("3) 粘贴那条 URL（或只粘 code= 后面的授权码）后回车：\n> ").strip()
    if not pasted:
        sys.exit("没有收到授权码，已中止。")

    if pasted.startswith("http://") or pasted.startswith("https://"):
        flow.fetch_token(authorization_response=pasted)
    else:
        flow.fetch_token(code=pasted)

    return flow.credentials


def main() -> None:
    parser = argparse.ArgumentParser(description="生成 Google Ads API 刷新令牌")
    parser.add_argument(
        "--manual",
        action="store_true",
        help="不开浏览器，手动复制粘贴授权码（服务器/远程环境用）",
    )
    args = parser.parse_args()

    client_id, client_secret = read_credentials()

    if args.manual:
        credentials = run_manual_flow(client_id, client_secret)
    else:
        try:
            credentials = run_local_server_flow(client_id, client_secret)
        except Exception as exc:  # 没有浏览器 / 端口被占用 / 无图形界面
            print(f"本地服务器模式失败（{exc}），自动切换到手动模式。\n", file=sys.stderr)
            credentials = run_manual_flow(client_id, client_secret)

    if not credentials.refresh_token:
        sys.exit(
            "Google 没有下发 refresh_token。\n"
            "通常是因为该账号之前已经授权过。去 "
            "https://myaccount.google.com/permissions 撤销这个应用的授权后重试。"
        )

    print("\n授权成功。把下面这行写进 .env：\n")
    print(f"GOOGLE_ADS_REFRESH_TOKEN={credentials.refresh_token}")
    print(f"\n（.env 路径：{ENV_PATH}）")


if __name__ == "__main__":
    main()
