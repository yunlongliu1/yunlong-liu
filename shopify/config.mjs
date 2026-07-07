// Shopify Admin API configuration for the nozloo store.
//
// Loads credentials from environment variables (and a local .env file if
// present) and exposes a validated, ready-to-use config object.
//
// Required env:
//   SHOPIFY_ADMIN_TOKEN   Admin API access token (shpat_...)
// Optional env (defaults shown):
//   SHOPIFY_STORE_DOMAIN  r8hi1q-rx.myshopify.com   <- API domain, NOT nozloo.myshopify.com
//   SHOPIFY_API_VERSION   2024-10

import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { loadDotEnv } from '../lib/dotenv.mjs';

loadDotEnv(join(dirname(fileURLToPath(import.meta.url)), '..'));

const DEFAULTS = {
  storeDomain: 'r8hi1q-rx.myshopify.com',
  apiVersion: '2024-10',
};

const storeDomain = (process.env.SHOPIFY_STORE_DOMAIN || DEFAULTS.storeDomain).trim();
const apiVersion = (process.env.SHOPIFY_API_VERSION || DEFAULTS.apiVersion).trim();
const adminToken = (process.env.SHOPIFY_ADMIN_TOKEN || '').trim();

export const config = {
  storeDomain,
  apiVersion,
  adminToken,
  endpoint: `https://${storeDomain}/admin/api/${apiVersion}/graphql.json`,
  get headers() {
    return {
      'Content-Type': 'application/json',
      'X-Shopify-Access-Token': adminToken,
    };
  },
};

// Validate config before use. Call before any API request.
export function assertConfigured() {
  // Guardrail for the "iron rule": the public storefront handle is NOT the API host.
  if (storeDomain === 'nozloo.myshopify.com') {
    throw new Error(
      'SHOPIFY_STORE_DOMAIN is nozloo.myshopify.com, which is NOT the API domain. ' +
        'Use r8hi1q-rx.myshopify.com instead.'
    );
  }
  if (!adminToken) {
    throw new Error(
      'Missing SHOPIFY_ADMIN_TOKEN. Copy .env.example to .env and set your Admin API ' +
        'access token (shpat_...), or export SHOPIFY_ADMIN_TOKEN in your environment.'
    );
  }
  if (!/^shpat_/.test(adminToken)) {
    console.warn('[shopify] Warning: SHOPIFY_ADMIN_TOKEN does not start with "shpat_".');
  }
}
