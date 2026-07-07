# Google Search Console API — nozloo.com

Reusable, zero-dependency tooling for the **nozloo.com** Search Console
(Webmasters v3) property: search-analytics queries and sitemap management.
OAuth credentials are read from the environment (or a local, git-ignored
`.env`) — **no secrets live in this repo**.

## Facts

| | |
|---|---|
| Google Cloud project | `my-project-6202-1762606633672` |
| Auth URI | `https://accounts.google.com/o/oauth2/auth` |
| Token URI | `https://oauth2.googleapis.com/token` |
| Redirect URI | `http://localhost` (installed-app / loopback flow) |
| Read scope | `https://www.googleapis.com/auth/webmasters.readonly` |
| Write scope | `https://www.googleapis.com/auth/webmasters` (needed to submit sitemaps) |
| API base | `https://www.googleapis.com/webmasters/v3` |
| Default property | `sc-domain:nozloo.com` (run `sites` to confirm the exact string) |

## One-time authorization

The client id/secret only *identify* the app. To call the API unattended you
mint a long-lived **refresh token** once, via browser consent:

```bash
cp .env.example .env            # then fill in GOOGLE_CLIENT_ID / GOOGLE_CLIENT_SECRET

# 1. Print the consent URL and open it in a browser signed into the Google
#    account that owns the nozloo.com property. Grant access.
node gsc/cli.mjs auth-url
#    (add --write if you also need to submit sitemaps)

# 2. The browser lands on http://localhost/?code=XXXX (it will show
#    "can't reach this site" — that's fine). Copy the `code` value and:
node gsc/cli.mjs exchange 'XXXX'

# 3. Paste the printed GOOGLE_REFRESH_TOKEN=... line into .env.
```

After that the refresh token is used automatically — access tokens are minted
on demand and expire on their own.

## Usage

```bash
node gsc/cli.mjs sites                       # list verified properties + your access level
node gsc/cli.mjs query                       # top 10 queries, last 28 days
node gsc/cli.mjs query --dim page --limit 20 # top 20 pages
node gsc/cli.mjs query --dim query,page --days 90
node gsc/cli.mjs query --start 2026-06-01 --end 2026-06-30
node gsc/cli.mjs sitemaps                     # list submitted sitemaps

# npm script equivalents
npm run gsc -- query --dim page
```

**Programmatic:**

```js
import { searchAnalytics, listSites } from './gsc/client.mjs';

const { rows } = await searchAnalytics({
  startDate: '2026-06-01',
  endDate: '2026-06-30',
  dimensions: ['query'],
  rowLimit: 25,
});
```

`searchAnalytics()` / `api()` refresh the access token automatically and throw
the API's error message on failure.

## Files

| File | Purpose |
|---|---|
| `config.mjs` | Loads/validates OAuth env (+ optional `.env`) |
| `auth.mjs` | Build consent URL, exchange code, refresh access token |
| `client.mjs` | `api()` + `listSites` / `searchAnalytics` / `listSitemaps` / `submitSitemap` |
| `cli.mjs` | `auth-url` / `exchange` / `token` / `sites` / `query` / `sitemaps` |
| `../lib/dotenv.mjs` | Shared zero-dep `.env` loader |
| `../.env.example` | Template — copy to `.env` and fill in |

## Troubleshooting

- **`redirect_uri_mismatch`** — the OAuth client's registered redirect URI
  must include exactly `http://localhost`. Set `GOOGLE_REDIRECT_URI` if yours
  differs.
- **"Google hasn't verified this app"** — for a project in *testing* mode, add
  your Google account under *OAuth consent screen → Test users*, then click
  *Advanced → Go to … (unsafe)* to proceed. It's your own app.
- **No `refresh_token` on exchange** — Google only returns one on first
  consent. Revoke the prior grant at
  <https://myaccount.google.com/permissions> and re-run `auth-url`
  (the URL already sends `prompt=consent&access_type=offline`).
- **`403 / insufficientPermissions`** — the authorized account isn't a verified
  owner/user of the property, or you used the readonly scope for a write.

## Security

The refresh token and client secret are password-equivalent. They are **never**
committed — `.gitignore` excludes `.env`, and only placeholders live in
`.env.example`. If exposed, revoke at
<https://myaccount.google.com/permissions> and rotate the client secret in the
Google Cloud console.
