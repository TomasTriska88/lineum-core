import fs from 'fs';
import path from 'path';

const CZECH_CHARS = /[áčďéěíňóřšťúůýžÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ]/;

export function checkFile(filePath) {
    const content = fs.readFileSync(filePath, 'utf8');
    const lines = content.split('\n');
    let found = false;

    lines.forEach((line, index) => {
        // Safe words whitelist
        let sanitizedLine = line
            .replace(/Čeština/g, '')
            .replace(/Tomáš Tříska/g, '')
            .replace(/Lineum Dynamics s.r.o./g, '');

        if (CZECH_CHARS.test(sanitizedLine)) {
            console.error(`Czech character found in ${filePath}:${index + 1}:`);
            console.error(`  > ${line.trim()}`);
            found = true;
        }
    });

    return found;
}

export function walkDir(dir, callback) {
    if (!fs.existsSync(dir)) return;
    fs.readdirSync(dir).forEach(f => {
        const dirPath = path.join(dir, f);
        const isDirectory = fs.statSync(dirPath).isDirectory();
        isDirectory ? walkDir(dirPath, callback) : callback(dirPath);
    });
}
