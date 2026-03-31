import { test, expect } from '@playwright/test';
import { level1Concepts } from '../src/lib/data/concepts';

test.describe('Lineum Book Renderer - Layout & Content Integrity', () => {

  test('Page loads without horizontal overflow (CSS Margins verification)', async ({ page }) => {
    await page.goto('/');
    await page.click('text=Single Page');
    const bodyWidth = await page.evaluate(() => document.body.scrollWidth);
    const windowWidth = await page.evaluate(() => window.innerWidth);
    expect(bodyWidth).toBeLessThanOrEqual(windowWidth);
    
    // Verify Front Matter presence
    await expect(page.locator('text=LINEUM CORE').first()).toBeVisible();
    await expect(page.locator('text=Math You Can See').first()).toBeVisible();
    await expect(page.locator('text=Imprint / Legal').first()).toBeVisible();
    await expect(page.locator('text=Contents').first()).toBeVisible();
    await expect(page.locator('text=Preface').first()).toBeVisible();
  });

  test('Content Integrity: 100% of defined concepts are rendered with all sections', async ({ page }) => {
    await page.goto('/');
    
    // Switch to single view
    await page.click('text=Single Page');
    
    // Make sure we have 15 concepts
    expect(level1Concepts.length).toBe(15);
    
    for (const concept of level1Concepts) {
      // Each concept should have its H2 title rendered (excluding raw latex due to KaTeX)
      const baseTitle = concept.title.split('(')[0].trim();
      const titleLocator = page.locator('h2', { hasText: baseTitle }).first();
      await expect(titleLocator).toBeVisible();
      
      const hookLocator = page.locator('p.concept-hook').filter({ hasText: concept.hook }).first();
      await expect(hookLocator).toBeVisible();
      
      if (concept.aha !== "") {
        await expect(page.locator('.aha-box p', { hasText: concept.aha }).first()).toBeVisible();
      }
      
      // Check the logical blocks
      await expect(page.locator('h4.run-in-header', { hasText: 'What it is' }).nth(level1Concepts.indexOf(concept))).toBeVisible();
      await expect(page.locator('h4.run-in-header', { hasText: 'How to solve' }).nth(level1Concepts.indexOf(concept))).toBeVisible();
      await expect(page.locator('h4.run-in-header', { hasText: 'Why it works' }).nth(level1Concepts.indexOf(concept))).toBeVisible();
      await expect(page.locator('h4.summary-label', { hasText: 'Summary' }).nth(level1Concepts.indexOf(concept))).toBeVisible();
    }
  });

  test('Images: All concepts must expose an IMG or Placeholder with a data-prompt attribute', async ({ page }) => {
    await page.goto('/');
    await page.click('text=Single Page');
    
    for (const concept of level1Concepts) {
       // Search for either the real <img> hero or the placeholder explicitly storing the exact prompt
       const promptHost = page.locator(`[data-prompt="${concept.image.prompt}"]`).first();
       await expect(promptHost).toBeVisible();
    }
  });

  test('Print mode establishes CSS page breaks correctly', async ({ page }) => {
    await page.goto('/');
    await page.click('text=Preview Print PDF');
    const pages = page.locator('.page');
    // 4 Front matter pages + 15 spreads (30 pages) = 34 pages expected
    const count = await pages.count();
    expect(count).toBeGreaterThanOrEqual(34); 
  });

  test('Math Rendering: KaTeX successfully transformed inline and block math', async ({ page }) => {
    await page.goto('/');
    await page.click('text=Single Page');
    
    // Check if katex nodes are present
    const katexNodes = page.locator('.katex');
    const katexCount = await katexNodes.count();
    expect(katexCount).toBeGreaterThan(0);
    
    // Extract raw text and ensure no broken latex tokens are dangling
    const bodyText = await page.locator('body').innerText();
    expect(bodyText).not.toContain('$$');
    expect(bodyText).not.toContain('\\cdot');
    // Exclude checking raw $ because it might match legitimate currency or regex artifacts if any exist. But inside prose-p it should not be pure math delimiters:
    const proseText = await page.locator('.prose-p').allInnerTexts();
    for (const text of proseText) {
       expect(text).not.toContain('$$');
       expect(text).not.toContain('\\sqrt');
    }
  });
});
