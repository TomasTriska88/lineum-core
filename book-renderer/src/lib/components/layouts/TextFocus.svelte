<script lang="ts">
  import type { Concept } from '$lib/data/concepts';
  export let concept: Concept;
</script>

<div class="layout">
  <div class="top-section">
     <h3 class="meta-subtitle">{concept.title} &mdash; Spatial Analysis</h3>
  </div>
  
  <!-- Massive quote acting as the anchor of the page -->
  <div class="massive-quote">
     {concept.whyItWorks}
  </div>
  
  <div class="summary-box">
     <h4 class="meta-label">Final Summary</h4>
     <p>{concept.summary}</p>
  </div>
</div>

<style>
  .layout { 
    height: 100%; 
    display: flex; 
    flex-direction: column; 
    justify-content: space-between; 
    background: #FFFFFF; /* Hard isolated feeling */
    margin: -25mm -20mm -25mm -30mm; /* Bleeds slightly to create boundary */
    padding: 25mm 20mm 25mm 30mm;
  }
  
  .meta-subtitle {
     font-family: var(--font-sans);
     font-size: 0.875rem;
     text-transform: uppercase;
     letter-spacing: 0.15em;
     color: #9CA3AF;
     border-bottom: 1px solid #E5E7EB;
     padding-bottom: 1rem;
     display: inline-block;
  }
  
  /* Very confident typography anchor */
  .massive-quote {
    font-size: 3.5rem;
    font-weight: 300;
    font-family: var(--font-sans);
    line-height: 1.25;
    letter-spacing: -0.04em;
    color: #111827;
    max-width: 85%;
    margin-top: 5rem;
    margin-bottom: auto;
    border-left: 6px solid #111827;
    padding-left: 3rem;
  }
  
  /* Summary is a heavy dark block visually different from the rest */
  .summary-box {
    margin-top: auto;
    padding-top: 3rem;
    border-top: 2px solid #000;
  }
  
  .meta-label {
    font-family: var(--font-mono);
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    color: var(--color-accent);
    margin-bottom: 1rem;
  }
  
  .summary-box p {
    font-size: 1.75rem;
    font-family: var(--font-serif);
    color: #000;
    font-weight: 400;
    line-height: 1.6;
    max-width: 90%;
  }
</style>
