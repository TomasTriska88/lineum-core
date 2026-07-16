# Lineum Under Adversarial Review: Fundamental Physics, Philosophy, and a Verification Program

**Document status:** active research basis for future whitepaper revisions; not itself a whitepaper or evidence that the theory is physically valid
**Research version:** 0.7
**Evidence and calculation cutoff date:** July 16, 2026
**Language:** English
**Reproducibility:** all seven embedded programs reproduce the embedded JSON outputs with semantic identity
**Current confidence:** high for the reproduced numerical results, deterministic reference lane, time-step diagnosis, zero-kappa RNG-claim audit, and scope findings; medium for the numerical classification of stochastic candidates; low for their physical interpretation and the other untested hypotheses proposed for future work
**Standalone portability:** all essential equations, inputs, programs, outputs, limitations, and external source metadata are embedded in this single document; no repository file is required
**Scope of evaluation:** published arguments, mathematical statements, and physical claims only; this document contains no personal or reputational assessment

## Abstract

This study subjects the Lineum project to adversarial physical, mathematical, and philosophical scrutiny. Its default rule is that every ontological or physical claim made by Lineum remains an **untested hypothesis** until it follows from a single well-defined dynamics, passes numerical checks, and is consistent with existing experiments. The review combines an audit of four repositories, primary scholarly literature, a full-text analysis of Jan Fikáček's dissertation, a bibliographic and sample-based analysis of his book, a review of relevant articles and public lectures, and original reproducible calculations.

The result is demanding but constructive. Lineum has a legitimate research objective: to investigate whether finite local microdynamics can produce smooth macroscopic phenomena, stable localized objects, and a physical account of information. A later Gate-0 audit has now established one named deterministic regression lane and corrected one opt-in time-step inconsistency without changing historical defaults. The implementation is nevertheless not yet a physical theory of spacetime or quantum mechanics. It still does not supply one final canonical physical law, a relativistic structure, the Born rule, a measurement mechanism, a model of gravity, a derivation of mass, or demonstrated stable particles. Its stochastic ontology is also unresolved. A regular square lattice introduces preferred directions; some numerical schemes reduce that artifact but may replace strict locality with a global update.

The original calculations in this report show, among other results: (i) angular anisotropy of lattice dispersion relations that grows with wavenumber; (ii) instantaneous nonzero tails under spectral evolution; (iii) finite-lattice wave-packet energy saturation without a dynamical prohibition against collapse into one cell; (iv) logical independence between a field norm and Shannon information; (v) the Bell bound \(|S|\le 2\) for local hidden-variable models, compared with the quantum value \(2\sqrt 2\); (vi) decoherence without selection of a unique outcome; (vii) regularization of black-hole curvature by a cutoff without derived gravitational dynamics; (viii) numerical convergence of discrete transport to smooth macroscopic motion, which does not by itself establish ontically continuous motion; and (ix) a state-independent Peres–Mermin contradiction for noncontextual hidden values.

The most defensible next step is to avoid claiming that “the lattice already explains the physics” and instead let several clearly separated hypotheses compete: an effective reaction–diffusion medium, a local unitary quantum automaton, Lorentz-compatible random causal discreteness, charge- or topology-stabilized particles, a derived nonsingular gravitational sector, and operational finitism with certified error bounds. This document defines decision gates and rejection criteria for each option.

---

## 1. Technical Summary and Current Conclusion

### 1.1 What the present evidence supports

| Claim | Evidential status | Conclusion of this review |
|---|---:|---|
| Lineum currently implements finite numerical models of two fields on a periodic 2D grid. | **Documented** | Yes, as a software and experimental platform. |
| Lineum has one reproducible software reference lane. | **Implemented and characterized** | Yes: `RD-0` is a deterministic regression ruler with named legacy and continuous-time profiles; it is not a declaration of fundamental physics. |
| The current \(\phi\)-diffusion defines one trajectory when \(\Delta t\) is refined. | **False in legacy; repaired in an opt-in profile** | The legacy term is applied per update. Multiplication by \(h\) restores first-order convergence in the tested deterministic lane. |
| The current ongoing stochastic source has a nonzero continuous-time variance limit. | **Contradicted in the tested source/diffusion lane** | Ensemble spread scales approximately as \(h^{0.488}\) and vanishes; several alternative contracts retain finite spread but encode different physics. |
| The historical zero-\(\kappa\) “true RNG / edge of chaos” test demonstrates chaos. | **Contradicted by source audit, exact recurrence, and runtime reproduction** | Its original perturbation is overwritten, while a new \(10^{-5}+10^{-5}i\) input is added for all 1,500 steps. The threshold crossing is a damped geometric sum, not exponential sensitivity or true randomness. |
| All four audited repositories jointly define Lineum physics. | **No** | Core is the canonical research authority. Dynamics is mainly a company and product layer; OEA and Lina EI are purpose-built applications and stress tests. |
| Discrete microdynamics can approximate smooth macroscopic motion. | **Established in general and reproduced here** | Yes, for smooth data and within a stated resolution; this does not establish whether nature is ontically discrete or continuous. |
| Physical space is a regular lattice. | **Not demonstrated** | This is an ontological hypothesis, not a consequence of the code or of Fikáček's critique of infinity. |
| The current dynamics is Lorentz invariant. | **Contradicted by the present model** | The square lattice and dissipative evolution select a preferred frame and preferred directions. |
| Lineum already produces stable elementary particles. | **Not demonstrated; internal negative results exist** | The branches examined here have not produced isolated stable objects without artificial boundaries, caps, or an active background. |
| The lattice dynamically prevents a particle from collapsing into one cell. | **Not demonstrated** | The cutoff bounds the numerical divergence, but does not itself provide a repulsive interaction or conservation law. |
| Information is mass. | **Not demonstrated** | Landauer's principle relates logically irreversible information processing to heat; it does not establish a universal identity between abstract information and rest mass. |
| Lineum reproduces quantum mechanics and Bell correlations. | **No** | A many-body Hilbert-space construction, the Born rule, a measurement model, and a Bell-experiment model are absent. |
| Lineum reproduces quantum contextuality. | **Not verified** | A physical model of compatible measurement contexts and the Peres–Mermin protocol is absent. |
| Lineum explains measurement outcomes without an observer. | **No** | Decoherence, objective collapse, and branching have not been derived as alternatives within one canonical dynamics. |
| Lineum models a nonsingular black hole. | **No** | A metric, Einstein or surrogate field equations, a source tensor, and tests of the horizon and energy conditions are absent. |
| Lineum proves that actual infinity does not exist. | **No** | Even if physical reality is finite, that premise alone does not select a particular lattice, topology, field content, or equation. |

### 1.2 Alignment with Jan Fikáček's published program

The alignment is **strong in motivation**, **partial in ontological direction**, and currently **limited at the level of specific physical evidence**.

Lineum overlaps with Fikáček's program in treating physical singularities as possible signs of an incomplete theory, asking whether infinities mark the boundary of a model's validity, emphasizing physical carriers of information, and exploring particles as localized manifestations of a deeper medium. His more recent public lectures also examine ideas that are conceptually close to Lineum: a physical wave that guides a localized object and particles understood as condensates or excitations of an environment.

The important difference is one of specificity and evidence. Fikáček's philosophical argument does not by itself specify a regular square lattice, a particular pair of fields, or a concrete update law. His emphasis on empiricism therefore raises the evidential standard for Lineum: the model must predict a measurable phenomenon that cannot be produced merely by selecting a numerical scheme or changing a calibration convention.

### 1.3 Recommendations for current whitepapers

Until the gates below are met, we recommend:

1. **maintain the canonical physics specification in Lineum Core only** and mark all application deviations in Dynamics, OEA and Lina EI as downstream variants until they are formally accepted back into Core;
2. **retain** platform description, exact dimensionless equations, numerical constraints, negative results, and clearly labeled hypotheses;
3. **rephrase** "Planck pixels", "steps are reality", "linons are particles", and "information has mass" into testable options;
4. **suspend** claims about Lorentz invariance, quantum measurement, Bell correlations, gravity and black holes until there is a derivation and test;
5. **remove from physical evidence** SI frequencies and masses created only by assigning reporting \(\Delta t\); they are calibration scenarios, not predictions;
6. **cite Jan Fikáček's work as a source of research questions and philosophical premises, not as empirical validation of a particular Lineum dynamics**.
7. **use the named deterministic continuous-time profile for refinement claims and the named legacy profile for historical reproduction; do not call either the final Lineum law**;
8. **do not describe the present stochastic source as a continuously driven quantum vacuum; keep initial branching, continuous forcing, discrete events, deterministic chaos, memory, and quantum-amplitude explanations as separately falsifiable hypotheses**.
9. **withdraw “true RNG” and “edge of chaos” as conclusions of the historical zero-\(\kappa\) test; require exact replay, one-shot perturbation growth, a positive Lyapunov estimate, and robustness before restoring either claim**.

### 1.4 Claim-language guide for future whitepaper editing

| Strong or ambiguous wording | Formulation safe in current state | What is required to restore the strong version |
|---|---|---|
| "Space is made up of Planck pixels." | "The simulation uses dimensionless cells; the physical length of the cell is an open hypothesis." | independent calibration \(a_*\), derived prediction and compliance with Lorentz-invariance bounds |
| "Discrete steps are a reality." | "Discrete update is a candidate microdynamics and numerical method." | empirically distinguish the ontic discreteness from the regulator |
| "Changing `dt` only changes simulation precision." | "This is true for the validated deterministic profile, not for the legacy \(\phi\)-diffusion or unresolved stochastic source." | convergence of every retained deterministic and stochastic term at fixed physical time |
| "Coordinates are integer to arbitrarily large distances." | "Each run has a finite periodic domain; enlarging the box is a numerical sequence of finite models." | define the global topology and explain its relation to the rejection of actual infinity |
| "Linon is a particle." | "A linon is a candidate localized excitation." | cap-free stability, \(E(p)\), spin and statistics, collisions, and convergence |
| "Frequency gives mass \(m=hf/c^2\)." | "Under a chosen SI calibration, a frequency can be converted to a mass-equivalent energy." | a dynamically derived energy, independent calibration of \(\Delta t\), and independent tests of inertial and gravitational mass |
| "The model is isotropic." | "The chosen spectral space operator is angularly isotropic on the periodic box; local stencils have a measured residual anisotropy." | rotational and Lorentz Ward identities or the experimentally sufficient emergent limit |
| "The model is a local cellular automaton." | "An explicit finite stencil can be local; a spectral exponential has a global real-space kernel." | one canonical update law with an exact discrete causal cone |
| "The norm is energy." | "The norm is a diagnostic quantity unless it is derived from time-translation symmetry or a Hamiltonian." | an action or Hamiltonian, a Noether derivation, and conservation under the complete update |
| "The lattice removes singularities." | "A UV cutoff bounds numerical values." | a dynamically regular solution without a cap, regulator independence, and the correct macroscopic limit |
| "Information is matter." | "Information requires a physical carrier, and logically irreversible manipulation can have an energy cost." | a specific Hamiltonian and a measurable, carrier-dependent relation \(\Delta I\to\Delta E\to\Delta m\) |
| "Actual infinity is logically disproved." | "Lineum examines finitism as a philosophical and physical hypothesis." | an exact formal system, a cardinality/inclusion/density separation, and a measurable consequence of the finite threshold |
| "OEA Shows Cosmic Web/Gravity." | "OEA creates morphologically similar figures using image operations." | statistical comparison with cosmological data and derived gravitational dynamics |
| "Dynamics, OEA, or Lina EI confirm Lineum." | "Downstream applications test the transfer of selected equations and may reveal integration errors." | canonicalization of any change in Core and genuinely independent external replication of a physical prediction |
| "The tests confirm the physics." | "Tests validate implementation contracts." | experimental prediction, blind data and independent replication |

Every future physics claim should be required to state: **equation**, **domain of validity**, **units**, **source of evidence**, **numerical uncertainty**, **strongest comparative model**, and **result that would disprove the claim**.

---

## 2. Method, Scope, and Rules of Evidence

### 2.1 Examined material

The audit covered four repositories in these revisions:

| Repository | Revision | Branch | Working-copy status during the audit |
|---|---|---|---|
| Lineum Core | `badb9fbca451a4f9edee0d42d34a00a29fcd1b92` | `develop` | contained uncommitted changes |
| Lineum Dynamics | `9890cf3fd557717767b8a93ede00a73a36318d22` | `develop` | contained uncommitted changes |
| OEA | `5b3b7394e21a7bc1d01420cbefa13f4ca5c2f399` | `dev` | clean |
| Lina EI | `4ea7335bb5db8c55ca11f474478acd087975c25e` | `main` | contained uncommitted changes |

This table is part of the reproducibility record: conclusions about implementation state may be superseded by later code changes. The review did not modify the pre-existing uncommitted changes or interpret them as independent experimental evidence.

Repositories do not have the same epistemic role in this review:

| Repository | Primary role | What can be legitimately proven from it | What cannot be deduced from it without further evidence |
|---|---|---|---|
| **Lineum Core** | major research repository, history of equations, whitepapers and reference physics experiments | what the project actually formulates as candidate Lineum dynamics in a given revision; numerical and negative results of the main research | that formulated dynamics describe nature; here too, physical conclusions remain unverified hypotheses |
| **Lineum Dynamics** | mainly a company, product, and monetization layer that consumes or copies parts of Core | whether downstream integration preserves Core contracts, how scientific concepts are transferred into products, and whether semantic divergence occurs | new canonical physics or independent replication merely because a copied test or module passes |
| **OEA** | purpose-built generative-imaging software inspired by Lineum themes | properties of its image algorithm, including determinism, ablation behavior, and output sensitivity | a definition of Lineum, cosmological proof, physical validation of a lattice, or an identity between image intensity and energy or matter |
| **Lina EI** | purpose-built application using candidate Lineum equations | integration stress tests, deterministic replay, losses introduced by observation mappings, and application-specific negative results | general validity of the equations, a canonical change to the theory, or independent confirmation of a physical ontology |

If meanings conflict, the explicit research specification in Lineum Core takes precedence when describing the candidate theory. A deviation in Dynamics, OEA, or Lina EI remains an application fork, integration deviation, or experimental probe until it is accepted into Core as a versioned canonical change. This priority does not grant Core automatic empirical truth; it only determines **which statement is under test**.

A control set with fixed seed `20260715` was created for the audit. The checker had SHA-256 `1347346bf7b5f4a48a7e74133542536643db01b7dfb1a939c24904000bdb35b2`; its structured output matched SHA-256 `d7471ab706ae18bd122fb7c91b0d1cd225ac275cbbaa957332ebcc91e2fdd87a` on two consecutive runs. The code re-extracted directly from the appendix produced a semantically identical JSON on the auditing environment, and also an identical SHA-256 when written with the original CRLF line endings. The complete executable program, parameters and aggregated numerical outputs are embedded in the appendix of this document; reproduction is therefore not dependent on an external notebook or local machine state.

The standalone OEA ablation check uses the same seed, NumPy 1.26.4 and SciPy 1.17.1. The program has SHA-256 `a2862597f6e8262957ec146c5c8696aff7881a248474f4650a4f6492da890ef7`; the two runs produced bitwise SHA-256 output `12294612bc00b0c78b6f4054d839808cb7f74d5083d5c211df0970ee853310e9`. Also, this program and the full output are embedded in the appendix.

### 2.2 Meaning of the evidence labels

- **[OBSERVED]** directly from a code audit, documentation or published source.
- **[CALCULATED]** from equation or reproducible program embedded in an appendix.
- **[LITERATURE]** conclusion of a primary or authoritative scholarly source.
- **[INFERENCE]** a reasonable but not deductively necessary interpretation of multiple pieces of evidence.
- **[HYPOTHESIS]** a proposal that does not yet have experimental confirmation.
- **[OPEN]** question without sufficient decisive test.

### 2.3 Hierarchy of evidence

Reproducible experimental data carry the greatest weight, followed by peer-reviewed primary studies, precisely derived mathematical implications, and reproducible code. Whitepapers, documentation, blogs, videos, analogies, and aesthetic appeal can motivate a hypothesis, but do not confirm it by themselves. Internal tests establish that software follows its stated contract; they do not establish that the contract describes nature.

### 2.4 What this study does not claim

The study does not prove that spacetime is continuous, that actual infinity exists physically, or that a discrete foundation is impossible. It establishes a narrower conclusion: **no specific Lineum ontology follows from the present evidence**, and some current implementation choices are in tension with well-tested physics.

---

## 3. What exactly is the current Lineum

### 3.1 There is not yet one canonical theory

In the main Lineum Core research repository, the audit found at least four significantly different layers:

1. simultaneous simple update of two real fields in the presentation whitepaper;
2. historical equation denoted by Eq. 10 and Eq. 11;
3. later provisional equation with biharmonic term;
4. real runtime branches with a diffuse and complex wave backend.

These layers are not simply numerical implementations of the same physics. They differ in derivative order, linearity, dissipation, field type, locality, conserved quantities, and long-term qualitative behavior. Until one equation and one interpretation of its variables are declared canonical, Lineum cannot be falsified as a single theory. Application-specific variants in Dynamics, OEA, and Lina EI do not decide this selection; they provide supporting evidence about integration and robustness, not an equivalent source of fundamental law.

A subsequent characterization step narrows this statement without overturning it. Lineum now has a provisional **software reference lane**, `Reference Dynamics 0` (`RD-0`), consisting of the noise-free diffusive subset on a periodic LAP4 grid. It is a regression ruler for comparing implementations and future candidates, not another claim that an `Eq-N` label has become a law of nature.

### 3.2 The equation presented in the summary whitepaper

For dimensionless arrays \(\psi_{ij}^n,\phi_{ij}^n\) on a periodic 2D lattice, the reported update has the form

\[
\psi^{n+1}=\psi^n+\tilde\lambda+\xi+\phi^n\psi^n-\delta\psi^n
+\nabla_d^2\psi^n+\nabla_d\phi^n,
\]

\[
\phi^{n+1}=\phi^n+
\alpha_{\rm eff}(|\psi^n|^2-\phi^n)+\beta_{\rm eff}\nabla_d^2\phi^n,
\]

while the \(\kappa\) parameter can be spatially variable. The typical parameters given are

\[
\alpha=7\times10^{-4},\quad \beta=1.5\times10^{-2},\quad
\delta=4.62\times10^{-3},\quad \sigma_\xi=5\times10^{-3},\quad \kappa=0.5.
\]

This is a dimensionless periodic model in two spatial dimensions. It does not include a metric, the speed of light as a dynamical constant, \(\hbar\), \(G\), spinors, gauge fields, or transformation rules for the Lorentz group. Labeling its structures as particles is therefore an analogy at this stage.

The \(\Delta t=10^{-21}\,\mathrm{s}\) assignment correctly appears as a reporting label in the material, not a derived property. Subsequent

\[
f=\frac{\tilde f}{\Delta t},\qquad m=\frac{hf}{c^2}
\]

is therefore a conditional conversion: a different choice of \(\Delta t\) produces a different reported “mass” without changing the simulation. Without independent calibration, the model does not predict \(m\).

### 3.3 Historical Eq. 10 and Eq. 11

Eq. 10 was formulated approximately as

\[
\partial_t\psi=\nabla^2\psi+[\alpha\tanh(c_1\phi)-\gamma]\psi,
\]
\[
\partial_t\phi=\beta\nabla^2\phi+\alpha\phi(|\psi|^2-\phi).
\]

Later Candidate Eq. 11 added saturation and gradient nonlinearity:

\[
\partial_t\Psi=D_\psi\nabla^2\Psi+
[\alpha\tanh(c_1\Phi)-\gamma-\lambda\Phi^2-c_w|\nabla\Psi|^2]\Psi,
\]

\[
\partial_t\Phi=D_\phi\nabla^2\Phi+c_2|\Psi|^2-\gamma_\phi\Phi.
\]

Later internal results withdrew the earlier optimistic interpretation of robust particles. They documented activity far from the putative object, persistent background excitation, collapse under global conservation, no convincing isolated \(N=1\) object, and no robust binding for \(N\ge 3\). These are scientifically valuable negative results and should remain visible in future whitepapers.

### 3.4 Provisional biharmonic backbone

A later design uses

\[
\partial_t\psi=D_r\nabla^2\psi-\nu\nabla^4\psi+
(g\phi-\mu-\lambda\phi^2)\psi,
\]

\[
\partial_t\phi=D_\phi\nabla^2\phi+a|\psi|^2-b\phi.
\]

The biharmonic term penalizes short wavelengths, but for \(D_r>0\) and \(\nu>0\) it does not by itself select a nonzero wavenumber: the linear damping rate is \(-D_rk^2-\nu k^4\), so the least-damped mode is always \(k=0\). Selecting a finite scale requires an additional instability, a multifield Turing mechanism, front pinning, or another competition between operators.

Homogeneous solutions can be analyzed without simulation. In addition to the vacuum \((\psi,\phi)=(0,0)\), there is a pair of non-zero branches at \(g^2\ge 4\lambda\mu\)

\[
\phi_\pm=\frac{g\pm\sqrt{g^2-4\lambda\mu}}{2\lambda},
\qquad
|\psi_\pm|^2=\frac{b\phi_\pm}{a}.
\]

For an amplitude perturbation \(u\) and a second-field perturbation \(v\), the Fourier mode \(k\) has the linearization matrix

\[
M(k)=
\begin{pmatrix}
-D_rk^2-\nu k^4 & |\psi_0|(g-2\lambda\phi_0)\\
2a|\psi_0| & -D_\phi k^2-b
\end{pmatrix}.
\]

At \(k=0\), the determinant is \(-2b\phi_0(g-2\lambda\phi_0)\). The lower branch \(\phi_-\) is therefore unstable to amplitude perturbations, whereas the upper branch \(\phi_+\) is homogeneously stable because \(g-2\lambda\phi_+=-\sqrt{g^2-4\lambda\mu}<0\). The phase perturbation has eigenvalue \(-D_rk^2-\nu k^4\), including the neutral global \(U(1)\) mode at \(k=0\).

In the fast-relaxation limit for large \(b\), substituting \(\phi\approx a|\psi|^2/b\) yields an effective cubic–quintic reaction

\[
\partial_t\psi\approx D_r\nabla^2\psi-\nu\nabla^4\psi+
\left[-\mu+\frac{ga}{b}|\psi|^2-\frac{\lambda a^2}{b^2}|\psi|^4\right]\psi.
\]

The quintic term can limit the amplitude without a software cap, but the natural nonzero attractor here is a spatially homogeneous plateau. A localized dissipative structure would require demonstrated coexistence of the vacuum and plateau states, front equilibrium, and stability against radial, azimuthal, and translational perturbations. The analysis therefore supports the statement “the equation contains a dynamically formulated saturation mechanism,” but not the stronger statement “a particle has been derived.”

The audited revision also did not contain an operational implementation of the stated ETD2 scheme, dealiasing, and corresponding validation suite. The equation is therefore an interesting hypothesis, not a validated physical core.

### 3.5 Observed runtime behavior

The default runtime uses approximately

\[
\Delta t=1,\quad D_\psi=D_\phi=0.05,\quad
\eta=0.005,\quad r=0.0007,\quad \sigma=0.005,\quad d=-0.004,
\]

with a choice between five- and nine-point Laplacians and between diffuse and complex-wave modes. Fields and gradients have a hard cap of \(10^6\). When a value becomes non-finite or approaches the cap, the safety logic may reset \(\psi\). This is a legitimate software safeguard, but it is not a physical mechanism that prevents a singularity.

The semantic divergence of backends is concrete:

- one numerical branch always performs diffusion regardless of the declared wave mode;
- another supports complex spectral step \(\hat\psi\mapsto e^{iD\Lambda\Delta t}\hat\psi\);
- one branch uses fixed damping `0.005` instead of configured dissipation;
- the spectral “isotropic” operator is rotationally symmetric in Fourier space but global in real space.

The linear complex spectral substep is unitary because it multiplies each mode by a phase. However, the entire evolution with reaction, binding, damping, caps and resets is not unitary.

### 3.6 What green tests mean

The selected set of 22 mathematical-operator, wave, contract, and whitepaper-consistency tests passed in 11.74 s. This supports software stability. Some test names, however, imply stronger physical conclusions than their assertions establish: “perfect isotropy” tests the spectral solver; “CFL sanity” checks caps; “mode coupling preservation” only increments \(\phi\); and “unitarity” permits a relative tolerance of 10%. A passing test therefore establishes compliance with an internal specification, not confirmation of a law of nature.

An additional targeted run in Lineum Dynamics passed 24 traceability, proof-consistency, claim-verification, and wave-metric-transfer tests in 25.13 s. It also emitted `ComplexWarning` three times: the orthogonality metric effectively computes

\[
\operatorname{abs}(\operatorname{float}\langle\psi_0|\psi_1\rangle)
=|\operatorname{Re}\langle\psi_0|\psi_1\rangle|
\]

instead of the correct one

\[
|\langle\psi_0|\psi_1\rangle|
=\sqrt{(\operatorname{Re}z)^2+(\operatorname{Im}z)^2}.
\]

A purely imaginary overlap could therefore be reported as zero. The affected orthogonality results should be recalculated after changing the order of operations: remove `float` and take the absolute value of the complex number. This audit does not correct that implementation; it limits the scope of the affected claim.

Lina EI's four targeted probes — active contract, canonical replay, closed energy reachability, and observation map information loss — completed 18 tests in 4.84 s. Tests confirm deterministic reproduction of stored negative results; they do not turn them into positive physical evidence.

### 3.7 Role of other repositories

This section does not move authority for the candidate theory outside Core. The other repositories are audited as **downstream applications and stress tests**: they can reveal an error, ambiguity, or missing contract in the main model, but an application-specific modification does not itself change the canonical equation.

Lineum Dynamics is primarily a company, integration, and monetization layer that consumes and copies parts of Core. Three audited copies of the validation module—one in Core and two in Dynamics—had the same SHA-256 hash, `09ffb1185948ee3b8b5c5ea345b4be9286b39a160a8d993b3664a94047cd95db`. The match supports product synchronization, but is not an independent replication: it also reproduces the same complex-number cast in the orthogonality metric. Physical comments or function names in this layer should therefore not override the Core research specification.

OEA is custom generative-imaging software inspired by Lineum themes; it is not a separate definition of Lineum physics. Its operational “Eq‑8 spatial expansion” can be reduced mathematically to this sequence:

1. create a zero-valued image and insert unit-valued points at regular intervals;
2. crop the input patch and scale it bilinearly by an iteration factor of \(i\);
3. in `WAVE` mode, perform \(F\leftarrow|F-H_i|\);
4. in `DIFFUSE` mode, execute \(F\leftarrow\tanh(F+G_{\sigma=1.5}*H_i)\);
5. normalize by the maximum and map scalar values to RGB channels.

These operations are legitimate texture-generation methods, but they do not define physical time, units, a Hamiltonian, a metric, gravitational coupling, or cosmological initial conditions. Moreover, the documented “zero vacuum state” contains unit-valued nodes from the first step. Qualitative resemblance to filaments is vulnerable to pattern overinterpretation; a physical claim would require at least power-spectrum, two- and three-point-correlation, cosmic-void, and topological comparisons against cosmological data and simple null models.

**[CALCULATED]** Ablation at \(192\times192\) points and 192 scales showed:

| Variant relative to `lattice_step5_diffuse` | relative \(L^2\) difference | fourfold spectral anisotropy | low-frequency power share | final/initial intensity sum |
|---|---:|---:|---:|---:|
| same reference run | 0 | 0.839723 | 0.956832 | 20.4101 |
| grid step 4 instead of 5 | \(2.63\times10^{-7}\) | 0.839723 | 0.956832 | 13.4738 |
| grid step 6 instead of 5 | \(1.59\times10^{-7}\) | 0.839723 | 0.956832 | 30.3162 |
| randomly shuffled scale order | 0.344893 | 0.682574 | 0.952842 | 13.6622 |
| mode `WAVE` instead of `DIFFUSE` | 0.780669 | 0.715730 | 0.933065 | 4.62161 |
| random seed with the same density | 0.272033 | 0.870145 | 0.928983 | 17.7856 |

In the selected `DIFFUSE` order, changing the lattice interval among 4, 5, and 6 was almost invisible in the final normalized image, although the total unnormalized intensity changed by more than a factor of two. By contrast, shuffling the same scales changed the image by 34.5%, and switching between the two manually defined aggregation modes changed it by 78.1%. The large fourfold anisotropy records the axial geometry. These results do not support treating morphology as a diagnostic of the “Planck seed” alone: scale ordering and image operators are at least as consequential. The intensity sum is not conserved and cannot be identified with energy or mass without a derived physical mapping.

Minimum future validation protocol for a cosmological interpretation of OEA:

1. before preregistering the test, define the conversion from pixels to comoving length and from intensity to density contrast \(\delta=(\rho-\bar\rho)/\bar\rho\);
2. use a Gaussian random field with the same power spectrum and standard \(\Lambda\)CDM simulation as a comparison model;
3. without further fitting, compare \(P(k)\), BAO two-point correlation peak, bispectrum, Minkowski functionals, filament skeleton and void size function;
4. perform blinded classification across multiple seeds rather than selecting the aesthetically strongest image;
5. reject the cosmological interpretation if OEA does not outperform a random field with the same spectrum, or if the result is unstable under changes in resolution, crop, or layer order.

Claiming that a 1,024-pixel canvas at “Phase 11” realizes the Bekenstein bound would be a category error unless physical scales are supplied. The [Bekenstein bound](https://doi.org/10.1103/PhysRevD.23.287) has the form

\[
S\le \frac{2\pi k_BRE}{\hbar c},\qquad
I_{\max}\le\frac{2\pi RE}{\hbar c\ln2},
\]

and the pixel count does not determine it without a physical radius \(R\) and energy \(E\). Likewise, `int256` does not enable infinite zoom; it represents at most \(2^{256}\) distinct bit patterns. Terms such as BAO, dark matter, gravity, 11 dimensions, and heat death therefore belong to OEA's inspirational vocabulary, not to its verified outputs.

Lina EI is a purpose-built application using candidate Lineum equations for a specific application goal. It contains useful deterministic-replay and falsification tests: the closed “energy epsilon” hypothesis was either unreachable or had no effect, and the topological observation signatures were not unique. These results stress-test the transfer of equations into an application; they do not constitute an independent physics program. Among \(3\times3\) grids, one observation signature was shared by topologically distinct states across 45 configurations; among \(4\times4\) grids, 21 such signatures occurred across 41,152 configurations. This demonstrates that the selected observation map does not uniquely preserve topology.

The particular \(3\times3\) witness on the periodic torus is

\[
A=\begin{pmatrix}0&1&1\\1&1&0\\1&0&0\end{pmatrix},\qquad
B=\begin{pmatrix}0&1&1\\0&1&1\\1&0&0\end{pmatrix}.
\]

Both states have five occupied cells, 12 periodic edges between distinct neighbors, and the same complete production observation vector, including mean amplitude \(5/9\), variance \(0.24691358\), relative gradient energy 2.4, and zero vortices. Nevertheless, \(A\) has one toroidally connected component and \(B\) has two. An analogous first witness for \(4\times4\) is

\[
C=\begin{pmatrix}1&0&1&1\\1&1&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix},\qquad
D=\begin{pmatrix}1&1&1&1\\0&0&0&0\\1&0&0&0\\0&0&0&0\end{pmatrix},
\]

