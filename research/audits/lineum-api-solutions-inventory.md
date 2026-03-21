# Lineum API Solutions & Applications Inventory

This document serves as a central inventory of all pre-prepared applications, PoCs, demos, and concepts derived from Lineum mechanisms that are (or were) part of considerations for API products in the `Portal`.

## 1. Completed and Verified Demos (Portal API Solutions)

### Diffusion Showcase (Routing, Traffic, Evacuation)
- **What it solves:** Finding optimal paths, modeling evacuation, crowd and traffic simulation (urban planning).
- **Status:** Fully functional demo on the portal.
- **Traces in the repo:** `portal/src/routes/(app)/api-solutions/+page.svelte`, `portal/src/lib/components/showcase/DiffusionShowcase.svelte`, `lineum_core` (A* vs Lineum benchmarking).
- **Lineum core mechanism used:** Utilizes `phi` (memory) and `psi` (wave) for diffusion-based pathfinding of least resistance across obstacles (`kappa`).
- **Actually completed:** Visual Svelte components, escape exit/swamp scenarios, verification of NMS and thresholding parameters (Flow Vulnerability) in analytical tests.
- **Remaining:** Connection to a scalable cloud backend with the Lineum Edge SDK (delta streaming) for extensive production customer maps.

### Fast TRNG API (Vacuum Noise)
- **What it solves:** Fast entropy generation for everyday cryptography and session keys.
- **Status:** PoC specified.
- **Traces in the repo:** Mentions in `todo.md`, historical TRNG/API sections in frontend Svelte components (`FastTrngApp`).
- **Lineum core mechanism used:** Reading microscopic phase fluctuations from the "vacuum" (baseline `psi` noise without settled topologies).
- **Actually completed:** Concept and visual integration into a Svelte demo.
- **Remaining:** Robust NIST statistical tests, operationalizing a secure streaming path (Hex strings via API).

### Extreme Zeta Entropy API (Quantum Chaos)
- **What it solves:** Generating cryptographic noise ("unbreakable entropy") for post-quantum security and extreme use-cases (military, banking).
- **Status:** Experimental idea (zeta models audit in progress).
- **Traces in the repo:** `ZetaEntropyApp` in the portal, mentions in `todo.md`.
- **Lineum core mechanism used:** Extracting patterns generated from collisions of massive `phi` structures (topological defects, collapse into "zeta" points, GUE distribution).
- **Actually completed:** Discovery of zeta-nodes as mathematically unique anomalies of the engine.
- **Remaining:** Mechanism for parallel densification and irreversible "hashing" of these topological patterns before distribution to clients.

### Web3 Oracle API (ZK-Proof Trusted Seed)
- **What it solves:** Delivering transparent and auditable randomness for smart contracts (e.g., Ethereum VRF replacement).
- **Status:** Mentioned concept, PoC does not exist.
- **Traces in the repo:** `Web3VrfApp` in the frontend, architectural plan in `todo.md`.
- **Lineum core mechanism used:** Providing field topology with a deterministic baseline for easier zero-knowledge proof ("this hash was created by a fifty-step perturbation").
- **Actually completed:** Empty visual portal modules.
- **Remaining:** Conceptual shift from the words "Zeta-structure" to an actual zk-SNARK / zk-STARK provability specification over Lineum physics.

### LineumHash API (Topological One-Way Function)
- **What it solves:** Data (password) encryption. Input is a string, output is a topological seal from the physical Lineum matrix. Resistant to encryption acceleration (Quantum Shor's Algorithm).
- **Status:** Formal proposal of properties, not implemented.
- **Traces in the repo:** Mentions in `LineumHashApp` and `todo.md`.
- **Lineum core mechanism used:** Wave collapse as a one-way function. It can be simulated step-by-step forward, but not algorithmically accelerated backward.
- **Actually completed:** Lineum engine core generating the wrinkling of fields.
- **Remaining:** Clear transformation of 1D byte input into semantic 2D perturbation at the start of hashing. Collision analysis.

### Gaming Provably-Fair RNG API
- **What it solves:** Generating guaranteed certified game values for online casinos (e.g., roulette 1-37). The customer downloads the generation protocol from the server.
- **Status:** Concept in UI.
- **Traces in the repo:** `GamingRngApp`.
- **Lineum core mechanism used:** Same source as Fast TRNG, but with a provable visualization footprint of "exactly how the selection occurred".
- **Actually completed:** UI tab in the frontend.
- **Remaining:** Architecture of the certification payload in JSON.

## 2. Proposed Domain B2B Applications (For Future Exploration)

1. **Topographic City-Connection Routing:** Robust calculation of nationwide logistics across large 4K+ elevations (`kappa`), bypassing mountain ranges and naturally respecting load like a river network (article on advantages over traditional A* graph).
2. **Generative Antenna Design (Fractal):** Finding antenna topology in 2D `kappa` plates for broadband communication, inspired by biological Lineum branching (137.5° splitting angles).
3. **Medical Vascular By-passes / Microchip Routing:** The same "least resistance" routing, applied microscopically to printed circuits to eliminate antenna interference from classic 90° bends, or to bypass cardiac blockages based on CT scans.
4. **Crisis Management (Panic Effect / Traffic Jam):** Deliberate use of memory pressure `phi` and terrain hardening parameters to model panic in stadiums and massive crowd evacuations with realistic corridor damage.

## 3. Maturity Summary
By far the most mature and mathematically tested application direction of the project is **Flow Vulnerability / Topological Routing** (Diffusion Showcase). It is empirically documented, has precise parameters, and wins benchmarks for complex terrains. The encryption and cryptography directions represent an architecturally prepared, but not yet production-certified (Phase 2), B2B path.
