# Prime-fraction geometry, wave descriptions, and Riemann-zero spacings in Lineum

**Status:** active (preregistered, not validated)  
**Version:** 0.1.0  
**Evidence cutoff:** 2026-11-22  
**Programme membership:** standalone; no inherited root programme is asserted  
**Repository / branch at registration:** `TomasTriska88/lineum-core` / `develop`  
**Prior HEAD:** `c03b9746f8b5867c35265ee79810433706eab3c7`  
**Confidence:** high in the elementary mathematical identities, low/unknown in any connection to Riemann-zero gaps or emergent Lineum outputs  
**Root scientific question:** Can a genuinely scale-consistent, independently predictive relationship connect prime-derived fractional geometric layers, spacing of nontrivial zeta zeros, and *uninjected* emergent spectral modes from the Lineum engine?

## Owner's original intuition (not a scientific finding)

The project owner proposes that fractions or decompositions associated with each prime may have a geometric length/structure that could "fit" within gaps between successive Riemann zeros, and that frequency, interference, and phase might explain why. The owner points to the 2D prime-grid intersections in Vlastimil Smeták's public presentation. **The owner's intent is not limited to base-10 repeating decimals**; earlier conversations about fractional expansions should not replace the actual prime-grid motivation. The objective is to learn about Lineum, not to establish priority for the presentation's author or to recreate an unrelated prime detector.

## Third-party research intake and boundaries

- **Public source actually discussed:** Vlastimil Smeták (lead author), Jiří Chlebníček and Boris Koštel (co-authors as credited on title slide), *Detekce prvočísel pomocí π*, video: https://www.youtube.com/watch?v=7ardq_YdtVQ; user-supplied screenshots of 80 video frames, inspected in discussion on 2026-11-22. This is **not** a complete video transcript or a review of unpublished material.
- **Rights holder / license:** slide copyright and redistribution license not established. Publicly discuss high-level mathematical facts, independent derivations, and source attribution; **do not copy or republish screenshots, slides, distinctive figures or equations as expressed in the presentation into public Core** until rights permit it. This report contains independently expressed mathematics rather than presentation text.
- **Prior provisional Git history (NOT on develop):** `research/smetak-pi-review-20261122`, with a source-description Markdown document, separate toy arithmetic/Fourier code and an 80-frame hash list. These prior commits are not evidence that the images themselves were saved in Git, nor that those calculations were independently rerun in this checkpoint. Keep that branch as provenance; do not silently promote its claims or copy restricted images.
- **External mathematics:** the Euler product for ζ(s) at Re(s)>1, 2D visibility/coprimality of integer lattice points (density 1/ζ(2)=6/π²), and the Riemann explicit formula relating zero ordinates and prime powers are established mathematical background, not Lineum discoveries. Accessible references: B. Green, *The Prime Numbers* (Oxford lecture notes), https://people.maths.ox.ac.uk/greenbj/papers/primenumbers.pdf ; J. C. Baez, *Riemann's explicit formula, one zero at a time*, https://math.ucr.edu/home/baez/mathematical/riemann_explicit_formula/riemann_explicit_formula.html .
- **Scope:** independent analytic arithmetic, toy grids, basic nulls and measurement-design preregistration only. No copying third-party implementation, no broad Lineum run, no Canonical Core change, no whitepaper promotion, no claim about real physical waves.

## Historical Lineum evidence and negative gates

The current `develop` whitepaper `whitepapers/3-ontology/hypotheses/03-ontology-hyp-zeta-resonance.md` (status on 2026-11-22: **CLOSED_NEGATIVE / AUDIT_FAILED_INTEGRABILITY_BLOCK**) records that early RNB/zeta positional alignment, including correlation 0.9842, was not established after controls. Its RZ-0 separable Hamiltonian produced integrable/Poisson behavior; tested RZ-1 nonseparable variants lost apparent GUE structure and failed random-weight controls at larger sizes. The tested Eq-12 coupling remains blocked. Related `whitepapers/2-cosmology/hypotheses/06-cosmo-hyp-law-transition.md` marks previous zeta/GUE overlays as look-elsewhere density artifacts. These failures remain binding **for those tested constructions**, not for every possible prime-related observable.

Core v1 is a 2D periodic numerical model with explicit equations and audited boundaries; the main whitepaper expressly excludes quantitative Riemann-zero correlations. The proposed fraction–gap bridge must not be manufactured by injecting primes, zero ordinates, spectral target frequencies, or trained matching into the Lineum state.

## Registered distinct candidate mechanisms (before any scoring)

- **G0 — direct fraction-to-gap tiling [untested]:** use the new uncovered area contribution of each successive prime `p`, `ΔA(p)=A_previous/p²` with `A_previous=∏_{q<p, q prime}(1−1/q²)`, as an intrinsic geometric quantity. Ask whether an *a priori* mapping to consecutive zero gaps exists. A mismatch of dimensions, indexing or arbitrary scale is a **non-identifiability** result, not a refutation of all connections.
- **G1 — repeat lengths of reciprocals [untested]:** if a base-`b` expansion `1/p` is used, measure its cycle period `ord_p(b)` when `gcd(p,b)=1`. Change base as a negative control; base-specific digit cycles alone cannot imply an intrinsic scale-free property of zeros.
- **G2 — Fourier geometry of divisibility grids [known identity; no scored Lineum test]:** a grid that selects coordinates divisible by `p` has a spatial Fourier mode lattice with fundamental period `p`, i.e. characteristic wavenumbers `2πk/p`. A Fourier representation is **not a traveling physical wave**, an emergence proof or a zeta zero.
- **G3 — arithmetic prime frequencies [established mathematical bridge; untested in Lineum]:** zeta's explicit formula uses contributions from prime powers with logarithmic `log p` phase structure. **`log(p)` and `1/p` are different frequency laws.** Determine what additional transform or operator (if any) could relate them; never quietly replace one with the other.
- **G4 — actual Lineum-native spectrum [deferred, closed historical formulations respected]:** select a spectral observable solely from the current engine, lock observer, normalization and seed before zeta comparison, then compare with shuffled/noise and appropriate Poisson/GOE/GUE nulls. This is **not** authorized merely by finding a toy correspondence.
- **G5 — conventional null and generic periodic masks [required controls]:** scrambled spacing, evenly spaced lattices, composite moduli and randomized prime-label assignments; they may reproduce visual regularity with no arithmetic signal.