again with five occupied cells and 12 distinct edges, but with one connected component versus two. The decision to “use global observations only as basic telemetry” is therefore supported by exhaustive enumeration rather than by a random sample.

The closed-energy check is also unambiguously negative: the public configuration does not support the \(\epsilon\) field, the output does not preserve it, and the recognized fields are bitwise identical with and without the \(\epsilon\) environment variable. Both runs had the same state SHA-256, `ad6bd956f348a663fe1a609904f88f12b88033c911c5371c321720dcd0eed552`, total diagnostic wave energy 4.9924679633, and maximum amplitude 0.1960578903. The stated thermodynamic-binding test therefore did not execute the intended mechanism; the exact closed-energy equation under test must first be recovered.

Lina EI's active extension and Core's canonical path are each independently bit-reproducible, but they are not declared numerically equivalent. In the audited replays, the extension solver produced diagnostic energy 0.7178229871 and the canonical solver 1.3851098432. This difference is another reason not to aggregate results from distinct solvers under one physical claim.

### 3.8 Named deterministic reference profiles and their boundary

Two stable names now prevent the time convention from being hidden inside one Boolean:

| Profile | Fixed identity | Purpose |
|---|---|---|
| `legacy-per-update-v1` | `phi_diffusion_scales_with_dt=False` | reproduce historical per-update behavior and preserve the unnamed default |
| `rd0-c1-deterministic-continuous-time-v1` | `phi_diffusion_scales_with_dt=True`; stochastic source off; diffusive \(\psi\); LAP4; mode coupling off; \(\mu\) off; PML off | refine a declared deterministic trajectory while changing \(h\) |

The continuous-time profile defaults to \(h=0.1\) but permits \(h\) and non-identity numerical coefficients to vary. Attempts to change a profile-defining value or use the ambiguous name `canonical` fail closed. The implementation contract contains 13 profile tests, two legacy characterization cases, four original time-refinement cases, and eight broader deterministic falsification cases: 27 passing cases in both the working state and a clean isolated tree.

The broader suite checks four Fourier modes, a corner impulse with periodic wrapping, nonuniform \(\kappa\), the analytic LAP4 stability boundary, and NumPy/PyTorch CPU parity. It therefore enforces the tested software meaning of the profile. It does not prove that the profile is the unique, final, or physically correct Lineum dynamics.

### 3.9 The historical zero-kappa test did not demonstrate chaos or true randomness

A permanent test previously claimed that two almost identical runs at \(\kappa=0\) amplified thermal floating-point noise into “True Randomness” at an “Edge of Chaos.” The implementation does not test that proposition.

The source audit gives four decisive facts:

1. the initial \(10^{-15}+10^{-15}i\) perturbation is placed at cell `[32,32]`, inside a region reset to exactly `1+0i` at step zero and every fifth step;
2. \(\kappa=0\) multiplies the stochastic source, interaction, diffusion, reaction, and field-flow transfer by zero in this branch;
3. the second run receives a new explicit \(j=10^{-5}+10^{-5}i\) injection at cell `[15,15]` on **every** one of 1,500 steps;
4. the remaining difference obeys deterministic damping with factor \(r=1-0.005=0.995\).

The exact scalar recurrence is therefore

\[
d_{n+1}=r(d_n+j),\qquad d_0=0,
\]

with solution

\[
|d_N|=|j|r\frac{1-r^N}{1-r}.
\]

At \(N=1500\), this predicts `0.0028127574610763545`. The historical test printed `0.0028127574077312194`, an absolute difference of `5.334513516683237e-11` and relative difference `1.8965423043058553e-08`. The apparent “amplification ratio” of `198.89198745601468` is simply the ratio of a damped 1,500-step geometric sum to one injection. A single one-time \(10^{-5}+10^{-5}i\) perturbation instead decays to `7.67602033217176e-09` after 1,500 steps.

The misleading contract was replaced by three characterization tests: exact replay of identical complete states, decay of a one-shot perturbation, and exact agreement of repeated forcing with the geometric sum. Together with the profile and RD-0 suites, 30 targeted cases pass.

**Verdict:** this test is negative evidence for its former interpretation, not negative evidence against all Lineum chaos hypotheses. A chaos claim still requires growth from a one-time infinitesimal perturbation without continued differential forcing, a positive finite-time Lyapunov estimate over a declared regime, convergence and saturation controls, and separation from stochastic branching and numerical instability.

---

## 4. Jan Fikáček's Published Argumentative Corpus and Its Relevance to Lineum

### 4.1 Definition of the corpus

