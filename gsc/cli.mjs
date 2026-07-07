#!/usr/bin/env node
// Command-line entry for the Google Search Console API (nozloo.com).
//
//   node gsc/cli.mjs auth-url [--write]   Print the OAuth consent URL
//   node gsc/cli.mjs exchange <code>      Exchange an auth code for tokens
//   node gsc/cli.mjs token                Print a fresh access token
//   node gsc/cli.mjs sites                List verified properties
//   node gsc/cli.mjs query [flags]        Run a Search Analytics query
//   node gsc/cli.mjs sitemaps             List submitted sitemaps
//
// `query` flags: --days N (default 28) --lag N (default 3, GSC data latency)
//                --dim query[,page,country,device,date] (default query)
//                --limit N (default 10) --start YYYY-MM-DD --end YYYY-MM-DD

import { config } from './config.mjs';
import { buildAuthUrl, exchangeCode, getAccessToken } from './auth.mjs';
import { listSites, searchAnalytics, listSitemaps } from './client.mjs';

function parseFlags(args) {
  const flags = {};
  const positional = [];
  for (let i = 0; i < args.length; i++) {
    const a = args[i];
    if (a.startsWith('--')) {
      const key = a.slice(2);
      const next = args[i + 1];
      if (next !== undefined && !next.startsWith('--')) {
        flags[key] = next;
        i++;
      } else {
        flags[key] = true;
      }
    } else {
      positional.push(a);
    }
  }
  return { flags, positional };
}

function isoDaysAgo(n) {
  return new Date(Date.now() - n * 86_400_000).toISOString().slice(0, 10);
}

const HELP = `Google Search Console CLI — ${config.siteUrl}

  node gsc/cli.mjs auth-url [--write]   Print the OAuth consent URL (--write adds sitemap write scope)
  node gsc/cli.mjs exchange <code>      Exchange an auth code for tokens (prints the refresh token)
  node gsc/cli.mjs token                Print a fresh access token
  node gsc/cli.mjs sites                List verified properties
  node gsc/cli.mjs query [--days 28] [--dim query,page] [--limit 10] [--start …] [--end …]
  node gsc/cli.mjs sitemaps             List submitted sitemaps
`;

async function main() {
  const [cmd = 'help', ...rest] = process.argv.slice(2);
  const { flags, positional } = parseFlags(rest);

  switch (cmd) {
    case 'auth-url': {
      const scope = flags.write ? config.writeScope : config.scope;
      console.log(buildAuthUrl(scope));
      break;
    }
    case 'exchange': {
      const code = positional[0];
      if (!code) throw new Error('Usage: node gsc/cli.mjs exchange <code>');
      const tok = await exchangeCode(code);
      console.log('# Add this line to .env (git-ignored):');
      if (tok.refresh_token) {
        console.log(`GOOGLE_REFRESH_TOKEN=${tok.refresh_token}`);
      } else {
        console.log('# ⚠ No refresh_token returned. Revoke the prior grant at');
        console.log('#   https://myaccount.google.com/permissions and retry auth-url.');
      }
      console.log(`# access_token ok (expires in ${tok.expires_in}s); scope: ${tok.scope ?? '(default)'}`);
      break;
    }
    case 'token': {
      console.log(await getAccessToken());
      break;
    }
    case 'sites': {
      const data = await listSites();
      const sites = data.siteEntry ?? [];
      if (!sites.length) {
        console.log('No verified properties on this account.');
        break;
      }
      for (const s of sites) {
        console.log(`${(s.permissionLevel ?? '').padEnd(18)} ${s.siteUrl}`);
      }
      break;
    }
    case 'query': {
      const days = Number(flags.days ?? 28);
      const lag = Number(flags.lag ?? 3);
      const endDate = typeof flags.end === 'string' ? flags.end : isoDaysAgo(lag);
      const startDate = typeof flags.start === 'string' ? flags.start : isoDaysAgo(lag + days);
      const dimensions = (typeof flags.dim === 'string' ? flags.dim : 'query').split(',');
      const rowLimit = Number(flags.limit ?? 10);
      const data = await searchAnalytics({ startDate, endDate, dimensions, rowLimit });
      console.log(`# ${config.siteUrl}  ${startDate} → ${endDate}  dims=${dimensions.join(',')}`);
      const rows = data.rows ?? [];
      if (!rows.length) {
        console.log('(no rows — property may be empty or dates too recent)');
        break;
      }
      for (const r of rows) {
        const key = r.keys.join(' | ');
        console.log(
          `${key.padEnd(40)}  clicks=${r.clicks}  impr=${r.impressions}  ` +
            `ctr=${(r.ctr * 100).toFixed(2)}%  pos=${r.position.toFixed(1)}`
        );
      }
      break;
    }
    case 'sitemaps': {
      console.log(JSON.stringify(await listSitemaps(), null, 2));
      break;
    }
    default:
      console.log(HELP);
      if (cmd !== 'help') process.exit(2);
  }
}

main().catch((err) => {
  console.error('❌', err.message);
  process.exit(1);
});
