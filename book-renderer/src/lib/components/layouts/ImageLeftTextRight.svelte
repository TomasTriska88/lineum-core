<script lang="ts">
  import type { Concept } from '$lib/data/concepts';
  export let concept: Concept;
</script>

<div class="layout">
  <div class="page-title">
    <h2>{concept.title}</h2>
    <div class="divider"></div>
  </div>

  <div class="content-grid">
    <!-- Image Box -->
    <div class="col-image">
      <div class="image-wrapper">
         <div class="prompt-meta">[{concept.image.prompt}]</div>
      </div>
    </div>
    
    <!-- Editorial Text -->
    <div class="col-text">
       <p class="concept-hook">{concept.hook}</p>
       
       <div class="logical-section">
         <h4 class="meta-label">What it is</h4>
         <p>{concept.whatItIs}</p>
       </div>
       
       <div class="logical-section">
         <h4 class="meta-label">How to solve</h4>
         <p>{concept.howToSolve}</p>
       </div>
       
       <div class="logical-section">
         <h4 class="meta-label">Why it works in space</h4>
         <p>{concept.whyItWorks}</p>
       </div>
    </div>
  </div>

  <!-- AHA Breakout Box -->
  <div class="aha-box">
    <span class="icon">💡</span>
    <p>{concept.aha}</p>
  </div>
</div>

<style>
  .layout { 
    height: 100%; 
    display: flex; 
    flex-direction: column; 
    justify-content: flex-start;
  }
  
  .page-title {
    margin-bottom: 3rem;
  }
  
  .divider {
    height: 1px;
    width: 6rem;
    background: #D1D5DB;
    margin-top: 1.5rem;
  }
  
  .content-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 5rem;
  }
  
  .image-wrapper {
    width: 100%;
    aspect-ratio: 1;
    background: #F9FAFB;
    border: 1px solid #E5E7EB;
    box-sizing: border-box;
    display: flex;
    align-items: flex-end;
    padding: 1.5rem;
  }
  
  .prompt-meta {
    font-family: var(--font-mono);
    color: #6B7280;
    font-size: 0.75rem;
    line-height: 1.5;
  }
  
  .col-text {
    display: flex;
    flex-direction: column;
  }
  
  .logical-section { margin-top: 3rem; }
  
  .meta-label {
    font-size: 0.75rem;
    font-family: var(--font-mono);
    text-transform: uppercase;
    letter-spacing: 0.15em;
    color: var(--color-accent);
    margin-bottom: 1rem;
    border-bottom: 1px solid #E5E7EB;
    padding-bottom: 0.5rem;
    display: inline-block;
  }
  
  /* Pushing the AHA box strictly to the bottom margin to anchor the page */
  .aha-box {
    margin: auto -30mm -25mm -30mm; /* Expanding outside the basic padding if possible, or just sticking to bottom */
    margin-top: auto; /* Pull to bottom of flex container */
  }
</style>