The principal sources examined are the dissertation *Philosophy of Infinity* (2021), whose official record and full text are available at [Theses.cz](https://theses.cz/id/7965gy/), and the book *The End of Infinity* (2024, ISBN 978-80-7551-342-7). This review read the complete available dissertation text. It evaluates the book from its bibliographic record, publisher's synopsis, and available sample, and does not claim to have read the complete book. The supplementary corpus consists of the articles and public lectures listed below. The evaluation is limited to their arguments and physical implications.

### 4.2 Main thesis

The dissertation centers on an “empirical axiom” that actual infinity does not exist in the physical world. Fikáček distinguishes actual or completed infinity from a potentially unending process. He argues from the finitude of measurements and physical information carriers, interprets physical singularities as signs of theory failure, discusses a noetic horizon, and emphasizes the impossibility of empirically completing an infinite set of observations. He also treats reality and abstraction as layers of materially realized models and develops what he calls a “negative metaphysics.”

The following themes are particularly relevant for Lineum:

- the actual physical carrier of information is finite;
- an infinite value in a physics equation may signal that the domain of validity has been exceeded;
- discrete and continuous descriptions can emerge from each other;
- time can be related to irreversibility or "quantum friction";
- there could be a physical wave under the probability wave;
- particles may be condensed or localized manifestations of a deeper medium;
- the quantum state is supposed to exist objectively without a conscious observer.

### 4.3 Four logically distinct infinity theses

For a precise discussion, it is convenient to divide one general slogan into four statements of varying strength:

| Code | Claim | Evidential status | Consequence for Lineum |
|---|---|---|---|
| F1 | Every actual measurement and stored record contains a finite number of distinguishable outcomes. | strongly supported by operational practice | simulations and experiments must report finite precision |
| F2 | Physically observable quantities should be finite, and a divergence usually signals the boundary of a model's domain. | useful methodological rule, not a universal theorem | a singularity cannot be declared explained merely by bounding it; the completed dynamics must be derived |
| F3 | Neither actual infinity nor a continuum exists in the ontology of nature. | does not follow logically from F1 or F2 | requires an independent empirical signature of discreteness |
| F4 | Nature's foundation is a particular regular lattice governed by Lineum dynamics. | substantially stronger than F3 and not demonstrated | the topology, fields, update law, and physical scales must be derived |

The finite data \(D\) are typically compatible with both the continuous theory \(C\) and the sufficiently fine discrete theory \(L(a)\):

\[
P(D\mid C)\approx P(D\mid L(a))\qquad\text{for }a\ll\text{experimental resolution}.
\]

This is an instance of underdetermination: finite data can fit more than one ontology. The alternatives become distinguishable only if \(L(a)\) predicts a residual effect, or if it reproduces all observations with demonstrably lower descriptive complexity. F2 is therefore methodologically useful as a heuristic, while F3 and F4 must remain separate hypotheses.

The general proposition “actual infinity does not exist in physical reality” has no obvious finite falsification test: every instrument returns a finite record, while a candidate infinite domain can always be placed beyond a new observational horizon. An empirical program must therefore translate the proposition into a family of parameterized models—for example, \(a_*>0\), a finite local Hilbert-space dimension, or a maximum information density. Only their concrete consequences, such as dispersion, recurrence, entropy saturation, or symmetry breaking, can be measured and potentially refuted.

### 4.4 Constructive contributions of the argumentative program

The program usefully emphasizes the distinction between a mathematical object and a physical ontology. It is heuristically productive to ask whether a divergence diagnoses an incomplete model and whether finite microdynamics can reproduce an effectively continuous description. Its interdisciplinary synthesis also raises questions that narrower models may leave implicit. The effort to formulate fundamental physics without a conscious observer is likewise a legitimate research objective.

### 4.5 Areas requiring additional evidence or clarification

The most consequential logical gap is the transition

\[
\text{“finite measurement cannot confirm actual infinity”}
\quad\not\Rightarrow\quad
\text{“actual infinity does not exist.”}
\]

The first statement is an epistemic limitation; the second is an ontological conclusion. The implication requires an additional premise—for example, a verificationist principle that only finitely verifiable entities exist. Such a premise is philosophical and requires its own independent defense.

Other issues:

1. **Mathematical versus physical existence.** Standard axiomatic set theory treats actually infinite sets as formal objects. This does not imply that the universe contains infinitely many physical objects; conversely, physical finitude would not negate the consistency or utility of an infinite mathematical model.
2. **Scope of falsification.** The corpus also uses “falsification” for relations among axioms and geometries. Popper's criterion concerns the empirical falsifiability of general propositions; non-Euclidean geometry does not simply “disprove” Euclidean geometry, because each applies under different axioms.
3. **From metaphor to mechanism.** Terms such as “quantum friction,” a physical wave, or a particle condensate become physical explanations only when accompanied by dynamics, energy accounting, symmetry, and a measurable deviation from alternatives.
4. **Source and concept precision.** Several central steps rely on popularization sources where primary literature is available, and some mathematical or physical terms are used in specialized senses. Replacing those steps with primary citations and explicit definitions would make the argument easier to evaluate and reproduce.
5. **Quantum superposition.** An image involving “two cats” or doubled mass can conflate vector superposition of amplitudes in Hilbert space with classical simultaneous duplication of matter. Standard quantum theory does not imply that \(|A\rangle+|B\rangle\) automatically has twice the rest mass.
6. **Bell and signaling.** Bell tests rule out local factorizable latent variables under given assumptions; violation of the inequality alone does not allow superluminal transmission of usable information.

### 4.6 Publications and public corpus relevant to Lineum

In addition to the dissertation and the book, the following were identified in particular:

- *Experimental philosophy as an effective way to a revolution in physics* (ERGOT, 2017);
- chapter on quantum consciousness, medicine, psychology and biology in the collection *Psychosomatic Medicine 2020*;
- conference text *Reality as Natural Virtual Reality* (1997);
- article *Are all geniuses against infinity? What about Logic* (2026), which updates the mathematical argument of the book and dissertation;
- a popularization blog with more than three hundred texts; the author explicitly distinguishes this informal venue from his dissertation;
- lectures *Colorful world beyond infinity* (2024) and *New world beyond Schrödinger's cat and beyond infinity* (2025), as well as videos on reality simulation, relativity, black holes and quantum consciousness.

Complete automatic Czech transcripts were analyzed for the 2024 and 2025 lectures. Because automatic captions can mistranscribe technical terms, this review evaluates the structure of the arguments rather than isolated wording. The videos document publicly presented positions; they are not treated as peer-reviewed evidence.

#### 4.6.1 Formal check of the current argument about mathematical infinity

The 2026 text clarifies several steps relevant to Lineum: it distinguishes between actual and potential infinity, marks "completed infinity" as linguistically contradictory, interprets Galileo's assignment of natural numbers to their squares as a logical contradiction, and various paradoxes of set theory as evidence of the inconsistency of actual infinity. These steps must be separated.

1. **"Finished" does not mean "with the last element".** In axiomatic mathematics, \(\mathbb N\) is determined by the properties of the entire structure; it does not arise from the physical completion of an infinitely long computation. The statement \(\forall n\in\mathbb N: n+1\in\mathbb N\) does not postulate the largest number or the moment when the enumeration was done. The linguistic sense of tension is therefore not a formal dispute \(P\land\neg P\).
2. **Galileo's paradox is not a contradiction within the theory.** Let's mark \(\mathbb N_+=\{1,2,3,\ldots\}\). The representation \(f(n)=n^2\) is a bijection between \(\mathbb N_+\) and the set of positive squares \(Q\subsetneq\mathbb N_+\). At the same time, \(Q\) is a proper subset and has an asymptotic density of zero:

   \[
   |\{n^2\le N:n\in\mathbb N_+\}|=\lfloor\sqrt N\rfloor,
   \qquad
   \lim_{N\to\infty}\frac{\lfloor\sqrt N\rfloor}{N}=0.
   \]

"Equally many" here means equal cardinality defined by the existence of a bijection; "less" can mean self-inclusion or lower density. These are two different relations, not a proof of a proposition and its negation in the same sense.
3. **Paradoxes of naive set theory do not invalidate every set theory.** The Russell and Burali–Forti paradoxes show that unrestricted set formation is inconsistent. Axiomatic theories therefore restrict comprehension. The Banach–Tarski theorem, by contrast, follows from specific axioms, including the axiom of choice, and uses nonmeasurable sets; its counterintuitive character is not a formal inconsistency. Independence of the continuum hypothesis means that it can be neither proved nor disproved from a specified standard axiom system, not that both a proposition and its negation follow from the same axioms.
4. **A finite syntax can describe an infinite model.** Every human proof is a finite string of symbols, but it can quantify over a structure whose intended model is infinite. The finiteness of the notation does not imply the finiteness of the semantic domain. The opposite thesis is a possible finitist philosophical program, not a consequence of formal logic itself.

For Lineum, this clarification is constructive. Rejection of actual infinity can be developed as a finitist or constructive alternative, but is not established by shifting among cardinality, proper inclusion, and density as different meanings of “number.” The physical program still requires a parameterized finite theory with a differentiating prediction; a dispute about the interpretation of mathematical objects does not by itself select a lattice or dynamics.

### 4.7 Alignment matrix for Lineum

| Theme | Position in the reviewed Fikáček corpus | Current Lineum | Degree of alignment |
|---|---|---|---|
| Actual infinity in physics | rejected | finite step, but some formulations use an unbounded coordinate range | shared motivation; Lineum formulation requires clarification |
| Singularities | interpreted as boundaries of theory validity | cutoff or cap bounds numerical values | aligned objective, but no derived mechanism |
| Continuous and discrete descriptions | treated as mutually emergent | discrete microstep with a smooth field | useful heuristic alignment |
| Physical wave beneath quantum probability | proposed | real or complex field \(\psi\) | conceptual analogy; quantum predictions remain absent |
| Particles as condensates or excitations | proposed | localized structures are sought | direct conceptual alignment; current stability results are negative |
| Objective reality without consciousness | defended | autonomous dynamics is intended | aligned objective; measurement model remains absent |
| Information with a physical carrier | emphasized | fields receive an informational interpretation | partial alignment; does not imply information equals matter |
| Speed associated with quantum entanglement | described as superluminal in the reviewed corpus | local-neighbor or globally spectral updates | Bell correlations and signaling constraints remain unresolved |
| Time and irreversibility | “quantum friction” working hypothesis | current runtime is dissipative | conceptual similarity; dissipation alone does not derive time |

### 4.8 Pilot-wave ideas: three models that must remain distinct

The motif of a “physical wave beneath the probability wave” is natural for Lineum, but at least three inequivalent possibilities must be distinguished:

1. **Bohmian mechanics.** The standard wave function \(\Psi\) evolves by the Schrödinger equation, while the actual particle configuration \(Q=(\mathbf q_1,\ldots,\mathbf q_N)\) obeys the guidance equation

   \[
   \frac{d\mathbf q_k}{dt}
   =\frac{\hbar}{m_k}\operatorname{Im}
   \left.\frac{\nabla_k\Psi}{\Psi}\right|_{Q(t)}.
   \]

For \(N\) spinless particles, \(\Psi\) is generally a field in \(3N\)-dimensional configuration space, not an ordinary local wave in three-dimensional space. In the entangled state, therefore, the velocity of a single particle depends on the entire configuration. Bohm's theory is deterministic but explicitly nonlocal; at quantum equilibrium \(\rho(Q)=|\Psi(Q)|^2\) reproduces the statistics of standard quantum mechanics. This is not a local cellular automaton model and does not automatically solve the origin of Born's rule — it changes the ontology, not the experimental predictions of quantum theory.

2. **A local field in ordinary space.** Lineum currently resembles this variant more closely: one or more fields \(\psi(\mathbf x,t)\) on a 2D or 3D lattice. Such a model can naturally produce localized or solitonic excitations, but for two or more particles it must still explain what replaces configuration space and how tensor products, exchange statistics, Bell correlations, and no-signaling emerge together. The statement “everything is one wave” is not a substitute for that construction.

3. **The hydrodynamic analogy of walking droplets.** A macroscopic droplet on a vibrating liquid is guided by a memory wave that it excites. This demonstrates the existence of classical pilot-wave-like dynamics and can inspire mechanisms for localization or orbit quantization. It does not establish general equivalence with quantum mechanics. Andersen et al. showed that, in their two-slit arrangement, the droplet follows one path, the relevant quantum amplitude and phase relations are absent, and a source-term particle–wave model does not reproduce quantum statistics in general.

This creates a clear fork for Lineum. Either the theory accepts a configuration-space state and explains its ontology and nonlocality, or it remains with local fields in ordinary space and supplies a new mechanism that reproduces many-particle quantum structure. Hydrodynamic similarity can be a constructive heuristic, but not validating evidence. The decisive test is not visual interference of a single wave; it is at minimum the joint reproduction of Born-rule statistics, complementarity, contextuality, and a loophole-free Bell protocol.

---

## 5. Adversarial Questions and Lineum's Current Physical Answers

### 5.1 Motion, Zeno, and the “hidden return of infinity”

**Refined question.** If fundamental history is a finite sequence of states, is a particle position defined only at lattice sites, or as a functional of an extended field? Which observables are discrete, and how can a macroscopic trajectory be shown to be independent of the interpolation used for visualization?

Zeno's paradox is not a proof of the impossibility of motion in modern mathematics. Finite time can be represented by a convergent series; a detailed philosophical analysis is offered by the [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/archives/spr2024/entries/paradox-zeno/). However, this does not solve the ontological question of whether nature is continuous.

A mathematical limit also does not state that nature or a computer must “take infinitely many steps” sequentially. For example, \(\lim_{x\to a}f(x)=L\) is a static relation among quantified values:

\[
\forall\varepsilon>0\ \exists\delta>0:\quad
0<|x-a|<\delta\Rightarrow |f(x)-L|<\varepsilon.
\]

This definition uses a continuous mathematical structure, but does not describe a physical algorithm that counts through an infinite sequence. Constructive or finite exact formulations can produce a finite \(\delta\) for each specified experimental tolerance. Lineum therefore need not “smooth jumps by secretly adding infinity”; it must instead state whether continuous limits are only an effective predictive language or whether the field amplitudes themselves form a continuum.

There are three distinct scenarios on the grid:

1. point token jumps between cells — ontic movement is discrete;
2. amplitude is spread out and centroid \(x_c=\sum_i x_i|\psi_i|^2/\sum_i|\psi_i|^2\) varies by fractions of grid step — observable motion may be smoother than nodes;
3. interpolation creates a smooth image for the observer only — smoothness is representational, not fundamental.

**[CALCULATED]** A Lax–Wendroff discretization transporting a smooth periodic profile at CFL \(0.5\) produced the following relative errors for \(N=32,64,128,256,512\):

\[
0.0351041,\ 0.00906404,\ 0.00227938,\ 0.000570516,\ 0.000142665.
\]

Successive error ratios were \(3.8729,3.9765,3.9953,3.9990\), consistent with second-order convergence. Discrete microdynamics can therefore approximate smooth macroscopic motion arbitrarily well as the numerical grid is refined. A fixed ontic lattice, however, does not take the \(a\to0\) limit; the theory must show either that residual lattice effects lie below experimental bounds or that they produce a specific measurable signature.

**Verdict:** emergence can address part of the question, but current Lineum does not define particle position or provide a convergence test that distinguishes ontic motion from visual interpolation.

**Rejection criterion:** a dependence of velocity, dispersion, or phase on subcell position or lattice orientation that exceeds experimental bounds.

### 5.2 Particle size and energy divergence

For a normalized wave packet in continuous two-dimensional space, the gradient energy is

\[
E_\nabla=\frac{\hbar^2}{2m}\int |\nabla\psi|^2\,d^2x.
\]

For a Gaussian of width \(\sigma\), \(E_\nabla\propto1/\sigma^2\), so progressively tighter localization costs progressively more energy. On a lattice with spacing \(a\), the largest representable wavenumber is bounded by the Brillouin zone; the divergence is replaced by a finite maximum of order \(1/a^2\).

This argument is non-relativistic. When the required localization energy reaches the order of \(mc^2\), i.e. at a width around the reduced Compton length

\[
\bar\lambda_C=\frac{\hbar}{mc},
\]

single-particle Schrödinger theory ceases to be a complete description, and quantum field theory permits creation of additional particles and antiparticles. A “point particle” in the Standard Model is also not a classical sphere with density \(m\delta^3(x)\); it is an excitation of a quantum field, with local operators defined through distributional and renormalized structures. The sharper question is therefore not only “where is the divergence cut off?” but also “what is the state space above the one-particle regime, and does the proposed model reproduce quantum-field-theoretic phenomena?”

**[CALCULATED]** For a normalized 2D Gaussian and a five-point Laplacian, the dimensionless energy \(a^2E_\nabla\) at \(\sigma/a=0.05,0.1,0.2,0.4,0.7,1,2,4,8\) was

\[
4.0000,\ 4.0000,\ 3.98456,\ 2.45560,\ 0.90143,\ 0.470012,
0.123067,\ 0.031128,\ 0.0078049.
\]

The effective number of occupied cells \(N_{\rm eff}=1/\sum p_i^2\) for the same widths was approximately

\[
1,\ 1,\ 1.00003,\ 1.3899,\ 5.9696,\ 12.5638,\ 50.2655,
201.062,\ 804.248.
\]

The cutoff therefore removes the numerical divergence, but the energy merely saturates at a finite value during collapse. Nothing in that fact forces the packet to remain wider than one cell. A stable size requires an energy minimum, a conserved charge, topology, a repulsive nonlinearity, pressure, or another quantum constraint.

For fixed physical width \(\sigma=2\) and lattice spacings \(a=1,0.5,0.25\), the gradient energies were \(0.123067,0.124513,0.124878\), compared with the continuum value \(0.125\). The corresponding errors, \(1.546\%,0.3896\%,0.0976\%\), establish numerical convergence rather than a fundamental cutoff.

**Verdict:** current hard caps and resets are software protection, not physical stabilization.

**Rejection criterion:** the object survives only because of a cap, boundary, continuous noise, or active background, and collapses or disperses when that support is removed.

### 5.3 Information, energy and matter

At least four terms must be separated:

- Shannon probability distribution information;
- algorithmic complexity of the description;
- thermodynamic entropy of the physical carrier;
- energy and mass of a specific physical state.

For probabilities \(p_i\), define the entropy deficit relative to the uniform state as

\[
I=\log_2N-H_2(p)=D_{\rm KL}(p\|u).
\]

**[CALCULATED]** A uniform field with total norm \(Q=1\) and another with \(Q=100\) both have \(I=0\), yet have different energies if energy depends on the norm. On a 4,096-cell lattice, uniform and single-cell states with the same norm \(Q=1\) have \(I=0\) and \(I=12\) bits, respectively. A state supported uniformly on half the lattice has \(I=1\) bit. The norm therefore does not determine the information measure, and the information measure does not determine the norm.

[Landauer's principle](https://www.dna.caltech.edu/courses/cs191/paperscs191/landauer1961.pdf) gives the minimum heat of irreversible erasure of one bit

\[
E_{\rm bit}\ge k_BT\ln2.
\]

At \(T=300\,\mathrm K\), the minimum is \(2.87098\times10^{-21}\,\mathrm J\) per erased bit, with mass equivalent \(3.19439\times10^{-38}\,\mathrm{kg}\). For 1 GB, interpreted as \(8\times10^9\) bits, the minimum is \(2.29678\times10^{-11}\,\mathrm J\), with mass equivalent \(2.55552\times10^{-28}\,\mathrm{kg}\). Experimental support for the Landauer bound was provided, for example, by [Bérut et al.](https://www.nature.com/articles/nature10872).

This is the minimum thermodynamic cost of logically irreversible erasure in an environment at temperature \(T\), not the rest mass of an abstract file. A physical connection in Lineum would require a derived energy functional, for example

\[
E[\psi,\phi]=\sum_x\left(A|\nabla\psi|^2+V(\psi,\phi)+
k_BT\,p_x\ln\frac{p_x}{u_x}\right),
\]

and must predict inertia, gravitational coupling, and experimental energy change. The word "arrangement" alone is not enough.

**Verdict:** investigating the physics of information is well motivated; a universal identity between information and matter is not established.

### 5.4 Black holes and the singularity

Penrose's theorem does not simply state that “the interior contains a physical point of infinite density.” Under specified global and energy assumptions, it proves geodesic incompleteness. [Einstein Online](https://www.einstein-online.info/en/spotlight/singularities/) gives an accessible account of the distinction, and the original paper appears in [Physical Review Letters](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.14.57). General relativity thereby signals a boundary of the classical description.

For Schwarzschild geometry, the Kretschmann scalar is

\[
K=R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}
=\frac{48G^2M^2}{c^4r^6}.
\]

**[CALCULATED]** For \(M=M_\odot\), the Schwarzschild radius is \(r_s=2953.339\,\mathrm m\). The values of \(K\) at \(r_s\), 1 m, the proton scale \(10^{-15}\) m, and the Planck length are approximately

\[
1.57735\times10^{-13},\ 1.04667\times10^8,\ 1.04667\times10^{98},\
5.87149\times10^{216}\ \mathrm{m^{-4}}.
\]

The corresponding average densities when the solar mass is compressed to these radii are

\[
1.84285\times10^{19},\ 4.74712\times10^{29},\ 4.74712\times10^{74},\
1.12435\times10^{134}\ \mathrm{kg\,m^{-3}}.
\]

Replacing \(r^2\) with \(r^2+a^2\), for example

\[
K_a(r)=\frac{48G^2M^2}{c^4(r^2+a^2)^3},
\]

produces a finite \(K_a(0)\), but this is only a regulator. Without a metric that solves specified gravitational field equations and has a consistent source tensor, the existence of a horizon, regular core, or stable finite object is not established. Regular black-hole models exist, including the [Hayward model](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.96.031103), but their physical origin and energy conditions require separate analysis.

In addition, the non-singular model must preserve black hole thermodynamics. For a stationary black hole, the target relations derived in the classical works of [Bekenstein](https://doi.org/10.1103/PhysRevD.7.2333) and [Hawking](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-43/issue-3/Particle-creation-by-black-holes/cmp/1103899181.pdf) hold:

\[
\frac{S_{\rm BH}}{k_B}=\frac{A}{4\ell_{\rm Pl}^2},\qquad
T_H=\frac{\hbar c^3}{8\pi GMk_B}.
\]

For one solar mass, \(A=1.09607\times10^8\,\mathrm{m^2}\),

\[
\frac{S_{\rm BH}}{k_B}=1.04895\times10^{77},\qquad
I_{\rm BH}=\frac{S_{\rm BH}}{k_B\ln2}=1.51332\times10^{77}\ \text{bits},
\]

and \(T_H=6.17007\times10^{-8}\,\mathrm K\). If Lineum treats cells as finite information carriers, it must derive not only area scaling but also the \(1/4\) coefficient, the radiation spectrum, the generalized second law, and the fate of information during evaporation. Simply counting cells in a volume would instead yield volume scaling and would be insufficient.

**Verdict:** Lineum does not currently model a black hole; a cutoff alone replaces a divergence with a parametrically large finite number.

### 5.5 The grid: mathematical tool or reality?

A numerical lattice and ontic discreteness can produce identical value tables in a simulation. They become distinguishable only through a prediction that survives refinement of the numerical regulator while remaining tied to a fixed physical scale \(a_*\). Candidate signatures include modified dispersion, rotational or Lorentz-symmetry breaking, a maximum information density, or characteristic noise correlations.

The use of a numerical lattice does not demonstrate that physical space is a lattice. Lattice QCD introduces a regulator and seeks a continuum limit; different microscopic discretizations can belong to the same universality class. Lineum must therefore either:

- demonstrate regulator independence and present the lattice as a computational tool; or
- declare \(a_*\) as a physical parameter and derive an unambiguous measurable deviation.

**Verdict:** the current evidence does not establish an ontic interpretation of the lattice.

### 5.6 Time, causality and speed of information

Four notions must remain distinct:

1. **causal order \(n\):** which complete state precedes another;
2. **numerical step \(h\):** the resolution used to approximate an evolution parameter \(t\);
3. **internal clocks:** repeatable model processes such as phase rotation, propagation, damping, diffusion, or a localized excitation traversing a distance;
4. **time arrow:** irreversibility from damping, diffusion, coarse-graining, or stochastic branching.

Multiplying a deterministic rate by \(h\) addresses only the second item. It does not assert that \(t\) is a fundamental universal clock. Friction, permeability, and interaction with a medium can define rates and operational clocks relative to \(t\), but do not by themselves define causal ordering.

A finite-neighborhood local update can have an exact discrete light cone: after \(n\) steps, a cell depends only on nodes within distance \(nR\). The corresponding maximum physical speed would be \(v_{\max}=Ra/\Delta t\). This requires a synchronous update with no global operation.

Even an exact finite cone does not give special relativity by itself. A synchronous full-grid clock defines the preferred "all cells now" foliation, while Lorentz transformations mix space and time and alter simultaneity. The model must show that no low-energy experiment can detect this microscopic rest frame, or openly predict its measurable signature.

Current spectral branches do not have this property. **[CALCULATED]** Starting from a unit impulse on a \(64^2\) lattice, one update produced:

| Operator/evolution | number of non-zero cells | probability outside radius 1 | outside radius 2 | outside the quarter grid |
|---|---:|---:|---:|---:|
| explicit local Euler, LAP4 | 5 | 0 | 0 | 0 |
| exponential FFT, LAP4 | 141 above \(10^{-15}\) | \(3.11166\times10^{-5}\) | \(3.2864\times10^{-8}\) | numerically negligible |
| exponential FFT, LAP8 | 241 above \(10^{-15}\) | \(6.51265\times10^{-4}\) | \(3.1656\times10^{-6}\) | numerically negligible |
| spectral \(-k^2\) | all 4096 | \(3.82477\times10^{-3}\) | \(8.83557\times10^{-4}\) | \(5.8841\times10^{-6}\) |

A spectral update is a legitimate numerical PDE method, but it is not a strictly local cellular automaton. A nonzero tail alone does not demonstrate an operational superluminal signal; it does show that causality cannot be inferred from the statement “only neighbors interact” when the implementation applies a global FFT-based exponential.

The deterministic \(\phi\)-diffusion exposed a separate numerical-time defect. In the legacy branch,

\[
\Delta\phi_{\rm diff}=\kappa D_\phi\mathcal L_\kappa\phi
\]

is applied once per update, while the other declared rates are multiplied by \(h\). Over a fixed \(T\), halving \(h\) therefore doubles the number of unscaled diffusion applications. The opt-in continuous-time profile instead uses

\[
\Delta\phi_{\rm diff}=h\kappa D_\phi\mathcal L_\kappa\phi.
\]

For the coupled RD-0 fixture at fixed \(T=10\), pairwise \(\phi\) errors in the candidate shrink by factors `2.0020180135950105` and `2.000999833715611`, as expected for first-order Euler convergence. Broader tests reproduce the analytic Fourier-mode solution within `6.994405055138486e-15`, remain first-order for nonuniform \(\kappa\), and locate the predicted checkerboard stability boundary at \(h_{\max}=100\).

Stochastic time has a different scaling law. The present source is schematically

\[
\Delta\psi_n=h(aB_n+\sigma Z_n),
\qquad
\operatorname{Var}[\Delta\psi(T)]
=Th\left(a^2p(1-p)+\sigma^2\right).
\]

Its mean can remain finite while its standard deviation vanishes as \(\sqrt h\). A 1,024-member source/diffusion ensemble measured \(R(h)\propto h^q\) with `q=0.4883584910429441`; 16 independent blocks of 64 give a 95% interval `[0.4841855067201953, 0.49252687348968344]`. The result survives a packet initial field (`q=0.4908912808483476`), a \(16\times16\) grid (`q=0.49028328526425435`), and \(T=4\) (`q=0.4883346728799905`).

Three alternative controls retain finite spread under refinement: initial-only branching (`q=-0.0018375549150722406`), Gaussian \(\sqrt h\) forcing (`q=-0.010816373320071146`), and Poisson-rate events (`q=-0.009123887126903518`). They are physically inequivalent. Initial-only branching provides no renewed foam, Gaussian forcing does not define discrete births, and Poisson events require an uncalibrated rate and jump amplitude. Numerical consistency narrows the choice but does not select the ontology.

**Verdict:** Lineum now has a consistent numerical-time convention for one deterministic reference lane, but physical causality, internal proper time, conversion to seconds, relativity of simultaneity, and stochastic ontology have not been derived.

### 5.7 Measurement without a conscious observer

Decoherence explains suppression of interference terms in a reduced density matrix when a system couples to its environment. For a qubit,

\[
\rho(0)=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad
\rho(t)=\frac12\begin{pmatrix}1&e^{-\gamma t}\\e^{-\gamma t}&1\end{pmatrix}.
\]

**[CALCULATED]** For \(\gamma t=0,0.5,1,2,5\) absolute off-diagonal dropped from \(0.5\) to

\[
0.5,\ 0.303265,\ 0.183940,\ 0.067668,\ 0.003369,
\]

and purity \(\operatorname{Tr}\rho^2\) from 1 to

\[
1,\ 0.683940,\ 0.567668,\ 0.509158,\ 0.500023.
\]

Both diagonal probabilities remained \(1/2\). Decoherence therefore selects a stable basis and explains effective classicality, but does not by itself select one outcome in a single run. Reviews are provided by [Schlosshauer](https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.76.1267) and [Zurek](https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.75.715).

Lineum must explicitly choose an ontology:

- unitary evolution and branching;
- objective stochastic collapse, for example the [GRW family](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.34.470);
- relational/epistemic interpretation without physical collapse;
- hidden variables with their non-local structure.

Modern interferometry sets a stronger evidential burden than the historical two-slit demonstrations alone. Matter-wave interferometry with sodium nanoparticles has demonstrated quantum interference for objects containing more than 7,000 atoms and exceeding 170,000 Da. For objects near 172 kDa, measured visibilities were \(V=0.10\pm0.01\) and \(0.08\pm0.01\); the experiment compared classical and quantum models while varying phase-grating power. The superposed paths were separated by approximately 133 nm, and the paper reports macroscopicity \(\mu=15.5\). This does not settle the interpretation of measurement, but it makes superposition quantitatively testable. A Lineum alternative must reproduce the interference curve and its decoherence dependence, not only provide an intuitive narrative. See [Pedalino et al., Nature](https://www.nature.com/articles/s41586-025-09917-9).

**Verdict:** consciousness need not be postulated, but the current model does not include an alternative full measurement mechanism.

### 5.8 Lorentz invariance and directional anisotropy

For the plane wave \(e^{i(k_xx+k_yy)}\) the five-point Laplace operator has the symbol

\[
\Lambda_4(k_x,k_y)=2\cos k_x+2\cos k_y-4.
\]

With the same \(|\mathbf k|\), the value differs between the axis and the diagonal. A nine-point operator with weights of 1 for axial and 0.25 for diagonal neighbors has the symbol

\[
\Lambda_8=2(\cos k_x+\cos k_y)+\cos k_x\cos k_y-5.
\]

Its low-wavenumber term is \(-1.5|k|^2\), so without normalization it changes the effective diffusion or wave coefficient.

**[CALCULATED]** The relative axis–diagonal differences for a Schrödinger-type frequency \(\omega\propto-\Lambda\) and a wave phase velocity \(v_p\propto\sqrt{-\Lambda}/|k|\) are:

| \(|k|/\pi\) | LAP4: \(\Delta\omega/\bar\omega\) | LAP4: \(\Delta v/\bar v\) | LAP8: \(\Delta\omega/\bar\omega\) | LAP8: \(\Delta v/\bar v\) | spectral \(-k^2\) |
|---:|---:|---:|---:|---:|---:|
| 0.10 | 0.004117 | 0.002059 | 0.0000136 | 0.0000068 | 0 |
| 0.25 | 0.025901 | 0.012951 | 0.000535 | 0.000268 | 0 |
| 0.50 | 0.106032 | 0.053053 | 0.008889 | 0.004445 | 0 |
| 0.75 | 0.247948 | 0.124454 | 0.047688 | 0.023847 | \(\approx0\) |
| 0.90 | 0.368024 | 0.185597 | 0.103093 | 0.051581 | 0 |

The nine-point stencil significantly reduces but does not eliminate anisotropy, and without normalization has a phase speed of about \(\sqrt{1.5}\approx1.225\) relative to LAP4 at small \(k\). Normalization by the coefficient \(2/3\) restores the low-energy scale, not the exact Lorentz symmetry. The spectral \(-k^2\) is angularly isotropic on the periodic box, but the update is spatially global and time remains preferred.

Symbol analysis is complemented by direct wavefront evolution. A point pulse is not a suitable null control because it spans the square Brillouin zone, whose cutoff already carries fourfold geometry. The calculation therefore used a circularly band-limited initial state,

\[
\widehat\psi_0(\mathbf k)=
\exp\!\left[-\frac{(|\mathbf k|-k_0)^2}{2\sigma_k^2}\right]
\Theta(0.9\pi-|\mathbf k|),
\qquad \sigma_k=0.035\pi,
\]

on a \(512^2\) lattice. Each operator evolved it through a unitary linear step \(\widehat\psi(t)=e^{i\Lambda(\mathbf k)t}\widehat\psi_0\) to \(t=20\). The fourfold deformation of \(p=|\psi|^2/\sum|\psi|^2\) was measured by the complex moment

\[
C_4=\frac{\sum_{\mathbf x}r^2p(\mathbf x)e^{4i\theta}}{\sum_{\mathbf x}r^2p(\mathbf x)},
\qquad A_4=|C_4|.
\]

For an exactly circular distribution, \(A_4=0\); here, negative \(C_4\) indicates diagonal elongation. **[CALCULATED]** The result was:

| \(k_0/\pi\) | initial \(A_4\) | LAP4: \(C_4(t)\) | normalized LAP8: \(C_4(t)\) | spectral \(-k^2\): \(C_4(t)\) |
|---:|---:|---:|---:|---:|
| 0.10 | \(2.86886\times10^{-4}\) | \(-1.15094\times10^{-2}\) | \(-6.58623\times10^{-5}\) | \(+7.96978\times10^{-6}\) |
| 0.25 | \(7.18419\times10^{-4}\) | \(-8.10496\times10^{-2}\) | \(-2.17718\times10^{-3}\) | \(+1.29363\times10^{-9}\) |
| 0.50 | \(1.43684\times10^{-3}\) | \(-3.55247\times10^{-1}\) | \(-3.85797\times10^{-2}\) | \(-2.37212\times10^{-17}\) |

The spectral null control remained circular to numerical precision, whereas LAP4 produced a fourfold moment of 0.355 at \(k_0=0.5\pi\), and normalized LAP8 reduced it to approximately 0.0386 rather than zero. Under bandwidth changes \(\sigma_k/\pi=0.025,0.035,0.05\), the \(A_4\) ranges at \(k_0/\pi=0.25\) remained 0.0752–0.0883 for LAP4, 0.00193–0.00259 for LAP8, and \(6.30\times10^{-11}\)–\(5.77\times10^{-8}\) for the spectral control. The maximum absolute change in \(A_4\) between \(256^2\) and \(512^2\) was \(3.29\times10^{-7}\); the maximum probability beyond \(r>0.4N\) was \(1.66\times10^{-9}\); and the norm error was at most \(3.33\times10^{-16}\). The effect is therefore not explained by a periodic self-image, norm loss, or resolution artifact.

Discreteness need not imply a regular lattice. Causal-set theory uses Lorentz-invariant Poisson “sprinkling”; its tradeoffs include stochasticity and a characteristic form of nonlocality. See the [original proposal](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.59.521) and a [modern review](https://link.springer.com/article/10.1007/s41114-019-0023-1).

Experimental limits on Lorentz symmetry breaking are very tight; [Standard-Model Extension data tables](https://arxiv.org/abs/0801.0287), photon arrival time from [GRB 090510](https://www.nature.com/articles/nature08574), and high-energy limits [HAWC](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.124.131101) are relevant. The specific limit depends on the operator and the sector, it cannot be replaced by the general statement "the Planck scale is too small".

A recent sector-specific example is the analysis of the approximately 220 PeV neutrino candidate KM3-230213A, which gives \(\Lambda_2>5.0\times10^{19}\,\mathrm{GeV}\) at 90% confidence for a specified quadratic parameterization of Lorentz violation. This is a model-dependent bound in one sector, not a universal conversion into a lattice spacing. It nevertheless shows that Lineum must specify the particle species, operator order, and sign of the correction. See [Physical Review D 111, 123037 (2025)](https://journals.aps.org/prd/abstract/10.1103/6zzg-tv4s).

For the five-point stencil, the low-wave expansion can be written

\[
-\frac{\Lambda_4}{a^2}=k^2-\frac{a^2}{12}(k_x^4+k_y^4)+O(a^4k^6).
\]

The angular factor of the fourth order is

\[
\cos^4\theta+\sin^4\theta=\frac{3+\cos4\theta}{4},
\]

so the natural signature of a square lattice is a \(\cos4\theta\) harmonic and an order-\((ka)^2\) correction, not automatically a correction linear in energy. Fermi's observation of GRB 090510 gave a lower limit of \(1.2E_{\rm Pl}\) for a model with **linear** energy dependence, equivalent to an effective length below

\[
\frac{\ell_{\rm Pl}}{1.2}\approx1.35\times10^{-35}\,\mathrm m.
\]

This result constrains \(a_*\) only if Lineum derives a linear term with a coefficient of order unity. A symmetric central stencil usually has a leading even, quadratic correction, to which the corresponding quadratic bounds must be applied. Identifying \(a_*\) directly with the Planck length without deriving the coefficient would be unsupported.

**Verdict:** the regular current lattice fundamentally lacks Lorentz invariance. Emergence at small \(ka\) is possible, but must be quantitatively compared with experiments.

### 5.9 Bell's theorem, non-locality and local automaton

For Alice's settings \(a,a'\), Bob's settings \(b,b'\), and a local hidden variable \(\lambda\), with \(A,B\in\{-1,1\}\), the CHSH combination is

\[
S=E(a,b)+E(a,b')+E(a',b)-E(a',b'),\qquad |S|\le2.
\]

Every deterministic local strategy has exactly \(|S|=2\); mixtures will not exceed this limit. A quantum singlet for suitable angles gives \(2\sqrt2\approx2.828427\). The original argument is in [Bell's article](https://journals.aps.org/ppf/pdf/10.1103/PhysicsPhysiqueFizika.1.195); loophole-free experiments include [Hensen et al.](https://www.nature.com/articles/nature15759), [Shalm et al.](https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.115.250402) and [Giustina et al.](https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.115.250401).

**[CALCULATED]** One million Monte Carlo samples for each local-model setting gave

\[
E_{00}=-0.501610,\ E_{01}=-0.498866,\ E_{10}=-0.499904,\ E_{11}=0.499620,
\]

thus \(|S|\approx2.0000\). The quantum singlet simulation gave \(S=2.828836\), theoretically \(2.828427\), with a standard error of about \(0.001414\) and a maximum marginal bias of \(0.001128\).

The common statement “Bell physically requires nonlocality” is shorthand. Bell experiments rule out the conjunction of local factorization, measurement-setting independence, and the usual single-outcome assumptions; different interpretations revise different premises. A local quantum Hamiltonian can create an entangled state through a common past interaction, but a classical local automaton with ordinary probabilities cannot reproduce all Bell correlations. At the same time, no-signaling marginals can remain exactly local.

The result is not limited to photons or individual atoms. A loophole-free test using two superconducting circuits approximately 30 m apart analyzed more than one million runs and measured \(S=2.0747\pm0.0033\) with \(p<10^{-108}\); its timing closed the locality loophole, and the analysis included all outcomes. See [Storz et al., Nature 617 (2023)](https://www.nature.com/articles/s41586-023-05885-0). This is particularly relevant to any attempt to explain quantum correlations through a classical local medium.

**Verdict:** the current Lineum model has no construction of a composite quantum state or Bell experiment. If it remains a classical local automaton, reproducing quantum data requires abandoning at least one Bell assumption.

### 5.10 Grid origin and infinite regress

Every theory has primitive concepts. Postulating a causal network or algebraic state as fundamental does not automatically create an infinite regress, and standard theories do not derive every primitive from a “super-theory.” The problem arises only if Lineum claims to explain geometry through a lattice mechanism while assuming the fixed lattice geometry that needs explanation.

A good fundamental postulation must be:

- minimal;
- mathematically consistent;
- able to create known symmetries and laws;
- empirically more economical or predictably stronger than the competition.

The \(a\) and \(\Delta t\) values ​​can be fundamental constants, dynamic mean values ​​of the emergent network, or just simulation units. Each option leads to different tests. The current Lineum did not decide between them.

**Verdict:** regress is not a logical objection to every discrete theory. The substantive objection is a postulated lattice that adds no explanatory or predictive content.

---

## 6. Additional Questions a Reviewer Must Ask

### 6.1 A finite grid is not automatically a finite state space

If a grid has \(N\) cells, but each field takes on an arbitrary real number, the state space for two scalar fields is

\[
\mathcal S=\mathbb R^{2N},
\]

which is still uncountable. Discrete space and time do not by themselves remove a continuum of amplitudes. A computer's `float64` representation has finitely many bit patterns, but that is an implementation property; a physical theory must state whether amplitudes are physically quantized and which values represent distinct states.

If each of two arrays has exactly \(q\) states per cell, then

\[
|\mathcal S|=q^{2N},\qquad B=\log_2|\mathcal S|=2N\log_2q.
\]

For grid \(128\times128\) and the 16-bit value of each field is

\[
N=16\,384,\qquad B=524\,288\ \text{bits},\qquad
|\mathcal S|=2^{524\,288}.
\]

This space is finite, but finiteness has unavoidable dynamical consequences. By the pigeonhole principle, a deterministic map \(F:\mathcal S\to\mathcal S\) must revisit a state after at most \(|\mathcal S|+1\) states; the subsequent history is periodic. If \(F\) is bijective, every state lies on a cycle and there are no dissipative attractors. If it is not bijective, information is fundamentally lost and the update is irreversible. If genuine randomness is added, the theory must specify its physical source and probability law.

Thus, a trilemma arises:

1. **real amplitudes:** discrete geometry but infinite state space;
2. **finite reversible automaton:** exact recurrence and no fundamental dissipation;
3. **finite irreversible or stochastic automaton:** real loss of information or new random postulate.

Lineum must explicitly choose one branch and derive both thermodynamic and quantum consequences.

### 6.2 A unified law and clear provenance

Which exact equation is theory and which equations are historical experiments? Is the runtime mathematically equivalent to the published equation? Why do two backends with the same name do different physics?

**[CALCULATED]** For a unit-normalized initial field with \(D=0.05\), \(\Delta t=0.1\), and \(N=128\), the diffusive and unitary-wave laws gave:

| Number of steps | Diffusive norm | Unitary-wave norm | Relative \(L^2\) difference |
|---:|---:|---:|---:|
| 1 | 0.9988009 | 1.0000000 | 0.000624 |
| 100 | 0.8871055 | 1.0000000 | 0.060455 |
| 1000 | 0.3065662 | 1.0000000 | 0.461237 |

These are different theories, not interchangeable implementations.

### 6.3 Dimensional analysis and calibration

What are the dimensions of \(\psi,\phi,\alpha,\beta,\delta,\kappa\)? How many independent physical scales are there? Which observations fix \(a\), \(\Delta t\), the amplitude scale, and energy? Does any parameter-independent prediction remain after calibration?

Calibration degeneracy can be shown directly. If the simulation has a dimensionless frequency of \(\tilde f=0.1\) cycles per step, then

\[
f=\frac{\tilde f}{\Delta t},\qquad
E=hf,\qquad m=\frac{hf}{c^2}.
\]

| selected \(\Delta t\) | \(f\) | \(E\) | \(m\) | \(E\) in MeV |
|---:|---:|---:|---:|---:|
| \(10^{-21}\,\mathrm s\) | \(10^{20}\,\mathrm{Hz}\) | \(6.62607\times10^{-14}\,\mathrm J\) | \(7.37250\times10^{-31}\,\mathrm{kg}\) | 0.413567 |
| \(10^{-18}\,\mathrm s\) | \(10^{17}\,\mathrm{Hz}\) | \(6.62607\times10^{-17}\,\mathrm J\) | \(7.37250\times10^{-34}\,\mathrm{kg}\) | \(4.13567\times10^{-4}\) |
| \(10^{-15}\,\mathrm s\) | \(10^{14}\,\mathrm{Hz}\) | \(6.62607\times10^{-20}\,\mathrm J\) | \(7.37250\times10^{-37}\,\mathrm{kg}\) | \(4.13567\times10^{-7}\) |

Thus, the same simulation gets an arbitrarily different SI mass just by changing the reporting label. Calibration only becomes physics when one observed quantity fixes \(\Delta t\) and other, independent quantities are subsequently predicted without further readjustment.

### 6.4 Hamiltonian, unitarity and conserved quantities

Is there an action \(S\), Hamiltonian \(H\) or discrete variational principle? Which Noether symmetry produces energy, momentum, charge, and angular momentum? A dissipative reaction-diffusion system can be a good model of an open medium, but without additional structure it is not fundamental closed quantum dynamics.

### 6.5 Stability of particles and Derrick's theorem

In multiple spatial dimensions, static solitons made only from scalar fields often fail a scaling argument; the classical reference is [Derrick's theorem](https://doi.org/10.1063/1.1704233). Stability can arise from conserved charge, topology, higher derivatives, gauge fields, or time periodicity. [Q-balls](https://doi.org/10.1016/0550-3213%2885%2990286-X) are an example of nontopological, charge-stabilized solitons.

For static configuration and scaling \(\psi_\lambda(x)=\psi(\lambda x)\) the energy terms behave as

\[
T_2[\psi_\lambda]=\lambda^{2-d}T_2,\qquad
T_4[\psi_\lambda]=\lambda^{4-d}T_4,\qquad
V[\psi_\lambda]=\lambda^{-d}V.
\]

In \(d=2\), the ordinary gradient energy \(T_2\) is scale neutral, while the biharmonic term \(T_4\) grows as \(\lambda^2\) and the potential term scales as \(\lambda^{-2}\). Higher derivatives can therefore create competing scales and a finite characteristic size. This explains why the provisional term \(-\nu\nabla^4\psi\) is of research interest. Its presence alone does not establish stability: the signs, boundary conditions, and conserved constraints must be specified, and the second variation of the energy must be positive in the relevant directions.

Lineum must document for a localized object:

- existence and spectrum of linear perturbations;
- stable size without a cap;
- translation without Peierls–Nabarro pinning;
- elastic or well-defined inelastic scattering;
- relation of energy, momentum and speed;
- multidimensional stability and box independence.

### 6.6 Fermions, spin and doubling

How do spin \(1/2\), Fermi statistics, antisymmetry and chiral gauge coupling arise from real scalar fields? Local translation-invariant lattice fermions run into the [Nielsen–Ninomiya doubling problem](https://www.sciencedirect.com/science/article/pii/0370269381910261). It is not impossible to solve it, but the solution has a price: Wilson term, staggered fermions, domain walls or other change of symmetries.

### 6.7 Gauge symmetry and interactions

Are the electromagnetic, weak, and strong interactions emergent or fundamental? How do local \(U(1)\), \(SU(2)\), and \(SU(3)\) symmetries, Gauss's law, and gauge redundancy arise? Two scalar fields alone do not supply this structure.

### 6.8 The Born rule and composite systems

Why is the outcome probability \(|\psi|^2\) and not \(|\psi|^p\)? How are the two systems composed: the Cartesian product of classical configurations, or the tensor product of Hilbert spaces? Without a compositional rule, entanglement cannot even be precisely formulated.

### 6.9 Contextuality: objective reality does not mean predetermined values of all quantities

The Bell test is not the only condition for a realistic model. The Kochen–Specker theorem rules out the non-contextual assignment of pre-existing outcomes to all quantum observables while preserving their functional relations. A clear state-independent proof is given by the Peres–Mermin square of two qubits. In each row and column below, there are three operators that commute with each other:

| First operator | Second operator | Third operator | Row product |
|---|---|---|---:|
| \(X\otimes I\) | \(I\otimes X\) | \(X\otimes X\) | \(+I\) |
| \(I\otimes Y\) | \(Y\otimes I\) | \(Y\otimes Y\) | \(+I\) |
| \(X\otimes Y\) | \(Y\otimes X\) | \(Z\otimes Z\) | \(+I\) |
| column product | \(+I\) | \(+I\) | \(-I\) |

If every operator had a context-independent predetermined value \(v(A)\in\{-1,+1\}\), the product of all row products and the product of all column products would both equal the product of the squares of the nine values, namely \(+1\). Quantum operator identities instead require total row product \(+1\) and total column product \(-1\). The contradiction arises without selecting a quantum state and without spatially separated parties.

This does not rule out an objective or deterministic theory. It means that an outcome must depend on the complete compatible measurement context, unless the model abandons another assumption of the theorem. Lineum must therefore model not only “particles before measurement,” but also the apparatus state, the choice of jointly measured quantities, and the invariance of the resulting statistics across operationally equivalent implementations. A local automaton can be contextual; however, no Lineum protocol yet reproduces these operator relations.

### 6.10 Thermodynamics and the arrow of time

Is the fundamental update reversible? If not, where do information and energy go? If it is reversible, how do macroscopic entropy, a low-entropy initial condition, and the arrow of time arise? Adding damping to an equation assumes an arrow of time rather than explaining it.

### 6.11 Continuous limit, renormalization and universality

What dimensionless combinations of parameters remain with \(a\to0\)? Is there a critical point and correlation length \(\xi/a\to\infty\)? Which operators are relevant, irrelevant and forbidden by symmetry? If different microdynamics yield the same macrophysics, why is a particular grid ontically privileged?

### 6.12 Gravitation and the equivalence principle

How does the universal binding of all forms of energy to one geometry arise? How do test bodies move along geodesics, how is local Lorentz invariance restored, and what is the weak-field Newtonian limit? Visual clustering or field gradient is not equivalent to gravity.

### 6.13 A unique prediction and the Occam cost

How many free parameters are fitted? Which single preregistered prediction distinguishes Lineum from the Standard Model, general relativity, an ordinary reaction–diffusion equation, and a numerical artifact? A framework that accommodates every result by changing its update rule is not falsifiable as one theory.

### 6.14 What mathematics remains after rejecting actual infinity?

Physical finitism and mathematical finitism are not the same thing. It is consistent to claim that nature has a finite number of distinguishable states while using real analysis as an effective predictive language. However, a stronger program that rejects actual infinity even in mathematical semantics must specify a replacement for \(\mathbb R\), limits, function spaces, and probability measures.

The minimum operational requirement can be stated without resolving the metaphysical dispute. For each physical quantity \(O\), finite-precision input, and required tolerance \(\varepsilon\), there must be a finite algorithm that returns an interval

\[
O\in[L_\varepsilon,U_\varepsilon],
\qquad U_\varepsilon-L_\varepsilon\le\varepsilon,

\]

together with a correctness or error certificate and a finite upper bound on computational resources. If a fundamental minimum accuracy \(\varepsilon_*\) exists, the theory must also derive where its predictions measurably depart from a continuum model. Without \(\varepsilon_*\), requests for arbitrarily fine refinement reintroduce a potentially unbounded family of states; with \(\varepsilon_*>0\), the cutoff becomes testable.

Lineum must therefore choose whether to use ordinary continuous mathematics instrumentally, constructive or computational analysis, rational interval dynamics, finite state algebra, or some other well-defined system. Mere `float64` is not a philosophical solution: its rounding is an implementation property, and without error proofs it can create and destroy attractors.

---

## 7. New Working Hypotheses for Lineum

The following proposals are not conclusions. They are competing research programs with explicit rejection criteria.

### H0 — Effective open reaction–diffusion medium

**Hypothesis.** The current model describes an effective nonlinear pattern-forming medium rather than fundamental spacetime.

**Mechanism.** Preserve the existing two fields, specify one PDE precisely, and study its bifurcations, dispersion, and pattern formation.

**Strength.** This interpretation most closely matches the observed dissipative implementation and does not require treating nonunitary dynamics as quantum-unitary evolution.

**Tests.** Phase map, linear stability of homogeneous states, convergence, independence from solver, comparison with canonical reaction–diffusion models.

**Rejection criterion.** The behavior depends entirely on caps, resets, or backend defects, and no robust phenomenon remains after convergence and solver-independence checks.

### H1 — Fundamental regular grid

**Hypothesis.** There is a fixed physical spacing \(a_*\) and a preferred microscopic frame.

**Prediction.** Modified dispersion for example

\[
E^2=p^2c^2+m^2c^4+\eta_2p^2c^2(pa_*/\hbar)^2+
\eta_4p^2c^2(pa_*/\hbar)^4+\cdots
\]

and angular harmonics corresponding to lattice symmetry.

**Tests.** Derive \(\eta_i\) directly from the update rule and compare with photon arrival time, laboratory isotropy and particle limits.

**Rejection criterion.** The experimental upper bound on \(a_*\) makes the target mechanism impossible, or the model predicts excluded anisotropy.

### H2 — Lorentz-compatible random causal discreteness

**Hypothesis.** The foundation is not a regular lattice but a random, locally finite causal set.

**Mechanism.** Events are Poisson-distributed with respect to invariant four-volume, and causal partial order is the primary structure.

**Strength.** It selects no regular axis and is more compatible with the joint goal of discreteness and Lorentz invariance.

**Tradeoffs.** A fundamental rewrite of Lineum, stochasticity, and difficult reconstruction of locality, fields, and dimensionality.

**Rejection criterion.** No stable low-energy local limit can be derived, or the induced fluctuations exceed experimental bounds.

### H3 — Local unitary quantum automaton / quantum walk

**Hypothesis.** The fundamental state is quantum and complex-valued, and its update is exactly unitary and local:

\[
|\Psi_{n+1}\rangle=U|\Psi_n\rangle,\qquad
U=\prod_{\ell}U_\ell,
\]

where each \(U_\ell\) only affects disjoint local blocks in the given layer.

**Goal.** Derive the Dirac equation, finite propagation speed, tensor-product composition of systems, and Bell correlations without signaling in the long-wavelength limit.

**Tests.** Unitarity to a declared numerical tolerance, an exact causal cone, dispersion, fermion species, entanglement entropy, a CHSH protocol, and the Born rule.

**Rejection criterion.** A need for global normalization, reduction to classical hidden variables with \(|S|\le2\), uncontrolled fermion doubling, or irreducible Lorentz anisotropy.

### H4 — Particles as Q-balls or topological defects

**Hypothesis.** A stable object requires a complex field carrying conserved charge \(Q\), rather than reactive self-focusing alone. A schematic candidate is

\[
\mathcal L=|\partial_\mu\psi|^2-U(|\psi|)-g\phi|\psi|^2+
\frac12(\partial_\mu\phi)^2-V(\phi),
\]

\[
Q=i\int(\psi^*\dot\psi-\dot\psi^*\psi)\,d^dx.
\]

Q-ball stability requires an appropriate \(U(|\psi|)/|\psi|^2\) ratio and energy inequality against free quanta. An alternative is the topological charge of vacuum mapping.

**Tests.** Energy variation at a fixed \(Q\), perturbation spectrum, boost, collisions, long-term energy drift, \(a,L\) extrapolation.

**Rejection criterion.** The object has no energy minimum, radiates away, is lattice-pinned, or loses stability when the box boundary or cap is removed.

### H5 — Information contributes through free energy but is not identical to matter

**Hypothesis.** A physical distribution contributes a relative-entropy term to free energy, for example

\[
F[p]=E[p]-TS[p],\qquad
\Delta F\ge k_BT D_{\rm KL}(p\|p_{\rm eq}).
\]

Changing an information-bearing state can change the mass equivalent of a particular device through \(\Delta m=\Delta E/c^2\), but the relation depends on its Hamiltonian, process, and temperature.

**Tests.** Two physical realizations of the same bit pattern, reversible versus irreversible operations, calorimetry and energy balance.

**Rejection criterion.** The model assigns the same mass to abstractly identical information regardless of its physical carrier, or violates the second law.

### H6 — Nonsingular gravity from a derived effective stress–energy tensor

**Hypothesis.** A finite core arises dynamically, for example from an effective density

\[
\rho(r)=\frac{3M\ell^2}{4\pi(r^2+\ell^2)^{5/2}},
\qquad
m(r)=4\pi\int_0^r\rho(s)s^2ds,
\]

and the metric

\[
ds^2=-f(r)c^2dt^2+f(r)^{-1}dr^2+r^2d\Omega^2,
\quad f(r)=1-\frac{2Gm(r)}{c^2r}.
\]

The integral can be done exactly in this illustrative case:

\[
m(r)=M\frac{r^3}{(r^2+\ell^2)^{3/2}},
\qquad
f(r)=1-\frac{2GM}{c^2}\frac{r^2}{(r^2+\ell^2)^{3/2}}.
\]

The Schwarzschild term \(1-2GM/(c^2r)\) is recovered for \(r\gg\ell\). Near the center,

\[
f(r)=1-\frac{2GM}{c^2\ell^3}r^2+O(r^4),
\qquad
K(0)=\frac{96G^2M^2}{c^4\ell^6},
\]

so every \(\ell>0\) produces a finite de Sitter-like core rather than a numerical clip. A horizon, however, is not automatic. Introducing \(x=r/\ell\) and \(C=r_s/\ell=2GM/(c^2\ell)\), its zeros satisfy

\[
f(x)=1-C\frac{x^2}{(1+x^2)^{3/2}}.
\]

The function \(x^2/(1+x^2)^{3/2}\) has maximum \(2/(3\sqrt3)\) at \(x=\sqrt2\). Two horizons therefore exist only when

\[
C>\frac{3\sqrt3}{2},
\]

At the critical value they merge; below it, no horizon exists. The construction separates three distinct statements: “curvature is finite,” “a horizon exists,” and “the object is dynamically stable.”

This is only an illustration of the required procedure. The specific \(\rho\), its radial and tangential pressures, and the scale \(\ell\) must follow from a Lineum action rather than being selected by hand. The energy conditions and stability of the inner and outer horizons must also be tested.

**Tests.** Finiteness of all invariants, conservation of \(\nabla_\mu T^{\mu\nu}=0\), horizons, thermodynamics, stability of perturbations, weak field limits, and gravitational waves.

**Rejection criterion.** The construction requires manual violation of conservation, develops pathological instabilities, or conflicts with precision tests of relativity.

### H7 — Objective measurement without consciousness

**Variant A: unitary branching.** Not a physical collapse; Lineum must derive the decoherence basis and probabilities.

**Variant B: objective stochastic collapse.** Norm-preserving nonlinear noise is added schematically:

\[
d|\psi\rangle=\left[-\frac{i}{\hbar}Hdt+
\sqrt\lambda(A-\langle A\rangle)dW_t-
\frac\lambda2(A-\langle A\rangle)^2dt\right]|\psi\rangle.
\]

**Tests.** Interferometry of large objects, spontaneous heating, X-ray emissions, mass and space dependence.

**Rejection criterion.** The parameters required for macroscopic classicality are experimentally excluded, or the dynamics permits signaling.

### H8 — Operational finitism with certified error bounds

**Hypothesis.** The fundamental theory need not treat real numbers as ontic entities; every physical prediction is a finite interval with an algorithmically certified error.

**Mechanism.** The state is represented by a finite algebra or by intervals with an explicit refinement rule. For any tolerance above the fundamental threshold \(\varepsilon_*\), the calculation terminates after finite resources and returns a certified interval. A continuous PDE serves only as compact notation for this family of finite calculations.

**Strength.** This operationalizes finitude without a logical leap to a square lattice and distinguishes physical finitude from the instrumental usefulness of continuous mathematics.

**Tests.** Certify reproduction of free-wave dispersion, conservation laws, quantum probabilities, and thermodynamic balance; prove that intervals narrow monotonically; derive at least one parameter-independent deviation when the threshold \(\varepsilon_*\) is reached.

**Rejection criterion.** The calculation requires a hidden infinite-precision oracle, intervals expand uncontrollably during long evolution, the model cannot reach existing experimental precision, or no finite threshold has a measurable consequence.

### H9 — Quantum foam as an open hypothesis registry

**Research policy.** “Quantum foam” must not be encoded prematurely as one preferred random-number generator. The phrase can refer to physically different mechanisms, including no fundamental randomness at all. The following registry keeps those mechanisms alive while preventing an unfalsifiable mixture.

Each candidate must declare four things before entering production physics: **what fluctuates**, **whether randomness is fundamental or emergent**, **its time law**, and **an observable that distinguishes it from the other rows**.

| Candidate family | Minimal mathematical form | Distinguishing signature | Rejection condition |
|---|---|---|---|
| F0: current per-step classical source | \(\Delta\psi=h(aB+\sigma Z)\) | finite mean but ensemble spread \(R\propto h^{1/2}\) | reject as continuous physical forcing if the intended variance must survive \(h\to0\) |
| F1: initial branch selection | \(\psi(0)=\psi_0+\eta_0\), then deterministic evolution | seed-dependent branches persist, but no new conditional variance appears after conditioning on the state | reject if matched states continue to branch at later times |
| F2: Markov Gaussian field forcing | \(d\psi=F(\psi)dt+G(\psi)dW_t\) | continuous paths, approximately Gaussian short increments, variance proportional to elapsed time | reject if increments show robust jumps, long memory, or non-Gaussian event counts |
| F3: Poisson linon births | \(d\psi=Fdt+A\,dN_t\), \(N_t\) Poisson with rate \(\lambda\) | discrete jumps, exponential waiting times, mean and variance proportional to \(\lambda T\) | reject if waiting times, Fano factor, or jump-size statistics disagree after detector bias is controlled |
| F4: state-dependent or self-exciting events | \(dN_t\) has intensity \(\lambda[\psi,\phi,\kappa,\mathcal H_t]\) | clustering, refractory periods, or bursts correlated with local medium state and event history | reject if one state-independent rate explains conditional event statistics |
| F5: colored noise and medium memory | \(\tau d\eta=-\eta dt+\sigma dW_t\), \(d\psi=Fdt+G\eta dt\) | finite correlation time, colored spectrum, non-Markov behavior in \(\psi\) that becomes Markov after adding \(\eta\) | reject if correlation time tends to zero under refinement or no auxiliary state improves prediction |
| F6: deterministic chaos | \(\dot X=F(X)\) with no stochastic source | exact replay from a complete state; positive Lyapunov exponent; apparent randomness scales with initial uncertainty | reject if identical complete states branch under a deterministic backend or if no chaotic regime survives refinement |
| F7: threshold or topological avalanches | an event occurs when \(C[\psi,\phi,\kappa]\) crosses a stability threshold | burst-size and duration distributions, critical slowing, hysteresis, or discrete topology changes | reject if events persist without threshold proximity or statistics are explained by independent noise |
| F8: unresolved subgrid dynamics | resolved variables obey a generalized Langevin equation with memory kernel \(K(t-s)\) and orthogonal force | noise and memory change predictably with observation scale; finer resolved state reduces the residual | reject if refinement does not reduce or transform the inferred residual as projection theory predicts |
| F9: stochastic or changing causal geometry | fields remain local on a graph whose links, order, or cell volumes fluctuate | propagation correlations follow causal-graph distance rather than fixed Euclidean grid distance; statistical rotational/Lorentz behavior may emerge | reject if geometry changes are observationally redundant or create excluded preferred-frame signals |
| F10: quantum amplitude dynamics rather than classical noise | unitary or completely positive evolution of amplitudes on a composite state space, with probabilities derived at measurement | interference phases, entanglement, contextuality, Bell violation with no-signalling | reject if it cannot reproduce quantum composition and probabilities; classical moment matching is insufficient evidence |

These families are not mutually exclusive in nature, but they must be tested separately before any hybrid is introduced. A hybrid with unconstrained initial noise, Gaussian forcing, event births, memory, and changing geometry could fit almost any finite simulation and would therefore have little explanatory content.

**Discriminator sequence.** The smallest useful experiments are:

1. compare identical complete-state replays and finite-precision perturbations to separate fundamental branching from deterministic chaos;
2. measure short-time increment histograms, jump counts, waiting times, skewness, kurtosis, and Fano factor to separate Gaussian diffusion from event processes;
3. test conditional autocorrelation and the Chapman–Kolmogorov property to detect missing memory variables;
4. vary spatial and temporal observation scale to test whether apparent noise is unresolved deterministic dynamics;
5. condition event rates on \(|\psi|\), \(\nabla|\psi|\), \(\phi\), \(\kappa\), and recent events to test self-excitation or refractory behavior;
6. compare propagation by Euclidean and causal-graph distance if geometry itself becomes dynamic;
7. reserve interference, Born probabilities, Bell, contextuality, and no-signalling tests for F10, because no classical noise law is validated as quantum merely by looking irregular.

**Current evidence.** The time-refinement experiment rejects only F0 as a nonzero continuous-variance forcing law in the tested source/diffusion lane. It does not reject F0 as a discrete per-update automaton, and it does not choose among F1–F10. Initial-only, Gaussian, and Poisson controls establish numerical counterexamples showing that finite stochastic limits are possible; they are not evidence that those mechanisms exist physically. The historical zero-\(\kappa\) test also does not support F6: it repeatedly forces one run and exactly follows a damped geometric sum. F6 remains open for other regimes, but currently lacks a valid positive Lyapunov or one-shot perturbation-growth result.

**Next read-only gate.** Build a common observation protocol for F1–F8 and identify the smallest pair of simulations whose predicted signatures do not overlap within uncertainty. Do not modify the default runtime until at least one discriminator is demonstrated and its false-positive controls pass.

---

## 8. Decision Gates for Future Research

### Gate 0 — Define and freeze the theory under test

**Current status: partially completed as a software gate, not completed as a physics gate.** `RD-0` freezes one deterministic comparison lane, the named profiles make its time convention explicit, and the tested CPU backends agree there. Competing wave, stochastic, biharmonic, geometric, and ontological candidates remain unresolved; therefore there is still no single final physical law.

- one canonical equation and one reference implementation;
- exact type of each field and state space;
- a decision on whether continuous mathematics is instrumental or replaced by an exact finite or constructive formalism;
- no silent caps, resets or backend divergences;
- versioned parameters and units;
- each physics statement assigned to a specific equation and test.

**Output:** a minimal specification that can be falsified as one theory.

### Gate 1 — Numerical and dimensional integrity

**Current status: begun.** The deterministic \(\phi\)-diffusion candidate passes fixed-time refinement, analytic-mode, nonuniform-medium, stability, and CPU-backend controls. Spatial refinement, units, complete-system conservation, boundary policy, cap-free long runs, and stochastic convergence remain open.

- convergence in \(a,\Delta t,L\);
- stability analysis and a documented defect map;
- matching of at least two independent solvers in their common mode;
- dimensionless groups and separate calibration;
- results without hard cap or analytically controlled limiter.

### Gate 2 — Locality, unitarity, and the relativistic limit

- exact causal cone;
- dispersion relation in all directions;
- conservation of norm/energy according to the chosen type of theory;
- quantitative comparison with Lorentz limits;
- a clear decision between a preferred frame and emergent invariance.

### Gate 3 — Particle

- isolated stable object in open/large vacuum;
- energy, momentum, effective mass and dissipation;
- stability when changing resolution and box;
- interaction of two objects and conservation balance;
- a stability mechanism derived from an action or invariant.

### Gate 4 — Quantum structure

- system composition and entanglement;
- the Born rule;
- Bell/CHSH including choice of settings and margins;
- state-independent contextuality and dependence of the result on the physical measurement context;
- measurement model without consciousness;
- no-signalling and comparison with quantum tomography.

### Gate 5 — Gravity

- dynamic geometry or well-defined alternative gravity stage;
- equivalence principle and Newton's limit;
- Schwarzschild/Kerr limit in exterior;
- regular interior as solution, not clip;
- gravitational waves, cosmology and observational limits.

### Gate 6 — A unique prediction

- a preregistered parameter region;
- at least one quantitative prediction not fitted to the target observation;
- comparison with the strongest standard benchmark model;
- blind analysis or independent replication;
- publishing a negative result.

---

## 9. Final List of Verification Questions

The following list supersedes the original proposal. Each question should have a numerical metric, a tolerance, and a predetermined pass/fail result.

1. Which single equation and which discrete update define the current Lineum theory?
2. Are all computational implementations convergent approximations of the same law, or are they different models?
3. What are the physical dimensions of the fields and parameters, and what data independently fix \(a,\Delta t\) and the energy scale?
4. Which quantities are exactly conserved and from which symmetries do they follow?
5. Is the fundamental update reversible, unitary, stochastic, or dissipative?
6. Does a local perturbation after one step have exactly zero response outside the finite neighborhood?
7. What is the maximum propagation speed, and how is it mapped to \(c\)?
8. What is the total dispersion relation throughout the Brillouin zone and its angular anisotropy?
9. Does the inferred anisotropy satisfy the particular experimental Lorentz-invariance bounds without an additional fit?
10. Is macroscopic smooth motion a property of observable fields or just an interpolation visualization?
11. Is there a stable localized object without cap, reset, noise, active background and periodic image of itself?
12. What invariant or energy minimum prevents the collapse of an object into a single cell or its dissolution?
13. Do the size, energy and frequency of the object converge at \(a\to0\), \(\Delta t\to0\), \(L\to\infty\)?
14. Does the object move in any direction without grid pinning and direction-dependent mass?
15. What is its relationship \(E(p)\), rest mass, momentum, and dispersion law?
16. How does spin \(1/2\), Fermi statistics and chiral fermion arise without pathological doubling?
17. How do gauge symmetries and gauge couplings arise?
18. How are two systems composed and where is the state space of entanglement?
19. Why does the model give Born's \(|\psi|^2\) and how does it exclude other exponents?
20. Does the predefined Bell protocol reproduce \(S>2\) and at the same time zero signaling margins?
21. Which Bell assumption does the model abandon and what other measurable consequences does it have?
22. What physically constitutes a "measurement result" and why is there only one in one run?
23. Is decoherence only effective, or does the model contain objective collapse; what are its parameters and experimental limits?
24. How is the information rate converted to the energy of a particular carrier and why should it create inertia?
25. Does the same abstract information in different carriers give the same mass? If so, how is the energy balance maintained?
26. Is the physical lattice empirically distinguishable from the numerical regulator?
27. Why is a regular square grid chosen instead of triangulation, random causal set, or gridless dynamics?
28. How do 3+1 dimensions, topology, and dynamical geometry arise from the current 2D periodic box?
29. How is the equivalence principle and universal gravitational coupling formulated?
30. Is a nonsingular black hole a solution of derived equations with \(\nabla_\mu T^{\mu\nu}=0\), or merely a cutoff?
31. Does the exterior reproduce Schwarzschild/Kerr geometry and observed gravitational waves?
32. How does the thermodynamic arrow of time arise without embedded damping and special initial conditions?
33. Which results are invariant to changing the numerical solver and microscopic stencil?
34. What is the universality class of the model and which lattice details are physically relevant?
35. Which single quantitative, preregistered, and as-yet-unmeasured prediction distinguishes Lineum from standard physics?
36. Which result would the team accept as a definitive refutation of each main hypothesis?
37. Are the field amplitudes physically continuous, or do they have a finite alphabet; what experiment will distinguish these possibilities?
38. If the entire state space is finite and the update is deterministic, what are the recurrences and why do they not contradict the required thermodynamics?
39. If the update is irreversible or fundamentally random, where does the information go or where does the probability law come from?
40. Does the model reproduce the state-independent Peres–Mermin contextuality, and on which physical state of the apparatus does the outcome of one observable depend?
41. If the "pilot wave" is a field in ordinary space, how exactly does it encode a general \(N\)-particle entangled state; if a field is in configuration space, what ontological meaning and kind of non-locality does Lineum assign to it?
42. What exact finitistic, constructive, or interval formalism replaces the real numbers and limits, how does it certify the \(\varepsilon\) error, and what measurable deviation does it predict for the \(\varepsilon_*\) fundamental threshold?

---

## 10. Limitations and Risks of Misinterpretation

1. **This is not an experimental validation of Lineum.** The calculations test mathematical implications of the stencils, information–mass claims, Bell locality, decoherence, and cutoffs. There is not yet one unique Lineum theory whose complete predictions can be confronted with data.
2. **The audit is a snapshot.** Several repositories contained pre-existing uncommitted changes. The recorded revisions and cutoff date make it possible to determine later which conclusions have been superseded by new implementation evidence.
3. **A periodic 2D box is not a universe.** Stability in a periodic 2D environment cannot be extrapolated to an isolated object in 3+1 dimensions without a derivation.
4. **Spectral numerics and physical nonlocality are not identical.** A global FFT step refutes a claim that the runtime update is strictly finite-neighbor local; it does not by itself demonstrate superluminal signaling in an effective theory.
5. **Bell's Monte Carlo test is a demonstration control.** Decisive evidence is provided by the analytical CHSH limit and laboratory experiments, not the pseudorandom sample generated here.
6. **The black hole calculation is not numerical relativity.** It only shows the growth of the classical invariant and an arbitrary cutoff. It does not solve Einstein's equations or dynamical collapse.
7. **Automatic video transcripts contain errors.** The review therefore uses videos to identify the direction and structure of arguments, not to attribute isolated wording. The full dissertation was available; the complete text of *The End of Infinity* was not.
8. **Absence of evidence is not evidence of absence.** When the audit did not find an implementation or derivation, the conclusion is "not documented in the audited corpus", not "does not exist anywhere".
9. **Model-dependent experimental limits are not universal.** Lorentz, collapse, and gravitational limits can only be used after mapping a specific Lineum operator to experimental analysis parameters.
10. **No external independent replication was performed.** Replication here means repeated execution in two software environments with all code and outputs published in this document. Independent reproduction by another team is still required.
11. **The new time controls are deliberately narrow.** Deterministic results cover the RD-0 lane; stochastic comparisons isolate \(\psi\)-source, damping, and diffusion. They do not establish long-lived linon identity, collisions, quantum statistics, or a full-system continuum limit.
12. **The zero-kappa result is a claim audit, not a complete chaos survey.** It proves why one historical threshold test passed and why that pass did not measure chaos. It does not calculate Lyapunov spectra across every nonlinear, pumped, bounded, wave, or mode-coupled Lineum regime.

## 11. Final Assessment

Lineum has credible research potential if it maintains the distinction between an idea and its proof: ontological intuition can motivate a program, but does not confirm it. The project has now moved beyond a purely narrative starting point by establishing a reproducible deterministic reference lane, identifying and repairing one opt-in time-step inconsistency, and distinguishing four stochastic time contracts. Its strongest assets are still not a ready-made “theory of everything,” but an open simulation laboratory, a willingness to preserve negative results, and an improving ability to formulate sharp tests of finite microdynamics.

For future work, Lineum Core should remain the sole repository in which canonical candidate physics is accepted and versioned. Dynamics is primarily the company and product-integration layer, OEA is custom generative-imaging software, and Lina EI is a purpose-built application of candidate equations. Their results can falsify a claim, reveal a constraint, or expose a missing Core contract; they cannot redefine the candidate theory without an explicit change to the Core research specification.

The reviewed Fikáček corpus is relevant to this program where it raises foundational questions: what infinity could mean physically, when a singularity signals model failure, how abstraction relates to a physical carrier, and whether probabilistic formalism is the final ontological layer. For Lineum, this suggests a methodological safeguard: broad synthesis should be paired with precise definitions, primary sources, derivations, and experimental falsification tests.

The most accurate current wording is therefore:

> **Lineum is a candidate research framework with one validated deterministic software-reference lane for investigating emergence from finite dynamics. It is not yet a verified model of particles, quantum measurement, relativity or gravity.**

This conclusion is not a loss. It is an accurate starting point from which to build a credible future whitepaper.

---

## 12. Bibliography and Source Corpus

### Published corpus by Jan Fikáček

1. Fikáček, J. *Filosofie nekonečna* [*Philosophy of Infinity*]. Doctoral dissertation, Palacký University Olomouc, 2021. [Record and full text](https://theses.cz/id/7965gy/).
2. Fikáček, J. *Konec nekonečna* [*The End of Infinity*]. Jonathan Livingston, 2024, ISBN 978-80-7551-342-7. [Bibliographic record and synopsis](https://www.kosmas.cz/knihy/540757/konec-nekonecna/).
3. Fikáček, J. *Experimentální filosofie jako efektivní cesta k revoluci ve fyzice* [*Experimental Philosophy as an Effective Path to a Revolution in Physics*]. ERGOT, 2017. [Article](https://ergotsite.wordpress.com/2017/09/03/experimentalni-filosofie-jako-efektivni-cesta-k-revoluci-ve-fyzice/).
4. Fikáček, J. *Skutečnost jako přirozená virtuální realita* [*Reality as Natural Virtual Reality*]. Conference paper, 1997; later [author's summary](https://blog.idnes.cz/fikacek/co-je-skutecnost-velmi-proste-za-par-minut.Bg21110976?setver=full).
5. Fikáček, J. *Nový svět za Schrödingerovou kočkou a za nekonečnem* [*A New World Beyond Schrödinger's Cat and Beyond Infinity*]. Public lecture, 2025. [Video](https://www.youtube.com/watch?v=XmX2tDur7Lo).
6. Fikáček, J. *Barvitý svět za nekonečnem* [*A Colorful World Beyond Infinity*]. Public lecture, 2024. [Video](https://www.youtube.com/watch?v=fGQLnDDNTCU).

### Physics, mathematics, and philosophy

7. Bell, J. S. *On the Einstein Podolsky Rosen Paradox*. Physics Physique Fizika 1, 195–200 (1964). [Original article](https://journals.aps.org/ppf/pdf/10.1103/PhysicsPhysiqueFizika.1.195).
8. Hensen, B. et al. *Loophole-free Bell inequality violation using electron spins separated by 1.3 kilometres*. Nature 526, 682–686 (2015). [Article](https://www.nature.com/articles/nature15759).
9. Shalm, L. K. et al. *Strong Loophole-Free Test of Local Realism*. PRL 115, 250402 (2015). [Article](https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.115.250402).
10. Giustina, M. et al. *Significant-Loophole-Free Test of Bell’s Theorem with Entangled Photons*. PRL 115, 250401 (2015). [Article](https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.115.250401).
11. Bombelli, L. et al. *Space-Time as a Causal Set*. PRL 59, 521 (1987). [Article](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.59.521).
12. Surya, S. *The causal set approach to quantum gravity*. Living Reviews in Relativity 22, 5 (2019). [Review](https://link.springer.com/article/10.1007/s41114-019-0023-1).
13. Abdo, A. A. et al. *A limit on the variation of the speed of light arising from quantum gravity effects*. Nature 462, 331–334 (2009). [Article](https://www.nature.com/articles/nature08574).
14. Albert, A. et al. *Constraints on Lorentz Invariance Violation from HAWC Observations of Gamma Rays above 100 TeV*. PRL 124, 131101 (2020). [Article](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.124.131101).
15. Kostelecký, V. A.; Russell, N. *Data Tables for Lorentz and CPT Violation*. [Continuously updated tables](https://arxiv.org/abs/0801.0287).
16. Landauer, R. *Irreversibility and Heat Generation in the Computing Process*. IBM J. Res. Dev. 5, 183–191 (1961). [Full text](https://www.dna.caltech.edu/courses/cs191/paperscs191/landauer1961.pdf).
17. Bérut, A. et al. *Experimental verification of Landauer’s principle linking information and thermodynamics*. Nature 483, 187–189 (2012). [Article](https://www.nature.com/articles/nature10872).
18. Penrose, R. *Gravitational Collapse and Space-Time Singularities*. PRL 14, 57 (1965). [Article](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.14.57).
19. Hayward, S. A. *Formation and Evaporation of Nonsingular Black Holes*. PRL 96, 031103 (2006). [Article](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.96.031103).
20. Schlosshauer, M. *Decoherence, the measurement problem, and interpretations of quantum mechanics*. RMP 76, 1267 (2005). [Article](https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.76.1267).
21. Zurek, W. H. *Decoherence, einselection, and the quantum origins of the classical*. RMP 75, 715 (2003). [Article](https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.75.715).
22. Ghirardi, G. C.; Rimini, A.; Weber, T. *Unified dynamics for microscopic and macroscopic systems*. PRD 34, 470 (1986). [Article](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.34.470).
23. Derrick, G. H. *Comments on Nonlinear Wave Equations as Models for Elementary Particles*. J. Math. Phys. 5, 1252 (1964). [DOI](https://doi.org/10.1063/1.1704233).
24. Coleman, S. *Q-balls*. Nuclear Physics B 262, 263–283 (1985). [DOI](https://doi.org/10.1016/0550-3213%2885%2990286-X).
25. Friedberg, R.; Lee, T. D.; Sirlin, A. *A Class of Scalar-Field Soliton Solutions in Three Space Dimensions*. PRD 13, 2739 (1976). [Article](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.13.2739).
26. Nielsen, H. B.; Ninomiya, M. *Absence of neutrinos on a lattice*. Nuclear Physics B 185, 20–40 (1981). [Article](https://www.sciencedirect.com/science/article/pii/0370269381910261).
27. Stanford Encyclopedia of Philosophy. *Zeno’s Paradoxes*. [Entry](https://plato.stanford.edu/archives/spr2024/entries/paradox-zeno/).
28. Stanford Encyclopedia of Philosophy. *Infinity*. [Entry](https://plato.stanford.edu/entries/infinity/index.html).
29. Stanford Encyclopedia of Philosophy. *Set Theory*. [Entry](https://plato.stanford.edu/entries/set-theory/index.html).
30. Pedalino, S. et al. *Probing quantum mechanics with nanoparticle matter-wave interferometry*. Nature 649, 866–870 (2026). [Article](https://www.nature.com/articles/s41586-025-09917-9).
31. KM3NeT Collaboration et al. *Constraints on Lorentz-invariance violation in the neutrino sector from the ultrahigh-energy event KM3-230213A*. PRD 111, 123037 (2025). [Article](https://journals.aps.org/prd/abstract/10.1103/6zzg-tv4s).
32. Storz, S. et al. *Loophole-free Bell inequality violation with superconducting circuits*. Nature 617, 265–270 (2023). [Article](https://www.nature.com/articles/s41586-023-05885-0).
33. Bekenstein, J. D. *Black Holes and Entropy*. PRD 7, 2333–2346 (1973). [Article](https://doi.org/10.1103/PhysRevD.7.2333).
34. Hawking, S. W. *Particle Creation by Black Holes*. Communications in Mathematical Physics 43, 199–220 (1975). [Article](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-43/issue-3/Particle-creation-by-black-holes/cmp/1103899181.pdf).
35. Bekenstein, J. D. *Universal upper bound on the entropy-to-energy ratio for bounded systems*. PRD 23, 287–298 (1981). [Article](https://doi.org/10.1103/PhysRevD.23.287).
36. Bohm, D. *A Suggested Interpretation of the Quantum Theory in Terms of “Hidden” Variables. I*. Physical Review 85, 166–179 (1952). [Article](https://journals.aps.org/pr/abstract/10.1103/PhysRev.85.166).
37. Bohm, D. *A Suggested Interpretation of the Quantum Theory in Terms of “Hidden” Variables. II*. Physical Review 85, 180–193 (1952). [Article](https://journals.aps.org/pr/abstract/10.1103/PhysRev.85.180).
38. Andersen, A. et al. *Double-slit experiment with single wave-driven particles and its relation to quantum mechanics*. Physical Review E 92, 013006 (2015). [Record and abstract](https://pubmed.ncbi.nlm.nih.gov/26274269/).
39. Mermin, N. D. *Simple Unified Form for the Major No-Hidden-Variables Theorems*. Physical Review Letters 65, 3373–3376 (1990). [Article](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.65.3373).
40. Kochen, S.; Specker, E. P. *The Problem of Hidden Variables in Quantum Mechanics*. Journal of Mathematics and Mechanics 17, 59–87 (1967). [Full text](https://doi.org/10.1512/iumj.1968.17.17004).

### Current supplement to the published corpus

41. Fikáček, J. *Jsou všichni géniové proti nekonečnu? A co na to logika* [*Are All Geniuses Against Infinity? What Does Logic Say?*]. Mensa 33(3), 14–16 (2026). [Mensa Czech Republic magazine](https://magazin.mensa.cz/wp-content/uploads/mensa_cz154_casopis_03-2026.pdf).

---

## Appendix A — Reproduction Log and Control Outputs

### A.1 Environment

- audit environment: Python 3.11.15 and NumPy 1.26.4
- replay environment: Python 3.12.13 and NumPy 2.3.5
- deterministic seed `20260715`
- three general-physics checks use only NumPy and the standard library; the OEA ablation additionally uses SciPy 1.17.1 to reproduce the imaging operations accurately
- all seven programs were executed against their embedded JSON in the audit environment; with the frozen versions, they reproduced exactly the same structure and values
- in the newer Python/NumPy environment, the three programs that do not require SciPy passed semantic comparison with \(\mathrm{rtol}=10^{-11}\) and \(\mathrm{atol}=10^{-13}\); differences were limited to runtime metadata and final floating-point bits
- the OEA program was not replayed in the second environment because SciPy was not installed there; its full reproduction therefore applies to the stated audit environment with SciPy 1.17.1
- the automatic document audit passed: 7/7 executable Python/JSON pairs, 42 contiguous adversarial questions, 41 contiguous bibliographic entries, balanced code fences, and no local-file references

### A.2 Control principles

1. Each number in the main tables is either directly printed by the program or derived algebraically from the displayed equation.
2. Axial and diagonal modes are compared with the same \(|\mathbf k|\).
3. Localization test always renormalizes \(\sum|\psi|^2=1\).
4. The Bell test uses a common hidden variable for all settings and a quantum singlet generator separately.
5. The black-hole test is a diagnostic of classical Schwarzschild divergence and toy regularization, not a simulation of Lineum gravity.
6. The backend test only isolates the difference between diffuse and unitary linear steps.

### A.2.1 Controls, ablations, sensitivity checks, and limits of interpretation

| Experiment | Primary metric | Check | Ablation / Sensitivity | What the result does not prove |
|---|---|---|---|---|
| Dispersion and anisotropy | axis–diagonal difference at fixed \(|k|\) | spectral \(-k^2\) with zero angular error | LAP4 vs. LAP8 vs. normalized LAP8; five values of \(|k|/\pi\) | that the spectral solver is local or Lorentz invariant in time |
| Band-limited wavefront | \(C_4\) and \(A_4=|C_4|\) | circular spectrum with spectral \(-k^2\) | three \(k_0\), three bandwidths, \(N=256/512\), boundary and norm controls | complete spacetime Lorentz invariance or physical validity of spectral nonlocality |
| One-step support | probability outside a stated radius | explicit Euler LAP4 with exact five-cell support | three Laplace symbols; radii 1, 2, and one quarter of the box | that any nonzero tail permits a usable signal |
| Localization | gradient energy and \(N_{\rm eff}\) | continuum value for the Gaussian | nine \(\sigma/a\) values and three \(a\) values at fixed \(\sigma\) | dynamical existence or stability of a particle |
| Information–energy | \(I=D_{\rm KL}(p\|u)\) compared with norm \(Q\) | same information with different \(Q\); same \(Q\) with different information | uniform, half-support, and single-cell states | that no specific information–energy relation can exist |
| Bell/CHSH | \(S\) and marginal bias | exact deterministic bound \(|S|=2\) | local and quantum generators; \(10^6\) samples per setting | a choice among all interpretations of quantum theory |
| Peres–Mermin square | the product of six compatible contexts | direct multiplication of the Pauli matrices | three rows against three columns; the result is independent of the state | the impossibility of an objective or deterministic theory; excludes non-contextual values ​​under the given assumptions |
| Decoherence | off-diagonal, purity, diagonals | \(\gamma t=0\) | five values ​​\(\gamma t\) | the occurrence of a single result in a single run |
| Biharmonic backbone | homogeneous fixed points and eigenvalues | vacuum branch | lower and upper roots plus arbitrary Fourier mode \(k\) | existence of a localized particle or nonlinear global stability |
| Black hole | Kretschmann scalar and average density | value at the horizon | four radii; toy cutoff \(r^2+a^2\) | existence of a regular Lineum gravity metric |
| Discrete → continuous transport | relative \(L^2\) error | analytically translated periodic wave | \(N=32\) to 512 at fixed CFL | ontic continuity of physical space |
| Backend divergence | norm and relative \(L^2\) difference | identical initial data and Laplace symbol | 1, 100, and 1,000 steps | which backend is physically correct |
| OEA image ablation | relative \(L^2\), spectral anisotropy, sum of intensities | reference step 5, `DIFFUSE`, ordered scales | steps 4/6, staggered scales, `WAVE`, random seed | similarity or dissimilarity to actual cosmological data |
| deterministic time semantics | Fourier error, fixed-time refinement factor, stability multiplier | exact LAP4 eigenmodes and predicted \(h_{\max}=100\) | four modes, periodic impulse, nonuniform \(\kappa\), four \(h\), two CPU backends | physical value of \(t\), SI calibration, or final Lineum law |
| stochastic time contracts | RMS complex ensemble spread and fitted exponent \(q\) | analytic current-source \(q=1/2\) | current, initial-only, Gaussian-SDE, and Poisson laws; two grids, two initial fields, two horizons | which stochastic ontology is physically correct |
| historical zero-kappa RNG claim | exact difference recurrence and one-shot decay | closed-form damped geometric sum | original printed value, scalar recurrence, actual runtime, 1,500 steps | absence of chaos in every other Lineum regime |

### A.3 Numerical audit summary

| Check | Reference number |
|---|---:|
| LAP4 low-\(k\) coefficient | \(\approx1\) |
| LAP8 low-\(k\) coefficient | \(\approx1.50013\) |
| normalized LAP8 | \(\approx1.00009\) |
| spectral operator | 1 |
| wavefront \(k_0/\pi=0.5\): \(A_4\) LAP4 / normalized LAP8 / spectral control | \(0.355247 / 0.0385797 / 2.38\times10^{-17}\) |
| wavefront: max \(|\Delta A_4|\) between \(N=256\) and 512 | \(3.29\times10^{-7}\) |
| local Euler: number of cells after 1 step | 5 |
| spectral \(-k^2\): number of non-zero cells | 4096 |
| Landauer 300 K | \(2.870978885\times10^{-21}\,\mathrm{J/bit}\) |
| CHSH local | \(\approx2\) |
| CHSH quantum | \(2.828836\) |
| Peres–Mermin: product of row contexts | \(+1\) |
| Peres–Mermin: product of column contexts | \(-1\) |
| \(r_s(M_\odot)\) | \(2953.339\,\mathrm m\) |
| illustrative regular kernel: critical compactness \(r_s/\ell\) | \(3\sqrt3/2\approx2.598076\) |
| advection: asymptotic error ratio | \(\approx4\) |
| diffusion after 1000 steps: norm | \(0.3065662\) |
| wave after 1000 steps: norm | \(1.0\) |

### A.4 Complete executable program

The following code is the authoritative reproduction program. It requires no project data or repository files; when executed, it writes JSON containing every metric used above.

```python
"""Self-contained numerical checks for the Lineum foundational opposition audit.

Only NumPy and the Python standard library are required.  The script prints one
canonical JSON document.  It deliberately reimplements the audited numerical
operators instead of importing a Lineum package, so the calculations remain
independently reproducible.
"""

from __future__ import annotations

import itertools
import json
import math
import platform
from dataclasses import dataclass

import numpy as np


SEED = 20_260_715
RNG = np.random.default_rng(SEED)


def scalar(value):
    if isinstance(value, (np.integer,)):
        return int(value)
    if isinstance(value, (np.floating,)):
        return float(value)
    if isinstance(value, np.ndarray):
        return value.tolist()
    raise TypeError(type(value).__name__)


def lap_symbol(stencil: str, kx, ky):
    """Dimensionless symbols for unit lattice spacing."""
    if stencil == "LAP4":
        return -4.0 * (np.sin(kx / 2.0) ** 2 + np.sin(ky / 2.0) ** 2)
    if stencil == "LAP8":
        return -5.0 + 2.0 * np.cos(kx) + 2.0 * np.cos(ky) + np.cos(kx) * np.cos(ky)
    if stencil == "LAP8_NORMALIZED":
        return lap_symbol("LAP8", kx, ky) / 1.5
    if stencil == "ISOTROPIC":
        return -(kx * kx + ky * ky)
    raise ValueError(stencil)


def dispersion_audit():
    rows = []
    for fraction in (0.10, 0.25, 0.50, 0.75, 0.90):
        q = fraction * math.pi
        for stencil in ("LAP4", "LAP8", "LAP8_NORMALIZED", "ISOTROPIC"):
            lam_axis = float(lap_symbol(stencil, q, 0.0))
            lam_diag = float(lap_symbol(stencil, q / math.sqrt(2.0), q / math.sqrt(2.0)))
            # The implemented wave substep is Schrodinger-like: omega = -D*lambda.
            ratio_axis = -lam_axis / q**2
            ratio_diag = -lam_diag / q**2
            anis = abs(ratio_axis - ratio_diag) / ((ratio_axis + ratio_diag) / 2.0)

            # A generic hyperbolic lattice wave equation has omega=c*sqrt(-lambda).
            phase_axis = math.sqrt(max(-lam_axis, 0.0)) / q
            phase_diag = math.sqrt(max(-lam_diag, 0.0)) / q
            wave_anis = abs(phase_axis - phase_diag) / ((phase_axis + phase_diag) / 2.0)
            rows.append(
                {
                    "q_over_pi": fraction,
                    "stencil": stencil,
                    "schrodinger_axis_ratio": ratio_axis,
                    "schrodinger_diagonal_ratio": ratio_diag,
                    "schrodinger_directional_anisotropy": anis,
                    "wave_axis_phase_speed_over_c": phase_axis,
                    "wave_diagonal_phase_speed_over_c": phase_diag,
                    "wave_directional_anisotropy": wave_anis,
                }
            )
    q0 = 1.0e-6
    low_k_coefficients = {
        stencil: float(-lap_symbol(stencil, q0, 0.0) / q0**2)
        for stencil in ("LAP4", "LAP8", "LAP8_NORMALIZED", "ISOTROPIC")
    }
    return {"low_k_coefficients": low_k_coefficients, "rows": rows}


def periodic_distance_indices(size):
    raw = np.arange(size)
    return np.minimum(raw, size - raw)


def fft_propagate_impulse(size, stencil, diffusion=0.05, dt=1.0):
    freqs = np.fft.fftfreq(size) * 2.0 * math.pi
    ky, kx = np.meshgrid(freqs, freqs, indexing="ij")
    symbol = lap_symbol(stencil, kx, ky)
    psi_hat = np.ones((size, size), dtype=np.complex128)
    psi = np.fft.ifft2(psi_hat * np.exp(1j * diffusion * symbol * dt))
    probability = np.abs(psi) ** 2
    probability /= probability.sum()
    dy = periodic_distance_indices(size)[:, None]
    dx = periodic_distance_indices(size)[None, :]
    manhattan = dx + dy
    outside_one = manhattan > 1
    outside_two = manhattan > 2
    far = manhattan > size // 4
    return {
        "probability_outside_manhattan_radius_1": float(probability[outside_one].sum()),
        "probability_outside_manhattan_radius_2": float(probability[outside_two].sum()),
        "probability_beyond_quarter_grid": float(probability[far].sum()),
        "maximum_amplitude_outside_radius_1": float(np.abs(psi)[outside_one].max()),
        "nonzero_cells_threshold_1e_minus_15": int(np.count_nonzero(np.abs(psi) > 1.0e-15)),
        "norm": float(np.sum(np.abs(psi) ** 2)),
    }


def explicit_local_impulse(size=64, diffusion=0.05, dt=1.0):
    psi = np.zeros((size, size), dtype=np.complex128)
    psi[0, 0] = 1.0
    lap = (
        np.roll(psi, 1, 0)
        + np.roll(psi, -1, 0)
        + np.roll(psi, 1, 1)
        + np.roll(psi, -1, 1)
        - 4.0 * psi
    )
    psi = psi + diffusion * dt * lap
    weight = np.abs(psi) ** 2
    weight /= weight.sum()
    dy = periodic_distance_indices(size)[:, None]
    dx = periodic_distance_indices(size)[None, :]
    manhattan = dx + dy
    return {
        "probability_outside_manhattan_radius_1": float(weight[manhattan > 1].sum()),
        "nonzero_cells_threshold_1e_minus_15": int(np.count_nonzero(np.abs(psi) > 1.0e-15)),
        "norm_before_normalizing_weight": float(np.sum(np.abs(psi) ** 2)),
    }


def locality_audit():
    return {
        "explicit_local_euler_lap4": explicit_local_impulse(),
        "fft_exponential": {
            stencil: fft_propagate_impulse(64, stencil)
            for stencil in ("LAP4", "LAP8", "ISOTROPIC")
        },
    }


def gaussian_state(size, sigma_cells):
    coords = np.arange(size) - size // 2
    y, x = np.meshgrid(coords, coords, indexing="ij")
    # |psi|^2 is a Gaussian with coordinate standard deviation sigma_cells.
    psi = np.exp(-(x * x + y * y) / (4.0 * sigma_cells**2)).astype(np.complex128)
    psi /= np.linalg.norm(psi)
    return psi, x, y


def link_gradient_energy(psi, spacing=1.0):
    return float(
        (
            np.sum(np.abs(np.roll(psi, -1, 0) - psi) ** 2)
            + np.sum(np.abs(np.roll(psi, -1, 1) - psi) ** 2)
        )
        / spacing**2
    )


def localization_audit():
    rows = []
    for sigma in (0.05, 0.10, 0.20, 0.40, 0.70, 1.0, 2.0, 4.0, 8.0):
        psi, x, y = gaussian_state(256, sigma)
        p = np.abs(psi) ** 2
        rows.append(
            {
                "sigma_over_a": sigma,
                "gradient_energy_times_a_squared": link_gradient_energy(psi),
                "inverse_participation_ratio": float(np.sum(p * p)),
                "effective_site_count": float(1.0 / np.sum(p * p)),
                "rms_radius_over_a": float(np.sqrt(np.sum(p * (x * x + y * y)))),
                "peak_probability": float(p.max()),
            }
        )

    continuum_rows = []
    physical_sigma = 2.0
    exact = 1.0 / (2.0 * physical_sigma**2)
    for spacing in (1.0, 0.5, 0.25):
        size = int(round(64.0 / spacing))
        psi, _, _ = gaussian_state(size, physical_sigma / spacing)
        energy = link_gradient_energy(psi, spacing)
        continuum_rows.append(
            {
                "spacing": spacing,
                "size": size,
                "gradient_energy": energy,
                "continuum_value": exact,
                "relative_error": abs(energy - exact) / exact,
            }
        )
    return {
        "fixed_lattice_localization": rows,
        "continuum_refinement_fixed_physical_width": continuum_rows,
        "single_site_gradient_energy_times_a_squared": 4.0,
    }


def lineum_information(p):
    p = np.asarray(p, dtype=float)
    p = p / p.sum()
    nonzero = p > 0.0
    entropy = -float(np.sum(p[nonzero] * np.log(p[nonzero])))
    return math.log(p.size) - entropy


def information_energy_audit():
    count = 4096
    uniform = np.full(count, 1.0 / count)
    localized = np.zeros(count)
    localized[0] = 1.0
    half = np.zeros(count)
    half[: count // 2] = 2.0 / count
    examples = []
    for name, p, total_norm in (
        ("uniform_Q1", uniform, 1.0),
        ("uniform_Q100", uniform, 100.0),
        ("localized_Q1", localized, 1.0),
        ("half_support_Q1", half, 1.0),
    ):
        examples.append(
            {
                "state": name,
                "total_wave_norm_Q": total_norm,
                "I_logN_minus_H_nats": lineum_information(p),
                "I_bits": lineum_information(p) / math.log(2.0),
            }
        )

    k_b = 1.380649e-23
    c = 299_792_458.0
    temperature = 300.0
    erasure_energy = k_b * temperature * math.log(2.0)
    one_gb_bits = 8_000_000_000
    return {
        "counterexamples": examples,
        "identity": "log(N)-H(p) = D_KL(p || uniform)",
        "landauer_300K": {
            "joules_per_erased_bit": erasure_energy,
            "mass_equivalent_kg_per_erased_bit": erasure_energy / c**2,
            "decimal_1GB_minimum_erasure_joules": erasure_energy * one_gb_bits,
            "decimal_1GB_mass_equivalent_kg": erasure_energy * one_gb_bits / c**2,
        },
    }


def sign_nonzero(x):
    return np.where(x >= 0.0, 1, -1)


def bell_audit(trials=1_000_000):
    a = (0.0, math.pi / 2.0)
    b = (math.pi / 4.0, -math.pi / 4.0)
    local_correlations = {}
    quantum_correlations = {}
    quantum_marginals = {}
    quantum_variance = 0.0

    # One shared hidden-variable sample defines all four counterfactual local
    # outcomes.  Thus the finite-sample CHSH combination is itself bounded by 2.
    hidden = RNG.uniform(0.0, 2.0 * math.pi, size=trials)
    local_a = [sign_nonzero(np.cos(hidden - setting)) for setting in a]
    local_b = [-sign_nonzero(np.cos(hidden - setting)) for setting in b]

    for i, j in itertools.product(range(2), repeat=2):
        product = local_a[i] * local_b[j]
        corr = float(product.mean())
        local_correlations[f"E{i}{j}"] = corr

        qa = RNG.choice(np.array([-1, 1], dtype=np.int8), size=trials)
        expected_product = -math.cos(a[i] - b[j])
        probability_plus = (1.0 + expected_product) / 2.0
        qproduct = np.where(RNG.random(trials) < probability_plus, 1, -1)
        qb = qa * qproduct
        qcorr = float(qproduct.mean())
        quantum_correlations[f"E{i}{j}"] = qcorr
        quantum_marginals[f"A{i}_when_B{j}"] = float(qa.mean())
        quantum_marginals[f"B{j}_when_A{i}"] = float(qb.mean())
        quantum_variance += (1.0 - qcorr**2) / trials

    def chsh(c):
        return abs(c["E00"] + c["E01"] + c["E10"] - c["E11"])

    deterministic_values = []
    for a0, a1, b0, b1 in itertools.product((-1, 1), repeat=4):
        deterministic_values.append(abs(a0 * b0 + a0 * b1 + a1 * b0 - a1 * b1))

    return {
        "seed": SEED,
        "trials_per_setting_pair": trials,
        "settings_radians": {"a0": a[0], "a1": a[1], "b0": b[0], "b1": b[1]},
        "local_hidden_variable": {
            "correlations": local_correlations,
            "S": chsh(local_correlations),
            "finite_sample_bound": "S <= 2 because all four outcomes share one local hidden state per trial",
        },
        "quantum_singlet": {
            "correlations": quantum_correlations,
            "S": chsh(quantum_correlations),
            "standard_error_S": math.sqrt(quantum_variance),
            "theory_S": 2.0 * math.sqrt(2.0),
            "maximum_absolute_sample_marginal": max(abs(v) for v in quantum_marginals.values()),
            "sample_marginals": quantum_marginals,
        },
        "exact_deterministic_local_strategy_unique_abs_S": sorted(set(deterministic_values)),
    }


def decoherence_audit():
    rows = []
    for gamma_t in (0.0, 0.5, 1.0, 2.0, 5.0):
        coherence = 0.5 * math.exp(-gamma_t)
        purity = 0.5 * (1.0 + math.exp(-2.0 * gamma_t))
        rows.append(
            {
                "gamma_t": gamma_t,
                "rho_00": 0.5,
                "rho_11": 0.5,
                "abs_rho_01": coherence,
                "purity": purity,
                "selected_unique_outcome": False,
            }
        )
    return {"initial_state": "|+><+|", "pure_dephasing_rows": rows}


def black_hole_cutoff_audit():
    gravitational_constant = 6.67430e-11
    c = 299_792_458.0
    solar_mass = 1.98847e30
    planck_length = 1.616255e-35
    schwarzschild_radius = 2.0 * gravitational_constant * solar_mass / c**2

    def kretschmann(radius):
        return 48.0 * gravitational_constant**2 * solar_mass**2 / (c**4 * radius**6)

    def mean_density(radius):
        return solar_mass / ((4.0 / 3.0) * math.pi * radius**3)

    rows = []
    for label, radius in (
        ("Schwarzschild_radius", schwarzschild_radius),
        ("one_meter", 1.0),
        ("proton_scale", 1.0e-15),
        ("Planck_length", planck_length),
    ):
        rows.append(
            {
                "cutoff": label,
                "radius_m": radius,
                "Kretschmann_m_minus_4": kretschmann(radius),
                "mean_density_if_mass_inside_kg_m_minus_3": mean_density(radius),
            }
        )
    return {
        "solar_mass_kg": solar_mass,
        "Schwarzschild_radius_m": schwarzschild_radius,
        "rows": rows,
        "regularized_example": "K_a(r)=48 G^2 M^2/[c^4 (r^2+a^2)^3] is finite by construction but is not a derived field-equation solution",
    }


def lax_wendroff(u, courant):
    return (
        u
        - 0.5 * courant * (np.roll(u, -1) - np.roll(u, 1))
        + 0.5 * courant**2 * (np.roll(u, -1) - 2.0 * u + np.roll(u, 1))
    )


def zeno_convergence_audit():
    courant = 0.5
    final_time = 0.25
    rows = []
    previous_error = None
    for size in (32, 64, 128, 256, 512):
        x = np.arange(size) / size
        u = np.sin(2.0 * math.pi * x) + 0.25 * np.cos(6.0 * math.pi * x)
        steps = size // 2
        for _ in range(steps):
            u = lax_wendroff(u, courant)
        exact_x = (x - final_time) % 1.0
        exact = np.sin(2.0 * math.pi * exact_x) + 0.25 * np.cos(6.0 * math.pi * exact_x)
        error = float(np.sqrt(np.mean((u - exact) ** 2)))
        rows.append(
            {
                "cells": size,
                "dx": 1.0 / size,
                "dt": courant / size,
                "steps": steps,
                "L2_error": error,
                "error_ratio_previous_over_current": None if previous_error is None else previous_error / error,
            }
        )
        previous_error = error
    return {
        "equation": "u_t + u_x = 0 on a periodic unit interval",
        "scheme": "local Lax-Wendroff, Courant number 0.5",
        "rows": rows,
    }


def backend_formula_audit(size=128):
    psi, _, _ = gaussian_state(size, 5.0)
    dt = 0.1
    diffusion = 0.05
    # Reconstructed linear NumPy path: hard-coded 0.005 damping plus explicit diffusion.
    lap = (
        np.roll(psi, 1, 0)
        + np.roll(psi, -1, 0)
        + np.roll(psi, 1, 1)
        + np.roll(psi, -1, 1)
        - 4.0 * psi
    )
    freqs = np.fft.fftfreq(size) * 2.0 * math.pi
    ky, kx = np.meshgrid(freqs, freqs, indexing="ij")
    symbol = lap_symbol("LAP4", kx, ky)
    psi_hat = np.fft.fft2(psi)
    norm0 = float(np.sum(np.abs(psi) ** 2))
    rows = []
    for steps in (1, 100, 1000):
        numpy_path = np.fft.ifft2(psi_hat * (1.0 - 0.005 * dt + diffusion * dt * symbol) ** steps)
        torch_wave_formula = np.fft.ifft2(
            psi_hat * np.exp(1j * diffusion * symbol * dt * steps)
        )
        norm_numpy = float(np.sum(np.abs(numpy_path) ** 2))
        norm_wave = float(np.sum(np.abs(torch_wave_formula) ** 2))
        rows.append(
            {
                "steps": steps,
                "numpy_diffusion_path_norm": norm_numpy,
                "wave_fft_path_norm": norm_wave,
                "numpy_relative_norm_change": norm_numpy / norm0 - 1.0,
                "wave_relative_norm_change": norm_wave / norm0 - 1.0,
                "relative_L2_difference_between_paths": float(
                    np.linalg.norm(numpy_path - torch_wave_formula) / np.linalg.norm(psi)
                ),
            }
        )
    return {
        "initial_norm": norm0,
        "rows": rows,
        "parameters": {"size": size, "dt": dt, "psi_diffusion": diffusion},
    }


def main():
    result = {
        "schema": "lineum.foundational-opposition-audit.v1",
        "seed": SEED,
        "runtime": {"python": platform.python_version(), "numpy": np.__version__},
        "dispersion_and_anisotropy": dispersion_audit(),
        "one_step_locality": locality_audit(),
        "localization_and_uv_cutoff": localization_audit(),
        "information_energy_independence": information_energy_audit(),
        "bell_chsh": bell_audit(),
        "decoherence": decoherence_audit(),
        "black_hole_cutoff": black_hole_cutoff_audit(),
        "discrete_to_continuum_convergence": zeno_convergence_audit(),
        "backend_formula_divergence": backend_formula_audit(),
    }
    print(json.dumps(result, indent=2, sort_keys=True, default=scalar, allow_nan=False))


if __name__ == "__main__":
    main()

```
### A.5 Full reference output

The following is the complete JSON from the audit environment. It is embedded so that metrics not selected for the main tables remain available for audit.

```json
{
  "backend_formula_divergence": {
    "initial_norm": 0.9999999999999999,
    "parameters": {
      "dt": 0.1,
      "psi_diffusion": 0.05,
      "size": 128
    },
    "rows": [
      {
        "numpy_diffusion_path_norm": 0.99880086876885,
        "numpy_relative_norm_change": -0.001199131231149897,
        "relative_L2_difference_between_paths": 0.0006240481010925598,
        "steps": 1,
        "wave_fft_path_norm": 1.0,
        "wave_relative_norm_change": 2.220446049250313e-16
      },
      {
        "numpy_diffusion_path_norm": 0.887105515368855,
        "numpy_relative_norm_change": -0.11289448463114493,
        "relative_L2_difference_between_paths": 0.06045483803599482,
        "steps": 100,
        "wave_fft_path_norm": 1.0,
        "wave_relative_norm_change": 2.220446049250313e-16
      },
      {
        "numpy_diffusion_path_norm": 0.3065661648756069,
        "numpy_relative_norm_change": -0.693433835124393,
        "relative_L2_difference_between_paths": 0.4612371402460408,
        "steps": 1000,
        "wave_fft_path_norm": 1.0,
        "wave_relative_norm_change": 2.220446049250313e-16
      }
    ]
  },
  "bell_chsh": {
    "exact_deterministic_local_strategy_unique_abs_S": [
      2
    ],
    "local_hidden_variable": {
      "S": 1.9999999999999998,
      "correlations": {
        "E00": -0.50161,
        "E01": -0.498866,
        "E10": -0.499904,
        "E11": 0.49962
      },
      "finite_sample_bound": "S <= 2 because all four outcomes share one local hidden state per trial"
    },
    "quantum_singlet": {
      "S": 2.828836,
      "correlations": {
        "E00": -0.707606,
        "E01": -0.706728,
        "E10": -0.706764,
        "E11": 0.707738
      },
      "maximum_absolute_sample_marginal": 0.001128,
      "sample_marginals": {
        "A0_when_B0": -0.00071,
        "A0_when_B1": -0.00028,
        "A1_when_B0": 0.001128,
        "A1_when_B1": -0.00016,
        "B0_when_A0": 0.000588,
        "B0_when_A1": -0.000768,
        "B1_when_A0": 0.000992,
        "B1_when_A1": -0.000102
      },
      "standard_error_S": 0.0014140087886714142,
      "theory_S": 2.8284271247461903
    },
    "seed": 20260715,
    "settings_radians": {
      "a0": 0.0,
      "a1": 1.5707963267948966,
      "b0": 0.7853981633974483,
      "b1": -0.7853981633974483
    },
    "trials_per_setting_pair": 1000000
  },
  "black_hole_cutoff": {
    "Schwarzschild_radius_m": 2953.3393820668784,
    "regularized_example": "K_a(r)=48 G^2 M^2/[c^4 (r^2+a^2)^3] is finite by construction but is not a derived field-equation solution",
    "rows": [
      {
        "Kretschmann_m_minus_4": 1.577349089601718e-13,
        "cutoff": "Schwarzschild_radius",
        "mean_density_if_mass_inside_kg_m_minus_3": 1.8428515995982211e+19,
        "radius_m": 2953.3393820668784
      },
      {
        "Kretschmann_m_minus_4": 104666562.06800605,
        "cutoff": "one_meter",
        "mean_density_if_mass_inside_kg_m_minus_3": 4.747122445349117e+29,
        "radius_m": 1.0
      },
      {
        "Kretschmann_m_minus_4": 1.04666562068006e+98,
        "cutoff": "proton_scale",
        "mean_density_if_mass_inside_kg_m_minus_3": 4.747122445349115e+74,
        "radius_m": 1e-15
      },
      {
        "Kretschmann_m_minus_4": 5.871494668601715e+216,
        "cutoff": "Planck_length",
        "mean_density_if_mass_inside_kg_m_minus_3": 1.1243480982257166e+134,
        "radius_m": 1.616255e-35
      }
    ],
    "solar_mass_kg": 1.98847e+30
  },
  "decoherence": {
    "initial_state": "|+><+|",
    "pure_dephasing_rows": [
      {
        "abs_rho_01": 0.5,
        "gamma_t": 0.0,
        "purity": 1.0,
        "rho_00": 0.5,
        "rho_11": 0.5,
        "selected_unique_outcome": false
      },
      {
        "abs_rho_01": 0.3032653298563167,
        "gamma_t": 0.5,
        "purity": 0.6839397205857212,
        "rho_00": 0.5,
        "rho_11": 0.5,
        "selected_unique_outcome": false
      },
      {
        "abs_rho_01": 0.18393972058572117,
        "gamma_t": 1.0,
        "purity": 0.5676676416183064,
        "rho_00": 0.5,
        "rho_11": 0.5,
        "selected_unique_outcome": false
      },
      {
        "abs_rho_01": 0.06766764161830635,
        "gamma_t": 2.0,
        "purity": 0.5091578194443671,
        "rho_00": 0.5,
        "rho_11": 0.5,
        "selected_unique_outcome": false
      },
      {
        "abs_rho_01": 0.0033689734995427335,
        "gamma_t": 5.0,
        "purity": 0.5000226999648812,
        "rho_00": 0.5,
        "rho_11": 0.5,
        "selected_unique_outcome": false
      }
    ]
  },
  "discrete_to_continuum_convergence": {
    "equation": "u_t + u_x = 0 on a periodic unit interval",
    "rows": [
      {
        "L2_error": 0.035104069331325295,
        "cells": 32,
        "dt": 0.015625,
        "dx": 0.03125,
        "error_ratio_previous_over_current": null,
        "steps": 16
      },
      {
        "L2_error": 0.009064039971591671,
        "cells": 64,
        "dt": 0.0078125,
        "dx": 0.015625,
        "error_ratio_previous_over_current": 3.8728943651338423,
        "steps": 32
      },
      {
        "L2_error": 0.002279384963882293,
        "cells": 128,
        "dt": 0.00390625,
        "dx": 0.0078125,
        "error_ratio_previous_over_current": 3.9765288072066687,
        "steps": 64
      },
      {
        "L2_error": 0.0005705159334825787,
        "cells": 256,
        "dt": 0.001953125,
        "dx": 0.00390625,
        "error_ratio_previous_over_current": 3.995304653400879,
        "steps": 128
      },
      {
        "L2_error": 0.00014266548960616016,
        "cells": 512,
        "dt": 0.0009765625,
        "dx": 0.001953125,
        "error_ratio_previous_over_current": 3.998976452241779,
        "steps": 256
      }
    ],
    "scheme": "local Lax-Wendroff, Courant number 0.5"
  },
  "dispersion_and_anisotropy": {
    "low_k_coefficients": {
      "ISOTROPIC": 1.0,
      "LAP4": 0.9999999999999166,
      "LAP8": 1.5001333508735115,
      "LAP8_NORMALIZED": 1.000088900582341
    },
    "rows": [
      {
        "q_over_pi": 0.1,
        "schrodinger_axis_ratio": 0.9918023401109023,
        "schrodinger_diagonal_ratio": 0.9958944233953627,
        "schrodinger_directional_anisotropy": 0.004117412031442919,
        "stencil": "LAP4",
        "wave_axis_phase_speed_over_c": 0.9958927352435614,
        "wave_diagonal_phase_speed_over_c": 0.9979451003914808,
        "wave_directional_anisotropy": 0.0020587081970642974
      },
      {
        "q_over_pi": 0.1,
        "schrodinger_axis_ratio": 1.4877035101663525,
        "schrodinger_diagonal_ratio": 1.4877236788887236,
        "schrodinger_directional_anisotropy": 1.3556858285952249e-05,
        "stencil": "LAP8",
        "wave_axis_phase_speed_over_c": 1.2197145199456931,
        "wave_diagonal_phase_speed_over_c": 1.2197227877221626,
        "wave_directional_anisotropy": 6.778429143034364e-06
      },
      {
        "q_over_pi": 0.1,
        "schrodinger_axis_ratio": 0.9918023401109016,
        "schrodinger_diagonal_ratio": 0.9918157859258159,
        "schrodinger_directional_anisotropy": 1.3556858286138816e-05,
        "stencil": "LAP8_NORMALIZED",
        "wave_axis_phase_speed_over_c": 0.995892735243561,
        "wave_diagonal_phase_speed_over_c": 0.9958994858547803,
        "wave_directional_anisotropy": 6.778429143095241e-06
      },
      {
        "q_over_pi": 0.1,
        "schrodinger_axis_ratio": 1.0,
        "schrodinger_diagonal_ratio": 0.9999999999999999,
        "schrodinger_directional_anisotropy": 1.1102230246251565e-16,
        "stencil": "ISOTROPIC",
        "wave_axis_phase_speed_over_c": 1.0,
        "wave_diagonal_phase_speed_over_c": 0.9999999999999998,
        "wave_directional_anisotropy": 2.2204460492503136e-16
      },
      {
        "q_over_pi": 0.25,
        "schrodinger_axis_ratio": 0.9496412035517837,
        "schrodinger_diagonal_ratio": 0.9745606939309757,
        "schrodinger_directional_anisotropy": 0.025901118184938513,
        "stencil": "LAP4",
        "wave_axis_phase_speed_over_c": 0.9744953584044327,
        "wave_diagonal_phase_speed_over_c": 0.9871984065682924,
        "wave_directional_anisotropy": 0.012951102145177404
      },
      {
        "q_over_pi": 0.25,
        "schrodinger_axis_ratio": 1.4244618053276756,
        "schrodinger_diagonal_ratio": 1.4252244790872841,
        "schrodinger_directional_anisotropy": 0.0005352685758987366,
        "stencil": "LAP8",
        "wave_axis_phase_speed_over_c": 1.1935081924007376,
        "wave_diagonal_phase_speed_over_c": 1.1938276588717838,
        "wave_directional_anisotropy": 0.00026763429274176686
      },
      {
        "q_over_pi": 0.25,
        "schrodinger_axis_ratio": 0.9496412035517837,
        "schrodinger_diagonal_ratio": 0.9501496527248561,
        "schrodinger_directional_anisotropy": 0.0005352685758987756,
        "stencil": "LAP8_NORMALIZED",
        "wave_axis_phase_speed_over_c": 0.9744953584044327,
        "wave_diagonal_phase_speed_over_c": 0.9747562016857632,
        "wave_directional_anisotropy": 0.00026763429274197914
      },
      {
        "q_over_pi": 0.25,
        "schrodinger_axis_ratio": 1.0,
        "schrodinger_diagonal_ratio": 1.0,
        "schrodinger_directional_anisotropy": 0.0,
        "stencil": "ISOTROPIC",
        "wave_axis_phase_speed_over_c": 1.0,
        "wave_diagonal_phase_speed_over_c": 1.0,
        "wave_directional_anisotropy": 0.0
      },
      {
        "q_over_pi": 0.5,
        "schrodinger_axis_ratio": 0.8105694691387024,
        "schrodinger_diagonal_ratio": 0.9013275703126176,
        "schrodinger_directional_anisotropy": 0.10603219595847191,
        "stencil": "LAP4",
        "wave_axis_phase_speed_over_c": 0.9003163161571062,
        "wave_diagonal_phase_speed_over_c": 0.9493827312062388,
        "wave_directional_anisotropy": 0.053053403599979614
      },
      {
        "q_over_pi": 0.5,
        "schrodinger_axis_ratio": 1.2158542037080533,
        "schrodinger_diagonal_ratio": 1.226710392526157,
        "schrodinger_directional_anisotropy": 0.008889172335373379,
        "stencil": "LAP8",
        "wave_axis_phase_speed_over_c": 1.1026577908435842,
        "wave_diagonal_phase_speed_over_c": 1.1075695881190297,
        "wave_directional_anisotropy": 0.004444608117876938
      },
      {
        "q_over_pi": 0.5,
        "schrodinger_axis_ratio": 0.8105694691387022,
        "schrodinger_diagonal_ratio": 0.8178069283507714,
        "schrodinger_directional_anisotropy": 0.008889172335373379,
        "stencil": "LAP8_NORMALIZED",
        "wave_axis_phase_speed_over_c": 0.9003163161571062,
        "wave_diagonal_phase_speed_over_c": 0.9043267818387176,
        "wave_directional_anisotropy": 0.0044446081178769825
      },
      {
        "q_over_pi": 0.5,
        "schrodinger_axis_ratio": 1.0,
        "schrodinger_diagonal_ratio": 1.0,
        "schrodinger_directional_anisotropy": 0.0,
        "stencil": "ISOTROPIC",
        "wave_axis_phase_speed_over_c": 1.0,
        "wave_diagonal_phase_speed_over_c": 1.0,
        "wave_directional_anisotropy": 0.0
      },
      {
        "q_over_pi": 0.75,
        "schrodinger_axis_ratio": 0.614990505506426,
        "schrodinger_diagonal_ratio": 0.7890556266110312,
        "schrodinger_directional_anisotropy": 0.2479478659894113,
        "stencil": "LAP4",
        "wave_axis_phase_speed_over_c": 0.7842133035765372,
        "wave_diagonal_phase_speed_over_c": 0.8882880313338862,
        "wave_directional_anisotropy": 0.12445398468148085
      },
      {
        "q_over_pi": 0.75,
        "schrodinger_axis_ratio": 0.9224857582596389,
        "schrodinger_diagonal_ratio": 0.9675517158353854,
        "schrodinger_directional_anisotropy": 0.0476878984606638,
        "stencil": "LAP8",
        "wave_axis_phase_speed_over_c": 0.960461221632419,
        "wave_diagonal_phase_speed_over_c": 0.9836420669305402,
        "wave_directional_anisotropy": 0.023847339217512517
      },
      {
        "q_over_pi": 0.75,
        "schrodinger_axis_ratio": 0.6149905055064259,
        "schrodinger_diagonal_ratio": 0.6450344772235902,
        "schrodinger_directional_anisotropy": 0.0476878984606638,
        "stencil": "LAP8_NORMALIZED",
        "wave_axis_phase_speed_over_c": 0.7842133035765371,
        "wave_diagonal_phase_speed_over_c": 0.8031403845054675,
        "wave_directional_anisotropy": 0.02384733921751241
      },
      {
        "q_over_pi": 0.75,
        "schrodinger_axis_ratio": 1.0,
        "schrodinger_diagonal_ratio": 0.9999999999999997,
        "schrodinger_directional_anisotropy": 3.3306690738754706e-16,
        "stencil": "ISOTROPIC",
        "wave_axis_phase_speed_over_c": 1.0,
        "wave_diagonal_phase_speed_over_c": 0.9999999999999998,
        "wave_directional_anisotropy": 2.2204460492503136e-16
      },
      {
        "q_over_pi": 0.9,
        "schrodinger_axis_ratio": 0.4881070508249903,
        "schrodinger_diagonal_ratio": 0.7082514805469938,
        "schrodinger_directional_anisotropy": 0.36802417327110437,
        "stencil": "LAP4",
        "wave_axis_phase_speed_over_c": 0.6986465850664342,
        "wave_diagonal_phase_speed_over_c": 0.8415767823241048,
        "wave_directional_anisotropy": 0.18559671315703297
      },
      {
        "q_over_pi": 0.9,
        "schrodinger_axis_ratio": 0.7321605762374854,
        "schrodinger_diagonal_ratio": 0.8117433486945655,
        "schrodinger_directional_anisotropy": 0.10309290775406592,
        "stencil": "LAP8",
        "wave_axis_phase_speed_over_c": 0.8556638219753628,
        "wave_diagonal_phase_speed_over_c": 0.9009680064766814,
        "wave_directional_anisotropy": 0.05158073964906
      },
      {
        "q_over_pi": 0.9,
        "schrodinger_axis_ratio": 0.4881070508249903,
        "schrodinger_diagonal_ratio": 0.5411622324630436,
        "schrodinger_directional_anisotropy": 0.10309290775406578,
        "stencil": "LAP8_NORMALIZED",
        "wave_axis_phase_speed_over_c": 0.6986465850664342,
        "wave_diagonal_phase_speed_over_c": 0.7356372968134797,
        "wave_directional_anisotropy": 0.051580739649060015
      },
      {
        "q_over_pi": 0.9,
        "schrodinger_axis_ratio": 1.0,
        "schrodinger_diagonal_ratio": 1.0,
        "schrodinger_directional_anisotropy": 0.0,
        "stencil": "ISOTROPIC",
        "wave_axis_phase_speed_over_c": 1.0,
        "wave_diagonal_phase_speed_over_c": 1.0,
        "wave_directional_anisotropy": 0.0
      }
    ]
  },
  "information_energy_independence": {
    "counterexamples": [
      {
        "I_bits": 2.562741203051934e-15,
        "I_logN_minus_H_nats": 1.7763568394002505e-15,
        "state": "uniform_Q1",
        "total_wave_norm_Q": 1.0
      },
      {
        "I_bits": 2.562741203051934e-15,
        "I_logN_minus_H_nats": 1.7763568394002505e-15,
        "state": "uniform_Q100",
        "total_wave_norm_Q": 100.0
      },
      {
        "I_bits": 12.0,
        "I_logN_minus_H_nats": 8.317766166719343,
        "state": "localized_Q1",
        "total_wave_norm_Q": 1.0
      },
      {
        "I_bits": 0.999999999999995,
        "I_logN_minus_H_nats": 0.6931471805599418,
        "state": "half_support_Q1",
        "total_wave_norm_Q": 1.0
      }
    ],
    "identity": "log(N)-H(p) = D_KL(p || uniform)",
    "landauer_300K": {
      "decimal_1GB_mass_equivalent_kg": 2.5555158539292775e-28,
      "decimal_1GB_minimum_erasure_joules": 2.296783108062979e-11,
      "joules_per_erased_bit": 2.870978885078724e-21,
      "mass_equivalent_kg_per_erased_bit": 3.1943948174115975e-38
    }
  },
  "localization_and_uv_cutoff": {
    "continuum_refinement_fixed_physical_width": [
      {
        "continuum_value": 0.125,
        "gradient_energy": 0.1230670620946237,
        "relative_error": 0.01546350324301038,
        "size": 64,
        "spacing": 1.0
      },
      {
        "continuum_value": 0.125,
        "gradient_energy": 0.12451298783610379,
        "relative_error": 0.0038960973111696884,
        "size": 128,
        "spacing": 0.5
      },
      {
        "continuum_value": 0.125,
        "gradient_energy": 0.12487800912156984,
        "relative_error": 0.0009759270274413145,
        "size": 256,
        "spacing": 0.25
      }
    ],
    "fixed_lattice_localization": [
      {
        "effective_site_count": 1.0,
        "gradient_energy_times_a_squared": 4.0,
        "inverse_participation_ratio": 1.0,
        "peak_probability": 1.0,
        "rms_radius_over_a": 7.440151952041778e-44,
        "sigma_over_a": 0.05
      },
      {
        "effective_site_count": 1.0,
        "gradient_energy_times_a_squared": 3.999999999888897,
        "inverse_participation_ratio": 1.0,
        "peak_probability": 1.0,
        "rms_radius_over_a": 2.777588772992814e-11,
        "sigma_over_a": 0.1
      },
      {
        "effective_site_count": 1.0000298135031362,
        "gradient_energy_times_a_squared": 3.9845564820152335,
        "inverse_participation_ratio": 0.9999701873856822,
        "peak_probability": 0.9999850935539649,
        "rms_radius_over_a": 0.0038608938842697904,
        "sigma_over_a": 0.2
      },
      {
        "effective_site_count": 1.3898854034731627,
        "gradient_energy_times_a_squared": 2.4555959929792843,
        "inverse_participation_ratio": 0.7194837772244501,
        "peak_probability": 0.84496157652871,
        "rms_radius_over_a": 0.4020015869505464,
        "sigma_over_a": 0.4
      },
      {
        "effective_site_count": 5.969577697750171,
        "gradient_energy_times_a_squared": 0.9014313498892826,
        "inverse_participation_ratio": 0.16751603725283323,
        "peak_probability": 0.324724157283455,
        "rms_radius_over_a": 0.9887422620972435,
        "sigma_over_a": 0.7
      },
      {
        "effective_site_count": 12.563771395712344,
        "gradient_energy_times_a_squared": 0.4700124274365519,
        "inverse_participation_ratio": 0.07959393469553827,
        "peak_probability": 0.1591549413887541,
        "rms_radius_over_a": 1.4142134130093151,
        "sigma_over_a": 1.0
      },
      {
        "effective_site_count": 50.26548245743667,
        "gradient_energy_times_a_squared": 0.1230670620946237,
        "inverse_participation_ratio": 0.019894367886486925,
        "peak_probability": 0.039788735772973836,
        "rms_radius_over_a": 2.8284271247461903,
        "sigma_over_a": 2.0
      },
      {
        "effective_site_count": 201.06192982974673,
        "gradient_energy_times_a_squared": 0.031128246959025958,
        "inverse_participation_ratio": 0.00497359197162173,
        "peak_probability": 0.009947183943243459,
        "rms_radius_over_a": 5.656854249492381,
        "sigma_over_a": 4.0
      },
      {
        "effective_site_count": 804.2477193189859,
        "gradient_energy_times_a_squared": 0.007804875570098115,
        "inverse_participation_ratio": 0.0012433979929054341,
        "peak_probability": 0.0024867959858108665,
        "rms_radius_over_a": 11.313708498984765,
        "sigma_over_a": 8.0
      }
    ],
    "single_site_gradient_energy_times_a_squared": 4.0
  },
  "one_step_locality": {
    "explicit_local_euler_lap4": {
      "nonzero_cells_threshold_1e_minus_15": 5,
      "norm_before_normalizing_weight": 0.6499999999999999,
      "probability_outside_manhattan_radius_1": 0.0
    },
    "fft_exponential": {
      "ISOTROPIC": {
        "maximum_amplitude_outside_radius_1": 0.025248621044932505,
        "nonzero_cells_threshold_1e_minus_15": 4096,
        "norm": 1.0000000000000002,
        "probability_beyond_quarter_grid": 5.884100621866482e-06,
        "probability_outside_manhattan_radius_1": 0.003824767102907896,
        "probability_outside_manhattan_radius_2": 0.0008835566727202756
      },
      "LAP4": {
        "maximum_amplitude_outside_radius_1": 0.002493756506620347,
        "nonzero_cells_threshold_1e_minus_15": 141,
        "norm": 0.9999999999999997,
        "probability_beyond_quarter_grid": 6.414780274400069e-33,
        "probability_outside_manhattan_radius_1": 3.11166014574914e-05,
        "probability_outside_manhattan_radius_2": 3.2863987277368226e-08
      },
      "LAP8": {
        "maximum_amplitude_outside_radius_1": 0.012651443282323574,
        "nonzero_cells_threshold_1e_minus_15": 241,
        "norm": 1.0,
        "probability_beyond_quarter_grid": 8.295541444361262e-33,
        "probability_outside_manhattan_radius_1": 0.0006512650712993924,
        "probability_outside_manhattan_radius_2": 3.1656278104242776e-06
      }
    }
  },
  "runtime": {
    "numpy": "1.26.4",
    "python": "3.11.15"
  },
  "schema": "lineum.foundational-opposition-audit.v1",
  "seed": 20260715
}

```

---

## Appendix B — Supplemental Analytical Controls

This short block reproduces the values used in the analytical checks of calibration, state-space finiteness, lattice dispersion, Derrick scaling, and the illustrative regular-gravity core.

```python
import json
import math

h = 6.62607015e-34
c = 299792458.0
electronvolt = 1.602176634e-19
planck_length = 1.616255e-35
dimensionless_frequency = 0.1
G = 6.67430e-11
hbar = 1.054571817e-34
k_B = 1.380649e-23
solar_mass = 1.98847e30

calibration = []
for dt in (1e-21, 1e-18, 1e-15):
    frequency = dimensionless_frequency / dt
    energy = h * frequency
    calibration.append(
        {
            "dt_s": dt,
            "frequency_hz": frequency,
            "energy_j": energy,
            "mass_kg": energy / c**2,
            "energy_MeV": energy / electronvolt / 1e6,
        }
    )

side = 128
sites = side**2
levels_per_field = 2**16
fields = 2
state_bits = fields * sites * 16

derived_planck_length = math.sqrt(hbar * G / c**3)
schwarzschild_radius = 2 * G * solar_mass / c**2
horizon_area = 4 * math.pi * schwarzschild_radius**2
entropy_over_k_B = horizon_area / (4 * derived_planck_length**2)
hawking_temperature = hbar * c**3 / (8 * math.pi * G * solar_mass * k_B)

result = {
    "calibration_for_dimensionless_frequency_0.1": calibration,
    "finite_state_space": {
        "side": side,
        "sites": sites,
        "fields": fields,
        "levels_per_field": levels_per_field,
        "log2_number_of_states": state_bits,
        "deterministic_recurrence_upper_bound_steps": f"2^{state_bits}+1",
    },
    "lorentz_diagnostics": {
        "fermi_linear_effect_length_upper_bound_m": planck_length / 1.2,
        "lap4_phase_correction_axis_coefficient_for_a2k2": 1 / 24,
        "lap4_phase_correction_diagonal_coefficient_for_a2k2": 1 / 48,
        "lap4_cos4theta_coefficient_for_a2k2": 1 / 96,
    },
    "derrick_scaling_exponents_d2": {
        "two_derivative_T2": 0,
        "four_derivative_T4": 2,
        "potential_V": -2,
    },
    "illustrative_regular_core": {
        "x_at_maximum_compactness_profile": math.sqrt(2),
        "maximum_x2_over_1_plus_x2_pow_3_over_2": 2 / (3 * math.sqrt(3)),
        "critical_rs_over_ell_for_horizons": 3 * math.sqrt(3) / 2,
        "critical_ell_over_rs": 2 / (3 * math.sqrt(3)),
        "kretschmann_center_coefficient_in_G2M2_over_c4ell6": 96,
    },
    "solar_mass_black_hole_thermodynamics": {
        "schwarzschild_radius_m": schwarzschild_radius,
        "horizon_area_m2": horizon_area,
        "entropy_over_k_B": entropy_over_k_B,
        "entropy_bits": entropy_over_k_B / math.log(2),
        "hawking_temperature_K": hawking_temperature,
    },
}

print(json.dumps(result, indent=2, sort_keys=True))

```

Reference output:

```json
{
  "calibration_for_dimensionless_frequency_0.1": [
    {
      "dt_s": 1e-21,
      "energy_MeV": 0.4135667696923859,
      "energy_j": 6.62607015e-14,
      "frequency_hz": 1.0000000000000002e+20,
      "mass_kg": 7.372497323812709e-31
    },
    {
      "dt_s": 1e-18,
      "energy_MeV": 0.0004135667696923858,
      "energy_j": 6.626070149999999e-17,
      "frequency_hz": 1e+17,
      "mass_kg": 7.372497323812707e-34
    },
    {
      "dt_s": 1e-15,
      "energy_MeV": 4.1356676969238585e-07,
      "energy_j": 6.62607015e-20,
      "frequency_hz": 100000000000000.0,
      "mass_kg": 7.372497323812708e-37
    }
  ],
  "derrick_scaling_exponents_d2": {
    "four_derivative_T4": 2,
    "potential_V": -2,
    "two_derivative_T2": 0
  },
  "finite_state_space": {
    "deterministic_recurrence_upper_bound_steps": "2^524288+1",
    "fields": 2,
    "levels_per_field": 65536,
    "log2_number_of_states": 524288,
    "side": 128,
    "sites": 16384
  },
  "illustrative_regular_core": {
    "critical_ell_over_rs": 0.3849001794597505,
    "critical_rs_over_ell_for_horizons": 2.598076211353316,
    "kretschmann_center_coefficient_in_G2M2_over_c4ell6": 96,
    "maximum_x2_over_1_plus_x2_pow_3_over_2": 0.3849001794597505,
    "x_at_maximum_compactness_profile": 1.4142135623730951
  },
  "lorentz_diagnostics": {
    "fermi_linear_effect_length_upper_bound_m": 1.3468791666666668e-35,
    "lap4_cos4theta_coefficient_for_a2k2": 0.010416666666666666,
    "lap4_phase_correction_axis_coefficient_for_a2k2": 0.041666666666666664,
    "lap4_phase_correction_diagonal_coefficient_for_a2k2": 0.020833333333333332
  },
  "solar_mass_black_hole_thermodynamics": {
    "entropy_bits": 1.5133220124066416e+77,
    "entropy_over_k_B": 1.0489548861789662e+77,
    "hawking_temperature_K": 6.170073824811396e-08,
    "horizon_area_m2": 109606567.48978263,
    "schwarzschild_radius_m": 2953.3393820668784
  }
}
```

---

## Appendix C — OEA Imaging-Mechanism Ablation

Dependencies: Python 3.11.15, NumPy 1.26.4, and SciPy 1.17.1. The program neither reads nor creates image files; it measures the scalar field directly before color mapping.

```python
import json
import math

import numpy as np
from scipy import ndimage

SEED = 20260715
SIZE = 192
ITERATIONS = 192


def lattice(size, step):
    grid = np.zeros((size, size), dtype=np.float32)
    grid[::step, ::step] = 1.0
    return grid


def random_scatter(size, density, seed):
    rng = np.random.default_rng(seed)
    return (rng.random((size, size)) < density).astype(np.float32)


def expansion(grid, scale, size):
    input_size = int(np.ceil(size / scale)) + 2
    patch = grid[:input_size, :input_size]
    expanded = ndimage.zoom(patch, scale, order=1)
    return expanded[:size, :size]


def simulate(base, mode, scales):
    field = base.copy()
    sums = [float(field.sum())]
    for scale in scales:
        layer = expansion(base, scale, base.shape[0])
        if mode == "WAVE":
            field = np.abs(field - layer)
        elif mode == "DIFFUSE":
            field = np.tanh(field + ndimage.gaussian_filter(layer, sigma=1.5))
        else:
            raise ValueError(mode)
        sums.append(float(field.sum()))
    maximum = float(field.max())
    if maximum > 0:
        field = field / maximum
    return field, sums


def metrics(field):
    centered = field - field.mean()
    fft = np.fft.fftshift(np.fft.fft2(centered))
    power = np.abs(fft) ** 2
    yy, xx = np.indices(field.shape)
    cy = (field.shape[0] - 1) / 2
    cx = (field.shape[1] - 1) / 2
    dx = xx - cx
    dy = yy - cy
    radius = np.hypot(dx, dy)
    angle = np.arctan2(dy, dx)
    mask = radius > 2
    weighted = power[mask]
    denom = float(weighted.sum()) + 1e-300
    fourfold = float(np.sum(weighted * np.cos(4 * angle[mask])) / denom)
    twofold = float(np.sum(weighted * np.cos(2 * angle[mask])) / denom)
    low_frequency = float(power[(radius > 0) & (radius < SIZE * 0.08)].sum() / (power.sum() + 1e-300))
    hist, _ = np.histogram(field, bins=256, range=(0, 1))
    p = hist[hist > 0] / hist.sum()
    histogram_entropy_bits = float(-np.sum(p * np.log2(p)))
    gy, gx = np.gradient(field)
    return {
        "mean": float(field.mean()),
        "std": float(field.std()),
        "histogram_entropy_bits_max8": histogram_entropy_bits,
        "fourfold_power_anisotropy": fourfold,
        "twofold_power_anisotropy": twofold,
        "low_frequency_power_fraction": low_frequency,
        "gradient_energy": float(np.mean(gx * gx + gy * gy)),
        "fraction_above_0_99": float(np.mean(field > 0.99)),
    }


def relative_l2(a, b):
    return float(np.linalg.norm(a - b) / (np.linalg.norm(a) + 1e-300))


def main():
    scales = list(range(2, ITERATIONS + 2))
    shuffled = scales.copy()
    np.random.default_rng(SEED).shuffle(shuffled)
    cases = {
        "lattice_step5_diffuse": (lattice(SIZE, 5), "DIFFUSE", scales),
        "lattice_step5_wave": (lattice(SIZE, 5), "WAVE", scales),
        "lattice_step4_diffuse": (lattice(SIZE, 4), "DIFFUSE", scales),
        "lattice_step6_diffuse": (lattice(SIZE, 6), "DIFFUSE", scales),
        "lattice_step5_diffuse_shuffled_scales": (lattice(SIZE, 5), "DIFFUSE", shuffled),
        "random_same_density_diffuse": (random_scatter(SIZE, 1 / 25, SEED), "DIFFUSE", scales),
    }
    fields = {}
    result = {
        "schema": "lineum.oea-ablation-audit.v1",
        "seed": SEED,
        "size": SIZE,
        "iterations": ITERATIONS,
        "cases": {},
    }
    for name, (base, mode, case_scales) in cases.items():
        field, sums = simulate(base, mode, case_scales)
        fields[name] = field
        result["cases"][name] = {
            "metrics": metrics(field),
            "unnormalized_sum_initial": sums[0],
            "unnormalized_sum_final": sums[-1],
            "sum_ratio_final_to_initial": sums[-1] / sums[0],
            "sum_min": min(sums),
            "sum_max": max(sums),
        }
    reference = fields["lattice_step5_diffuse"]
    result["relative_L2_from_lattice_step5_diffuse"] = {
        name: relative_l2(reference, field) for name, field in fields.items()
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

```

Full reference output:

```json
{
  "cases": {
    "lattice_step4_diffuse": {
      "metrics": {
        "fourfold_power_anisotropy": 0.8397233090504599,
        "fraction_above_0_99": 0.014214409722222222,
        "gradient_energy": 2.3931181658554124e-06,
        "histogram_entropy_bits_max8": 6.178288849604806,
        "low_frequency_power_fraction": 0.9568318186144196,
        "mean": 0.8765373826026917,
        "std": 0.07500865310430527,
        "twofold_power_anisotropy": 2.0227853548606114e-10
      },
      "sum_max": 31043.748046875,
      "sum_min": 2304.0,
      "sum_ratio_final_to_initial": 13.473848978678385,
      "unnormalized_sum_final": 31043.748046875,
      "unnormalized_sum_initial": 2304.0
    },
    "lattice_step5_diffuse": {
      "metrics": {
        "fourfold_power_anisotropy": 0.8397233197054805,
        "fraction_above_0_99": 0.014214409722222222,
        "gradient_energy": 2.3931381747388514e-06,
        "histogram_entropy_bits_max8": 6.178288849604806,
        "low_frequency_power_fraction": 0.9568316274970509,
        "mean": 0.8765373826026917,
        "std": 0.07500869780778885,
        "twofold_power_anisotropy": 5.151685625742397e-10
      },
      "sum_max": 31043.74609375,
      "sum_min": 1521.0,
      "sum_ratio_final_to_initial": 20.410089476495727,
      "unnormalized_sum_final": 31043.74609375,
      "unnormalized_sum_initial": 1521.0
    },
    "lattice_step5_diffuse_shuffled_scales": {
      "metrics": {
        "fourfold_power_anisotropy": 0.6825744960004119,
        "fraction_above_0_99": 0.0018988715277777778,
        "gradient_energy": 8.598610293120146e-05,
        "histogram_entropy_bits_max8": 7.149652398253605,
        "low_frequency_power_fraction": 0.9528419882639602,
        "mean": 0.5873393416404724,
        "std": 0.14952081441879272,
        "twofold_power_anisotropy": -1.2914047920238734e-10
      },
      "sum_max": 27955.12890625,
      "sum_min": 1521.0,
      "sum_ratio_final_to_initial": 13.662204398833005,
      "unnormalized_sum_final": 20780.212890625,
      "unnormalized_sum_initial": 1521.0
    },
    "lattice_step5_wave": {
      "metrics": {
        "fourfold_power_anisotropy": 0.715729974477162,
        "fraction_above_0_99": 2.712673611111111e-05,
        "gradient_energy": 0.00023175455862656236,
        "histogram_entropy_bits_max8": 6.460800586348542,
        "low_frequency_power_fraction": 0.9330646616360697,
        "mean": 0.19068671762943268,
        "std": 0.09042205661535263,
        "twofold_power_anisotropy": 5.623879113559638e-17
      },
      "sum_max": 9496.5615234375,
      "sum_min": 1521.0,
      "sum_ratio_final_to_initial": 4.621614133896285,
      "unnormalized_sum_final": 7029.47509765625,
      "unnormalized_sum_initial": 1521.0
    },
    "lattice_step6_diffuse": {
      "metrics": {
        "fourfold_power_anisotropy": 0.8397233365500669,
        "fraction_above_0_99": 0.014214409722222222,
        "gradient_energy": 2.393150907664676e-06,
        "histogram_entropy_bits_max8": 6.178288849604806,
        "low_frequency_power_fraction": 0.9568315023485555,
        "mean": 0.8765373826026917,
        "std": 0.07500872761011124,
        "twofold_power_anisotropy": 7.797286089887536e-10
      },
      "sum_max": 31043.74609375,
      "sum_min": 1024.0,
      "sum_ratio_final_to_initial": 30.316158294677734,
      "unnormalized_sum_final": 31043.74609375,
      "unnormalized_sum_initial": 1024.0
    },
    "random_same_density_diffuse": {
      "metrics": {
        "fourfold_power_anisotropy": 0.8701446340349552,
        "fraction_above_0_99": 0.005099826388888889,
        "gradient_energy": 5.0762253522407264e-05,
        "histogram_entropy_bits_max8": 7.244492134790721,
        "low_frequency_power_fraction": 0.9289828356485665,
        "mean": 0.7567093372344971,
        "std": 0.17100019752979279,
        "twofold_power_anisotropy": 0.7911013313518602
      },
      "sum_max": 25782.220703125,
      "sum_min": 1440.0,
      "sum_ratio_final_to_initial": 17.785636393229165,
      "unnormalized_sum_final": 25611.31640625,
      "unnormalized_sum_initial": 1440.0
    }
  },
  "iterations": 192,
  "relative_L2_from_lattice_step5_diffuse": {
    "lattice_step4_diffuse": 2.625390000640522e-07,
    "lattice_step5_diffuse": 0.0,
    "lattice_step5_diffuse_shuffled_scales": 0.34489327808584586,
    "lattice_step5_wave": 0.78066911274231,
    "lattice_step6_diffuse": 1.5893637911601955e-07,
    "random_same_density_diffuse": 0.27203338047702086
  },
  "schema": "lineum.oea-ablation-audit.v1",
  "seed": 20260715,
  "size": 192
}
```
---

## Appendix D — Band-Limited Wavefront Distortion

This appendix reproduces the direct test from Section 5.8 without random numbers. The circular spectrum, all operators, metrics, resolution control, bandwidth sensitivity, and complete structured output are embedded here.

```python
import json
import platform

import numpy as np


def clean(value):
    return float(f"{float(value):.12g}")


def simulate(n, sigma_ratio, time=20.0):
    k = 2.0 * np.pi * np.fft.fftfreq(n)
    kx, ky = np.meshgrid(k, k, indexing="ij")
    radius_k = np.hypot(kx, ky)
    operators = {
        "LAP4": 2.0 * np.cos(kx) + 2.0 * np.cos(ky) - 4.0,
        "LAP8_normalized": (2.0 / 3.0)
        * (
            2.0 * (np.cos(kx) + np.cos(ky))
            + np.cos(kx) * np.cos(ky)
            - 5.0
        ),
        "spectral": -(radius_k**2),
    }
    x = np.arange(n) - n // 2
    xx, yy = np.meshgrid(x, x, indexing="ij")
    radius_x = np.hypot(xx, yy)
    theta = np.arctan2(yy, xx)

    result = {}
    for k_ratio in (0.1, 0.25, 0.5):
        spectrum = np.exp(
            -0.5
            * ((radius_k - k_ratio * np.pi) / (sigma_ratio * np.pi)) ** 2
        )
        spectrum[radius_k > 0.9 * np.pi] = 0.0
        by_operator = {}
        for name, symbol in operators.items():
            psi = np.fft.fftshift(
                np.fft.ifft2(spectrum * np.exp(1j * symbol * time))
            )
            probability = np.abs(psi) ** 2
            probability /= probability.sum()
            radial_weight = probability * radius_x**2
            c4 = np.sum(radial_weight * np.exp(4j * theta)) / radial_weight.sum()
            by_operator[name] = {
                "c4_signed": clean(c4.real),
                "a4_abs": clean(abs(c4)),
                "r_rms": clean(np.sqrt(np.sum(probability * radius_x**2))),
                "boundary_tail_r_gt_0_4N": clean(
                    probability[radius_x > 0.4 * n].sum()
                ),
                "norm_error": clean(abs(probability.sum() - 1.0)),
            }
        result[str(k_ratio)] = by_operator
    return result


reference = simulate(512, 0.035)
initial = simulate(512, 0.035, time=0.0)
sensitivity_runs = {
    str(sigma): simulate(512, sigma) for sigma in (0.025, 0.035, 0.05)
}
resolution_256 = simulate(256, 0.035)

sensitivity = {}
for k_ratio in ("0.1", "0.25", "0.5"):
    sensitivity[k_ratio] = {}
    for operator in ("LAP4", "LAP8_normalized", "spectral"):
        values = [
            sensitivity_runs[sigma][k_ratio][operator]["a4_abs"]
            for sigma in sensitivity_runs
        ]
        sensitivity[k_ratio][operator] = {
            "min_a4": clean(min(values)),
            "max_a4": clean(max(values)),
        }

resolution_deltas = []
for k_ratio in reference:
    for operator in reference[k_ratio]:
        resolution_deltas.append(
            abs(
                reference[k_ratio][operator]["a4_abs"]
                - resolution_256[k_ratio][operator]["a4_abs"]
            )
        )

payload = {
    "schema": "lineum.wavefront-anisotropy.v1",
    "runtime": {"python": platform.python_version(), "numpy": np.__version__},
    "method": {
        "grid_reference": 512,
        "grid_resolution_control": 256,
        "time": 20.0,
        "k0_over_pi": [0.1, 0.25, 0.5],
        "sigma_k_over_pi_reference": 0.035,
        "sigma_k_over_pi_sensitivity": [0.025, 0.035, 0.05],
        "hard_radial_spectral_cutoff_over_pi": 0.9,
        "metric": "c4=sum(r^2 p exp(4 i theta))/sum(r^2 p)",
        "seed": None,
    },
    "initial_a4": {
        k_ratio: initial[k_ratio]["spectral"]["a4_abs"] for k_ratio in initial
    },
    "reference": reference,
    "sensitivity_sigma": sensitivity,
    "max_abs_a4_delta_N256_vs_N512": clean(max(resolution_deltas)),
    "max_reference_boundary_tail": clean(
        max(
            reference[k_ratio][operator]["boundary_tail_r_gt_0_4N"]
            for k_ratio in reference
            for operator in reference[k_ratio]
        )
    ),
}

canonical = json.dumps(payload, indent=2, sort_keys=True)
print(canonical)
```

```json
{
  "initial_a4": {
    "0.1": 0.000286885533085,
    "0.25": 0.000718419225729,
    "0.5": 0.00143683845146
  },
  "max_abs_a4_delta_N256_vs_N512": 3.289475666e-07,
  "max_reference_boundary_tail": 1.66018002885e-09,
  "method": {
    "grid_reference": 512,
    "grid_resolution_control": 256,
    "hard_radial_spectral_cutoff_over_pi": 0.9,
    "k0_over_pi": [
      0.1,
      0.25,
      0.5
    ],
    "metric": "c4=sum(r^2 p exp(4 i theta))/sum(r^2 p)",
    "seed": null,
    "sigma_k_over_pi_reference": 0.035,
    "sigma_k_over_pi_sensitivity": [
      0.025,
      0.035,
      0.05
    ],
    "time": 20.0
  },
  "reference": {
    "0.1": {
      "LAP4": {
        "a4_abs": 0.011509378309,
        "boundary_tail_r_gt_0_4N": 1.66018002664e-09,
        "c4_signed": -0.011509378309,
        "norm_error": 2.22044604925e-16,
        "r_rms": 14.8962780298
      },
      "LAP8_normalized": {
        "a4_abs": 6.58623222074e-05,
        "boundary_tail_r_gt_0_4N": 1.66018002593e-09,
        "c4_signed": -6.58623222074e-05,
        "norm_error": 3.33066907388e-16,
        "r_rms": 14.826212229
      },
      "spectral": {
        "a4_abs": 7.96977931156e-06,
        "boundary_tail_r_gt_0_4N": 1.66018002885e-09,
        "c4_signed": 7.96977931156e-06,
        "norm_error": 0.0,
        "r_rms": 15.1091686059
      }
    },
    "0.25": {
      "LAP4": {
        "a4_abs": 0.0810495797297,
        "boundary_tail_r_gt_0_4N": 9.15030213355e-28,
        "c4_signed": -0.0810495797297,
        "norm_error": 0.0,
        "r_rms": 30.0356047161
      },
      "LAP8_normalized": {
        "a4_abs": 0.00217717689466,
        "boundary_tail_r_gt_0_4N": 9.16991923707e-28,
        "c4_signed": -0.00217717689466,
        "norm_error": 3.33066907388e-16,
        "r_rms": 29.2424445
      },
      "spectral": {
        "a4_abs": 1.29363378461e-09,
        "boundary_tail_r_gt_0_4N": 9.11116972493e-28,
        "c4_signed": 1.29363378461e-09,
        "norm_error": 2.22044604925e-16,
        "r_rms": 32.5166520756
      }
    },
    "0.5": {
      "LAP4": {
        "a4_abs": 0.355246504463,
        "boundary_tail_r_gt_0_4N": 7.52668974191e-30,
        "c4_signed": -0.355246504463,
        "norm_error": 0.0,
        "r_rms": 46.087202956
      },
      "LAP8_normalized": {
        "a4_abs": 0.0385797365023,
        "boundary_tail_r_gt_0_4N": 8.23081953338e-30,
        "c4_signed": -0.0385797365023,
        "norm_error": 0.0,
        "r_rms": 41.0656117326
      },
      "spectral": {
        "a4_abs": 2.37606208548e-17,
        "boundary_tail_r_gt_0_4N": 2.08855298564e-29,
        "c4_signed": -2.37212444646e-17,
        "norm_error": 2.22044604925e-16,
        "r_rms": 63.3893838315
      }
    }
  },
  "runtime": {
    "numpy": "1.26.4",
    "python": "3.11.15"
  },
  "schema": "lineum.wavefront-anisotropy.v1",
  "sensitivity_sigma": {
    "0.1": {
      "LAP4": {
        "max_a4": 0.0178438534179,
        "min_a4": 0.00806505084303
      },
      "LAP8_normalized": {
        "max_a4": 0.000155598650137,
        "min_a4": 2.83851651566e-05
      },
      "spectral": {
        "max_a4": 1.22214158336e-05,
        "min_a4": 2.41202896414e-06
      }
    },
    "0.25": {
      "LAP4": {
        "max_a4": 0.0883481358742,
        "min_a4": 0.0751578003249
      },
      "LAP8_normalized": {
        "max_a4": 0.00259285745523,
        "min_a4": 0.00192529754097
      },
      "spectral": {
        "max_a4": 5.77357381125e-08,
        "min_a4": 6.30077954504e-11
      }
    },
    "0.5": {
      "LAP4": {
        "max_a4": 0.363526990029,
        "min_a4": 0.346451655377
      },
      "LAP8_normalized": {
        "max_a4": 0.04042372096,
        "min_a4": 0.0370798583377
      },
      "spectral": {
        "max_a4": 1.04813625951e-15,
        "min_a4": 2.37606208548e-17
      }
    }
  }
}
```


## Appendix E — Gate-0 Continuous-Time Decision Suite

This appendix independently reconstructs the deterministic `RD-0-C1` time-scaled candidate, its Fourier, boundary, nonuniform-medium, and stability controls, and the current stochastic source semantics. Save the program as `gate0_time_decision.py` and run it with Python 3 and NumPy.

### E.1 Complete executable program

**Embedded program SHA-256:** `2208d7c491173e24aa3d552527f221a268b59d29f333c79cabe6454fdf9dcc7e`

```python
"""Standalone deterministic and stochastic time-semantics decision suite."""

import json

import numpy as np


SIZE = 32
PHYSICAL_TIME = 10.0
TIME_STEPS = (0.2, 0.1, 0.05, 0.025)
D_PHI = 0.05
PHI_LAPLACE_RATE = 0.05
PHI_ALPHA = D_PHI * PHI_LAPLACE_RATE

STOCHASTIC_SIZE = 8
STOCHASTIC_TIME = 2.0
STOCHASTIC_SEEDS = 128
NOISE_SIGMA = 0.005


def weighted_laplace(field, kappa, rate):
    k_up = np.roll(kappa, 1, axis=0)
    k_down = np.roll(kappa, -1, axis=0)
    k_left = np.roll(kappa, 1, axis=1)
    k_right = np.roll(kappa, -1, axis=1)
    f_up = np.roll(field, 1, axis=0)
    f_down = np.roll(field, -1, axis=0)
    f_left = np.roll(field, 1, axis=1)
    f_right = np.roll(field, -1, axis=1)
    neighbors = (
        f_up * k_up
        + f_down * k_down
        + f_left * k_left
        + f_right * k_right
    )
    active = k_up + k_down + k_left + k_right
    return rate * (neighbors - active * field)


def mode(mode_x, mode_y, size=SIZE):
    y, x = np.mgrid[:size, :size]
    return np.cos(2 * np.pi * mode_x * x / size) * np.cos(
        2 * np.pi * mode_y * y / size
    )


def mode_amplitude(phi, spatial_mode):
    centered = phi - np.mean(phi)
    return float(
        np.sum(centered * spatial_mode) / np.sum(spatial_mode**2)
    )


def evolve_phi(phi, kappa, dt, physical_time=PHYSICAL_TIME):
    phi = phi.copy()
    for _ in range(round(physical_time / dt)):
        phi += (
            dt
            * kappa
            * D_PHI
            * weighted_laplace(phi, kappa, PHI_LAPLACE_RATE)
        )
    return phi


def relative_to_reference(estimate, reference):
    return float(
        np.linalg.norm(estimate - reference)
        / (np.linalg.norm(reference) + 1e-30)
    )


multiple_modes = []
for mode_x, mode_y in ((1, 0), (1, 1), (2, 3), (8, 8)):
    spatial_mode = mode(mode_x, mode_y)
    initial_phi = 0.5 + 0.05 * spatial_mode
    final_phi = evolve_phi(initial_phi, np.ones_like(initial_phi), 0.1)
    observed = mode_amplitude(final_phi, spatial_mode) / 0.05
    eigenvalue = (
        2 * np.cos(2 * np.pi * mode_x / SIZE)
        + 2 * np.cos(2 * np.pi * mode_y / SIZE)
        - 4
    )
    expected = float(
        (1 + 0.1 * PHI_ALPHA * eigenvalue)
        ** round(PHYSICAL_TIME / 0.1)
    )
    multiple_modes.append(
        {
            "mode": [mode_x, mode_y],
            "lap4_eigenvalue": float(eigenvalue),
            "observed_amplitude_ratio": observed,
            "analytic_amplitude_ratio": expected,
            "absolute_error": abs(observed - expected),
        }
    )


edge_phi = np.full((SIZE, SIZE), 0.5, dtype=np.float64)
edge_phi[0, 0] += 0.1
edge_after = evolve_phi(edge_phi, np.ones_like(edge_phi), 0.1, 0.1)
edge_delta = edge_after - edge_phi
periodic_edge = {
    "center_delta": float(edge_delta[0, 0]),
    "down_neighbor_delta": float(edge_delta[1, 0]),
    "up_wrapped_neighbor_delta": float(edge_delta[-1, 0]),
    "right_neighbor_delta": float(edge_delta[0, 1]),
    "left_wrapped_neighbor_delta": float(edge_delta[0, -1]),
}


y, x = np.mgrid[:SIZE, :SIZE]
nonuniform_phi = 0.5 + 0.08 * mode(2, 1)
nonuniform_kappa = 0.6 + 0.3 * np.cos(2 * np.pi * x / SIZE) * np.cos(
    2 * np.pi * y / SIZE
)
nonuniform_states = {
    dt: evolve_phi(nonuniform_phi, nonuniform_kappa, dt)
    for dt in TIME_STEPS
}
nonuniform_errors = []
for coarse, fine in zip(TIME_STEPS, TIME_STEPS[1:]):
    nonuniform_errors.append(
        {
            "coarse_dt": coarse,
            "fine_dt": fine,
            "phi_relative_l2": relative_to_reference(
                nonuniform_states[coarse], nonuniform_states[fine]
            ),
        }
    )


checkerboard = mode(SIZE // 2, SIZE // 2)
stability = []
for dt in (99.0, 101.0):
    initial_phi = 0.5 + 0.1 * checkerboard
    final_phi = evolve_phi(initial_phi, np.ones_like(initial_phi), dt, dt)
    stability.append(
        {
            "dt": dt,
            "amplitude_ratio_after_one_step": mode_amplitude(
                final_phi, checkerboard
            )
            / 0.1,
        }
    )


def stochastic_run(dt, seed, initial_psi, physical_time):
    np.random.seed(seed)
    psi = initial_psi.astype(np.complex128).copy()
    kappa = np.ones((STOCHASTIC_SIZE, STOCHASTIC_SIZE), dtype=np.float64)
    for _ in range(round(physical_time / dt)):
        amplitude = np.abs(psi)
        grad_x, grad_y = np.gradient(amplitude)
        grad_magnitude = np.sqrt(grad_x**2 + grad_y**2)
        probability = 1.0 / (
            1.0 + np.exp(-5.0 * (amplitude + grad_magnitude))
        )
        linons = (
            np.random.rand(STOCHASTIC_SIZE, STOCHASTIC_SIZE) < probability
        ).astype(np.float64)
        linon_effect = (0.03 + 0.02 * amplitude) * linons
        phase = np.exp(1j * np.angle(psi))
        linon_complex = linon_effect * phase
        fluctuation = np.clip(
            np.random.normal(
                0.0,
                NOISE_SIGMA,
                (STOCHASTIC_SIZE, STOCHASTIC_SIZE),
            ),
            -1.0,
            1.0,
        ) * phase
        psi += (linon_complex + fluctuation) * kappa * dt
        psi -= 0.005 * psi * dt
    return psi


stochastic_rows = []
vacuum_ensembles = {}
vacuum = np.zeros(
    (STOCHASTIC_SIZE, STOCHASTIC_SIZE), dtype=np.complex128
)
for dt in TIME_STEPS:
    ensemble = np.stack(
        [
            stochastic_run(dt, seed, vacuum, STOCHASTIC_TIME)
            for seed in range(STOCHASTIC_SEEDS)
        ]
    )
    vacuum_ensembles[dt] = ensemble
    per_seed_spatial_mean = np.mean(ensemble.real, axis=(1, 2))
    cellwise_ensemble_std = np.std(ensemble.real, axis=0, ddof=1)
    cellwise_complex_std = np.sqrt(
        np.var(ensemble.real, axis=0, ddof=1)
        + np.var(ensemble.imag, axis=0, ddof=1)
    )
    stochastic_rows.append(
        {
            "dt": dt,
            "steps": round(STOCHASTIC_TIME / dt),
            "ensemble_mean_spatial_mean_real_psi": float(
                np.mean(per_seed_spatial_mean)
            ),
            "ensemble_std_spatial_mean_real_psi": float(
                np.std(per_seed_spatial_mean, ddof=1)
            ),
            "mean_cellwise_ensemble_std_real_psi": float(
                np.mean(cellwise_ensemble_std)
            ),
            "mean_cellwise_ensemble_std_complex_psi": float(
                np.mean(cellwise_complex_std)
            ),
            "ensemble_mean_total_psi_energy": float(
                np.mean(np.sum(np.abs(ensemble) ** 2, axis=(1, 2)))
            ),
        }
    )


branch_y, branch_x = np.mgrid[:STOCHASTIC_SIZE, :STOCHASTIC_SIZE]
branch_initial = 0.02 * np.exp(1j * (0.2 * branch_x - 0.1 * branch_y))
branch_rows = []
branch_ensembles = {}
for dt in TIME_STEPS:
    ensemble = np.stack(
        [
            stochastic_run(dt, seed, branch_initial, 1.0)
            for seed in range(STOCHASTIC_SEEDS)
        ]
    )
    branch_ensembles[dt] = ensemble
    cellwise_complex_std = np.sqrt(
        np.var(ensemble.real, axis=0, ddof=1)
        + np.var(ensemble.imag, axis=0, ddof=1)
    )
    ensemble_mean = np.mean(ensemble, axis=0)
    branch_rows.append(
        {
            "dt": dt,
            "steps": round(1.0 / dt),
            "mean_cellwise_ensemble_std_complex_psi": float(
                np.mean(cellwise_complex_std)
            ),
            "ensemble_mean_total_psi_energy": float(
                np.sum(np.abs(ensemble_mean) ** 2)
            ),
        }
    )


def mean_cellwise_complex_std(ensemble):
    return float(
        np.mean(
            np.sqrt(
                np.var(ensemble.real, axis=0, ddof=1)
                + np.var(ensemble.imag, axis=0, ddof=1)
            )
        )
    )


bootstrap_rng = np.random.default_rng(20260716)
bootstrap_repetitions = 1000
vacuum_bootstrap_factors = [[], [], []]
branch_bootstrap_factors = [[], [], []]
for _ in range(bootstrap_repetitions):
    indices = bootstrap_rng.integers(
        0, STOCHASTIC_SEEDS, size=STOCHASTIC_SEEDS
    )
    vacuum_spreads = [
        mean_cellwise_complex_std(vacuum_ensembles[dt][indices])
        for dt in TIME_STEPS
    ]
    branch_spreads = [
        mean_cellwise_complex_std(branch_ensembles[dt][indices])
        for dt in TIME_STEPS
    ]
    for index in range(3):
        vacuum_bootstrap_factors[index].append(
            vacuum_spreads[index] / vacuum_spreads[index + 1]
        )
        branch_bootstrap_factors[index].append(
            branch_spreads[index] / branch_spreads[index + 1]
        )


def bootstrap_intervals(samples):
    return [
        {
            "lower_95": float(np.percentile(values, 2.5)),
            "upper_95": float(np.percentile(values, 97.5)),
        }
        for values in samples
    ]


source_only_control = []
probability = 0.5
linon_amplitude = 0.03
source_variance = (
    linon_amplitude**2 * probability * (1 - probability)
    + NOISE_SIGMA**2
)
for dt in TIME_STEPS:
    source_only_control.append(
        {
            "dt": dt,
            "expected_final_mean": STOCHASTIC_TIME
            * probability
            * linon_amplitude,
            "expected_final_std_current_dt_scaling": float(
                np.sqrt(STOCHASTIC_TIME * dt * source_variance)
            ),
            "expected_final_std_sde_sqrt_dt_scaling": float(
                np.sqrt(STOCHASTIC_TIME) * NOISE_SIGMA
            ),
        }
    )


low_mode_eigenvalue = 4 * np.cos(2 * np.pi / SIZE) - 4
output = {
    "configuration": {
        "deterministic_grid_size": SIZE,
        "deterministic_physical_time": PHYSICAL_TIME,
        "time_steps": list(TIME_STEPS),
        "stochastic_grid_size": STOCHASTIC_SIZE,
        "stochastic_physical_time": STOCHASTIC_TIME,
        "stochastic_seed_count": STOCHASTIC_SEEDS,
    },
    "deterministic_candidate": {
        "multiple_fourier_modes": multiple_modes,
        "periodic_edge": periodic_edge,
        "nonuniform_kappa_pairwise_refinement": nonuniform_errors,
        "nonuniform_kappa_error_reduction_factors": [
            nonuniform_errors[0]["phi_relative_l2"]
            / nonuniform_errors[1]["phi_relative_l2"],
            nonuniform_errors[1]["phi_relative_l2"]
            / nonuniform_errors[2]["phi_relative_l2"],
        ],
        "uniform_checkerboard_stability": stability,
        "predicted_uniform_lap4_max_stable_dt": 2
        / (8 * PHI_ALPHA),
    },
    "stochastic_current_runtime_semantics": {
        "ensemble_results": stochastic_rows,
        "cellwise_std_reduction_factors_when_dt_halves": [
            stochastic_rows[0]["mean_cellwise_ensemble_std_complex_psi"]
            / stochastic_rows[1]["mean_cellwise_ensemble_std_complex_psi"],
            stochastic_rows[1]["mean_cellwise_ensemble_std_complex_psi"]
            / stochastic_rows[2]["mean_cellwise_ensemble_std_complex_psi"],
            stochastic_rows[2]["mean_cellwise_ensemble_std_complex_psi"]
            / stochastic_rows[3]["mean_cellwise_ensemble_std_complex_psi"],
        ],
        "common_nonzero_state_branching": branch_rows,
        "branching_std_reduction_factors_when_dt_halves": [
            branch_rows[0]["mean_cellwise_ensemble_std_complex_psi"]
            / branch_rows[1]["mean_cellwise_ensemble_std_complex_psi"],
            branch_rows[1]["mean_cellwise_ensemble_std_complex_psi"]
            / branch_rows[2]["mean_cellwise_ensemble_std_complex_psi"],
            branch_rows[2]["mean_cellwise_ensemble_std_complex_psi"]
            / branch_rows[3]["mean_cellwise_ensemble_std_complex_psi"],
        ],
        "branching_std_reduction_factor_bootstrap_95": bootstrap_intervals(
            branch_bootstrap_factors
        ),
        "vacuum_std_reduction_factor_bootstrap_95": bootstrap_intervals(
            vacuum_bootstrap_factors
        ),
        "bootstrap_repetitions": bootstrap_repetitions,
        "source_only_analytic_control": source_only_control,
    },
    "internal_rate_examples": {
        "global_psi_damping_time_constant": 1 / 0.005,
        "low_mode_psi_diffusion_time_constant_at_kappa_1": float(
            1 / (0.05 * abs(low_mode_eigenvalue))
        ),
        "low_mode_phi_diffusion_time_constant_at_kappa_1": float(
            1 / (PHI_ALPHA * abs(low_mode_eigenvalue))
        ),
    },
}

print(json.dumps(output, indent=2, sort_keys=True))
```

### E.2 Full reference output

**Normalized execution-output SHA-256:** `a2d508368032cea8ba25c9970e0dc37a83d597101ce844005bf8d5a6515b9e6e`

```json
{
  "configuration": {
    "deterministic_grid_size": 32,
    "deterministic_physical_time": 10.0,
    "stochastic_grid_size": 8,
    "stochastic_physical_time": 2.0,
    "stochastic_seed_count": 128,
    "time_steps": [
      0.2,
      0.1,
      0.05,
      0.025
    ]
  },
  "deterministic_candidate": {
    "multiple_fourier_modes": [
      {
        "absolute_error": 1.2212453270876722e-15,
        "analytic_amplitude_ratio": 0.9990397207685476,
        "lap4_eigenvalue": -0.03842943919353914,
        "mode": [
          1,
          0
        ],
        "observed_amplitude_ratio": 0.9990397207685489
      },
      {
        "absolute_error": 4.440892098500626e-16,
        "analytic_amplitude_ratio": 0.998080354460703,
        "lap4_eigenvalue": -0.07685887838707828,
        "mode": [
          1,
          1
        ],
        "observed_amplitude_ratio": 0.9980803544607025
      },
      {
        "absolute_error": 6.994405055138486e-15,
        "analytic_amplitude_ratio": 0.9878412315137362,
        "lap4_eigenvalue": -0.4893017103723363,
        "mode": [
          2,
          3
        ],
        "observed_amplitude_ratio": 0.9878412315137292
      },
      {
        "absolute_error": 6.661338147750939e-16,
        "analytic_amplitude_ratio": 0.9047921471137089,
        "lap4_eigenvalue": -3.9999999999999996,
        "mode": [
          8,
          8
        ],
        "observed_amplitude_ratio": 0.9047921471137096
      }
    ],
    "nonuniform_kappa_error_reduction_factors": [
      2.000131472537297,
      2.0000659448645504
    ],
    "nonuniform_kappa_pairwise_refinement": [
      {
        "coarse_dt": 0.2,
        "fine_dt": 0.1,
        "phi_relative_l2": 3.4681650239936567e-09
      },
      {
        "coarse_dt": 0.1,
        "fine_dt": 0.05,
        "phi_relative_l2": 1.733968527375885e-09
      },
      {
        "coarse_dt": 0.05,
        "fine_dt": 0.025,
        "phi_relative_l2": 8.669556780505624e-10
      }
    ],
    "periodic_edge": {
      "center_delta": -9.999999999998899e-05,
      "down_neighbor_delta": 2.5000000000052758e-05,
      "left_wrapped_neighbor_delta": 2.5000000000052758e-05,
      "right_neighbor_delta": 2.5000000000052758e-05,
      "up_wrapped_neighbor_delta": 2.5000000000052758e-05
    },
    "predicted_uniform_lap4_max_stable_dt": 99.99999999999999,
    "uniform_checkerboard_stability": [
      {
        "amplitude_ratio_after_one_step": -0.9799999999999994,
        "dt": 99.0
      },
      {
        "amplitude_ratio_after_one_step": -1.0199999999999994,
        "dt": 101.0
      }
    ]
  },
  "internal_rate_examples": {
    "global_psi_damping_time_constant": 200.0,
    "low_mode_phi_diffusion_time_constant_at_kappa_1": 5204.343445990867,
    "low_mode_psi_diffusion_time_constant_at_kappa_1": 260.2171722995434
  },
  "stochastic_current_runtime_semantics": {
    "bootstrap_repetitions": 1000,
    "branching_std_reduction_factor_bootstrap_95": [
      {
        "lower_95": 1.380100685682375,
        "upper_95": 1.421757148019419
      },
      {
        "lower_95": 1.387459161864581,
        "upper_95": 1.4308822629478066
      },
      {
        "lower_95": 1.3887844422350775,
        "upper_95": 1.4349241478590746
      }
    ],
    "branching_std_reduction_factors_when_dt_halves": [
      1.4013622492053581,
      1.408187849410732,
      1.4121621526410548
    ],
    "cellwise_std_reduction_factors_when_dt_halves": [
      1.0292085935227464,
      1.0188710590442107,
      1.0100934078383172
    ],
    "common_nonzero_state_branching": [
      {
        "dt": 0.2,
        "ensemble_mean_total_psi_energy": 0.08529647704710092,
        "mean_cellwise_ensemble_std_complex_psi": 0.007258234066983663,
        "steps": 5
      },
      {
        "dt": 0.1,
        "ensemble_mean_total_psi_energy": 0.084696643068043,
        "mean_cellwise_ensemble_std_complex_psi": 0.005179413153950338,
        "steps": 10
      },
      {
        "dt": 0.05,
        "ensemble_mean_total_psi_energy": 0.0845031895276381,
        "mean_cellwise_ensemble_std_complex_psi": 0.0036780697661307803,
        "steps": 20
      },
      {
        "dt": 0.025,
        "ensemble_mean_total_psi_energy": 0.08428553361262872,
        "mean_cellwise_ensemble_std_complex_psi": 0.002604566167739291,
        "steps": 40
      }
    ],
    "ensemble_results": [
      {
        "dt": 0.2,
        "ensemble_mean_spatial_mean_real_psi": 0.01787051141925871,
        "ensemble_mean_total_psi_energy": 0.07378548000540894,
        "ensemble_std_spatial_mean_real_psi": 0.0035329295364034887,
        "mean_cellwise_ensemble_std_complex_psi": 0.02881458225082336,
        "mean_cellwise_ensemble_std_real_psi": 0.02881458225082336,
        "steps": 10
      },
      {
        "dt": 0.1,
        "ensemble_mean_spatial_mean_real_psi": 0.017066526935238868,
        "ensemble_mean_total_psi_energy": 0.06904762936513884,
        "ensemble_std_spatial_mean_real_psi": 0.0034087546062588786,
        "mean_cellwise_ensemble_std_complex_psi": 0.027996834103568465,
        "mean_cellwise_ensemble_std_real_psi": 0.027996834103568465,
        "steps": 20
      },
      {
        "dt": 0.05,
        "ensemble_mean_spatial_mean_real_psi": 0.016603226985407026,
        "ensemble_mean_total_psi_energy": 0.06621789351723734,
        "ensemble_std_spatial_mean_real_psi": 0.0033186245019622956,
        "mean_cellwise_ensemble_std_complex_psi": 0.02747828967664654,
        "mean_cellwise_ensemble_std_real_psi": 0.02747828967664654,
        "steps": 40
      },
      {
        "dt": 0.025,
        "ensemble_mean_spatial_mean_real_psi": 0.01641395396640176,
        "ensemble_mean_total_psi_energy": 0.06487020763061033,
        "ensemble_std_spatial_mean_real_psi": 0.003285649392178308,
        "mean_cellwise_ensemble_std_complex_psi": 0.02720371152154367,
        "mean_cellwise_ensemble_std_real_psi": 0.02720371152154367,
        "steps": 80
      }
    ],
    "source_only_analytic_control": [
      {
        "dt": 0.2,
        "expected_final_mean": 0.03,
        "expected_final_std_current_dt_scaling": 0.01,
        "expected_final_std_sde_sqrt_dt_scaling": 0.007071067811865476
      },
      {
        "dt": 0.1,
        "expected_final_mean": 0.03,
        "expected_final_std_current_dt_scaling": 0.007071067811865475,
        "expected_final_std_sde_sqrt_dt_scaling": 0.007071067811865476
      },
      {
        "dt": 0.05,
        "expected_final_mean": 0.03,
        "expected_final_std_current_dt_scaling": 0.005,
        "expected_final_std_sde_sqrt_dt_scaling": 0.007071067811865476
      },
      {
        "dt": 0.025,
        "expected_final_mean": 0.03,
        "expected_final_std_current_dt_scaling": 0.0035355339059327377,
        "expected_final_std_sde_sqrt_dt_scaling": 0.007071067811865476
      }
    ],
    "vacuum_std_reduction_factor_bootstrap_95": [
      {
        "lower_95": 1.0237213486317018,
        "upper_95": 1.0353375308393835
      },
      {
        "lower_95": 1.0144254432593718,
        "upper_95": 1.0234777396838273
      },
      {
        "lower_95": 1.007380788718166,
        "upper_95": 1.0128752595785082
      }
    ]
  }
}
```

## Appendix F — Open Stochastic-Contract Comparison

This appendix compares the current source with initial-only branching, Gaussian-SDE forcing, and Poisson-rate events. It includes every fixture, parameter, seed, metric, block-uncertainty calculation, and robustness condition used in the updated time assessment. Save the program as `stochastic_contract_comparison.py` and run it with Python 3 and NumPy.

### F.1 Complete executable program

**Embedded program SHA-256:** `46381f186273e8d95f81bd8d0d1c506ad7f09125ceb9ef3050540f1a5f6dfd25`

```python
"""Standalone comparison of candidate stochastic time contracts for Lineum."""

import json

import numpy as np


TIME_STEPS = (0.2, 0.1, 0.05, 0.025)
CONTRACTS = ("current", "initial_only", "gaussian_sde", "poisson_events")
PSI_DIFFUSION = 0.05
DAMPING = 0.005
CURRENT_NOISE_SIGMA = 0.005
INITIAL_SIGMA = 0.005
GAUSSIAN_SIGMA = 0.005
POISSON_RATE = 2.5
POISSON_JUMP = 0.01


def initial_fixture(size, kind):
    y, x = np.mgrid[:size, :size]
    phase = 0.2 * x - 0.1 * y
    if kind == "phase_gradient":
        amplitude = np.full((size, size), 0.02)
    elif kind == "packet":
        center = (size - 1) / 2
        radius_squared = (x - center) ** 2 + (y - center) ** 2
        amplitude = 0.015 + 0.015 * np.exp(
            -radius_squared / (2 * (size / 5) ** 2)
        )
    else:
        raise ValueError(kind)
    return amplitude * np.exp(1j * phase)


def lap4(field):
    return (
        np.roll(field, 1, axis=-2)
        + np.roll(field, -1, axis=-2)
        + np.roll(field, 1, axis=-1)
        + np.roll(field, -1, axis=-1)
        - 4 * field
    )


def deterministic_step(psi, dt):
    psi = psi - DAMPING * psi * dt
    return psi + PSI_DIFFUSION * lap4(psi) * dt


def current_source(psi, rng):
    amplitude = np.abs(psi)
    grad_y, grad_x = np.gradient(amplitude, axis=(-2, -1))
    grad_magnitude = np.sqrt(grad_x**2 + grad_y**2)
    probability = 1.0 / (
        1.0 + np.exp(-5.0 * (amplitude + grad_magnitude))
    )
    linons = (rng.rand(*psi.shape) < probability).astype(np.float64)
    linon_effect = np.clip((0.03 + 0.02 * amplitude) * linons, 0.0, 10.0)
    phase = np.exp(1j * np.angle(psi))
    fluctuation = np.clip(
        rng.normal(0.0, CURRENT_NOISE_SIGMA, psi.shape), -1.0, 1.0
    ) * phase
    return linon_effect * phase + fluctuation


def evolve_ensemble(contract, dt, physical_time, initial, seeds, seed):
    rng = np.random.RandomState(seed)
    psi = np.broadcast_to(initial, (seeds, *initial.shape)).astype(
        np.complex128
    ).copy()
    if contract == "initial_only":
        initial_rng = np.random.RandomState(seed)
        perturbation = (
            initial_rng.normal(size=psi.shape)
            + 1j * initial_rng.normal(size=psi.shape)
        ) / np.sqrt(2.0)
        psi += INITIAL_SIGMA * perturbation

    for _ in range(round(physical_time / dt)):
        if contract == "current":
            psi += current_source(psi, rng) * dt
        elif contract == "gaussian_sde":
            increment = (
                rng.normal(size=psi.shape) + 1j * rng.normal(size=psi.shape)
            ) / np.sqrt(2.0)
            psi += GAUSSIAN_SIGMA * np.sqrt(dt) * increment
        elif contract == "poisson_events":
            counts = rng.poisson(POISSON_RATE * dt, size=psi.shape)
            psi += POISSON_JUMP * counts * np.exp(1j * np.angle(psi))
        elif contract != "initial_only":
            raise ValueError(contract)
        psi = deterministic_step(psi, dt)
    return psi


def current_single_run(dt, seed, initial, physical_time):
    rng = np.random.RandomState(seed)
    psi = initial.astype(np.complex128).copy()
    for _ in range(round(physical_time / dt)):
        psi += current_source(psi, rng) * dt
        psi = deterministic_step(psi, dt)
    return psi


def rms_complex_spread(ensemble):
    mean = np.mean(ensemble, axis=0)
    return float(np.sqrt(np.mean(np.abs(ensemble - mean) ** 2)))


def mean_cellwise_complex_std(ensemble):
    variance = np.var(ensemble.real, axis=0, ddof=1) + np.var(
        ensemble.imag, axis=0, ddof=1
    )
    return float(np.mean(np.sqrt(variance)))


def scaling_exponent(rows):
    x = np.log([row["dt"] for row in rows])
    y = np.log([row["rms_complex_spread"] for row in rows])
    return float(np.polyfit(x, y, 1)[0])


def summarize_ensembles(ensembles):
    rows = []
    for dt in TIME_STEPS:
        ensemble = ensembles[dt]
        ensemble_mean = np.mean(ensemble, axis=0)
        rows.append(
            {
                "dt": dt,
                "steps": None,
                "rms_complex_spread": rms_complex_spread(ensemble),
                "mean_cellwise_complex_std": mean_cellwise_complex_std(
                    ensemble
                ),
                "ensemble_mean_energy": float(
                    np.sum(np.abs(ensemble_mean) ** 2)
                ),
                "ensemble_mean_spatial_real_psi": float(
                    np.mean(ensemble_mean.real)
                ),
            }
        )
    return {
        "rows": rows,
        "spread_reduction_factors_when_dt_halves": [
            rows[index]["rms_complex_spread"]
            / rows[index + 1]["rms_complex_spread"]
            for index in range(len(rows) - 1)
        ],
        "fitted_dt_power_exponent": scaling_exponent(rows),
    }


def block_exponent_interval(ensembles, block_size=64):
    seed_count = next(iter(ensembles.values())).shape[0]
    exponents = []
    for start in range(0, seed_count, block_size):
        stop = start + block_size
        block_rows = [
            {
                "dt": dt,
                "rms_complex_spread": rms_complex_spread(
                    ensembles[dt][start:stop]
                ),
            }
            for dt in TIME_STEPS
        ]
        exponents.append(scaling_exponent(block_rows))
    mean = float(np.mean(exponents))
    standard_error = float(np.std(exponents, ddof=1) / np.sqrt(len(exponents)))
    t_critical_df15 = 2.131449545559323
    return {
        "independent_seed_blocks": len(exponents),
        "seeds_per_block": block_size,
        "mean_exponent": mean,
        "lower_95_t_interval": mean - t_critical_df15 * standard_error,
        "upper_95_t_interval": mean + t_critical_df15 * standard_error,
        "minimum_block_exponent": float(np.min(exponents)),
        "maximum_block_exponent": float(np.max(exponents)),
    }


def run_condition(size, fixture, physical_time, seeds, seed_offset):
    initial = initial_fixture(size, fixture)
    results = {}
    for contract_index, contract in enumerate(CONTRACTS):
        ensembles = {}
        for dt_index, dt in enumerate(TIME_STEPS):
            ensemble_seed = seed_offset + contract_index * 100_000
            if contract != "initial_only":
                ensemble_seed += dt_index * 10_000
            ensembles[dt] = evolve_ensemble(
                contract,
                dt,
                physical_time,
                initial,
                seeds,
                ensemble_seed,
            )
        summary = summarize_ensembles(ensembles)
        for row in summary["rows"]:
            row["steps"] = round(physical_time / row["dt"])
        if seeds == 1024:
            summary["block_exponent_95"] = block_exponent_interval(ensembles)
        results[contract] = summary
    return results


base_amplitude = 0.02
base_probability = 1.0 / (1.0 + np.exp(-5.0 * base_amplitude))
base_linon_amplitude = 0.03 + 0.02 * base_amplitude
current_variance_rate_coefficient = (
    base_linon_amplitude**2 * base_probability * (1 - base_probability)
    + CURRENT_NOISE_SIGMA**2
)

analytic_source_only = {
    "current": [
        {
            "dt": dt,
            "expected_mean_at_T1": base_probability * base_linon_amplitude,
            "expected_std_at_T1": float(
                np.sqrt(dt * current_variance_rate_coefficient)
            ),
        }
        for dt in TIME_STEPS
    ],
    "initial_only": {
        "expected_std_without_dynamics_at_T1": INITIAL_SIGMA,
        "expected_dt_power_exponent": 0.0,
    },
    "gaussian_sde": {
        "expected_std_without_dynamics_at_T1": GAUSSIAN_SIGMA,
        "expected_dt_power_exponent": 0.0,
    },
    "poisson_events": {
        "expected_mean_at_T1": POISSON_RATE * POISSON_JUMP,
        "expected_std_at_T1": float(
            np.sqrt(POISSON_RATE) * POISSON_JUMP
        ),
        "expected_dt_power_exponent": 0.0,
    },
}


def compact_robustness(condition):
    return {
        contract: {
            "fitted_dt_power_exponent": summary[
                "fitted_dt_power_exponent"
            ],
            "rms_complex_spreads": [
                row["rms_complex_spread"] for row in summary["rows"]
            ],
            "spread_reduction_factors_when_dt_halves": summary[
                "spread_reduction_factors_when_dt_halves"
            ],
        }
        for contract, summary in condition.items()
    }


primary = run_condition(8, "phase_gradient", 1.0, 1024, 2_026_071_600)
packet_robustness = run_condition(8, "packet", 1.0, 256, 2_026_071_700)
grid_robustness = run_condition(
    16, "phase_gradient", 1.0, 256, 2_026_071_800
)
horizon_robustness = run_condition(
    8, "phase_gradient", 4.0, 256, 2_026_071_900
)

output = {
    "configuration": {
        "time_steps": list(TIME_STEPS),
        "psi_diffusion": PSI_DIFFUSION,
        "damping": DAMPING,
        "current_noise_sigma": CURRENT_NOISE_SIGMA,
        "initial_condition_sigma": INITIAL_SIGMA,
        "gaussian_sde_sigma": GAUSSIAN_SIGMA,
        "poisson_rate_per_cell_per_time": POISSON_RATE,
        "poisson_jump_amplitude": POISSON_JUMP,
    },
    "analytic_source_only": analytic_source_only,
    "primary_phase_gradient_grid8_T1_seeds1024": primary,
    "robustness_packet_grid8_T1_seeds256": compact_robustness(
        packet_robustness
    ),
    "robustness_phase_gradient_grid16_T1_seeds256": compact_robustness(
        grid_robustness
    ),
    "robustness_phase_gradient_grid8_T4_seeds256": compact_robustness(
        horizon_robustness
    ),
}

print(json.dumps(output, indent=2, sort_keys=True))
```

### F.2 Full reference output

**Normalized execution-output SHA-256:** `95b33e072da0f320e1e79d7e0b4676d5e5060f4ec90d3aced1bdadc84f52bc48`

```json
{
  "analytic_source_only": {
    "current": [
      {
        "dt": 0.2,
        "expected_mean_at_T1": 0.015959367299359775,
        "expected_std_at_T1": 0.007147913839780989
      },
      {
        "dt": 0.1,
        "expected_mean_at_T1": 0.015959367299359775,
        "expected_std_at_T1": 0.005054338347446311
      },
      {
        "dt": 0.05,
        "expected_mean_at_T1": 0.015959367299359775,
        "expected_std_at_T1": 0.0035739569198904946
      },
      {
        "dt": 0.025,
        "expected_mean_at_T1": 0.015959367299359775,
        "expected_std_at_T1": 0.0025271691737231553
      }
    ],
    "gaussian_sde": {
      "expected_dt_power_exponent": 0.0,
      "expected_std_without_dynamics_at_T1": 0.005
    },
    "initial_only": {
      "expected_dt_power_exponent": 0.0,
      "expected_std_without_dynamics_at_T1": 0.005
    },
    "poisson_events": {
      "expected_dt_power_exponent": 0.0,
      "expected_mean_at_T1": 0.025,
      "expected_std_at_T1": 0.0158113883008419
    }
  },
  "configuration": {
    "current_noise_sigma": 0.005,
    "damping": 0.005,
    "gaussian_sde_sigma": 0.005,
    "initial_condition_sigma": 0.005,
    "poisson_jump_amplitude": 0.01,
    "poisson_rate_per_cell_per_time": 2.5,
    "psi_diffusion": 0.05,
    "time_steps": [
      0.2,
      0.1,
      0.05,
      0.025
    ]
  },
  "primary_phase_gradient_grid8_T1_seeds1024": {
    "current": {
      "block_exponent_95": {
        "independent_seed_blocks": 16,
        "lower_95_t_interval": 0.4841855067201953,
        "maximum_block_exponent": 0.5023339044656487,
        "mean_exponent": 0.48835619010493936,
        "minimum_block_exponent": 0.4763282434792172,
        "seeds_per_block": 64,
        "upper_95_t_interval": 0.49252687348968344
      },
      "fitted_dt_power_exponent": 0.4883584910429441,
      "rows": [
        {
          "dt": 0.2,
          "ensemble_mean_energy": 0.08246842852465047,
          "ensemble_mean_spatial_real_psi": 0.029922558517219457,
          "mean_cellwise_complex_std": 0.006478956276162863,
          "rms_complex_spread": 0.006477012524774123,
          "steps": 5
        },
        {
          "dt": 0.1,
          "ensemble_mean_energy": 0.08242897851247968,
          "ensemble_mean_spatial_real_psi": 0.02990188677026183,
          "mean_cellwise_complex_std": 0.00463467871503456,
          "rms_complex_spread": 0.004633481607547739,
          "steps": 10
        },
        {
          "dt": 0.05,
          "ensemble_mean_energy": 0.08241677992007483,
          "ensemble_mean_spatial_real_psi": 0.029895560207200345,
          "mean_cellwise_complex_std": 0.0033099329282166266,
          "rms_complex_spread": 0.003309189397166538,
          "steps": 20
        },
        {
          "dt": 0.025,
          "ensemble_mean_energy": 0.08239833411531253,
          "ensemble_mean_spatial_real_psi": 0.029894412691645566,
          "mean_cellwise_complex_std": 0.002345081524964385,
          "rms_complex_spread": 0.002344596767140405,
          "steps": 40
        }
      ],
      "spread_reduction_factors_when_dt_halves": [
        1.3978716380838447,
        1.4001862847484987,
        1.4114108846113447
      ]
    },
    "gaussian_sde": {
      "block_exponent_95": {
        "independent_seed_blocks": 16,
        "lower_95_t_interval": -0.013698082559373425,
        "maximum_block_exponent": -0.00256055148190971,
        "mean_exponent": -0.010940959310200374,
        "minimum_block_exponent": -0.02107381467738071,
        "seeds_per_block": 64,
        "upper_95_t_interval": -0.008183836061027324
      },
      "fitted_dt_power_exponent": -0.010816373320071146,
      "rows": [
        {
          "dt": 0.2,
          "ensemble_mean_energy": 0.02467154571769403,
          "ensemble_mean_spatial_real_psi": 0.016362359491959043,
          "mean_cellwise_complex_std": 0.004428416695036037,
          "rms_complex_spread": 0.004426727569595373,
          "steps": 5
        },
        {
          "dt": 0.1,
          "ensemble_mean_energy": 0.024620861591628483,
          "ensemble_mean_spatial_real_psi": 0.01634169862028973,
          "mean_cellwise_complex_std": 0.004494887476495649,
          "rms_complex_spread": 0.004493112487890099,
          "steps": 10
        },
        {
          "dt": 0.05,
          "ensemble_mean_energy": 0.024663324384987993,
          "ensemble_mean_spatial_real_psi": 0.016348319778253857,
          "mean_cellwise_complex_std": 0.004521477164038717,
          "rms_complex_spread": 0.0045196908818695425,
          "steps": 20
        },
        {
          "dt": 0.025,
          "ensemble_mean_energy": 0.024624811230657656,
          "ensemble_mean_spatial_real_psi": 0.016341699216082382,
          "mean_cellwise_complex_std": 0.004531540776558599,
          "rms_complex_spread": 0.0045298361259017445,
          "steps": 40
        }
      ],
      "spread_reduction_factors_when_dt_halves": [
        0.9852251822153023,
        0.9941194221741886,
        0.997760350760993
      ]
    },
    "initial_only": {
      "block_exponent_95": {
        "independent_seed_blocks": 16,
        "lower_95_t_interval": -0.0018480367028937924,
        "maximum_block_exponent": -0.0017886357731242497,
        "mean_exponent": -0.0018364415616148495,
        "minimum_block_exponent": -0.0018710586287576238,
        "seeds_per_block": 64,
        "upper_95_t_interval": -0.0018248464203359067
      },
      "fitted_dt_power_exponent": -0.0018375549150722406,
      "rows": [
        {
          "dt": 0.2,
          "ensemble_mean_energy": 0.02462849579927516,
          "ensemble_mean_spatial_real_psi": 0.01634796639854512,
          "mean_cellwise_complex_std": 0.004082562037128639,
          "rms_complex_spread": 0.004081199330359511,
          "steps": 5
        },
        {
          "dt": 0.1,
          "ensemble_mean_energy": 0.024632020738579067,
          "ensemble_mean_spatial_real_psi": 0.016347986853968766,
          "mean_cellwise_complex_std": 0.004091737531942177,
          "rms_complex_spread": 0.004090371984334379,
          "steps": 10
        },
        {
          "dt": 0.05,
          "ensemble_mean_energy": 0.024633760342845888,
          "ensemble_mean_spatial_real_psi": 0.016347997076574725,
          "mean_cellwise_complex_std": 0.004096219895287795,
          "rms_complex_spread": 0.004094852960511229,
          "steps": 20
        },
        {
          "dt": 0.025,
          "ensemble_mean_energy": 0.024634624543592564,
          "ensemble_mean_spatial_real_psi": 0.016348002186602074,
          "mean_cellwise_complex_std": 0.004098435585566003,
          "rms_complex_spread": 0.004097067965236058,
          "steps": 40
        }
      ],
      "spread_reduction_factors_when_dt_halves": [
        0.9977575012712784,
        0.998905705230429,
        0.9994593683229999
      ]
    },
    "poisson_events": {
      "block_exponent_95": {
        "independent_seed_blocks": 16,
        "lower_95_t_interval": -0.011550888975693892,
        "maximum_block_exponent": -0.00048515417249803724,
        "mean_exponent": -0.008857043132295475,
        "minimum_block_exponent": -0.0168207889507734,
        "seeds_per_block": 64,
        "upper_95_t_interval": -0.006163197288897059
      },
      "fitted_dt_power_exponent": -0.009123887126903518,
      "rows": [
        {
          "dt": 0.2,
          "ensemble_mean_energy": 0.12526282807295921,
          "ensemble_mean_spatial_real_psi": 0.03688423325997961,
          "mean_cellwise_complex_std": 0.014042152511038346,
          "rms_complex_spread": 0.014039277842503736,
          "steps": 5
        },
        {
          "dt": 0.1,
          "ensemble_mean_energy": 0.12656964961621275,
          "ensemble_mean_spatial_real_psi": 0.037071705759489204,
          "mean_cellwise_complex_std": 0.014256136630850425,
          "rms_complex_spread": 0.01425411108923073,
          "steps": 10
        },
        {
          "dt": 0.05,
          "ensemble_mean_energy": 0.1264373030126293,
          "ensemble_mean_spatial_real_psi": 0.03705354064078942,
          "mean_cellwise_complex_std": 0.014303531708996578,
          "rms_complex_spread": 0.014301595583609309,
          "steps": 20
        },
        {
          "dt": 0.025,
          "ensemble_mean_energy": 0.1257080280049453,
          "ensemble_mean_spatial_real_psi": 0.03695299352102705,
          "mean_cellwise_complex_std": 0.01432481277643377,
          "rms_complex_spread": 0.014322490076541412,
          "steps": 40
        }
      ],
      "spread_reduction_factors_when_dt_halves": [
        0.9849283308245503,
        0.9966797764556425,
        0.9985411410431817
      ]
    }
  },
  "robustness_packet_grid8_T1_seeds256": {
    "current": {
      "fitted_dt_power_exponent": 0.4908912808483476,
      "rms_complex_spreads": [
        0.00645213012364146,
        0.004639868743193143,
        0.0033073763700386147,
        0.0023234525567024976
      ],
      "spread_reduction_factors_when_dt_halves": [
        1.3905846222712595,
        1.4028850133977862,
        1.4234748889095143
      ]
    },
    "gaussian_sde": {
      "fitted_dt_power_exponent": -0.011403265686550323,
      "rms_complex_spreads": [
        0.004434346810032629,
        0.00446349948338111,
        0.0045390404718023535,
        0.004527334162032967
      ],
      "spread_reduction_factors_when_dt_halves": [
        0.9934686508966731,
        0.9833574983764691,
        1.0025856959858537
      ]
    },
    "initial_only": {
      "fitted_dt_power_exponent": -0.0018262355838070882,
      "rms_complex_spreads": [
        0.004090173935938564,
        0.0040993098235694286,
        0.004103773017915712,
        0.004105979276393661
      ],
      "spread_reduction_factors_when_dt_halves": [
        0.9977713595643988,
        0.9989124168596073,
        0.9994626717941241
      ]
    },
    "poisson_events": {
      "fitted_dt_power_exponent": -0.010601093072029558,
      "rms_complex_spreads": [
        0.014051085370087802,
        0.014222129343753118,
        0.014296262012130663,
        0.014374565873878208
      ],
      "spread_reduction_factors_when_dt_halves": [
        0.9879733920616856,
        0.9948145418491462,
        0.9945526103233601
      ]
    }
  },
  "robustness_phase_gradient_grid16_T1_seeds256": {
    "current": {
      "fitted_dt_power_exponent": 0.49028328526425435,
      "rms_complex_spreads": [
        0.006473693393076739,
        0.004630853379867862,
        0.0032810052154164777,
        0.0023392155686119583
      ],
      "spread_reduction_factors_when_dt_halves": [
        1.3979482531708791,
        1.4114129895645533,
        1.4026091735373314
      ]
    },
    "gaussian_sde": {
      "fitted_dt_power_exponent": -0.010621292989555154,
      "rms_complex_spreads": [
        0.0044194720293460575,
        0.004487966527352967,
        0.004504321969215145,
        0.004523780697418101
      ],
      "spread_reduction_factors_when_dt_halves": [
        0.9847381887566554,
        0.9963689447659472,
        0.9956985695141981
      ]
    },
    "initial_only": {
      "fitted_dt_power_exponent": -0.0018170837095550757,
      "rms_complex_spreads": [
        0.004096440545051363,
        0.004105544266493287,
        0.0041099919471333365,
        0.004112190584534552
      ],
      "spread_reduction_factors_when_dt_halves": [
        0.9977825786665554,
        0.998917837140009,
        0.9994653366968242
      ]
    },
    "poisson_events": {
      "fitted_dt_power_exponent": -0.009446051344368614,
      "rms_complex_spreads": [
        0.013996548750423445,
        0.014215120263869374,
        0.014294831540133881,
        0.014278741874469368
      ],
      "spread_reduction_factors_when_dt_halves": [
        0.9846240123622821,
        0.9944237694553649,
        1.001126826565391
      ]
    }
  },
  "robustness_phase_gradient_grid8_T4_seeds256": {
    "current": {
      "fitted_dt_power_exponent": 0.4883346728799905,
      "rms_complex_spreads": [
        0.011014470919017442,
        0.007917521291920554,
        0.005643476232654814,
        0.003989941599085501
      ],
      "spread_reduction_factors_when_dt_halves": [
        1.3911514112702388,
        1.4029511183386307,
        1.414425773537213
      ]
    },
    "gaussian_sde": {
      "fitted_dt_power_exponent": -0.011315921805392133,
      "rms_complex_spreads": [
        0.007075298426445509,
        0.007149270382092737,
        0.007154844146617378,
        0.007260837494904736
      ],
      "spread_reduction_factors_when_dt_halves": [
        0.989653216105449,
        0.9992209803022368,
        0.9854020492316845
      ]
    },
    "initial_only": {
      "fitted_dt_power_exponent": -0.00404317777227548,
      "rms_complex_spreads": [
        0.002536259179672041,
        0.0025487346154962794,
        0.002554918058842884,
        0.00255799625887062
      ],
      "spread_reduction_factors_when_dt_halves": [
        0.9951052433045058,
        0.9975797879993831,
        0.9987966362276482
      ]
    },
    "poisson_events": {
      "fitted_dt_power_exponent": -0.009747470923399684,
      "rms_complex_spreads": [
        0.022662606687303178,
        0.022831807299402308,
        0.0230965000780326,
        0.023089906312168593
      ],
      "spread_reduction_factors_when_dt_halves": [
        0.9925892589281112,
        0.9885397017844255,
        1.000285569190921
      ]
    }
  }
}
```

## Appendix G — Zero-Kappa RNG-Claim Audit

This appendix reproduces the exact scalar recurrence hidden inside the historical zero-kappa test and compares it with the test's printed difference. Save the program as `zero_kappa_rng_claim_audit.py` and run it with Python 3; it uses only the standard library.

### G.1 Complete executable program

**Embedded program SHA-256:** `2eb0527436ece128673bca1a322491274ce4e04c493a0b10015fa891b89b47c7`

```python
"""Standalone audit of the historical zero-kappa true-RNG test claim."""

import json


STEPS = 1_500
DT = 1.0
DAMPING_RATE = 0.005
INJECTION = 1e-5 + 1e-5j
INITIAL_PERTURBATION = 1e-15 + 1e-15j
ORIGINAL_REPORTED_DIFFERENCE = 0.0028127574077312194

damping_factor = 1.0 - DAMPING_RATE * DT

difference = 0.0j
for _ in range(STEPS):
    difference = (difference + INJECTION) * damping_factor

analytic_repeated_forcing = (
    abs(INJECTION)
    * damping_factor
    * (1.0 - damping_factor**STEPS)
    / (1.0 - damping_factor)
)
single_perturbation_after_steps = (
    abs(INJECTION) * damping_factor**STEPS
)

output = {
    "configuration": {
        "steps": STEPS,
        "dt": DT,
        "damping_rate": DAMPING_RATE,
        "damping_factor": damping_factor,
        "repeated_injection_real": INJECTION.real,
        "repeated_injection_imag": INJECTION.imag,
        "initial_perturbation_real": INITIAL_PERTURBATION.real,
        "initial_perturbation_imag": INITIAL_PERTURBATION.imag,
        "kappa": 0.0,
    },
    "source_path_implications": {
        "diffusion_transfer_multiplier": 0.0,
        "interaction_transfer_multiplier": 0.0,
        "stochastic_source_transfer_multiplier": 0.0,
        "initial_perturbation_is_overwritten_by_step_zero_pump": True,
        "remaining_difference_equation": "d[n+1]=(d[n]+j)*(1-0.005*dt)",
    },
    "results": {
        "scalar_recurrence_repeated_forcing": abs(difference),
        "analytic_repeated_forcing": analytic_repeated_forcing,
        "recurrence_vs_analytic_absolute_error": abs(
            abs(difference) - analytic_repeated_forcing
        ),
        "original_test_reported_difference": ORIGINAL_REPORTED_DIFFERENCE,
        "original_vs_analytic_absolute_error": abs(
            ORIGINAL_REPORTED_DIFFERENCE - analytic_repeated_forcing
        ),
        "original_vs_analytic_relative_error": abs(
            ORIGINAL_REPORTED_DIFFERENCE - analytic_repeated_forcing
        )
        / analytic_repeated_forcing,
        "single_1e_5_perturbation_after_1500_steps": (
            single_perturbation_after_steps
        ),
        "repeated_sum_to_one_injection_ratio": (
            analytic_repeated_forcing / abs(INJECTION)
        ),
    },
    "verdict": (
        "The reported threshold crossing is explained by explicit repeated "
        "forcing and damping; it is not evidence of chaos or true randomness."
    ),
}

print(json.dumps(output, indent=2, sort_keys=True))
```

### G.2 Full reference output

**Normalized execution-output SHA-256:** `40d54a9d1721d118b6d9533bffab078a9062d43fbd9a2e304693bd0fa550ab16`

```json
{
  "configuration": {
    "damping_factor": 0.995,
    "damping_rate": 0.005,
    "dt": 1.0,
    "initial_perturbation_imag": 1e-15,
    "initial_perturbation_real": 1e-15,
    "kappa": 0.0,
    "repeated_injection_imag": 1e-05,
    "repeated_injection_real": 1e-05,
    "steps": 1500
  },
  "results": {
    "analytic_repeated_forcing": 0.0028127574610763545,
    "original_test_reported_difference": 0.0028127574077312194,
    "original_vs_analytic_absolute_error": 5.334513516683237e-11,
    "original_vs_analytic_relative_error": 1.8965423043058553e-08,
    "recurrence_vs_analytic_absolute_error": 8.239936510889834e-18,
    "repeated_sum_to_one_injection_ratio": 198.89198745601468,
    "scalar_recurrence_repeated_forcing": 0.002812757461076363,
    "single_1e_5_perturbation_after_1500_steps": 7.67602033217176e-09
  },
  "source_path_implications": {
    "diffusion_transfer_multiplier": 0.0,
    "initial_perturbation_is_overwritten_by_step_zero_pump": true,
    "interaction_transfer_multiplier": 0.0,
    "remaining_difference_equation": "d[n+1]=(d[n]+j)*(1-0.005*dt)",
    "stochastic_source_transfer_multiplier": 0.0
  },
  "verdict": "The reported threshold crossing is explained by explicit repeated forcing and damping; it is not evidence of chaos or true randomness."
}
```
