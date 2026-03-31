import { chromium } from 'playwright';
import path from 'path';
import fs from 'fs';
import { execSync } from 'child_process';

// Node arguments parsing
const args = process.argv.slice(2);
const targetArg = args.find(a => a.startsWith('--target='));
const specificTarget = targetArg ? targetArg.split('=')[1] : 'all';
const isDryRun = args.includes('--dry-run');

// Fixed Export Configurations mapped to user requirements
const configs = {
  'print-global': { // 6x9" with 3mm bleed
    width: '158mm', // 152mm + 3mm left + 3mm right
    height: '235mm', // 229mm + 3mm top + 3mm bottom
    filenameSuffix: 'Print-6x9.pdf',
    printBackground: true,
    scale: 1
  },
  'print-eu': { // B5 with 3mm bleed
    width: '182mm', // 176mm + 3mm left + 3mm right
    height: '256mm', // 250mm + 3mm top + 3mm bottom
    filenameSuffix: 'Print-B5.pdf',
    printBackground: true,
    scale: 1 
  },
  'ebook': { // Digital display (6x9 default, RGB, no bleeds)
    width: '152mm',
    height: '229mm',
    filenameSuffix: 'Digital.pdf',
    printBackground: true,
    scale: 1
  }
};

const defaultBooks = ['foundations', 'motion', 'structure'];

const activeTargets = specificTarget === 'all' 
  ? Object.keys(configs) 
  : [specificTarget];

for (const t of activeTargets) {
  if (!configs[t]) {
    console.error(`Invalid target: ${t}. Allowed: print-global, print-eu, ebook, all`);
    process.exit(1);
  }
}

async function exportTarget(target, bookId) {
  const conf = configs[target];
  const bookNameCap = bookId.charAt(0).toUpperCase() + bookId.slice(1);
  const targetFilename = `${bookNameCap}-${conf.filenameSuffix}`;
  
  // Ensure book-specific export directory exists
  const outDirStr = path.join(process.cwd(), 'exports', bookId);
  if (!fs.existsSync(outDirStr)) {
    fs.mkdirSync(outDirStr, { recursive: true });
  }

  console.log(`\n================================`);
  console.log(`Initializing PDF Production Pipeline [Book: ${bookNameCap} | Target: ${target}]...`);
  
  if (isDryRun) {
    console.log(`[DRY RUN] Simulating physical page generation to ${targetFilename}...`);
    const outFile = path.join(outDirStr, targetFilename);
    const coverFile = path.join(outDirStr, `Cover-${targetFilename}`);
    fs.writeFileSync(outFile, 'DRY RUN PDF BODY');
    fs.writeFileSync(coverFile, 'DRY RUN PDF COVER');
    console.log(`[DRY RUN] 🚀 Pipeline Completed: ${outDirStr}\n`);
    return;
  }

  const browser = await chromium.launch();
  const page = await browser.newPage();
  
  const devServerUrl = `http://localhost:5173/?export=true&format=${target}&book=${bookId}`;
  console.log(`Loading Book Architecture from ${devServerUrl}`);
  
  await page.goto(devServerUrl, { waitUntil: 'networkidle' });
  
  // Extra pause for KaTeX font loading (embedded fonts synchronization factor)
  await page.waitForTimeout(2000);
  
  const outFile = path.join(outDirStr, targetFilename);
  console.log(`Generating physical pages to ${targetFilename} (Dimensions: ${conf.width} x ${conf.height})...`);
  
  await page.pdf({
    path: outFile,
    width: conf.width,
    height: conf.height,
    printBackground: conf.printBackground,
    scale: conf.scale,
    displayHeaderFooter: false,
    margin: { top: '0', right: '0', bottom: '0', left: '0' }
  });
  
  console.log(`✅ Book Body Extracted Successfully.`);

  // Export Cover
  console.log(`Loading Cover Assembly...`);
  const coverUrl = `http://localhost:5173/?cover=true&format=${target}&book=${bookId}`;
  await page.goto(coverUrl, { waitUntil: 'networkidle' });
  await page.waitForTimeout(1000);
  
  const coverFile = path.join(outDirStr, `Cover-${targetFilename}`);
  
  // Covers have dynamic widths, we can let Playwright use preferCSSPageSize if possible
  // However, Playwright 'preferCSSPageSize' requires @page CSS rules. Since our Svelte DOM sets specific mm pixels on .full-print-cover,
  // we can measure the DOM element and pass exactly those pixels to page.pdf() width!
  
  const coverDimensions = await page.evaluate(() => {
     const c = document.querySelector('.full-print-cover');
     return c ? { w: c.getBoundingClientRect().width, h: c.getBoundingClientRect().height } : null;
  });

  if (coverDimensions) {
    console.log(`Cover math calculated (Spine + Front + Back): ${coverDimensions.w}px width`);
    await page.pdf({
      path: coverFile,
      width: `${coverDimensions.w}px`,
      height: `${coverDimensions.h}px`,
      printBackground: true,
      margin: { top: 0, right: 0, bottom: 0, left: 0 }
    });
    console.log(`✅ Book Cover Extracted Successfully.`);
  }

  await browser.close();
  console.log(`🚀 Pipeline Completed: ${outDirStr}\n`);
}

async function runBatch() {
  const exportsDir = path.join(process.cwd(), 'exports');
  
  // Wipe the exports directory at the start of the batch
  if (!process.env.SKIP_WIPE && fs.existsSync(exportsDir)) {
    console.log('🧹 Wiping existing exports directory...');
    try {
      // Safely delete the full tree, capturing Windows EBUSY exceptions if files are locked
      fs.rmSync(exportsDir, { recursive: true, force: true });
    } catch (e) {
      console.error(`❌ CRITICAL ERROR: Cannot wipe exports directory. Is a PDF or folder open? Error: ${e.message}`);
      process.exit(1);
    }
  }

  // Allow passing a specific test book if needed
  const targetBooks = process.env.TEST_BOOK ? [process.env.TEST_BOOK] : defaultBooks;

  for (const book of targetBooks) {
    for (const t of activeTargets) {
      await exportTarget(t, book);
    }
  }
  console.log('\n🌟 ALL BOOKS EXPORTED FINISHED');
}

runBatch().catch(console.error);
