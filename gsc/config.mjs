// Google Search Console (Webmasters v3) configuration for nozloo.com.
//
// Loads OAuth credentials from environment variables (and a local .env file
// if present). The client id/secret authorize the app; the refresh token —
// minted once via the interactive consent flow — is what actually lets the
// tooling call the API unattended.
//
// Required env:
//   GOOGLE_CLIENT_ID       OAuth 2.0 client id
//   GOOGLE_CLIENT_SECRET   OAuth 2.0 client secret
//   GOOGLE_REFRESH_TOKEN   Long-lived refresh token (from `cli.mjs exchange`)
// Optional env (defaults shown):
//   GSC_SITE_URL           sc-domain:nozloo.com   (or https://nozloo.com/)
//   GSC_SCOPE              .../auth/webmasters.readonly
//   GOOGLE_REDIRECT_URI    http://localhost

import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { loadDotEnv } from '../lib/dotenv.mjs';

loadDotEnv(join(dirname(fileURLToPath(import.meta.url)), '..'));

const DEFAULTS = {
  authUri: 'https://accounts.google.com/o/oauth2/auth',
  tokenUri: 'https://oauth2.googleapis.com/token',
  redirectUri: 'http://localhost',
  scope: 'https://www.googleapis.com/auth/webmasters.readonly',
  writeScope: 'https://www.googleapis.com/auth/webmasters',
  apiBase: 'https://www.googleapis.com/webmasters/v3',
  siteUrl: 'sc-domain:nozloo.com',
};

export const config = {
  clientId: (process.env.GOOGLE_CLIENT_ID || '').trim(),
  clientSecret: (process.env.GOOGLE_CLIENT_SECRET || '').trim(),
  refreshToken: (process.env.GOOGLE_REFRESH_TOKEN || '').trim(),
  projectId: (process.env.GOOGLE_PROJECT_ID || '').trim(),
  siteUrl: (process.env.GSC_SITE_URL || DEFAULTS.siteUrl).trim(),
  scope: (process.env.GSC_SCOPE || DEFAULTS.scope).trim(),
  redirectUri: (process.env.GOOGLE_REDIRECT_URI || DEFAULTS.redirectUri).trim(),
  authUri: DEFAULTS.authUri,
  tokenUri: DEFAULTS.tokenUri,
  writeScope: DEFAULTS.writeScope,
  apiBase: DEFAULTS.apiBase,
};

// The app is configured, i.e. we can at least start the OAuth flow.
export function assertClient() {
  if (!config.clientId || !config.clientSecret) {
    throw new Error(
      'Missing GOOGLE_CLIENT_ID / GOOGLE_CLIENT_SECRET. Copy .env.example to .env ' +
        'and fill them in (or export them in your environment).'
    );
  }
}

// We have a refresh token, i.e. we can call the API unattended.
export function assertAuthorized() {
  assertClient();
  if (!config.refreshToken) {
    throw new Error(
      'Missing GOOGLE_REFRESH_TOKEN. Authorize once:\n' +
        '  1. node gsc/cli.mjs auth-url        (open the URL, grant access)\n' +
        '  2. node gsc/cli.mjs exchange <code> (copy the `code` from the redirect URL)\n' +
        '  3. save GOOGLE_REFRESH_TOKEN=... into .env'
    );
  }
}
