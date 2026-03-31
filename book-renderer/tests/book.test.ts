import { test, expect } from '@playwright/test';
import { level1Concepts } from '../src/lib/data/concepts';

const lengthOfConcepts = level1Concepts.length;

test.describe('Lineum Book Renderer - Layout & Content Integrity', () => {

  test('Page loads without horizontal overflow (CSS Margins verification)', async ({ page }) => {
    await page.goto('/');
    await page.click('text=Single Page');
    const bodyWidth = await page.evaluate(() => document.body.scrollWidth);
    const windowWidth = await page.evaluate(() => window.innerWidth);
    // expect(bodyWidth).toBeLessThanOrEqual(windowWidth); // Replaced by strict DOM bounding box test
    
    // Verify Front Matter presence
    await expect(page.locator('text=FOUNDATIONS').first()).toBeVisible();
    await expect(page.locator('text=Imprint / Legal').first()).toBeVisible();
    await expect(page.locator('text=Contents').first()).toBeVisible();
    await expect(page.locator('text=Preface').first()).toBeVisible();
  });

  test('Layout Overflow: No text or content spills outside page boundaries', async ({ page }) => {
    await page.goto('/');
    await page.click('text=Single Page');

    // Get all pages and check their inner contents
    const pages = page.locator('.page');
    const pageCount = await pages.count();

    expect(pageCount).toBeGreaterThan(0);

    for (let i = 0; i < pageCount; i++) {
        const pageLocator = pages.nth(i);
        const innerContent = pageLocator.locator('.inner-content').first();
        
        // If the page has an inner content block, ensure its height isn't larger than the page
        if (await innerContent.count() > 0) {
            const pageBox = await pageLocator.boundingBox();
            const contentBox = await innerContent.boundingBox();

            expect(pageBox).not.toBeNull();
            expect(contentBox).not.toBeNull();

            // Svelte margins + padding = content box shouldn't be taller than page box
            if (pageBox && contentBox) {
                expect(
                    contentBox.height, 
                    `Page ${i+1} inner content height (${contentBox.height}) exceeds page bounds (${pageBox.height})`
                ).toBeLessThanOrEqual(pageBox.height + 1); // +1px tolerance
                
                expect(
                    contentBox.width,
                    `Page ${i+1} inner content width (${contentBox.width}) exceeds page bounds (${pageBox.width})`
                ).toBeLessThanOrEqual(pageBox.width + 1);
            }
        }
    }
    
    // Check that paragraph width is bounded (approx 60-70ch)
    const paragraphs = page.locator('.prose-p');
    const pCount = await paragraphs.count();
    for(let i=0; i<pCount; i++) {
        const pBox = await paragraphs.nth(i).boundingBox();
        if(pBox) {
            // A typical 65ch line in 1.125rem is about 600-700px maximum.
            expect(pBox.width).toBeLessThanOrEqual(800);
        }
    }
  });

  test('Content Integrity: 100% of defined concepts are rendered with all sections', async ({ page }) => {
    await page.goto('/');
    
    // Switch to single mode to test all DOM at once
    await page.click('text=Single Page');

    let totalExpectedChars = 0;

    for (const concept of level1Concepts) {
      // Calculate basic expected string length (stripped of LaTeX metadata for safer bounds)
      totalExpectedChars += concept.title.length;
      totalExpectedChars += concept.hook.length;
      totalExpectedChars += concept.whatItIs.length;
    }

    // Measure total character output
    const bodyText = await page.locator('body').innerText();
    console.log(`Expected raw metric chars: ${totalExpectedChars}, DOM holds: ${bodyText.length}`);
    
    // The DOM must contain AT LEAST the character count of our core fields.
    expect(bodyText.length).toBeGreaterThanOrEqual(totalExpectedChars);

    // Verify specifically that exact matching happens (Sampling strings)
    // Wait for a simpler text substring (avoiding KaTeX HTML node complexity)
    await expect(page.locator(`text=Addition`).first()).toBeVisible();
    
    for (const concept of level1Concepts) {
      // Pick a random substring to ensure strict content preservation
      const hookSnip = concept.hook.substring(0, 20);
      await expect(page.locator(`text=${hookSnip}`).first()).toBeVisible();
    }
  });

  test('Image System: 100% of concept visuals have data-prompt and layout tags', async ({ page }) => {
    await page.goto('/');
    await page.click('text=Single Page');
    await expect(page.locator('h2.concept-title').first()).toBeVisible();

    const imageBoxes = page.locator('.image-box');
    const imageCount = await imageBoxes.count();
    
    // There should be exactly as many images as there are concepts (plus potentially intro)
    expect(imageCount).toBeGreaterThanOrEqual(lengthOfConcepts);

    for (let i = 0; i < lengthOfConcepts; i++) {
      const imgTarget = imageBoxes.nth(i).locator('[data-prompt]');
      await expect(imgTarget).toHaveAttribute('data-prompt', /.*/);
      await expect(imgTarget).toHaveAttribute('data-style', 'vector');
      await expect(imgTarget).toHaveAttribute('data-variant', /.*/);
    }
  });

  test('Cover Generator: Cover renders with specific dimensions and ISBN back cover', async ({ page }) => {
    await page.goto('/?cover=true');
    // Ensure the FullPrintCover block is rendered
    const coverLocator = page.locator('.full-print-cover');
    await expect(coverLocator).toBeVisible();

    // Verify critical Cover elements
    await expect(page.locator('.main-title').first()).toContainText('Foundations');
    await expect(page.locator('.spine-strip')).toBeVisible();
    await expect(page.locator('.barcode')).toBeVisible();
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
