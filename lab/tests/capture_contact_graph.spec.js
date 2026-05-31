import { test, expect } from '@playwright/test';
import fs from 'fs';
import path from 'path';

test('capture contact graph screenshots and validate metrics', async ({ page }) => {
    // Increase test timeout to 2 minutes
    test.setTimeout(120000);

    // Listen to browser console and error logs
    page.on('console', msg => console.log('BROWSER LOG:', msg.text()));
    page.on('pageerror', err => console.error('BROWSER ERROR:', err.message));

    // Set viewport size for consistent screenshot aspect ratios
    await page.setViewportSize({ width: 1280, height: 800 });

    // Expose the QA test hook before navigation to enable WebGL preserveDrawingBuffer
    await page.addInitScript(() => {
        window.__playwright_test__ = true;
    });

    // 1. Open Svelte Lab UI
    console.log('Navigating to Lab UI...');
    await page.goto('http://127.0.0.1:5174/');
    
    // 2. Wait for loading screen to disappear
    console.log('Waiting for loader spinner to disappear...');
    await page.waitForSelector('.spinner', { state: 'detached', timeout: 30000 });
    await page.waitForTimeout(1000); // stable hydrate

    // 3. Switch to Contact Graph Tab
    console.log('Switching to CONTACT GRAPH tab...');
    const tabBtn = page.locator('button[data-testid="tab-contact-graph"]');
    await tabBtn.click();
    await expect(tabBtn).toHaveClass(/active/);

    // Enable ContactGraph debug view & show node IDs via UI toggles
    console.log('Enabling ContactGraph debug view and show node IDs...');
    const debugCheckbox = page.locator('input[type="checkbox"]').first();
    await debugCheckbox.check();
    const nodeIdsCheckbox = page.locator('input[type="checkbox"]').nth(1);
    await nodeIdsCheckbox.check();

    // 4. Create target screenshots directory
    const screenshotsDir = 'c:/Projects/lineum-core/research/audits/screenshots/phase_77_contactgraph';
    if (!fs.existsSync(screenshotsDir)) {
        fs.mkdirSync(screenshotsDir, { recursive: true });
    }

    // 5. Capture the warning banner
    console.log('Capturing warning banner...');
    const warningBox = page.locator('.warning-box');
    await warningBox.screenshot({ path: path.join(screenshotsDir, 'warning_banner.png') });

    // Get run selector and list of options
    const runSelector = page.locator('.run-selector');
    const options = await runSelector.locator('option').all();
    const runIds = [];
    for (const opt of options) {
        runIds.push(await opt.getAttribute('value'));
    }
    console.log('Available Run IDs:', runIds);

    // For run 1: capture initial state
    const run1 = runIds[0];
    await runSelector.selectOption(run1);
    await page.waitForFunction((expectedRunId) => {
        return window.engine && window.engine.runId === expectedRunId;
    }, run1, { timeout: 15000 });
    console.log(`Loaded Run: ${run1}`);

    // Log canvas diagnostics
    const canvasInfo = await page.evaluate(() => {
        const container = document.querySelector('.canvas-container');
        const canvas = document.querySelector('canvas');
        return {
            containerHtml: container ? container.innerHTML : 'no container',
            containerRect: container ? container.getBoundingClientRect().toJSON() : null,
            canvasRect: canvas ? canvas.getBoundingClientRect().toJSON() : null,
            canvasWidthAttr: canvas ? canvas.width : null,
            canvasHeightAttr: canvas ? canvas.height : null,
            engineExists: typeof window.engine !== 'undefined'
        };
    });
    console.log('CANVAS DIAGNOSTICS:', canvasInfo);

    // Jump directly to frame 391 where linons are active
    console.log('Jumping to Run 1 frame 391...');
    await page.evaluate(() => {
        if (window.engine) {
            window.engine.isPaused = true;
            window.engine.jumpToFrame(391);
        }
    });
    await page.waitForFunction(() => {
        return window.engine && window.engine.currentFrameIndex === 391;
    }, { timeout: 5000 });

    // Focus camera on active contacts
    await page.evaluate(() => {
        if (window.engine) window.engine.focusOnActiveContacts();
    });

    // Take screenshot of ContactGraph panel & full viewport
    await page.screenshot({ path: path.join(screenshotsDir, 'run1_frame391_full.png') });
    await page.locator('.contact-graph-panel').screenshot({ path: path.join(screenshotsDir, 'run1_frame391_panel.png') });

    // Load Run 3 (birth frame = 228) for long-duration slips/contacts
    const run3 = runIds[2];
    await runSelector.selectOption(run3);
    await page.waitForFunction((expectedRunId) => {
        return window.engine && window.engine.runId === expectedRunId;
    }, run3, { timeout: 15000 });
    console.log(`Loaded Run: ${run3}`);

    // Jump directly to frame 230
    console.log('Jumping to Run 3 frame 230...');
    await page.evaluate(() => {
        if (window.engine) {
            window.engine.isPaused = true;
            window.engine.jumpToFrame(230);
        }
    });
    await page.waitForFunction(() => {
        return window.engine && window.engine.currentFrameIndex === 230;
    }, { timeout: 5000 });

    // Focus camera on active contacts
    await page.evaluate(() => {
        if (window.engine) window.engine.focusOnActiveContacts();
    });

    await page.screenshot({ path: path.join(screenshotsDir, 'run3_frame230_full.png') });
    await page.locator('.contact-graph-panel').screenshot({ path: path.join(screenshotsDir, 'run3_frame230_panel.png') });

    // Jump directly to frame 250 (slips)
    console.log('Jumping to Run 3 frame 250...');
    await page.evaluate(() => {
        if (window.engine) {
            window.engine.isPaused = true;
            window.engine.jumpToFrame(250);
        }
    });
    await page.waitForFunction(() => {
        return window.engine && window.engine.currentFrameIndex === 250;
    }, { timeout: 5000 });

    // Focus camera on active contacts
    await page.evaluate(() => {
        if (window.engine) window.engine.focusOnActiveContacts();
    });
    
    await page.screenshot({ path: path.join(screenshotsDir, 'run3_frame250_full.png') });
    await page.locator('.contact-graph-panel').screenshot({ path: path.join(screenshotsDir, 'run3_frame250_panel.png') });

    // Jump directly to frame 350 (longer duration / component clustering)
    console.log('Jumping to Run 3 frame 350...');
    await page.evaluate(() => {
        if (window.engine) {
            window.engine.isPaused = true;
            window.engine.jumpToFrame(350);
        }
    });
    await page.waitForFunction(() => {
        return window.engine && window.engine.currentFrameIndex === 350;
    }, { timeout: 5000 });

    // Focus camera on active contacts
    await page.evaluate(() => {
        if (window.engine) window.engine.focusOnActiveContacts();
    });

    await page.screenshot({ path: path.join(screenshotsDir, 'run3_frame350_full.png') });
    await page.locator('.contact-graph-panel').screenshot({ path: path.join(screenshotsDir, 'run3_frame350_panel.png') });

    // Load Run 4 (birth frame = 228) for decay/collapse behavior
    const run4 = runIds[3];
    await runSelector.selectOption(run4);
    await page.waitForFunction((expectedRunId) => {
        return window.engine && window.engine.runId === expectedRunId;
    }, run4, { timeout: 15000 });
    console.log(`Loaded Run: ${run4}`);

    // Jump directly to frame 250
    console.log('Jumping to Run 4 frame 250...');
    await page.evaluate(() => {
        if (window.engine) {
            window.engine.isPaused = true;
            window.engine.jumpToFrame(250);
        }
    });
    await page.waitForFunction(() => {
        return window.engine && window.engine.currentFrameIndex === 250;
    }, { timeout: 5000 });

    // Focus camera on active contacts
    await page.evaluate(() => {
        if (window.engine) window.engine.focusOnActiveContacts();
    });

    await page.screenshot({ path: path.join(screenshotsDir, 'run4_frame250_full.png') });
    await page.locator('.contact-graph-panel').screenshot({ path: path.join(screenshotsDir, 'run4_frame250_panel.png') });

    // Jump directly to frame 390 (decay/shatter)
    console.log('Jumping to Run 4 frame 390...');
    await page.evaluate(() => {
        if (window.engine) {
            window.engine.isPaused = true;
            window.engine.jumpToFrame(390);
        }
    });
    await page.waitForFunction(() => {
        return window.engine && window.engine.currentFrameIndex === 390;
    }, { timeout: 5000 });

    // Focus camera on active contacts
    await page.evaluate(() => {
        if (window.engine) window.engine.focusOnActiveContacts();
    });

    await page.screenshot({ path: path.join(screenshotsDir, 'run4_frame390_full.png') });
    await page.locator('.contact-graph-panel').screenshot({ path: path.join(screenshotsDir, 'run4_frame390_panel.png') });

    console.log('Validation screenshots captured successfully.');
});
