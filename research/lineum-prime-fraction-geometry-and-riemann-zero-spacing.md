# Prime-fraction geometry, wave descriptions, and Riemann-zero spacings in Lineum

**Status:** active (preregistered, not validated)  
**Version:** 0.1.1  
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

## Executed checkpoint 1: finite-prime layers, coordinate dependence, and an independent integer control (2026-11-22)

**Report version:** 0.1.1  
**Execution environment:** isolated Python 3.13.5, Python standard library only; no repository checkout, no Lineum runtime, no source video processing during this run.  
**Frozen input:** P = (2, 3, 5, 7, 11), residue square 1..2310 in each coordinate, reciprocal digit bases 2, 10 and 12.  
**Execution command:** `python /mnt/data/.scratch/lineum-prime-fraction/sanity.py` in the disposable runtime. Script SHA-256 was `da1879a57f475b361439842fee853eca02d661d1fdb9295cb242acc87b10e36e`. The exact standalone reimplementation follows below; ephemeral paths are **not** required to repeat the result.

### Exact arithmetic results

Each prime layer `p` removes precisely those 2D points at which **both** coordinates are divisible by `p`. At a complete period, its independent area fraction is `1/p²`. Inclusion/exclusion gives the following *incremental fractions*; these are exact rational numbers, **not** a decimal expansion of `1/p`:

| Newly added prime | Fraction of whole plane newly covered | Fraction still uncovered |
| ---: | ---: | ---: |
| 2 | 1/4 | 3/4 |
| 3 | 1/12 | 2/3 |
| 5 | 2/75 | 16/25 |
| 7 | 16/1225 | 768/1225 |
| 11 | 768/148225 | 18432/29645 |

The combined grid repeats after 2310 integer steps on each axis. Of its `2310² = 5,336,100` points, precisely **3,317,760** remain uncovered.

**Independent check:** direct integer enumeration over every pair of 2310² lattice coordinates produced 3,317,760, independently matching the Chinese-remainder/counting identity `∏(p²−1)=3,317,760`. These checks agree *exactly*, without a graph, fitting or numerical tolerance.

The same checkpoint recomputed the visible presentation's finite-grid counts by a separate Euler-totient sieve:

- `N=5000`: **15,200,915** coprime ordered-coordinate pairs, exactly the slide count.
- `N=20,000`: **243,180,791** pairs, whereas the supplied slide shows **243,180,790**; the unexplained difference of **one** can arise from pixel coordinate/boundary convention and is not proof of an error in the author's construction. It is a reconciliation item, not new mathematics.

The density `18432/29645≈0.62175746` for only the first five prime layers is expected to exceed the all-prime limit `6/π²≈0.60792710`. The observed sequence is the classical finite Euler product, not evidence of a new Riemann-zero-spacing law.

### Reciprocal digit-period coordinate control

For `1/7`, the repeating period is **3** digits in base 2 and **6** digits in base 10; for `1/11`, it is **2** digits in base 10 but **1** digit in base 12. These are calculated multiplicative orders `ord_p(b)`. Therefore **a specific decimal (or other fixed-base) digit-cycle length is not a base-invariant physical or zeta-gap length**. This is a bounded negative for *G1 if interpreted as a base-independent digit-period identity*. It does **not** falsify the owner's geometric fractional-layer intuition G0.

### Different meanings of frequency (important anti-conflation)

For the first primes `2,3,5,7,11`, spatial divisor-grid scales `1/p` are `0.5,0.333333,0.2,0.142857,0.090909`, whereas the prime frequencies used in zeta explicit-formula phases `log p` are `0.693147,1.098612,1.609438,1.945910,2.397895`. The former decrease as p grows while the latter increase. **No single positive scale factor maps these two ordered sequences term by term.** A nonlinear transform or newly defined operator must be stated explicitly before suggesting they represent the same physical rhythm.

