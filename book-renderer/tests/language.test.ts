import { test, expect } from '@playwright/test';
import * as fs from 'fs';
import * as path from 'path';

test.describe('English-Only Codebase Policy Validation', () => {

  test('All JS/TS and Svelte scripts must be free of Czech diacritics', async () => {
    
    function getAllFiles(dirPath: string, arrayOfFiles: string[] = []): string[] {
      if (!fs.existsSync(dirPath)) return arrayOfFiles;
      
      const files = fs.readdirSync(dirPath);
      
      files.forEach(function(file) {
        if (fs.statSync(dirPath + "/" + file).isDirectory()) {
          arrayOfFiles = getAllFiles(dirPath + "/" + file, arrayOfFiles);
        } else {
          arrayOfFiles.push(path.join(dirPath, "/", file));
        }
      });
      return arrayOfFiles;
    }

    const srcFiles = getAllFiles(path.resolve('./src'));
    const scriptFiles = getAllFiles(path.resolve('./scripts'));
    
    // We filter specifically files that are codebase text scripts.
    const allScripts = [...srcFiles, ...scriptFiles].filter(file => {
      if (file.includes('language.test.ts')) return false;
      return file.endsWith('.ts') || file.endsWith('.js') || file.endsWith('.svelte');
    });

    const forbiddenCzechRegex = /[ěščřžýáíéúůďťňĚŠČŘŽÝÁÍÉÚŮĎŤŇ]/;

    for (const file of allScripts) {
      const content = fs.readFileSync(file, 'utf-8');
      const lines = content.split('\n');

      for (let i = 0; i < lines.length; i++) {
        const line = lines[i];
        
        // Exclude the mock data file (concepts.ts) since it might legitimately contain translated content later
        // But for codebase enforcement, we verify logic files. The user said "all js scripts".
        // concepts.ts is a data file, but technically .ts. We will test it too.
        
        // Assert that the line has no Czech characters
        expect(
          forbiddenCzechRegex.test(line), 
          `Rule violation: Czech diacritics found in ${file} at line ${i + 1} -> "${line.trim()}"`
        ).toBeFalsy();
      }
    }

  });
});
