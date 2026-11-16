const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { audit } = require('./check-static-links.cjs');

function fixture(content) {
  const scratch = path.resolve(__dirname, '../../.scratch');
  fs.mkdirSync(scratch, { recursive: true });
  const root = fs.mkdtempSync(path.join(scratch, 'lineum-preview-'));
  for (const [name, contents] of Object.entries(content)) {
    fs.mkdirSync(path.dirname(path.join(root, name)), { recursive: true });
    fs.writeFileSync(path.join(root, name), contents);
  }
  return root;
}

test('detects a missing Czech localized page and absent wiki media', () => {
  const root = fixture({
    'index.html': '<a href="/cs/o-nas/">O nas</a><a href="/wiki/">Wiki</a>',
    'wiki/index.html': '<img src="/wiki/assets/not-found.png">'
  });
  try {
    const out = audit(root);
    assert.deepEqual(new Set(out.errors.map(x => x.target)), new Set(['/cs/o-nas/', '/wiki/assets/not-found.png']));
  } finally { fs.rmSync(root, { recursive: true, force: true }); }
});

test('resolves assets, image srcset, HTML pages and external links', () => {
  const root = fixture({
    'index.html': '<a href="/cs/o-nas/">O nas</a><img src="/branding/logo.svg"><a href="https://github.com/">Source</a>',
    'cs/o-nas/index.html': '<source srcset="/branding/logo.svg 1x, /branding/logo.svg 2x"><a href="/#hero">Home</a>',
    'branding/logo.svg': '<svg/>'
  });
  try { assert.equal(audit(root).errors.length, 0); }
  finally { fs.rmSync(root, { recursive: true, force: true }); }
});

test('does not accept a slash after an asset filename', () => {
  const root = fixture({ 'index.html': '<img src="/assets/missing.png/">' });
  try { assert.equal(audit(root).errors.length, 1); }
  finally { fs.rmSync(root, { recursive: true, force: true }); }
});
