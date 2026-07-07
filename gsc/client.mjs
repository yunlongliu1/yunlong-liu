// Minimal Search Console (Webmasters v3) client. Zero dependencies (Node 18+ fetch).

import { config } from './config.mjs';
import { getAccessToken } from './auth.mjs';

const enc = encodeURIComponent;

// Authenticated request. Refreshes the access token on every call (simple and
// safe for short-lived CLI use); throws with the API's error message on failure.
export async function api(method, path, body) {
  const accessToken = await getAccessToken();
  const res = await fetch(`${config.apiBase}${path}`, {
    method,
    headers: {
      Authorization: `Bearer ${accessToken}`,
      ...(body ? { 'Content-Type': 'application/json' } : {}),
    },
    body: body ? JSON.stringify(body) : undefined,
  });
  const text = await res.text();
  let data;
  try {
    data = text ? JSON.parse(text) : {};
  } catch {
    throw new Error(`Google API returned non-JSON (HTTP ${res.status}): ${text.slice(0, 300)}`);
  }
  if (!res.ok) {
    throw new Error(`Google API HTTP ${res.status}: ${data?.error?.message ?? JSON.stringify(data)}`);
  }
  return data;
}

// GET /sites — list the properties this account can access.
export function listSites() {
  return api('GET', '/sites');
}

// POST /sites/{site}/searchAnalytics/query — clicks/impressions/ctr/position.
export function searchAnalytics(requestBody, siteUrl = config.siteUrl) {
  return api('POST', `/sites/${enc(siteUrl)}/searchAnalytics/query`, requestBody);
}

// GET /sites/{site}/sitemaps — list submitted sitemaps.
export function listSitemaps(siteUrl = config.siteUrl) {
  return api('GET', `/sites/${enc(siteUrl)}/sitemaps`);
}

// PUT /sites/{site}/sitemaps/{feedpath} — submit a sitemap (needs the full
// webmasters scope, not the readonly one).
export function submitSitemap(feedpath, siteUrl = config.siteUrl) {
  return api('PUT', `/sites/${enc(siteUrl)}/sitemaps/${enc(feedpath)}`);
}
