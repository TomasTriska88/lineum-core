<script lang="ts">
  export let title: string;
  export let subtitle: string;
</script>

<div class="page right-page title-page">
  <div class="inner-content">
    
    <div class="front-matter">
       <span class="lineum-brand">FOUNDATIONS // OEA</span>
       <span class="version-brand">BOOK 1</span>
    </div>

    <div class="title-block">
      <h1>{title}</h1>
      <h2>{subtitle}</h2>
    </div>
    
    <div class="colophon-block">
       <p>The Official Documentation for Flow Geometry</p>
       <div class="spine-anchor"></div>
    </div>
  </div>
</div>

<style>
  .title-page {
    background: #020617; /* Dark slate */
    color: #F8FAFC;
    border-left: 20px solid #0EA5E9; /* Massive cyan binding strip */
  }

  .inner-content {
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 6rem 4rem;
  }

  .front-matter {
    display: flex;
    justify-content: space-between;
    font-family: var(--font-mono);
    font-size: 0.875rem;
    letter-spacing: 0.3em;
    color: #94A3B8;
    text-transform: uppercase;
  }

  .title-block {
    margin: auto 0;
  }

  h1 {
    font-family: var(--font-sans);
    font-size: 6rem;
    font-weight: 800;
    letter-spacing: -0.05em;
    line-height: 0.95;
    color: #FFFFFF;
    margin-bottom: 2rem;
    text-wrap: balance;
  }

  h2 {
    font-family: var(--font-serif);
    font-size: 2.25rem;
    font-weight: 300;
    font-style: italic;
    color: #CBD5E1;
    max-width: 25ch;
    line-height: 1.4;
    text-wrap: balance;
  }

  .colophon-block {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    border-top: 1px solid #1E293B;
    padding-top: 2rem;
  }
  
  .colophon-block p {
    font-family: var(--font-mono);
    text-transform: uppercase;
    font-size: 0.75rem;
    letter-spacing: 0.15em;
    color: #475569;
    max-width: 30ch;
  }

  .spine-anchor {
    width: 3rem;
    height: 3rem;
    background: #8B5CF6; /* Purple Memory */
    border-radius: 50%;
    opacity: 0.8;
  }
</style>
