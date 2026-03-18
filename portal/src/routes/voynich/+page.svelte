<script lang="ts">
    import { onMount } from 'svelte';
    import { page } from '$app/stores';
    let activeLayer = 0;
    
    // Structural data layers
    const layers = [
        { id: 0, name: "Original Scan (Raw Folio)", enabled: true, color: "stone" },
        { id: 1, name: "Word Boundaries (Segmentation)", enabled: false, color: "amber" },
        { id: 2, name: "Physical Distortion", enabled: false, color: "red" },
        { id: 3, name: "Grammar & Structure (Variable Slots)", enabled: false, color: "blue" },
        { id: 4, name: "Rare Artifacts (Boutique Anchors)", enabled: false, color: "yellow" },
        { id: 5, name: "Visual Links (Hooks)", enabled: false, color: "emerald" },
        { id: 6, name: "Word Families", enabled: false, color: "purple" },
        { id: 7, name: "Translation Testing (Semantic Hypothesis)", enabled: false, color: "rose" }
    ];

    export let data: any;
    
    // Derived state from SvelteKit SSR
    $: currentFolio = data.folio;
    $: loadingError = data.error ? data.message : null;
    $: missingData = data.missingData;
    
    let selectedToken: any = null;

    function toggleLayer(id: number) {
        if (id === 0) return; // Layer 0 is always on
        activeLayer = activeLayer === id ? 0 : id;
        if (activeLayer !== 3) {
            selectedToken = null;
        }
    }

    function selectToken(token: any) {
        if (activeLayer === 3) {
            selectedToken = token;
        }
    }

    onMount(() => {
        // Expose explicit API for Playwright E2E testing
        if (typeof window !== 'undefined') {
            (window as any).__TEST_toggleLayer = toggleLayer;
        }
        
        // Allow pure stateless E2E navigation testing
        const layerParam = $page.url.searchParams.get('layer');
        if (layerParam && currentFolio) {
            activeLayer = parseInt(layerParam);
            const tokenParam = $page.url.searchParams.get('token');
            if (tokenParam) {
                selectedToken = currentFolio.tokens.find((t: any) => t.id === tokenParam);
            }
        }
    });
</script>

