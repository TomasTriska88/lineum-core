<script>
    import { createEventDispatcher } from "svelte";
    import { t } from "../i18n";

    const dispatch = createEventDispatcher();

    export let trajData = [];
    export let frame = 0;

    // Visual Clarity Pass bindings
    export let debugView = false;
    export let showNodeIds = false;

    // UI observer threshold only; not a physics parameter.
    const ACTIVE_AMPLITUDE_THRESHOLD = 1000;

    // Configuration
    const CONTACT_THRESHOLD = 12.0;

    // Derived active nodes for the current frame
    let activeNodes = [];
    let candidateEdges = [];
    let components = [];
    let contactStats = [];

    // Reactive calculations when trajData or frame changes
    $: if (trajData && frame !== undefined) {
        calculateContactGraph();
    }

    function calculateContactGraph() {
        activeNodes = [];
        candidateEdges = [];
        components = [];
        contactStats = [];

        if (!trajData || trajData.length === 0) return;

        // 1. Identify active (born) nodes in the current frame
        trajData.forEach(traj => {
            const point = traj.path[frame];
            if (point && point[2] >= ACTIVE_AMPLITUDE_THRESHOLD) {
                activeNodes.push({
                    id: traj.id,
                    x: point[0],
                    y: point[1],
                    amp: point[2],
                    traj: traj
                });
            }
        });

        // 2. Identify candidate contact edges (Euclidean distance < 12.0)
        for (let i = 0; i < activeNodes.length; i++) {
            for (let j = i + 1; j < activeNodes.length; j++) {
                const n1 = activeNodes[i];
                const n2 = activeNodes[j];
                const dx = n1.x - n2.x;
                const dy = n1.y - n2.y;
                const dist = Math.sqrt(dx * dx + dy * dy);

                if (dist < CONTACT_THRESHOLD) {
                    // Compute contact duration dynamically around the current frame
                    const duration = calculateContactDuration(n1.traj, n2.traj, frame);

                    candidateEdges.push({
                        u: n1.id,
                        v: n2.id,
                        dist: dist,
                        duration: duration
                    });
                }
            }
        }

        // 3. Find connected components (DFS)
        const adj = {};
        activeNodes.forEach(node => adj[node.id] = []);
        candidateEdges.forEach(edge => {
            adj[edge.u].push(edge.v);
            adj[edge.v].push(edge.u);
        });

        const visited = new Set();
        activeNodes.forEach(node => {
            if (!visited.has(node.id)) {
                const comp = [];
                const stack = [node.id];
                while (stack.length > 0) {
                    const u = stack.pop();
                    if (!visited.has(u)) {
                        visited.add(u);
                        comp.push(u);
                        (adj[u] || []).forEach(v => {
                            if (!visited.has(v)) stack.push(v);
                        });
                    }
                }
                components.push(comp);
            }
        });
    }

    // Backtracks/looks ahead around the current frame to calculate contact duration
    function calculateContactDuration(t1, t2, currentFrame) {
        let duration = 0;
        const totalFrames = Math.min(t1.path.length, t2.path.length);

        // Find consecutive frames where distance < 12.0
        // We look backward from the current frame to find the start of contact
        let start = currentFrame;
        while (start >= 0) {
            const p1 = t1.path[start];
            const p2 = t2.path[start];
            if (!p1 || !p2 || p1[2] < ACTIVE_AMPLITUDE_THRESHOLD || p2[2] < ACTIVE_AMPLITUDE_THRESHOLD) break;
            const dist = Math.sqrt(Math.pow(p1[0] - p2[0], 2) + Math.pow(p1[1] - p2[1], 2));
            if (dist >= CONTACT_THRESHOLD) break;
            start--;
        }
        start++; // adjust back to first contact frame

        // We look forward from the current frame to find the end of contact
        let end = currentFrame;
        while (end < totalFrames) {
            const p1 = t1.path[end];
            const p2 = t2.path[end];
            if (!p1 || !p2 || p1[2] < ACTIVE_AMPLITUDE_THRESHOLD || p2[2] < ACTIVE_AMPLITUDE_THRESHOLD) break;
            const dist = Math.sqrt(Math.pow(p1[0] - p2[0], 2) + Math.pow(p1[1] - p2[1], 2));
            if (dist >= CONTACT_THRESHOLD) break;
            end++;
        }
        end--; // adjust back to last contact frame

        return (end - start + 1); // Return number of frames
    }

    // Helper to find contacts for a specific node
    function getNodeContacts(nodeId) {
        return candidateEdges.filter(e => e.u === nodeId || e.v === nodeId).map(e => {
            const partnerId = e.u === nodeId ? e.v : e.u;
            return {
                partnerId,
                dist: e.dist,
                duration: e.duration
            };
        });
    }
