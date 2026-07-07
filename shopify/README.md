# Shopify Admin API — NOZLOO

Reusable, zero-dependency tooling for calling the **nozloo** store's Shopify
Admin GraphQL API. Credentials are read from the environment (or a local,
git-ignored `.env`) — **no secrets live in this repo**.

## Store facts

| | |
|---|---|
| Store handle | `nozloo` (admin.shopify.com/store/nozloo) |
| **API domain** | **`r8hi1q-rx.myshopify.com`** |
| Storefront | `nozloo.com` |
| App | Claude Admin (dev.shopify.com org 209023901) |
| API version | `2024-10` |
| Endpoint | `POST https://r8hi1q-rx.myshopify.com/admin/api/2024-10/graphql.json` |
| Auth header | `X-Shopify-Access-Token: <shpat_…>` |

> **Iron rule:** always call the API on `r8hi1q-rx.myshopify.com`.
> Never use `nozloo.myshopify.com` — the config layer throws if you try.

**Scopes granted:** `write_products`, `write_content`, `write_themes`,
`write_files`, `write_inventory`, `write_translations`,
`write_online_store_navigation`, `read_orders`, `read_customers`,
`read_product_listings`, `read_analytics`.

## Setup

```bash
cp .env.example .env
# edit .env and paste the real Admin API access token (shpat_…)
```

`.env` is git-ignored. Alternatively, export the vars directly (e.g. in the
Claude Code web environment's variable settings):

```bash
export SHOPIFY_ADMIN_TOKEN=shpat_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# SHOPIFY_STORE_DOMAIN and SHOPIFY_API_VERSION default to the values above.
```

## Usage

**CLI (Node 18+, no install):**

```bash
node shopify/cli.mjs test          # connectivity + auth smoke test
node shopify/cli.mjs shop          # dump shop details as JSON
node shopify/cli.mjs query '{ products(first: 5) { nodes { title } } }'
echo '{ shop { name } }' | node shopify/cli.mjs query -

# npm script equivalents
npm run shopify:test
```

**curl (no Node):**

```bash
./shopify/shopify.sh                          # connectivity test
./shopify/shopify.sh '{ shop { name } }'      # inline query
```

**Programmatic:**

```js
import { graphql } from './shopify/client.mjs';

const data = await graphql(
  `query ($n: Int!) { products(first: $n) { nodes { id title } } }`,
  { n: 10 }
);
console.log(data.products.nodes);
```

`graphql()` throws on HTTP errors, GraphQL `errors`, and mutation
`userErrors`, so a resolved promise always means success.

## Files

| File | Purpose |
|---|---|
| `config.mjs` | Loads/validates env (+ optional `.env`), builds endpoint & headers |
| `client.mjs` | `graphql(query, variables)` helper over `fetch` |
| `cli.mjs` | `test` / `shop` / `query` / `mutation` command line |
| `shopify.sh` | curl-based quick tester (needs `jq`) |
| `../.env.example` | Template — copy to `.env` and fill in the token |

## Security

- The Admin API token is a password-equivalent secret. It is **never**
  committed — `.gitignore` excludes `.env`, and only placeholders live in
  `.env.example`.
- If the token is ever exposed, rotate it in the Claude Admin app
  (Settings → Apps → Claude Admin → API credentials) and update `.env`.
