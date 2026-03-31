<script lang="ts">
  import type { BookData } from '$lib/data/books';
  export let activeBook: BookData;

  const nextVolumes = {
    'foundations': 'Volume II: Motion',
    'motion': 'Volume III: Structure',
    'structure': 'A New Beginning'
  };

  $: nextTeaser = nextVolumes[activeBook.id as keyof typeof nextVolumes] || 'Loading...';
</script>

<div class="page right-page backmatter-page" style="--theme: {activeBook.theme.primaryColor}">
  <div class="inner-content">
    <div class="closing-statement">
      <h3>The Next System</h3>
      <p>This book is merely the foundational grammar. Mathematics is not static; it lives. Once you can hold shapes in equilibrium, it is time to set them into motion. The visual language continues.</p>
    </div>

    <div class="teaser-block">
      <span class="teaser-label">LINEUM SERIES</span>
      <h2 class="teaser-title">{nextTeaser}</h2>
    </div>

    <div class="credit-block">
      <span class="author">TOMÁS TRISKA</span>
      <span class="brand">LINEUM PUBLISHING</span>
    </div>
  </div>
</div>

<style>
  .backmatter-page {
    background: #FAFAFA;
    border-left: 1px solid #E5E7EB;
  }
  .inner-content {
    display: flex;
    flex-direction: column;
    height: 100%;
    padding: 25mm 15mm 25mm 30mm;
    justify-content: center;
    align-items: center;
    text-align: center;
  }

  .closing-statement {
    margin-top: auto;
    max-width: 45ch;
  }
  .closing-statement h3 {
    font-family: var(--font-sans);
    font-size: 0.875rem;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    color: var(--color-muted);
    margin-bottom: 1rem;
  }
  .closing-statement p {
    font-family: var(--font-serif);
    font-size: 1.125rem;
    line-height: 1.8;
    color: #374151;
  }

  .teaser-block {
    margin: 6rem 0;
    padding: 4rem 0;
    width: 100%;
    border-top: 1px solid #E5E7EB;
    border-bottom: 1px solid #E5E7EB;
  }
  .teaser-label {
    font-family: var(--font-mono);
    font-size: 0.75rem;
    letter-spacing: 0.3em;
    color: var(--theme);
    display: block;
    margin-bottom: 1rem;
  }
  .teaser-title {
    font-family: var(--font-sans);
    font-size: 2.25rem;
    font-weight: 300;
    letter-spacing: -0.02em;
    color: #000;
    margin: 0;
  }

  .credit-block {
    margin-top: auto;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }
  .credit-block .author {
    font-family: var(--font-serif);
    font-size: 1.25rem;
    font-weight: 900;
    color: #111827;
  }
  .credit-block .brand {
    font-family: var(--font-mono);
    font-size: 0.75rem;
    letter-spacing: 0.2rem;
    color: #9CA3AF;
  }
</style>