## Frozen first-step protocol (analytic sanity check; no fit)

**Question:** Are the numerical objects proposed for "a fraction fitting in a zero gap" intrinsically comparable before any Lineum run?

1. Prime set, fixed before analysis: `P=(2,3,5,7,11)`. Compare exact finite grid densities `A_k=∏_{i≤k}(1−1/p_i²)` and uncovered increments `ΔA_k=A_{k−1}−A_k`. Calculate independently using (a) integer enumeration over a full period `L=2·3·5·7·11=2310` *per spatial axis if computationally practical* or a smaller valid subset with declared scope; and (b) algebraic inclusion–exclusion. A full 2310² Boolean grid is optional, not necessary for first-step reasoning.
2. Compare dimensionless prime-stage quantities with **no fitted free scale**; do not assign a prime index `k` to a zeta gap index `n` unless a causal, prespecified mapping is given. The existence of mathematical points in both sequences is not such a mapping.
3. For reciprocal periods use bases `b=2,10,12`; omit `p` when not coprime with a chosen base. If the digit period changes under a base change while prime geometry and zeta zeros stay fixed, classify **that decimal-period version** as coordinate dependent, without overgeneralization to grid fractions.
4. For log-prime versus reciprocal geometry, compare the first five normalized candidate frequencies `1/p` and `log(p)`; log and reciprocal trends are opposite. Record exact sample values but do not label this a test of Riemann alignment.
5. Real zeros: optional reference ordinates are `γ_1≈14.134725`, `γ_2≈21.022040`, `γ_3≈25.010858`; the first two gaps are about 6.8873 and 3.9888. Comparing them numerically to arbitrary fractions without a unit/scale and indexed matching rule cannot yield a valid scientific test.
6. **Pass for this checkpoint:** exact agreement of area algebra with independent integer counting, complete dimensional/scale/observer inventory and an explicit next noncircular test. **Fail:** mathematical inconsistency, ambiguous coordinate convention, or a reported "match" that requires retrospectively tuned scaling. **Not tested:** Lineum's wave dynamics or a zero-spacing mechanism.

**Minimal exact recipe, standard Python (no Lineum dependency):**

```python
from fractions import Fraction
from math import gcd, log

primes = (2, 3, 5, 7, 11)
remaining = Fraction(1)
for p in primes:
    removed = remaining / (p * p)
    remaining -= removed
    print(p, removed, remaining, 1 / p, log(p))
# For a p×p prime grid on integer coordinates 1..p, exactly
# one of p² sites has both coordinates divisible by p.
for p in (2, 3, 5, 7, 11):
    brute = sum(x % p == 0 and y % p == 0
                for x in range(1, p + 1)
                for y in range(1, p + 1))
    assert brute == 1
```

## Three-layer physical claim boundary

1. **Code:** no new Lineum observation is produced by this preregistration; known whitepaper audit exclusions and negative spectral history remain unchanged.
2. **Known mathematics / reality:** exactly defined prime factorizations, Euler products and Riemann zero ordinates are abstract numerical structures. A spatial Fourier decomposition is a descriptive identity, not a real-world electromagnetic or fluid mechanism.
3. **Open Lineum hypothesis:** emergent, non-injected field modes may have nontrivial relation to arithmetic spectra, but this remains **unresolved** without a dimensionally meaningful, independent observable and controls.

## Reopenable coverage, forbidden inference, and next checkpoint

All G0–G5 variants remain registered; G0/G1 are owner-motivated possible interpretations, G2/G3 are known mathematical baselines, G4 is a deferred empirical-scoring lane, G5 is the negative-control family. Historical RZ-0/RZ-1 negatives cannot be silently overwritten or "repaired" by changing the metric after seeing a desirable overlap.

This checkpoint does **not** claim a discovery, a prime decomposition law for Riemann gaps, a formal proof, a physical wave, or a corrected Lineum result.

**Next permitted step after verifying this report in Git:** run the frozen first-step numerical sanity checks, independently verify key counts by direct enumeration, append the exact results/limitations to THIS same report and commit them before considering any further experiment. If the check produces a material negative, preserve it and trigger the required owner-intuition gate before selecting a replacement mechanism. Canonical whitepapers stay unchanged unless a separately validated Lineum result passes their promotion gate.

**ClickUp:** one narrow search in workspace `90121717552` retrieved task `869ek96jb`, but its explicit prerequisite restricts a distinct future rank–trace Lineum-native audit. No task or status changes were made; this arithmetic preflight is not authorization to bypass that prerequisite. ClickUp mode = unsynchronized for this standalone programme.
