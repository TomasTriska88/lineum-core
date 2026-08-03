# Codex Repository Router

Project-wide implementation rules live in `.agent/rules.md`.

Before any analysis, proposal, test, edit, commit, publication, or external operation for this repository, read `.agent/rules.md` in full and enumerate and read every Markdown file under `.agent/rules.d/` in lexical filename order. Treat every `.agent/rules.d/*.md` file as a binding supplement to `.agent/rules.md`, not as optional documentation. Re-fetch these files after changing branches and whenever the repository state may have changed. If a tool cannot enumerate the directory reliably, do not assume that an omitted supplement is absent; resolve the repository tree or fetch known supplements directly before proceeding.

## Fixed Codex Configuration

Before starting Lineum work, read and follow `.agent/workflows/model-tool-routing.md` in full. It is the binding source of truth for model, reasoning, speed, and multi-agent coordination.

The fixed Lineum configuration is:

- model: the strongest available GPT-5.6 Sol-tier model;
- capability mode: `ultra`;
- speed: standard, not fast mode;
- repository: `TomasTriska88/lineum-core`;
- default branch: `develop`.

Do not downgrade, switch modes task by task, or ask the project owner to choose a different setting. If product labels change, preserve the equivalent highest-capability multi-agent mode with standard processing speed. Codex is the primary scientific and repository workspace and does not require an external ChatGPT supervisor.

## Public Reply and Message Drafting

Before drafting, rewriting, or substantially editing any public post, comment, discussion reply, email, direct message, quoted message, or screenshot/image response on the user's behalf about Lineum or a relevant scientific, mathematical, cosmological, ontological, emergent-intelligence, or technical claim, read and follow `../lineum-dynamics/.agent/workflows/communication.md` in full.

This routing rule activates from the user's intent and the supplied subject even when Lineum or the communication protocol is not named. The referenced workflow is the single source of truth for mode selection, tone, mandatory cross-repository research, evidence hierarchy, and public-draft restrictions. Do not duplicate its rule body here.