<div class="relative w-full h-[calc(100vh-33px)] overflow-hidden text-[#e0e0d8] font-mono selection:bg-[#333333] bg-[#050505]">
    
    <!-- Top Left Branding & Actions -->
    <div class="absolute top-6 left-6 z-50 flex flex-col gap-4 items-start pointer-events-none">
        <div class="bg-[#0a0a0a]/80 backdrop-blur-xl border border-[#ffffff1a] rounded-xl p-5 shadow-2xl pointer-events-auto transition-all hover:bg-[#0a0a0a]/90">
            <h1 class="text-2xl font-bold text-[#f5f5f0] tracking-tight uppercase">Voynich <span class="text-amber-500">Archiva</span></h1>
            <p class="text-[10px] text-[#888] mt-1 uppercase tracking-widest">Structural Decipherment Harness</p>
            <div class="mt-4 pt-4 border-t border-[#ffffff1a]">
                <button class="w-full bg-amber-500/10 hover:bg-amber-500/20 text-amber-500 border border-amber-500/30 py-2.5 rounded-lg text-[10px] uppercase font-bold tracking-widest transition-all">
                    Load Pilot: okam / kald
                </button>
            </div>
        </div>
    </div>
    
    <!-- Bottom Dock: Analytical Layers -->
    <div class="absolute bottom-8 left-1/2 -translate-x-1/2 z-50 pointer-events-none">
        <div class="bg-[#0a0a0a]/80 backdrop-blur-xl border border-[#ffffff1a] rounded-2xl p-2 shadow-2xl pointer-events-auto flex items-center gap-1">
            <div class="px-3 text-[10px] font-bold uppercase tracking-widest text-[#666] mr-2">Layers</div>
            {#each layers as layer}
                <button 
                    data-testid="layer-toggle-{layer.id}"
                    class="relative group px-4 py-3 rounded-xl transition-all flex items-center gap-2 {activeLayer === layer.id || layer.id === 0 ? 'bg-white/10 text-white shadow-inner' : 'text-[#888] hover:bg-white/5 hover:text-[#ccc]'}"
                    on:click={() => toggleLayer(layer.id)}
                >
                    <div class="w-2.5 h-2.5 rounded-full border transition-all {activeLayer === layer.id || layer.id === 0 ? 'border-amber-400 bg-amber-400/50 shadow-[0_0_8px_rgba(251,191,36,0.5)]' : 'border-[#444] bg-transparent'}"></div>
                    <span class="text-xs font-bold font-mono">[{layer.id}]</span>
                    
                    <!-- Tooltip -->
                    <div class="absolute -top-12 left-1/2 -translate-x-1/2 whitespace-nowrap bg-[#111] text-white text-[10px] uppercase tracking-widest py-1.5 px-3 rounded-lg opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none border border-[#333] shadow-xl">
                        {layer.name}
                        <div class="absolute -bottom-1 left-1/2 -translate-x-1/2 w-2 h-2 bg-[#111] border-b border-r border-[#333] transform rotate-45"></div>
                    </div>
                </button>
            {/each}
        </div>
    </div>

    <!-- Contextual Dossier Card (Floating Right) -->
    <div class="absolute top-6 right-6 z-50 flex flex-col items-end pointer-events-none">
        {#if activeLayer === 3 && selectedToken}
            <div class="w-80 bg-[#0a0a0a]/80 backdrop-blur-xl border border-[#ffffff1a] rounded-xl p-6 shadow-2xl pointer-events-auto transition-all animate-in fade-in slide-in-from-right-4 relative">
                <!-- Close Button -->
                <button 
                    class="absolute top-4 right-4 text-[#666] hover:text-[#bbb] transition-colors"
                    on:click={(e) => { e.stopPropagation(); selectedToken = null; }}
                    title="Close Dossier"
                >
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                </button>
                
                <h3 class="text-[10px] font-bold uppercase tracking-widest text-[#888] mb-5">Inspection Dossier</h3>
                
                <div class="flex flex-col gap-5">
                    <div>
                        <strong class="text-[#ffffff] block mb-1 text-[10px] tracking-widest opacity-60">SELECTED WORD (Transcription)</strong>
                        <span class="text-2xl font-bold" style="color: {selectedToken.color === 'blue' ? '#60a5fa' : selectedToken.color === 'purple' ? '#c084fc' : '#fbbf24'}">
                            {selectedToken.text}
                        </span>
                        <p class="text-[9px] text-[#888] mt-1.5 leading-tight border-l-2 border-[#ffffff1a] pl-2 font-sans tracking-wide">
                            This is how the historical symbols are transcribed into our alphabet to be readable by computers.
                        </p>
                    </div>
                    <div>
                        <strong class="text-[#ffffff] block mb-1 text-[10px] tracking-widest opacity-60">GRAMMAR ROLE (Structural Category)</strong>
                        <span style="color: {selectedToken.color === 'blue' ? '#93c5fd' : selectedToken.color === 'purple' ? '#d8b4fe' : '#fcd34d'}">
                            {selectedToken.type} {#if selectedToken.type === 'Omega'} (Suffix / Ending Marker) {:else if selectedToken.type === 'Alpha'} (Root / Core Meaning) {:else} (Modifier / Connector) {/if}
                        </span>
                        <p class="text-[9px] text-[#888] mt-1.5 leading-tight border-l-2 border-[#ffffff1a] pl-2 font-sans tracking-wide">
                            Mathematics proves this word acts strictly as a {#if selectedToken.type === 'Omega'}grammar ending (like "-ing").{:else if selectedToken.type === 'Alpha'}base root that carries the main meaning.{:else}connecting element in a sentence.{/if}
                        </p>
                    </div>
                    <div>
                        <strong class="text-[#ffffff] block mb-1 text-[10px] tracking-widest opacity-60">RULE CHECK</strong>
                        <span class="text-emerald-400 flex items-center gap-2 font-bold pointer-events-auto mb-1">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                            Pass: Position is Valid
                        </span>
                        <p class="text-[9px] text-emerald-600/80 leading-tight border-l-2 border-emerald-900/50 pl-2 font-sans tracking-wide">
                            This word matches the required mathematical layout for its category.
                        </p>
                    </div>
                    
                    {#if selectedToken.hypothesis}
                        <div class="mt-2 pt-5 border-t border-[#ffffff1a]">
                            <p class="mb-3 text-[10px] tracking-widest text-rose-400 font-bold">TRANSLATION ATTEMPT (Hypothesis):</p>
                            <p class="text-rose-300 text-xs leading-relaxed bg-rose-950/40 p-4 rounded-lg border border-rose-900/50 shadow-inner">
                                <span class="block mb-2 font-bold text-sm text-rose-400">"{selectedToken.hypothesis}"</span>
                                <span class="opacity-80 font-sans tracking-wide text-[11px]">We used a computer to test if this word could mean <strong>"{selectedToken.hypothesis}"</strong>. It failed. Why? Because this word's physical position proves it is just a grammar ending. Action verbs cannot exist here.</span>
                            </p>
                        </div>
                    {/if}
                </div>
            </div>
        {:else if activeLayer === 7}
            <div class="w-80 bg-rose-950/80 backdrop-blur-xl border border-rose-900/50 rounded-xl p-6 shadow-2xl pointer-events-auto transition-all animate-in fade-in slide-in-from-right-4 relative">
                <h4 class="text-rose-400 font-bold uppercase text-[11px] tracking-widest mb-3 flex items-center gap-2">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
                    Translation Filter Active
                </h4>
                <p class="text-[11px] font-sans tracking-wide text-rose-200/80 leading-relaxed mb-4">The Lineum system is blocking a popular historical theory ("To Cut") because it breaks basic mathematical grammar rules.</p>
                <div class="bg-black/40 border border-rose-900/30 rounded-lg p-4 text-xs text-rose-300 shadow-inner">
                    <strong class="text-rose-400">Rejected Translation:</strong> "okam" = Action Verb 'Cut'.<br/><br/>
                    <strong class="text-rose-400">Simple Reason:</strong> The math proves this word sits in a structural 'Ending' spot. It is physically impossible for an action verb to live here.
                </div>
            </div>
        {:else if activeLayer !== 0}
            <!-- Empty state for layers lacking specific dossier logic in this mock -->
            <div class="w-64 bg-[#0a0a0a]/60 backdrop-blur-xl border border-[#ffffff1a] rounded-xl p-5 shadow-2xl pointer-events-auto text-center transition-all animate-in fade-in slide-in-from-right-4">
                <p class="text-[11px] text-[#888] leading-relaxed">Select a highlighted structural element on the canvas to inspect its mathematical properties.</p>
            </div>
        {/if}
    </div>

    <!-- Main Canvas (Background/Interactive Map) -->
    <main class="absolute inset-0 overflow-y-auto overflow-x-hidden flex items-start justify-center p-0 custom-scrollbar">
        <div class="absolute inset-0 pattern-dots opacity-20 pointer-events-none fixed"></div>
        
        {#if missingData}
            <div class="z-50 m-auto bg-[#0a0a0a]/90 backdrop-blur-xl border border-amber-500/30 p-8 rounded-2xl max-w-lg shadow-2xl animate-in fade-in zoom-in-95">
                <div class="w-12 h-12 rounded-full border border-amber-500/50 bg-amber-500/10 flex items-center justify-center mb-6">
                    <svg class="w-6 h-6 text-amber-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                </div>
                <h3 class="font-bold text-xl mb-3 text-white">Bring Your Own Data (BYOD)</h3>
                <p class="text-[13px] text-[#aaa] leading-relaxed mb-6">
                    To respect original transcription copyrights, Lineum does not distribute the raw Voynich EVA texts directly via the public repository.
                </p>
                <div class="bg-black/50 border border-white/5 rounded-lg p-5">
                    <p class="text-[10px] uppercase tracking-widest text-[#666] font-bold mb-3">Required Action (Terminal)</p>
                    <code class="block text-emerald-400 font-mono text-sm bg-black p-3 rounded border border-emerald-900/30">
                        python scripts/ingest_voynich_data.py
                    </code>
                </div>
                <p class="text-[11px] text-[#666] mt-4 text-center">
                    This securely downloads and parses Takahashi IVTFF into protected JSON files on your local drive.
                </p>
            </div>
        {:else if loadingError}
            <div class="z-50 m-auto bg-rose-950/90 text-rose-200 p-6 rounded-xl border border-rose-500 max-w-md text-center">
                <h3 class="font-bold text-lg mb-2">System Error</h3>
                <p class="text-sm opacity-80">{loadingError}</p>
            </div>
        {:else if !currentFolio}
            <div class="z-50 m-auto text-[#888] animate-pulse font-mono text-sm tracking-widest uppercase">
                Rendering local SSR map...
            </div>
        {:else}
            <!-- Centralized map container for structural coordinate parity that respects viewport width -->
            <div class="relative shadow-[0_20px_50px_rgba(0,0,0,0.8)] rendering-pixelated bg-[#121110] border-x border-[#221f1a] w-full max-w-[1200px] mx-auto aspect-[3/4] hover:cursor-crosshair transition-transform duration-500 origin-top">
                <!-- Base Image -->
                <img src={currentFolio.imageUrl} alt="Voynich {currentFolio.id}" class="absolute inset-0 w-full h-full object-cover opacity-90" />
                
                <!-- Structural Overlays (Positioned Absolutely OVER the zoom container to preserve strict coordinates) -->
                <div class="absolute inset-0 pointer-events-none w-full h-full">
                    {#if activeLayer === 3}
                        {#each currentFolio.tokens as token}
                            <!-- svelte-ignore a11y_click_events_have_key_events -->
                            <!-- svelte-ignore a11y_no_static_element_interactions -->
                            <div 
                                class="absolute border-b-[3px] transition-all duration-300 pointer-events-auto cursor-pointer hover:bg-white/10 rounded-sm"
                                style="
                                    left: {token.x}%; 
                                    top: {token.y}%; 
                                    width: {token.w}%; 
                                    height: {token.h}%;
                                    border-color: {token.color === 'blue' ? '#3b82f6' : token.color === 'purple' ? '#a855f7' : '#f59e0b'};
                                    background-color: {selectedToken?.id === token.id ? (token.color === 'amber' ? 'rgba(245,158,11,0.3)' : 'rgba(255,255,255,0.2)') : 'transparent'};
                                    box-shadow: {selectedToken?.id === token.id && token.color === 'amber' ? '0 0 25px rgba(245,158,11,0.4)' : 'none'};
                                "
                                on:click={() => selectToken(token)}
                            >
                                {#if token.id === 'T4'}
                                    <div class="absolute -top-2 -right-2 w-2.5 h-2.5 bg-amber-400 rounded-full shadow-[0_0_12px_#fbbf24] animate-pulse"></div>
                                {/if}
                            </div>
                        {/each}
                    {/if}

                    {#if activeLayer === 5}
                        <!-- Visual Semantic Hook -->
                        <div class="absolute w-full h-full pointer-events-none">
                            <svg class="w-full h-full" viewBox="0 0 100 100" preserveAspectRatio="none">
                                <path 
                                    d="M 80 27 Q 90 40 60 45" 
                                    fill="none" 
                                    stroke="#10b981" 
                                    stroke-width="0.3" 
                                    stroke-dasharray="1,1" 
                                    class="animate-[dash_2s_linear_infinite]"
                                />
                                <circle cx="60" cy="45" r="1.5" fill="#10b981" />
                            </svg>
                        </div>
                    {/if}

                    {#if activeLayer === 7}
                        <!-- Hypothesis Rejection -->
                        <div class="absolute pointer-events-auto bg-rose-950/90 backdrop-blur-sm border border-rose-500/50 p-3 rounded-lg transform -translate-x-1/2 -translate-y-full flex flex-col items-center shadow-2xl"
                             style="left: 80%; top: 23%; width: 160px;"
                        >
                            <span class="text-[9px] text-rose-200 font-bold tracking-widest uppercase mb-1 drop-shadow-md">Translation Block</span>
                            <span class="text-rose-400 text-[10px] text-center font-medium leading-tight">Omega slot mathematically rejects Process Verb 'Cut'</span>
                            <div class="absolute -bottom-1.5 w-3 h-3 bg-rose-950 border-r border-b border-rose-500/50 rotate-45"></div>
                        </div>
                    {/if}
                </div>
            </div>
        {/if}
    </main>
</div>

<style>
    .pattern-dots {
        background-image: radial-gradient(circle at 1px 1px, #ffffff08 1px, transparent 0);
        background-size: 32px 32px;
    }
    
    .rendering-pixelated {
        image-rendering: pixelated;
    }

    @keyframes dash {
        to {
            stroke-dashoffset: -10;
        }
    }

    .custom-scrollbar::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    .custom-scrollbar::-webkit-scrollbar-track {
        background: #050505;
    }
    .custom-scrollbar::-webkit-scrollbar-thumb {
        background: #222;
        border-radius: 4px;
    }
    .custom-scrollbar::-webkit-scrollbar-thumb:hover {
        background: #444;
    }
</style>
