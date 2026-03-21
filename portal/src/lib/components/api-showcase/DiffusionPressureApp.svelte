<script lang="ts">
    import { onMount, tick } from "svelte";

    // The backend base URL (matches dev environment Vite proxies or prod domains)
    const API_BASE = "http://127.0.0.1:8000/api/v1/spatial/diffusion";

    // UX State
    let activeScenario = "evacuation_door";
    let inferenceMode = "full";
    let isComputing = false;
    let inferenceMetrics: any = null;
    let bottlenecks: any[] = [];
    let canvas: HTMLCanvasElement;
    let ctx: CanvasRenderingContext2D | null = null;
    let loadedMap: any = null;
    let rawExportData: any = null;
    
    // PACK-A State
    let iterations = 1500;
    let laplaceCutoff = 0.1;
    let prevPrimaryBottleneck: any = null;
    let rankInversionWarning = false;

    // Load a preset from the backend
    async function loadDemo(scenario_id: string) {
        activeScenario = scenario_id;
        inferenceMetrics = null;
        rawExportData = null;
        bottlenecks = [];
        prevPrimaryBottleneck = null;
        rankInversionWarning = false;
        
        try {
            const res = await fetch(`${API_BASE}/demos/${scenario_id}`);
            if (!res.ok) throw new Error("Failed to load scenario.");
            loadedMap = await res.json();
            drawMapBase();
        } catch (e) {
            console.error(e);
        }
    }

    // Unpack Float32 from Base64 String
    function decodeFloat32Array(b64: string): Float32Array {
        const binaryStr = window.atob(b64);
        const bytes = new Uint8Array(binaryStr.length);
        for (let i = 0; i < binaryStr.length; i++) {
            bytes[i] = binaryStr.charCodeAt(i);
        }
        return new Float32Array(bytes.buffer);
    }

    // Map a scalar [0..1] to an Inferno-ish heatmap string
    // Red -> Yellow -> White for max pressure
    function getHeatmapColor(val: number): [number, number, number, number] {
        if (val < 0.01) return [0, 0, 0, 0]; // Transparent zero
        
        // Simple Jet/Inferno approximation
        const r = Math.min(255, Math.floor(255 * (val * 2)));
        const g = Math.min(255, Math.floor(255 * (val > 0.5 ? (val - 0.5) * 2 : 0)));
        const b = Math.min(255, Math.floor(255 * (val > 0.8 ? (val - 0.8) * 5 : 0)));
        
        return [r, g, b, Math.floor(255 * (0.4 + val * 0.6))];
    }

    // Execute Inference Pipeline
    async function runDiffusion(telemetry: boolean = false) {
        if (!loadedMap) return;
        isComputing = true;
        
        try {
            const reqBody = { 
                ...loadedMap, 
                mode: inferenceMode,
                diffusion_params: {
                    ...loadedMap.diffusion_params,
                    max_iterations: iterations,
                    laplace_cutoff: -laplaceCutoff,
                    enable_telemetry: telemetry
                }
            };
            const res = await fetch(`${API_BASE}/infer`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(reqBody)
            });
            const data = await res.json();
            
            rawExportData = data;
            inferenceMetrics = data.summary_metrics;
            const newBottlenecks = data.ranked_bottlenecks || [];
            
            // Validate Bottleneck Drift
            if (prevPrimaryBottleneck && newBottlenecks.length > 0) {
                const b1 = newBottlenecks[0];
                const pb = prevPrimaryBottleneck;
                const dist = Math.sqrt(Math.pow(b1.x - pb.x, 2) + Math.pow(b1.y - pb.y, 2));
                rankInversionWarning = dist > 5;
            } else {
                rankInversionWarning = false;
            }
            if (newBottlenecks.length > 0) {
                prevPrimaryBottleneck = { ...newBottlenecks[0] };
            }
            bottlenecks = newBottlenecks;
            
            const floats = decodeFloat32Array(data.pressure_heatmap);
            drawHeatmap(floats);

        } catch (e) {
            console.error("Diffusion execution failed.", e);
        } finally {
            isComputing = false;
        }
    }

    function exportJson() {
        if (!rawExportData) return;
        const blob = new Blob([JSON.stringify(rawExportData, null, 2)], { type: "application/json" });
        const url = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = `diffusion_inference_${activeScenario}_${inferenceMode}.json`;
        a.click();
        URL.revokeObjectURL(url);
    }

    // Base Rendering (Kappa / Friction array)
    function drawMapBase() {
        if (!canvas || !loadedMap) return;
        ctx = canvas.getContext("2d");
        if (!ctx) return;

        const size = loadedMap.grid_size[0];
        canvas.width = size;
        canvas.height = size;

        const imgData = ctx.createImageData(size, size);
        for (let y = 0; y < size; y++) {
            for (let x = 0; x < size; x++) {
                const kappa = loadedMap.kappa[y][x];
                const idx = (y * size + x) * 4;
                
                // Low kappa = black wall, High kappa = empty space
                const col = Math.floor(kappa * 255);
                imgData.data[idx] = col;
                imgData.data[idx + 1] = col;
                imgData.data[idx + 2] = col;
                imgData.data[idx + 3] = 255;
            }
        }
        ctx.putImageData(imgData, 0, 0);

        // Draw seeds (Sources)
        ctx.fillStyle = "rgba(16, 185, 129, 0.8)";
        (loadedMap.source_seeds || []).forEach((s: any) => {
            ctx!.fillRect(s.x - 2, s.y - 2, 4, 4);
        });

        // Draw targets (Sinks)
        ctx.fillStyle = "rgba(239, 68, 68, 0.8)";
        (loadedMap.sink_targets || []).forEach((s: any) => {
            ctx!.fillRect(s.x - 2, s.y - 2, 4, 4);
        });
    }

    function drawHeatmap(phiArray: Float32Array) {
        if (!ctx || !loadedMap) return;
        
        const size = loadedMap.grid_size[0];
        // Overlay heatmap onto current canvas
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
                    // Alpha composite
                    const alpha = c[3] / 255.0;
                    imgData.data[pIdx] = Math.floor(c[0] * alpha + imgData.data[pIdx] * (1 - alpha));
                    imgData.data[pIdx+1] = Math.floor(c[1] * alpha + imgData.data[pIdx+1] * (1 - alpha));
                    imgData.data[pIdx+2] = Math.floor(c[2] * alpha + imgData.data[pIdx+2] * (1 - alpha));
                }
            }
        }
        ctx.putImageData(imgData, 0, 0);
        
        // Draw Bottleneck Rings
        bottlenecks.forEach(b => {
             ctx!.beginPath();
             ctx!.arc(b.x, b.y, 4, 0, 2 * Math.PI, false);
             ctx!.lineWidth = 2;
             ctx!.strokeStyle = b.rank === 1 ? "#FF3333" : "#FF9933";
             ctx!.stroke();
        });
    }

    onMount(() => {
        loadDemo("evacuation_door");
    });
