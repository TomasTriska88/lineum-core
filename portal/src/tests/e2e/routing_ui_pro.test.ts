import { expect, test } from '@playwright/test';

test.describe('Diffusion Phase Lab - Canvas Lifecycle', () => {

    test('Page load, UI elements and navigation safely mount/unmount Diffusion canvas', async ({ page }) => {
        const consoleErrors: string[] = [];

        // Listen for canvas contexts
        page.on('console', msg => {
            if (msg.type() === 'error' ) {
                consoleErrors.push(msg.text());
            }
        });

        // Mock the backend APIs to ensure the test does not implicitly crash if backend offline
        await page.route('**/api/v1/spatial/diffusion/demos/*', async route => {
            await route.fulfill({ status: 200, json: { scenario_summary: "Mock summary", grid_size: [128, 128], kappa: Array(128).fill(Array(128).fill(1)) } });
        });

        // Step 1: Direct navigation to Diffusion section
        await page.goto('/api-solutions');

        // Monitor the visibility of the canvas element
        const webglCanvas = page.locator('#pressure-inference canvas').first();
        await expect(webglCanvas).toBeVisible({ timeout: 10000 });

        // Test the existence of the main B2B UI elements
        await expect(page.getByText('Lineum API Solutions', { exact: false })).toBeVisible();

        const startBtn = page.getByRole('button', { name: /Run Analysis/i }).first();
        await expect(startBtn).toBeVisible();

        // Step 2: Lifecycle navigation to verify unmounting 
        // We go back to the Homepage, and then back to API Solutions.
        await page.goto('/');
        await page.waitForLoadState('networkidle');

        // The canvas on the homepage must load correctly
        await expect(page.locator('canvas.shader-canvas')).toBeVisible();

        // And back to API Solutions
        await page.goto('/api-solutions');
        await expect(page.locator('#pressure-inference canvas').first()).toBeVisible();

        // Evaluate if any errors were caught in the console.
        expect(consoleErrors).toEqual([]);
    });

});
