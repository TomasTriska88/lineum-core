<script lang="ts">
  import type { BookData } from '$lib/data/books';
  import { renderMath } from '$lib/utils/mathRender';
  
  export let activeBook: BookData;

  // Aggregate chapter names for TOC
  $: chapters = Array.from(new Set(activeBook.frontMatter.toc.map(t => t.chapter)));
</script>

<!-- TITLE PAGE -->
<div class="page right-page title-page" style="border-left-color: {activeBook.theme.primaryColor}">
  <div class="inner-content">
    <div class="front-meta">
       <span class="version-brand">VOLUME {activeBook.id === 'foundations' ? '1' : activeBook.id === 'motion' ? '2' : '3'}</span>
    </div>
    <div class="title-block">
      <h1>{activeBook.frontMatter.title}</h1>
      <h2>{activeBook.frontMatter.subtitle}</h2>
    </div>
    <div class="colophon-block">
       <div class="prose-p">The Official Documentation for {activeBook.frontMatter.title}</div>
       <div class="spine-anchor" style="background: {activeBook.theme.accentColor}"></div>
    </div>
  </div>
</div>

<!-- IMPRINT & COPYRIGHT PAGE (LEFT PAGE) -->
<div class="page left-page imprint-page">
  <div class="inner-content bottom-heavy">
    <div class="legal-text">
       <h4 class="run-in-header">Imprint / Legal</h4>
       <div class="prose-p"><strong>Published by:</strong> {activeBook.frontMatter.imprint.publisher}</div>
       <div class="prose-p">{activeBook.frontMatter.imprint.copyright}</div>
       <div class="prose-p">{activeBook.frontMatter.imprint.license}</div>
       <div class="prose-p"><strong>ISBN:</strong> {activeBook.frontMatter.imprint.isbn}</div>
    </div>
  </div>
</div>

<!-- TABLE OF CONTENTS (RIGHT PAGE) -->
<div class="page right-page toc-page">
  <div class="inner-content">
    <h3 class="toc-title">Contents</h3>
    <ul class="toc-list">
      {#each chapters as chapter, idx}
        <li class="toc-chapter">
          <span class="chap-num">Part {idx + 1}</span>
          <span class="chap-name">{chapter}</span>
        </li>
      {/each}
    </ul>
  </div>
</div>

<!-- PREFACE / HOW TO USE (LEFT PAGE) -->
<div class="page left-page preface-page">
  <div class="inner-content">
    <div class="page-header">
       <h3 class="meta-subtitle" style="color: {activeBook.theme.primaryColor}">Preface</h3>
       <h2 class="concept-title">Hook Intro</h2>
    </div>
    
    <div class="prose-segment">
      <h4 class="run-in-header" style="--accent: {activeBook.theme.primaryColor}">Context & Method</h4>
      <div class="prose-p">{activeBook.frontMatter.preface.hook}</div>
    </div>

    <div class="prose-segment" style="margin-top: 4rem;">
      <h4 class="run-in-header" style="--accent: {activeBook.theme.primaryColor}">How to Use This Book</h4>
      <div class="prose-p">{activeBook.frontMatter.preface.howToUse}</div>
    </div>
  </div>
</div>

<style>
  /* TITLE STYLES */
  .title-page {
    background: #0F172A; 
    color: #F8FAFC;
    border-left: 20px solid #0EA5E9;
  }
  .inner-content {
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    /* Print margins: 25mm top/bottom, 30mm inner, 15mm outer */
    padding: 25mm 15mm 25mm 30mm;
  }
  
  .left-page .inner-content {
    padding: 25mm 30mm 25mm 15mm; /* Flip for left page (inner is right) */
  }

  /* ... rest of title styling mapped into standard Svelte ... */
  .front-meta {
    display: flex;
    justify-content: space-between;
    font-family: var(--font-mono);
    font-size: 0.875rem;
    letter-spacing: 0.3em;
    color: #94A3B8;
    text-transform: uppercase;
  }
  .title-block { margin: auto 0; }
  h1 {
    font-family: var(--font-sans);  font-size: 6rem;
    font-weight: 800; letter-spacing: -0.05em; line-height: 0.95;
    color: #FFFFFF; margin-bottom: 2rem; text-wrap: balance;
  }
  h2 {
    font-family: var(--font-serif); font-size: 2.25rem; font-weight: 300;
    font-style: italic; color: #CBD5E1; max-width: 25ch; line-height: 1.4; text-wrap: balance;
  }
  .colophon-block {
    display: flex; justify-content: space-between; align-items: flex-end;
    border-top: 1px solid #1E293B; padding-top: 2rem;
  }
  .colophon-block .prose-p {
    font-family: var(--font-mono); text-transform: uppercase;
    font-size: 0.75rem; letter-spacing: 0.15em; color: #475569; max-width: 30ch;
  }

  .spine-anchor { width: 3rem; height: 3rem; background: #8B5CF6; border-radius: 50%; opacity: 0.8;}

  /* OTHER PAGES */
  .bottom-heavy { justify-content: flex-end; }
  .legal-text { font-family: var(--font-mono); font-size: 0.875rem; color: #64748B; margin-bottom: 2rem; }
  .legal-text .prose-p { margin-bottom: 0.5rem; }

  .toc-title { font-family: var(--font-sans); font-size: 3rem; font-weight: 800; margin-bottom: 4rem; color: #0F172A; }
  .toc-list { list-style: none; padding: 0; margin: 0; }
  .toc-chapter { display: flex; flex-direction: column; margin-bottom: 2rem; border-bottom: 1px solid #E2E8F0; padding-bottom: 1rem; }
  .chap-num { font-family: var(--font-mono); font-size: 0.875rem; letter-spacing: 0.1em; color: #0EA5E9; margin-bottom: 0.5rem; }
  .chap-name { font-family: var(--font-serif); font-size: 1.5rem; color: #0F172A; }

  /* PREFACE */
  .page-header { margin-bottom: 4rem; }
  .meta-subtitle { font-family: var(--font-mono); font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.2em; color: #0EA5E9; margin-bottom: 1rem; display: inline-block; }
  .concept-title { font-family: var(--font-sans); font-size: 3.5rem; font-weight: 800; line-height: 1.1; letter-spacing: -0.05em; color: #0F172A; text-wrap: balance; }
  .prose-segment .prose-p { font-family: var(--font-serif); font-size: 1.125rem; color: #334155; line-height: 1.8; margin: 0; text-wrap: pretty; }
  .run-in-header { font-family: var(--font-sans); font-weight: 700; font-size: 0.875rem; text-transform: uppercase; letter-spacing: 0.1em; color: #0F172A; margin: 0 0 0.5rem 0; display: block; position: relative; }
  .run-in-header::after { content: ''; display: inline-block; width: 2rem; height: 2px; background: #0EA5E9; vertical-align: middle; margin-left: 0.75rem; }
</style>
