<script lang="ts">
  import type { Concept } from '$lib/data/concepts';
  export let concept: Concept;
</script>

<div class="layout">
  <div class="header">
    {#if concept.chapterTitle}
      <h3 class="chapter-meta">Chapter {concept.chapterNumber} &mdash; {concept.chapterTitle}</h3>
    {/if}
    <h1>{concept.title}</h1>
  </div>
  
  <div class="hero-image-wrapper">
    <div class="prompt-meta">[{concept.image.prompt}]</div>
  </div>
  
  <div class="text-content">
    <p class="concept-hook">{concept.hook}</p>
    <p class="explain-text">{concept.explain}</p>
  </div>
</div>

<style>
  .layout { height: 100%; display: flex; flex-direction: column; }
  
  .header { 
    margin-bottom: 2rem; 
    text-align: center;
  }
  
  .chapter-meta {
    font-size: 0.875rem;
    font-weight: 700;
    letter-spacing: 0.25em;
    color: #9CA3AF;
    margin-bottom: 2rem;
    display: inline-block;
    border-bottom: 1px solid #E5E7EB;
    padding-bottom: 0.5rem;
  }
  
  .hero-image-wrapper {
    width: 100%;
    margin-bottom: 4rem;
    height: 60%; /* Dominant image presence */
    background: #F9FAFB;
    display: flex;
    align-items: flex-end;
    padding: 2rem;
    box-sizing: border-box;
    /* Clean, quiet but confident frame container */
    border: 1px solid #E5E7EB;
  }
  
  .prompt-meta {
    font-family: var(--font-mono);
    color: #6B7280;
    font-size: 0.875rem;
    line-height: 1.5;
  }
  
  .text-content {
    max-width: 80%;
    margin: 0 auto;
  }
  
  .explain-text {
    font-size: 1.25rem;
    line-height: 1.8;
    color: #374151;
  }
</style>
