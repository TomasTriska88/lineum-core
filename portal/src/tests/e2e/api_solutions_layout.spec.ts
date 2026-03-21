import { test, expect } from './base';

test.describe('API Solutions Layout', () => {

    test('Hero section should not be obscured by the global navigation on the main page', async ({ page }) => {
        await page.goto('/api-solutions');

        // Wait for the main heading and the global header
        const heading = page.locator('h1').first();
        await expect(heading).toBeVisible();

        const nav = page.locator('nav').first();
        await expect(nav).toBeVisible();

        // Get their bounding boxes
        const headingBox = await heading.boundingBox();
        const navBox = await nav.boundingBox();

        expect(headingBox).not.toBeNull();
        expect(navBox).not.toBeNull();
        console.log("MAIN PAGE BOXES:", { headingBox, navBox });

        // Assert that the top of the heading is BELOW the bottom of the header
        if (headingBox && navBox) {
            const navBottom = navBox.y + navBox.height;
            expect(headingBox.y).toBeGreaterThanOrEqual(navBottom);
        }
    });

    test('Hero section should not be obscured by the global navigation on subdomain pages', async ({ page }) => {
        await page.goto('/api-solutions/urban-logistics');

        // Wait for the domain heading and the global header
        const heading = page.locator('h1', { hasText: 'Urban Traffic & Logistics' });
        await expect(heading).toBeVisible();

        const nav = page.locator('nav');
        await expect(nav).toBeVisible();

        // Get their bounding boxes
        const headingBox = await heading.boundingBox();
        const navBox = await nav.boundingBox();

        expect(headingBox).not.toBeNull();
        expect(navBox).not.toBeNull();
        console.log("SUBPAGE BOXES:", { headingBox, navBox });

        // Assert that the top of the heading is BELOW the bottom of the header
        if (headingBox && navBox) {
            const navBottom = navBox.y + navBox.height;
            expect(headingBox.y).toBeGreaterThanOrEqual(navBottom);
        }
    });

    test('Ambient background should bridge the navigation gap completely', async ({ page }) => {
        await page.goto('/api-solutions');
        
        const ambientBg = page.locator('div[aria-hidden="true"]').first();
        await expect(ambientBg).toBeAttached();
        
        const bgBox = await ambientBg.boundingBox();
        expect(bgBox).not.toBeNull();
        
        if (bgBox) {
            // The top of the background should be negative to hide the nav gap
            expect(bgBox.y).toBeLessThan(0);
        }
    });

    test('Hero CTA buttons should utilize correct Tailwind utility classes', async ({ page }) => {
        await page.goto('/api-solutions');
        
        const primaryBtn = page.locator('.bg-cyan-400').first();
        const secondaryBtn = page.locator('.border-white\\/10').first();
        
        await expect(primaryBtn).toBeVisible();
        await expect(primaryBtn).toHaveClass(/bg-cyan-400/);
        
        await expect(secondaryBtn).toBeVisible();
        await expect(secondaryBtn).toHaveClass(/bg-white\/5/);
    });

    test('ROI component should maintain mx-auto centering and proper bottom spacing', async ({ page }) => {
        await page.goto('/api-solutions');
        
        // Target the ROI grid container via input[type="range"]
        const roiGrid = page.locator('.grid.lg\\:grid-cols-2').filter({ has: page.locator('input[type="range"]') }).first();
        await expect(roiGrid).toBeVisible();
        
        // Assert centering and margin-bottom are applied
        await expect(roiGrid).toHaveClass(/mx-auto/);
        await expect(roiGrid).toHaveClass(/mb-32/);
    });

});
