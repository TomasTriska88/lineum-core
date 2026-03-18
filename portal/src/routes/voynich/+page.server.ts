import { error } from '@sveltejs/kit';
import * as fs from 'fs';
import * as path from 'path';

export const load = async ({ url }) => {
    // Determine target folio: default to f1v, allow URL override ?folio=f2r
    const targetFolio = url.searchParams.get('folio') || 'f1v';
    
    try {
        // Resolve absolute path upwards to the lineum-core/data directory
        // In local dev, process.cwd() is 'portal'. We need to go up one level.
        const dataPath = path.resolve(process.cwd(), '../data/voynich', `${targetFolio}.json`);
        
        if (!fs.existsSync(dataPath)) {
            return {
                folio: null,
                target: targetFolio,
                missingData: true,
                message: "Bring Your Own Data: Transliteration corpus not found. Please run 'python scripts/ingest_voynich_data.py' in the repository root to build the interactive Voynich maps."
            };
        }
        
        const fileContents = fs.readFileSync(dataPath, 'utf-8');
        return {
            folio: JSON.parse(fileContents),
            target: targetFolio,
            missingData: false
        };
    } catch (e) {
        return {
            folio: null,
            target: targetFolio,
            error: true,
            message: `Failed to load Voynich JSON structure for '${targetFolio}': ${e}`
        };
    }
};
