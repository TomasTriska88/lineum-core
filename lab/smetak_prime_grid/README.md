# Smeták prime-grid reference study — experimental only

**Source:** Vlastimil Smeták (lead), Jiří Chlebníček, Boris Koštel, *Detekce prvočísel pomocí π*; https://www.youtube.com/watch?v=7ardq_YdtVQ  
**Date:** 2026-11-22  
**Status:** Independently replicated elementary number-theory and spatial-Fourier results. **Not a new proof, not a new physical phenomenon, and not a verified Lineum result.**

## The geometry in plain language

Every prime p labels a repeated 2D grid of points where **both coordinates are divisible by p**. Its area density is 1/p². Removing points covered by *any* prime grid leaves lattice points with coprime coordinates: gcd(x,y)=1. This construction relates the displayed counts to the classical Euler product, not to a newly discovered law.

The number of coprime ordered positive-integer pairs in an N×N square is exactly:

`C(N) = 2 * sum(EulerTotient(k) for k in 1..N) - 1`.

As N becomes large, C(N)/N² tends to 6/π². The finite-size error does not decrease monotonically.

**Verification from the supplied slides:** 5000×5000: slide 15,200,915, exact count 15,200,915; 20000×20000: slide 243,180,790, exact count 243,180,791 (one-pixel discrepancy; cause unknown).

## What "waves" means here

Each grid divisible by p can be expressed as a sum of complex spatial Fourier modes. The Fourier reconstruction of the grid is an **algebraic identity**: not a traveling physical wave, not a spontaneous Lineum resonance, and not evidence of the Riemann hypothesis. For p = 2,3,5,7, the 2D grid repeats every 210 coordinates in both directions. A structured periodic image produces spectral peaks, unlike the same pixels randomly shuffled. This is expected; the shuffle control does not establish a new effect.

**Crucial distinction:** spatial waves of prime-divisibility grids involve modes based on 1/p; the zeta-function explicit formula involves log(p). They are not interchangeable.

## Experimental methodology and limitations

- All raw slide screenshots stay under the user's control; this public repository contains only independently authored documentation and test code until rights to republish slides are established.
- Slide pixel counts were independently recomputed with an exact integer totient sieve.
- The grid and Fourier reconstruction were computed independently and numerically compared.
- The Fourier peak was compared against 100 seeded spatial shuffles preserving the number of remaining pixels. This is a *simple demonstration of periodicity*, not a test for a connection to nontrivial zeta zeros.
- No actual Lineum simulation output was used. A genuine follow-up must compare **untuned** Lineum observables, controls, multiple seeds, and independently obtained zeta-zero spacings.

## Reproduce

Install Python with `numpy` and `pytest`, then from this folder:

```sh
python prime_grid_study.py
python -m pytest -q test_prime_grid_study.py
```

Outputs are written to `results/`. Tests were independently run locally on 2026-11-22 and all **7** passed.

**Research provenance:** Full capture archive 80 original frames; manually selected 65 views after flagging repeated captures. Source video and all three credited authors must accompany derivative analyses. No novel claims from these screenshots are accepted as established facts.
