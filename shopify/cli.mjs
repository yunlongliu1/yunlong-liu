#!/usr/bin/env node
// Command-line entry for quick Shopify Admin API calls.
//
//   node shopify/cli.mjs test               # connectivity + auth check
//   node shopify/cli.mjs shop               # print shop details as JSON
//   node shopify/cli.mjs query '<gql>'      # run an inline query
//   node shopify/cli.mjs query -            # read a query from stdin
//   echo '{ shop { name } }' | node shopify/cli.mjs query -
//
// Variables may be passed as a trailing JSON string:
//   node shopify/cli.mjs query '<gql>' '{"id":"gid://shopify/Product/1"}'

import { readFileSync } from 'node:fs';
import { config } from './config.mjs';
import { graphql } from './client.mjs';

const SHOP_QUERY = `{
  shop {
    name
    myshopifyDomain
    primaryDomain { url host }
    email
    currencyCode
    plan { displayName }
    ianaTimezone
  }
}`;

function readStdin() {
  try {
    return readFileSync(0, 'utf8');
  } catch {
    return '';
  }
}

async function main() {
  const [cmd = 'test', ...rest] = process.argv.slice(2);

  switch (cmd) {
    case 'test': {
      const { shop } = await graphql(SHOP_QUERY);
      console.log('✅ Connected to Shopify Admin API');
      console.log(`   endpoint  : ${config.endpoint}`);
      console.log(`   shop      : ${shop.name}`);
      console.log(`   api domain: ${shop.myshopifyDomain}`);
      console.log(`   storefront: ${shop.primaryDomain?.url}`);
      console.log(`   currency  : ${shop.currencyCode}`);
      console.log(`   plan      : ${shop.plan?.displayName}`);
      break;
    }
    case 'shop': {
      const { shop } = await graphql(SHOP_QUERY);
      console.log(JSON.stringify(shop, null, 2));
      break;
    }
    case 'query':
    case 'mutation': {
      let doc = rest[0];
      if (!doc || doc === '-') doc = readStdin();
      if (!doc.trim()) throw new Error('No GraphQL document provided.');
      const variables = rest[1] ? JSON.parse(rest[1]) : {};
      const data = await graphql(doc, variables);
      console.log(JSON.stringify(data, null, 2));
      break;
    }
    default:
      console.error(`Unknown command: ${cmd}`);
      console.error('Usage: node shopify/cli.mjs [test|shop|query|mutation] ...');
      process.exit(2);
  }
}

main().catch((err) => {
  console.error('❌', err.message);
  process.exit(1);
});