For reference, the first two nontrivial-zeta-zero gaps from standard published ordinates are `γ₂−γ₁≈6.8873144970` and `γ₃−γ₂≈3.9888179414`. The present test **did not** pair prime fraction `k` with zeta gap `k` or optimize a fit. There is not yet a defensible shared unit, indexing rule, prediction or null distribution that would make such a "fraction fits the gap" claim falsifiable.

### Standalone verification code (standard Python)

```python
from fractions import Fraction
from math import gcd, log, pi, prod

P = (2, 3, 5, 7, 11)
remaining = Fraction(1)
for p in P:
    new_coverage = remaining / (p * p)
    remaining -= new_coverage
    print(p, new_coverage, remaining)

L = prod(P)
direct = 0
for x in range(1, L + 1):
    factors = [p for p in P if x % p == 0]
    direct += sum(
        all(y % p != 0 for p in factors)
        for y in range(1, L + 1)
    )
crt = prod(p * p - 1 for p in P)
assert direct == crt == 3_317_760
assert remaining * L * L == crt

def period(p, b):
    if gcd(p, b) != 1:
        return None
    v = b % p
    n = 1
    while v != 1:
        v = v * b % p
        n += 1
    return n

assert period(7, 2) == 3 and period(7, 10) == 6
assert period(11, 10) == 2 and period(11, 12) == 1
print("period controls:", period(7, 2), period(7, 10),
      period(11, 10), period(11, 12))

N = 20_000
phi = list(range(N + 1))
for p in range(2, N + 1):
    if phi[p] == p:
        for k in range(p, N + 1, p):
            phi[k] -= phi[k] // p

def coprime_pairs(n):
    return 2 * sum(phi[1:n + 1]) - 1

assert coprime_pairs(5_000) == 15_200_915
assert coprime_pairs(20_000) == 243_180_791
print("finite grid controls:", coprime_pairs(5_000),
      coprime_pairs(20_000))
print("finite density:", float(remaining), "all-prime limit:", 6 / pi**2)
print("prime scale directions:", [(p, 1 / p, log(p)) for p in P])
```

### Independent-check scope, adversarial review and verdict

- Integer enumeration versus a CRT product is an independently implemented exact count. The totient sieve is a separate known-identity check of the finite-grid slide values.
- This is **not** a statistical randomization test. It establishes arithmetic consistency, not causal emergence, not a spectral fit and not evidence for a Lineum universe.
- The arbitrary orientation and coordinate origin of a rendered grid are observer choices; the residues, density and counting identities are intrinsic to the explicitly selected integer-coordinate construction, not to every possible geometry.
- The 20,000-side count mismatch remains unresolved pending boundary and pixel-coordinate conventions.
- **G0:** open/untested as a zero-gap mapping; **G1:** fixed-base digit-cycle interpretation is not coordinate independent; **G2:** known Fourier identity, not a new result; **G3:** known log-prime arithmetic oscillations, not yet linked to a geometric operator here; **G4:** deferred genuine Lineum-native evidence; **G5:** controls still required before any scored fit.
- **Local verdict:** supported_within_tested_domain for the exact prime-layer counts; unresolved for a geometrically defined zero-gap connection; no claim about actual Lineum output.
- **Canonical impact:** the existing Zeta–RNB negative audit stays closed; no whitepaper or engine change is justified.
- **Root-programme relationships:** independent of continuous-source cosmology; related arithmetic/spectral motif does not grant membership in that programme. No cross-programme physical equivalence is claimed.

**Next authorized scientific checkpoint:** define a base-independent length/phase observable from the *2D intersection geometry*, and derive an explicit **non-fitted** prediction (including which zeta-gap index, which normalization and what would constitute a failed prediction) before touching Lineum data. Predeclare shuffled/composite/Poisson-like controls. Do **not** re-use earlier RZ-0/RZ-1 operators or silently reopen Eq-12. If this definition cannot be made without target-dependent tuning, record a bounded non-identifiability result and open the owner-intuition failure gate rather than trying random scales.

**Persistence receipt:** this complete standalone method, results and interpretation are being retained directly as ordinary Git Markdown; the original presentation screenshots are not embedded or redistributed.
