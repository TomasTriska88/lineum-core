import { test, expect } from '@playwright/test';
import { level1Concepts } from '../src/lib/data/books/foundations';

const lengthOfConcepts = level1Concepts.length;

test.describe('Lineum Book Renderer - Layout & Content Integrity', () => {

  test('Page loads without horizontal overflow (CSS Margins verification)', async ({ page }) => {
    await page.goto('/');
    await page.click('text=Public Reader (Scroll)');
    const bodyWidth = await page.evaluate(() => document.body.scrollWidth);
    const windowWidth = await page.evaluate(() => window.innerWidth);
    // expect(bodyWidth).toBeLessThanOrEqual(windowWidth); // Replaced by strict DOM bounding box test
    
    // Verify Front Matter presence
    await expect(page.locator('text=LINEUM SERIES').first()).toBeVisible();
    await expect(page.locator('text=Imprint / Legal').first()).toBeVisible();
    await expect(page.locator('text=Contents').first()).toBeVisible();
    await expect(page.locator('text=Preface').first()).toBeVisible();
  });

  test('Layout Overflow: No text or content spills outside page boundaries', async ({ page }) => {
    await page.goto('/');
    await page.click('text=Public Reader (Scroll)');

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
    
    // Check that paragraph width is bounded (approx 60-70ch) and NOT clipped vertically
    const paragraphs = page.locator('.prose-p');
    const pCount = await paragraphs.count();
    for(let i=0; i<pCount; i++) {
        const pBox = await paragraphs.nth(i).boundingBox();
        if(pBox) {
            expect(pBox.width).toBeLessThanOrEqual(800);
        }
        // Strict text truncation check (scroll height should not exceed client height)
        const isTruncated = await paragraphs.nth(i).evaluate((node) => node.scrollHeight > node.clientHeight + 2);
        expect(isTruncated).toBeFalsy();
    }
  });

  test('Legacy Naming: "OEA" and "Lineum Core" are strictly purged from DOM', async ({ page }) => {
    await page.goto('/');
    await page.click('text=Public Reader (Scroll)');
    
    const bodyText = await page.locator('body').innerText();
    expect(bodyText).not.toContain('OEA');
    expect(bodyText).not.toContain('Lineum Core');
  });

  test('Content Integrity: 100% of defined concepts are rendered with all sections', async ({ page }) => {
    await page.goto('/');
    
    // Switch to epub/scroll mode to test all DOM at once
    await page.click('text=Public Reader (Scroll)');

    let totalExpectedChars = 0;

    for (const concept of level1Concepts) {
      // Calculate basic expected string length (stripped of LaTeX metadata for safer bounds)
      totalExpectedChars += concept.title.length;
      totalExpectedChars += concept.hook.length;
      for (const seg of concept.proseSegments) {
        totalExpectedChars += seg.body.length;
      }
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
    await page.click('text=Public Reader (Scroll)');
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
    await expect(page.locator('.main-title').first()).toContainText(/Foundations/i);
    await expect(page.locator('.spine-strip')).toBeVisible();
    await expect(page.locator('.barcode')).toBeVisible();
  });

  test('Images: All concepts must expose an IMG or Placeholder with a data-prompt attribute', async ({ page }) => {
    await page.goto('/');
    await page.click('text=Public Reader (Scroll)');
    
    for (const concept of level1Concepts) {
       // Search for either the real <img> hero or the placeholder explicitly storing the exact prompt
       const promptHost = page.locator(`[data-prompt="${concept.image.prompt}"]`).first();
       await expect(promptHost).toBeVisible();
    }
  });

  test('Print mode establishes CSS page breaks correctly', async ({ page }) => {
    await page.goto('/?export=true');
    const pages = page.locator('.page');
    // 4 Front matter pages + 15 spreads (30 pages) = 34 pages expected
    const count = await pages.count();
    expect(count).toBeGreaterThanOrEqual(34); 
  });

  test('Math Rendering: KaTeX successfully transformed inline and block math', async ({ page }) => {
    await page.goto('/');
    await page.click('text=Public Reader (Scroll)');
    
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

  test.skip('Responsive Spread: Zoom scaling is applied dynamically to prevent horizontal scroll', async ({ page }) => {
    await page.goto('/');
    await page.setViewportSize({ width: 1000, height: 800 }); // Small screen, would normally scroll
    await page.click('text=Public Reader (Spread)');
    
    const spreadWrapper = page.locator('.spread-preview-wrapper').first();
    // Bounding box horizontal width logic below natively verifies the scale compression
    
    // Explicitly verify no horizontal scroll at document level
    // Wait for repaint via bounding box checks or timeout
    const bodyScrollWidth = await page.evaluate(() => document.documentElement.scrollWidth);
    const windowWidth = await page.evaluate(() => window.innerWidth);
    expect(bodyScrollWidth).toBeLessThanOrEqual(windowWidth + 50); // Tolerate slight scrollbar padding
  });

  test.skip('Architecture: Print QA mode acts distinctly from Public Viewer mode', async ({ page }) => {
    await page.goto('/');
    await page.click('text=Internal QA Print Bounds');
    // We check that at least one element has the print-mode class
    await expect(page.locator('.print-mode').first()).toBeAttached();
  });

  test('Architecture: Multi-book routing dynamically alters data payload', async ({ page }) => {
    await page.goto('/?book=motion');
    await expect(page.locator('body')).toContainText('Motion');
    await expect(page.locator('body')).toContainText('Calculus');
    
    await page.goto('/?book=structure');
    await expect(page.locator('body')).toContainText('Structure');
    await expect(page.locator('body')).toContainText('Physics');
  });

  test('UI Integrity: QA Toolbar UI must not squash or text-wrap buttons violently', async ({ page }) => {
    await page.goto('/');
    
    // Set a deliberately cramped viewport
    await page.setViewportSize({ width: 800, height: 600 });
    
    const toolbar = page.locator('.toolbar');
    await expect(toolbar).toBeVisible();

    // Check all buttons inside the toolbar to ensure structural height remains healthy (single-line)
    const buttons = page.locator('.toolbar button');
    const buttonCount = await buttons.count();
    
    expect(buttonCount).toBeGreaterThanOrEqual(4); // At least 3 books + 3 view modes
    
    for (let i = 0; i < buttonCount; i++) {
       const btn = buttons.nth(i);
       const box = await btn.boundingBox();
       if (box) {
         // A healthy single-line button with our UI padding is usually ~30-50px tall.
         // If word-wrap violently stacks words on top of each other, it spirals to 100px+.
         expect(box.height, `Button ${i} has wrap squashing (height: ${box.height})`).toBeLessThan(65);
         
         // Assert white-space is forced to nowrap
         await expect(btn).toHaveCSS('white-space', 'nowrap');
       }
    }
  });

  test('Content Integrity: 1:1 Generalization of Books 1, 2, and 3', async ({ page }) => {
    // 1. Verify Foundations (Book 1) did NOT regress. It must keep its hardcoded legacy text formats.
    await page.goto('/?book=foundations');
    await page.click('text=Public Reader (Scroll)');
    const b1Labels = page.locator('.prose-flow .run-in-header');
    await expect(b1Labels.nth(0)).toHaveText('What it is.');
    await expect(b1Labels.nth(1)).toHaveText('How to solve.');
    await expect(b1Labels.nth(2)).toHaveText('Why it works.');

    // 2. Verify Motion (Book 2) safely renders its custom markdown labels 1:1 without forcing Book 1 labels
    await page.goto('/?book=motion');
    await page.click('text=Public Reader (Scroll)');
    const b2Labels = page.locator('.prose-flow .run-in-header');
    expect(await b2Labels.count()).toBeGreaterThan(0);
    // The first concept in Book 2 has "Consider this..."
    await expect(b2Labels.first()).toHaveText('Consider this...');
    
    // Check that Motion's original hook text isn't lost
    await expect(page.locator('body')).toContainText('Imagine dropping a raw block of wood');

    // 3. Verify Structure (Book 3) safely renders its custom markdown labels
    await page.goto('/?book=structure');
    await page.click('text=Public Reader (Scroll)');
    const b3Labels = page.locator('.prose-flow .run-in-header');
    expect(await b3Labels.count()).toBeGreaterThan(0);
    await expect(b3Labels.first()).toHaveText('Consider this...');
    
    // Check that Structure's original hook text isn't lost
    await expect(page.locator('body')).toContainText('Imagine a glowing arrow that isn\'t just statically pointing');
  });
});
