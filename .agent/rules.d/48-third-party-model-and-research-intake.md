# Third-Party Model and Research Intake Gate

## Status and scope

This file is a binding supplement to `.agent/rules.md`.

Apply this gate before any Lineum analysis, experiment, implementation, publication, dependency addition, dataset use, model comparison, clean-room reconstruction, or repository transfer that involves material created by another person, project, company, research group, model provider, or rights holder.

The gate applies to source code, binaries, packages, model weights, prompts, equations as expressed in documents, datasets, images, diagrams, papers, whitepapers, repositories, issue discussions, private messages, attachments, unpublished files, generated outputs, and technical descriptions supplied through chat or any connected service.

Access to material is not evidence of permission to copy, modify, redistribute, publish, train on, derive from, or incorporate it. User possession, upload, invitation, collaboration, or conversational disclosure does not replace a license or an explicit rights grant.

## Mandatory pre-research intake record

Before substantive research begins, record the following in the active standalone report or, when no research report yet exists, in a dedicated version-controlled provenance record:

1. exact project, model, dataset, document, package, or artifact name;
2. rights holder or source organization when known;
3. public URL or connector source, repository and path, version, tag, branch, commit, release, or document date;
4. retrieval date and cryptographic hash for retained files when technically possible;
5. declared license, SPDX identifier when available, file-level notices, repository-level notices, terms of service, dataset terms, model-card terms, and any conflicting or missing terms;
6. whether the material is public, private, confidential, unpublished, access-controlled, all-rights-reserved, or of unknown status;
7. the exact permitted research mode: public factual audit, black-box behavioural comparison, dependency use, quotation, reproduction, redistribution, adaptation, clean-room specification, implementation, or no use;
8. what information will be used and what information is explicitly excluded;
9. the target repository and whether the result is public Core, private Dynamics, OEA, or Lina EI work;
10. the unresolved legal, licensing, confidentiality, attribution, patent, trademark, or provenance risks.

No technical experiment may silently outrun the permitted research mode recorded at intake.

## License classification and hard stops

Classify every material input and dependency before use.

### Permissive or public-domain material

MIT, BSD-family, ISC, Apache-2.0, CC0, Unlicense, and similarly permissive terms may be considered for use only after checking the exact version, attribution and notice requirements, patent clauses, file-level exceptions, and target-repository compatibility.

### Copyleft material

AGPL, GPL, LGPL, EUPL, MPL, OSL, and other reciprocal licenses require an explicit compatibility review before any copying, linking, modification, distribution, hosted-service use, vendoring, or derivative implementation. Strong or network copyleft is not automatically prohibited, but it is a mandatory human-review gate for private repositories, mixed-license products, hosted services, and any work whose source-disclosure obligations are uncertain.

The intentional AGPL license of public `lineum-core` is not evidence that third-party AGPL or GPL material may be copied into Lineum, transferred into private repositories, or treated as Lineum-owned code. The origin, compatibility, notice duties, corresponding-source duties, and derivative-work boundary must still be reviewed independently.

### Source-available, non-commercial, custom, or restricted material

SSPL, Business Source License, Commons Clause, Elastic License, PolyForm, CC-BY-NC, CC-BY-ND, research-only terms, non-commercial terms, field-of-use restrictions, custom licenses, API terms, model licenses, and dataset-specific restrictions require explicit human review before research can move beyond isolated reading or black-box comparison.

### Missing, conflicting, or all-rights-reserved terms

Unknown license, no license, conflicting repository and file notices, all-rights-reserved material, leaked material, or material whose redistribution authority is unclear is a hard stop for copying, adaptation, dependency addition, publication, repository storage, or implementation derived from protected technical details.

At this stop, the agent may preserve only the minimum provenance needed to describe the uncertainty. It must not infer permission from availability, collaboration, an attachment, or the absence of a copyright warning.

## Confidential and unpublished information boundary

Private messages, calls, attachments, shared drafts, unreleased repositories, unpublished model files, and access-controlled technical descriptions are confidential by default unless the rights holder clearly authorizes another treatment.

Confidential information may be used only for the explicitly authorized private purpose. It must not be:

- quoted or closely paraphrased in a public report;
- converted into public implementation details, equations, architecture, tests, prompts, diagrams, or documentation;
- used to fill gaps in a public reconstruction;
- presented as public evidence;
- moved from a private repository into public Core;
- exposed through commit messages, issue text, filenames, hashes, screenshots, logs, or generated artifacts.

Confidential communication may justify a conservative scope limitation such as stating that later unavailable versions were not assessed. The public wording must not reveal the existence, names, participants, contents, or technical claims of confidential work unless publication permission is explicit and recorded.

## Clean-room and independent reconstruction requirements

When a third-party mechanism is scientifically relevant but direct reuse is not clearly permitted, use a clean-room-style boundary:

