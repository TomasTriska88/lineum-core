'use strict';
/** Public static preview asset consolidation. Science source documents remain unchanged. */
const fs = require('node:fs');
const path = require('node:path');
const { fixLocaleAliases, fixBrandingAssets } = require('./repair-localization.cjs');
const { audit } = require('./check-static-links.cjs');

const ARCHIVAL_REFERENCES = Object.freeze({
  'wiki/docs/verification_checklist.md': 'portal/src/lib/data/docs/verification_checklist.md',
  'wiki/whitepaper/05-validation.md': 'portal/src/lib/data/whitepapers-legacy/05-validation.md',
  'wiki/hydrogen_wave_core/hydrogen_orbital_log.png': 'whitepapers/1-core/experiments/validation/hydrogen_orbital_log.png',
  'wiki/output/spec6_false_s41_figure0_canonical.png': 'output_wp/archive/spec6_false_s41_20260215_023130/spec6_false_s41_figure0_canonical.png',
  'wiki/output/spec6_false_s41_lineum_report.html': 'output_wp/archive/spec6_false_s41_20260215_023130/spec6_false_s41_lineum_report.html',
  'wiki/elements/proton.png': 'elements/proton.png',
  'wiki/elements/transverson.png': 'elements/transverson.png',
  'wiki/elements/antitransverson.png': 'elements/antitransverson.png',
  'wiki/assets/cymatic_atom_visualization_1772669049825.png': 'whitepapers/assets/cymatic_atom_visualization_1772669049825.png',
  'wiki/assets/cymatic_hydrogen_1772671292243.png': 'whitepapers/assets/cymatic_hydrogen_1772671292243.png',
  'wiki/assets/cymatic_carbon_1772671312972.png': 'whitepapers/assets/cymatic_carbon_1772671312972.png',
  'wiki/assets/cymatic_oxygen_1772671326730.png': 'whitepapers/assets/cymatic_oxygen_1772671326730.png',
  'wiki/assets/cymatic_iron_1772671340188.png': 'whitepapers/assets/cymatic_iron_1772671340188.png',
  'wiki/assets/cymatic_uranium_1772671352750.png': 'whitepapers/assets/cymatic_uranium_1772671352750.png'
});
const PREFIXES = ['', 'cs/', 'de/', 'ja/'];
function checkedPath(root, relative) {
  const resolved = path.resolve(root, relative);
  if (resolved !== root && !resolved.startsWith(root + path.sep)) throw new Error('Unsafe path: ' + relative);
  return resolved;
}
function copyPublicArchiveAssets(site, repository) {
  let copied = 0;
  for (const [target, origin] of Object.entries(ARCHIVAL_REFERENCES)) {
    const source = checkedPath(repository, origin);
    if (!fs.existsSync(source) || !fs.statSync(source).isFile()) {
      throw new Error('Referenced original asset missing from repository: ' + origin);
    }
    if (fs.statSync(source).size > 25 * 1024 * 1024) throw new Error('Asset exceeds Cloudflare Pages file limit: ' + origin);
    for (const prefix of PREFIXES) {
      const dest = checkedPath(site, prefix + target);
      fs.mkdirSync(path.dirname(dest), { recursive: true });
      fs.copyFileSync(source, dest);
      copied++;
    }
  }
  // Keep the historical HTML report self-contained: it references CSV plots,
  // figures and GIFs by relative filenames, not only the report HTML itself.
  const report = 'wiki/output/spec6_false_s41_lineum_report.html';
  const reportSource = checkedPath(repository, ARCHIVAL_REFERENCES[report]);
  const originalHtml = fs.readFileSync(reportSource, 'utf8');
  const resourcePattern = /<(?:a|img)\b[^>]*?(?:href|src)=(['"])(.*?)\1/gi;
  const reportFolder = path.dirname(reportSource);
  for (const match of originalHtml.matchAll(resourcePattern)) {
    const raw = match[2];
    if (/^(?:[a-z][a-z0-9+.-]*:|\/\/|#)/i.test(raw)) continue;
    const rel = decodeURIComponent(raw.split(/[?#]/, 1)[0]);
    if (!rel || rel === '.') continue;
    const asset = checkedPath(reportFolder, rel);
    if (!fs.existsSync(asset) || !fs.statSync(asset).isFile()) {
      throw new Error('The HTML audit report references a missing original file: ' + rel);
    }
    if (fs.statSync(asset).size > 25 * 1024 * 1024) throw new Error('Report asset exceeds Cloudflare Pages file limit: ' + rel);
    for (const prefix of PREFIXES) {
      const destination = checkedPath(site, path.join(prefix, 'wiki', 'output', rel));
      fs.mkdirSync(path.dirname(destination), { recursive: true });
      fs.copyFileSync(asset, destination);
      copied++;
    }
  }
  return copied;
}
function finalizePresentation(siteDir, repositoryDir) {
  const site = path.resolve(siteDir);
  const repository = path.resolve(repositoryDir);
  if (!fs.existsSync(path.join(site, 'index.html'))) throw new Error('Missing static homepage');
  const aliases = fixLocaleAliases(site);
  const branding = fixBrandingAssets(site);
  const assets = copyPublicArchiveAssets(site, repository);
  const check = audit(site);
  if (check.errors.length) {
    const first = check.errors.slice(0, 12);
    throw new Error(`Static preview has ${check.errors.length} broken references: ${JSON.stringify(first)}`);
  }
  return { pages: check.htmlPages, brokenReferences: 0, aliasesCreated: aliases.length, brandingCopied: branding, archiveFilesCopied: assets };
}
if (require.main === module) {
  try {
    const [siteDir, repositoryDir] = process.argv.slice(2);
    if (!siteDir || !repositoryDir) throw new Error('Usage: node finalize-presentation.cjs <output-directory> <repository-root>');
    console.log(JSON.stringify(finalizePresentation(siteDir, repositoryDir), null, 2));
  } catch(error) { console.error(error); process.exitCode = 1; }
}
module.exports = { finalizePresentation, copyPublicArchiveAssets, ARCHIVAL_REFERENCES };
