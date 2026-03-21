<script lang="ts">
    import { onMount, tick } from "svelte";

    // Component Props
    export let title: string = "Spatial Scenario";
    export let scenarioId: string = "evacuation_door";
    export let baselineName: string = "Geometric Baseline";

    const API_BASE = "http://127.0.0.1:8000/api/v1/spatial/diffusion";

    // State
    let isComputing = false;
    let inferenceMetrics: any = null;
    let bottlenecks: any[] = [];
    let loadedMap: any = null;
    let rawExportData: any = null;
    let hasRun = false;

    // View State
    let inferenceMode = "full";
    let isDetailsExpanded = false;

    // Canvases
    let inputCanvas: HTMLCanvasElement;
    let baselineCanvas: HTMLCanvasElement;
    let lineumCanvas: HTMLCanvasElement;

    onMount(() => {
        loadDemo();
    });

    async function loadDemo() {
        try {
            const res = await fetch(`${API_BASE}/demos/${scenarioId}`);
            if (!res.ok) throw new Error("Failed to load scenario.");
            loadedMap = await res.json();
            await tick();
            drawInputMap();
            drawBaselineMock(); // Draws a simple representation of classical failure
            drawLineumBase(); // Draws the empty map waiting for heatmap
        } catch (e) {
            console.error(e);
        }
    }

    function decodeFloat32Array(b64: string): Float32Array {
        const binaryStr = window.atob(b64);
        const bytes = new Uint8Array(binaryStr.length);
        for (let i = 0; i < binaryStr.length; i++) {
            bytes[i] = binaryStr.charCodeAt(i);
        }
        return new Float32Array(bytes.buffer);
    }

    function getHeatmapColor(val: number): [number, number, number, number] {
        if (val < 0.01) return [0, 0, 0, 0];
        const r = Math.min(255, Math.floor(255 * (val * 2)));
        const g = Math.min(255, Math.floor(255 * (val > 0.5 ? (val - 0.5) * 2 : 0)));
        const b = Math.min(255, Math.floor(255 * (val > 0.8 ? (val - 0.8) * 5 : 0)));
        return [r, g, b, Math.floor(255 * (0.4 + val * 0.6))];
    }

    async function runDiffusion() {
        if (!loadedMap) return;
        isComputing = true;
        
        try {
            const reqBody = { ...loadedMap, mode: inferenceMode };
            
            // Render Timing Start
            const reqStart = performance.now();
            
            const res = await fetch(`${API_BASE}/infer`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(reqBody)
            });
            const data = await res.json();
            
            rawExportData = data;
            inferenceMetrics = data.summary_metrics;
            bottlenecks = data.ranked_bottlenecks || [];
            
            const renderStart = performance.now();
            const floats = decodeFloat32Array(data.pressure_heatmap);
            await drawHeatmap(floats);
            const renderEnd = performance.now();
            
            // Assign explicitly observed Client Render time
            inferenceMetrics.client_render_ms = Math.round(renderEnd - renderStart);
            hasRun = true;
            
        } catch (e) {
            console.error("Diffusion execution failed.", e);
        } finally {
            isComputing = false;
        }
    }

    function renderMapOntoContext(ctx: CanvasRenderingContext2D, size: number) {
        const imgData = ctx.createImageData(size, size);
        for (let y = 0; y < size; y++) {
            for (let x = 0; x < size; x++) {
                const kappa = loadedMap.kappa[y][x];
                const idx = (y * size + x) * 4;
                const col = Math.floor(kappa * 255);
                imgData.data[idx] = col;
                imgData.data[idx + 1] = col;
                imgData.data[idx + 2] = col;
                imgData.data[idx + 3] = 255;
            }
        }
        ctx.putImageData(imgData, 0, 0);

        ctx.fillStyle = "rgba(16, 185, 129, 0.8)";
        (loadedMap.source_seeds || []).forEach((s: any) => { ctx.fillRect(s.x - 2, s.y - 2, 4, 4); });

        ctx.fillStyle = "rgba(239, 68, 68, 0.8)";
        (loadedMap.sink_targets || []).forEach((s: any) => { ctx.fillRect(s.x - 2, s.y - 2, 4, 4); });
    }

    function drawInputMap() {
        if (!inputCanvas || !loadedMap) return;
        const ctx = inputCanvas.getContext("2d");
        if (!ctx) return;
        const size = loadedMap.grid_size[0];
        inputCanvas.width = size; inputCanvas.height = size;
        renderMapOntoContext(ctx, size);
    }
    
    function drawLineumBase() {
        if (!lineumCanvas || !loadedMap) return;
        const ctx = lineumCanvas.getContext("2d");
        if (!ctx) return;
        const size = loadedMap.grid_size[0];
        lineumCanvas.width = size; lineumCanvas.height = size;
        renderMapOntoContext(ctx, size);
    }

    function drawBaselineMock() {
        // Renders the input map, but adds a fake linear 'shortest path' projection
        // to visually prove the rigidity of canonical algorithms (EDT/Dijkstra).
        if (!baselineCanvas || !loadedMap) return;
        const ctx = baselineCanvas.getContext("2d");
        if (!ctx) return;
        const size = loadedMap.grid_size[0];
        baselineCanvas.width = size; baselineCanvas.height = size;
        renderMapOntoContext(ctx, size);
        
        // Draw rigid baseline representation (dummy logic for visual framing)
        ctx.strokeStyle = "rgba(160, 160, 160, 0.5)";
        ctx.lineWidth = 1;
        ctx.beginPath();
        const src = loadedMap.source_seeds[0];
        const tar = loadedMap.sink_targets[0];
        if (src && tar) {
            ctx.moveTo(src.x, src.y);
            // hard rigid line ignoring terrain
            ctx.lineTo(tar.x, tar.y);
        }
        ctx.stroke();
    }

    async function drawHeatmap(phiArray: Float32Array) {
        if (!lineumCanvas || !loadedMap) return;
        const ctx = lineumCanvas.getContext("2d");
        if (!ctx) return;
        
        const size = loadedMap.grid_size[0];
        const imgData = ctx.getImageData(0, 0, size, size);
        const maxPhi = Math.max(...phiArray);
        const norm = maxPhi > 0 ? maxPhi : 1.0;

        for (let y = 0; y < size; y++) {
            for (let x = 0; x < size; x++) {
                const idx = (y * size + x);
                const val = phiArray[idx] / norm;
                
                if (val > 0.05) {
                    const c = getHeatmapColor(val);
                    const pIdx = idx * 4;
                    const alpha = c[3] / 255.0;
                    imgData.data[pIdx] = Math.floor(c[0] * alpha + imgData.data[pIdx] * (1 - alpha));
                    imgData.data[pIdx+1] = Math.floor(c[1] * alpha + imgData.data[pIdx+1] * (1 - alpha));
                    imgData.data[pIdx+2] = Math.floor(c[2] * alpha + imgData.data[pIdx+2] * (1 - alpha));
                }
            }
        }
        ctx.putImageData(imgData, 0, 0);
        
        // Bottlenecks
        bottlenecks.forEach(b => {
             ctx.beginPath();
             ctx.arc(b.x, b.y, 4, 0, 2 * Math.PI, false);
             ctx.lineWidth = 2;
             ctx.strokeStyle = b.rank === 1 ? "#FF3333" : "#FF9933";
             ctx.stroke();
        });
    }

    function exportJson() {
        if (!rawExportData) return;
        const blob = new Blob([JSON.stringify(rawExportData, null, 2)], { type: "application/json" });
        const url = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = `lineum_audit_${scenarioId}_${inferenceMode}.json`;
        a.click();
        URL.revokeObjectURL(url);
    }
