# External research reference: *Detekce prvočísel pomocí π*

**Status:** External source / unverified mathematical claims / research reference only  
**Record date:** 2026-11-22  
**Source video:** https://www.youtube.com/watch?v=7ardq_YdtVQ  
**Lead author credited on title slide:** Vlastimil Smeták  
**Co-authors credited on title slide:** Jiří Chlebníček; Boris Koštel  

## Scope and provenance

The user supplied **80 screenshots in chronological order**, in four batches of 20 (filenames `image(20261122-010305).png` through `image(20261122-013018).png`). These are stills from a presentation, **not a transcript**, independently inspectable source code, or full video analysis.

## Git-first research storage status

**Git-only policy adopted:** See `.agent/rules.md` §17 on this research branch.

- **Committed to Git:** Source attribution, the presentation analysis, the reproducible numerical study and seven tests under `lab/smetak_prime_grid/`, with a machine-readable results snapshot.
- **NOT yet committed:** The original 80 user-supplied PNG slides and the curated 65-view copy. The connector can write Git UTF-8 source text but cannot move binary ZIP files directly from the execution container to Git. Therefore the source archive is **NOT fully migrated to Git**. It would be incorrect to call this task complete.
- **Integrity of pending local binary archive:** 80-original ZIP SHA-256 `44ecd3250e89ee6dcbcb33966cbbdcbe089a40365ac3bc5e8ccee59927492dd7`; curated 65 ZIP SHA-256 `e39389890b65171e1336d95d7099fa1d29bf36ef5fcaa21cb06c46566968ed3a`. Preserve original screenshot hashes and duplicate mappings when a rights-compatible Git repository with binary transfer support is available.
- **Copyright:** This repository is public. The photographs contain slides from a third-party presentation; cite the authors but do not assume that public redistribution of the slides is licensed. Place source images only in a rights-compatible Git repository (preferably private while rights are unclear).
- **No off-Git research archive is an accepted final destination.** The research output in Git is reproducible without the original photographs; the complete source-image retention requirement is still **blocked**.

**15 repeated captures** were identified across the 80 frames by slide-content review (including altered cropping). No source frame should be discarded prior to rights-compatible archival. The source image is not yet in this Git history.

## Observed material in all 80 supplied screenshots

- Presentation title, source author credits, and prime detection with π.
- Illustrative geometric diagrams labeled *Graf 2ⁿ*, *Graf Xⁿ*, and a 32,000 × 32,000 px recursively constructed structure (including zooms).
- Figures labeled as a fractal representing composite integers, half-ellipses for integer factorization, electromagnetic fields in numbers, and a quadrilateral network associated with a claimed Goldbach conjecture proof.
- Introductory Euler product, Riemann zeta function, classical ζ(2) = π²/6 relation, and Bernoulli closed forms for even zeta values.
- Worked, partially repeated prime Euler-product factors with initial primes 2, 3, 5, 7 for exponents **s = 2** and **s = 26**, with corresponding expressions yielding approximations of π.
- Some nested rational expressions named “prime layers”; these must be checked algebraically before assuming that they define a novel prime detector.

A temporary local archive has an image-by-image manifest and duplicate mapping; **these binary assets and full manifest are not yet Git-tracked**, so no persistent Git image inventory is claimed.

### Batch 3: grid construction and number geometry (frames 41–60)

- GIMP demonstration of two prime-number layers and larger (5000² and 20000² pixel) areas; ratios yield approximations to ζ(2) and π.
- Definition of periodically spaced 2D grid layers with nominal area fractions 1/n² (examples n=2,3,4,5), plus rules for overlap and change when adding a new prime layer.
- Prime-number layer intersections with 2 and 3; later with 2,3,5; multiple slides are alternate captures of the same source slide.

### Batch 4: intersections and finite grids (frames 61–80)

