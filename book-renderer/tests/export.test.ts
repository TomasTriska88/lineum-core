import { test, expect } from '@playwright/test';
import { execSync } from 'child_process';
import path from 'path';
import fs from 'fs';

test.describe('Export Pipeline Architecture', () => {

  test('Export script correctly wipes the root exports folder and isolates book folders', async () => {
    // Timeout buffer for the lightweight node process
    test.setTimeout(5000); 

    const exportsDir = path.join(process.cwd(), 'exports');

    // 1. Manually inject an orphan dummy file to prove wiping logic operates correctly
    if (!fs.existsSync(exportsDir)) {
      fs.mkdirSync(exportsDir, { recursive: true });
    }
    const dummyFile = path.join(exportsDir, 'orphan.txt');
    fs.writeFileSync(dummyFile, 'Should be erased');

    // 2. Perform a fast mock dry-run (skips chromium boot and dev server connections)
    execSync('node scripts/export-pdf.js --target=ebook --dry-run', { 
        env: { ...process.env, TEST_BOOK: 'foundations' },
        stdio: 'inherit'
    });

    // 3. Verify the orphan was completely blasted from the tree
    expect(fs.existsSync(dummyFile)).toBe(false);

    // 4. Verify book categorization 
    const foundationsDir = path.join(exportsDir, 'foundations');
    const expectedPdfPath = path.join(foundationsDir, 'Foundations-Digital.pdf');
    const expectedCoverPath = path.join(foundationsDir, 'Cover-Foundations-Digital.pdf');

    expect(fs.existsSync(foundationsDir)).toBe(true);
    // Since dry-run just touches TXT payloads to these paths to simulate PDF completion:
    expect(fs.existsSync(expectedPdfPath)).toBe(true);
    expect(fs.existsSync(expectedCoverPath)).toBe(true);
  });
});