</script>

<div class="w-full max-w-6xl mx-auto flex flex-col lg:flex-row gap-8 bg-slate-900 border border-slate-800 rounded-3xl p-8 relative overflow-hidden">
    <!-- Left Panel: Rendering & Controls -->
    <div class="flex-1 flex flex-col items-center">
        <!-- Scenario Selectors -->
        <div class="flex gap-2 mb-6 flex-wrap justify-center">
            <button class="px-4 py-2 text-xs font-bold uppercase tracking-wider rounded-lg transition-colors border {activeScenario === 'evacuation_door' ? 'bg-indigo-500/20 text-indigo-400 border-indigo-500/50' : 'bg-slate-800 text-slate-400 border-transparent hover:text-white'}" on:click={() => loadDemo('evacuation_door')}>
                Evacuation Crush
            </button>
            <button class="px-4 py-2 text-xs font-bold uppercase tracking-wider rounded-lg transition-colors border {activeScenario === 'narrow_tunnel' ? 'bg-indigo-500/20 text-indigo-400 border-indigo-500/50' : 'bg-slate-800 text-slate-400 border-transparent hover:text-white'}" on:click={() => loadDemo('narrow_tunnel')}>
                N. Tunnel
            </button>
            <button class="px-4 py-2 text-xs font-bold uppercase tracking-wider rounded-lg transition-colors border {activeScenario === 'wide_corridor' ? 'bg-indigo-500/20 text-indigo-400 border-indigo-500/50' : 'bg-slate-800 text-slate-400 border-transparent hover:text-white'}" on:click={() => loadDemo('wide_corridor')}>
                W. Corridor
            </button>
            <button class="px-4 py-2 text-xs font-bold uppercase tracking-wider rounded-lg transition-colors border {activeScenario === 'branching' ? 'bg-indigo-500/20 text-indigo-400 border-indigo-500/50' : 'bg-slate-800 text-slate-400 border-transparent hover:text-white'}" on:click={() => loadDemo('branching')}>
                Branching
            </button>
            <button class="px-4 py-2 text-xs font-bold uppercase tracking-wider rounded-lg transition-colors border {activeScenario === 'pegs' ? 'bg-indigo-500/20 text-indigo-400 border-indigo-500/50' : 'bg-slate-800 text-slate-400 border-transparent hover:text-white'}" on:click={() => loadDemo('pegs')}>
                Pegs
            </button>
        </div>

        <div class="relative w-[384px] h-[384px] md:w-[512px] md:h-[512px] border border-slate-700 bg-black rounded-lg overflow-hidden shadow-[0_0_30px_rgba(0,0,0,0.5)]">
            <canvas bind:this={canvas} class="w-full h-full object-contain filter contrast-125 saturate-150" style="image-rendering: pixelated;"></canvas>
            
            {#if isComputing}
                <div class="absolute inset-0 bg-slate-900/80 backdrop-blur-sm flex flex-col gap-4 items-center justify-center">
                    <div class="text-white font-bold tracking-widest animate-pulse border border-white/20 px-6 py-3 rounded-full bg-black/50">SOLVING DIFFERENTIALS</div>
                    {#if inferenceMode === 'preview'}
                        <div class="text-amber-500 font-mono text-sm">[ FAST PREVIEW ESTIMATE ]</div>
                    {/if}
                </div>
            {/if}
        </div>
        
        <div class="mt-4 p-4 lg:w-[512px] bg-slate-800/50 border border-slate-700/50 rounded-lg text-sm text-slate-300 leading-relaxed shadow-inner">
            {loadedMap?.scenario_summary || "Loading topology bounds..."}
        </div>

        <div class="mt-8 flex flex-col gap-4 w-full px-4 lg:w-[512px]">
            <!-- PACK A Sensitivity Calibration Options -->
            <div class="bg-indigo-900/10 border border-indigo-500/20 p-4 rounded-xl flex flex-col gap-4">
                <div class="text-xs uppercase tracking-widest text-indigo-400 font-bold mb-1">Sensitivity Calibration (Pack-A)</div>
                
                <div class="flex flex-col gap-2">
                    <label class="text-xs text-slate-400 font-bold flex justify-between">
                        <span>Iterations</span>
                        <span class="text-white bg-slate-800 px-2 py-1 rounded font-mono">{iterations}</span>
                    </label>
                    <input type="range" min="300" max="5000" step="100" bind:value={iterations} class="accent-indigo-500">
                </div>
                
                <div class="flex flex-col gap-2">
                    <label class="text-xs text-slate-400 font-bold flex justify-between">
                        <span>Laplace Threshold (-x)</span>
                        <span class="text-white bg-slate-800 px-2 py-1 rounded font-mono">{laplaceCutoff.toFixed(2)}</span>
                    </label>
                    <input type="range" min="0.01" max="0.50" step="0.01" bind:value={laplaceCutoff} class="accent-indigo-500">
                </div>
                
                {#if rankInversionWarning}
                    <div class="mt-2 text-[10px] sm:text-xs font-bold text-red-400 bg-red-500/10 border border-red-500/20 px-3 py-2 rounded">
                        ⚠️ WARNING: Primary Bottleneck shifted out of stability bounds!
                    </div>
                {/if}
            </div>
            <div class="flex flex-col sm:flex-row items-center justify-center gap-6 bg-slate-900 border border-slate-800 p-3 rounded-xl shadow-inner">
                <label class="flex items-center gap-2 cursor-pointer text-sm font-bold {inferenceMode === 'preview' ? 'text-white' : 'text-slate-500 hover:text-slate-400'}">
                    <input type="radio" bind:group={inferenceMode} value="preview" class="accent-indigo-500 w-4 h-4">
                    Preview (300 iters)
                </label>
                <label class="flex items-center gap-2 cursor-pointer text-sm font-bold {inferenceMode === 'full' ? 'text-white' : 'text-slate-500 hover:text-slate-400'}">
                    <input type="radio" bind:group={inferenceMode} value="full" class="accent-indigo-500 w-4 h-4">
                    Full Analysis
                </label>
            </div>
            
            <div class="flex gap-4">
                <button 
                    class="flex-1 py-3 px-6 rounded-xl font-bold uppercase tracking-wider transition-all {isComputing ? 'bg-indigo-900 text-indigo-500 cursor-not-allowed' : 'bg-indigo-600 hover:bg-indigo-500 text-white shadow hover:shadow-lg hover:-translate-y-0.5'}"
                    on:click={() => runDiffusion(false)}
                    disabled={isComputing}
                >
                    {isComputing ? 'Computing...' : 'Run Diffusion Analysis'}
                </button>
                <button 
                    class="py-3 px-6 rounded-xl font-bold tracking-wider transition-all border {isComputing ? 'border-slate-800 text-slate-600 cursor-not-allowed' : 'border-indigo-500/50 text-indigo-400 hover:bg-indigo-500/10'}"
                    on:click={() => runDiffusion(true)}
                    disabled={isComputing}
                    title="Run Convergence Trace (Pack-B)"
                >
                    Trace
                </button>
            </div>
            
            {#if rawExportData && rawExportData.telemetry_log && rawExportData.telemetry_log.length > 0}
            <div class="mt-4 bg-slate-950 border border-slate-800 rounded-lg p-3 max-h-64 overflow-y-auto">
                <div class="text-[10px] text-indigo-500 font-bold uppercase tracking-widest mb-2">Convergence Trace Log</div>
                <table class="w-full text-left font-mono text-[9px] text-slate-400">
                    <thead class="text-slate-500 border-b border-slate-800">
                        <tr>
                            <th class="py-1">Iter</th>
                            <th class="py-1">Σ Φ</th>
                            <th class="py-1">Max Φ</th>
                            <th class="py-1">Max ΔΦ</th>
                            <th class="py-1">L2 ΔΦ</th>
                            <th class="py-1">Bots</th>
                            <th class="py-1">Coords</th>
                            <th class="py-1">RPI</th>
                        </tr>
                    </thead>
                    <tbody>
                        {#each rawExportData.telemetry_log as row}
                            <tr class="border-b border-slate-900/50 hover:bg-slate-900">
                                <td class="py-1 text-white">{row.iteration}</td>
                                <td class="py-1">{row.sum_phi.toExponential(2)}</td>
                                <td class="py-1">{row.max_phi.toExponential(2)}</td>
                                <td class="py-1 text-amber-400">{row.max_abs_delta_phi.toExponential(2)}</td>
                                <td class="py-1 text-indigo-400">{row.l2_norm_delta_phi.toExponential(2)}</td>
                                <td class="py-1">{row.number_of_detected_bottlenecks}</td>
                                <td class="py-1 text-emerald-400">{row.primary_bottleneck_coords}</td>
                                <td class="py-1 text-white">{row.RPI}</td>
                            </tr>
                        {/each}
                    </tbody>
                </table>
            </div>
            {/if}
            
            <button class="px-8 py-3 bg-slate-800 border-slate-700 text-slate-300 font-bold tracking-tight rounded-full hover:bg-slate-700 transition-colors disabled:opacity-50" on:click={() => loadDemo(activeScenario)}>
                Reset Topology
            </button>
        </div>
    </div>

    <!-- Right Panel: Data Science Metrics & Output Payload -->
    <div class="w-full lg:w-[400px] flex flex-col gap-6">
        <div class="bg-black/40 border border-slate-800 rounded-xl p-6">
            <h3 class="text-white font-bold text-lg mb-1">Spatial Pressure Contract</h3>
            <p class="text-slate-400 text-sm mb-6 pb-4 border-b border-slate-800">Mathematically identify topological bottlenecks on continuous resistance landscapes without local A* sampling.</p>
            
            {#if !inferenceMetrics}
                <div class="h-32 flex items-center justify-center border border-dashed border-slate-700 rounded-lg text-slate-500 font-mono text-sm">
                    [ Awaiting Execution ]
                </div>
            {:else}
                <div class="flex flex-col gap-4">
                    <div class="grid grid-cols-2 gap-4">
                        <div class="bg-slate-900 p-3 flex flex-col justify-center rounded-lg border border-slate-800 relative overflow-hidden">
                            <div class="text-[10px] uppercase text-emerald-500 font-bold mb-2">Engine Latency</div>
                            <div class="flex flex-col gap-1 text-xs font-mono text-slate-300">
                                <div class="flex justify-between"><span>Compute:</span> <span class="text-white">{inferenceMetrics.compute_ms}ms</span></div>
                                <div class="flex justify-between"><span>Serialize:</span> <span class="text-white">{inferenceMetrics.serialization_ms}ms</span></div>
                                <div class="flex justify-between border-t border-slate-800 mt-1 pt-1 font-bold"><span>Total:</span> <span class="text-emerald-400">{inferenceMetrics.total_inference_ms}ms</span></div>
                            </div>
                        </div>
                        <div class="bg-slate-900 p-3 rounded-lg border border-slate-800 flex flex-col justify-center items-center relative overflow-hidden">
                            <div class="text-[10px] uppercase text-sky-500 font-bold mb-1 w-full text-left">Max Structural Stress</div>
                            <div class="text-3xl mt-1 text-white font-mono flex items-end gap-1">
                                {inferenceMetrics.relative_pressure_index}
                                <span class="text-sm text-slate-500 font-sans mb-1">RPI</span>
                            </div>
                            <div class="text-[9px] text-slate-500 mt-1">(Relative Pressure Index)</div>
                        </div>
                    </div>

                    <h4 class="text-white font-bold mt-4 border-b border-slate-800 pb-2">High-Pressure Bottlenecks</h4>
                    <ul class="flex flex-col gap-2 max-h-48 overflow-y-auto pr-2">
                        {#each bottlenecks as b}
                            <li class="flex items-center justify-between p-3 bg-slate-900 border border-slate-800 rounded-lg group hover:border-slate-600 transition-colors cursor-pointer">
                                <div class="flex items-center gap-3">
                                    <div class="w-6 h-6 rounded flex items-center justify-center text-xs font-bold {b.rank === 1 ? 'bg-red-500/20 text-red-400 border border-red-500/50' : 'bg-amber-500/10 text-amber-500 border border-amber-500/20'}">{b.rank}</div>
                                    <div class="text-slate-300 font-mono text-sm">[{b.x}, {b.y}]</div>
                                </div>
                                <div class="flex flex-col items-end">
                                    <div class="text-slate-300 text-xs font-bold font-mono">Crit: {b.criticality_score}%</div>
                                </div>
                            </li>
                        {/each}
                    </ul>
                    
                    <button class="w-full py-2 bg-slate-800 text-slate-300 font-mono text-xs mt-4 rounded hover:text-white transition-colors border border-dashed border-slate-600 focus:outline-none" on:click={exportJson}>
                        Export RAW Audit JSON
                    </button>
                </div>
            {/if}
        </div>
    </div>
</div>
