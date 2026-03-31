<script lang="ts">
  import { level1Concepts } from '$lib/data/concepts';
  import PreviewToolbar from '$lib/components/PreviewToolbar.svelte';
  import FrontMatter from '$lib/components/FrontMatter.svelte';
  import ConceptSpread from '$lib/components/layouts/ConceptSpread.svelte';
  import FullPrintCover from '$lib/components/FullPrintCover.svelte';
  import { onMount } from 'svelte';

  let viewMode: 'single' | 'spread' | 'print' = 'spread';
  let isExportMode = false;
  let isCoverMode = false;
  let printFormat: 'ebook' | 'print-global' | 'print-eu' = 'ebook';

  onMount(() => {
    const params = new URLSearchParams(window.location.search);
    if (params.get('export') === 'true') {
      viewMode = 'single';
      isExportMode = true;
    }
    if (params.get('cover') === 'true') {
      isCoverMode = true;
    }
    const format = params.get('format');
    if (format === 'print-global' || format === 'print-eu') {
      printFormat = format;
    }
  });
</script>

<main class:print-mode={viewMode === 'print' || isExportMode}>
  {#if !isExportMode}
    <PreviewToolbar bind:mode={viewMode} />
  {/if}

  <div class="book-preview-container {viewMode === 'spread' && !isExportMode ? 'spread-mode' : 'single-mode'} {isExportMode ? 'export-clean' : ''}">
    
    {#if isCoverMode}
      <FullPrintCover mode={printFormat} />
    {:else}
      <!-- Front Matter (Handles its own 4 pages: Title, Imprint, TOC, Preface) -->
      {#if viewMode === 'spread'}
        <div class="spread-preview">
          <!-- Title & Imprint -->
          <FrontMatter />
        </div>
      {:else}
        <FrontMatter />
      {/if}

      <!-- Concepts flow: StartPageNum = 5 because FrontMatter takes 4 pages -->
      {#if viewMode === 'spread'}
        {#each level1Concepts as concept, i}
          <div class="spread-preview">
             <ConceptSpread {concept} startPageNum={(i * 2) + 5} layoutVariant={i % 4 === 0 ? 'text-first' : (i % 3 === 0 ? 'shifted' : 'standard')} />
          </div>
        {/each}
      {:else}
        {#each level1Concepts as concept, i}
           <!-- In single mode, just render them consecutively -->
           <ConceptSpread {concept} startPageNum={(i * 2) + 5} layoutVariant={i % 4 === 0 ? 'text-first' : (i % 3 === 0 ? 'shifted' : 'standard')} />
        {/each}
      {/if}
    {/if}

  </div>
</main>

<style>
 .page-number {
   position: absolute;
   bottom: 15mm;
   font-family: var(--font-sans);
   font-size: 0.875rem;
   color: #9CA3AF;
 }
 :global(.left-page) .page-number { left: var(--margin-outer, 15mm); }
 :global(.right-page) .page-number { right: var(--margin-outer, 15mm); }
 :global(.front-matter) .page-number { font-family: var(--font-serif); font-style: italic; }

 .empty-page {
    background: #FAFAFA;
 }

 .export-clean {
   padding: 0 !important;
   background: transparent !important;
   gap: 0 !important;
 }
 .export-clean :global(.page) {
   box-shadow: none !important;
   margin: 0 !important;
   width: 100vw !important;
   height: 100vh !important;
   page-break-after: always;
   break-after: page;
 }

 .print-mode .book-preview-container {
   padding: 0;
   background: white;
 }
 .print-mode .spread-preview {
   flex-direction: column;
 }
</style>
