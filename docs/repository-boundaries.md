# Repository Boundaries

Lineum separates its reusable public physics from private commercial products.

## Lineum Core

`lineum-core` is the public, open-source source of truth for:

- the reusable Lineum physics library;
- canonical equations and general numerical mechanisms;
- scientific verification, reference packs, and whitepapers;
- Simulacrum, the public research and visualization environment.

Core must remain application-neutral. It must not import, test, deploy, or require private product code.

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
