// Tiny zero-dependency .env loader shared across API integrations.
//
// Reads <rootDir>/.env and populates process.env for keys that are not
// already set. Real environment variables always take precedence over the
// file (standard dotenv convention).

import { readFileSync } from 'node:fs';
import { join } from 'node:path';

export function loadDotEnv(rootDir) {
  let text;
  try {
    text = readFileSync(join(rootDir, '.env'), 'utf8');
  } catch {
    return; // no .env file — rely on the real environment
  }
  for (const rawLine of text.split('\n')) {
    const line = rawLine.trim();
    if (!line || line.startsWith('#')) continue;
    const eq = line.indexOf('=');
    if (eq === -1) continue;
    const key = line.slice(0, eq).trim();
    let val = line.slice(eq + 1).trim();
    if (
      (val.startsWith('"') && val.endsWith('"')) ||
      (val.startsWith("'") && val.endsWith("'"))
    ) {
      val = val.slice(1, -1);
    }
    if (!(key in process.env)) process.env[key] = val;
  }
}
