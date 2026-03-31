<script lang="ts">
  import { level1Concepts } from '$lib/data/concepts';
  import PreviewToolbar from '$lib/components/PreviewToolbar.svelte';
  import FrontMatter from '$lib/components/FrontMatter.svelte';
  import ConceptSpread from '$lib/components/layouts/ConceptSpread.svelte';
  import { onMount } from 'svelte';

  let viewMode: 'single' | 'spread' | 'print' = 'spread';
  let isExportMode = false;

  onMount(() => {
    if (window.location.search.includes('export=true')) {
      viewMode = 'single';
      isExportMode = true;
    }
  });
</script>

<main class:print-mode={viewMode === 'print' || isExportMode}>
  {#if !isExportMode}
    <PreviewToolbar bind:mode={viewMode} />
  {/if}

  <div class="book-preview-container {viewMode === 'spread' && !isExportMode ? 'spread-mode' : 'single-mode'} {isExportMode ? 'export-clean' : ''}">
    
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
           <ConceptSpread {concept} startPageNum={(i * 2) + 5} leftHeavy={i % 2 === 0} />
        </div>
      {/each}
    {:else}
      {#each level1Concepts as concept, i}
         <!-- In single mode, just render them consecutively -->
         <ConceptSpread {concept} startPageNum={(i * 2) + 5} leftHeavy={i % 2 === 0} />
      {/each}
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
 :global(.left-page) .page-number { left: var(--margin-outer); }
 :global(.right-page) .page-number { right: var(--margin-outer); }

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
   break-after: page;
   page-break-after: always;
 }

 .print-mode .book-preview-container {
   padding: 0;
   background: white;
 }
 .print-mode .spread-preview {
   flex-direction: column;
 }
</style>
