# External research reference: *Detekce prvočísel pomocí π*

**Status:** External source / unverified mathematical claims / research reference only  
**Record date:** 2026-11-22  
**Source video:** https://www.youtube.com/watch?v=7ardq_YdtVQ  
**Lead author credited on title slide:** Vlastimil Smeták  
**Co-authors credited on title slide:** Jiří Chlebníček; Boris Koštel  

## Scope and provenance

The user supplied **80 screenshots in chronological order**, in four batches of 20 (filenames `image(20261122-010305).png` through `image(20261122-013018).png`). These are stills from a presentation, **not a transcript**, independently inspectable source code, or full video analysis.

The complete, unmodified original PNG screenshots, a SHA-256 manifest, deduplication annotations, and a selected deduplicated reading edition are preserved in the user's **private ChatGPT Library** at:

- Full source archive (**80 original frames**, SHA-256 ZIP `44ecd3250e89ee6dcbcb33966cbbdcbe089a40365ac3bc5e8ccee59927492dd7`): `/Research/Lineum/External - Smetak pi 2026-11-22/lineum-smetak-presentation-ALL-80-originals-2026-11-22.zip`
- Deduplicated viewing archive (**65 representative frames**, SHA-256 ZIP `e39389890b65171e1336d95d7099fa1d29bf36ef5fcaa21cb06c46566968ed3a`): `/Research/Lineum/External - Smetak pi 2026-11-22/lineum-smetak-presentation-CURATED-65-2026-11-22.zip`
- Searchable inventory: `/Research/Lineum/External - Smetak pi 2026-11-22/MANIFEST.json`.

**15 repeat captures were flagged by manual slide-content comparison** (e.g. different crop or player overlay), but are **not deleted from the full archival ZIP**. The exact duplicate-to-representative sequence mapping is in each archive's `DUPLICATES.csv`.

**Binary ZIP limitation:** The available GitHub integration in this session supports text file changes, but could not transfer these locally generated binary archives to GitHub. Therefore the ZIP files are **not yet hosted in GitHub**. This document is the Git-tracked provenance and analysis index. Do not misrepresent the archives as GitHub assets.

This path is a personal research archive, not a public download link. Images are **not embedded or published in this public repository**, because their reuse/publication license has not been established. Do not encode the slides as base64 in source code or Markdown; attribution does not substitute for a license.

## Observed material in all 80 supplied screenshots

- Presentation title, source author credits, and prime detection with π.
- Illustrative geometric diagrams labeled *Graf 2ⁿ*, *Graf Xⁿ*, and a 32,000 × 32,000 px recursively constructed structure (including zooms).
- Figures labeled as a fractal representing composite integers, half-ellipses for integer factorization, electromagnetic fields in numbers, and a quadrilateral network associated with a claimed Goldbach conjecture proof.
- Introductory Euler product, Riemann zeta function, classical ζ(2) = π²/6 relation, and Bernoulli closed forms for even zeta values.
- Worked, partially repeated prime Euler-product factors with initial primes 2, 3, 5, 7 for exponents **s = 2** and **s = 26**, with corresponding expressions yielding approximations of π.
- Some nested rational expressions named “prime layers”; these must be checked algebraically before assuming that they define a novel prime detector.

The per-image inventory and integrity hashes are in `MANIFEST.json`, the manually reviewed repeated-capture mapping in `DUPLICATES.csv`, and the curated sequence in `CURATED_ORDER.txt` inside the consolidated ZIP archives.

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