</script>

<div class="contact-graph-panel">
    <div class="panel-header">
        <h3>{$t('tab_contact_graph') || "Diagnostic ContactGraph"}</h3>
        <p class="desc">{$t('contact_graph_desc') || "Observer-only proximity analysis on the continuous spatial substrate."}</p>
    </div>

    <!-- Warning Box (Strictly Required) -->
    <div class="warning-box">
        <span class="warning-icon">⚠️</span>
        <div class="warning-text">
            <strong>{$t('contact_graph_warning_title') || "DIAGNOSTIC OBSERVER ONLY"}</strong>: 
            {$t('contact_graph_warning') || "Edges represent diagnostic proximity/contact candidate indicators (<12.0 px separation), NOT simulated physical bonds. Continuous boundary perturbations do not support a stable physical bond-state. No active forces are injected."}
        </div>
    </div>

    <!-- Metrics Scorecard -->
    <div class="scorecard-grid">
        <div class="scorecard-item">
            <span class="score-label">{$t('contact_graph_nodes') || "Active Nodes"}</span>
            <span class="score-value">{activeNodes.length}</span>
        </div>
        <div class="scorecard-item highlight">
            <span class="score-label">{$t('contact_graph_edges') || "Contact Edges"}</span>
            <span class="score-value">{candidateEdges.length}</span>
        </div>
        <div class="scorecard-item">
            <span class="score-label">{$t('contact_graph_components') || "Clusters / Components"}</span>
            <span class="score-value">{components.length}</span>
        </div>
    </div>

    <!-- Details Section -->
    <div class="details-section">
        <h4>{$t('contact_graph_diagnostic_mode') || "Observer Diagnostics"}</h4>
        <div class="diagnostic-meta">
            <span class="meta-label">{$t('contact_graph_threshold') || "Distance Threshold"}:</span>
            <span class="meta-value">{CONTACT_THRESHOLD.toFixed(1)} px</span>
        </div>

        <div class="diagnostic-controls" style="margin: 10px 0; padding: 10px; background: rgba(0, 255, 255, 0.05); border: 1px solid rgba(0, 255, 255, 0.1); border-radius: 4px; display: flex; flex-direction: column; gap: 8px;">
            <label class="control-label" style="display: flex; align-items: center; justify-content: space-between; font-size: 0.72rem; color: #cbd5e1; cursor: pointer; user-select: none;">
                <span>{$t('contact_graph_debug_view') || "ContactGraph debug view"}</span>
                <input 
                    type="checkbox" 
                    bind:checked={debugView} 
                    on:change={() => dispatch('toggleDebug', debugView)}
                    style="accent-color: #00ffff; cursor: pointer; width: 14px; height: 14px;"
                />
            </label>
            <label class="control-label" style="display: flex; align-items: center; justify-content: space-between; font-size: 0.72rem; color: #cbd5e1; cursor: pointer; user-select: none;">
                <span>{$t('contact_graph_show_node_ids') || "Show node IDs"}</span>
                <input 
                    type="checkbox" 
                    bind:checked={showNodeIds} 
                    on:change={() => dispatch('toggleNodeIds', showNodeIds)}
                    style="accent-color: #00ffff; cursor: pointer; width: 14px; height: 14px;"
                />
            </label>
            <button 
                type="button" 
                on:click={() => dispatch('focusContacts')}
                style="margin-top: 4px; background: rgba(0, 255, 255, 0.1); border: 1px solid rgba(0, 255, 255, 0.4); color: #00ffff; font-size: 0.65rem; padding: 6px 10px; border-radius: 4px; cursor: pointer; text-transform: uppercase; letter-spacing: 0.5px; transition: all 0.2s;"
            >
                {$t('contact_graph_focus_contacts') || "Focus active contact"}
            </button>
        </div>

        {#if activeNodes.length === 0}
            <div class="empty-state">
                {$t('contact_graph_no_active_nodes') || "No active nodes detected in the current frame."}
            </div>
        {:else}
            <div class="nodes-list">
                {#each activeNodes as node}
                    {@const contacts = getNodeContacts(node.id)}
                    <div class="node-item">
                        <div class="node-header">
                            <span class="node-id">Node #{node.id}</span>
                            <span class="node-coords">Pos: ({node.x.toFixed(2)}, {node.y.toFixed(2)})</span>
                        </div>
                        <div class="node-body">
                            <span class="node-amp">Amp: {node.amp.toExponential(2)}</span>
                            
                            <div class="node-contacts">
                                <span class="contacts-title">Contacts ({contacts.length}):</span>
                                {#if contacts.length === 0}
                                    <span class="no-contacts">None</span>
                                {:else}
                                    <div class="contacts-grid">
                                        {#each contacts as c}
                                            <div class="contact-sub-item">
                                                <span class="partner">Node #{c.partnerId}</span>
                                                <span class="distance">d = {c.dist.toFixed(2)} px</span>
                                                <span class="duration" class:flicker={c.duration <= 5}>
                                                    {c.duration} fr. ({c.duration <= 5 ? "Flicker" : "Persistent"})
                                                </span>
                                            </div>
                                        {/each}
                                    </div>
                                {/if}
                            </div>
                        </div>
                    </div>
                {/each}
            </div>
        {/if}
    </div>
</div>

<style>
    .contact-graph-panel {
        display: flex;
        flex-direction: column;
        gap: 14px;
        color: #fff;
    }

    .panel-header h3 {
        margin: 0;
        font-size: 0.9rem;
        color: #00ffff;
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    .desc {
        font-size: 0.7rem;
        color: #888;
        margin: 4px 0 0 0;
    }

    /* Warning Overlay */
    .warning-box {
        background: rgba(217, 119, 6, 0.1);
        border: 1px solid rgba(217, 119, 6, 0.4);
        border-radius: 6px;
        padding: 10px 12px;
        display: flex;
        gap: 10px;
        align-items: flex-start;
    }

    .warning-icon {
        font-size: 1.1rem;
    }

    .warning-text {
        font-size: 0.72rem;
        line-height: 1.4;
        color: #fbbf24;
    }

    /* Scorecard Grid */
    .scorecard-grid {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 8px;
    }

    .scorecard-item {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-left: 2px solid #555;
        border-radius: 4px;
        padding: 8px 10px;
        display: flex;
        flex-direction: column;
        gap: 4px;
    }

    .scorecard-item.highlight {
        border-left-color: #00ffff;
        background: rgba(0, 255, 255, 0.03);
        border-right: 1px solid rgba(0, 255, 255, 0.1);
        border-top: 1px solid rgba(0, 255, 255, 0.1);
        border-bottom: 1px solid rgba(0, 255, 255, 0.1);
    }

    .score-label {
        font-size: 0.58rem;
        color: #888;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .score-value {
        font-size: 1.2rem;
        font-family: monospace;
        font-weight: bold;
    }

    /* Details Section */
    .details-section {
        display: flex;
        flex-direction: column;
        gap: 8px;
    }

    .details-section h4 {
        margin: 0;
        font-size: 0.8rem;
        color: #cbd5e1;
        text-transform: uppercase;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        padding-bottom: 4px;
    }

    .diagnostic-meta {
        font-size: 0.72rem;
        display: flex;
        justify-content: space-between;
        color: #94a3b8;
    }

    .meta-value {
        font-family: monospace;
        color: #00ffff;
    }

    .empty-state {
        font-size: 0.7rem;
        color: #64748b;
        text-align: center;
        padding: 20px;
        background: rgba(0,0,0,0.2);
        border-radius: 4px;
    }

    /* Node List */
    .nodes-list {
        display: flex;
        flex-direction: column;
        gap: 8px;
        max-height: 280px;
        overflow-y: auto;
        padding-right: 4px;
    }

    .node-item {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 4px;
        padding: 8px;
        font-size: 0.72rem;
        display: flex;
        flex-direction: column;
        gap: 6px;
    }

    .node-header {
        display: flex;
        justify-content: space-between;
        font-weight: bold;
        color: #38bdf8;
    }

    .node-coords {
        font-family: monospace;
        color: #94a3b8;
        font-weight: normal;
    }

    .node-body {
        display: flex;
        flex-direction: column;
        gap: 4px;
    }

    .node-amp {
        font-family: monospace;
        color: #a1a1aa;
        font-size: 0.65rem;
    }

    .node-contacts {
        margin-top: 4px;
        border-top: 1px dashed rgba(255, 255, 255, 0.05);
        padding-top: 4px;
    }

    .contacts-title {
        color: #888;
        font-size: 0.65rem;
    }

    .no-contacts {
        color: #52525b;
        font-style: italic;
        margin-left: 4px;
    }

    .contacts-grid {
        display: flex;
        flex-direction: column;
        gap: 4px;
        margin-top: 2px;
    }

    .contact-sub-item {
        display: flex;
        justify-content: space-between;
        background: rgba(0, 0, 0, 0.15);
        padding: 4px 6px;
        border-radius: 2px;
        font-size: 0.68rem;
    }

    .partner {
        color: #fbbf24;
    }

    .distance {
        font-family: monospace;
        color: #00ffff;
    }

    .duration {
        font-family: monospace;
        color: #34d399;
    }

    .duration.flicker {
        color: #f87171;
    }
</style>
