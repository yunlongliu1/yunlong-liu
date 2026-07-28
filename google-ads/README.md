# Google Ads API 接入

连接 Google Ads API 的最小可用工具集，对应账号 **nozloo-claude (851-773-3884)**。

## 先搞清楚一件事：光有开发者令牌是连不上的

API 中心页面上的**开发者令牌**只是四件套里的一件。完整的一次调用需要：

| 需要的东西 | 从哪来 | 状态 |
|---|---|---|
| 开发者令牌 | Google Ads → 管理 → API 中心 | ✅ 你已经有了 |
| OAuth client_id | Google Cloud Console → 凭据 | ⬜ 需要创建 |
| OAuth client_secret | 同上 | ⬜ 需要创建 |
| refresh_token | 跑 `oauth_setup.py` 授权换取 | ⬜ 需要生成 |

开发者令牌回答的是"**哪个应用**在调 API"，OAuth 那三件回答的是"**代表哪个 Google 账号**在调"。两者缺一不可。

另外你的令牌是**基本访问权限（Basic Access）**，可以正常访问生产账号，配额是每天 15,000 次操作，一般用量完全够。

## 安装

```bash
cd google-ads
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 第一步：建 OAuth 客户端

1. 打开 https://console.cloud.google.com/ ，新建一个项目（或用现成的）
2. **API 和服务 → 库** → 搜 "Google Ads API" → **启用**
3. **API 和服务 → OAuth 权限请求页面**：
   - User Type 选 **外部（External）**
   - 填应用名、支持邮箱（用 `info@nozloo.com`）
   - 作用域那一步可以先跳过
   - **测试用户**里把要授权的那个 Google 账号加进去（就是能登录 851-773-3884 的账号）
4. **API 和服务 → 凭据 → 创建凭据 → OAuth 客户端 ID**：
   - 应用类型选 **桌面应用（Desktop app）**
   - 创建完记下 **客户端 ID** 和 **客户端密钥**

> 应用保持"测试中"状态就行，不用提交 Google 审核。测试状态下 refresh_token 有效期 7 天；
> 想长期用就在 OAuth 权限请求页面点「发布应用」，令牌就不会过期了。

## 第二步：填凭据

```bash
cp .env.example .env
```

编辑 `.env`，填入开发者令牌、client_id、client_secret。
（`.env` 已经在 `.gitignore` 里，不会被提交。）

## 第三步：换取 refresh_token

**有图形界面的电脑**（会自动开浏览器）：

```bash
python oauth_setup.py
```

**服务器 / 远程环境 / 没浏览器**：

```bash
python oauth_setup.py --manual
```

手动模式会打印一条授权链接，你在任意浏览器里打开并授权，
浏览器会跳到 `http://localhost:8080/?code=...` 并显示"无法访问"——**这是正常的**，
把地址栏那一整条 URL 复制粘贴回终端即可。

授权时如果看到"Google 尚未验证此应用"的警告，点 **高级 → 继续前往**（你自己的应用，安全）。

脚本最后会输出一行 `GOOGLE_ADS_REFRESH_TOKEN=...`，把它填进 `.env`。

## 第四步：验证连接

```bash
python test_connection.py
```

成功的话会看到账号名称、币种、时区，以及经理账号下所有可投放的子账号：

```
[1/3] 验证凭据，拉取可访问的账号列表 ...
      凭据有效，可访问 1 个账号：
        - 851-773-3884
[2/3] 读取账号 851-773-3884 的基本信息 ...
      账号名称:   nozloo-claude
      经理账号:   是
[3/3] 851-773-3884 是经理账号，列出旗下账号 ...
      可以投放的子账号（把其中一个填进 .env 的 GOOGLE_ADS_CUSTOMER_ID）：
        - xxx-xxx-xxxx  ...
```

如果 851-773-3884 确实是经理账号，把上面列出的**子账号 ID** 填回 `.env` 的
`GOOGLE_ADS_CUSTOMER_ID`，`GOOGLE_ADS_LOGIN_CUSTOMER_ID` 保持经理账号 ID 不变。

## 第五步：查数据

```bash
# 默认：最近 7 天各广告系列的花费/展示/点击/转化
python query.py

# 自定义 GAQL
python query.py "SELECT campaign.name, metrics.clicks FROM campaign WHERE segments.date DURING LAST_30_DAYS"

# 临时指定别的账号
python query.py --customer-id 123-456-7890
```

GAQL 可用字段：https://developers.google.com/google-ads/api/fields/v25/overview

## 文件说明

| 文件 | 作用 |
|---|---|
| `ads_client.py` | 读 `.env` 构建 `GoogleAdsClient`，共享工具函数 |
| `oauth_setup.py` | 一次性脚本，走 OAuth 拿 refresh_token |
| `test_connection.py` | 连通性自检 + 列出所有可访问账号 |
| `query.py` | 执行 GAQL 查询 |
| `.env.example` | 凭据模板（`.env` 不会被提交） |

## 常见报错

| 报错 | 原因 / 处理 |
|---|---|
| `DEVELOPER_TOKEN_NOT_APPROVED` | 令牌还没通过审核，只能连测试账号 |
| `USER_PERMISSION_DENIED` | 授权的 Google 账号对该广告账号没权限，或 `GOOGLE_ADS_LOGIN_CUSTOMER_ID` 没填经理账号 |
| `CUSTOMER_NOT_FOUND` | `GOOGLE_ADS_CUSTOMER_ID` 填错，或该账号在经理账号层级之外 |
| `invalid_grant` | refresh_token 过期（测试状态 7 天）——重跑 `oauth_setup.py`，或把 OAuth 应用发布 |
| 没拿到 refresh_token | 该账号之前授权过。去 https://myaccount.google.com/permissions 撤销后重试 |

## 安全提示

开发者令牌 + client_secret + refresh_token 三者合起来就是你 Google Ads 账号的完整
操作权限（包括花钱投广告）。这些值只存在 `.env` 里，不要提交进仓库、不要贴到聊天/截图里。
如果怀疑泄露，去 API 中心点「重置令牌」，并在 Google Cloud Console 里重新生成 OAuth 密钥。
