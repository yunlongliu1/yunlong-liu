// Minimal Shopify Admin GraphQL client (zero dependencies, Node 18+ global fetch).

import { config, assertConfigured } from './config.mjs';

/**
 * Run a GraphQL operation (query or mutation) against the Shopify Admin API.
 * Throws on HTTP errors, GraphQL `errors`, and any first-level `userErrors`.
 *
 * @param {string} query        GraphQL document
 * @param {object} [variables]  GraphQL variables
 * @returns {Promise<object>}    the `data` object
 */
export async function graphql(query, variables = {}) {
  assertConfigured();

  const res = await fetch(config.endpoint, {
    method: 'POST',
    headers: config.headers,
    body: JSON.stringify({ query, variables }),
  });

  const text = await res.text();
  let body;
  try {
    body = JSON.parse(text);
  } catch {
    throw new Error(`Shopify returned non-JSON (HTTP ${res.status}): ${text.slice(0, 500)}`);
  }

  if (!res.ok) {
    throw new Error(`Shopify HTTP ${res.status}: ${JSON.stringify(body.errors ?? body)}`);
  }
  if (body.errors) {
    throw new Error(`Shopify GraphQL errors: ${JSON.stringify(body.errors)}`);
  }

  // Surface first-level userErrors (mutations) so callers don't silently ignore them.
  const data = body.data ?? {};
  for (const key of Object.keys(data)) {
    const ue = data[key]?.userErrors;
    if (Array.isArray(ue) && ue.length) {
      throw new Error(`Shopify userErrors on ${key}: ${JSON.stringify(ue)}`);
    }
  }

  return data;
}
