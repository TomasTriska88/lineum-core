import { chromium } from 'playwright';

(async () => {
  console.log('Initializing PDF visual renderer...');
  const browser = await chromium.launch();
  const page = await (await browser.newContext()).newPage();

  // Enforce SCREEN mode -> bypass explicit @media print fallback scaling
  await page.emulateMedia({ media: 'screen' });

  console.log('Loading export mode on local development server...');
  await page.goto('http://localhost:5173/?export=true', { waitUntil: 'networkidle' });

  // Await web font loading (Merriweather/Inter) and local hero images
  await page.waitForTimeout(3000);

  console.log('Printing to lineum-book-level1.pdf preserving exact background styling...');
  await page.pdf({
    path: 'lineum-book-level1.pdf',
    printBackground: true,     // Mandatory for Lineum Dark Identity
    format: 'A4',              
    margin: { top: 0, right: 0, bottom: 0, left: 0 } 
  });

  await browser.close();
  console.log('✅ Export successful (deterministic screen layout secured).');
})().catch(err => {
  console.error(err);
  process.exit(1);
});
