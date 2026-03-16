import { test, expect } from '@playwright/test';

test.describe('Voynich Frontend Integration', () => {
    test('lineum.io/voynich loads modern Fullscreen Map Engine HUD', async ({ page }) => {
        test.setTimeout(90000); // Massive bump for heavy canvas
        page.on('console', msg => console.log(`BROWSER: ${msg.text()}`));
        
        console.log("Starting Navigation...");
        await page.goto('http://127.0.0.1:5173/voynich', { waitUntil: 'commit' });
        console.log("Marker: 0 - Navigated");

        // Force a stable URL wait before interacting
        await expect(page).toHaveURL(/.*voynich/);
        
        console.log("Marker: 1 - Canvas Check");
        const canvasMap = page.locator('main.overflow-x-hidden');
        await expect(canvasMap).toBeVisible({ timeout: 15000 });
        await expect(canvasMap).toHaveClass(/custom-scrollbar/);
        
        console.log("Marker: 1.5 - Horizontal Overflow Test");
        // Explicitly test that the horizontal flow is contained properly after the Faza 187 fix
        const isHorizontalScrollContained = await page.evaluate(() => {
            return document.documentElement.scrollWidth <= window.innerWidth;
        });
        expect(isHorizontalScrollContained).toBe(true);

        // 2. Verify the base Folio image is massive and spans coordinate parity
        console.log("Marker: 2 - Folio Image Check");
        const folioImage = page.locator('img[alt="Voynich f1v"]');
        await expect(folioImage).toBeVisible();
        await expect(folioImage).toHaveClass(/object-cover/);

        // 3. Verify Layer 3 (Variable Slots) via URL State override
        console.log("Marker: 3 - Layer 3 API Call");
        await page.goto('http://127.0.0.1:5173/voynich?layer=3', { waitUntil: 'commit' });
        
        // Let Reactivity settle
        await page.waitForTimeout(500);

        // Check that the Contextual Dossier card prompt appears
        console.log("Marker: 4 - Select Prompt Check");
        await expect(page.locator('text=Select a highlighted structural element')).toBeVisible();

        // 4. Test activating the Omega Target token (okam) via URL State override
        console.log("Marker: 5 - Layer 7 API Call");
        await page.goto('http://127.0.0.1:5173/voynich?layer=7&token=T4', { waitUntil: 'commit' });
        
        // Add a slight delay to allow the flexbox DOM to settle
        await page.waitForTimeout(500);

        console.log("Marker: 6 - Final Translation Block Check");
        await expect(page.getByText('Hypothesis Filter Active')).toBeVisible({ timeout: 15000 });
        console.log("Marker: 7 - DONE");
    });
});
