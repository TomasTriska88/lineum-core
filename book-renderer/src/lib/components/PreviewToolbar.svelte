<script lang="ts">
  export let mode: 'single' | 'spread' | 'print' = 'spread';
</script>

<div class="toolbar">
  <button on:click={() => mode = 'single'} class:active={mode === 'single'}>Single Page</button>
  <button on:click={() => mode = 'spread'} class:active={mode === 'spread'}>Two-Page Spread</button>
  <div class="divider"></div>
  <button on:click={() => mode = 'print'} class="print-btn">Preview Print PDF</button>
</div>

<style>
  .toolbar {
    position: fixed;
    bottom: 2rem;
    left: 50%;
    transform: translateX(-50%);
    background: #111827;
    padding: 0.5rem;
    border-radius: 99px;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    z-index: 1000;
    box-shadow: 0 10px 40px rgba(0,0,0,0.3);
  }
  .divider {
    width: 1px;
    height: 1.5rem;
    background: #374151;
    margin: 0 0.5rem;
  }
  button {
    background: transparent;
    color: #9CA3AF;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 99px;
    font-weight: 600;
    cursor: pointer;
    font-size: 0.875rem;
    transition: all 0.2s;
    font-family: var(--font-sans);
  }
  button:hover { color: #FFF; background: rgba(255,255,255,0.1); }
  button.active { background: #FFFFFF; color: #000; }
  .print-btn { color: #60A5FA; }
  .print-btn:hover { background: rgba(96, 165, 250, 0.2); }
  
  @media print {
    .toolbar { display: none; }
  }
</style>
