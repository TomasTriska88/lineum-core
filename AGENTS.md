# Codex Repository Router

Project-wide implementation rules live in `.agent/rules.md`.

Before any analysis, proposal, test, edit, commit, publication, or external operation for this repository, read `.agent/rules.md` in full and enumerate and read every Markdown file under `.agent/rules.d/` in lexical filename order. Treat every `.agent/rules.d/*.md` file as a binding supplement to `.agent/rules.md`, not as optional documentation. Re-fetch these files after changing branches and whenever the repository state may have changed. If a tool cannot enumerate the directory reliably, do not assume that an omitted supplement is absent; resolve the repository tree or fetch known supplements directly before proceeding.

## Model and Execution Routing

Before deciding whether Lineum work should remain in ChatGPT or be proposed for execution in Codex, read and follow `.agent/workflows/model-tool-routing.md` in full. It is the binding source of truth for choosing ChatGPT Sol Pro or Extra High for scientific judgment, Codex Max for repository-local execution, and Codex Ultra only for safely parallelizable lanes. When proposing Codex to the project owner, provide the smallest exact copyable execution brief required by that workflow rather than a vague tool recommendation.

## Public Reply and Message Drafting

Before drafting, rewriting, or substantially editing any public post, comment, discussion reply, email, direct message, quoted message, or screenshot/image response on the user's behalf about Lineum or a relevant scientific, mathematical, cosmological, ontological, emergent-intelligence, or technical claim, read and follow `../lineum-dynamics/.agent/workflows/communication.md` in full.

This routing rule activates from the user's intent and the supplied subject even when Lineum or the communication protocol is not named. The referenced workflow is the single source of truth for mode selection, tone, mandatory cross-repository research, evidence hierarchy, and public-draft restrictions. Do not duplicate its rule body here.