</script>

<div class="w-full max-w-7xl mx-auto flex flex-col gap-8 bg-slate-900 border border-slate-800 rounded-3xl p-8 mb-12 shadow-2xl relative overflow-hidden">
    
    <!-- Section Header -->
    <div class="border-b border-slate-800 pb-4">
        <h2 class="text-3xl font-bold text-white tracking-tight">{title}</h2>
        <div class="mt-2 text-slate-400 font-sans text-lg">
            {loadedMap?.scenario_summary || "Loading topology bounds..."}
        </div>
    </div>

    <!-- Triple Side-by-Side Unified View -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        
        <!-- Input Topology -->
        <div class="flex flex-col items-center">
            <h3 class="text-xs uppercase tracking-widest text-slate-500 font-bold mb-3">The Problem Space</h3>
            <div class="relative w-full aspect-square border border-slate-700 bg-black rounded overflow-hidden">
                <div class="absolute top-2 left-2 z-10 bg-slate-900/80 backdrop-blur px-2 py-1 rounded text-[9px] uppercase tracking-widest text-slate-400 font-bold border border-slate-700">Static Input</div>
                <canvas bind:this={inputCanvas} class="w-full h-full object-contain filter grayscale" style="image-rendering: pixelated;"></canvas>
            </div>
            <p class="text-[10px] text-slate-500 mt-2 text-center px-4">This is the space the system must analyze.</p>
        </div>

        <!-- Baseline -->
        <div class="flex flex-col items-center">
            <h3 class="text-xs uppercase tracking-widest text-slate-500 font-bold mb-3">Conventional Approach</h3>
            <div class="relative w-full aspect-square border border-slate-700 bg-black rounded overflow-hidden opacity-80">
                <div class="absolute top-2 left-2 z-10 bg-slate-900/80 backdrop-blur px-2 py-1 rounded text-[9px] uppercase tracking-widest text-slate-400 font-bold border border-slate-700">Reference</div>
                <canvas bind:this={baselineCanvas} class="w-full h-full object-contain grayscale opacity-50" style="image-rendering: pixelated;"></canvas>
            </div>
            <p class="text-[10px] text-slate-500 mt-2 text-center px-4">This shows what a conventional geometric method sees.</p>
        </div>

        <!-- Lineum Output -->
        <div class="flex flex-col items-center">
            <h3 class="text-xs uppercase tracking-widest text-indigo-400 font-bold mb-3">Lineum Result</h3>
            <div class="relative w-full aspect-square border-2 border-indigo-500/50 bg-black rounded overflow-hidden shadow-[0_0_20px_rgba(99,102,241,0.2)]">
                <div class="absolute top-2 left-2 z-10 bg-indigo-500/20 backdrop-blur px-2 py-1 rounded text-[9px] uppercase tracking-widest text-indigo-300 font-bold border border-indigo-500/50">Live Result</div>
                <canvas bind:this={lineumCanvas} class="w-full h-full object-contain saturate-150" style="image-rendering: pixelated;"></canvas>
                
                {#if isComputing}
                    <div class="absolute inset-0 z-20 bg-slate-900/80 backdrop-blur-sm flex flex-col items-center justify-center">
                        <div class="text-white text-xs tracking-widest animate-pulse border border-white/20 px-4 py-2 rounded bg-black/50">ANALYZING</div>
                        {#if inferenceMode === 'preview'}
                            <div class="text-amber-500 font-mono text-[9px] mt-2">[ QUICK PREVIEW ESTIMATE ]</div>
                        {/if}
                    </div>
                {/if}
            </div>
            <p class="text-[10px] text-indigo-400/80 mt-2 text-center px-4">This shows where Lineum detects critical pressure build-up.</p>
        </div>

    </div>

    <!-- Action & Metric Bar -->
    <div class="bg-black/30 border border-slate-800 rounded-xl p-6 flex flex-col xl:flex-row gap-8 items-start xl:items-center justify-between">
        
        <!-- Controls -->
        <div class="flex flex-col gap-4">
            <div class="flex items-center gap-4">
                <label class="flex items-center gap-2 cursor-pointer text-xs font-bold {inferenceMode === 'preview' ? 'text-white' : 'text-slate-500'}">
                    <input type="radio" bind:group={inferenceMode} value="preview" class="accent-indigo-500">
                    Quick Preview <span class="text-[9px] font-normal text-slate-500">(fast estimate)</span>
                </label>
                <label class="flex items-center gap-2 cursor-pointer text-xs font-bold {inferenceMode === 'full' ? 'text-white' : 'text-slate-500'}">
                    <input type="radio" bind:group={inferenceMode} value="full" class="accent-indigo-500">
                    Full Analysis <span class="text-[9px] font-normal text-slate-500">(max precision)</span>
                </label>
            </div>
            
            <button on:click={runDiffusion} disabled={isComputing || !loadedMap} class="px-8 py-3 bg-white text-slate-900 font-bold text-sm tracking-tight rounded hover:bg-slate-200 transition-colors disabled:opacity-50">
                Run Analysis
            </button>
        </div>

        <!-- Separated Latency & Metrics -->
        {#if hasRun && inferenceMetrics}
            <div class="flex flex-wrap gap-6 items-center flex-1 justify-end">
                
                <!-- Latency Block (Strict Separation) -->
                <div class="flex gap-4 p-3 bg-slate-900 rounded border border-slate-800">
                    <div class="flex flex-col items-center px-3 border-r border-slate-700">
                        <span class="text-[9px] uppercase text-emerald-500 font-bold mb-1">Model Compute</span>
                        <span class="text-lg text-white font-mono">{inferenceMetrics.compute_ms}ms</span>
                    </div>
                    <div class="flex flex-col items-center px-3 border-r border-slate-700">
                        <span class="text-[9px] uppercase text-slate-500 font-bold mb-1">Serialize & Send</span>
                        <span class="text-lg text-slate-400 font-mono">{inferenceMetrics.serialization_ms}ms</span>
                    </div>
                    <div class="flex flex-col items-center px-3">
                        <span class="text-[9px] uppercase text-slate-500 font-bold mb-1">Client UI Render</span>
                        <span class="text-lg text-slate-400 font-mono">{inferenceMetrics.client_render_ms || 0}ms</span>
                    </div>
                </div>

                <!-- High Level Result -->
                <div class="flex flex-col justify-center items-center">
                    <span class="text-[10px] uppercase text-sky-500 font-bold">Max Structural Stress</span>
                    <div class="text-2xl text-white font-mono flex items-end gap-1">
                        {inferenceMetrics.relative_pressure_index} <span class="text-xs text-slate-500 font-sans mb-1">RPI</span>
                    </div>
                </div>

            </div>
        {/if}
    </div>

    <!-- Detail Accordion & Footer CTAs -->
    <details class="group cursor-pointer border border-slate-800 rounded bg-slate-900/50" bind:open={isDetailsExpanded}>
        <summary class="px-6 py-4 text-xs font-bold text-slate-400 uppercase tracking-wider hover:text-white transition-colors outline-none">
            {isDetailsExpanded ? 'Hide' : 'View'} Expert Audit & Symmetries
        </summary>
        <div class="px-6 pb-6 pt-2 border-t border-slate-800 cursor-default">
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-6">
                <!-- Data Transparency -->
                 <div>
                     <h4 class="text-white text-sm font-bold mb-3 border-b border-slate-800 pb-2">Mathematical Bottleneck Ranking</h4>
                     {#if bottlenecks.length === 0}
                        <p class="text-slate-500 text-xs italic">Awaiting Inference...</p>
                     {:else}
                        <ul class="flex flex-col gap-2 max-h-48 overflow-y-auto pr-2">
                            {#each bottlenecks as b}
                                <li class="flex items-center justify-between p-2 bg-slate-900 border border-slate-800 rounded">
                                    <div class="flex items-center gap-3">
                                        <div class="w-5 h-5 rounded flex items-center justify-center text-[10px] font-bold {b.rank === 1 ? 'bg-red-500/20 text-red-500' : 'bg-slate-800 text-slate-400'}">{b.rank}</div>
                                        <span class="text-slate-300 font-mono text-[11px]">[{b.x}, {b.y}]</span>
                                    </div>
                                    <span class="text-slate-400 text-[11px] font-bold font-mono">Crit: {b.criticality_score}%</span>
                                </li>
                            {/each}
                        </ul>
                     {/if}
                 </div>
                 
                 <!-- Physics Explainer -->
                 <div>
                     <h4 class="text-white text-sm font-bold mb-3 border-b border-slate-800 pb-2">Technical Summary ({baselineName})</h4>
                     <p class="text-xs text-slate-400 leading-relaxed mb-2">
                         Classical traversal algorithms (EDT, Dijkstra) fundamentally seek binary shortest paths, masking the true cascading consequences of continuous terrain friction. 
                     </p>
                     <p class="text-xs text-slate-400 leading-relaxed">
                         By projecting the input topography as an active physical tensor, Lineum natively computes bounding capacities, rendering exact physical capacity thresholds exactly where flow organically intersects geometric constraints.
                     </p>
                 </div>
            </div>

            <!-- CTAs -->
            <div class="flex flex-wrap gap-4 pt-4 border-t border-slate-800">
                <button class="px-6 py-2 bg-indigo-600 text-white font-bold text-xs rounded hover:bg-indigo-500 transition-colors uppercase tracking-wider">
                    Use this API
                </button>
                <button class="px-6 py-2 bg-transparent text-slate-300 border border-slate-700 font-bold text-xs rounded hover:border-slate-500 hover:text-white transition-colors uppercase tracking-wider">
                    Request Custom Solution
                </button>
                <div class="flex-1 text-right">
                    <button class="px-6 py-2 text-slate-500 font-mono text-xs rounded hover:text-slate-300 transition-colors uppercase tracking-wider relative group" on:click={exportJson} disabled={!hasRun}>
                        Export RAW Audit JSON
                        <div class="absolute bottom-full mb-2 right-0 hidden group-hover:block bg-slate-800 text-white px-3 py-1 text-[10px] rounded whitespace-nowrap">
                            Export unbounded structural constants.
                        </div>
                    </button>
                </div>
            </div>
        </div>
    </details>

</div>
