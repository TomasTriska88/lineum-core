// Export a static brochure and wiki without deploying the Node runtime or Python API.
const fs = require('node:fs');
const path = require('node:path');
const { spawnSync } = require('node:child_process');
const root = path.resolve(__dirname, '..');
const source = path.join(root, '.svelte-kit', 'output');
const destination = path.join(root, 'build-presentation');
const env = { ...process.env, VITE_LINEUM_PRESENTATION_ONLY: '1',
  PUBLIC_ENABLE_API_SOLUTIONS: 'false', PUBLIC_SIMULACRUM_URL: '/wiki' };

function run(args) {
  const cmd = process.platform === 'win32' ? 'npm.cmd' : 'npm';
  const p = spawnSync(cmd, args, { cwd: root, env, stdio: 'inherit' });
  if (p.error) throw p.error;
  if (p.status !== 0) process.exit(p.status || 1);
}
function files(folder) {
  if (!fs.existsSync(folder)) return [];
  const pending = [folder], result = [];
  while (pending.length) {
    const current = pending.pop();
    for (const dirent of fs.readdirSync(current, { withFileTypes: true })) {
      const full = path.join(current, dirent.name);
      if (dirent.isDirectory()) pending.push(full);
      else if (dirent.isFile()) result.push(full);
    }
  }
  return result;
}
function copy(sourceFolder, filter) {
  for (const file of files(sourceFolder)) {
    const relative = path.relative(sourceFolder, file);
    if (!filter(relative)) continue;
    const to = path.join(destination, relative);
    fs.mkdirSync(path.dirname(to), { recursive: true });
    fs.copyFileSync(file, to);
  }
}
function allowedPage(relative) {
  const normalized = relative.replace(/\\/g, '/').replace(/(^|\/)index\.html$/, '$1')
    .replace(/\.html$/, '').replace(/\/$/, '');
  if (!normalized) return true;
  const parts = normalized.split('/');
  if (['cs', 'de', 'ja', 'en'].includes(parts[0])) parts.shift();
  if (parts.length === 1) {
    return ['about', 'brand', 'codex', 'privacy', 'support', 'wiki'].includes(parts[0]);
  }
  return parts.length === 2 && parts[0] === 'wiki';
}

run(['run', 'sync']);
run(['exec', '--', 'vite', 'build']);
if (!fs.existsSync(path.join(source, 'client')) ||
    !fs.existsSync(path.join(source, 'prerendered', 'pages'))) {
  throw new Error('Prerendered SvelteKit pages missing; refusing to publish');
}
fs.rmSync(destination, { recursive: true, force: true });
fs.mkdirSync(destination, { recursive: true });
copy(path.join(source, 'client'), () => true);
copy(path.join(source, 'prerendered', 'pages'), allowedPage);
copy(path.join(source, 'prerendered', 'dependencies'),
  relative => !relative.replace(/\\/g, '/').startsWith('api/'));
const images = path.join(root, 'src', 'lib', 'data', 'source');
for (const file of files(images)) {
  const relative = path.relative(images, file);
  if (!/\.(png|jpe?g|webp|svg|gif)$/i.test(relative)) continue;
  const to = path.join(destination, 'data', 'source', relative);
  fs.mkdirSync(path.dirname(to), { recursive: true });
  fs.copyFileSync(file, to);
}
for (const page of ['index.html', 'about', 'brand', 'codex', 'privacy', 'support', 'wiki']) {
  const candidates = page === 'index.html' ? ['index.html'] : [page + '/index.html', page + '.html'];
  if (!candidates.some(p => fs.existsSync(path.join(destination, p)))) {
    throw new Error('Required presentation page missing: ' + page);
  }
}
const html = files(destination).filter(file => file.endsWith('.html'));
if (!html.some(file => path.relative(destination, file).replace(/\\/g, '/').startsWith('wiki/'))) {
  throw new Error('No wiki document pages exported');
}
const homepage = fs.readFileSync(path.join(destination, 'index.html'), 'utf8');
if (homepage.includes('http://127.0.0.1:8000/redoc')) {
  throw new Error('Local API development link leaked into public navigation');
}
fs.writeFileSync(path.join(destination, 'robots.txt'), 'User-agent: *\nDisallow: /\n');
console.log('Verified static presentation: ' + html.length + ' HTML pages');
