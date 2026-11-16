'use strict';
// Proof of concept for the generated presentation artifact only.
// Never claim that an untranslated page has been translated.
const fs = require('node:fs');
const path = require('node:path');
const htmlEscape = value => value.replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const translations = {
  cs: { lang: 'cs', title: 'Stránka zatím není v češtině', text: 'Tato část webu zatím nemá ověřenou českou verzi. Anglický obsah je k dispozici bez přihlášení.', open: 'Otevřít anglickou stránku' },
  de: { lang: 'de', title: 'Seite noch nicht auf Deutsch verfügbar', text: 'Für diesen Bereich gibt es noch keine überprüfte deutsche Übersetzung. Die englische Seite ist öffentlich verfügbar.', open: 'Englische Seite öffnen' },
  ja: { lang: 'ja', title: 'このページは日本語未対応です', text: 'このページの日本語版はまだ確認されていません。英語のページをご覧ください。', open: '英語のページを開く' }
};
const redirectAliases = {
  'cs/': '/',
  'de/': '/',
  'ja/': '/',
  'cs/o-nas/': '/about/',
  'de/ueber-uns/': '/about/',
  'cs/podpora/': '/support/',
  'cs/znalostni-baze/': '/wiki/',
  'de/wissensdatenbank/': '/wiki/'
};
function safeDest(root, relative) {
  const result = path.resolve(root, relative);
  if (!result.startsWith(root + path.sep) && result !== root) throw new Error('Unsafe path');
  return result;
}
function fixLocaleAliases(root) {
  const missing=[];
  for (const [relative, target] of Object.entries(redirectAliases)) {
    const destination=safeDest(root, path.join(relative, 'index.html'));
    if (fs.existsSync(destination)) continue;
    const exists = fs.existsSync(safeDest(root,path.join(target.replace(/^\//, ''), 'index.html')));
    if(!exists) throw new Error('Missing English fallback page: '+target);
    const t = translations[relative.split('/')[0]];
    const content=`<!doctype html><html lang="${t.lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex"><title>${t.title} | Lineum</title><style>body{background:#0b1019;color:#eff7fc;font:18px/1.6 system-ui,sans-serif;margin:0;min-height:100vh;display:grid;place-items:center}main{max-width:540px;padding:32px}a{color:#8ee8ff;font-weight:bold}h1{font-size:1.6em}</style></head><body><main><h1>${t.title}</h1><p>${t.text}</p><p><a href="${htmlEscape(target)}">${t.open}</a></p></main></body></html>\n`;
    fs.mkdirSync(path.dirname(destination),{recursive:true});
    fs.writeFileSync(destination,content);
    missing.push(relative);
  }
  return missing;
}
function fixBrandingAssets(root) {
  let copied=0;
  const assetRoot=safeDest(root,'branding');
  for(const lang of ['cs','de','ja']) {
    for(const name of fs.readdirSync(assetRoot)) {
      const source=path.join(assetRoot,name);
      if (!fs.statSync(source).isFile()) continue;
      const target=safeDest(root,path.join(lang,'branding',name));
      if(fs.existsSync(target)) continue;
      fs.mkdirSync(path.dirname(target),{recursive:true});
      fs.copyFileSync(source,target);
      copied++;
    }
  }
  return copied;
}
if(require.main===module){const root=path.resolve(process.argv[2]||'.'); const aliases=fixLocaleAliases(root); const brand=fixBrandingAssets(root);console.log(JSON.stringify({createdLocalizedFallbackPages:aliases,brandAssetsCopied:brand},null,2));}
module.exports={fixLocaleAliases,fixBrandingAssets,redirectAliases};
