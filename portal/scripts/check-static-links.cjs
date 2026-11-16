/**
 * Audit a generated static site before it is published.
 * Usage: node check-static-links.cjs <site-directory>
 * This is standalone and uses only Node.js built-in modules.
 */
const fs = require('node:fs');
const path = require('node:path');

const CONTENT_TAG = /<(a|img|source|script|link|video|audio)\b([^>]*?)>/gi;
const ATTR = /\b(href|src|srcset)\s*=\s*(["'])(.*?)\2/gi;

function allFiles(folder) {
  if (!fs.existsSync(folder)) throw new Error(`Missing output directory: ${folder}`);
  const result = [];
  const dirs = [folder];
  while (dirs.length) {
    const dir = dirs.pop();
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      const file = path.join(dir, entry.name);
      if (entry.isDirectory()) dirs.push(file);
      else if (entry.isFile()) result.push(file);
    }
  }
  return result;
}

function htmlDecode(value) {
  return value.replace(/&amp;/g, '&').replace(/&quot;/g, '"').replace(/&#39;/g, "'");
}

function candidates(root, url) {
  const normalized = decodeURIComponent(url.pathname);
  if (normalized.includes('\0')) throw new Error('NUL byte in URL');
  const relative = normalized.replace(/^\/+/, '');
  const dest = path.resolve(root, relative);
  if (dest !== root && !dest.startsWith(root + path.sep)) throw new Error(`Unsafe path: ${normalized}`);
  if (path.extname(normalized)) return [dest];
  return [dest, path.join(dest, 'index.html'), dest + '.html'];
}

function audit(rootDir) {
  const root = path.resolve(rootDir);
  const output = [];
  const files = allFiles(root);
  const htmlFiles = files.filter(x => x.endsWith('.html'));
  for (const file of htmlFiles) {
    const body = fs.readFileSync(file, 'utf8');
    const relativeFile = path.relative(root, file).split(path.sep).join('/');
    const pageUrl = new URL(relativeFile.replace(/(^|\/)index\.html$/, '$1'), 'https://preview.invalid/');
    for (const tag of body.matchAll(CONTENT_TAG)) {
      const tagName = tag[1].toLowerCase();
      for (const attr of tag[2].matchAll(ATTR)) {
        const key = attr[1].toLowerCase();
        if ((tagName === 'a' || tagName === 'link') && key === 'src') continue;
        const raw = htmlDecode(attr[3].trim());
        const values = key === 'srcset'
          ? raw.split(',').map(part => part.trim().split(/\s+/)[0])
          : [raw];
        for (const value of values) {
          if (!value || value.startsWith('#') || value.startsWith('//') || /^(?:mailto|tel|data|blob):/i.test(value)) continue;
          let url;
          try { url = new URL(value, pageUrl); }
          catch { output.push({ from: relativeFile, target: value, issue: 'invalid URL' }); continue; }
          if (url.origin !== pageUrl.origin) continue;
          try {
            const paths = candidates(root, url);
            if (!paths.some(p => fs.existsSync(p) && fs.statSync(p).isFile())) {
              output.push({ from: relativeFile, target: url.pathname, issue: 'missing static target' });
            }
          } catch (error) {
            output.push({ from: relativeFile, target: url.pathname, issue: error.message });
          }
        }
      }
    }
  }
  return { htmlPages: htmlFiles.length, errors: output };
}

if (require.main === module) {
  try {
    const root = process.argv[2];
    if (!root) throw new Error('Usage: node check-static-links.cjs <site-directory>');
    const summary = audit(root);
    const unique = [...new Set(summary.errors.map(x => x.target))];
    console.log(JSON.stringify({ pages: summary.htmlPages, brokenReferences: summary.errors.length, uniqueTargets: unique.length, examples: summary.errors.slice(0, 30) }, null, 2));
    if (summary.errors.length) process.exitCode = 1;
  } catch (error) { console.error(error); process.exitCode = 2; }
}
module.exports = { audit, candidates };
