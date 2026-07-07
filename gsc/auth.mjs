// Google OAuth 2.0 helpers for the Search Console API (installed-app / loopback flow).

import { config, assertClient, assertAuthorized } from './config.mjs';

// Build the consent URL. Open it in a browser, grant access, and Google
// redirects to the redirect_uri with `?code=...`. access_type=offline +
// prompt=consent guarantee a refresh_token is returned.
export function buildAuthUrl(scope = config.scope) {
  assertClient();
  const params = new URLSearchParams({
    client_id: config.clientId,
    redirect_uri: config.redirectUri,
    response_type: 'code',
    scope,
    access_type: 'offline',
    prompt: 'consent',
    include_granted_scopes: 'true',
  });
  return `${config.authUri}?${params.toString()}`;
}

async function tokenRequest(params) {
  const res = await fetch(config.tokenUri, {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams(params).toString(),
  });
  const text = await res.text();
  let body;
  try {
    body = JSON.parse(text);
  } catch {
    throw new Error(`Token endpoint returned non-JSON (HTTP ${res.status}): ${text.slice(0, 300)}`);
  }
  if (!res.ok) {
    const detail = [body.error, body.error_description].filter(Boolean).join(': ');
    throw new Error(`Token endpoint HTTP ${res.status}: ${detail || text.slice(0, 300)}`);
  }
  return body;
}

// Exchange an authorization code for tokens (returns access_token + refresh_token).
export async function exchangeCode(rawCode) {
  assertClient();
  // Codes copied straight from the redirect URL may be percent-encoded.
  const code = rawCode.includes('%') ? decodeURIComponent(rawCode.trim()) : rawCode.trim();
  return tokenRequest({
    code,
    client_id: config.clientId,
    client_secret: config.clientSecret,
    redirect_uri: config.redirectUri,
    grant_type: 'authorization_code',
  });
}

// Mint a short-lived access token from the stored refresh token.
export async function getAccessToken() {
  assertAuthorized();
  const body = await tokenRequest({
    client_id: config.clientId,
    client_secret: config.clientSecret,
    refresh_token: config.refreshToken,
    grant_type: 'refresh_token',
  });
  if (!body.access_token) throw new Error('Refresh succeeded but no access_token was returned.');
  return body.access_token;
}