1. derive the research question only from lawful public facts, observable behaviour, published interfaces, and independently citable material;
2. write an original, implementation-neutral specification that records all public sources;
3. exclude confidential and license-restricted implementation details from the specification;
4. implement independently without line-by-line translation, structural copying, copied identifiers, copied tests, copied constants without public provenance, or imitation of distinctive non-public architecture;
5. compare outputs and declared observables, not source-code resemblance;
6. record which facts were independently derived and which remain unavailable;
7. retain a null control and at least one conventional alternative so that the reconstruction is a scientific test rather than disguised duplication.

A clean-room label is not a legal conclusion. If the derivative-work boundary remains uncertain, stop incorporation and request human or legal review.

## Dataset, model, and generated-output controls

Before using third-party data, model weights, corpora, images, or generated outputs:

- verify download, storage, redistribution, modification, publication, and commercial-use rights separately;
- distinguish raw data from derived statistics and from copyrighted expression;
- do not commit restricted raw material merely because a processing script can read it;
- use runtime download into `.scratch/` only when the terms allow the download and processing but not repository redistribution;
- record provenance, checksum, version, filtering, transformations, and deletion requirements;
- verify whether generated outputs carry source, training-data, personality, likeness, trademark, or attribution restrictions;
- never assume that a model provider's output terms grant rights to embedded third-party material.

## Dependency and transitive-license audit

Before adding or updating any package, tool, container, model runtime, dataset client, or vendored component:

1. inspect the direct package license and exact version;
2. inspect lock files and transitive dependencies when the component will be distributed, bundled, deployed, or used in a hosted product;
3. inspect bundled assets, fonts, examples, codecs, native binaries, model files, and optional extras separately;
4. record attribution, notice, source-offer, relinking, patent, trademark, and network-use obligations;
5. reject package-name or registry metadata as the sole evidence when repository or file notices conflict;
6. require explicit human review for copyleft, source-available, custom, unknown, or mixed-license results;
7. preserve the audit receipt in version control before the dependency informs a consequential implementation decision.

## Pre-commit and pre-publication contamination scan

Before every commit or publication involving third-party research, inspect the exact diff for:

- copied or translated source code;
- distinctive identifiers, comments, tests, constants, equations as expressed, diagrams, screenshots, prose, prompts, and file structure;
- foreign copyright or license headers;
- new or changed `LICENSE`, `NOTICE`, manifest, lock, container, model, dataset, or asset files;
- vendored dependencies and generated bundles;
- confidential names, quotes, technical details, filenames, hashes, links, or collaboration metadata;
- wording that implies audit of a version that was not actually available;
- claims that a private message or inaccessible artifact is public evidence;
- transfers across the Core, Dynamics, OEA, and Lina EI repository boundaries.

The commit must state the audited third-party scope and any remaining limitation. A public report must identify the exact public historical version or evidence cutoff without revealing confidential successor work.

## Contamination incident protocol

If potentially unauthorized third-party material is discovered:

1. stop further propagation, publication, testing, adaptation, and cross-repository copying;
2. identify affected files, commits, branches, releases, artifacts, deployments, and downstream repositories;
3. preserve factual provenance and the discovery timeline without repeating the protected material more than necessary;
4. classify whether the issue is a dependency obligation, missing notice, incompatible license, confidential disclosure, copied expression, uncertain derivative work, dataset restriction, or unknown origin;
5. do not rewrite shared history, delete evidence, or force-push without explicit owner approval and legal-risk review;
6. prepare the smallest reversible containment plan, including isolation, replacement, attribution, source offer, relicensing request, or removal as applicable;
7. re-audit downstream outputs before research resumes.

## Third-party comparison reporting rule

A Lineum report that evaluates another project must distinguish:

- the exact public artifact actually inspected;
- claims reproduced from public evidence;
- black-box observations made by Lineum;
- Lineum's independent interpretation;
- confidential context used only to narrow scope;
- later, private, inaccessible, or differently licensed versions that were not audited.

Do not shorten a model name in a way that creates a false separate entity. Do not call an audit complete when only a historical public version was available. Preserve negative results, but bind every conclusion to the exact tested version and evidence cutoff.

## Completion gate

Third-party research may proceed only after the intake record is complete enough to answer all of these questions:

- What exact material are we using?
- Who supplied or published it?
- Under what terms?
- What may we inspect, quote, store, modify, implement, redistribute, and publish?
- What must remain confidential or excluded?
- Which repository may contain the result?
- How will an independent reviewer reproduce the public evidence without receiving restricted material?

If any answer is unknown and could change the legality, confidentiality, repository boundary, or scientific independence of the work, the permitted action is the narrowest non-incorporating audit or a hard stop pending explicit human or legal review.