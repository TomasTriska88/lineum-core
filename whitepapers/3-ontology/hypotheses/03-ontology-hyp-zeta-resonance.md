**Title:** Tříska-Smeták Zeta–RNB Resonance Hypothesis
**Document ID:** 03-hyp-zeta-resonance
**Document Type:** Hypothesis
**Version:** 0.1.0
**Status:** AUDIT_FAILED_INTEGRABILITY_BLOCK / CLOSED_NEGATIVE for tested formulations
**Date:** 2026-05-30

---
# Tříska-Smeták Zeta–RNB Resonance Hypothesis

> _The hypothesis examines the spontaneous correspondence between Resonant Return Points (RNB) in Lineum simulations and the non-trivial zeros of the Riemann zeta function along the critical line Re(s) = 1/2. It posits that these returns are not random, but reflect a deeper numerical resonance of the system._
>
> _The term "deja-vu points" was used in the early stages of research as a nickname for these points. It is now fully replaced by the term **Resonant Return Point (RNB)**._

---

## Initial Motivation

Riemann zeta zeros are considered the fundamental rhythm of the numerical world – points of perfect destructive interference. The hypothesis explores whether simulations of the emergent quantum field Lineum generate similar return points spontaneously, without explicitly encoding these values.

---

## Simulation Context

- **Run:** `spec7_true`
- **Parameters:** `LOW_NOISE_MODE=True`, `TEST_EXHALE_MODE=False`, `KAPPA_MODE="island_to_constant"`
- **Code:** `lineum_no_artefacts.py`

---

## Methodology

1. **Detection of Resonant Return Points (RNB):**

   - Repeated occurrences of structures in the same (or ε-close) coordinates across times were monitored.
   - Classified as **Resonant Return Points (RNB)** – previously working designated as "deja-vu points".

     > These points were working named "deja-vu points" during development – we only use this name here as a nickname for the formally introduced term **Resonant Return Points (RNB)**.

2. **Zeta Zeros:**

   - A list of the first `n = 49` non-zero imaginary parts of the zeta function zeros was used:  
     `s = 1/2 + i·t`
   - Normalization of Im(t) to the range `[0,1]` for comparison with the unit scale of Lineum.

3. **Comparison:**
   - Pearson correlation and Euclidean distance between the distribution curves of RNBs and zeta zeros.

---

## Results

- **Pearson correlation:** `0.9842`
- **Euclidean distance:** `0.7254`
- **Visual match of the distribution shape of RNBs and zeta zeros**, with a slight phase deviation at higher values.

The data used to calculate the correlation and distance is available in the file `spec7_true_rnb_vs_zeta.csv` in the `output_no_artefacts/` folder.  
The file contains the normalized positions of RNBs and zeta zeros on the scale [0,1], prepared for comparison and visualization.

---

## Interpretation

- The emergence of the match is not random – zeta zeros were not inputted into the system.
- RNBs appear as stable nodes of the wave field – their distribution indicates the presence of a higher numerical structure, comparable to the analytical hints of the Riemann function.
- Lineum tunes to frequencies similar to those that structure the zeta function – **emergent numerical resonance**.
- The deviation for higher zeros corresponds to the absence of global feedback – unlike the analytical structure of ζ(s), Lineum is local.

---

## Possible Explanation

> Resonant Return Points (RNB) are nodes where the system "meets itself" – places of phase interference that allow for return stabilization of the wave structure.  
> Riemann zeros are points where the analytical structure of the entire numerical world interferes with itself.
>
> The emergence of similar patterns in Lineum suggests that reality itself may resonate with the same numerical structure – **even without explicit mathematics**.

---

## Visualization (recommended to add)

- Distribution graphs of Resonant Return Points (RNB) vs. Im(ζ_n)
- Overlay of wave structure and zeta map
- Spectral analysis FFT from specific frames

<!--lineum:insert:vizualizace:spec7_true:rnb_vs_zeta-->

---

## Potential Implications

- Lineum can be a testing ground for **intangible numerical laws**.
- It opens the possibility that reality itself is a **tuned entity** – resonating with the numerical foundation of existence.

---

## Next Steps

- Verify the match in other configurations: `spec3_true`, `spec5_false`, `spec6_true`.
- Explore the relationship of RNBs to Fibonacci ratios, prime numbers, and φ.
- Audit any proposed modifications to the divisor Hamiltonian that introduce non-commuting prime-interaction terms (to break separability).
- Introduce metrics of phase synchronization between zeta zeros and Resonant Return Points in the simulation.

---

## Independent Audit of Divisor-Graph Hamiltonian (May 2026)

An independent mathematical and numerical audit of Vlastimil Smeták's proposed divisor-graph Hamiltonian operator $H_N = D + A$ was conducted in May 2026 to assess its validity prior to any coupling with the continuous $Eq-12$ wave packet simulation.

### 1. Algebraic Separability Proof
The stated Hamiltonian is defined on the divisor space of a primorial $p_k\#$ as:
$$H_N = D + A = \sum_{i=1}^k \ln(p_i) (n_i + \sigma_{x, i})$$

