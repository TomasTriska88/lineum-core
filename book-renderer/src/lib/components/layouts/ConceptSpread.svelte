<script lang="ts">
  import type { Concept } from '$lib/data/concepts';
  import { renderMath } from '$lib/utils/mathRender';
  export let concept: Concept;
  export let startPageNum: number;
  export let layoutVariant: 'standard' | 'shifted' | 'text-first' = 'standard';
</script>

<div class="page left-page">
  <div class="page-number left" class:hidden={startPageNum === 0}>{startPageNum}</div>
  
  <div class="inner-content">
    
    {#if layoutVariant === 'standard' || layoutVariant === 'shifted'}
      <!-- VISUAL/HOOK FOCUS (LEFT) -->
      <div class="page-header">
        <h3 class="meta-subtitle">Chapter {concept.chapterNumber} &mdash; {concept.chapterTitle}</h3>
        <h2 class="concept-title">{@html renderMath(concept.title)}</h2>
      </div>

      <div class="prose-p concept-hook" style={layoutVariant === 'shifted' ? 'font-size: 1.5rem;' : ''}>{@html renderMath(concept.hook)}</div>
      
      <div class="image-box" class:hero-shifted={layoutVariant === 'shifted'}>
        {#if concept.image.path}
          <img src="/{concept.image.path}" alt="{concept.title}" data-prompt="{concept.image.prompt}" data-style="vector" data-variant="{layoutVariant}" class="hero-image" />
        {:else}
          <div class="placeholder-img" data-prompt="{concept.image.prompt}" data-style="vector" data-variant="{layoutVariant}"></div>
        {/if}
      </div>
    {:else if layoutVariant === 'text-first'}
      <!-- TEXT FOCUS (LEFT) -->
      <div class="page-header">
        <h3 class="meta-subtitle">Chapter {concept.chapterNumber} &mdash; {concept.chapterTitle}</h3>
        <h2 class="concept-title">{@html renderMath(concept.title)}</h2>
      </div>

      <div class="prose-p concept-hook">{@html renderMath(concept.hook)}</div>
      <div class="prose-p explain-text">{@html renderMath(concept.explain)}</div>
      
      <div class="aha-editorial" style="margin-top: auto;">
        <span class="aha-icon">💡</span>
        <div class="prose-p aha-quote">{@html renderMath(concept.aha)}</div>
      </div>
    {/if}

  </div>
</div>

<div class="page right-page">
  <div class="page-number right">{startPageNum + 1}</div>
  
  <div class="inner-content right-rhythm">
    
    {#if layoutVariant === 'standard' || layoutVariant === 'shifted'}
      <!-- EXPLANATION/AHA FOCUS (RIGHT) -->
      <div class="prose-p explain-text">{@html renderMath(concept.explain)}</div>
      
      <div class="aha-editorial">
        <span class="aha-icon">💡</span>
        <div class="prose-p aha-quote">{@html renderMath(concept.aha)}</div>
      </div>

      <div class="prose-flow" class:shifted-flow={layoutVariant === 'shifted'}>
        <div class="prose-segment">
          <h4 class="run-in-header">What it is.</h4>
          <div class="prose-p">{@html renderMath(concept.whatItIs)}</div>
        </div>
        <div class="prose-segment">
          <h4 class="run-in-header">How to solve.</h4>
          <div class="prose-p">{@html renderMath(concept.howToSolve)}</div>
        </div>
        <div class="prose-segment">
          <h4 class="run-in-header">Why it works.</h4>
          <div class="prose-p">{@html renderMath(concept.whyItWorks)}</div>
        </div>
      </div>
    {:else if layoutVariant === 'text-first'}
      <!-- VISUAL/WHAT FOCUS (RIGHT) -->
      <div class="image-box" style="margin-top: 0; margin-bottom: 2rem;">
        {#if concept.image.path}
          <img src="/{concept.image.path}" alt="{concept.title}" data-prompt="{concept.image.prompt}" data-style="vector" data-variant="{layoutVariant}" class="hero-image" />
        {:else}
          <div class="placeholder-img" data-prompt="{concept.image.prompt}" data-style="vector" data-variant="{layoutVariant}"></div>
        {/if}
      </div>

      <div class="prose-flow">
        <div class="prose-segment">
          <h4 class="run-in-header">What it is.</h4>
          <div class="prose-p">{@html renderMath(concept.whatItIs)}</div>
        </div>
        <div class="prose-segment">
          <h4 class="run-in-header">How to solve.</h4>
          <div class="prose-p">{@html renderMath(concept.howToSolve)}</div>
        </div>
        <div class="prose-segment">
          <h4 class="run-in-header">Why it works.</h4>
          <div class="prose-p">{@html renderMath(concept.whyItWorks)}</div>
        </div>
      </div>
    {/if}

    <!-- FIXED: Summary always caps the right page -->
    <div class="summary-editorial">
      <h4 class="summary-label">Summary</h4>
      <div class="prose-p">{@html renderMath(concept.summary)}</div>
    </div>
  </div>
</div>

<style>
  .inner-content {
    height: 100%;
    display: flex;
    flex-direction: column;
  }
  
  /* L E F T   P A G E */
  .page-header { margin-bottom: 2rem; }
  
  .meta-subtitle {
     font-family: var(--font-mono);
     font-size: 0.75rem;
     text-transform: uppercase;
     letter-spacing: 0.2em;
     color: #0EA5E9; /* Lineum Cyan */
     margin-bottom: 1rem;
     display: inline-block;
  }
  
  .concept-title {
     font-family: var(--font-sans);
     font-size: 3.5rem;
     font-weight: 800;
     line-height: 1.1;
     letter-spacing: -0.05em;
     color: #0F172A;
     text-wrap: balance; /* Prevents awkward title breaks */
  }

  /* Math string stability override */
  .concept-title :global(.katex) {
    display: inline-block;
    vertical-align: bottom;
  }
  
  .concept-hook {
     font-family: var(--font-serif);
     font-size: 1.5rem;
     line-height: 1.4;
     font-style: italic;
     color: #334155;
     padding-left: 2rem;
     border-left: 3px solid #8B5CF6; /* Lineum Purple */
     margin-bottom: 2rem;
     text-wrap: pretty;
  }
  
  .explain-text {
    font-family: var(--font-serif);
    font-size: 1.125rem;
    line-height: 1.8;
    color: #0F172A;
    margin-bottom: 3rem;
    text-wrap: pretty;
  }

  /* IMAGE STYLING: Bright / Light Mode (No Duotone Filter) */
  .image-box {
    margin-top: auto;
    width: 100%;
    aspect-ratio: 16/10;
    position: relative;
    background: #F8FAFC; 
    border: 1px solid #E2E8F0;
    overflow: hidden;
    border-radius: 4px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
  }
  
  .hero-image {
    width: 100%; height: 100%;
    object-fit: cover;
  }
  
  .placeholder-img {
    width: 100%; height: 100%;
    background: repeating-linear-gradient(45deg, #f1f5f9, #f1f5f9 10px, #e2e8f0 10px, #e2e8f0 20px);
    opacity: 0.5;
  }

  /* R I G H T   P A G E */
  .right-rhythm {
    justify-content: flex-start;
  }

  .aha-editorial {
    margin: 2rem 0 4rem 0;
    padding: 3rem;
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-left: 4px solid #F59E0B; /* Lineum Amber / Identity */
    display: flex;
    gap: 1.5rem;
    align-items: flex-start;
  }
  
  .aha-icon {
    font-size: 2rem;
    opacity: 0.8;
  }

  .aha-quote {
    font-family: var(--font-serif);
    font-size: 1.625rem;
    font-weight: 300;
    color: #0F172A;
    line-height: 1.4;
    font-style: italic;
    margin: 0;
    text-wrap: balance;
  }

  .prose-flow {
    display: flex;
    flex-direction: column;
    gap: 2rem;
    margin-bottom: auto; /* Pushes summary to the bottom */
  }

  .prose-segment .prose-p {
    font-family: var(--font-serif);
    font-size: 1.125rem;
    color: #334155;
    line-height: 1.8;
    margin: 0;
    text-wrap: pretty;
  }

  /* Editorial Run-in (marginalia effect) instead of form labels */
  .run-in-header {
    font-family: var(--font-sans);
    font-weight: 700;
    font-size: 0.875rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #0F172A;
    margin: 0 0 0.5rem 0;
    display: block;
    position: relative;
  }
  .run-in-header::after {
    content: '';
    display: inline-block;
    width: 2rem;
    height: 2px;
    background: #0EA5E9; /* Golden ratio / Cyan bridge */
    vertical-align: middle;
    margin-left: 0.75rem;
  }

  /* The anchor block at the bottom */
  .summary-editorial {
    margin-top: 4rem;
    padding-top: 2rem;
    border-top: 1px solid #0F172A;
  }

  .summary-label {
    font-family: var(--font-mono);
    font-size: 0.75rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #64748B;
    margin: 0 0 1rem 0;
  }
  
  .summary-editorial .prose-p {
    font-family: var(--font-serif);
    font-size: 1.375rem;
    font-weight: 400;
    color: #0F172A;
    line-height: 1.5;
    margin: 0;
    text-wrap: pretty;
  }

  /* Reset layout constraints and awkward words breaking */
  :global(.prose-p) { hyphens: none !important; word-wrap: break-word; overflow-wrap: break-word; }
  :global(.katex-display) { margin: 1rem 0 !important; }
</style>
