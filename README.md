# Lineum™

> **"No Magic, Just Structure."**
> Emergence of stable localized excitations in discrete fields without physical constants.

Lineum is an open research project investigating whether particle-like structures ("linons") and field-mediated interactions can arise from simple, local update rules on a discrete grid, without embedding any physical laws or constants a priori.

## 📂 Project Structure

This public repository contains two distinct components:

| Component | Path | Description | Tech Stack |
| :--- | :--- | :--- | :--- |
| **Core** | `/` | The simulation engine and audit tools. | Python 3.11 |
| **Lab** | `/lab` | "Simulacrum" - Interactive 3D visualizer. | Svelte/Vite |

Commercial applications, the hosted Portal, and company-specific services live in the private `lineum-dynamics` repository. They consume released versions of Lineum Core; this public repository never depends on them.

---

## 🛠️ Prerequisites

To run and develop this repository, you need the following prerequisites installed on your system:
*   **Git** (for version control and project hooks)
*   **Python 3.11** with **pip** or **uv** (required for **Core** dependencies, manage via [requirements.txt](requirements.txt))
*   **Node.js (LTS version)** (required for **Lab**)

---

## 🔬 Core (Simulation Engine)
The heart of the project. A Python-based engine that runs the discrete field updates.

*   **Entry Point**: `lineum.py`
*   **Documentation**: `whitepapers/lineum-core.md` (Scientific paper)
*   **Usage**:
    ```bash
    # Install dependencies
    pip install -r requirements.txt

    # Run a simulation
    python lineum.py
    ```
*   **Audit**: See `whitepapers/` for full scientific methodology or [Verification Checklist](docs/verification_checklist.md) for independent reproduction.

### Reusable Python Library

`lineum-core` is also an application-neutral Python library for Lina EI and other independent Lineum applications. Its public package version has one source in `lineum_core/_version.py`; `setup.py`, built wheels, and runtime introspection all read that value.

Tagged releases build and attach a versioned `lineum_core-<version>-py3-none-any.whl`. Downstream applications pin an immutable release artifact or source commit and update deliberately. Lineum Core never depends on Lina-specific identity, cognition, embodiment, devices, or product policy.

For local development, install the active checkout explicitly:

```bash
python -m pip install --editable .
python -c "import lineum_core; print(lineum_core.__version__)"
```

See [Library Distribution Contract](docs/library-distribution.md) for the release and downstream update boundary.

### ⚡ Hardware Acceleration (CUDA/GPU)
Lineum Core uses the safe NumPy CPU backend by default and does **not** select a visible GPU implicitly. Select a backend explicitly through the cross-platform `LINEUM_DEVICE` environment variable:

- `LINEUM_DEVICE=numpy` — NumPy CPU, the default.
- `LINEUM_DEVICE=torch-cpu` — PyTorch on CPU.
- `LINEUM_DEVICE=cuda` — PyTorch on CUDA for exploratory runs only.

An explicit CUDA request is accepted only when PyTorch reports CUDA as available and the installed PyTorch build contains the detected GPU architecture. An incompatible request fails before a physics kernel is launched. Canonical audit runs always use CPU for cross-hardware determinism, even if CUDA was requested. The legacy `LINEUM_USE_PYTORCH=1` switch remains supported and maps to `torch-cpu`; it never enables CUDA implicitly.

See [Execution Device Policy](docs/execution-device-policy.md) for the runtime contract and verification commands.

### 📦 Reference Pack
For independent offline verification without reproducing the entire run, download the pre-built reference pack from the [Lineum Core GitHub Releases](https://github.com/TomasTriska88/lineum-core/releases) page (attached as an asset to `v*` tags).

To verify the downloaded pack:
```bash
python scripts/verify_reference_pack.py --pack <path_to_downloaded_zip>
```

---

## 🧪 Lab (Simulacrum)
An interactive 3D laboratory for visualizing field data and harmonics.

*   **Status**: Experimental / Visualizer.
*   **Tech**: Three.js + Svelte.
*   **Deployment**: Deployed to Railway as a static site.

---

## 🔬 Research & Audits
The `research/` directory contains exploratory materials, raw-data logs, and non-canonical working documentation.
*   **Purpose:** This is the project's internal scratchpad for testing hypotheses (e.g. `research/audits/`). 
*   **Disclaimer:** Documents located here are **not official product docs**, they make **no marketing claims**, their content is highly volatile, and they frequently document explicit *failed tests* used to map the engine's theoretical boundaries. Do not extrapolate these logs into official Lineum capabilities.

---

## 🚀 Release Workflow

### Git Protocol
*   **`dev` branch**: All development happens here.
*   **`main` branch**: Production releases only.

Tagged Core releases build the reusable Python wheel and the canonical reference pack. Commercial deployment is intentionally outside this public repository.

---

## 🛠 Troubleshooting
### Localhost vs 127.0.0.1 (Windows IPv6 Bug)
SvelteKit (Vite) development servers on Windows frequently bind to the IPv6 loopback (`::1`) while browsers attempt to resolve `localhost` via IPv4. This results in standard `npm run dev` endpoints returning a **404 error** or `ERR_CONNECTION_REFUSED`.
To bypass this, always run the dev servers bound explicitly to IPv4 via `--host` and navigate to the numeric IP:
```bash
# Lab
npx vite dev --host 127.0.0.1 --port 5174
```
**Do not use `localhost`** in the browser in these cases; use `http://127.0.0.1:5174` explicitly.

---

## 👥 Team & Acknowledgements
* **Tomáš Tříska**: Primary author, lead researcher, and creator of the Lineum Core engine.
* **Kateřina Marečková**: Contributor. Provided foundational critical opposition, hypothesis testing, and conceptual clarity for the ontological frameworks.
* **Vlastimil Smeták**: Contributor. Contributed key insights and correlations with the external OEA (Obecně Evoluční Algoritmus) model, influencing structural hypotheses.

---

## 📜 AGPLv3 + Commercial License

This entire repository, including the Core engine and Simulacrum, is open-source and natively governed by the **GNU AGPLv3 License**.
If you operate Lineum as a network service (SaaS) and modify the codebase, you must offer the source code of your running version to the users of your service. 

If you wish to operate Lineum in a closed-source ecosystem or cannot comply with the AGPLv3 requirements, a **Commercial License / Exception** is available from the copyright holder.

Contact for commercial licensing: TODO_CONTACT

### 🛡️ Trademarks
"Lineum™" and "Lina™" are trademarks of Tomáš Tříska.
Explicit permission is granted to contributors and users of the AGPLv3 Core Engine to use the "Lineum" and "Lina" names in connection with this project and its Lab interface, as long as such use is non-commercial (in accordance with the Codex) and accurately refers to this original repository.
