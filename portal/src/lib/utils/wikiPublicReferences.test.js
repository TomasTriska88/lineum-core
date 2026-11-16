import { test } from 'node:test';
import assert from 'node:assert/strict';
import { markUnpublishedWikiReferences, unpublishedReferenceFilenames } from './wikiPublicReferences.js';

test('missing archival documents are shown as non-clickable references without changing their labels', () => {
    const original = '<p>See <a href="./lineum-core.md#3-equation"><em>Equation section</em></a>.</p>';
    const output = markUnpublishedWikiReferences(original);
    assert.match(output, /Equation section/);
    assert.match(output, /source file unavailable/);
    assert.doesNotMatch(output, /<a\b/);
});

test('missing images are transparently marked, not replaced with invented scientific figures', () => {
    const output = markUnpublishedWikiReferences('<img alt="Density map" src="../output/lineum_return_density_127_0.png"/>');
    assert.match(output, /Illustration unavailable: Density map/);
    assert.doesNotMatch(output, /<img\b/);
});

test('existing, public and external references stay intact', () => {
    const html = '<a href="../docs/verification_checklist.md">Checklist</a><img src="../assets/cymatic_hydrogen_1772671292243.png"><a href="https://doi.org/10.1234">DOI</a>';
    assert.equal(markUnpublishedWikiReferences(html), html);
    const external = '<a href="https://example.org/lineum-core.md">External archived reference</a>';
    assert.equal(markUnpublishedWikiReferences(external), external);
});

test('a missing linked graph is kept as a labeled but non-clickable reference', () => {
    const result = markUnpublishedWikiReferences('<a href="../spectrum_difference_matrix.png">Spectral difference graph</a>');
    assert.match(result, /Spectral difference graph/);
    assert.match(result, /source file unavailable/);
    assert.doesNotMatch(result, /href=/);
});

test('all known truly absent archival targets are explicitly catalogued', () => {
    assert.equal(unpublishedReferenceFilenames.size, 11);
});
