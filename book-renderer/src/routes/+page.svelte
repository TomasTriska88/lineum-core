<script lang="ts">
  import { books, type BookData } from '$lib/data/books';
  import PreviewToolbar from '$lib/components/PreviewToolbar.svelte';
  import FrontMatter from '$lib/components/FrontMatter.svelte';
  import ConceptSpread from '$lib/components/layouts/ConceptSpread.svelte';
  import FullPrintCover from '$lib/components/FullPrintCover.svelte';
  import BackMatter from '$lib/components/BackMatter.svelte';
  import { onMount } from 'svelte';

  let viewMode: 'epub' | 'spread' | 'qa-print' = 'spread';
  let isExportMode = false;
  let isCoverMode = false;
  let printFormat: 'ebook' | 'print-global' | 'print-eu' = 'ebook';
  let clientWidth = 1600;
  
  // URL selected Book default to Foundations
  let activeBook: BookData = books['foundations'];

  // Svelte reactive derived scale for spread layout
  $: scaleFactor = Math.min(1, clientWidth / 1700);

  onMount(() => {
    const params = new URLSearchParams(window.location.search);
    const bId = params.get('book');
    if (bId && books[bId]) {
      activeBook = books[bId];
    }
    if (params.get('export') === 'true') {
      viewMode = 'epub'; // For ebooks layout
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

<svelte:window bind:innerWidth={clientWidth} />

<main class:print-mode={viewMode === 'qa-print' || isExportMode}>
  {#if !isExportMode}
    <PreviewToolbar bind:mode={viewMode} activeBookId={activeBook.id} />
  {/if}

  <div class="book-preview-container {viewMode === 'spread' && !isExportMode ? 'spread-mode' : 'single-mode'} {isExportMode ? 'export-clean' : ''}">
    
    {#if isCoverMode}
      <FullPrintCover mode={printFormat} {activeBook} />
    {:else}
      <!-- Front Matter (Handles its own 4 pages: Title, Imprint, TOC, Preface) -->
      {#if viewMode === 'spread'}
        <div class="spread-preview-wrapper" style="--responsive-scale: {scaleFactor}">
          <div class="spread-preview">
            <FrontMatter {activeBook} />
          </div>
        </div>
      {:else}
        <FrontMatter {activeBook} />
      {/if}

      <!-- Concepts flow -->
      {#if viewMode === 'spread'}
        {#each activeBook.concepts as concept, i}
          <div class="spread-preview-wrapper" style="--responsive-scale: {scaleFactor}">
            <div class="spread-preview">
               <ConceptSpread {concept} startPageNum={(i * 2) + 5} layoutVariant={i % 4 === 0 ? 'text-first' : (i % 3 === 0 ? 'shifted' : 'standard')} />
            </div>
          </div>
        {/each}
        
        <!-- Back Matter Spread matching last single page and back matter -->
        <div class="spread-preview-wrapper" style="--responsive-scale: {scaleFactor}">
          <div class="spread-preview">
             <div class="page left-page empty-page"></div>
             <BackMatter {activeBook} />
          </div>
        </div>
      {:else}
        {#each activeBook.concepts as concept, i}
           <ConceptSpread {concept} startPageNum={(i * 2) + 5} layoutVariant={i % 4 === 0 ? 'text-first' : (i % 3 === 0 ? 'shifted' : 'standard')} />
        {/each}
        <BackMatter {activeBook} />
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
 
 .spread-preview-wrapper {
   transform: scale(var(--responsive-scale, 1));
   transform-origin: top center;
   transition: transform 0.2s ease;
   display: flex;
   justify-content: center;
   margin-bottom: 2rem;
 }
</style>
