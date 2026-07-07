#!/usr/bin/env bash
# Quick Shopify Admin API call via curl (zero Node dependency).
#
# Reads credentials from the environment or a local .env file at repo root.
#   ./shopify/shopify.sh                        # connectivity test
#   ./shopify/shopify.sh '{ shop { name } }'    # run an inline query
#   echo '{ shop { name } }' | ./shopify/shopify.sh -
#
# Requires: curl, jq
set -euo pipefail

# Load .env from repo root if present. Real environment variables take
# precedence — a var already set in the environment is not overwritten.
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
if [[ -f "$ROOT/.env" ]]; then
  while IFS='=' read -r key val || [[ -n "$key" ]]; do
    key="${key#"${key%%[![:space:]]*}"}"   # ltrim
    key="${key%"${key##*[![:space:]]}"}"   # rtrim
    [[ -z "$key" || "$key" == \#* ]] && continue
    val="${val%$'\r'}"                      # strip trailing CR
    if [[ "$val" == \"*\" || "$val" == \'*\' ]]; then
      val="${val:1:${#val}-2}"             # strip surrounding quotes
    fi
    [[ -z "${!key:-}" ]] && export "$key=$val"
  done < "$ROOT/.env"
fi

DOMAIN="${SHOPIFY_STORE_DOMAIN:-r8hi1q-rx.myshopify.com}"
VERSION="${SHOPIFY_API_VERSION:-2024-10}"
TOKEN="${SHOPIFY_ADMIN_TOKEN:-}"

if [[ -z "$TOKEN" ]]; then
  echo "Missing SHOPIFY_ADMIN_TOKEN (set it in .env or the environment)." >&2
  exit 1
fi
if [[ "$DOMAIN" == "nozloo.myshopify.com" ]]; then
  echo "SHOPIFY_STORE_DOMAIN must be the API domain (r8hi1q-rx.myshopify.com), not nozloo.myshopify.com." >&2
  exit 1
fi

if [[ $# -ge 1 ]]; then
  QUERY="$1"
else
  QUERY='{ shop { name myshopifyDomain primaryDomain { url } } }'
fi
if [[ "$QUERY" == "-" ]]; then
  QUERY="$(cat)"
fi

jq -n --arg q "$QUERY" '{query: $q}' | curl -sS \
  -X POST "https://${DOMAIN}/admin/api/${VERSION}/graphql.json" \
  -H "X-Shopify-Access-Token: ${TOKEN}" \
  -H "Content-Type: application/json" \
  -d @- | jq .
