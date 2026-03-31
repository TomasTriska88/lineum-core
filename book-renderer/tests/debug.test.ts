import { test, expect } from '@playwright/test';

test('Debug headers', async ({ page }) => {
  await page.goto('/?book=foundations');
  await page.click('text=Public Reader (Scroll)');
  await page.waitForTimeout(2000);
  const texts = await page.locator('.run-in-header').allInnerTexts();
  console.log("DEBUG HEADERS FOUND:", texts);
});
