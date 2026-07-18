# Lineum Under Adversarial Review: Fundamental Physics, Philosophy, and a Verification Program

**Document status:** active research basis for future whitepaper revisions; not itself a whitepaper or evidence that the theory is physically valid
**Research version:** 0.9
**Evidence and calculation cutoff date:** July 18, 2026
**Language:** English
**Reproducibility:** all nine embedded programs reproduce the embedded JSON outputs with semantic identity
**Current confidence:** high for the reproduced numerical results, deterministic reference lane, time-step diagnosis, zero-kappa RNG-claim audit, finite-time Lyapunov calculations in the declared regimes, and mathematical classification of the isolated current source; medium for the signature protocol within its declared resolution; low for the physical interpretation and the other untested hypotheses proposed for future work
**Standalone portability:** all essential equations, inputs, programs, outputs, limitations, and external source metadata are embedded in this single document; no repository file is required
**Scope of evaluation:** published arguments, mathematical statements, and physical claims only; this document contains no personal or reputational assessment

## Abstract

This study subjects the Lineum project to adversarial physical, mathematical, and philosophical scrutiny. Its default rule is that every ontological or physical claim made by Lineum remains an **untested hypothesis** until it follows from a single well-defined dynamics, passes numerical checks, and is consistent with existing experiments. The review combines an audit of four repositories, primary scholarly literature, a full-text analysis of Jan Fikáček's dissertation, a bibliographic and sample-based analysis of his book, a review of relevant articles and public lectures, and original reproducible calculations.

The result is demanding but constructive. Lineum has a legitimate research objective: to investigate whether finite local microdynamics can produce smooth macroscopic phenomena, stable localized objects, and a physical account of information. A later Gate-0 audit has now established one named deterministic regression lane and corrected one opt-in time-step inconsistency without changing historical defaults. The implementation is nevertheless not yet a physical theory of spacetime or quantum mechanics. It still does not supply one final canonical physical law, a relativistic structure, the Born rule, a measurement mechanism, a model of gravity, a derivation of mass, or demonstrated stable particles. Its stochastic ontology is also unresolved. A regular square lattice introduces preferred directions; some numerical schemes reduce that artifact but may replace strict locality with a global update.

The original calculations in this report show, among other results: (i) angular anisotropy of lattice dispersion relations that grows with wavenumber; (ii) instantaneous nonzero tails under spectral evolution; (iii) finite-lattice wave-packet energy saturation without a dynamical prohibition against collapse into one cell; (iv) logical independence between a field norm and Shannon information; (v) the Bell bound \(|S|\le 2\) for local hidden-variable models, compared with the quantum value \(2\sqrt 2\); (vi) decoherence without selection of a unique outcome; (vii) regularization of black-hole curvature by a cutoff without derived gravitational dynamics; (viii) numerical convergence of discrete transport to smooth macroscopic motion, which does not by itself establish ontically continuous motion; (ix) a state-independent Peres–Mermin contradiction for noncontextual hidden values; (x) no positive finite-time Lyapunov exponent in 84 estimates across seven declared deterministic Lineum regimes, while the same estimator correctly detects a positive logistic-map control; and (xi) a validated but resolution-limited observation protocol that separates five declared stochastic controls and identifies the present isolated source as a finite-step Bernoulli-plus-Gaussian law rather than a continuous Gaussian, Poisson, or memory process.

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
| Deterministic chaos currently explains the foam-like behavior. | **Not supported in the seven tested deterministic regimes** | All 84 finite-time Lyapunov estimates were negative. This narrows, but does not eliminate, the chaos hypothesis; other parameters, states, operators, dimensions, or longer asymptotic behavior remain untested. |
| The isolated current source is continuous Gaussian noise, a Poisson birth law, or colored memory. | **Contradicted for the audited source contract** | It is a state-dependent Bernoulli linon term plus Gaussian fluctuation, both multiplied by \(h\). Its centered excess kurtosis is about \(-1.615\), lag-one correlation is consistent with zero, and variance rate scales as \(h^{0.99974}\). |
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
10. **do not identify foam-like morphology with deterministic chaos in the currently tested regimes; describe initial branching, dissipative self-organization, stochastic forcing, event processes, memory, unresolved variables, and quantum amplitudes as separate candidates until a discriminator selects among them**.
11. **describe the current random source as the finite-step F0 software contract, not as verified quantum foam; use the validated signature protocol only within its temporal and amplitude resolution, and preserve the documented equivalences between short memory and white noise, high-rate events and Gaussian forcing, and weak dependence and independent events**.

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

### 3.10 Finite-time Lyapunov audit of declared deterministic regimes

The next audit applied that stronger test. It reconstructed the deterministic NumPy update as a standalone program and used a Benettin renormalization procedure. Let \(X_n\) contain the real and imaginary parts of \(\psi\), \(\phi\), and \(\mu\) when enabled. After each joint update of a base and perturbed trajectory, the full-state separation \(r_n=\|\delta X_n\|_2\) was measured and the perturbation was restored to length \(\epsilon\). The finite-time estimate is

\[
\lambda_T=\frac{1}{T}\sum_{n=1}^{N}\log\!\left(\frac{r_n}{\epsilon}\right),
\qquad T=Nh.
\]

There is one random perturbation direction at the start of measurement and **no continuing differential forcing**. The primary audit used a \(16\times16\) periodic grid, burn time 10, measurement time 40, six directions, and both \(\epsilon=10^{-7}\) and \(10^{-9}\). Pump and cavity-wall operations, where present, were applied identically to both trajectories. No amplitude cap triggered.

| Deterministic regime | Mean \(\lambda_{40}\) at \(\epsilon=10^{-7}\) | Largest of six | Positive estimates |
|---|---:|---:|---:|
| zero-\(\kappa\) damping control | \(-0.0050012504\) | \(-0.0050012495\) | 0/6 |
| `RD-0` continuous, \(\kappa=1\) | \(-0.0187590333\) | \(-0.0081997905\) | 0/6 |
| continuous mode coupling, \(\kappa=0.5\) | \(-0.0295624732\) | \(-0.0278775755\) | 0/6 |
| continuous mode coupling, \(\kappa=1\) | \(-0.0436792076\) | \(-0.0399089103\) | 0/6 |
| continuous mode coupling with \(\mu\), \(\kappa=1\) | \(-0.0424670530\) | \(-0.0366145544\) | 0/6 |
| driven cavity, continuous, \(\kappa=0.5\) | \(-0.0588907573\) | \(-0.0561030528\) | 0/6 |
| legacy per-update \(\phi\), mode coupling, \(\kappa=1\) | \(-0.0452076318\) | \(-0.0428988547\) | 0/6 |

Across both perturbation sizes this gives 84 estimates: zero positive, minimum `-0.06044663723779249`, and maximum `-0.005001222715633557`. The largest difference between matched \(\epsilon\) estimates was `4.0322631715550283e-07`, so the sign is not an artifact of choosing one perturbation magnitude.

Three controls constrain interpretation:

1. the same estimator gives `0.6930771849` and `0.6930771978` for the chaotic logistic map at \(r=4\), compared with the exact \(\ln 2=0.6931471806\);
2. the zero-\(\kappa\) result agrees with the exact damping exponent \(h^{-1}\log(1-0.005h)=-0.0050012504\);
3. ten reconstructed updates in two regimes agree element by element with the actual deterministic NumPy runtime, with maximum absolute difference `0.0`.

The sign also remained negative in fixed-physical-time sensitivities: \(h=0.2,0.1,0.05\); \(\kappa=0,0.25,0.5,0.75,1\); grids \(16^2\) and \(24^2\); and measurement horizons 20, 40, and 80. However, the mean for the continuous mode-coupled \(\kappa=1\) regime moved from `-0.0830428` at \(T=20\), through `-0.0431786` at \(T=40\), to `-0.0245938` at \(T=80\). Because it trends toward zero, this audit does **not** establish a strictly negative asymptotic largest Lyapunov exponent.

**Verdict [CALCULATED]:** no positive finite-time Lyapunov exponent was found in the declared deterministic regimes. Therefore deterministic chaos is not presently a supported explanation of foam-like morphology in those lanes. The result does not prove that all Lineum parameter space is non-chaotic, and it does not distinguish initial branch selection, ordinary dissipative pattern formation, finite-step stochastic forcing, events, memory, unresolved variables, or quantum-amplitude dynamics. Visual irregularity alone cannot make that choice.

### 3.11 A common observation protocol separates declared foam controls, not hidden ontologies below resolution

The next gate asked a narrower question: **if a deterministic backbone is known and subtracted, can observable source residuals distinguish F1–F5 under controlled conditions?** Let \(D_h\) be that declared deterministic update and define the observed innovation

\[
r_n=X_{n+1}-D_h(X_n).
\]

Five controls were constructed on an \(8\times8\) field. Their approximate one-step marginal scale was matched at the primary step \(h=0.1\), so classification could not rely merely on one candidate being visibly larger:

| Candidate | Controlled residual law | Primary signature |
|---|---|---|
| F1 initial only | \(r_n=0\) after the initial branch | zero matched-state future innovation |
| F2 Gaussian white | \(r_n=\sigma\sqrt h\,Z_n\) | Gaussian kurtosis and zero temporal correlation |
| F3 independent events | \(r_n=A(N_n^+-N_n^-)\), \(N_n^\pm\sim{\rm Poisson}(\lambda h/2)\), \(A=\sigma/\sqrt\lambda\) | heavy tails, independent event times |
| F4 state/history events | Poisson intensity depends on a declared state score and a stable Hawkes excitation | high state-rate or previous-event rate ratio |
| F5 colored memory | \(\eta_{n+1}=\rho\eta_n+\sqrt{1-\rho^2}Z_n\), \(\rho=e^{-h/\tau}\), \(r_n=Gh\eta_n\) | nonzero signed lag correlation and accumulated variance |

The protocol measures innovation RMS, one-step and one-unit variance rates, excess kurtosis, signed and absolute lag-one correlations, the tail fraction above \(2.5\) standard deviations, event-count Fano factor, waiting-time coefficient of variation, and event-rate ratios conditioned on the previous event and on high versus low state score. Each confidence interval treats an independently seeded run—not individual correlated cells—as the replication unit.

The original decision tree allowed any one of state dependence, event-history dependence, or Fano factor above `1.3` to select F4. This rule was preserved as a negative result: it classified 79/80 calibration runs correctly and 174/180 time-step sensitivity runs correctly. Six independent Poisson runs were false positives because a Fano estimate based on only 25 windows fluctuated above the threshold.

The recorded correction did **not** tune the Fano threshold. Instead, Fano factor became supporting evidence and F4 selection required direct state-rate or history-rate ratio above `1.5`. A third seed family, not used to diagnose the failure, then supplied the post-revision audit:

| Dataset | Original rule | Revised rule |
|---|---:|---:|
| calibration, \(h=0.1\), 16 runs per candidate | 79/80 | 80/80 |
| first separate validation, \(h=0.1\), 16 runs per candidate | 80/80 | 80/80 |
| development sensitivity, \(h=0.2,0.1,0.05\), 12 runs per candidate and step | 174/180 | 180/180 |
| post-revision audit, new seeds, same three steps | 177/180 | **180/180** |

Four predeclared pairwise checks also had non-overlapping run-level 95% \(t\)-intervals:

| Pair | Metric | Left 95% interval | Right 95% interval |
|---|---|---:|---:|
| F1 vs. F2 | innovation RMS | exactly \(0\) | \([0.00157894,0.00158321]\) |
| F2 vs. F3 | excess kurtosis | \([-0.00600,0.00937]\) | \([19.4617,20.0713]\) |
| F2 vs. F5 | signed lag-one correlation | \([-0.00336,0.000121]\) | \([0.818523,0.821349]\) |
| F3 vs. F4 | high-state/low-state event-rate ratio | \([1.00605,1.06151]\) | \([7.98509,9.61900]\) |

The perfect post-revision score applies only to these declared controls. Deliberately weaker boundary cases demonstrate three observational equivalences:

| Boundary test at \(h=0.1\) | Result | Meaning |
|---|---|---|
| colored memory \(\tau/h=0.2\) or \(0.5\) | 24/24 classified as F2 | memory shorter than the observation interval is unresolved and looks white |
| colored memory \(\tau/h=1,2,5\) | 36/36 classified as F5 | resolved memory produces the predicted lag |
| Poisson rate \(10\), jump size reduced to preserve variance | 12/12 classified as F2 | many small jumps approach a Gaussian law |
| Hawkes branching \(0.1\), no state dependence | 7/12 F3 and 5/12 F4 | weak history dependence overlaps independent events at this sample size |
| branching \(0.3\) or \(0.6\), or state coefficient \(0.3\) or \(0.9\) | every declared run classified as F4 | stronger dependence is resolved |

These are not defects that can be removed by better labeling. They are identifiability limits: two different hidden mechanisms can induce the same observable law after temporal or amplitude coarse-graining. State heterogeneity can also imitate event memory because repeated events occur in the same high-rate cells. Separating state dependence from genuine self-excitation therefore requires a conditional ablation, not only an unconditional waiting-time statistic. Exact tables are used here because the decision depends on interval boundaries and classification counts rather than on a visual trend.

The same protocol was then applied to the **isolated present source contract** on a controlled positive-phase field. After subtracting its conditional mean, the projected innovation is

\[
r_h=h\left[A(B-p)+\sigma Z\right],\qquad
p=\frac{1}{1+e^{-5(|\psi|+|\nabla|\psi||)}},\qquad
A=0.03+0.02|\psi|,
\]

where \(B\) is Bernoulli and \(Z\) is Gaussian. Consequently,

\[
\frac{{\rm Var}(r_h)}{h}
=h\,\mathbb E\!\left[A^2p(1-p)+\sigma^2\right].
\]

The controlled fixture gives the coefficient
`0.0002551958227644319`. The simulation agrees with this formula within
`0.1216%`, and its fitted variance-rate exponent is
`0.999737593589198`, compared with the exact exponent \(1\):

| \(h\) | innovation RMS | variance per unit time | excess kurtosis | signed lag-one correlation |
|---:|---:|---:|---:|---:|
| 0.200 | 0.00319384 | \(5.09992\times10^{-5}\) | -1.61489 | 0.000871 |
| 0.100 | 0.00159848 | \(2.55506\times10^{-5}\) | -1.61621 | -0.000932 |
| 0.050 | 0.000798670 | \(1.27574\times10^{-5}\) | -1.61574 | 0.001168 |
| 0.025 | 0.000399430 | \(6.38175\times10^{-6}\) | -1.61440 | -0.00000848 |

The standalone source reconstruction was also compared with actual deterministic and stochastic runtime steps at \(h=0.2,0.1,0.05\). After accounting for the subsequent damping factor, the maximum absolute difference was
`4.628188023797497e-18`.

**Verdict [CALCULATED]:** the protocol can distinguish declared, sufficiently resolved F1–F5 controls, and its failure boundaries are now explicit. The isolated current source is not one of those continuous controls: it is the finite-step F0 state-dependent Bernoulli-plus-Gaussian software law, with no detected lag memory and a variance rate that vanishes linearly under refinement. This classifies the implemented source contract, **not the physical ontology of quantum foam and not the full visual morphology of an evolving nonlinear simulation**. No production default should change on this evidence alone.

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

**Current evidence.** The time-refinement experiment rejects F0 as a nonzero continuous-variance forcing law in the tested source/diffusion lane but preserves it as a discrete per-update software contract. A direct signature audit now classifies that isolated source more precisely: a state-dependent Bernoulli linon term plus Gaussian fluctuation, both multiplied by \(h\), with excess kurtosis near \(-1.615\), no detected lag memory, and variance rate proportional to \(h^{0.99974}\). A common protocol separates declared, sufficiently resolved F1–F5 controls, but it also demonstrates observational equivalences: short memory looks white, many small Poisson jumps look Gaussian, and weak dependence looks independent. These controls validate the discriminator, not any physical ontology. The historical zero-\(\kappa\) test does not support F6 because it repeatedly forces one run and exactly follows a damped geometric sum. A subsequent Benettin audit also found zero positive finite-time Lyapunov estimates among 84 measurements in seven declared deterministic regimes. This is reproducible negative evidence for F6 **within those regimes**, but not a global rejection: other parameter ranges, initial states, dimensions, operators, and asymptotic horizons remain open.

**Next read-only gate.** Move from the isolated source to source-to-morphology causality. Starting from identical complete states, compare deterministic-only, initial-only, current F0, Gaussian, Poisson, state-dependent, and memory controls under the same nonlinear backbone. Measure which source changes persistent morphology, localization, event topology, and seed-to-seed branch identity after matching coarse variance. Separate state dependence from self-excitation by conditioning history tests on the full declared state. Do not modify the default runtime until the result survives time, grid, horizon, detector-threshold, and observation-scale controls.

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
12. **The zero-kappa result is a claim audit, not a complete chaos survey.** It proves why one historical threshold test passed and why that pass did not measure chaos.
13. **The Lyapunov audit is finite and regime-bound.** It covers seven declared deterministic regimes plus sensitivities in step, permeability, grid, and horizon. It does not exhaust every nonlinear coefficient, initial state, boundary, wave backend, dimension, or asymptotic attractor. The drift of the finite-time estimate toward zero at longer horizons precludes a claim of strictly negative asymptotic exponent.
14. **The foam-signature protocol is an identifiability test, not an ontology detector.** Its 180/180 post-revision score concerns five declared, sufficiently separated synthetic controls. Short memory, frequent small jumps, weak dependence, state heterogeneity, coarse observations, and an incorrect deterministic backbone can make distinct mechanisms observationally equivalent. The current F0 conclusion classifies the isolated implemented source, not the complete nonlinear morphology or a physical quantum vacuum.

## 11. Final Assessment

Lineum has credible research potential if it maintains the distinction between an idea and its proof: ontological intuition can motivate a program, but does not confirm it. The project has now moved beyond a purely narrative starting point by establishing a reproducible deterministic reference lane, identifying and repairing one opt-in time-step inconsistency, distinguishing four stochastic time contracts, finding no support for deterministic chaos as the current explanation in seven tested deterministic regimes, and classifying the isolated current source as a finite-step Bernoulli-plus-Gaussian contract with explicit observational alternatives. Its strongest assets are still not a ready-made “theory of everything,” but an open simulation laboratory, a willingness to preserve negative results, and an improving ability to formulate sharp tests of finite microdynamics.

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

### Statistical process source

