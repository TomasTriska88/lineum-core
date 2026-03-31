<script lang="ts">
  export let mode: 'epub' | 'spread' | 'qa-print' = 'spread';
  export let activeBookId: string = 'foundations';
</script>

<div class="toolbar">
  <div class="mode-group book-switcher glass-pill">
    <button on:click={() => window.location.href='/?book=foundations'} class:active={activeBookId === 'foundations'} class="book-pill">B1: Foundations</button>
    <button on:click={() => window.location.href='/?book=motion'} class:active={activeBookId === 'motion'} class="book-pill">B2: Motion</button>
    <button on:click={() => window.location.href='/?book=structure'} class:active={activeBookId === 'structure'} class="book-pill">B3: Structure</button>
  </div>
  
  <div class="mode-group viewer-modes glass-pill">
    <button on:click={() => mode = 'spread'} class:active={mode === 'spread'} class="view-btn">Public Reader (Spread)</button>
    <button on:click={() => mode = 'epub'} class:active={mode === 'epub'} class="view-btn">Public Reader (Scroll)</button>
  </div>
  
  <div class="mode-group qa-modes glass-pill">
    <button on:click={() => mode = 'qa-print'} class="print-btn" title="Internal diagnostic mode showing flat DOM for automated scaling/page breaks">Internal QA Print Bounds</button>
  </div>
</div>

<style>
  .toolbar {
    position: fixed;
    bottom: 2rem;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    gap: 0.75rem;
    z-index: 1000;
    width: 100%;
    max-width: 95vw;
    pointer-events: none; /* Let clicks pass through empty space */
  }
  
  .glass-pill {
    background: rgba(17, 24, 39, 0.95);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    padding: 0.35rem 0.5rem;
    border-radius: 99px;
    display: flex;
    align-items: center;
    gap: 0.25rem;
    box-shadow: 0 10px 40px rgba(0,0,0,0.3), inset 0 1px 0 rgba(255,255,255,0.1);
    pointer-events: auto; /* Re-enable clicks inside pills */
  }

  button {
    background: transparent;
    color: #9CA3AF;
    border: none;
    padding: 0.6rem 1.25rem;
    border-radius: 99px;
    font-weight: 600;
    cursor: pointer;
    font-size: 0.875rem;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    font-family: var(--font-sans);
    white-space: nowrap;
    flex-shrink: 0;
  }
  
  button:hover { 
    color: #FFF; 
    background: rgba(255,255,255,0.08); 
  }
  
  .view-btn.active { 
    background: #FFFFFF; 
    color: #000; 
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  }
  
  .print-btn { 
    color: #60A5FA; 
  }
  
  .print-btn:hover { 
    background: rgba(96, 165, 250, 0.15); 
    color: #93C5FD;
  }
  
  .book-pill {
    font-size: 0.75rem;
    padding: 0.5rem 1rem;
    background: #1F2937;
  }
  
  .book-pill:hover {
    background: #374151;
  }
  
  .book-pill.active {
    background: #3B82F6;
    color: #FFF;
    font-weight: 700;
    box-shadow: 0 0 15px rgba(59, 130, 246, 0.5);
  }

  @media print {
    .toolbar { display: none; }
  }
</style>
