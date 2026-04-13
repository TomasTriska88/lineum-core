---
description: How to manage git branches and commits
---

# Git Policy (STRICT)

**# Git Policy (STRICT)

**CRITICAL RULE 1:** NEVER WORK DIRECTLY ON `main`.
**CRITICAL RULE 2 (NO AUTO-PUSH):** The AI Agent is strictly FORBIDDEN from ever executing `git push` automatically on its own initiative. However, if the human user EXPLICITLY commands a push (e.g., "push prosím", "push please"), the agent MUST execute the `git push` command immediately.
**CRITICAL RULE 3 (PULL REQUESTS):** NEVER run interactive GitHub CLI commands like `gh pr create` directly, as they hang waiting for GUI/Terminal input. To create a pull request, either output the direct `https://github.com/[repo]/compare/main...dev?expand=1` URL for the user to click, or explicitly use `gh` with strict non-interactive flags (e.g., `--fill`) if you are absolutely certain it won't prompt.

1.  **BEFORE YOU WRITE ANY CODE:** Check the current branch:
    ```bash
    git branch
    ```
2.  **Switch to DEV:** If you are on `main`, STOP. Switch to `dev` immediately:
    ```bash
    git checkout dev
    ```
    (Create it if it doesn't exist: `git checkout -b dev`)

3.  **Commit Only:** Only when you are safely on `dev` (or a feature branch), you may proceed with `git add` and `git commit`. Do NOT push!
4.  **Watcher Sync Delay:** ALWAYS wait 2 seconds before running `git add` to allow the Svelte/Vite dev server watcher to sync generated.
5.  **NEVER blindly `git add .`:** Because `.agent/scratch`, temporary test JSONs, and local generated artifacts can bleed into the working directory, NEVER use `git add .` unless you have meticulously verified `git status`. Preferred method is exact file staging: `git add src/file.py whitepapers/doc.md` or `git add -u` to stage only tracked modifications.
    ```bash
    Start-Sleep -Seconds 2
    git add <specific file paths>
    git commit -m "..."
    # STOP HERE. DO NOT PUSH.
    ```

**Correction Protocol:**
If you accidentally commit to `main` locally:
1.  `git reset --soft HEAD~1` (undo commit, keep changes)
2.  `git checkout dev`
3.  `git commit`
4.  Inform the user the correction is strictly committed locally.

// turbo
5.  Check status to confirm everything is clean on dev.
