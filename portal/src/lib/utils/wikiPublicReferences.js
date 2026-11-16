/**
 * References retained in archival whitepapers but absent from the Git repository.
 * This changes only presentation HTML in the standalone, backend-free preview.
 * Original scientific Markdown files and production website are unaffected.
 */
export const unpublishedReferenceFilenames = new Set([
    'lineum-core-equation-history.md',
    'lineum-core.md',
    'spectral_balance.md',
    'resonant_seed.md',
    'spectral_observer.md',
    'harmonic_spectrum.md',
    'transverson_resonance.md',
    'spectrum_difference_matrix.png',
    'spectrum_heal_vs_ruin_final.png',
    'lineum_return_density_127_0.png',
    'lineum_return_density_127_127.png'
]);

function isUnpublishedReference(href) {
    try {
        const resolved = new URL(href, 'https://lineum.invalid/wiki/document/');
        if (resolved.origin !== 'https://lineum.invalid') return false;
        const path = resolved.pathname;
        const filename = decodeURIComponent(path.split('/').filter(Boolean).at(-1) || '');
        return unpublishedReferenceFilenames.has(filename);
    } catch {
        return false;
    }
}

/** Replace dead archival links with clearly labeled, non-clickable references. */
export function markUnpublishedWikiReferences(html) {
    return html
        .replace(/<a\b([^>]*?)\bhref=(['"])(.*?)\2([^>]*)>([\s\S]*?)<\/a>/gi,
            (original, before, quote, href, after, label) => {
                if (!isUnpublishedReference(href)) return original;
                return `<span class="lineum-archive-reference" role="note" title="The linked source file is not in the public archive">${label} <small>(source file unavailable)</small></span>`;
            })
        .replace(/<img\b[^>]*>/gi, original => {
            const src = original.match(/\bsrc=(['"])(.*?)\1/i)?.[2];
            if (!src || !isUnpublishedReference(src)) return original;
            const alt = original.match(/\balt=(['"])(.*?)\1/i)?.[2] || 'Referenced illustration';
            // alt is already HTML-escaped by the Markdown renderer.
            return `<span class="lineum-archive-figure" role="note" title="Source image is not in the public archive">[Illustration unavailable: ${alt}]</span>`;
        });
}