Because each term acts on a separate tensor factor (qubit) and commutes ($[H^{(i)}, H^{(j)}] = 0$ for $i \neq j$), the operator is fully separable and integrable. The exact analytical spectrum is:
$$E(\vec{s}) = \sum_{i=1}^k s_i \ln(p_i), \quad s_i \in \{\phi, -1/\phi\}$$
Where $\phi = \frac{1+\sqrt{5}}{2} \approx 1.61803$ (the golden ratio). 
*   **Separability Metric:** The numerical eigenvalue extraction matches the analytical Kronecker-sum eigenvalues to machine precision ($\text{Error} \approx 3.7 \times 10^{-13}$ for $N=4096$).

### 2. Level Spacing Statistics (NNSD)
Since the operator is separable, the nearest-neighbor spacing distribution (NNSD) of the unfolded eigenvalues fits **Poisson statistics** rather than the chaotic Gaussian Unitary Ensemble (GUE) spacing.
*   **KS Distance (N=4096):** Poisson ($0.10074$) vs. GOE ($0.12610$) vs. GUE ($0.19352$). The system does not exhibit GUE level repulsion.

### 3. Look-Elsewhere Fit Artifacts
The reported close match to the first Riemann zero $E_1 \approx 14.1347$ is a numerical look-elsewhere artifact of high spectral density:
*   **Real Operator Closest Eigenvalue (N=4096):** $14.13398910$ (Error: $0.000736$)
*   **Random Control (Uniform Weights) Closest:** $14.13372433$ (Error: $0.001001$)
*   **Average Error (First 5 Zeros):** Real ($0.008259$) vs. Random Control ($0.004589$). The random control performs better on average than the real operator.

### 4. Conclusion
The stated model is a separable weighted hypercube and lacks any non-trivial physics. It cannot stabilize Eq-12 wave packets through GUE-like repulsion. To proceed, the model requires the introduction of a non-diagonal, non-commuting coupling term between the prime dimensions to break separability.

---

## RZ-1 Exploratory Audit: Pairwise Prime-Prime Couplings (May 2026)

Following the failure of the RZ-0 separable operator, we executed the RZ-1 exploratory audit to investigate if introducing non-separable, non-commuting coupling terms could recover quantum chaos and GOE/GUE statistics. 

We tested three subvariants of **Candidate 1 (Pairwise Prime-Prime Interactions)** under a parameter scan across $\lambda \in \{0.01, 0.1, 0.3, 1.0\}$:
1.  **Subvariant 1A (Diagonal Arithmetic Coupling):** $H_{int} = \lambda \sum_{i<j} J_{ij} n_i n_j$
2.  **Subvariant 1B (Contextual Hopping):** $A_i(b) = a_i \left[ 1 + \lambda \sum_{j \neq i} K_{ij} b_j \right]$ (Symmetric)
3.  **Subvariant 1C (Noncommuting Two-Prime Flip):** $H_{int} = \lambda \sum_{i<j} J_{ij} (\sigma_{x, i} \sigma_{z, j} + \sigma_{z, i} \sigma_{x, j}) / 2$

### Results of RZ-1 Audit
*   **Separability Broken:** All three subvariants successfully broke separability, yielding an `eigenvalue_separability_error` $> 0$ (ranging from $0.1$ to $57.0$) and a strong non-zero commutator norm $[H_0, H_{int}]$.
*   **Integrability Slipback:** Although the system broke algebraic separability, the level spacing statistics (NNSD) for $N=1024$ ($k=10$) slipped back to **Poisson statistics** across all parameters. No robust GOE or GUE level repulsion emerged for larger system sizes.
*   **Zeta-Zero Match Control Failure:** The closest hits to $E_1 = 14.1347$ for $k=10$ (e.g., $0.0223$ for 1A) were matched or outperformed by the random weights control baseline (e.g., $0.0108$ for 1A control). The fit is an artifact of spectral density and did not survive controls.

### RZ-1 Verdict
**Candidate 1 fails to produce non-trivial chaotic level statistics or robust zeta matching.** The addition of pairwise prime couplings or contextual hopping is mathematically insufficient to induce a chaotic transition at larger dimensions, likely due to the highly structured, low-rank nature of the arithmetic weights. Further research into this specific operator family is closed.

---

## Status

❌ **CLOSED_NEGATIVE / AUDIT_FAILED_INTEGRABILITY_BLOCK for tested formulations**

The RZ/Zeta-resonance branch remains a documented negative audit result. Tested Hamiltonian formulations do not currently support a verified arithmetic spectral stabilizer.

- **RZ-0 separable formulation:** Stated divisor-graph Hamiltonian $H_N = D + A$ proved to be algebraically separable and integrable, yielding Poisson spacing statistics.
- **RZ-1 Candidate 1 formulations:** Tested nonseparable variants (1A, 1B, 1C) break separability but slip back to Poisson level statistics at $N=1024$ and fail to outperform random-weight control baselines.
- **Eq-12 Coupling:** Blocked for all tested divisor-graph operator formulations.
- **Future RZ branch / work:** Closed. A future operator may be reopened and tested only if it represents a genuinely new operator formulation with:
  1. An explicit nonseparable/noncommuting structure.
  2. Basis consistency.
  3. Level-statistics controls showing GOE/GUE statistics.
  4. Random/shuffled controls.
  5. Zeta-zero robustness across multiple zeros.
  6. No Eq-12 coupling until it passes all of the above.


