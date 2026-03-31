<script lang="ts">
  import { frontMatter } from '$lib/data/frontMatter';

  // Config parameters for physical printing logic
  export let totalPages: number = 34; // This is dynamic based on concepts * 2 + 4 front matter
  export let paperThicknessMm: number = 0.05; // Standard interior paper
  export let mode: 'ebook' | 'print-global' | 'print-eu' = 'ebook';

  $: spineWidthMm = totalPages * paperThicknessMm;
  
  // Dimensions map to standard sizes, allowing the CSS to render true physical millimeter limits
  const dimensions = {
    'ebook': { w: 152, h: 229, b: 0 },
    'print-global': { w: 152, h: 229, b: 3 }, // 6x9 inch + 3mm bleed
    'print-eu': { w: 176, h: 250, b: 3 } // B5 + 3mm bleed
  };

  $: conf = dimensions[mode];
  $: bleed = conf.b;
  $: fullWidthMm = (conf.w * 2) + spineWidthMm + (bleed * 2);
  $: fullHeightMm = conf.h + (bleed * 2);
</script>

<div 
  class="full-print-cover" 
  style="
    width: {fullWidthMm}mm; 
    height: {fullHeightMm}mm; 
    --spine: {spineWidthMm}mm;
    --trim-w: {conf.w}mm;
    --bleed: {bleed}mm;
  "
>
  <!-- Background Canvas -->
  <div class="cover-canvas">
    <svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none" style="position: absolute; inset: 0; z-index: 1;">
       <!-- Subtle paper grain texture + geometric flowing wave -->
       <defs>
          <linearGradient id="wave-grad" x1="0%" y1="0%" x2="100%" y2="100%">
             <stop offset="0%" stop-color="rgba(14, 165, 233, 0.4)" />
             <stop offset="100%" stop-color="rgba(139, 92, 246, 0.4)" />
          </linearGradient>
       </defs>
       <!-- A clean vector flowing across entire spine and front/back -->
       <path d="M 0,20 Q 30,50 60,10 T 120,80 T 180,30" stroke="url(#wave-grad)" stroke-width="0.3" fill="none" class="vector-wave" />
       <path d="M -10,150 Q 50,120 80,180 T 200,100" stroke="rgba(14, 165, 233, 0.2)" stroke-width="0.5" fill="none" class="vector-wave" />
    </svg>
  </div>

  <!-- Physical layout grid matching printer templates -->
  <div class="spine-grid">
    <!-- BACK COVER -->
    <div class="back-cover panel">
      <div class="safe-zone">
        <h3 class="subtitle">{frontMatter.subtitle}</h3>
        <p class="blurb">{frontMatter.preface.hook}</p>
        
        <div class="bottom-group">
          <div class="isbn-box">
             <div class="barcode">|||||| ||| || |||</div>
             <span>{frontMatter.imprint.isbn}</span>
          </div>
          <div class="author-block">
             <span>{frontMatter.imprint.copyright}</span>
          </div>
        </div>
      </div>
    </div>

    <!-- SPINE -->
    <div class="spine-strip">
       <span class="spine-title">{frontMatter.title}</span>
    </div>

    <!-- FRONT COVER -->
    <div class="front-cover panel">
      <div class="safe-zone">
         <div class="branding">
            LINEUM
         </div>
         <h1 class="main-title">{frontMatter.title}</h1>
         <h2 class="sub-title">A Simple Way to Finally<br/>Understand Math Through Shapes.</h2>
         
         <div class="author-label">Tomáš Tříska</div>
      </div>
    </div>
  </div>
</div>

<style>
  .full-print-cover {
    position: relative;
    background: #F8FAFC; /* Neutral light base as requested */
    overflow: hidden;
    /* CSS scales exactly to the Playwright generated PDF size */
  }

  .cover-canvas {
    position: absolute; inset: 0; z-index: 1;
  }
  .vector-wave {
    vector-effect: non-scaling-stroke;
  }

  .spine-grid {
    position: absolute; inset: 0; z-index: 2;
    display: flex;
    flex-direction: row;
  }

  .panel {
    width: calc(var(--trim-w) + var(--bleed));
    height: 100%;
    position: relative;
  }
  
  .back-cover { padding-right: var(--bleed); } /* Spine is at right of back cover */
  .front-cover { padding-left: var(--bleed); } /* Spine is at left of front cover */
  
  .safe-zone {
    /* Hard 10mm safety margin from trims */
    position: absolute;
    inset: calc(var(--bleed) + 15mm);
    display: flex;
    flex-direction: column;
  }

  /* SPINE */
  .spine-strip {
    width: var(--spine);
    height: 100%;
    background: #FFFFFF;
    border-left: 0.5px solid #E2E8F0;
    border-right: 0.5px solid #E2E8F0;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .spine-title {
    writing-mode: vertical-rl;
    text-orientation: mixed;
    transform: rotate(180deg);
    font-family: var(--font-sans);
    font-size: 0.5rem; /* Will be tiny because page counts are small */
    letter-spacing: 0.1em;
    font-weight: 700;
    color: #475569;
    white-space: nowrap;
  }

  /* FRONT COVER TYPOGRAPHY */
  .branding {
    font-family: var(--font-mono); font-size: 0.75rem; letter-spacing: 0.3em; color: #0EA5E9; margin-bottom: auto;
  }
  .main-title {
    font-family: var(--font-sans); font-size: 4rem; font-weight: 800; letter-spacing: -0.05em; color: #0F172A; text-wrap: balance; line-height: 1; margin: 0 0 1rem 0;
  }
  .sub-title {
    font-family: var(--font-serif); font-size: 1.25rem; font-weight: 400; font-style: italic; color: #334155; text-wrap: balance; line-height: 1.4; margin: 0 0 auto 0;
  }
  .author-label {
    font-family: var(--font-mono); font-size: 0.875rem; letter-spacing: 0.1em; color: #475569; text-transform: uppercase;
  }

  /* BACK COVER TYPOGRAPHY */
  .subtitle { font-family: var(--font-sans); font-size: 1rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #0EA5E9; margin-bottom: 2rem; }
  .blurb { font-family: var(--font-serif); font-size: 1rem; color: #334155; line-height: 1.6; text-wrap: pretty; }
  
  .bottom-group { margin-top: auto; display: flex; justify-content: space-between; align-items: flex-end; }
  .isbn-box { display: flex; flex-direction: column; align-items: center; background: #FFF; padding: 10px; border: 1px solid #E2E8F0; }
  .barcode { font-family: monospace; font-size: 1.5rem; letter-spacing: -2px; color: #0F172A; }
  .isbn-box span { font-family: var(--font-mono); font-size: 0.5rem; color: #64748B; margin-top: 5px; }
  .author-block { font-family: var(--font-mono); font-size: 0.6rem; color: #94A3B8; }
</style>
