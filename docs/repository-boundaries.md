# Repository Boundaries

Lineum separates its reusable public physics from private commercial products.

## Lineum Core

`lineum-core` is the public, open-source source of truth for:

- the reusable Lineum physics library;
- canonical equations and general numerical mechanisms;
- scientific verification, reference packs, and whitepapers;
- Simulacrum, the public research and visualization environment.

Core must remain application-neutral. It must not import, test, deploy, or require private product code.

## Public Library Promotion Gate

The installable `lineum_core/` package is a public library surface, not the default location for research code.

A new module, class, function, schema, or conceptual name may enter `lineum_core/` only when all of the following are true:

- it implements established Core behavior, fixes a verified defect, or provides genuinely general infrastructure required by more than one validated use case;
- its semantics are application-neutral and do not encode an unvalidated scientific interpretation, ontology, experimental decomposition, or product-specific concept;
- a durable research or engineering record states why the capability belongs in the public package rather than only in a report, test harness, or research runner;
- the public API, compatibility impact, failure behavior, and maintenance burden have been reviewed explicitly;
- regression tests pass in a repository-supported dependency environment;
- any decision-relevant scientific premise has passed the required validation and promotion gates before being represented as library architecture.

Technical reusability by itself is not evidence that code belongs in the library. A helper written for one experiment remains experiment code even when it could theoretically be imported elsewhere.

Research hypotheses, provisional decompositions, experimental initializers, one-off causal lanes, exploratory metrics, and interpretation-bearing adapters must remain outside `lineum_core/`. Disposable work belongs in `.scratch/`. Retained experiment logic belongs in the standalone report and, only when a separately executable tool is justified, in a clearly research-scoped path outside the installable package. Tests may verify an experiment, but passing tests do not promote that experiment into the library.

When classification is uncertain, the mandatory default is to keep the code outside `lineum_core/`. Adding a new interpretation-bearing public module requires an explicit promotion decision after the project owner receives a lay explanation of what would become permanent API.

If experiment-specific code is accidentally committed under `lineum_core/`, stop building on that placement. Preserve the scientific history, then remove or relocate the module in the next coherent checkpoint unless it independently passes this promotion gate.

## Lineum Dynamics

`lineum-dynamics` is the private company repository for:

- commercial applications and hosted services;
- the Portal and commercial API layer;
- company operations, integrations, deployment, and monetization logic;
- proprietary product behavior and non-public know-how.

Dynamics consumes a released or explicitly pinned version of the Core library.

## Dependency Direction

The allowed dependency direction is:

```text
Dynamics -> Core
```

The reverse dependency is forbidden. A local sibling checkout, directory junction, or generated copy must never be required to test or package Core. Generated presentation copies may exist inside Dynamics only when their source and synchronization mechanism are explicit; they are never a second source of truth.

Lina EI and future Lineum applications follow the same rule: they depend on the public Core contract while keeping identity, cognition, embodiment, devices, and product policy outside Core.