- Intersections for prime sets 2,3,5,7 and 2,3,5,7,11; slide-derived counts for k primes are 2^k−1 nonempty subset products and 2^k including the empty subset, giving observed ratios 1/2, 3/4, 7/8, and 15/16. This is ordinary subset combinatorics, not itself proof of novel prime distribution laws.
- Slides discuss Bertrand's postulate (already a proven theorem), claimed advantages of infinite grids, and a passage to finite multiplication tables for prime detection over a specified interval.
- These frames depict a geometrical approach related to the classical sieve of Eratosthenes and the Euler-product viewpoint; their computational complexity and claims of stronger results remain untested.

### Clear research boundary

The current visual record does **not** demonstrate that prime-number fractions fill the gaps between nontrivial Riemann zeros, nor that Lineum's emergent wave modes reproduce this arrangement. Test such a claim independently against explicit controls before considering it supported.

## Scientific interpretation and cautions

1. **Established mathematics:** For Re(s) > 1, the Euler product expresses ζ(s) through prime factors. Known even-integer ζ(2k) identities relate values of the zeta function and powers of π. Finite Euler products therefore produce corresponding approximations. These facts are not, by themselves, a new proof or algorithmic breakthrough.
2. **Unverified claims:** The slide headed “důkaz Goldbachovy domněnky” is a presentation claim, not sufficient evidence of a complete proof. The claimed prime-detection method, its correctness, and computational advantage need a formal definition and independently repeatable examples.
3. **Visual patterns:** Geometric and fractal-looking plots do not alone establish an invariant physical mechanism. Their exact generating rules, axes, and scaling must be recovered from the source before analogy to the Lineum fields ψ, φ, or κ is evaluated.
4. **Riemann zeros:** The screenshots establish an Euler-product/ζ connection, **not** a demonstrated positional/geometric map from gaps between nontrivial zeros to prime-fraction cycles, or a relationship with the Lineum zeta-points. Such a map remains a research hypothesis.
5. **Attribution:** Any future study, comparison, derived figure, or accepted method that uses this presentation must credit **Vlastimil Smeták, Jiří Chlebníček, and Boris Koštel**, and link to the source video. Clearly distinguish the originators' claims from independent Lineum test results.

## Suggested independent verification (not yet run)

- Reproduce the finite Euler products for s=2 and s=26 using high-precision arithmetic and check the displayed π approximations against the corresponding even-zeta/Bernoulli constants.
- Reconstruct the nested “prime layers” symbolically and establish whether they are algebraically equivalent to the finite Euler products.
- Obtain the exact definitions or source code behind the geometric figures; vary scale and render parameters to check which symmetries are genuine.
- If exploring a Lineum connection, preregister a **specific** frequency/spacing observable and compare with matched random and known-wave controls. Treat visual matches or high correlation of sorted sequences as insufficient.
- Do not change the frozen Lineum core or canonical scientific claims based on presentation screenshots.

**This record intentionally remains external research documentation.** Additional image batches may extend the archive and this index; no experimental promotion is implied.

## Independently reproduced numerical and wave results

A new lab reference implementation is available at `lab/smetak_prime_grid/` on the research branch, along with 7 passing local tests and `results/reference_results.json`. **No new mathematical discovery is claimed.**

- Exact count of coprime integer-coordinate pairs on a 5000² grid = 15,200,915, matching the author's slide. For a 20000² grid = 243,180,791 versus slide 243,180,790 (difference one); the relation is already classical mathematics, not a discovery.
- A prime-divisibility grid can be reconstructed exactly by superposing spatial Fourier modes. This is the ordinary Fourier representation of a periodic pattern, *not* physically propagating waves and not evidence of new Lineum dynamics.
- The experimental FFT control compares a deliberately periodic pattern to 100 randomly shuffled pixel patterns. The dramatic contrast is expected and **cannot support** a claim of novel connection to Riemann zeros.
- Whether the presenter explicitly discusses this Fourier reformulation **cannot be inferred from the supplied stills**; even if not, the mathematical representation is known and should not be marketed as a novel result.