42. Hawkes, A. G. *Spectra of Some Self-Exciting and Mutually Exciting Point Processes*. Biometrika 58(1), 83–90 (1971). [DOI](https://doi.org/10.1093/biomet/58.1.83).

---

## Appendix A — Reproduction Log and Control Outputs

### A.1 Environment

- audit environment: Python 3.11.15 and NumPy 1.26.4
- replay environment: Python 3.12.13 and NumPy 2.3.5
- deterministic seed `20260715`
- three general-physics checks use only NumPy and the standard library; the OEA ablation additionally uses SciPy 1.17.1 to reproduce the imaging operations accurately
- the seven earlier programs were executed against their embedded JSON in the audit environment; with the frozen versions, they reproduced exactly the same structure and values
- the eighth, finite-time Lyapunov program was executed twice in the replay environment with bitwise-identical normalized output; two reconstructed regimes also matched the actual deterministic NumPy runtime with maximum absolute difference `0.0`
- the ninth, foam-signature program was executed twice with bitwise-identical normalized output; its analytical Gaussian, Poisson, memory, and current-source controls passed, and its reconstructed current source matched actual runtime steps within `4.63e-18`
- in the newer Python/NumPy environment, the three programs that do not require SciPy passed semantic comparison with \(\mathrm{rtol}=10^{-11}\) and \(\mathrm{atol}=10^{-13}\); differences were limited to runtime metadata and final floating-point bits
- the OEA program was not replayed in the second environment because SciPy was not installed there; its full reproduction therefore applies to the stated audit environment with SciPy 1.17.1
- the automatic document audit passed: 9/9 executable Python/JSON pairs, 42 contiguous adversarial questions, 42 contiguous bibliographic entries, balanced code fences, and no local-file references

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
| deterministic chaos audit | finite-time largest Lyapunov estimate | logistic-map positive control and exact zero-\(\kappa\) damping exponent | seven regimes, two perturbation sizes, six directions, \(h\), \(\kappa\), horizon, and grid sensitivities | absence of chaos in all Lineum parameter space or a choice among non-chaotic foam mechanisms |
| foam-source signatures | innovation scale, kurtosis, lag correlation, event-rate ratios, Fano factor, waiting times | Gaussian, compound-Poisson, exact OU lag, and current-source variance formulas | three independent seed families, three \(h\), memory, event-rate, dependence, and resolution boundaries | a physical ontology, full nonlinear morphology, or mechanisms below observation resolution |

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
| foam protocol: revised post-audit classifications | \(180/180\) in declared controls |
| current F0: variance-rate exponent in \(h\) | \(0.9997376\) |
| current F0: centered excess kurtosis | \(\approx-1.615\) |
| current F0 reconstruction: maximum runtime difference | \(4.63\times10^{-18}\) |

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

## Appendix H — Finite-Time Lyapunov Audit

This appendix is a standalone reconstruction of the deterministic update used by the audit. It requires Python 3 and NumPy, reads no project data, writes no files, and prints every reported result as JSON. The primary calculation uses the Benettin method with full-state renormalization and contains both a known positive-chaos control and an analytically soluble damping control.

### H.1 Complete executable program

**Embedded program SHA-256 after LF normalization:** `9ab2eeebe6515d92aa43e4cc291d3ad1e750a6af120ff9a2244d17e4c5cbc9c2`

```python
"""Standalone finite-time Lyapunov audit for deterministic Lineum regimes."""

from __future__ import annotations

from dataclasses import dataclass
import json

import numpy as np


PRIMARY_SIZE = 16
PRIMARY_BURN_TIME = 10.0
PRIMARY_MEASURE_TIME = 40.0
PRIMARY_DIRECTIONS = 6
PRIMARY_EPSILONS = (1e-7, 1e-9)


@dataclass(frozen=True)
class Config:
    dt: float = 0.1
    psi_diffusion: float = 0.05
    phi_diffusion: float = 0.05
    reaction_strength: float = 0.0007
    drift_strength: float = -0.004
    use_mode_coupling: bool = False
    mode_coupling_strength: float = 0.001
    use_mu: bool = False
    mu_eta: float = 0.005
    mu_rho: float = 0.0001
    mu_cap: float = 10.0
    mu_peak_cutoff_ratio: float = 0.1
    phi_diffusion_scales_with_dt: bool = True
    psi_amp_cap: float = 1e6
    phi_cap: float = 1e6


def make_state(size, kappa_value, cavity=False):
    y, x = np.mgrid[:size, :size]
    if cavity:
        psi = np.full((size, size), 0.5, dtype=np.complex128)
        psi[size // 3 : 2 * size // 3, size // 3 : 2 * size // 3] = 1.0
        phi = np.zeros((size, size), dtype=np.float64)
    else:
        center = (size - 1) / 2
        radius_squared = (x - center) ** 2 + (y - center) ** 2
        envelope = np.exp(-radius_squared / (2 * 3.5**2))
        phase = 0.17 * x - 0.11 * y
        psi = envelope * np.exp(1j * phase)
        phi = 0.25 + 0.08 * np.cos(2 * np.pi * x / size) * np.cos(
            2 * np.pi * y / size
        )
    return {
        "psi": psi.astype(np.complex128),
        "phi": phi.astype(np.float64),
        "kappa": np.full((size, size), kappa_value, dtype=np.float64),
        "delta": np.zeros((size, size), dtype=np.float64),
        "mu": np.zeros((size, size), dtype=np.float64),
    }


def clone(state):
    return {name: value.copy() for name, value in state.items()}


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


def step_lineum(state, config):
    psi = state["psi"].copy()
    phi = state["phi"].copy()
    kappa = state["kappa"]
    mu = state["mu"].copy()
    size = psi.shape[0]

    drift_multiplier = 1.0 + mu
    phi_internal = np.clip(phi, 0.0, 10.0)
    interaction_factor = 0.1 * np.tanh(
        (0.04 * phi_internal * kappa * drift_multiplier) / 0.1
    )
    interaction = interaction_factor * psi
    interaction = interaction / (1.0 + np.abs(interaction) / 10.0)

    grad_phi_x, grad_phi_y = np.gradient(phi)
    flow = (
        config.drift_strength
        * (grad_phi_x + 1j * grad_phi_y)
        * kappa
        * drift_multiplier
    )
    flow = flow / (1.0 + np.abs(flow) / 10.0)

    psi += flow * config.dt
    psi += interaction * config.dt
    psi -= 0.005 * psi * config.dt
    psi += (
        weighted_laplace(psi, kappa, config.psi_diffusion)
        * kappa
        * config.dt
    )

    energy = np.abs(psi) ** 2
    if config.use_mode_coupling:
        transferred = (
            config.mode_coupling_strength * energy * kappa * config.dt
        )
        phi += transferred
        new_magnitude = np.sqrt(np.maximum(energy - transferred, 0.0))
        psi = psi / (np.sqrt(energy) + 1e-12) * new_magnitude
    else:
        scale_ratio = (128.0 / size) ** 2
        reaction = config.reaction_strength * scale_ratio
        phi += kappa * reaction * (energy - phi) * config.dt

    phi_step_scale = config.dt if config.phi_diffusion_scales_with_dt else 1.0
    phi += (
        kappa
        * config.phi_diffusion
        * weighted_laplace(phi, kappa, 0.05)
        * phi_step_scale
    )
    phi = np.clip(phi, 0.0, config.phi_cap)

    if config.use_mu:
        floor = config.mu_peak_cutoff_ratio
        if 0.0 < floor < 1.0:
            floor *= np.max(energy)
        active_energy = np.maximum(energy - floor, 0.0)
        mu += (
            config.mu_eta
            * active_energy
            * kappa
            * drift_multiplier
            * config.dt
        )
        mu -= config.mu_rho * mu * config.dt
        mu = np.clip(mu, 0.0, config.mu_cap)

    cap_trigger = bool(
        np.isnan(np.sum(psi)) or np.max(np.abs(psi)) >= 0.99 * config.psi_amp_cap
    )
    if cap_trigger:
        psi = np.zeros_like(psi)
    return {
        "psi": psi,
        "phi": phi,
        "kappa": kappa,
        "delta": state["delta"],
        "mu": mu,
    }, cap_trigger


def apply_cavity_drive(state, step_index):
    size = state["psi"].shape[0]
    y, x = np.ogrid[-size // 2 : size // 2, -size // 2 : size // 2]
    mask = x**2 + y**2 > (size // 2 - 3) ** 2
    state["psi"][mask] = 0.0j
    if step_index % 5 == 0:
        state["psi"][
            size // 3 : 2 * size // 3,
            size // 3 : 2 * size // 3,
        ] = 1.0 + 0.0j


def evolve_one_step(state, config, step_index, cavity):
    if cavity:
        apply_cavity_drive(state, step_index)
    return step_lineum(state, config)


def state_difference(base, perturbed, include_mu):
    d_psi = perturbed["psi"] - base["psi"]
    d_phi = perturbed["phi"] - base["phi"]
    components = [d_psi.real, d_psi.imag, d_phi]
    d_mu = None
    if include_mu:
        d_mu = perturbed["mu"] - base["mu"]
        components.append(d_mu)
    norm = float(np.sqrt(sum(np.sum(component**2) for component in components)))
    return d_psi, d_phi, d_mu, norm


def psi_perturbation(base, seed, epsilon):
    rng = np.random.RandomState(seed)
    real = rng.normal(size=base["psi"].shape)
    imag = rng.normal(size=base["psi"].shape)
    scale = epsilon / np.sqrt(np.sum(real**2) + np.sum(imag**2))
    perturbed = clone(base)
    perturbed["psi"] += scale * (real + 1j * imag)
    return perturbed


def renormalize(base, perturbed, epsilon, include_mu):
    d_psi, d_phi, d_mu, norm = state_difference(
        base, perturbed, include_mu
    )
    if norm == 0.0 or not np.isfinite(norm):
        return None, norm
    scale = epsilon / norm
    result = clone(base)
    result["psi"] += scale * d_psi
    result["phi"] += scale * d_phi
    if include_mu:
        result["mu"] += scale * d_mu
    return result, norm


def estimate_exponent(
    config,
    kappa,
    cavity,
    size,
    burn_time,
    measure_time,
    epsilon,
    seed,
):
    burn_steps = round(burn_time / config.dt)
    measure_steps = round(measure_time / config.dt)
    base = make_state(size, kappa, cavity)
    cap_triggers = 0
    for step_index in range(burn_steps):
        base, triggered = evolve_one_step(
            base, config, step_index, cavity
        )
        cap_triggers += int(triggered)

    perturbed = psi_perturbation(base, seed, epsilon)
    log_growth = []
    for offset in range(measure_steps):
        step_index = burn_steps + offset
        base, triggered = evolve_one_step(base, config, step_index, cavity)
        perturbed, perturbed_triggered = evolve_one_step(
            perturbed, config, step_index, cavity
        )
        cap_triggers += int(triggered) + int(perturbed_triggered)
        perturbed, norm = renormalize(
            base, perturbed, epsilon, config.use_mu
        )
        if perturbed is None:
            return {
                "exponent_per_time": float("-inf"),
                "cap_triggers": cap_triggers,
                "invalid_difference": True,
            }
        log_growth.append(np.log(norm / epsilon))

    return {
        "exponent_per_time": float(
            np.sum(log_growth) / (measure_steps * config.dt)
        ),
        "cap_triggers": cap_triggers,
        "invalid_difference": False,
        "final_energy": float(np.sum(np.abs(base["psi"]) ** 2)),
        "final_phi_sum": float(np.sum(base["phi"])),
        "final_mu_sum": float(np.sum(base["mu"])),
    }


def summarize(values):
    finite = np.asarray([value for value in values if np.isfinite(value)])
    return {
        "mean": float(np.mean(finite)),
        "minimum": float(np.min(finite)),
        "maximum": float(np.max(finite)),
        "standard_deviation": float(np.std(finite, ddof=1)) if len(finite) > 1 else 0.0,
        "positive_count": int(np.sum(finite > 0.0)),
        "count": int(len(finite)),
    }


def run_directions(
    config,
    kappa,
    cavity=False,
    size=PRIMARY_SIZE,
    burn_time=PRIMARY_BURN_TIME,
    measure_time=PRIMARY_MEASURE_TIME,
    epsilons=PRIMARY_EPSILONS,
    directions=PRIMARY_DIRECTIONS,
    seed_base=2_026_073_000,
):
    output = {}
    for epsilon in epsilons:
        rows = [
            estimate_exponent(
                config,
                kappa,
                cavity,
                size,
                burn_time,
                measure_time,
                epsilon,
                seed_base + direction,
            )
            for direction in range(directions)
        ]
        output[f"{epsilon:.0e}"] = {
            "summary": summarize(
                [row["exponent_per_time"] for row in rows]
            ),
            "direction_exponents": [
                row["exponent_per_time"] for row in rows
            ],
            "total_cap_triggers": int(
                sum(row["cap_triggers"] for row in rows)
            ),
        }
    return output


def logistic_benettin(epsilon, steps=20_000, burn_steps=100):
    x = 0.123456789
    for _ in range(burn_steps):
        x = 4.0 * x * (1.0 - x)
    perturbed = x + epsilon
    logs = []
    for _ in range(steps):
        x = 4.0 * x * (1.0 - x)
        perturbed = 4.0 * perturbed * (1.0 - perturbed)
        difference = perturbed - x
        magnitude = abs(difference)
        logs.append(np.log(magnitude / epsilon))
        perturbed = x + epsilon * np.sign(difference)
    return float(np.mean(logs))


primary_regimes = {
    "zero_kappa_damping_control": (
        Config(dt=0.1, use_mode_coupling=True),
        0.0,
        False,
    ),
    "rd0_continuous_kappa1": (
        Config(dt=0.1, use_mode_coupling=False),
        1.0,
        False,
    ),
    "continuous_mode_coupled_kappa0_5": (
        Config(dt=0.1, use_mode_coupling=True),
        0.5,
        False,
    ),
    "continuous_mode_coupled_kappa1": (
        Config(dt=0.1, use_mode_coupling=True),
        1.0,
        False,
    ),
    "continuous_mode_coupled_mu_kappa1": (
        Config(dt=0.1, use_mode_coupling=True, use_mu=True),
        1.0,
        False,
    ),
    "driven_cavity_continuous_kappa0_5": (
        Config(dt=0.1, use_mode_coupling=True),
        0.5,
        True,
    ),
    "legacy_mode_coupled_kappa1": (
        Config(
            dt=0.1,
            use_mode_coupling=True,
            phi_diffusion_scales_with_dt=False,
        ),
        1.0,
        False,
    ),
}

primary = {
    name: run_directions(
        config,
        kappa,
        cavity=cavity,
        seed_base=2_026_073_000 + index * 100,
    )
    for index, (name, (config, kappa, cavity)) in enumerate(
        primary_regimes.items()
    )
}

kappa_sweep = []
for index, kappa in enumerate((0.0, 0.25, 0.5, 0.75, 1.0)):
    result = run_directions(
        Config(dt=0.1, use_mode_coupling=True),
        kappa,
        epsilons=(1e-7,),
        directions=3,
        seed_base=2_026_074_000 + index * 100,
    )["1e-07"]
    kappa_sweep.append({"kappa": kappa, **result})

dt_sensitivity = {}
for regime_name, kappa, cavity in (
    ("mode_coupled_kappa1", 1.0, False),
    ("driven_cavity_kappa0_5", 0.5, True),
):
    rows = []
    for index, dt in enumerate((0.2, 0.1, 0.05)):
        result = run_directions(
            Config(dt=dt, use_mode_coupling=True),
            kappa,
            cavity=cavity,
            epsilons=(1e-7,),
            directions=4,
            seed_base=2_026_075_000 + index * 100,
        )["1e-07"]
        rows.append({"dt": dt, **result})
    dt_sensitivity[regime_name] = rows

horizon_sensitivity = []
for index, measure_time in enumerate((20.0, 40.0, 80.0)):
    result = run_directions(
        Config(dt=0.1, use_mode_coupling=True),
        1.0,
        measure_time=measure_time,
        epsilons=(1e-7,),
        directions=4,
        seed_base=2_026_076_000 + index * 100,
    )["1e-07"]
    horizon_sensitivity.append({"measure_time": measure_time, **result})

grid_sensitivity = []
for index, size in enumerate((16, 24)):
    result = run_directions(
        Config(dt=0.1, use_mode_coupling=True),
        1.0,
        size=size,
        epsilons=(1e-7,),
        directions=4,
        seed_base=2_026_077_000 + index * 100,
    )["1e-07"]
    grid_sensitivity.append({"size": size, **result})

all_primary_values = [
    value
    for regime in primary.values()
    for epsilon in regime.values()
    for value in epsilon["direction_exponents"]
]

output = {
    "configuration": {
        "primary_size": PRIMARY_SIZE,
        "primary_burn_time": PRIMARY_BURN_TIME,
        "primary_measure_time": PRIMARY_MEASURE_TIME,
        "primary_directions": PRIMARY_DIRECTIONS,
        "primary_epsilons": list(PRIMARY_EPSILONS),
        "distance": "Euclidean norm of psi.real, psi.imag, phi, and mu when enabled",
        "initial_perturbation": "psi-only random unit direction",
        "renormalization": "every update, full-state difference restored to epsilon",
    },
    "controls": {
        "logistic_r4_exact": float(np.log(2.0)),
        "logistic_r4_benettin": {
            f"{epsilon:.0e}": logistic_benettin(epsilon)
            for epsilon in PRIMARY_EPSILONS
        },
        "zero_kappa_expected_psi_damping_exponent": float(
            np.log(1.0 - 0.005 * 0.1) / 0.1
        ),
    },
    "primary_regimes": primary,
    "primary_summary": {
        "estimates": len(all_primary_values),
        "positive_estimates": int(
            np.sum(np.asarray(all_primary_values) > 0.0)
        ),
        "minimum": float(np.min(all_primary_values)),
        "maximum": float(np.max(all_primary_values)),
    },
    "kappa_sweep": kappa_sweep,
    "dt_sensitivity_fixed_physical_times": dt_sensitivity,
    "horizon_sensitivity": horizon_sensitivity,
    "grid_sensitivity": grid_sensitivity,
}

print(json.dumps(output, indent=2, sort_keys=True))
```

### H.2 Full reference output

**Normalized execution-output SHA-256:** `71ea4d98cc7aebbb3b7bd5c8134bea3c7793ab33c5cd7f0428f38c6a0d01dfa6`

```json
{
  "configuration": {
    "distance": "Euclidean norm of psi.real, psi.imag, phi, and mu when enabled",
    "initial_perturbation": "psi-only random unit direction",
    "primary_burn_time": 10.0,
    "primary_directions": 6,
    "primary_epsilons": [
      1e-07,
      1e-09
    ],
    "primary_measure_time": 40.0,
    "primary_size": 16,
    "renormalization": "every update, full-state difference restored to epsilon"
  },
  "controls": {
    "logistic_r4_benettin": {
      "1e-07": 0.6930771848594827,
      "1e-09": 0.6930771978175649
    },
    "logistic_r4_exact": 0.6931471805599453,
    "zero_kappa_expected_psi_damping_exponent": -0.005001250416822429
  },
  "dt_sensitivity_fixed_physical_times": {
    "driven_cavity_kappa0_5": [
      {
        "direction_exponents": [
          -0.05797564834895337,
          -0.058104570831719604,
          -0.05873141203357981,
          -0.06080728691690947
        ],
        "dt": 0.2,
        "summary": {
          "count": 4,
          "maximum": -0.05797564834895337,
          "mean": -0.058904729532790565,
          "minimum": -0.06080728691690947,
          "positive_count": 0,
          "standard_deviation": 0.0013106244502091257
        },
        "total_cap_triggers": 0
      },
      {
        "direction_exponents": [
          -0.0634698002405728,
          -0.05690858495749823,
          -0.05713810029174815,
          -0.05830415997334317
        ],
        "dt": 0.1,
        "summary": {
          "count": 4,
          "maximum": -0.05690858495749823,
          "mean": -0.05895516136579059,
          "minimum": -0.0634698002405728,
          "positive_count": 0,
          "standard_deviation": 0.0030711535793814465
        },
        "total_cap_triggers": 0
      },
      {
        "direction_exponents": [
          -0.05480810782135805,
          -0.05751447311323697,
          -0.057819788697932493,
          -0.0572072820461285
        ],
        "dt": 0.05,
        "summary": {
          "count": 4,
          "maximum": -0.05480810782135805,
          "mean": -0.056837412919664,
          "minimum": -0.057819788697932493,
          "positive_count": 0,
          "standard_deviation": 0.0013757852337449358
        },
        "total_cap_triggers": 0
      }
    ],
    "mode_coupled_kappa1": [
      {
        "direction_exponents": [
          -0.041386441933556305,
          -0.04084422255965535,
          -0.04614599699650241,
          -0.042795127175366085
        ],
        "dt": 0.2,
        "summary": {
          "count": 4,
          "maximum": -0.04084422255965535,
          "mean": -0.04279294716627004,
          "minimum": -0.04614599699650241,
          "positive_count": 0,
          "standard_deviation": 0.002381787317578803
        },
        "total_cap_triggers": 0
      },
      {
        "direction_exponents": [
          -0.046234073701521286,
          -0.04174644540426181,
          -0.03625068295951662,
          -0.04180838924226665
        ],
        "dt": 0.1,
        "summary": {
          "count": 4,
          "maximum": -0.03625068295951662,
          "mean": -0.041509897826891594,
          "minimum": -0.046234073701521286,
          "positive_count": 0,
          "standard_deviation": 0.004087469901910126
        },
        "total_cap_triggers": 0
      },
      {
        "direction_exponents": [
          -0.040952377982360594,
          -0.03720986139983058,
          -0.045624093269673115,
          -0.05188535002173687
        ],
        "dt": 0.05,
        "summary": {
          "count": 4,
          "maximum": -0.03720986139983058,
          "mean": -0.04391792066840029,
          "minimum": -0.05188535002173687,
          "positive_count": 0,
          "standard_deviation": 0.0063293880172601985
        },
        "total_cap_triggers": 0
      }
    ]
  },
  "grid_sensitivity": [
    {
      "direction_exponents": [
        -0.044792491376354035,
        -0.04011884184079961,
        -0.04423087145390178,
        -0.0456229181028834
      ],
      "size": 16,
      "summary": {
        "count": 4,
        "maximum": -0.04011884184079961,
        "mean": -0.043691280693484706,
        "minimum": -0.0456229181028834,
        "positive_count": 0,
        "standard_deviation": 0.002449310487624051
      },
      "total_cap_triggers": 0
    },
    {
      "direction_exponents": [
        -0.04315690103816857,
        -0.04071718563056873,
        -0.04332581083525892,
        -0.0443600110271271
      ],
      "size": 24,
      "summary": {
        "count": 4,
        "maximum": -0.04071718563056873,
        "mean": -0.042889977132780824,
        "minimum": -0.0443600110271271,
        "positive_count": 0,
        "standard_deviation": 0.0015430729028030569
      },
      "total_cap_triggers": 0
    }
  ],
  "horizon_sensitivity": [
    {
      "direction_exponents": [
        -0.08085777498935184,
        -0.0786893312646256,
        -0.08352529673858482,
        -0.08909869424875397
      ],
      "measure_time": 20.0,
      "summary": {
        "count": 4,
        "maximum": -0.0786893312646256,
        "mean": -0.08304277431032905,
        "minimum": -0.08909869424875397,
        "positive_count": 0,
        "standard_deviation": 0.004495689883256217
      },
      "total_cap_triggers": 0
    },
    {
      "direction_exponents": [
        -0.03928570672608923,
        -0.042184106910397125,
        -0.045520898909569014,
        -0.045723852802712205
      ],
      "measure_time": 40.0,
      "summary": {
        "count": 4,
        "maximum": -0.03928570672608923,
        "mean": -0.043178641337191896,
        "minimum": -0.045723852802712205,
        "positive_count": 0,
        "standard_deviation": 0.003060953585185238
      },
      "total_cap_triggers": 0
    },
    {
      "direction_exponents": [
        -0.028717516164470935,
        -0.021611878590722257,
        -0.022581187033923547,
        -0.025464638753483232
      ],
      "measure_time": 80.0,
      "summary": {
        "count": 4,
        "maximum": -0.021611878590722257,
        "mean": -0.024593805135649995,
        "minimum": -0.028717516164470935,
        "positive_count": 0,
        "standard_deviation": 0.003199263528892737
      },
      "total_cap_triggers": 0
    }
  ],
  "kappa_sweep": [
    {
      "direction_exponents": [
        -0.005001250390692494,
        -0.005001250255915015,
        -0.005001251390008718
      ],
      "kappa": 0.0,
      "summary": {
        "count": 3,
        "maximum": -0.005001250255915015,
        "mean": -0.005001250678872075,
        "minimum": -0.005001251390008718,
        "positive_count": 0,
        "standard_deviation": 6.195383242529992e-10
      },
      "total_cap_triggers": 0
    },
    {
      "direction_exponents": [
        -0.013471560385731987,
        -0.013377698922662268,
        -0.013225423422978938
      ],
      "kappa": 0.25,
      "summary": {
        "count": 3,
        "maximum": -0.013225423422978938,
        "mean": -0.013358227577124397,
        "minimum": -0.013471560385731987,
        "positive_count": 0,
        "standard_deviation": 0.0001242183604831236
      },
      "total_cap_triggers": 0
    },
    {
      "direction_exponents": [
        -0.02740759093379085,
        -0.02616350749104369,
        -0.03131641585246586
      ],
      "kappa": 0.5,
      "summary": {
        "count": 3,
        "maximum": -0.02616350749104369,
        "mean": -0.028295838092433467,
        "minimum": -0.03131641585246586,
        "positive_count": 0,
        "standard_deviation": 0.002688838672444136
      },
      "total_cap_triggers": 0
    },
    {
      "direction_exponents": [
        -0.038960759362195924,
        -0.03719425726590857,
        -0.04225934536833826
      ],
      "kappa": 0.75,
      "summary": {
        "count": 3,
        "maximum": -0.03719425726590857,
        "mean": -0.03947145399881425,
        "minimum": -0.04225934536833826,
        "positive_count": 0,
        "standard_deviation": 0.0025708726398339433
      },
      "total_cap_triggers": 0
    },
    {
      "direction_exponents": [
        -0.04504794127202338,
        -0.05310637073284753,
        -0.04490120619626167
      ],
      "kappa": 1.0,
      "summary": {
        "count": 3,
        "maximum": -0.04490120619626167,
        "mean": -0.04768517273371086,
        "minimum": -0.05310637073284753,
        "positive_count": 0,
        "standard_deviation": 0.004695468411670692
      },
      "total_cap_triggers": 0
    }
  ],
  "primary_regimes": {
    "continuous_mode_coupled_kappa0_5": {
      "1e-07": {
        "direction_exponents": [
          -0.029315856970737957,
          -0.02963629782517984,
          -0.028913689584494078,
          -0.02787757553943717,
          -0.029106050553867002,
          -0.03252536887208958
        ],
        "summary": {
          "count": 6,
          "maximum": -0.02787757553943717,
          "mean": -0.029562473224300934,
          "minimum": -0.03252536887208958,
          "positive_count": 0,
          "standard_deviation": 0.0015692764155321786
        },
        "total_cap_triggers": 0
      },
      "1e-09": {
        "direction_exponents": [
          -0.0293157823701915,
          -0.029636338483020754,
          -0.028913652081129983,
          -0.027877589649729185,
          -0.029106032735750666,
          -0.03252531895568592
        ],
        "summary": {
          "count": 6,
          "maximum": -0.027877589649729185,
          "mean": -0.02956245237925133,
          "minimum": -0.03252531895568592,
          "positive_count": 0,
          "standard_deviation": 0.0015692614017174733
        },
        "total_cap_triggers": 0
      }
    },
    "continuous_mode_coupled_kappa1": {
      "1e-07": {
        "direction_exponents": [
          -0.03990891034134706,
          -0.04182109640813812,
          -0.04082093098801403,
          -0.04870481049349974,
          -0.047413745315333204,
          -0.043405752046789106
        ],
        "summary": {
          "count": 6,
          "maximum": -0.03990891034134706,
          "mean": -0.04367920759885355,
          "minimum": -0.04870481049349974,
          "positive_count": 0,
          "standard_deviation": 0.0036087587378636227
        },
        "total_cap_triggers": 0
      },
      "1e-09": {
        "direction_exponents": [
          -0.03990891786477703,
          -0.04182113565177527,
          -0.04082094781156844,
          -0.048704935012313696,
          -0.047413720439268524,
          -0.04340576908891005
        ],
        "summary": {
          "count": 6,
          "maximum": -0.03990891786477703,
          "mean": -0.04367923764476884,
          "minimum": -0.048704935012313696,
          "positive_count": 0,
          "standard_deviation": 0.003608779734313135
        },
        "total_cap_triggers": 0
      }
    },
    "continuous_mode_coupled_mu_kappa1": {
      "1e-07": {
        "direction_exponents": [
          -0.04616703206008482,
          -0.04673917408780528,
          -0.03661455440608542,
          -0.039453139803257334,
          -0.042404113191353905,
          -0.0434243043020033
        ],
        "summary": {
          "count": 6,
          "maximum": -0.03661455440608542,
          "mean": -0.04246705297509834,
          "minimum": -0.04673917408780528,
          "positive_count": 0,
          "standard_deviation": 0.0039037563360924013
        },
        "total_cap_triggers": 0
      },
      "1e-09": {
        "direction_exponents": [
          -0.0461671200485302,
          -0.04673917423634246,
          -0.0366145606700027,
          -0.039453092366213555,
          -0.04240408870503252,
          -0.04342426722978245
        ],
        "summary": {
          "count": 6,
          "maximum": -0.0366145606700027,
          "mean": -0.042467050542650646,
          "minimum": -0.04673917423634246,
          "positive_count": 0,
          "standard_deviation": 0.003903776755410622
        },
        "total_cap_triggers": 0
      }
    },
    "driven_cavity_continuous_kappa0_5": {
      "1e-07": {
        "direction_exponents": [
          -0.056103052795666464,
          -0.05901453446855691,
          -0.05792863001871644,
          -0.06044662463588753,
          -0.05993750573729979,
          -0.05991419630262631
        ],
        "summary": {
          "count": 6,
          "maximum": -0.056103052795666464,
          "mean": -0.058890757326458903,
          "minimum": -0.06044662463588753,
          "positive_count": 0,
          "standard_deviation": 0.0016294869711842182
        },
        "total_cap_triggers": 0
      },
      "1e-09": {
        "direction_exponents": [
          -0.05610301700345035,
          -0.059014503249179784,
          -0.05792861037039308,
          -0.06044663723779249,
          -0.05993751499061558,
          -0.05991419320966627
        ],
        "summary": {
          "count": 6,
          "maximum": -0.05610301700345035,
          "mean": -0.058890746010182925,
          "minimum": -0.06044663723779249,
          "positive_count": 0,
          "standard_deviation": 0.0016295042705813845
        },
        "total_cap_triggers": 0
      }
    },
    "legacy_mode_coupled_kappa1": {
      "1e-07": {
        "direction_exponents": [
          -0.044794181558056013,
          -0.04806859085757653,
          -0.04875196665488706,
          -0.04289885474583912,
          -0.04290689433849633,
          -0.043825302376545694
        ],
        "summary": {
          "count": 6,
          "maximum": -0.04289885474583912,
          "mean": -0.04520763175523346,
          "minimum": -0.04875196665488706,
          "positive_count": 0,
          "standard_deviation": 0.0025866200487429025
        },
        "total_cap_triggers": 0
      },
      "1e-09": {
        "direction_exponents": [
          -0.04479415200136283,
          -0.04806864901337817,
          -0.048751837259135455,
          -0.04289877765196667,
          -0.042906929199715185,
          -0.04382533681452564
        ],
        "summary": {
          "count": 6,
          "maximum": -0.04289877765196667,
          "mean": -0.04520761365668066,
          "minimum": -0.048751837259135455,
          "positive_count": 0,
          "standard_deviation": 0.002586602278373438
        },
        "total_cap_triggers": 0
      }
    },
    "rd0_continuous_kappa1": {
      "1e-07": {
        "direction_exponents": [
          -0.02927615051022366,
          -0.020017009325964973,
          -0.01998092959879665,
          -0.009980079807697457,
          -0.008199790453747007,
          -0.02510024023748387
        ],
        "summary": {
          "count": 6,
          "maximum": -0.008199790453747007,
          "mean": -0.018759033322318933,
          "minimum": -0.02927615051022366,
          "positive_count": 0,
          "standard_deviation": 0.00827603562088332
        },
        "total_cap_triggers": 0
      },
      "1e-09": {
        "direction_exponents": [
          -0.029275996446843488,
          -0.020016930764872428,
          -0.019981111789884813,
          -0.009979971243380506,
          -0.008199807954127026,
          -0.025099837011166713
        ],
        "summary": {
          "count": 6,
          "maximum": -0.008199807954127026,
          "mean": -0.018758942535045828,
          "minimum": -0.029275996446843488,
          "positive_count": 0,
          "standard_deviation": 0.008275956232999954
        },
        "total_cap_triggers": 0
      }
    },
    "zero_kappa_damping_control": {
      "1e-07": {
        "direction_exponents": [
          -0.00500125069237188,
          -0.005001249909194006,
          -0.0050012511945918894,
          -0.0050012507378233055,
          -0.005001249521201461,
          -0.0050012502776012
        ],
        "summary": {
          "count": 6,
          "maximum": -0.005001249521201461,
          "mean": -0.00500125038879729,
          "minimum": -0.0050012511945918894,
          "positive_count": 0,
          "standard_deviation": 6.096536773276858e-10
        },
        "total_cap_triggers": 0
      },
      "1e-09": {
        "direction_exponents": [
          -0.005001222715633557,
          -0.00500131464421693,
          -0.005001258790769377,
          -0.0050013434622858885,
          -0.005001275531787884,
          -0.005001271535999228
        ],
        "summary": {
          "count": 6,
          "maximum": -0.005001222715633557,
          "mean": -0.005001281113448811,
          "minimum": -0.0050013434622858885,
          "positive_count": 0,
          "standard_deviation": 4.252805948627736e-08
        },
        "total_cap_triggers": 0
      }
    }
  },
  "primary_summary": {
    "estimates": 84,
    "maximum": -0.005001222715633557,
    "minimum": -0.06044663723779249,
    "positive_estimates": 0
  }
}
```

## Appendix I — Observable Foam-Source Signature Protocol

This appendix validates an offline observation protocol for five declared source families and then characterizes the isolated current F0 source. It contains the original decision-rule failure, the recorded correction, a separate post-revision audit, analytical controls, and explicit identifiability boundaries. It requires Python 3 and NumPy, reads no project data, and writes no files.

### I.1 Complete executable program

**Embedded program SHA-256 after LF normalization:** `86a836a40fe11aa1f6ef1408cb720a0381a5432535db95a4ec3f70ae6d295c8f`

```python
"""Standalone validation of observable signatures for candidate foam sources."""

from __future__ import annotations

import json
import math

import numpy as np


PRIMARY_DT = 0.1
PRIMARY_TIME = 100.0
PRIMARY_REPLICATES = 16
SENSITIVITY_TIME = 50.0
SENSITIVITY_REPLICATES = 12
GRID_SIZE = 8
SOURCE_SIGMA = 0.005
POISSON_RATE = 0.5
MEMORY_TIME = 0.5
HAWKES_BRANCHING_RATIO = 0.6
STATE_COEFFICIENT = 0.9
EVENT_THRESHOLD_SIGMA = 2.5
FANO_WINDOW_TIME = 2.0
T_CRITICAL_DF15 = 2.131449545559323
T_CRITICAL_DF11 = 2.200985160082949
CANDIDATES = (
    "F1_initial_only",
    "F2_gaussian_white",
    "F3_poisson_events",
    "F4_state_hawkes_events",
    "F5_colored_memory",
)


def state_fixture(size):
    y, x = np.mgrid[:size, :size]
    amplitude = (
        0.02
        + 0.006 * np.cos(2.0 * np.pi * x / size)
        + 0.004 * np.sin(2.0 * np.pi * y / size)
    )
    grad_y, grad_x = np.gradient(amplitude)
    source_state = amplitude + np.sqrt(grad_x**2 + grad_y**2)
    score = (source_state - np.mean(source_state)) / np.std(source_state)
    return amplitude, source_state, score


def candidate_residuals(
    candidate,
    dt,
    physical_time,
    replicates,
    seed,
    poisson_rate=POISSON_RATE,
    memory_time=MEMORY_TIME,
    hawkes_branching_ratio=HAWKES_BRANCHING_RATIO,
    state_coefficient=STATE_COEFFICIENT,
):
    steps = round(physical_time / dt)
    shape = (replicates, steps, GRID_SIZE, GRID_SIZE)
    rng = np.random.RandomState(seed)
    _, _, state_score = state_fixture(GRID_SIZE)

    if candidate == "F1_initial_only":
        residuals = np.zeros(shape, dtype=np.float64)
    elif candidate == "F2_gaussian_white":
        residuals = SOURCE_SIGMA * np.sqrt(dt) * rng.normal(size=shape)
    elif candidate == "F3_poisson_events":
        jump = SOURCE_SIGMA / np.sqrt(poisson_rate)
        positive = rng.poisson(poisson_rate * dt / 2.0, size=shape)
        negative = rng.poisson(poisson_rate * dt / 2.0, size=shape)
        residuals = jump * (positive - negative)
    elif candidate == "F4_state_hawkes_events":
        decay = np.exp(-dt / memory_time)
        alpha = (
            hawkes_branching_ratio * (1.0 - decay) / dt
        )
        base_mean = poisson_rate * (1.0 - hawkes_branching_ratio)
        state_multiplier = np.exp(state_coefficient * state_score)
        state_multiplier /= np.mean(state_multiplier)
        baseline = base_mean * state_multiplier
        excitation = np.zeros(
            (replicates, GRID_SIZE, GRID_SIZE), dtype=np.float64
        )
        jump = SOURCE_SIGMA / np.sqrt(poisson_rate)
        residuals = np.empty(shape, dtype=np.float64)
        for step in range(steps):
            intensity = baseline + excitation
            positive = rng.poisson(intensity * dt / 2.0)
            negative = rng.poisson(intensity * dt / 2.0)
            event_count = positive + negative
            residuals[:, step] = jump * (positive - negative)
            excitation = decay * excitation + alpha * event_count
    elif candidate == "F5_colored_memory":
        rho = np.exp(-dt / memory_time)
        innovation_scale = np.sqrt(1.0 - rho**2)
        eta = rng.normal(size=(replicates, GRID_SIZE, GRID_SIZE))
        forcing = SOURCE_SIGMA / np.sqrt(PRIMARY_DT)
        residuals = np.empty(shape, dtype=np.float64)
        for step in range(steps):
            eta = rho * eta + innovation_scale * rng.normal(size=eta.shape)
            residuals[:, step] = forcing * dt * eta
    else:
        raise ValueError(candidate)

    return residuals, np.broadcast_to(
        state_score, (steps, GRID_SIZE, GRID_SIZE)
    )


def current_f0_residuals(dt, physical_time, replicates, seed):
    steps = round(physical_time / dt)
    rng = np.random.RandomState(seed)
    amplitude, source_state, state_score = state_fixture(GRID_SIZE)
    probability = 1.0 / (1.0 + np.exp(-5.0 * source_state))
    linon_amplitude = 0.03 + 0.02 * amplitude
    shape = (replicates, steps, GRID_SIZE, GRID_SIZE)
    linons = rng.rand(*shape) < probability
    gaussian = rng.normal(0.0, SOURCE_SIGMA, size=shape)
    residuals = dt * (
        linon_amplitude * (linons - probability) + gaussian
    )
    return residuals, np.broadcast_to(
        state_score, (steps, GRID_SIZE, GRID_SIZE)
    )


def correlation(left, right):
    left = np.asarray(left, dtype=np.float64).ravel()
    right = np.asarray(right, dtype=np.float64).ravel()
    left -= np.mean(left)
    right -= np.mean(right)
    denominator = np.sqrt(np.sum(left**2) * np.sum(right**2))
    if denominator == 0.0:
        return 0.0
    return float(np.sum(left * right) / denominator)


def waiting_time_cv(events, dt):
    gaps = []
    for y in range(events.shape[1]):
        for x in range(events.shape[2]):
            indices = np.flatnonzero(events[:, y, x])
            if len(indices) >= 3:
                gaps.extend(np.diff(indices) * dt)
    if len(gaps) < 2 or np.mean(gaps) == 0.0:
        return 0.0
    return float(np.std(gaps, ddof=1) / np.mean(gaps))


def safe_rate_ratio(
    numerator_events,
    numerator_total,
    denominator_events,
    denominator_total,
):
    if (
        numerator_total < 20
        or denominator_total < 20
        or numerator_events + denominator_events < 20
    ):
        return 1.0
    numerator_rate = (numerator_events + 0.5) / (numerator_total + 1.0)
    denominator_rate = (denominator_events + 0.5) / (
        denominator_total + 1.0
    )
    return float(numerator_rate / denominator_rate)


def replicate_features(residuals, state_score, dt):
    rms = float(np.sqrt(np.mean(residuals**2)))
    if rms < 1e-15:
        return {
            "innovation_rms": rms,
            "one_step_variance_rate": 0.0,
            "one_unit_variance_rate": 0.0,
            "excess_kurtosis": 0.0,
            "signed_lag1_correlation": 0.0,
            "absolute_lag1_correlation": 0.0,
            "tail_fraction": 0.0,
            "event_count_fano": 0.0,
            "waiting_time_cv": 0.0,
            "history_rate_ratio": 0.0,
            "state_rate_ratio": 0.0,
        }

    centered = residuals - np.mean(residuals)
    variance = float(np.mean(centered**2))
    standardized = centered / np.sqrt(variance)
    excess_kurtosis = float(np.mean(standardized**4) - 3.0)
    signed_lag1 = correlation(centered[:-1], centered[1:])
    absolute_lag1 = correlation(
        np.abs(centered[:-1]), np.abs(centered[1:])
    )
    events = np.abs(standardized) > EVENT_THRESHOLD_SIGMA
    tail_fraction = float(np.mean(events))

    window_steps = max(1, round(FANO_WINDOW_TIME / dt))
    usable_steps = events.shape[0] // window_steps * window_steps
    window_counts = events[:usable_steps].reshape(
        -1, window_steps, GRID_SIZE, GRID_SIZE
    ).sum(axis=(1, 2, 3))
    event_count_fano = (
        float(np.var(window_counts, ddof=1) / np.mean(window_counts))
        if (
            len(window_counts) > 1
            and np.mean(window_counts) > 0.0
            and np.sum(window_counts) >= 20
        )
        else 0.0
    )

    previous = events[:-1]
    following = events[1:]
    history_rate_ratio = safe_rate_ratio(
        np.sum(following & previous),
        np.sum(previous),
        np.sum(following & ~previous),
        np.sum(~previous),
    )

    high_state = state_score > np.quantile(state_score, 0.75)
    low_state = state_score < np.quantile(state_score, 0.25)
    state_rate_ratio = safe_rate_ratio(
        np.sum(events & high_state),
        np.sum(high_state),
        np.sum(events & low_state),
        np.sum(low_state),
    )

    unit_steps = max(1, round(1.0 / dt))
    usable_unit_steps = residuals.shape[0] // unit_steps * unit_steps
    unit_sums = residuals[:usable_unit_steps].reshape(
        -1, unit_steps, GRID_SIZE, GRID_SIZE
    ).sum(axis=1)
    one_unit_variance_rate = float(np.var(unit_sums, ddof=1))

    return {
        "innovation_rms": rms,
        "one_step_variance_rate": variance / dt,
        "one_unit_variance_rate": one_unit_variance_rate,
        "excess_kurtosis": excess_kurtosis,
        "signed_lag1_correlation": signed_lag1,
        "absolute_lag1_correlation": absolute_lag1,
        "tail_fraction": tail_fraction,
        "event_count_fano": event_count_fano,
        "waiting_time_cv": waiting_time_cv(events, dt),
        "history_rate_ratio": history_rate_ratio,
        "state_rate_ratio": state_rate_ratio,
    }


def feature_rows(residuals, state_score, dt):
    return [
        replicate_features(residuals[index], state_score, dt)
        for index in range(residuals.shape[0])
    ]


def interval(values):
    values = np.asarray(values, dtype=np.float64)
    mean = float(np.mean(values))
    if len(values) == 1:
        return {
            "mean": mean,
            "standard_deviation": 0.0,
            "lower_95_t": mean,
            "upper_95_t": mean,
        }
    standard_deviation = float(np.std(values, ddof=1))
    standard_error = standard_deviation / np.sqrt(len(values))
    critical = (
        T_CRITICAL_DF15
        if len(values) == PRIMARY_REPLICATES
        else T_CRITICAL_DF11
    )
    return {
        "mean": mean,
        "standard_deviation": standard_deviation,
        "lower_95_t": mean - critical * standard_error,
        "upper_95_t": mean + critical * standard_error,
    }


def summarize(rows):
    return {
        metric: interval([row[metric] for row in rows])
        for metric in rows[0]
    }


def classify_original(row):
    if row["innovation_rms"] < 1e-15:
        return "F1_initial_only"
    if row["signed_lag1_correlation"] > 0.3:
        return "F5_colored_memory"
    if row["excess_kurtosis"] < 2.0:
        return "F2_gaussian_white"
    if (
        row["state_rate_ratio"] > 1.5
        or row["history_rate_ratio"] > 1.5
        or row["event_count_fano"] > 1.3
    ):
        return "F4_state_hawkes_events"
    return "F3_poisson_events"


def classify_revised(row):
    if row["innovation_rms"] < 1e-15:
        return "F1_initial_only"
    if row["signed_lag1_correlation"] > 0.3:
        return "F5_colored_memory"
    if row["excess_kurtosis"] < 2.0:
        return "F2_gaussian_white"
    if (
        row["state_rate_ratio"] > 1.5
        or row["history_rate_ratio"] > 1.5
    ):
        return "F4_state_hawkes_events"
    return "F3_poisson_events"


def classification_counts(rows, classifier):
    counts = {candidate: 0 for candidate in CANDIDATES}
    for row in rows:
        counts[classifier(row)] += 1
    return counts


def run_candidate_set(dt, physical_time, replicates, seed_offset):
    summaries = {}
    original_classifications = {}
    revised_classifications = {}
    for index, candidate in enumerate(CANDIDATES):
        residuals, score = candidate_residuals(
            candidate,
            dt,
            physical_time,
            replicates,
            seed_offset + index * 10_000,
        )
        rows = feature_rows(residuals, score, dt)
        summaries[candidate] = summarize(rows)
        original_classifications[candidate] = classification_counts(
            rows, classify_original
        )
        revised_classifications[candidate] = classification_counts(
            rows, classify_revised
        )
    return summaries, {
        "original": original_classifications,
        "revised": revised_classifications,
    }


def intervals_overlap(left, right):
    return not (
        left["upper_95_t"] < right["lower_95_t"]
        or right["upper_95_t"] < left["lower_95_t"]
    )


def pair_check(summaries, left, right, metric):
    left_interval = summaries[left][metric]
    right_interval = summaries[right][metric]
    return {
        "left": left,
        "right": right,
        "pre_registered_metric": metric,
        "left_interval": left_interval,
        "right_interval": right_interval,
        "intervals_overlap": intervals_overlap(
            left_interval, right_interval
        ),
    }


calibration_summaries, calibration_classification = run_candidate_set(
    PRIMARY_DT,
    PRIMARY_TIME,
    PRIMARY_REPLICATES,
    2_026_078_000,
)
validation_summaries, validation_classification = run_candidate_set(
    PRIMARY_DT,
    PRIMARY_TIME,
    PRIMARY_REPLICATES,
    2_026_088_000,
)

pre_registered_pair_checks = [
    pair_check(
        validation_summaries,
        "F1_initial_only",
        "F2_gaussian_white",
        "innovation_rms",
    ),
    pair_check(
        validation_summaries,
        "F2_gaussian_white",
        "F3_poisson_events",
        "excess_kurtosis",
    ),
    pair_check(
        validation_summaries,
        "F2_gaussian_white",
        "F5_colored_memory",
        "signed_lag1_correlation",
    ),
    pair_check(
        validation_summaries,
        "F3_poisson_events",
        "F4_state_hawkes_events",
        "state_rate_ratio",
    ),
]

dt_sensitivity = {}
for dt_index, dt in enumerate((0.2, 0.1, 0.05)):
    summaries, classifications = run_candidate_set(
        dt,
        SENSITIVITY_TIME,
        SENSITIVITY_REPLICATES,
        2_026_098_000 + dt_index * 100_000,
    )
    dt_sensitivity[f"{dt:.2f}"] = {
        "summaries": summaries,
        "classification_counts": classifications,
    }

audit_dt_sensitivity = {}
for dt_index, dt in enumerate((0.2, 0.1, 0.05)):
    summaries, classifications = run_candidate_set(
        dt,
        SENSITIVITY_TIME,
        SENSITIVITY_REPLICATES,
        2_026_208_000 + dt_index * 100_000,
    )
    audit_dt_sensitivity[f"{dt:.2f}"] = {
        "summaries": summaries,
        "classification_counts": classifications,
    }

memory_resolution_sweep = []
for index, memory_time in enumerate((0.02, 0.05, 0.1, 0.2, 0.5)):
    residuals, score = candidate_residuals(
        "F5_colored_memory",
        PRIMARY_DT,
        SENSITIVITY_TIME,
        SENSITIVITY_REPLICATES,
        2_026_408_000 + index * 10_000,
        memory_time=memory_time,
    )
    rows = feature_rows(residuals, score, PRIMARY_DT)
    summary = summarize(rows)
    memory_resolution_sweep.append(
        {
            "memory_time": memory_time,
            "memory_to_observation_step_ratio": (
                memory_time / PRIMARY_DT
            ),
            "expected_lag1_correlation": float(
                np.exp(-PRIMARY_DT / memory_time)
            ),
            "observed_lag1_interval": summary[
                "signed_lag1_correlation"
            ],
            "revised_classification_counts": classification_counts(
                rows, classify_revised
            ),
        }
    )

poisson_resolution_sweep = []
for index, poisson_rate in enumerate((0.25, 0.5, 1.0, 2.0, 5.0, 10.0)):
    residuals, score = candidate_residuals(
        "F3_poisson_events",
        PRIMARY_DT,
        SENSITIVITY_TIME,
        SENSITIVITY_REPLICATES,
        2_026_508_000 + index * 10_000,
        poisson_rate=poisson_rate,
    )
    rows = feature_rows(residuals, score, PRIMARY_DT)
    summary = summarize(rows)
    poisson_resolution_sweep.append(
        {
            "poisson_rate": poisson_rate,
            "expected_excess_kurtosis": (
                1.0 / (poisson_rate * PRIMARY_DT)
            ),
            "observed_excess_kurtosis_interval": summary[
                "excess_kurtosis"
            ],
            "revised_classification_counts": classification_counts(
                rows, classify_revised
            ),
        }
    )

event_dependence_sweep = []
for index, (branching_ratio, state_coefficient) in enumerate(
    (
        (0.0, 0.0),
        (0.1, 0.0),
        (0.3, 0.0),
        (0.6, 0.0),
        (0.0, 0.3),
        (0.0, 0.9),
        (0.3, 0.3),
    )
):
    residuals, score = candidate_residuals(
        "F4_state_hawkes_events",
        PRIMARY_DT,
        SENSITIVITY_TIME,
        SENSITIVITY_REPLICATES,
        2_026_608_000 + index * 10_000,
        hawkes_branching_ratio=branching_ratio,
        state_coefficient=state_coefficient,
    )
    rows = feature_rows(residuals, score, PRIMARY_DT)
    summary = summarize(rows)
    event_dependence_sweep.append(
        {
            "hawkes_branching_ratio": branching_ratio,
            "state_coefficient": state_coefficient,
            "history_rate_ratio_interval": summary[
                "history_rate_ratio"
            ],
            "state_rate_ratio_interval": summary[
                "state_rate_ratio"
            ],
            "revised_classification_counts": classification_counts(
                rows, classify_revised
            ),
        }
    )

current_f0 = {}
f0_variance_rates = []
for dt_index, dt in enumerate((0.2, 0.1, 0.05, 0.025)):
    residuals, score = current_f0_residuals(
        dt,
        SENSITIVITY_TIME,
        SENSITIVITY_REPLICATES,
        2_026_108_000 + dt_index * 100_000,
    )
    rows = feature_rows(residuals, score, dt)
    summary = summarize(rows)
    current_f0[f"{dt:.3f}"] = summary
    f0_variance_rates.append(
        summary["one_step_variance_rate"]["mean"]
    )

f0_variance_rate_exponent = float(
    np.polyfit(
        np.log(np.asarray((0.2, 0.1, 0.05, 0.025))),
        np.log(np.asarray(f0_variance_rates)),
        1,
    )[0]
)

amplitude, source_state, _ = state_fixture(GRID_SIZE)
probability = 1.0 / (1.0 + np.exp(-5.0 * source_state))
linon_amplitude = 0.03 + 0.02 * amplitude
f0_variance_coefficient = float(
    np.mean(
        linon_amplitude**2 * probability * (1.0 - probability)
        + SOURCE_SIGMA**2
    )
)

def score_classifications(classifications, replicates):
    correct = sum(
        classifications[candidate][candidate]
        for candidate in CANDIDATES
    )
    total = len(CANDIDATES) * replicates
    return {
        "correct": correct,
        "total": total,
        "accuracy": correct / total,
    }


def score_dt_collection(collection, classifier_name):
    correct = 0
    total = 0
    for result in collection.values():
        classifications = result["classification_counts"][classifier_name]
        score = score_classifications(
            classifications, SENSITIVITY_REPLICATES
        )
        correct += score["correct"]
        total += score["total"]
    return {
        "correct": correct,
        "total": total,
        "accuracy": correct / total,
    }

output = {
    "schema": "lineum.foam-signature-protocol.v1",
    "configuration": {
        "primary_dt": PRIMARY_DT,
        "primary_physical_time": PRIMARY_TIME,
        "primary_replicates_per_candidate": PRIMARY_REPLICATES,
        "sensitivity_time_steps": [0.2, 0.1, 0.05],
        "sensitivity_physical_time": SENSITIVITY_TIME,
        "sensitivity_replicates_per_candidate": SENSITIVITY_REPLICATES,
        "grid_size": GRID_SIZE,
        "source_sigma": SOURCE_SIGMA,
        "poisson_target_rate_per_cell_per_time": POISSON_RATE,
        "memory_time": MEMORY_TIME,
        "hawkes_branching_ratio": HAWKES_BRANCHING_RATIO,
        "state_coefficient": STATE_COEFFICIENT,
        "event_threshold_sigma": EVENT_THRESHOLD_SIGMA,
        "fano_window_time": FANO_WINDOW_TIME,
    },
    "original_pre_registered_decision_tree": [
        "innovation_rms < 1e-15 -> F1_initial_only",
        "signed_lag1_correlation > 0.3 -> F5_colored_memory",
        "excess_kurtosis < 2.0 -> F2_gaussian_white",
        (
            "state_rate_ratio > 1.5 OR history_rate_ratio > 1.5 "
            "OR event_count_fano > 1.3 -> F4_state_hawkes_events"
        ),
        "otherwise -> F3_poisson_events",
    ],
    "recorded_protocol_revision": {
        "failure": (
            "The original OR rule allowed a noisy Fano estimate from only "
            "25 windows to misclassify independent Poisson runs as F4."
        ),
        "change": (
            "Fano factor remains a supporting metric but cannot alone select "
            "F4; state-rate or event-history dependence must exceed 1.5."
        ),
        "revised_decision_tree": [
            "innovation_rms < 1e-15 -> F1_initial_only",
            "signed_lag1_correlation > 0.3 -> F5_colored_memory",
            "excess_kurtosis < 2.0 -> F2_gaussian_white",
            (
                "state_rate_ratio > 1.5 OR history_rate_ratio > 1.5 "
                "-> F4_state_hawkes_events"
            ),
            "otherwise -> F3_poisson_events",
        ],
        "audit_seed_family": "2026208000 plus fixed candidate and dt offsets",
    },
    "calibration_seed_family": {
        "summaries": calibration_summaries,
        "classification_counts": calibration_classification,
        "scores": {
            classifier_name: score_classifications(
                calibration_classification[classifier_name],
                PRIMARY_REPLICATES,
            )
            for classifier_name in ("original", "revised")
        },
    },
    "held_out_validation_seed_family": {
        "summaries": validation_summaries,
        "classification_counts": validation_classification,
        "scores": {
            classifier_name: score_classifications(
                validation_classification[classifier_name],
                PRIMARY_REPLICATES,
            )
            for classifier_name in ("original", "revised")
        },
    },
    "pre_registered_pair_checks": pre_registered_pair_checks,
    "dt_sensitivity": dt_sensitivity,
    "dt_sensitivity_classification_scores": {
        classifier_name: score_dt_collection(
            dt_sensitivity, classifier_name
        )
        for classifier_name in ("original", "revised")
    },
    "post_revision_audit_dt_sensitivity": audit_dt_sensitivity,
    "post_revision_audit_classification_scores": {
        classifier_name: score_dt_collection(
            audit_dt_sensitivity, classifier_name
        )
        for classifier_name in ("original", "revised")
    },
    "identifiability_boundaries": {
        "memory_resolution_sweep": memory_resolution_sweep,
        "poisson_resolution_sweep": poisson_resolution_sweep,
        "event_dependence_sweep": event_dependence_sweep,
        "interpretation": [
            (
                "Colored memory shorter than the observation interval can "
                "be observationally equivalent to white Gaussian forcing."
            ),
            (
                "High-rate small Poisson jumps approach a Gaussian law and "
                "cannot always be identified as discrete events."
            ),
            (
                "Weak state or history dependence can be observationally "
                "equivalent to independent Poisson events."
            ),
        ],
    },
    "current_f0_controlled_source": {
        "summaries_by_dt": current_f0,
        "analytic_pre_damping_variance_coefficient": (
            f0_variance_coefficient
        ),
        "expected_one_step_variance_rate": (
            "dt * analytic_pre_damping_variance_coefficient"
        ),
        "fitted_variance_rate_dt_exponent": f0_variance_rate_exponent,
        "interpretation": (
            "The isolated current source is an iid state-dependent Bernoulli "
            "plus Gaussian per-update law. Its one-step variance rate vanishes "
            "linearly as dt decreases and is outside F1-F5 continuous controls."
        ),
    },
    "limitations": [
        (
            "Synthetic identifiability does not establish which candidate, "
            "if any, exists in nature."
        ),
        (
            "The controls isolate source innovations after a known deterministic "
            "backbone; detector performance can degrade when the backbone is "
            "misspecified or observations are coarse."
        ),
        (
            "The F4 control combines state dependence and Hawkes memory; a later "
            "ablation must separate those two mechanisms."
        ),
        (
            "F7-F10 are not classified by this protocol."
        ),
        (
            "The decision tree identifies declared observable regimes, not "
            "hidden ontologies below the temporal or amplitude resolution."
        ),
    ],
}

print(json.dumps(output, indent=2, sort_keys=True))
```

### I.2 Full reference output

**Normalized execution-output SHA-256:** `8ed3a0f31cb5b8a7f6180d052ecee18c236a7810c2c9afcb6674d6a40aafa258`

```json
{
  "calibration_seed_family": {
    "classification_counts": {
      "original": {
        "F1_initial_only": {
          "F1_initial_only": 16,
          "F2_gaussian_white": 0,
          "F3_poisson_events": 0,
          "F4_state_hawkes_events": 0,
          "F5_colored_memory": 0
        },
        "F2_gaussian_white": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 16,
          "F3_poisson_events": 0,
          "F4_state_hawkes_events": 0,
          "F5_colored_memory": 0
        },
        "F3_poisson_events": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 0,
          "F3_poisson_events": 15,
          "F4_state_hawkes_events": 1,
          "F5_colored_memory": 0
        },
        "F4_state_hawkes_events": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 0,
          "F3_poisson_events": 0,
          "F4_state_hawkes_events": 16,
          "F5_colored_memory": 0
        },
        "F5_colored_memory": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 0,
          "F3_poisson_events": 0,
          "F4_state_hawkes_events": 0,
          "F5_colored_memory": 16
        }
      },
      "revised": {
        "F1_initial_only": {
          "F1_initial_only": 16,
          "F2_gaussian_white": 0,
          "F3_poisson_events": 0,
          "F4_state_hawkes_events": 0,
          "F5_colored_memory": 0
        },
        "F2_gaussian_white": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 16,
          "F3_poisson_events": 0,
          "F4_state_hawkes_events": 0,
          "F5_colored_memory": 0
        },
        "F3_poisson_events": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 0,
          "F3_poisson_events": 16,
          "F4_state_hawkes_events": 0,
          "F5_colored_memory": 0
        },
        "F4_state_hawkes_events": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 0,
          "F3_poisson_events": 0,
          "F4_state_hawkes_events": 16,
          "F5_colored_memory": 0
        },
        "F5_colored_memory": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 0,
          "F3_poisson_events": 0,
          "F4_state_hawkes_events": 0,
          "F5_colored_memory": 16
        }
      }
    },
    "scores": {
      "original": {
        "accuracy": 0.9875,
        "correct": 79,
        "total": 80
      },
      "revised": {
        "accuracy": 1.0,
        "correct": 80,
        "total": 80
      }
    },
    "summaries": {
      "F1_initial_only": {
        "absolute_lag1_correlation": {
          "lower_95_t": 0.0,
          "mean": 0.0,
          "standard_deviation": 0.0,
          "upper_95_t": 0.0
        },
        "event_count_fano": {
          "lower_95_t": 0.0,
          "mean": 0.0,
          "standard_deviation": 0.0,
          "upper_95_t": 0.0
        },
        "excess_kurtosis": {
          "lower_95_t": 0.0,
          "mean": 0.0,
          "standard_deviation": 0.0,
          "upper_95_t": 0.0
        },
        "history_rate_ratio": {
          "lower_95_t": 0.0,
          "mean": 0.0,
          "standard_deviation": 0.0,
          "upper_95_t": 0.0
        },
        "innovation_rms": {
          "lower_95_t": 0.0,
          "mean": 0.0,
          "standard_deviation": 0.0,
          "upper_95_t": 0.0
        },
        "one_step_variance_rate": {
          "lower_95_t": 0.0,
          "mean": 0.0,
          "standard_deviation": 0.0,
          "upper_95_t": 0.0
        },
        "one_unit_variance_rate": {
          "lower_95_t": 0.0,
          "mean": 0.0,
          "standard_deviation": 0.0,
          "upper_95_t": 0.0
        },
        "signed_lag1_correlation": {
          "lower_95_t": 0.0,
          "mean": 0.0,
          "standard_deviation": 0.0,
          "upper_95_t": 0.0
        },
        "state_rate_ratio": {
          "lower_95_t": 0.0,
          "mean": 0.0,
          "standard_deviation": 0.0,
          "upper_95_t": 0.0
        },
        "tail_fraction": {
          "lower_95_t": 0.0,
          "mean": 0.0,
          "standard_deviation": 0.0,
          "upper_95_t": 0.0
        },
        "waiting_time_cv": {
          "lower_95_t": 0.0,
          "mean": 0.0,
          "standard_deviation": 0.0,
          "upper_95_t": 0.0
        }
      },
      "F2_gaussian_white": {
        "absolute_lag1_correlation": {
          "lower_95_t": -0.003133666799836006,
          "mean": -0.0014595282285578305,
          "standard_deviation": 0.0031417840966793467,
          "upper_95_t": 0.00021461034272034479
        },
        "event_count_fano": {
          "lower_95_t": 0.872897555328334,
          "mean": 0.9667359664061161,
          "standard_deviation": 0.17610252379332322,
          "upper_95_t": 1.0605743774838983
        },
        "excess_kurtosis": {
          "lower_95_t": -0.015846703565262465,
          "mean": -0.00706369703164017,
          "standard_deviation": 0.01648269188810192,
          "upper_95_t": 0.001719309501982123
        },
        "history_rate_ratio": {
          "lower_95_t": 0.9026803075629555,
          "mean": 1.058704080822078,
          "standard_deviation": 0.292803127494495,
          "upper_95_t": 1.2147278540812005
        },
        "innovation_rms": {
          "lower_95_t": 0.0015797868300506267,
          "mean": 0.0015819572097811017,
          "standard_deviation": 4.073058609333307e-06,
          "upper_95_t": 0.0015841275895115768
        },
        "one_step_variance_rate": {
          "lower_95_t": 2.4957134819229265e-05,
          "mean": 2.5025750583765732e-05,
          "standard_deviation": 1.2876826416918036e-07,
          "upper_95_t": 2.50943663483022e-05
        },
        "one_unit_variance_rate": {
          "lower_95_t": 2.4815909261114608e-05,
          "mean": 2.5047859536664387e-05,
          "standard_deviation": 4.3529113984053825e-07,
          "upper_95_t": 2.5279809812214167e-05
        },
        "signed_lag1_correlation": {
          "lower_95_t": -0.001816642287045969,
          "mean": 3.3274727424157985e-05,
          "standard_deviation": 0.0034716599664754108,
          "upper_95_t": 0.0018831917418942851
        },
        "state_rate_ratio": {
          "lower_95_t": 0.9768421956830777,
          "mean": 1.0250683959927391,
          "standard_deviation": 0.09050404296012764,
          "upper_95_t": 1.0732945963024005
        },
        "tail_fraction": {
          "lower_95_t": 0.01213558487652073,
          "mean": 0.0122783203125,
          "standard_deviation": 0.00026786547451079985,
          "upper_95_t": 0.01242105574847927
        },
        "waiting_time_cv": {
          "lower_95_t": 0.9574588342945344,
          "mean": 0.9761661458732345,
          "standard_deviation": 0.03510720977219487,
          "upper_95_t": 0.9948734574519346
        }
      },
      "F3_poisson_events": {
        "absolute_lag1_correlation": {
          "lower_95_t": -0.0032018202245171377,
          "mean": -0.0010362525775109617,
          "standard_deviation": 0.004064027978551845,
          "upper_95_t": 0.0011293150694952141
        },
        "event_count_fano": {
          "lower_95_t": 0.8097426871542137,
          "mean": 0.8994132667363455,
          "standard_deviation": 0.16828093307477454,
          "upper_95_t": 0.9890838463184772
        },
        "excess_kurtosis": {
          "lower_95_t": 19.577819855133793,
          "mean": 19.829025849520974,
          "standard_deviation": 0.47142752200828597,
          "upper_95_t": 20.080231843908155
        },
        "history_rate_ratio": {
          "lower_95_t": 0.9329656436821773,
          "mean": 0.9798654830069967,
          "standard_deviation": 0.08801491815282396,
          "upper_95_t": 1.026765322331816
        },
        "innovation_rms": {
          "lower_95_t": 0.0015689604374599752,
          "mean": 0.001577522212090158,
          "standard_deviation": 1.606751545776973e-05,
          "upper_95_t": 0.0015860839867203407
        },
        "one_step_variance_rate": {
          "lower_95_t": 2.461768660943092e-05,
          "mean": 2.4887652915954583e-05,
          "standard_deviation": 5.06634195655462e-07,
          "upper_95_t": 2.5157619222478245e-05
        },
        "one_unit_variance_rate": {
          "lower_95_t": 2.44116614545009e-05,
          "mean": 2.4792024007046997e-05,
          "standard_deviation": 7.138100985567255e-07,
          "upper_95_t": 2.5172386559593094e-05
        },
        "signed_lag1_correlation": {
          "lower_95_t": -0.003976636828651215,
          "mean": -0.0021295366879728723,
          "standard_deviation": 0.0034663736601724475,
          "upper_95_t": -0.00028243654729452963
        },
        "state_rate_ratio": {
          "lower_95_t": 0.978650074460928,
          "mean": 1.0012792987488637,
          "standard_deviation": 0.04246729524530674,
          "upper_95_t": 1.0239085230367992
        },
        "tail_fraction": {
          "lower_95_t": 0.047676521402058435,
          "mean": 0.0481357421875,
          "standard_deviation": 0.0008617999640635258,
          "upper_95_t": 0.04859496297294156
        },
        "waiting_time_cv": {
          "lower_95_t": 0.9690843848820939,
          "mean": 0.977432054592875,
          "standard_deviation": 0.01566571393289152,
          "upper_95_t": 0.985779724303656
        }
      },
      "F4_state_hawkes_events": {
        "absolute_lag1_correlation": {
          "lower_95_t": 0.16054154118272884,
          "mean": 0.1659453628192322,
          "standard_deviation": 0.010141120436581243,
          "upper_95_t": 0.17134918445573555
        },
        "event_count_fano": {
          "lower_95_t": 2.4576091452685938,
          "mean": 2.6850488637583285,
          "standard_deviation": 0.42682637074583224,
          "upper_95_t": 2.9124885822480633
        },
        "excess_kurtosis": {
          "lower_95_t": 26.725429350095066,
          "mean": 27.474508348009564,
          "standard_deviation": 1.4057644469701571,
          "upper_95_t": 28.223587345924063
        },
        "history_rate_ratio": {
          "lower_95_t": 5.133839224405149,
          "mean": 5.281522700843929,
          "standard_deviation": 0.27715124994906093,
          "upper_95_t": 5.42920617728271
        },
        "innovation_rms": {
          "lower_95_t": 0.0015657849179120293,
          "mean": 0.0015850987076276983,
          "standard_deviation": 3.624536129585107e-05,
          "upper_95_t": 0.0016044124973433672
        },
        "one_step_variance_rate": {
          "lower_95_t": 2.452182789906487e-05,
          "mean": 2.5137465591430657e-05,
          "standard_deviation": 1.1553408686560982e-06,
          "upper_95_t": 2.5753103283796445e-05
        },
        "one_unit_variance_rate": {
          "lower_95_t": 2.4473646171210954e-05,
          "mean": 2.5265322370927092e-05,
          "standard_deviation": 1.4857047897108734e-06,
          "upper_95_t": 2.605699857064323e-05
        },
        "signed_lag1_correlation": {
          "lower_95_t": -0.0002359837191459515,
          "mean": 0.004257169824104711,
          "standard_deviation": 0.008432108660721957,
          "upper_95_t": 0.008750323367355373
        },
        "state_rate_ratio": {
          "lower_95_t": 8.568659417499372,
          "mean": 9.857382047275436,
          "standard_deviation": 2.4184905196766158,
          "upper_95_t": 11.1461046770515
        },
        "tail_fraction": {
          "lower_95_t": 0.04372182542294847,
          "mean": 0.044650390624999994,
          "standard_deviation": 0.0017425985128029105,
          "upper_95_t": 0.04557895582705152
        },
        "waiting_time_cv": {
          "lower_95_t": 2.2556483361540383,
          "mean": 2.3230763451620646,
          "standard_deviation": 0.1265392542807428,
          "upper_95_t": 2.390504354170091
        }
      },
      "F5_colored_memory": {
        "absolute_lag1_correlation": {
          "lower_95_t": 0.6278017549802759,
          "mean": 0.6302647627537912,
          "standard_deviation": 0.0046222211145401215,
          "upper_95_t": 0.6327277705273064
        },
        "event_count_fano": {
          "lower_95_t": 2.09149317556939,
          "mean": 2.3839660562813716,
          "standard_deviation": 0.5488713187160759,
          "upper_95_t": 2.6764389369933532
        },
        "excess_kurtosis": {
          "lower_95_t": -0.020118619225794575,
          "mean": -0.001622682163171213,
          "standard_deviation": 0.03471053227820087,
          "upper_95_t": 0.01687325489945215
        },
        "history_rate_ratio": {
          "lower_95_t": 45.09224637993597,
          "mean": 46.79745217917734,
          "standard_deviation": 3.2000866317366166,
          "upper_95_t": 48.50265797841871
        },
        "innovation_rms": {
          "lower_95_t": 0.0015787623267941456,
          "mean": 0.001582810223176542,
          "standard_deviation": 7.596513632386545e-06,
          "upper_95_t": 0.0015868581195589383
        },
        "one_step_variance_rate": {
          "lower_95_t": 2.4922685667081262e-05,
          "mean": 2.504979299292643e-05,
          "standard_deviation": 2.3853687010323123e-07,
          "upper_95_t": 2.51769003187716e-05
        },
        "one_unit_variance_rate": {
          "lower_95_t": 0.00014239122837381109,
          "mean": 0.00014349965605674672,
          "standard_deviation": 2.0801387210782044e-06,
          "upper_95_t": 0.00014460808373968235
        },
        "signed_lag1_correlation": {
          "lower_95_t": 0.8184751365611971,
          "mean": 0.8194636821029018,
          "standard_deviation": 0.0018551610452412829,
          "upper_95_t": 0.8204522276446065
        },
        "state_rate_ratio": {
          "lower_95_t": 0.8616110490488063,
          "mean": 0.9368517555332989,
          "standard_deviation": 0.14120100875247027,
          "upper_95_t": 1.0120924620177916
        },
        "tail_fraction": {
          "lower_95_t": 0.01203241181850986,
          "mean": 0.01233203125,
          "standard_deviation": 0.0005622829442327055,
          "upper_95_t": 0.01263165068149014
        },
        "waiting_time_cv": {
          "lower_95_t": 1.6132833495555046,
          "mean": 1.6474681295178732,
          "standard_deviation": 0.06415311126381479,
          "upper_95_t": 1.681652909480242
        }
      }
    }
  },
  "configuration": {
    "event_threshold_sigma": 2.5,
    "fano_window_time": 2.0,
    "grid_size": 8,
    "hawkes_branching_ratio": 0.6,
    "memory_time": 0.5,
    "poisson_target_rate_per_cell_per_time": 0.5,
    "primary_dt": 0.1,
    "primary_physical_time": 100.0,
    "primary_replicates_per_candidate": 16,
    "sensitivity_physical_time": 50.0,
    "sensitivity_replicates_per_candidate": 12,
    "sensitivity_time_steps": [
      0.2,
      0.1,
      0.05
    ],
    "source_sigma": 0.005,
    "state_coefficient": 0.9
  },
  "current_f0_controlled_source": {
    "analytic_pre_damping_variance_coefficient": 0.0002551958227644319,
    "expected_one_step_variance_rate": "dt * analytic_pre_damping_variance_coefficient",
    "fitted_variance_rate_dt_exponent": 0.999737593589198,
    "interpretation": "The isolated current source is an iid state-dependent Bernoulli plus Gaussian per-update law. Its one-step variance rate vanishes linearly as dt decreases and is outside F1-F5 continuous controls.",
    "summaries_by_dt": {
      "0.025": {
        "absolute_lag1_correlation": {
          "lower_95_t": -0.0017913877846502681,
          "mean": 0.00017723615931085866,
          "standard_deviation": 0.00309839135108825,
          "upper_95_t": 0.0021458601032719854
        },
        "event_count_fano": {
          "lower_95_t": 0.0,
          "mean": 0.0,
          "standard_deviation": 0.0,
          "upper_95_t": 0.0
        },
        "excess_kurtosis": {
          "lower_95_t": -1.6158616374796602,
          "mean": -1.614397839783796,
          "standard_deviation": 0.0023038519543162397,
          "upper_95_t": -1.6129340420879317
        },
        "history_rate_ratio": {
          "lower_95_t": 1.0,
          "mean": 1.0,
          "standard_deviation": 0.0,
          "upper_95_t": 1.0
        },
        "innovation_rms": {
          "lower_95_t": 0.0003991561247136573,
          "mean": 0.00039943048400623455,
          "standard_deviation": 4.318104845873359e-07,
          "upper_95_t": 0.0003997048432988118
        },
        "one_step_variance_rate": {
          "lower_95_t": 6.372974236256657e-06,
          "mean": 6.381749911304037e-06,
          "standard_deviation": 1.3811919615309114e-08,
          "upper_95_t": 6.390525586351417e-06
        },
        "one_unit_variance_rate": {
          "lower_95_t": 6.337576945032023e-06,
          "mean": 6.4129782156902435e-06,
          "standard_deviation": 1.1867306886373398e-07,
          "upper_95_t": 6.488379486348464e-06
        },
        "signed_lag1_correlation": {
          "lower_95_t": -0.0028635723988226316,
          "mean": -8.477756339548e-06,
          "standard_deviation": 0.0044935959322979085,
          "upper_95_t": 0.0028466168861435354
        },
        "state_rate_ratio": {
          "lower_95_t": 1.0,
          "mean": 1.0,
          "standard_deviation": 0.0,
          "upper_95_t": 1.0
        },
        "tail_fraction": {
          "lower_95_t": -7.818913802623367e-07,
          "mean": 6.510416666666666e-07,
          "standard_deviation": 2.2552744890219758e-06,
          "upper_95_t": 2.08397471359567e-06
        },
        "waiting_time_cv": {
          "lower_95_t": 0.0,
          "mean": 0.0,
          "standard_deviation": 0.0,
          "upper_95_t": 0.0
        }
      },
      "0.050": {
        "absolute_lag1_correlation": {
          "lower_95_t": -0.0005325724967244847,
          "mean": 0.002144272252173652,
          "standard_deviation": 0.004213050767585177,
          "upper_95_t": 0.004821117001071789
        },
        "event_count_fano": {
          "lower_95_t": 0.0,
          "mean": 0.0,
          "standard_deviation": 0.0,
          "upper_95_t": 0.0
        },
        "excess_kurtosis": {
          "lower_95_t": -1.6174318287542087,
          "mean": -1.6157420376779872,
          "standard_deviation": 0.0026595399653505224,
          "upper_95_t": -1.6140522466017657
        },
        "history_rate_ratio": {
          "lower_95_t": 1.0,
          "mean": 1.0,
          "standard_deviation": 0.0,
          "upper_95_t": 1.0
        },
        "innovation_rms": {
          "lower_95_t": 0.0007979711034977829,
          "mean": 0.0007986695829128914,
          "standard_deviation": 1.0993275710802976e-06,
          "upper_95_t": 0.0007993680623279998
        },
        "one_step_variance_rate": {
          "lower_95_t": 1.2735076251627746e-05,
          "mean": 1.275738936597898e-05,
          "standard_deviation": 3.511831740834962e-08,
          "upper_95_t": 1.2779702480330214e-05
        },
        "one_unit_variance_rate": {
          "lower_95_t": 1.2448875446591706e-05,
          "mean": 1.2663037300836514e-05,
          "standard_deviation": 3.370665275918422e-07,
          "upper_95_t": 1.2877199155081323e-05
        },
        "signed_lag1_correlation": {
          "lower_95_t": -0.001012694239469818,
          "mean": 0.001168425087191132,
          "standard_deviation": 0.0034328350410184586,
          "upper_95_t": 0.0033495444138520823
        },
        "state_rate_ratio": {
          "lower_95_t": 1.0,
          "mean": 1.0,
          "standard_deviation": 0.0,
          "upper_95_t": 1.0
        },
        "tail_fraction": {
          "lower_95_t": 0.0,
          "mean": 0.0,
          "standard_deviation": 0.0,
          "upper_95_t": 0.0
        },
        "waiting_time_cv": {
          "lower_95_t": 0.0,
          "mean": 0.0,
          "standard_deviation": 0.0,
          "upper_95_t": 0.0
        }
      },
      "0.100": {
        "absolute_lag1_correlation": {
          "lower_95_t": -0.006586463286167401,
          "mean": -0.0034938770070528417,
          "standard_deviation": 0.004867380897756648,
          "upper_95_t": -0.00040129072793828203
        },
        "event_count_fano": {
          "lower_95_t": 0.0,
          "mean": 0.0,
          "standard_deviation": 0.0,
          "upper_95_t": 0.0
        },
        "excess_kurtosis": {
          "lower_95_t": -1.6178847333543318,
          "mean": -1.6162108608846983,
          "standard_deviation": 0.0026344858796655372,
          "upper_95_t": -1.6145369884150649
        },
        "history_rate_ratio": {
          "lower_95_t": 1.0,
          "mean": 1.0,
          "standard_deviation": 0.0,
          "upper_95_t": 1.0
        },
        "innovation_rms": {
          "lower_95_t": 0.001596945746037247,
          "mean": 0.00159848073163464,
          "standard_deviation": 2.415893656885044e-06,
          "upper_95_t": 0.001600015717232033
        },
        "one_step_variance_rate": {
          "lower_95_t": 2.550168779241622e-05,
          "mean": 2.555060688732759e-05,
          "standard_deviation": 7.699312052025352e-08,
          "upper_95_t": 2.559952598223896e-05
        },
        "one_unit_variance_rate": {
          "lower_95_t": 2.5009382415851183e-05,
          "mean": 2.5358407989326524e-05,
          "standard_deviation": 5.493267627278054e-07,
          "upper_95_t": 2.5707433562801864e-05
        },
        "signed_lag1_correlation": {
          "lower_95_t": -0.00286994934618004,
          "mean": -0.000932211679876221,
          "standard_deviation": 0.003049779844632549,
          "upper_95_t": 0.0010055259864275978
        },
        "state_rate_ratio": {
          "lower_95_t": 1.0,
          "mean": 1.0,
          "standard_deviation": 0.0,
          "upper_95_t": 1.0
        },
        "tail_fraction": {
          "lower_95_t": 0.0,
          "mean": 0.0,
          "standard_deviation": 0.0,
          "upper_95_t": 0.0
        },
        "waiting_time_cv": {
          "lower_95_t": 0.0,
          "mean": 0.0,
          "standard_deviation": 0.0,
          "upper_95_t": 0.0
        }
      },
      "0.200": {
        "absolute_lag1_correlation": {
          "lower_95_t": -0.005766646834221772,
          "mean": -0.0011835160974528365,
          "standard_deviation": 0.007213329228912392,
          "upper_95_t": 0.0033996146393160988
        },
        "event_count_fano": {
          "lower_95_t": 0.0,
          "mean": 0.0,
          "standard_deviation": 0.0,
          "upper_95_t": 0.0
        },
        "excess_kurtosis": {
          "lower_95_t": -1.6189116779094828,
          "mean": -1.6148947258783244,
          "standard_deviation": 0.006322228005636494,
          "upper_95_t": -1.610877773847166
        },
        "history_rate_ratio": {
          "lower_95_t": 1.0,
          "mean": 1.0,
          "standard_deviation": 0.0,
          "upper_95_t": 1.0
        },
        "innovation_rms": {
          "lower_95_t": 0.0031877074756844585,
          "mean": 0.0031938419055018152,
          "standard_deviation": 9.65489846258393e-06,
          "upper_95_t": 0.003199976335319172
        },
        "one_step_variance_rate": {
          "lower_95_t": 5.080370807317834e-05,
          "mean": 5.099919520740151e-05,
          "standard_deviation": 3.0767463119815914e-07,
          "upper_95_t": 5.119468234162468e-05
        },
        "one_unit_variance_rate": {
          "lower_95_t": 5.0150192027055856e-05,
          "mean": 5.064381610939636e-05,
          "standard_deviation": 7.769084553219702e-07,
          "upper_95_t": 5.1137440191736864e-05
        },
        "signed_lag1_correlation": {
          "lower_95_t": -0.0031577110338639855,
          "mean": 0.0008713085822339084,
          "standard_deviation": 0.006341221018964259,
          "upper_95_t": 0.004900328198331802
        },
        "state_rate_ratio": {
          "lower_95_t": 1.0,
          "mean": 1.0,
          "standard_deviation": 0.0,
          "upper_95_t": 1.0
        },
        "tail_fraction": {
          "lower_95_t": 0.0,
          "mean": 0.0,
          "standard_deviation": 0.0,
          "upper_95_t": 0.0
        },
        "waiting_time_cv": {
          "lower_95_t": 0.0,
          "mean": 0.0,
          "standard_deviation": 0.0,
          "upper_95_t": 0.0
        }
      }
    }
  },
  "dt_sensitivity": {
    "0.05": {
      "classification_counts": {
        "original": {
          "F1_initial_only": {
            "F1_initial_only": 12,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 0
          },
          "F2_gaussian_white": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 12,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 0
          },
          "F3_poisson_events": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 10,
            "F4_state_hawkes_events": 2,
            "F5_colored_memory": 0
          },
          "F4_state_hawkes_events": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 12,
            "F5_colored_memory": 0
          },
          "F5_colored_memory": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 12
          }
        },
        "revised": {
          "F1_initial_only": {
            "F1_initial_only": 12,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 0
          },
          "F2_gaussian_white": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 12,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 0
          },
          "F3_poisson_events": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 12,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 0
          },
          "F4_state_hawkes_events": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 12,
            "F5_colored_memory": 0
          },
          "F5_colored_memory": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 12
          }
        }
      },
      "summaries": {
        "F1_initial_only": {
          "absolute_lag1_correlation": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "event_count_fano": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "excess_kurtosis": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "history_rate_ratio": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "innovation_rms": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "one_step_variance_rate": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "one_unit_variance_rate": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "signed_lag1_correlation": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "state_rate_ratio": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "tail_fraction": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "waiting_time_cv": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          }
        },
        "F2_gaussian_white": {
          "absolute_lag1_correlation": {
            "lower_95_t": -0.0028798389594410726,
            "mean": -0.0001611932284404773,
            "standard_deviation": 0.004278840783911327,
            "upper_95_t": 0.0025574525025601176
          },
          "event_count_fano": {
            "lower_95_t": 0.7319733187944546,
            "mean": 0.8935739811806641,
            "standard_deviation": 0.2543411585556996,
            "upper_95_t": 1.0551746435668736
          },
          "excess_kurtosis": {
            "lower_95_t": -0.010666248475310312,
            "mean": 0.0027039735994062544,
            "standard_deviation": 0.02104321679389724,
            "upper_95_t": 0.01607419567412282
          },
          "history_rate_ratio": {
            "lower_95_t": 0.8943725438935611,
            "mean": 1.1392899956980005,
            "standard_deviation": 0.38547235835938437,
            "upper_95_t": 1.38420744750244
          },
          "innovation_rms": {
            "lower_95_t": 0.0011176253555500682,
            "mean": 0.0011192524119976466,
            "standard_deviation": 2.5608027578720783e-06,
            "upper_95_t": 0.0011208794684452249
          },
          "one_step_variance_rate": {
            "lower_95_t": 2.498138165971039e-05,
            "mean": 2.5054338156042248e-05,
            "standard_deviation": 1.1482527068399348e-07,
            "upper_95_t": 2.5127294652374106e-05
          },
          "one_unit_variance_rate": {
            "lower_95_t": 2.452954934113419e-05,
            "mean": 2.4979553879500176e-05,
            "standard_deviation": 7.08256228367384e-07,
            "upper_95_t": 2.5429558417866164e-05
          },
          "signed_lag1_correlation": {
            "lower_95_t": -0.002325198749351136,
            "mean": 0.00017296677275251032,
            "standard_deviation": 0.003931829880976822,
            "upper_95_t": 0.002671132294856157
          },
          "state_rate_ratio": {
            "lower_95_t": 0.9238685085203583,
            "mean": 0.9729055521288226,
            "standard_deviation": 0.07717875842436837,
            "upper_95_t": 1.021942595737287
          },
          "tail_fraction": {
            "lower_95_t": 0.012230957858091748,
            "mean": 0.01245703125,
            "standard_deviation": 0.000355813940162839,
            "upper_95_t": 0.012683104641908253
          },
          "waiting_time_cv": {
            "lower_95_t": 0.9802694124681901,
            "mean": 0.9980726083764685,
            "standard_deviation": 0.028020216046416625,
            "upper_95_t": 1.0158758042847469
          }
        },
        "F3_poisson_events": {
          "absolute_lag1_correlation": {
            "lower_95_t": -0.0014816734196333493,
            "mean": 0.0010947606581201035,
            "standard_deviation": 0.004055015732003085,
            "upper_95_t": 0.0036711947358735566
          },
          "event_count_fano": {
            "lower_95_t": 0.7680945331140193,
            "mean": 0.9529451844363264,
            "standard_deviation": 0.2909340105594974,
            "upper_95_t": 1.1377958357586335
          },
          "excess_kurtosis": {
            "lower_95_t": 39.946122943161846,
            "mean": 40.81815292926939,
            "standard_deviation": 1.3724765337399336,
            "upper_95_t": 41.69018291537693
          },
          "history_rate_ratio": {
            "lower_95_t": 0.9447259166748447,
            "mean": 1.0498005370031753,
            "standard_deviation": 0.16537556390232022,
            "upper_95_t": 1.154875157331506
          },
          "innovation_rms": {
            "lower_95_t": 0.0011065579462786349,
            "mean": 0.0011135786225516127,
            "standard_deviation": 1.1049750110839178e-05,
            "upper_95_t": 0.0011205992988245906
          },
          "one_step_variance_rate": {
            "lower_95_t": 2.448844648859898e-05,
            "mean": 2.4802582865397126e-05,
            "standard_deviation": 4.944151146384732e-07,
            "upper_95_t": 2.5116719242195273e-05
          },
          "one_unit_variance_rate": {
            "lower_95_t": 2.4370187170794264e-05,
            "mean": 2.504255602336667e-05,
            "standard_deviation": 1.0582324998850132e-06,
            "upper_95_t": 2.5714924875939077e-05
          },
          "signed_lag1_correlation": {
            "lower_95_t": -0.002409860387392269,
            "mean": 0.00014562590657585887,
            "standard_deviation": 0.004022046290427402,
            "upper_95_t": 0.002701112200543987
          },
          "state_rate_ratio": {
            "lower_95_t": 0.9457851745806632,
            "mean": 0.9876140920676545,
            "standard_deviation": 0.0658339834607015,
            "upper_95_t": 1.0294430095546458
          },
          "tail_fraction": {
            "lower_95_t": 0.02400314947523778,
            "mean": 0.024290364583333335,
            "standard_deviation": 0.0004520440836630989,
            "upper_95_t": 0.02457757969142889
          },
          "waiting_time_cv": {
            "lower_95_t": 0.9759184288539443,
            "mean": 0.9957067130341889,
            "standard_deviation": 0.031144520386955667,
            "upper_95_t": 1.0154949972144336
          }
        },
        "F4_state_hawkes_events": {
          "absolute_lag1_correlation": {
            "lower_95_t": 0.09591978582978772,
            "mean": 0.10165812374591537,
            "standard_deviation": 0.009031494625213599,
            "upper_95_t": 0.10739646166204303
          },
          "event_count_fano": {
            "lower_95_t": 2.2747183696721374,
            "mean": 3.060835834084177,
            "standard_deviation": 1.2372599450216701,
            "upper_95_t": 3.8469532984962163
          },
          "excess_kurtosis": {
            "lower_95_t": 47.04058263826101,
            "mean": 48.89881049429045,
            "standard_deviation": 2.9246403992669197,
            "upper_95_t": 50.757038350319895
          },
          "history_rate_ratio": {
            "lower_95_t": 5.49941809537111,
            "mean": 5.826521068282162,
            "standard_deviation": 0.5148230698360696,
            "upper_95_t": 6.153624041193214
          },
          "innovation_rms": {
            "lower_95_t": 0.0010893352779627876,
            "mean": 0.001108930595476307,
            "standard_deviation": 3.0840812686425286e-05,
            "upper_95_t": 0.0011285259129898265
          },
          "one_step_variance_rate": {
            "lower_95_t": 2.3734912248512885e-05,
            "mean": 2.4611756551106764e-05,
            "standard_deviation": 1.380053723181539e-06,
            "upper_95_t": 2.5488600853700643e-05
          },
          "one_unit_variance_rate": {
            "lower_95_t": 2.3415458250925503e-05,
            "mean": 2.4821012588569342e-05,
            "standard_deviation": 2.212183498325998e-06,
            "upper_95_t": 2.622656692621318e-05
          },
          "signed_lag1_correlation": {
            "lower_95_t": -0.007639159639774854,
            "mean": -0.0003941080704270001,
            "standard_deviation": 0.011402891440752998,
            "upper_95_t": 0.006850943498920854
          },
          "state_rate_ratio": {
            "lower_95_t": 7.549396626892133,
            "mean": 9.557955206184811,
            "standard_deviation": 3.161243948761716,
            "upper_95_t": 11.56651378547749
          },
          "tail_fraction": {
            "lower_95_t": 0.02225216564123634,
            "mean": 0.02306380208333333,
            "standard_deviation": 0.0012774239285951775,
            "upper_95_t": 0.023875438525430323
          },
          "waiting_time_cv": {
            "lower_95_t": 2.087876388260958,
            "mean": 2.156424219441692,
            "standard_deviation": 0.10788653054726667,
            "upper_95_t": 2.2249720506224255
          }
        },
        "F5_colored_memory": {
          "absolute_lag1_correlation": {
            "lower_95_t": 0.7865374218447387,
            "mean": 0.7890680748392453,
            "standard_deviation": 0.003982961486797693,
            "upper_95_t": 0.791598727833752
          },
          "event_count_fano": {
            "lower_95_t": 4.102981631073504,
            "mean": 5.115062102506216,
            "standard_deviation": 1.5929001518607724,
            "upper_95_t": 6.127142573938928
          },
          "excess_kurtosis": {
            "lower_95_t": -0.019420533988395633,
            "mean": 0.017012080564851706,
            "standard_deviation": 0.0573408131987764,
            "upper_95_t": 0.053444695118099045
          },
          "history_rate_ratio": {
            "lower_95_t": 85.95532285892394,
            "mean": 90.37478777268582,
            "standard_deviation": 6.9557377411986705,
            "upper_95_t": 94.7942526864477
          },
          "innovation_rms": {
            "lower_95_t": 0.000788990142222395,
            "mean": 0.0007933066639735613,
            "standard_deviation": 6.793716850607331e-06,
            "upper_95_t": 0.0007976231857247275
          },
          "one_step_variance_rate": {
            "lower_95_t": 1.2444169862093476e-05,
            "mean": 1.2582830382454503e-05,
            "standard_deviation": 2.1823597053256299e-07,
            "upper_95_t": 1.272149090281553e-05
          },
          "one_unit_variance_rate": {
            "lower_95_t": 0.00014130383048551354,
            "mean": 0.00014381220819498488,
            "standard_deviation": 3.947902708452494e-06,
            "upper_95_t": 0.0001463205859044562
          },
          "signed_lag1_correlation": {
            "lower_95_t": 0.9043162629880939,
            "mean": 0.90559688082319,
            "standard_deviation": 0.0020155475790502677,
            "upper_95_t": 0.9068774986582862
          },
          "state_rate_ratio": {
            "lower_95_t": 0.750761564428392,
            "mean": 0.8731029302567649,
            "standard_deviation": 0.19255146770196918,
            "upper_95_t": 0.9954442960851377
          },
          "tail_fraction": {
            "lower_95_t": 0.012305039503800965,
            "mean": 0.012584635416666668,
            "standard_deviation": 0.0004400523324325822,
            "upper_95_t": 0.012864231329532372
          },
          "waiting_time_cv": {
            "lower_95_t": 2.2015971808005372,
            "mean": 2.26062868318893,
            "standard_deviation": 0.09290890573743452,
            "upper_95_t": 2.3196601855773227
          }
        }
      }
    },
    "0.10": {
      "classification_counts": {
        "original": {
          "F1_initial_only": {
            "F1_initial_only": 12,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 0
          },
          "F2_gaussian_white": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 12,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 0
          },
          "F3_poisson_events": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 10,
            "F4_state_hawkes_events": 2,
            "F5_colored_memory": 0
          },
          "F4_state_hawkes_events": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 12,
            "F5_colored_memory": 0
          },
          "F5_colored_memory": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 12
          }
        },
        "revised": {
          "F1_initial_only": {
            "F1_initial_only": 12,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 0
          },
          "F2_gaussian_white": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 12,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 0
          },
          "F3_poisson_events": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 12,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 0
          },
          "F4_state_hawkes_events": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 12,
            "F5_colored_memory": 0
          },
          "F5_colored_memory": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 12
          }
        }
      },
      "summaries": {
        "F1_initial_only": {
          "absolute_lag1_correlation": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "event_count_fano": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "excess_kurtosis": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "history_rate_ratio": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "innovation_rms": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "one_step_variance_rate": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "one_unit_variance_rate": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "signed_lag1_correlation": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "state_rate_ratio": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "tail_fraction": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "waiting_time_cv": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          }
        },
        "F2_gaussian_white": {
          "absolute_lag1_correlation": {
            "lower_95_t": -0.004386976652333363,
            "mean": -0.00019061387728065474,
            "standard_deviation": 0.006604600217393648,
            "upper_95_t": 0.004005748897772054
          },
          "event_count_fano": {
            "lower_95_t": 0.8653562131923338,
            "mean": 1.0259959944381936,
            "standard_deviation": 0.25282884035809977,
            "upper_95_t": 1.1866357756840533
          },
          "excess_kurtosis": {
            "lower_95_t": -0.028252475927441102,
            "mean": -0.011326525847391614,
            "standard_deviation": 0.02663953036731548,
            "upper_95_t": 0.005599424232657876
          },
          "history_rate_ratio": {
            "lower_95_t": 1.107447644421124,
            "mean": 1.3182865804105905,
            "standard_deviation": 0.3318366302240362,
            "upper_95_t": 1.529125516400057
          },
          "innovation_rms": {
            "lower_95_t": 0.0015760958452098208,
            "mean": 0.001581077529954389,
            "standard_deviation": 7.840608143452928e-06,
            "upper_95_t": 0.001586059214698957
          },
          "one_step_variance_rate": {
            "lower_95_t": 2.484053813965251e-05,
            "mean": 2.499803619983669e-05,
            "standard_deviation": 2.4788412687186536e-07,
            "upper_95_t": 2.5155534260020873e-05
          },
          "one_unit_variance_rate": {
            "lower_95_t": 2.4618963842202045e-05,
            "mean": 2.5130520220416314e-05,
            "standard_deviation": 8.051318601072604e-07,
            "upper_95_t": 2.5642076598630582e-05
          },
          "signed_lag1_correlation": {
            "lower_95_t": -0.000781372883643045,
            "mean": 0.0018923934284471179,
            "standard_deviation": 0.0042082056563540774,
            "upper_95_t": 0.004566159740537281
          },
          "state_rate_ratio": {
            "lower_95_t": 0.9507338014162575,
            "mean": 1.0347044769397993,
            "standard_deviation": 0.1321603425505816,
            "upper_95_t": 1.118675152463341
          },
          "tail_fraction": {
            "lower_95_t": 0.011957932455702518,
            "mean": 0.012299479166666669,
            "standard_deviation": 0.0005375558793187472,
            "upper_95_t": 0.012641025877630819
          },
          "waiting_time_cv": {
            "lower_95_t": 0.9167473725988048,
            "mean": 0.9422899390671152,
            "standard_deviation": 0.04020110964960023,
            "upper_95_t": 0.9678325055354257
          }
        },
        "F3_poisson_events": {
          "absolute_lag1_correlation": {
            "lower_95_t": -0.004297198688914875,
            "mean": 0.00025393674987623946,
            "standard_deviation": 0.007162972249950477,
            "upper_95_t": 0.004805072188667355
          },
          "event_count_fano": {
            "lower_95_t": 0.7001485006527008,
            "mean": 0.9370288447464512,
            "standard_deviation": 0.37282286016804506,
            "upper_95_t": 1.1739091888402016
          },
          "excess_kurtosis": {
            "lower_95_t": 19.64707232941522,
            "mean": 20.21563995372612,
            "standard_deviation": 0.8948611110200334,
            "upper_95_t": 20.784207578037023
          },
          "history_rate_ratio": {
            "lower_95_t": 0.919999522100735,
            "mean": 1.0074499214248605,
            "standard_deviation": 0.13763703410509484,
            "upper_95_t": 1.0949003207489858
          },
          "innovation_rms": {
            "lower_95_t": 0.0015801963874053334,
            "mean": 0.0015893339123423146,
            "standard_deviation": 1.4381430400632782e-05,
            "upper_95_t": 0.0015984714372792959
          },
          "one_step_variance_rate": {
            "lower_95_t": 2.4970454011187738e-05,
            "mean": 2.5261030639648436e-05,
            "standard_deviation": 4.5733473638415867e-07,
            "upper_95_t": 2.5551607268109133e-05
          },
          "one_unit_variance_rate": {
            "lower_95_t": 2.5063233164449883e-05,
            "mean": 2.545550082382515e-05,
            "standard_deviation": 6.173849133798598e-07,
            "upper_95_t": 2.5847768483200417e-05
          },
          "signed_lag1_correlation": {
            "lower_95_t": -0.005796828876500549,
            "mean": -0.000934325258009167,
            "standard_deviation": 0.007653030535559977,
            "upper_95_t": 0.003928178360482215
          },
          "state_rate_ratio": {
            "lower_95_t": 0.9384378863664496,
            "mean": 0.9803417963719068,
            "standard_deviation": 0.06595201319986205,
            "upper_95_t": 1.022245706377364
          },
          "tail_fraction": {
            "lower_95_t": 0.04777451904815635,
            "mean": 0.048421875,
            "standard_deviation": 0.00101886502418132,
            "upper_95_t": 0.04906923095184366
          },
          "waiting_time_cv": {
            "lower_95_t": 0.961265687352756,
            "mean": 0.9768394034614171,
            "standard_deviation": 0.024511267092630712,
            "upper_95_t": 0.9924131195700782
          }
        },
        "F4_state_hawkes_events": {
          "absolute_lag1_correlation": {
            "lower_95_t": 0.1597380841731125,
            "mean": 0.16724815937171256,
            "standard_deviation": 0.011820008647534894,
            "upper_95_t": 0.17475823457031261
          },
          "event_count_fano": {
            "lower_95_t": 1.8480814759285495,
            "mean": 2.3451880649010093,
            "standard_deviation": 0.782389526738208,
            "upper_95_t": 2.842294653873469
          },
          "excess_kurtosis": {
            "lower_95_t": 25.86229236312633,
            "mean": 27.054724629746005,
            "standard_deviation": 1.876753471878893,
            "upper_95_t": 28.24715689636568
          },
          "history_rate_ratio": {
            "lower_95_t": 5.132139432532634,
            "mean": 5.326940464972627,
            "standard_deviation": 0.30659478461928885,
            "upper_95_t": 5.52174149741262
          },
          "innovation_rms": {
            "lower_95_t": 0.0015481729710566427,
            "mean": 0.001571255008701592,
            "standard_deviation": 3.632851567410212e-05,
            "upper_95_t": 0.0015943370463465415
          },
          "one_step_variance_rate": {
            "lower_95_t": 2.3982472799473104e-05,
            "mean": 2.469987231445311e-05,
            "standard_deviation": 1.1291056675946091e-06,
            "upper_95_t": 2.541727182943312e-05
          },
          "one_unit_variance_rate": {
            "lower_95_t": 2.3179679737127444e-05,
            "mean": 2.4297982930863806e-05,
            "standard_deviation": 1.7600826983721442e-06,
            "upper_95_t": 2.5416286124600167e-05
          },
          "signed_lag1_correlation": {
            "lower_95_t": -0.006617746745858716,
            "mean": -0.002819300590228956,
            "standard_deviation": 0.0059783244800409975,
            "upper_95_t": 0.0009791455654008046
          },
          "state_rate_ratio": {
            "lower_95_t": 6.4031381853937575,
            "mean": 8.994169320542492,
            "standard_deviation": 4.077989848783295,
            "upper_95_t": 11.585200455691226
          },
          "tail_fraction": {
            "lower_95_t": 0.04298376508004173,
            "mean": 0.044171875,
            "standard_deviation": 0.0018699505872786155,
            "upper_95_t": 0.04535998491995827
          },
          "waiting_time_cv": {
            "lower_95_t": 1.969670734534311,
            "mean": 2.0286072262203865,
            "standard_deviation": 0.09275936964181641,
            "upper_95_t": 2.087543717906462
          }
        },
        "F5_colored_memory": {
          "absolute_lag1_correlation": {
            "lower_95_t": 0.6244961107480707,
            "mean": 0.6291004300494503,
            "standard_deviation": 0.007246677632264444,
            "upper_95_t": 0.6337047493508299
          },
          "event_count_fano": {
            "lower_95_t": 2.3331280715864113,
            "mean": 3.036153233794945,
            "standard_deviation": 1.106482062694726,
            "upper_95_t": 3.7391783960034783
          },
          "excess_kurtosis": {
            "lower_95_t": -0.03390567979697582,
            "mean": -0.00649684344024289,
            "standard_deviation": 0.04313840729795137,
            "upper_95_t": 0.020911992916490037
          },
          "history_rate_ratio": {
            "lower_95_t": 45.24726954918188,
            "mean": 48.781910798316666,
            "standard_deviation": 5.5631254049885985,
            "upper_95_t": 52.31655204745145
          },
          "innovation_rms": {
            "lower_95_t": 0.0015744527502979894,
            "mean": 0.0015819998210689571,
            "standard_deviation": 1.1878235492638724e-05,
            "upper_95_t": 0.0015895468918399249
          },
          "one_step_variance_rate": {
            "lower_95_t": 2.477860316144159e-05,
            "mean": 2.5019556539829937e-05,
            "standard_deviation": 3.792333553109941e-07,
            "upper_95_t": 2.526050991821828e-05
          },
          "one_unit_variance_rate": {
            "lower_95_t": 0.00014129154644091572,
            "mean": 0.0001433900904840782,
            "standard_deviation": 3.3028708876360236e-06,
            "upper_95_t": 0.0001454886345272407
          },
          "signed_lag1_correlation": {
            "lower_95_t": 0.8164821431558469,
            "mean": 0.8187694620259239,
            "standard_deviation": 0.0035999811065834026,
            "upper_95_t": 0.821056780896001
          },
          "state_rate_ratio": {
            "lower_95_t": 0.721905862427529,
            "mean": 0.8603842449817449,
            "standard_deviation": 0.21794930623232575,
            "upper_95_t": 0.9988626275359609
          },
          "tail_fraction": {
            "lower_95_t": 0.011983943620568696,
            "mean": 0.012411458333333333,
            "standard_deviation": 0.0006728597874450559,
            "upper_95_t": 0.012838973046097971
          },
          "waiting_time_cv": {
            "lower_95_t": 1.6049161475587457,
            "mean": 1.6513389012872974,
            "standard_deviation": 0.07306416194289922,
            "upper_95_t": 1.6977616550158492
          }
        }
      }
    },
    "0.20": {
      "classification_counts": {
        "original": {
          "F1_initial_only": {
            "F1_initial_only": 12,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 0
          },
          "F2_gaussian_white": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 12,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 0
          },
          "F3_poisson_events": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 10,
            "F4_state_hawkes_events": 2,
            "F5_colored_memory": 0
          },
          "F4_state_hawkes_events": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 12,
            "F5_colored_memory": 0
          },
          "F5_colored_memory": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 12
          }
        },
        "revised": {
          "F1_initial_only": {
            "F1_initial_only": 12,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 0
          },
          "F2_gaussian_white": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 12,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 0
          },
          "F3_poisson_events": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 12,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 0
          },
          "F4_state_hawkes_events": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 12,
            "F5_colored_memory": 0
          },
          "F5_colored_memory": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 12
          }
        }
      },
      "summaries": {
        "F1_initial_only": {
          "absolute_lag1_correlation": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "event_count_fano": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "excess_kurtosis": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "history_rate_ratio": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "innovation_rms": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "one_step_variance_rate": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "one_unit_variance_rate": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "signed_lag1_correlation": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "state_rate_ratio": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "tail_fraction": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "waiting_time_cv": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          }
        },
        "F2_gaussian_white": {
          "absolute_lag1_correlation": {
            "lower_95_t": -0.003557385846438699,
            "mean": -0.0005237229204360719,
            "standard_deviation": 0.00477464220674399,
            "upper_95_t": 0.002509940005566555
          },
          "event_count_fano": {
            "lower_95_t": 0.8471104262060813,
            "mean": 0.9394829106530848,
            "standard_deviation": 0.14538383918730843,
            "upper_95_t": 1.0318553951000882
          },
          "excess_kurtosis": {
            "lower_95_t": -0.022684646285773713,
            "mean": -0.0022029975330395413,
            "standard_deviation": 0.032235797774464184,
            "upper_95_t": 0.01827865121969463
          },
          "history_rate_ratio": {
            "lower_95_t": 1.0521617611894252,
            "mean": 1.447143159034054,
            "standard_deviation": 0.6216560306891759,
            "upper_95_t": 1.8421245568786828
          },
          "innovation_rms": {
            "lower_95_t": 0.0022278181420867455,
            "mean": 0.00223728933253222,
            "standard_deviation": 1.4906582158967924e-05,
            "upper_95_t": 0.0022467605229776946
          },
          "one_step_variance_rate": {
            "lower_95_t": 2.4814863226919904e-05,
            "mean": 2.5027039845695875e-05,
            "standard_deviation": 3.339419915800814e-07,
            "upper_95_t": 2.5239216464471846e-05
          },
          "one_unit_variance_rate": {
            "lower_95_t": 2.4457335692598214e-05,
            "mean": 2.4907949671186458e-05,
            "standard_deviation": 7.092154183231105e-07,
            "upper_95_t": 2.5358563649774702e-05
          },
          "signed_lag1_correlation": {
            "lower_95_t": -0.005701571761209016,
            "mean": -0.0012644235416271223,
            "standard_deviation": 0.006983569263810925,
            "upper_95_t": 0.0031727246779547713
          },
          "state_rate_ratio": {
            "lower_95_t": 0.8470327482256312,
            "mean": 0.9999233171556311,
            "standard_deviation": 0.24063245694477214,
            "upper_95_t": 1.152813886085631
          },
          "tail_fraction": {
            "lower_95_t": 0.012030190343027374,
            "mean": 0.012458333333333335,
            "standard_deviation": 0.0006738486252096754,
            "upper_95_t": 0.012886476323639297
          },
          "waiting_time_cv": {
            "lower_95_t": 0.8181454089860499,
            "mean": 0.8554516151830672,
            "standard_deviation": 0.05871574760498576,
            "upper_95_t": 0.8927578213800845
          }
        },
        "F3_poisson_events": {
          "absolute_lag1_correlation": {
            "lower_95_t": -0.0037772978330241416,
            "mean": 0.0015206750110693462,
            "standard_deviation": 0.008338409826210983,
            "upper_95_t": 0.0068186478551628335
          },
          "event_count_fano": {
            "lower_95_t": 0.7426286011685925,
            "mean": 0.9212625938967892,
            "standard_deviation": 0.2811496933059425,
            "upper_95_t": 1.099896586624986
          },
          "excess_kurtosis": {
            "lower_95_t": 9.745904747522113,
            "mean": 10.165462218935934,
            "standard_deviation": 0.6603359898678066,
            "upper_95_t": 10.585019690349755
          },
          "history_rate_ratio": {
            "lower_95_t": 0.9587439314330608,
            "mean": 1.0178702406641387,
            "standard_deviation": 0.09305812098105738,
            "upper_95_t": 1.0769965498952165
          },
          "innovation_rms": {
            "lower_95_t": 0.0022104909853248008,
            "mean": 0.00222860998214838,
            "standard_deviation": 2.8517250956326464e-05,
            "upper_95_t": 0.002246728978971959
          },
          "one_step_variance_rate": {
            "lower_95_t": 2.443237172374091e-05,
            "mean": 2.48357627766927e-05,
            "standard_deviation": 6.348918763313028e-07,
            "upper_95_t": 2.5239153829644488e-05
          },
          "one_unit_variance_rate": {
            "lower_95_t": 2.4555337059332628e-05,
            "mean": 2.4941816534463894e-05,
            "standard_deviation": 6.082749662743559e-07,
            "upper_95_t": 2.532829600959516e-05
          },
          "signed_lag1_correlation": {
            "lower_95_t": 0.000273832546157678,
            "mean": 0.004607390941971869,
            "standard_deviation": 0.0068205306017001775,
            "upper_95_t": 0.00894094933778606
          },
          "state_rate_ratio": {
            "lower_95_t": 0.9705032549943459,
            "mean": 1.0194408365374426,
            "standard_deviation": 0.07702221638695103,
            "upper_95_t": 1.0683784180805393
          },
          "tail_fraction": {
            "lower_95_t": 0.09065861936826818,
            "mean": 0.09234895833333334,
            "standard_deviation": 0.0026604022804005804,
            "upper_95_t": 0.09403929729839851
          },
          "waiting_time_cv": {
            "lower_95_t": 0.9324454511061855,
            "mean": 0.9482673834948144,
            "standard_deviation": 0.024901931433278856,
            "upper_95_t": 0.9640893158834434
          }
        },
        "F4_state_hawkes_events": {
          "absolute_lag1_correlation": {
            "lower_95_t": 0.23637567111316232,
            "mean": 0.25073643302768844,
            "standard_deviation": 0.02260221442876235,
            "upper_95_t": 0.26509719494221456
          },
          "event_count_fano": {
            "lower_95_t": 1.8311260009014232,
            "mean": 2.1938291679098882,
            "standard_deviation": 0.5708537474202012,
            "upper_95_t": 2.5565323349183533
          },
          "excess_kurtosis": {
            "lower_95_t": 15.88555016278816,
            "mean": 16.858732568581793,
            "standard_deviation": 1.5316789976022898,
            "upper_95_t": 17.831914974375426
          },
          "history_rate_ratio": {
            "lower_95_t": 4.715147760657016,
            "mean": 4.941520276211384,
            "standard_deviation": 0.35628472693797325,
            "upper_95_t": 5.167892791765753
          },
          "innovation_rms": {
            "lower_95_t": 0.0021631521505162256,
            "mean": 0.0022129684770414294,
            "standard_deviation": 7.840526156463713e-05,
            "upper_95_t": 0.0022627848035666333
          },
          "one_step_variance_rate": {
            "lower_95_t": 2.3432521644771326e-05,
            "mean": 2.4512656168619787e-05,
            "standard_deviation": 1.70000953049974e-06,
            "upper_95_t": 2.5592790692468248e-05
          },
          "one_unit_variance_rate": {
            "lower_95_t": 2.35552012963934e-05,
            "mean": 2.4623058882333018e-05,
            "standard_deviation": 1.6806870192850936e-06,
            "upper_95_t": 2.5690916468272636e-05
          },
          "signed_lag1_correlation": {
            "lower_95_t": -0.008314711352164834,
            "mean": -0.00205727974645052,
            "standard_deviation": 0.009848489360624341,
            "upper_95_t": 0.004200151859263794
          },
          "state_rate_ratio": {
            "lower_95_t": 8.147745697006373,
            "mean": 9.159787095762544,
            "standard_deviation": 1.5928386558887115,
            "upper_95_t": 10.171828494518715
          },
          "tail_fraction": {
            "lower_95_t": 0.0773384045428331,
            "mean": 0.080421875,
            "standard_deviation": 0.0048530336254056766,
            "upper_95_t": 0.08350534545716691
          },
          "waiting_time_cv": {
            "lower_95_t": 1.8443896650103258,
            "mean": 1.8994866425120749,
            "standard_deviation": 0.08671640873118133,
            "upper_95_t": 1.954583620013824
          }
        },
        "F5_colored_memory": {
          "absolute_lag1_correlation": {
            "lower_95_t": 0.4054337237799187,
            "mean": 0.4127926564714177,
            "standard_deviation": 0.011582127442127301,
            "upper_95_t": 0.4201515891629167
          },
          "event_count_fano": {
            "lower_95_t": 1.2528465143810112,
            "mean": 1.44704480197319,
            "standard_deviation": 0.30564613242539984,
            "upper_95_t": 1.641243089565369
          },
          "excess_kurtosis": {
            "lower_95_t": -0.02606228199799306,
            "mean": 0.0003227705582035852,
            "standard_deviation": 0.04152708743023542,
            "upper_95_t": 0.026707823114400227
          },
          "history_rate_ratio": {
            "lower_95_t": 18.939569083586857,
            "mean": 21.70930937782225,
            "standard_deviation": 4.359257845432884,
            "upper_95_t": 24.479049672057645
          },
          "innovation_rms": {
            "lower_95_t": 0.003148983296820672,
            "mean": 0.003170532962201633,
            "standard_deviation": 3.39167351083148e-05,
            "upper_95_t": 0.0031920826275825937
          },
          "one_step_variance_rate": {
            "lower_95_t": 4.956685325158618e-05,
            "mean": 5.0252639750442196e-05,
            "standard_deviation": 1.079350357017972e-06,
            "upper_95_t": 5.093842624929821e-05
          },
          "one_unit_variance_rate": {
            "lower_95_t": 0.0001438806025233335,
            "mean": 0.00014721119885385416,
            "standard_deviation": 5.241981789415424e-06,
            "upper_95_t": 0.0001505417951843748
          },
          "signed_lag1_correlation": {
            "lower_95_t": 0.6661256819723627,
            "mean": 0.6705303903215957,
            "standard_deviation": 0.006932512578237306,
            "upper_95_t": 0.6749350986708287
          },
          "state_rate_ratio": {
            "lower_95_t": 0.7305236901542586,
            "mean": 0.8974389483748298,
            "standard_deviation": 0.26270573108781214,
            "upper_95_t": 1.064354206595401
          },
          "tail_fraction": {
            "lower_95_t": 0.01210027975278221,
            "mean": 0.01255729166666667,
            "standard_deviation": 0.0007192850445955259,
            "upper_95_t": 0.01301430358055113
          },
          "waiting_time_cv": {
            "lower_95_t": 1.2370643650938158,
            "mean": 1.2804356333520117,
            "standard_deviation": 0.06826146906784543,
            "upper_95_t": 1.3238069016102076
          }
        }
      }
    }
  },
  "dt_sensitivity_classification_scores": {
    "original": {
      "accuracy": 0.9666666666666667,
      "correct": 174,
      "total": 180
    },
    "revised": {
      "accuracy": 1.0,
      "correct": 180,
      "total": 180
    }
  },
  "held_out_validation_seed_family": {
    "classification_counts": {
      "original": {
        "F1_initial_only": {
          "F1_initial_only": 16,
          "F2_gaussian_white": 0,
          "F3_poisson_events": 0,
          "F4_state_hawkes_events": 0,
          "F5_colored_memory": 0
        },
        "F2_gaussian_white": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 16,
          "F3_poisson_events": 0,
          "F4_state_hawkes_events": 0,
          "F5_colored_memory": 0
        },
        "F3_poisson_events": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 0,
          "F3_poisson_events": 16,
          "F4_state_hawkes_events": 0,
          "F5_colored_memory": 0
        },
        "F4_state_hawkes_events": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 0,
          "F3_poisson_events": 0,
          "F4_state_hawkes_events": 16,
          "F5_colored_memory": 0
        },
        "F5_colored_memory": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 0,
          "F3_poisson_events": 0,
          "F4_state_hawkes_events": 0,
          "F5_colored_memory": 16
        }
      },
      "revised": {
        "F1_initial_only": {
          "F1_initial_only": 16,
          "F2_gaussian_white": 0,
          "F3_poisson_events": 0,
          "F4_state_hawkes_events": 0,
          "F5_colored_memory": 0
        },
        "F2_gaussian_white": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 16,
          "F3_poisson_events": 0,
          "F4_state_hawkes_events": 0,
          "F5_colored_memory": 0
        },
        "F3_poisson_events": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 0,
          "F3_poisson_events": 16,
          "F4_state_hawkes_events": 0,
          "F5_colored_memory": 0
        },
        "F4_state_hawkes_events": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 0,
          "F3_poisson_events": 0,
          "F4_state_hawkes_events": 16,
          "F5_colored_memory": 0
        },
        "F5_colored_memory": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 0,
          "F3_poisson_events": 0,
          "F4_state_hawkes_events": 0,
          "F5_colored_memory": 16
        }
      }
    },
    "scores": {
      "original": {
        "accuracy": 1.0,
        "correct": 80,
        "total": 80
      },
      "revised": {
        "accuracy": 1.0,
        "correct": 80,
        "total": 80
      }
    },
    "summaries": {
      "F1_initial_only": {
        "absolute_lag1_correlation": {
          "lower_95_t": 0.0,
          "mean": 0.0,
          "standard_deviation": 0.0,
          "upper_95_t": 0.0
        },
        "event_count_fano": {
          "lower_95_t": 0.0,
          "mean": 0.0,
          "standard_deviation": 0.0,
          "upper_95_t": 0.0
        },
        "excess_kurtosis": {
          "lower_95_t": 0.0,
          "mean": 0.0,
          "standard_deviation": 0.0,
          "upper_95_t": 0.0
        },
        "history_rate_ratio": {
          "lower_95_t": 0.0,
          "mean": 0.0,
          "standard_deviation": 0.0,
          "upper_95_t": 0.0
        },
        "innovation_rms": {
          "lower_95_t": 0.0,
          "mean": 0.0,
          "standard_deviation": 0.0,
          "upper_95_t": 0.0
        },
        "one_step_variance_rate": {
          "lower_95_t": 0.0,
          "mean": 0.0,
          "standard_deviation": 0.0,
          "upper_95_t": 0.0
        },
        "one_unit_variance_rate": {
          "lower_95_t": 0.0,
          "mean": 0.0,
          "standard_deviation": 0.0,
          "upper_95_t": 0.0
        },
        "signed_lag1_correlation": {
          "lower_95_t": 0.0,
          "mean": 0.0,
          "standard_deviation": 0.0,
          "upper_95_t": 0.0
        },
        "state_rate_ratio": {
          "lower_95_t": 0.0,
          "mean": 0.0,
          "standard_deviation": 0.0,
          "upper_95_t": 0.0
        },
        "tail_fraction": {
          "lower_95_t": 0.0,
          "mean": 0.0,
          "standard_deviation": 0.0,
          "upper_95_t": 0.0
        },
        "waiting_time_cv": {
          "lower_95_t": 0.0,
          "mean": 0.0,
          "standard_deviation": 0.0,
          "upper_95_t": 0.0
        }
      },
      "F2_gaussian_white": {
        "absolute_lag1_correlation": {
          "lower_95_t": -0.0021417801932316887,
          "mean": -6.673054833990417e-05,
          "standard_deviation": 0.003894156723934578,
          "upper_95_t": 0.00200831909655188
        },
        "event_count_fano": {
          "lower_95_t": 0.9055358413430492,
          "mean": 1.0124577250308913,
          "standard_deviation": 0.2006557160325072,
          "upper_95_t": 1.1193796087187333
        },
        "excess_kurtosis": {
          "lower_95_t": -0.006001158487488359,
          "mean": 0.0016832691444405579,
          "standard_deviation": 0.014421035952624275,
          "upper_95_t": 0.009367696776369474
        },
        "history_rate_ratio": {
          "lower_95_t": 0.8062247419506688,
          "mean": 0.9878654913615342,
          "standard_deviation": 0.34087740859603644,
          "upper_95_t": 1.1695062407723995
        },
        "innovation_rms": {
          "lower_95_t": 0.0015789417989476218,
          "mean": 0.0015810773663915854,
          "standard_deviation": 4.0077278834265796e-06,
          "upper_95_t": 0.0015832129338355491
        },
        "one_step_variance_rate": {
          "lower_95_t": 2.4930377272601164e-05,
          "mean": 2.4997859732625106e-05,
          "standard_deviation": 1.2664144016833473e-07,
          "upper_95_t": 2.506534219264905e-05
        },
        "one_unit_variance_rate": {
          "lower_95_t": 2.4655316700650107e-05,
          "mean": 2.4865327097672468e-05,
          "standard_deviation": 3.9411751023597936e-07,
          "upper_95_t": 2.507533749469483e-05
        },
        "signed_lag1_correlation": {
          "lower_95_t": -0.003359656822413814,
          "mean": -0.0016192347429133194,
          "standard_deviation": 0.0032661755153932733,
          "upper_95_t": 0.00012118733658717548
        },
        "state_rate_ratio": {
          "lower_95_t": 0.96904993189409,
          "mean": 1.0230305697850293,
          "standard_deviation": 0.10130314931151492,
          "upper_95_t": 1.0770112076759684
        },
        "tail_fraction": {
          "lower_95_t": 0.012250216993062708,
          "mean": 0.012438476562500002,
          "standard_deviation": 0.0003532986644314728,
          "upper_95_t": 0.012626736131937296
        },
        "waiting_time_cv": {
          "lower_95_t": 0.9809300001031774,
          "mean": 1.0042308939393625,
          "standard_deviation": 0.04372778869615807,
          "upper_95_t": 1.0275317877755477
        }
      },
      "F3_poisson_events": {
        "absolute_lag1_correlation": {
          "lower_95_t": -0.0003377975338171471,
          "mean": 0.0018773957298295978,
          "standard_deviation": 0.004157158246155803,
          "upper_95_t": 0.004092588993476342
        },
        "event_count_fano": {
          "lower_95_t": 0.8725678435561115,
          "mean": 0.971985090292474,
          "standard_deviation": 0.18657208554336013,
          "upper_95_t": 1.0714023370288366
        },
        "excess_kurtosis": {
          "lower_95_t": 19.4617330403842,
          "mean": 19.766507271374188,
          "standard_deviation": 0.571956735499478,
          "upper_95_t": 20.071281502364176
        },
        "history_rate_ratio": {
          "lower_95_t": 1.0002803351753775,
          "mean": 1.0474752404180654,
          "standard_deviation": 0.08856865571322402,
          "upper_95_t": 1.0946701456607533
        },
        "innovation_rms": {
          "lower_95_t": 0.001575199354915086,
          "mean": 0.0015835956082375984,
          "standard_deviation": 1.575688871454697e-05,
          "upper_95_t": 0.0015919918615601109
        },
        "one_step_variance_rate": {
          "lower_95_t": 2.481430108400412e-05,
          "mean": 2.5079804306030267e-05,
          "standard_deviation": 4.982585162839967e-07,
          "upper_95_t": 2.5345307528056415e-05
        },
        "one_unit_variance_rate": {
          "lower_95_t": 2.475580314694732e-05,
          "mean": 2.5101769899349503e-05,
          "standard_deviation": 6.492609747633429e-07,
          "upper_95_t": 2.5447736651751685e-05
        },
        "signed_lag1_correlation": {
          "lower_95_t": -0.0021794572554494633,
          "mean": 2.5133905121690832e-05,
          "standard_deviation": 0.004137261733760886,
          "upper_95_t": 0.002229725065692845
        },
        "state_rate_ratio": {
          "lower_95_t": 1.006051221147317,
          "mean": 1.0337807370600158,
          "standard_deviation": 0.05203879391932281,
          "upper_95_t": 1.0615102529727147
        },
        "tail_fraction": {
          "lower_95_t": 0.04792632740333358,
          "mean": 0.0484306640625,
          "standard_deviation": 0.0009464669904425595,
          "upper_95_t": 0.04893500072166643
        },
        "waiting_time_cv": {
          "lower_95_t": 0.9805515117712592,
          "mean": 0.9884076123076616,
          "standard_deviation": 0.014743207133886624,
          "upper_95_t": 0.996263712844064
        }
      },
      "F4_state_hawkes_events": {
        "absolute_lag1_correlation": {
          "lower_95_t": 0.16516346274702093,
          "mean": 0.17164315047595982,
          "standard_deviation": 0.012160152216483314,
          "upper_95_t": 0.17812283820489871
        },
        "event_count_fano": {
          "lower_95_t": 2.5144055845075424,
          "mean": 2.8675193769168383,
          "standard_deviation": 0.6626735183949829,
          "upper_95_t": 3.2206331693261343
        },
        "excess_kurtosis": {
          "lower_95_t": 25.546409638611163,
          "mean": 26.30417064832703,
          "standard_deviation": 1.4220576063732626,
          "upper_95_t": 27.061931658042898
        },
        "history_rate_ratio": {
          "lower_95_t": 5.230675220240294,
          "mean": 5.414852651145839,
          "standard_deviation": 0.3456378900251461,
          "upper_95_t": 5.599030082051384
        },
        "innovation_rms": {
          "lower_95_t": 0.00155851569348418,
          "mean": 0.001576874641229414,
          "standard_deviation": 3.4453450298146986e-05,
          "upper_95_t": 0.001595233588974648
        },
        "one_step_variance_rate": {
          "lower_95_t": 2.4291395132136824e-05,
          "mean": 2.487603369903564e-05,
          "standard_deviation": 1.0971661386343568e-06,
          "upper_95_t": 2.546067226593446e-05
        },
        "one_unit_variance_rate": {
          "lower_95_t": 2.410603582560317e-05,
          "mean": 2.4808646935190064e-05,
          "standard_deviation": 1.318560152738715e-06,
          "upper_95_t": 2.5511258044776956e-05
        },
        "signed_lag1_correlation": {
          "lower_95_t": -0.00549237939954668,
          "mean": -0.0020501110466119477,
          "standard_deviation": 0.006459957469049884,
          "upper_95_t": 0.0013921573063227846
        },
        "state_rate_ratio": {
          "lower_95_t": 7.985086510131881,
          "mean": 8.802041365348774,
          "standard_deviation": 1.5331441589484365,
          "upper_95_t": 9.618996220565668
        },
        "tail_fraction": {
          "lower_95_t": 0.043719796081690035,
          "mean": 0.044672851562500004,
          "standard_deviation": 0.0017885583692010343,
          "upper_95_t": 0.045625907043309974
        },
        "waiting_time_cv": {
          "lower_95_t": 2.261411878694311,
          "mean": 2.331644184029331,
          "standard_deviation": 0.13180195699465191,
          "upper_95_t": 2.4018764893643514
        }
      },
      "F5_colored_memory": {
        "absolute_lag1_correlation": {
          "lower_95_t": 0.6288203463036125,
          "mean": 0.6314316141960827,
          "standard_deviation": 0.004900454524782103,
          "upper_95_t": 0.634042882088553
        },
        "event_count_fano": {
          "lower_95_t": 2.1132800454205403,
          "mean": 2.4097603546397206,
          "standard_deviation": 0.5563918880216886,
          "upper_95_t": 2.706240663858901
        },
        "excess_kurtosis": {
          "lower_95_t": -0.01765234444642067,
          "mean": -0.004896200320778449,
          "standard_deviation": 0.023938908903039176,
          "upper_95_t": 0.007859943804863772
        },
        "history_rate_ratio": {
          "lower_95_t": 46.83076241549249,
          "mean": 49.19901168823206,
          "standard_deviation": 4.444391897849242,
          "upper_95_t": 51.56726096097164
        },
        "innovation_rms": {
          "lower_95_t": 0.0015782184538583035,
          "mean": 0.0015841052772068683,
          "standard_deviation": 1.1047549046290055e-05,
          "upper_95_t": 0.001589992100555433
        },
        "one_step_variance_rate": {
          "lower_95_t": 2.4907061255280772e-05,
          "mean": 2.50935819802582e-05,
          "standard_deviation": 3.5003544956722444e-07,
          "upper_95_t": 2.5280102705235628e-05
        },
        "one_unit_variance_rate": {
          "lower_95_t": 0.00014266202848022214,
          "mean": 0.000144488711285054,
          "standard_deviation": 3.428057321155193e-06,
          "upper_95_t": 0.00014631539408988588
        },
        "signed_lag1_correlation": {
          "lower_95_t": 0.8185227491198667,
          "mean": 0.8199360115863727,
          "standard_deviation": 0.002652209093009847,
          "upper_95_t": 0.8213492740528788
        },
        "state_rate_ratio": {
          "lower_95_t": 0.9419563121016483,
          "mean": 1.0338810440658153,
          "standard_deviation": 0.17251120422847177,
          "upper_95_t": 1.1258057760299822
        },
        "tail_fraction": {
          "lower_95_t": 0.012131814303381961,
          "mean": 0.0123564453125,
          "standard_deviation": 0.0004215553862600923,
          "upper_95_t": 0.01258107632161804
        },
        "waiting_time_cv": {
          "lower_95_t": 1.6524751567654725,
          "mean": 1.677718774409299,
          "standard_deviation": 0.04737361519332059,
          "upper_95_t": 1.7029623920531254
        }
      }
    }
  },
  "identifiability_boundaries": {
    "event_dependence_sweep": [
      {
        "hawkes_branching_ratio": 0.0,
        "history_rate_ratio_interval": {
          "lower_95_t": 0.9519391229451754,
          "mean": 1.009251391473191,
          "standard_deviation": 0.09020302616107863,
          "upper_95_t": 1.066563660001207
        },
        "revised_classification_counts": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 0,
          "F3_poisson_events": 12,
          "F4_state_hawkes_events": 0,
          "F5_colored_memory": 0
        },
        "state_coefficient": 0.0,
        "state_rate_ratio_interval": {
          "lower_95_t": 0.9458577403368084,
          "mean": 0.9988323303621768,
          "standard_deviation": 0.08337601097738583,
          "upper_95_t": 1.0518069203875453
        }
      },
      {
        "hawkes_branching_ratio": 0.1,
        "history_rate_ratio_interval": {
          "lower_95_t": 1.3445252260182434,
          "mean": 1.4401605578331782,
          "standard_deviation": 0.15051919177495282,
          "upper_95_t": 1.535795889648113
        },
        "revised_classification_counts": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 0,
          "F3_poisson_events": 7,
          "F4_state_hawkes_events": 5,
          "F5_colored_memory": 0
        },
        "state_coefficient": 0.0,
        "state_rate_ratio_interval": {
          "lower_95_t": 0.9490822387883561,
          "mean": 1.0103746331659527,
          "standard_deviation": 0.09646729392354962,
          "upper_95_t": 1.0716670275435494
        }
      },
      {
        "hawkes_branching_ratio": 0.3,
        "history_rate_ratio_interval": {
          "lower_95_t": 2.1493959616598977,
          "mean": 2.2803162398541863,
          "standard_deviation": 0.2060537051190422,
          "upper_95_t": 2.411236518048475
        },
        "revised_classification_counts": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 0,
          "F3_poisson_events": 0,
          "F4_state_hawkes_events": 12,
          "F5_colored_memory": 0
        },
        "state_coefficient": 0.0,
        "state_rate_ratio_interval": {
          "lower_95_t": 0.9216908711684244,
          "mean": 0.9852353567508146,
          "standard_deviation": 0.10001183067075295,
          "upper_95_t": 1.0487798423332049
        }
      },
      {
        "hawkes_branching_ratio": 0.6,
        "history_rate_ratio_interval": {
          "lower_95_t": 4.340778488953402,
          "mean": 4.5673595685799615,
          "standard_deviation": 0.35661298318996404,
          "upper_95_t": 4.793940648206521
        },
        "revised_classification_counts": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 0,
          "F3_poisson_events": 0,
          "F4_state_hawkes_events": 12,
          "F5_colored_memory": 0
        },
        "state_coefficient": 0.0,
        "state_rate_ratio_interval": {
          "lower_95_t": 0.895755263962104,
          "mean": 1.0391676894239603,
          "standard_deviation": 0.22571493151481145,
          "upper_95_t": 1.1825801148858166
        }
      },
      {
        "hawkes_branching_ratio": 0.0,
        "history_rate_ratio_interval": {
          "lower_95_t": 1.0000767098945935,
          "mean": 1.08083328445917,
          "standard_deviation": 0.12710171129531772,
          "upper_95_t": 1.1615898590237463
        },
        "revised_classification_counts": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 0,
          "F3_poisson_events": 0,
          "F4_state_hawkes_events": 12,
          "F5_colored_memory": 0
        },
        "state_coefficient": 0.3,
        "state_rate_ratio_interval": {
          "lower_95_t": 2.095840080848945,
          "mean": 2.199729147853607,
          "standard_deviation": 0.16350963710834007,
          "upper_95_t": 2.3036182148582696
        }
      },
      {
        "hawkes_branching_ratio": 0.0,
        "history_rate_ratio_interval": {
          "lower_95_t": 1.5500678031933532,
          "mean": 1.647612273431086,
          "standard_deviation": 0.15352395964612153,
          "upper_95_t": 1.745156743668819
        },
        "revised_classification_counts": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 0,
          "F3_poisson_events": 0,
          "F4_state_hawkes_events": 12,
          "F5_colored_memory": 0
        },
        "state_coefficient": 0.9,
        "state_rate_ratio_interval": {
          "lower_95_t": 8.628145135876908,
          "mean": 9.051853113512685,
          "standard_deviation": 0.6668684170589916,
          "upper_95_t": 9.475561091148462
        }
      },
      {
        "hawkes_branching_ratio": 0.3,
        "history_rate_ratio_interval": {
          "lower_95_t": 2.1260449693707266,
          "mean": 2.2620947684885993,
          "standard_deviation": 0.2141269906815857,
          "upper_95_t": 2.398144567606472
        },
        "revised_classification_counts": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 0,
          "F3_poisson_events": 0,
          "F4_state_hawkes_events": 12,
          "F5_colored_memory": 0
        },
        "state_coefficient": 0.3,
        "state_rate_ratio_interval": {
          "lower_95_t": 1.9577763120539615,
          "mean": 2.1221509372352525,
          "standard_deviation": 0.25870706213971634,
          "upper_95_t": 2.2865255624165433
        }
      }
    ],
    "interpretation": [
      "Colored memory shorter than the observation interval can be observationally equivalent to white Gaussian forcing.",
      "High-rate small Poisson jumps approach a Gaussian law and cannot always be identified as discrete events.",
      "Weak state or history dependence can be observationally equivalent to independent Poisson events."
    ],
    "memory_resolution_sweep": [
      {
        "expected_lag1_correlation": 0.006737946999085467,
        "memory_time": 0.02,
        "memory_to_observation_step_ratio": 0.19999999999999998,
        "observed_lag1_interval": {
          "lower_95_t": 0.0020295857499592843,
          "mean": 0.0058114260867197,
          "standard_deviation": 0.0059521887999786135,
          "upper_95_t": 0.009593266423480115
        },
        "revised_classification_counts": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 12,
          "F3_poisson_events": 0,
          "F4_state_hawkes_events": 0,
          "F5_colored_memory": 0
        }
      },
      {
        "expected_lag1_correlation": 0.1353352832366127,
        "memory_time": 0.05,
        "memory_to_observation_step_ratio": 0.5,
        "observed_lag1_interval": {
          "lower_95_t": 0.1304563284918801,
          "mean": 0.133277683255733,
          "standard_deviation": 0.004440493180776869,
          "upper_95_t": 0.1360990380195859
        },
        "revised_classification_counts": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 12,
          "F3_poisson_events": 0,
          "F4_state_hawkes_events": 0,
          "F5_colored_memory": 0
        }
      },
      {
        "expected_lag1_correlation": 0.36787944117144233,
        "memory_time": 0.1,
        "memory_to_observation_step_ratio": 1.0,
        "observed_lag1_interval": {
          "lower_95_t": 0.3661243227512503,
          "mean": 0.36934540963818235,
          "standard_deviation": 0.005069626315472252,
          "upper_95_t": 0.3725664965251144
        },
        "revised_classification_counts": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 0,
          "F3_poisson_events": 0,
          "F4_state_hawkes_events": 0,
          "F5_colored_memory": 12
        }
      },
      {
        "expected_lag1_correlation": 0.6065306597126334,
        "memory_time": 0.2,
        "memory_to_observation_step_ratio": 2.0,
        "observed_lag1_interval": {
          "lower_95_t": 0.606670771726395,
          "mean": 0.6088933379476377,
          "standard_deviation": 0.0034980677636494615,
          "upper_95_t": 0.6111159041688803
        },
        "revised_classification_counts": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 0,
          "F3_poisson_events": 0,
          "F4_state_hawkes_events": 0,
          "F5_colored_memory": 12
        }
      },
      {
        "expected_lag1_correlation": 0.8187307530779818,
        "memory_time": 0.5,
        "memory_to_observation_step_ratio": 5.0,
        "observed_lag1_interval": {
          "lower_95_t": 0.8158811345901793,
          "mean": 0.8177931702299973,
          "standard_deviation": 0.003009327762957323,
          "upper_95_t": 0.8197052058698153
        },
        "revised_classification_counts": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 0,
          "F3_poisson_events": 0,
          "F4_state_hawkes_events": 0,
          "F5_colored_memory": 12
        }
      }
    ],
    "poisson_resolution_sweep": [
      {
        "expected_excess_kurtosis": 40.0,
        "observed_excess_kurtosis_interval": {
          "lower_95_t": 39.22755510172541,
          "mean": 40.53108043233804,
          "standard_deviation": 2.0516013851624515,
          "upper_95_t": 41.834605762950666
        },
        "poisson_rate": 0.25,
        "revised_classification_counts": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 0,
          "F3_poisson_events": 10,
          "F4_state_hawkes_events": 2,
          "F5_colored_memory": 0
        }
      },
      {
        "expected_excess_kurtosis": 20.0,
        "observed_excess_kurtosis_interval": {
          "lower_95_t": 19.944789417794553,
          "mean": 20.316329871066554,
          "standard_deviation": 0.5847626361188422,
          "upper_95_t": 20.687870324338554
        },
        "poisson_rate": 0.5,
        "revised_classification_counts": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 0,
          "F3_poisson_events": 12,
          "F4_state_hawkes_events": 0,
          "F5_colored_memory": 0
        }
      },
      {
        "expected_excess_kurtosis": 10.0,
        "observed_excess_kurtosis_interval": {
          "lower_95_t": 9.70901860706072,
          "mean": 10.009215112974049,
          "standard_deviation": 0.47247533506944833,
          "upper_95_t": 10.309411618887378
        },
        "poisson_rate": 1.0,
        "revised_classification_counts": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 0,
          "F3_poisson_events": 12,
          "F4_state_hawkes_events": 0,
          "F5_colored_memory": 0
        }
      },
      {
        "expected_excess_kurtosis": 5.0,
        "observed_excess_kurtosis_interval": {
          "lower_95_t": 4.877697365384861,
          "mean": 4.984815336265657,
          "standard_deviation": 0.1685915664803759,
          "upper_95_t": 5.091933307146453
        },
        "poisson_rate": 2.0,
        "revised_classification_counts": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 0,
          "F3_poisson_events": 7,
          "F4_state_hawkes_events": 5,
          "F5_colored_memory": 0
        }
      },
      {
        "expected_excess_kurtosis": 2.0,
        "observed_excess_kurtosis_interval": {
          "lower_95_t": 1.952886369713992,
          "mean": 2.0022175197315444,
          "standard_deviation": 0.077641648636089,
          "upper_95_t": 2.051548669749097
        },
        "poisson_rate": 5.0,
        "revised_classification_counts": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 5,
          "F3_poisson_events": 7,
          "F4_state_hawkes_events": 0,
          "F5_colored_memory": 0
        }
      },
      {
        "expected_excess_kurtosis": 1.0,
        "observed_excess_kurtosis_interval": {
          "lower_95_t": 0.9448760197160776,
          "mean": 0.9852721187870627,
          "standard_deviation": 0.06357888938778235,
          "upper_95_t": 1.0256682178580478
        },
        "poisson_rate": 10.0,
        "revised_classification_counts": {
          "F1_initial_only": 0,
          "F2_gaussian_white": 12,
          "F3_poisson_events": 0,
          "F4_state_hawkes_events": 0,
          "F5_colored_memory": 0
        }
      }
    ]
  },
  "limitations": [
    "Synthetic identifiability does not establish which candidate, if any, exists in nature.",
    "The controls isolate source innovations after a known deterministic backbone; detector performance can degrade when the backbone is misspecified or observations are coarse.",
    "The F4 control combines state dependence and Hawkes memory; a later ablation must separate those two mechanisms.",
    "F7-F10 are not classified by this protocol.",
    "The decision tree identifies declared observable regimes, not hidden ontologies below the temporal or amplitude resolution."
  ],
  "original_pre_registered_decision_tree": [
    "innovation_rms < 1e-15 -> F1_initial_only",
    "signed_lag1_correlation > 0.3 -> F5_colored_memory",
    "excess_kurtosis < 2.0 -> F2_gaussian_white",
    "state_rate_ratio > 1.5 OR history_rate_ratio > 1.5 OR event_count_fano > 1.3 -> F4_state_hawkes_events",
    "otherwise -> F3_poisson_events"
  ],
  "post_revision_audit_classification_scores": {
    "original": {
      "accuracy": 0.9833333333333333,
      "correct": 177,
      "total": 180
    },
    "revised": {
      "accuracy": 1.0,
      "correct": 180,
      "total": 180
    }
  },
  "post_revision_audit_dt_sensitivity": {
    "0.05": {
      "classification_counts": {
        "original": {
          "F1_initial_only": {
            "F1_initial_only": 12,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 0
          },
          "F2_gaussian_white": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 12,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 0
          },
          "F3_poisson_events": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 11,
            "F4_state_hawkes_events": 1,
            "F5_colored_memory": 0
          },
          "F4_state_hawkes_events": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 12,
            "F5_colored_memory": 0
          },
          "F5_colored_memory": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 12
          }
        },
        "revised": {
          "F1_initial_only": {
            "F1_initial_only": 12,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 0
          },
          "F2_gaussian_white": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 12,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 0
          },
          "F3_poisson_events": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 12,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 0
          },
          "F4_state_hawkes_events": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 12,
            "F5_colored_memory": 0
          },
          "F5_colored_memory": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 12
          }
        }
      },
      "summaries": {
        "F1_initial_only": {
          "absolute_lag1_correlation": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "event_count_fano": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "excess_kurtosis": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "history_rate_ratio": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "innovation_rms": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "one_step_variance_rate": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "one_unit_variance_rate": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "signed_lag1_correlation": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "state_rate_ratio": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "tail_fraction": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "waiting_time_cv": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          }
        },
        "F2_gaussian_white": {
          "absolute_lag1_correlation": {
            "lower_95_t": -0.003758729728416599,
            "mean": -0.0006910396818853295,
            "standard_deviation": 0.00482819704451369,
            "upper_95_t": 0.00237665036464594
          },
          "event_count_fano": {
            "lower_95_t": 0.8051520301208053,
            "mean": 0.9311138369814991,
            "standard_deviation": 0.1982496322580178,
            "upper_95_t": 1.0570756438421929
          },
          "excess_kurtosis": {
            "lower_95_t": -0.010028512815035143,
            "mean": -0.0016961049959058523,
            "standard_deviation": 0.013114267150780979,
            "upper_95_t": 0.006636302823223438
          },
          "history_rate_ratio": {
            "lower_95_t": 0.8894898468141725,
            "mean": 1.1199987869660168,
            "standard_deviation": 0.3627949912454669,
            "upper_95_t": 1.3505077271178612
          },
          "innovation_rms": {
            "lower_95_t": 0.0011150424854540965,
            "mean": 0.0011168449959558704,
            "standard_deviation": 2.836947587716601e-06,
            "upper_95_t": 0.0011186475064576442
          },
          "one_step_variance_rate": {
            "lower_95_t": 2.48662386515447e-05,
            "mean": 2.4946758707416315e-05,
            "standard_deviation": 1.267294576331138e-07,
            "upper_95_t": 2.502727876328793e-05
          },
          "one_unit_variance_rate": {
            "lower_95_t": 2.461986126131317e-05,
            "mean": 2.5039945202370127e-05,
            "standard_deviation": 6.611645935195675e-07,
            "upper_95_t": 2.5460029143427086e-05
          },
          "signed_lag1_correlation": {
            "lower_95_t": -0.00332758294679295,
            "mean": -0.0008870668368469442,
            "standard_deviation": 0.003841096228888274,
            "upper_95_t": 0.0015534492730990613
          },
          "state_rate_ratio": {
            "lower_95_t": 0.9220581052775485,
            "mean": 0.9920562631307565,
            "standard_deviation": 0.11016918063492391,
            "upper_95_t": 1.0620544209839644
          },
          "tail_fraction": {
            "lower_95_t": 0.012225814011963524,
            "mean": 0.012382812500000001,
            "standard_deviation": 0.0002470978568346407,
            "upper_95_t": 0.01253981098803648
          },
          "waiting_time_cv": {
            "lower_95_t": 0.9653638278026359,
            "mean": 0.9911681611177382,
            "standard_deviation": 0.040613101049272994,
            "upper_95_t": 1.0169724944328407
          }
        },
        "F3_poisson_events": {
          "absolute_lag1_correlation": {
            "lower_95_t": -0.00133900275980424,
            "mean": 0.0009566766012113406,
            "standard_deviation": 0.003613139573386663,
            "upper_95_t": 0.0032523559622269216
          },
          "event_count_fano": {
            "lower_95_t": 0.7809004658902713,
            "mean": 0.9357082424833777,
            "standard_deviation": 0.24364992488720555,
            "upper_95_t": 1.090516019076484
          },
          "excess_kurtosis": {
            "lower_95_t": 38.90992912718407,
            "mean": 40.12637570255209,
            "standard_deviation": 1.9145492767894579,
            "upper_95_t": 41.342822277920106
          },
          "history_rate_ratio": {
            "lower_95_t": 0.9521404107954831,
            "mean": 1.0520242474276091,
            "standard_deviation": 0.15720585766714737,
            "upper_95_t": 1.1519080840597353
          },
          "innovation_rms": {
            "lower_95_t": 0.0011104583278944524,
            "mean": 0.0011188072854409524,
            "standard_deviation": 1.3140314549170886e-05,
            "upper_95_t": 0.0011271562429874525
          },
          "one_step_variance_rate": {
            "lower_95_t": 2.46627118035689e-05,
            "mean": 2.5037425150553378e-05,
            "standard_deviation": 5.897564118304579e-07,
            "upper_95_t": 2.5412138497537857e-05
          },
          "one_unit_variance_rate": {
            "lower_95_t": 2.427602160700792e-05,
            "mean": 2.485132113225487e-05,
            "standard_deviation": 9.054563614235476e-07,
            "upper_95_t": 2.5426620657501817e-05
          },
          "signed_lag1_correlation": {
            "lower_95_t": -0.0011528104532524412,
            "mean": 0.001146851400781371,
            "standard_deviation": 0.00361940756680476,
            "upper_95_t": 0.003446513254815183
          },
          "state_rate_ratio": {
            "lower_95_t": 0.9214628274702409,
            "mean": 0.9700532517325594,
            "standard_deviation": 0.07647583010554367,
            "upper_95_t": 1.018643675994878
          },
          "tail_fraction": {
            "lower_95_t": 0.024169355757807227,
            "mean": 0.024567708333333337,
            "standard_deviation": 0.0006269618829334964,
            "upper_95_t": 0.024966060908859448
          },
          "waiting_time_cv": {
            "lower_95_t": 0.967985878573856,
            "mean": 0.9804298892506577,
            "standard_deviation": 0.01958546484823894,
            "upper_95_t": 0.9928738999274593
          }
        },
        "F4_state_hawkes_events": {
          "absolute_lag1_correlation": {
            "lower_95_t": 0.09210907537991013,
            "mean": 0.09894635224811227,
            "standard_deviation": 0.0107611001981451,
            "upper_95_t": 0.1057836291163144
          },
          "event_count_fano": {
            "lower_95_t": 2.6226139201351986,
            "mean": 3.015104824679718,
            "standard_deviation": 0.6177362760175569,
            "upper_95_t": 3.407595729224237
          },
          "excess_kurtosis": {
            "lower_95_t": 46.12254249866498,
            "mean": 48.63802814371106,
            "standard_deviation": 3.9590897948314954,
            "upper_95_t": 51.153513788757145
          },
          "history_rate_ratio": {
            "lower_95_t": 5.340108743161103,
            "mean": 5.657727592949765,
            "standard_deviation": 0.4998961331068833,
            "upper_95_t": 5.975346442738427
          },
          "innovation_rms": {
            "lower_95_t": 0.0010739625823203709,
            "mean": 0.0011015623353015209,
            "standard_deviation": 4.343888846383744e-05,
            "upper_95_t": 0.0011291620882826708
          },
          "one_step_variance_rate": {
            "lower_95_t": 2.3060919963323164e-05,
            "mean": 2.43032212524414e-05,
            "standard_deviation": 1.9552416709433958e-06,
            "upper_95_t": 2.5545522541559637e-05
          },
          "one_unit_variance_rate": {
            "lower_95_t": 2.2840634606401342e-05,
            "mean": 2.4229548866182137e-05,
            "standard_deviation": 2.185993898483706e-06,
            "upper_95_t": 2.561846312596293e-05
          },
          "signed_lag1_correlation": {
            "lower_95_t": -0.008353438772641645,
            "mean": -0.0009008395807513048,
            "standard_deviation": 0.011729547916001712,
            "upper_95_t": 0.006551759611139034
          },
          "state_rate_ratio": {
            "lower_95_t": 8.882898154637463,
            "mean": 10.131165958124157,
            "standard_deviation": 1.964632289487928,
            "upper_95_t": 11.379433761610851
          },
          "tail_fraction": {
            "lower_95_t": 0.021809088914608137,
            "mean": 0.0229140625,
            "standard_deviation": 0.0017391034029944328,
            "upper_95_t": 0.02401903608539186
          },
          "waiting_time_cv": {
            "lower_95_t": 2.0640728227385226,
            "mean": 2.1259543590376464,
            "standard_deviation": 0.09739453665054353,
            "upper_95_t": 2.1878358953367703
          }
        },
        "F5_colored_memory": {
          "absolute_lag1_correlation": {
            "lower_95_t": 0.783577184143274,
            "mean": 0.7857409794512433,
            "standard_deviation": 0.0034055689956952536,
            "upper_95_t": 0.7879047747592126
          },
          "event_count_fano": {
            "lower_95_t": 3.5177397082598256,
            "mean": 4.386488838016436,
            "standard_deviation": 1.3673128370506478,
            "upper_95_t": 5.255237967773046
          },
          "excess_kurtosis": {
            "lower_95_t": -0.04294478594387599,
            "mean": -0.018613351882092084,
            "standard_deviation": 0.038294924273304456,
            "upper_95_t": 0.005718082179691827
          },
          "history_rate_ratio": {
            "lower_95_t": 87.97559175264861,
            "mean": 91.13962256047483,
            "standard_deviation": 4.979826502475537,
            "upper_95_t": 94.30365336830106
          },
          "innovation_rms": {
            "lower_95_t": 0.0007852845937243646,
            "mean": 0.0007893421756430705,
            "standard_deviation": 6.3861748516345694e-06,
            "upper_95_t": 0.0007933997575617763
          },
          "one_step_variance_rate": {
            "lower_95_t": 1.2328415009070442e-05,
            "mean": 1.245630805072766e-05,
            "standard_deviation": 2.012891773213722e-07,
            "upper_95_t": 1.2584201092384877e-05
          },
          "one_unit_variance_rate": {
            "lower_95_t": 0.00013928336227333807,
            "mean": 0.0001415006241198529,
            "standard_deviation": 3.489719277982726e-06,
            "upper_95_t": 0.00014371788596636775
          },
          "signed_lag1_correlation": {
            "lower_95_t": 0.9037660701246631,
            "mean": 0.9046756406221411,
            "standard_deviation": 0.0014315610511777984,
            "upper_95_t": 0.9055852111196191
          },
          "state_rate_ratio": {
            "lower_95_t": 1.0029313059150047,
            "mean": 1.1515907192673251,
            "standard_deviation": 0.23397309679261824,
            "upper_95_t": 1.3002501326196456
          },
          "tail_fraction": {
            "lower_95_t": 0.01161772856640573,
            "mean": 0.011949218749999999,
            "standard_deviation": 0.0005217280430677418,
            "upper_95_t": 0.012280708933594267
          },
          "waiting_time_cv": {
            "lower_95_t": 2.1400731275835287,
            "mean": 2.2101220168917215,
            "standard_deviation": 0.11024902620514324,
            "upper_95_t": 2.2801709061999142
          }
        }
      }
    },
    "0.10": {
      "classification_counts": {
        "original": {
          "F1_initial_only": {
            "F1_initial_only": 12,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 0
          },
          "F2_gaussian_white": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 12,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 0
          },
          "F3_poisson_events": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 11,
            "F4_state_hawkes_events": 1,
            "F5_colored_memory": 0
          },
          "F4_state_hawkes_events": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 12,
            "F5_colored_memory": 0
          },
          "F5_colored_memory": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 12
          }
        },
        "revised": {
          "F1_initial_only": {
            "F1_initial_only": 12,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 0
          },
          "F2_gaussian_white": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 12,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 0
          },
          "F3_poisson_events": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 12,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 0
          },
          "F4_state_hawkes_events": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 12,
            "F5_colored_memory": 0
          },
          "F5_colored_memory": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 12
          }
        }
      },
      "summaries": {
        "F1_initial_only": {
          "absolute_lag1_correlation": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "event_count_fano": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "excess_kurtosis": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "history_rate_ratio": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "innovation_rms": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "one_step_variance_rate": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "one_unit_variance_rate": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "signed_lag1_correlation": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "state_rate_ratio": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "tail_fraction": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "waiting_time_cv": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          }
        },
        "F2_gaussian_white": {
          "absolute_lag1_correlation": {
            "lower_95_t": -0.0030732067839221847,
            "mean": -0.00039664332751789596,
            "standard_deviation": 0.004212608045026235,
            "upper_95_t": 0.002279920128886393
          },
          "event_count_fano": {
            "lower_95_t": 0.7811644388216028,
            "mean": 0.9854587455847063,
            "standard_deviation": 0.3215361243030115,
            "upper_95_t": 1.1897530523478097
          },
          "excess_kurtosis": {
            "lower_95_t": -0.01609676099265355,
            "mean": 0.005321823628430959,
            "standard_deviation": 0.033710428823185375,
            "upper_95_t": 0.02674040824951547
          },
          "history_rate_ratio": {
            "lower_95_t": 0.7206476658108891,
            "mean": 0.9813957924471314,
            "standard_deviation": 0.4103880494090698,
            "upper_95_t": 1.2421439190833736
          },
          "innovation_rms": {
            "lower_95_t": 0.0015803021252035051,
            "mean": 0.0015839526265777365,
            "standard_deviation": 5.745476133087931e-06,
            "upper_95_t": 0.001587603127951968
          },
          "one_step_variance_rate": {
            "lower_95_t": 2.497305545446829e-05,
            "mean": 2.5087889967431295e-05,
            "standard_deviation": 1.807365306423571e-07,
            "upper_95_t": 2.52027244803943e-05
          },
          "one_unit_variance_rate": {
            "lower_95_t": 2.492978046330272e-05,
            "mean": 2.52566828155059e-05,
            "standard_deviation": 5.145073155407741e-07,
            "upper_95_t": 2.5583585167709077e-05
          },
          "signed_lag1_correlation": {
            "lower_95_t": -0.00224921836410809,
            "mean": 0.0021849205036871683,
            "standard_deviation": 0.006978832884586901,
            "upper_95_t": 0.0066190593714824265
          },
          "state_rate_ratio": {
            "lower_95_t": 0.9360619607099413,
            "mean": 1.0084367130822347,
            "standard_deviation": 0.11390967151210048,
            "upper_95_t": 1.080811465454528
          },
          "tail_fraction": {
            "lower_95_t": 0.012023412889690582,
            "mean": 0.012369791666666666,
            "standard_deviation": 0.0005451610045053968,
            "upper_95_t": 0.01271617044364275
          },
          "waiting_time_cv": {
            "lower_95_t": 0.9066908850508832,
            "mean": 0.9409594296984561,
            "standard_deviation": 0.05393481201736216,
            "upper_95_t": 0.975227974346029
          }
        },
        "F3_poisson_events": {
          "absolute_lag1_correlation": {
            "lower_95_t": -0.004725315636769461,
            "mean": -0.0019176279610509028,
            "standard_deviation": 0.004418982730393545,
            "upper_95_t": 0.0008900597146676553
          },
          "event_count_fano": {
            "lower_95_t": 0.6643050227222055,
            "mean": 0.8258700534575506,
            "standard_deviation": 0.2542850783687234,
            "upper_95_t": 0.9874350841928957
          },
          "excess_kurtosis": {
            "lower_95_t": 19.976208802082034,
            "mean": 20.541131998490588,
            "standard_deviation": 0.8891251938445172,
            "upper_95_t": 21.10605519489914
          },
          "history_rate_ratio": {
            "lower_95_t": 0.9093994209481081,
            "mean": 0.9688061785704272,
            "standard_deviation": 0.09349951501800076,
            "upper_95_t": 1.0282129361927461
          },
          "innovation_rms": {
            "lower_95_t": 0.0015654036559884339,
            "mean": 0.0015782992871590724,
            "standard_deviation": 2.0296264407682862e-05,
            "upper_95_t": 0.0015911949183297109
          },
          "one_step_variance_rate": {
            "lower_95_t": 2.450642829733185e-05,
            "mean": 2.491310188802083e-05,
            "standard_deviation": 6.400582193323246e-07,
            "upper_95_t": 2.531977547870981e-05
          },
          "one_unit_variance_rate": {
            "lower_95_t": 2.4321952654701717e-05,
            "mean": 2.4844511956861512e-05,
            "standard_deviation": 8.22449217489854e-07,
            "upper_95_t": 2.5367071259021307e-05
          },
          "signed_lag1_correlation": {
            "lower_95_t": -0.0061407094932403525,
            "mean": -0.0032431122981307057,
            "standard_deviation": 0.004560490141250959,
            "upper_95_t": -0.00034551510302105936
          },
          "state_rate_ratio": {
            "lower_95_t": 0.9478253025663278,
            "mean": 0.9887920604112957,
            "standard_deviation": 0.06447704173178635,
            "upper_95_t": 1.0297588182562638
          },
          "tail_fraction": {
            "lower_95_t": 0.04700752307454474,
            "mean": 0.04772395833333334,
            "standard_deviation": 0.001127588037448504,
            "upper_95_t": 0.04844039359212193
          },
          "waiting_time_cv": {
            "lower_95_t": 0.9690339850408911,
            "mean": 0.9868546564552999,
            "standard_deviation": 0.028047720515828562,
            "upper_95_t": 1.0046753278697087
          }
        },
        "F4_state_hawkes_events": {
          "absolute_lag1_correlation": {
            "lower_95_t": 0.16205300888740393,
            "mean": 0.17219350567032432,
            "standard_deviation": 0.015959994606546967,
            "upper_95_t": 0.18233400245324471
          },
          "event_count_fano": {
            "lower_95_t": 2.2381674170774515,
            "mean": 2.855713302002449,
            "standard_deviation": 0.971947351662169,
            "upper_95_t": 3.4732591869274465
          },
          "excess_kurtosis": {
            "lower_95_t": 25.70757270259635,
            "mean": 27.042378102265193,
            "standard_deviation": 2.100832674725152,
            "upper_95_t": 28.377183501934034
          },
          "history_rate_ratio": {
            "lower_95_t": 5.317156311229929,
            "mean": 5.5626958981703645,
            "standard_deviation": 0.3864515286729904,
            "upper_95_t": 5.8082354851108
          },
          "innovation_rms": {
            "lower_95_t": 0.0015375020314202705,
            "mean": 0.0015683397614184988,
            "standard_deviation": 4.8535097933153905e-05,
            "upper_95_t": 0.001599177491416727
          },
          "one_step_variance_rate": {
            "lower_95_t": 2.3632003061240914e-05,
            "mean": 2.461794478352864e-05,
            "standard_deviation": 1.5517607181321928e-06,
            "upper_95_t": 2.560388650581637e-05
          },
          "one_unit_variance_rate": {
            "lower_95_t": 2.326176856109481e-05,
            "mean": 2.4602500700088564e-05,
            "standard_deviation": 2.110160691851427e-06,
            "upper_95_t": 2.5943232839082317e-05
          },
          "signed_lag1_correlation": {
            "lower_95_t": -0.012842283743913559,
            "mean": 9.490085658127561e-05,
            "standard_deviation": 0.020361664804782444,
            "upper_95_t": 0.013032085457076108
          },
          "state_rate_ratio": {
            "lower_95_t": 9.192103979024619,
            "mean": 10.528937412334423,
            "standard_deviation": 2.104024570217508,
            "upper_95_t": 11.865770845644228
          },
          "tail_fraction": {
            "lower_95_t": 0.042361465659153205,
            "mean": 0.044039062500000004,
            "standard_deviation": 0.0026403476185674884,
            "upper_95_t": 0.0457166593408468
          },
          "waiting_time_cv": {
            "lower_95_t": 2.006799215074401,
            "mean": 2.063503017782392,
            "standard_deviation": 0.08924536980422054,
            "upper_95_t": 2.120206820490383
          }
        },
        "F5_colored_memory": {
          "absolute_lag1_correlation": {
            "lower_95_t": 0.6261984865172984,
            "mean": 0.6294514123749323,
            "standard_deviation": 0.005119737252989209,
            "upper_95_t": 0.6327043382325662
          },
          "event_count_fano": {
            "lower_95_t": 2.11172159958326,
            "mean": 2.5602700152189235,
            "standard_deviation": 0.7059644559404589,
            "upper_95_t": 3.008818430854587
          },
          "excess_kurtosis": {
            "lower_95_t": -0.04802265485803392,
            "mean": -0.013390089934370408,
            "standard_deviation": 0.05450773874545549,
            "upper_95_t": 0.021242474989293103
          },
          "history_rate_ratio": {
            "lower_95_t": 44.19743759933262,
            "mean": 47.47583431671927,
            "standard_deviation": 5.159825504381595,
            "upper_95_t": 50.75423103410592
          },
          "innovation_rms": {
            "lower_95_t": 0.0015737293226827421,
            "mean": 0.0015836578752982304,
            "standard_deviation": 1.5626418467081786e-05,
            "upper_95_t": 0.0015935864279137187
          },
          "one_step_variance_rate": {
            "lower_95_t": 2.4762946093517535e-05,
            "mean": 2.507741726066599e-05,
            "standard_deviation": 4.949420367705567e-07,
            "upper_95_t": 2.5391888427814448e-05
          },
          "one_unit_variance_rate": {
            "lower_95_t": 0.00014096250140055536,
            "mean": 0.00014363463961338912,
            "standard_deviation": 4.205643212333093e-06,
            "upper_95_t": 0.00014630677782622288
          },
          "signed_lag1_correlation": {
            "lower_95_t": 0.8167185666459948,
            "mean": 0.8189628069525434,
            "standard_deviation": 0.0035321803216425873,
            "upper_95_t": 0.821207047259092
          },
          "state_rate_ratio": {
            "lower_95_t": 1.0045054633845405,
            "mean": 1.1019376996062606,
            "standard_deviation": 0.1533473160034499,
            "upper_95_t": 1.1993699358279808
          },
          "tail_fraction": {
            "lower_95_t": 0.011657292332125015,
            "mean": 0.012226562499999998,
            "standard_deviation": 0.0008959668351017644,
            "upper_95_t": 0.012795832667874981
          },
          "waiting_time_cv": {
            "lower_95_t": 1.626215129969153,
            "mean": 1.6846123463298948,
            "standard_deviation": 0.09191061129515773,
            "upper_95_t": 1.7430095626906366
          }
        }
      }
    },
    "0.20": {
      "classification_counts": {
        "original": {
          "F1_initial_only": {
            "F1_initial_only": 12,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 0
          },
          "F2_gaussian_white": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 12,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 0
          },
          "F3_poisson_events": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 11,
            "F4_state_hawkes_events": 1,
            "F5_colored_memory": 0
          },
          "F4_state_hawkes_events": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 12,
            "F5_colored_memory": 0
          },
          "F5_colored_memory": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 12
          }
        },
        "revised": {
          "F1_initial_only": {
            "F1_initial_only": 12,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 0
          },
          "F2_gaussian_white": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 12,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 0
          },
          "F3_poisson_events": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 12,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 0
          },
          "F4_state_hawkes_events": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 12,
            "F5_colored_memory": 0
          },
          "F5_colored_memory": {
            "F1_initial_only": 0,
            "F2_gaussian_white": 0,
            "F3_poisson_events": 0,
            "F4_state_hawkes_events": 0,
            "F5_colored_memory": 12
          }
        }
      },
      "summaries": {
        "F1_initial_only": {
          "absolute_lag1_correlation": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "event_count_fano": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "excess_kurtosis": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "history_rate_ratio": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "innovation_rms": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "one_step_variance_rate": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "one_unit_variance_rate": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "signed_lag1_correlation": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "state_rate_ratio": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "tail_fraction": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          },
          "waiting_time_cv": {
            "lower_95_t": 0.0,
            "mean": 0.0,
            "standard_deviation": 0.0,
            "upper_95_t": 0.0
          }
        },
        "F2_gaussian_white": {
          "absolute_lag1_correlation": {
            "lower_95_t": -0.003943029417941897,
            "mean": 0.0007846746348429967,
            "standard_deviation": 0.007440871270812315,
            "upper_95_t": 0.0055123786876278905
          },
          "event_count_fano": {
            "lower_95_t": 0.8411810577170579,
            "mean": 0.9752444842046247,
            "standard_deviation": 0.21100066490633668,
            "upper_95_t": 1.1093079106921917
          },
          "excess_kurtosis": {
            "lower_95_t": -0.023526610730082862,
            "mean": -0.005837020448963726,
            "standard_deviation": 0.02784141364298908,
            "upper_95_t": 0.01185256983215541
          },
          "history_rate_ratio": {
            "lower_95_t": 0.9168523386408511,
            "mean": 1.280498794293349,
            "standard_deviation": 0.5723383770190721,
            "upper_95_t": 1.6441452499458469
          },
          "innovation_rms": {
            "lower_95_t": 0.002224620529116067,
            "mean": 0.0022336168757106345,
            "standard_deviation": 1.4159231663063728e-05,
            "upper_95_t": 0.002242613222305202
          },
          "one_step_variance_rate": {
            "lower_95_t": 2.4744728509226566e-05,
            "mean": 2.4944685421134225e-05,
            "standard_deviation": 3.1470955554792266e-07,
            "upper_95_t": 2.5144642333041884e-05
          },
          "one_unit_variance_rate": {
            "lower_95_t": 2.5002826411552155e-05,
            "mean": 2.5340232397213278e-05,
            "standard_deviation": 5.31038846187308e-07,
            "upper_95_t": 2.56776383828744e-05
          },
          "signed_lag1_correlation": {
            "lower_95_t": -0.00011612289540557062,
            "mean": 0.005085508541737701,
            "standard_deviation": 0.008186779352060802,
            "upper_95_t": 0.010287139978880972
          },
          "state_rate_ratio": {
            "lower_95_t": 0.9584338693883774,
            "mean": 1.0820080618320047,
            "standard_deviation": 0.19449179730824737,
            "upper_95_t": 1.205582254275632
          },
          "tail_fraction": {
            "lower_95_t": 0.01170995845647709,
            "mean": 0.012223958333333333,
            "standard_deviation": 0.0008089776505041111,
            "upper_95_t": 0.012737958210189576
          },
          "waiting_time_cv": {
            "lower_95_t": 0.7992434410398234,
            "mean": 0.8413346514127115,
            "standard_deviation": 0.06624680278640745,
            "upper_95_t": 0.8834258617855996
          }
        },
        "F3_poisson_events": {
          "absolute_lag1_correlation": {
            "lower_95_t": -0.0053067144018958765,
            "mean": 0.0002874169093614297,
            "standard_deviation": 0.00880452974516593,
            "upper_95_t": 0.005881548220618735
          },
          "event_count_fano": {
            "lower_95_t": 0.7837539656706936,
            "mean": 0.9447798204031876,
            "standard_deviation": 0.25343647634441474,
            "upper_95_t": 1.1058056751356817
          },
          "excess_kurtosis": {
            "lower_95_t": 9.819284208205142,
            "mean": 10.185147070524236,
            "standard_deviation": 0.57582675034062,
            "upper_95_t": 10.55100993284333
          },
          "history_rate_ratio": {
            "lower_95_t": 0.9516641350351708,
            "mean": 1.0133579692966983,
            "standard_deviation": 0.09709911488060378,
            "upper_95_t": 1.0750518035582257
          },
          "innovation_rms": {
            "lower_95_t": 0.0022020288245356186,
            "mean": 0.002220180126017066,
            "standard_deviation": 2.8568094832754295e-05,
            "upper_95_t": 0.0022383314274985137
          },
          "one_step_variance_rate": {
            "lower_95_t": 2.424578383927529e-05,
            "mean": 2.4647682047526028e-05,
            "standard_deviation": 6.325423076772981e-07,
            "upper_95_t": 2.5049580255776767e-05
          },
          "one_unit_variance_rate": {
            "lower_95_t": 2.413236105825106e-05,
            "mean": 2.469143881225904e-05,
            "standard_deviation": 8.799251288789471e-07,
            "upper_95_t": 2.525051656626702e-05
          },
          "signed_lag1_correlation": {
            "lower_95_t": -0.006136149256059982,
            "mean": -0.000498879859862236,
            "standard_deviation": 0.008872424210074769,
            "upper_95_t": 0.00513838953633551
          },
          "state_rate_ratio": {
            "lower_95_t": 0.9331479069990084,
            "mean": 0.9755005336496035,
            "standard_deviation": 0.06665824243000514,
            "upper_95_t": 1.0178531603001986
          },
          "tail_fraction": {
            "lower_95_t": 0.09038229687813899,
            "mean": 0.09164583333333333,
            "standard_deviation": 0.0019886634197293653,
            "upper_95_t": 0.09290936978852767
          },
          "waiting_time_cv": {
            "lower_95_t": 0.9316987924463216,
            "mean": 0.9482829211338362,
            "standard_deviation": 0.026101542170282745,
            "upper_95_t": 0.9648670498213507
          }
        },
        "F4_state_hawkes_events": {
          "absolute_lag1_correlation": {
            "lower_95_t": 0.2363782406865469,
            "mean": 0.25333665236328606,
            "standard_deviation": 0.026690621247691268,
            "upper_95_t": 0.27029506404002523
          },
          "event_count_fano": {
            "lower_95_t": 1.788858946767896,
            "mean": 2.3249576492979087,
            "standard_deviation": 0.843758701779472,
            "upper_95_t": 2.8610563518279215
          },
          "excess_kurtosis": {
            "lower_95_t": 16.1231336515353,
            "mean": 17.121285636453067,
            "standard_deviation": 1.5709782900018634,
            "upper_95_t": 18.11943762137083
          },
          "history_rate_ratio": {
            "lower_95_t": 4.716152707620733,
            "mean": 4.937323492652244,
            "standard_deviation": 0.3480977916362079,
            "upper_95_t": 5.158494277683754
          },
          "innovation_rms": {
            "lower_95_t": 0.0021409080418723293,
            "mean": 0.0022092532005776604,
            "standard_deviation": 0.00010756754700202527,
            "upper_95_t": 0.0022775983592829914
          },
          "one_step_variance_rate": {
            "lower_95_t": 2.2946714031479797e-05,
            "mean": 2.4455719807942698e-05,
            "standard_deviation": 2.3750043581849205e-06,
            "upper_95_t": 2.59647255844056e-05
          },
          "one_unit_variance_rate": {
            "lower_95_t": 2.2651928973225636e-05,
            "mean": 2.4674330601359796e-05,
            "standard_deviation": 3.1830313413892992e-06,
            "upper_95_t": 2.6696732229493957e-05
          },
          "signed_lag1_correlation": {
            "lower_95_t": -0.009029187799059304,
            "mean": 0.0012555429783943815,
            "standard_deviation": 0.016187002594825122,
            "upper_95_t": 0.011540273755848067
          },
          "state_rate_ratio": {
            "lower_95_t": 7.35181435248869,
            "mean": 9.535256372235995,
            "standard_deviation": 3.436490697139108,
            "upper_95_t": 11.7186983919833
          },
          "tail_fraction": {
            "lower_95_t": 0.07591041976358565,
            "mean": 0.07967708333333333,
            "standard_deviation": 0.005928302285850835,
            "upper_95_t": 0.08344374690308101
          },
          "waiting_time_cv": {
            "lower_95_t": 1.8965791410199624,
            "mean": 1.946879394967498,
            "standard_deviation": 0.07916690857421804,
            "upper_95_t": 1.9971796489150337
          }
        },
        "F5_colored_memory": {
          "absolute_lag1_correlation": {
            "lower_95_t": 0.4043191174345639,
            "mean": 0.4094527210068353,
            "standard_deviation": 0.008079711189652889,
            "upper_95_t": 0.41458632457910666
          },
          "event_count_fano": {
            "lower_95_t": 1.0577979025571913,
            "mean": 1.257846206762142,
            "standard_deviation": 0.31485339668342976,
            "upper_95_t": 1.4578945109670929
          },
          "excess_kurtosis": {
            "lower_95_t": -0.018012427887076434,
            "mean": 0.019144884066087425,
            "standard_deviation": 0.058481404911553944,
            "upper_95_t": 0.05630219601925128
          },
          "history_rate_ratio": {
            "lower_95_t": 18.668366924885415,
            "mean": 20.458413339322465,
            "standard_deviation": 2.8173305244771583,
            "upper_95_t": 22.248459753759516
          },
          "innovation_rms": {
            "lower_95_t": 0.0031398134053078727,
            "mean": 0.003153453447330935,
            "standard_deviation": 2.1467882864260648e-05,
            "upper_95_t": 0.003167093489353997
          },
          "one_step_variance_rate": {
            "lower_95_t": 4.928823966765595e-05,
            "mean": 4.9716730994153205e-05,
            "standard_deviation": 6.743968669628526e-07,
            "upper_95_t": 5.0145222320650464e-05
          },
          "one_unit_variance_rate": {
            "lower_95_t": 0.00014344402108157171,
            "mean": 0.00014541493564683628,
            "standard_deviation": 3.1019965298513195e-06,
            "upper_95_t": 0.00014738585021210085
          },
          "signed_lag1_correlation": {
            "lower_95_t": 0.665127829462874,
            "mean": 0.6683238060309097,
            "standard_deviation": 0.005030105514595004,
            "upper_95_t": 0.6715197825989454
          },
          "state_rate_ratio": {
            "lower_95_t": 0.8429314107915641,
            "mean": 0.9773233298339846,
            "standard_deviation": 0.21151767502092844,
            "upper_95_t": 1.111715248876405
          },
          "tail_fraction": {
            "lower_95_t": 0.011893382627475798,
            "mean": 0.012588541666666668,
            "standard_deviation": 0.0010941016750644285,
            "upper_95_t": 0.013283700705857538
          },
          "waiting_time_cv": {
            "lower_95_t": 1.2333123316640138,
            "mean": 1.2724446811888594,
            "standard_deviation": 0.0615898905870151,
            "upper_95_t": 1.3115770307137051
          }
        }
      }
    }
  },
  "pre_registered_pair_checks": [
    {
      "intervals_overlap": false,
      "left": "F1_initial_only",
      "left_interval": {
        "lower_95_t": 0.0,
        "mean": 0.0,
        "standard_deviation": 0.0,
        "upper_95_t": 0.0
      },
      "pre_registered_metric": "innovation_rms",
      "right": "F2_gaussian_white",
      "right_interval": {
        "lower_95_t": 0.0015789417989476218,
        "mean": 0.0015810773663915854,
        "standard_deviation": 4.0077278834265796e-06,
        "upper_95_t": 0.0015832129338355491
      }
    },
    {
      "intervals_overlap": false,
      "left": "F2_gaussian_white",
      "left_interval": {
        "lower_95_t": -0.006001158487488359,
        "mean": 0.0016832691444405579,
        "standard_deviation": 0.014421035952624275,
        "upper_95_t": 0.009367696776369474
      },
      "pre_registered_metric": "excess_kurtosis",
      "right": "F3_poisson_events",
      "right_interval": {
        "lower_95_t": 19.4617330403842,
        "mean": 19.766507271374188,
        "standard_deviation": 0.571956735499478,
        "upper_95_t": 20.071281502364176
      }
    },
    {
      "intervals_overlap": false,
      "left": "F2_gaussian_white",
      "left_interval": {
        "lower_95_t": -0.003359656822413814,
        "mean": -0.0016192347429133194,
        "standard_deviation": 0.0032661755153932733,
        "upper_95_t": 0.00012118733658717548
      },
      "pre_registered_metric": "signed_lag1_correlation",
      "right": "F5_colored_memory",
      "right_interval": {
        "lower_95_t": 0.8185227491198667,
        "mean": 0.8199360115863727,
        "standard_deviation": 0.002652209093009847,
        "upper_95_t": 0.8213492740528788
      }
    },
    {
      "intervals_overlap": false,
      "left": "F3_poisson_events",
      "left_interval": {
        "lower_95_t": 1.006051221147317,
        "mean": 1.0337807370600158,
        "standard_deviation": 0.05203879391932281,
        "upper_95_t": 1.0615102529727147
      },
      "pre_registered_metric": "state_rate_ratio",
      "right": "F4_state_hawkes_events",
      "right_interval": {
        "lower_95_t": 7.985086510131881,
        "mean": 8.802041365348774,
        "standard_deviation": 1.5331441589484365,
        "upper_95_t": 9.618996220565668
      }
    }
  ],
  "recorded_protocol_revision": {
    "audit_seed_family": "2026208000 plus fixed candidate and dt offsets",
    "change": "Fano factor remains a supporting metric but cannot alone select F4; state-rate or event-history dependence must exceed 1.5.",
    "failure": "The original OR rule allowed a noisy Fano estimate from only 25 windows to misclassify independent Poisson runs as F4.",
    "revised_decision_tree": [
      "innovation_rms < 1e-15 -> F1_initial_only",
      "signed_lag1_correlation > 0.3 -> F5_colored_memory",
      "excess_kurtosis < 2.0 -> F2_gaussian_white",
      "state_rate_ratio > 1.5 OR history_rate_ratio > 1.5 -> F4_state_hawkes_events",
      "otherwise -> F3_poisson_events"
    ]
  },
  "schema": "lineum.foam-signature-protocol.v1"
}
```
