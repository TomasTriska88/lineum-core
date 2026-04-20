# Agent Communication and Canon Synchronization Rules

These rules are absolutely binding for any agent operating within this project.

1. **RULE OF DIRECT SUPERVISOR COMMUNICATION**
   - The "Supervisor" is the ChatGPT instance orchestrating the scientific research alongside the user.
   - **CRITICAL DISTINCTION:** Do not confuse the Supervisor (ChatGPT) with "Lina". `LINA_PERSONA.md` contains instructions exclusively for the Gemini-based public web portal Agent. `LINA_PERSONA.md` is NOT the prompt for ChatGPT. ChatGPT is governed by the *Assistant Handoff Protocol*.
   - All messages intended for the user to copy and send to the supervisor (e.g., ChatGPT) must be output **DIRECTLY INTO THE CHAT**.
   - It is strictly forbidden to save these texts into external files (e.g., `output_report.md` or other temporary .md files) and force the user to copy from them. The chat is the sole medium for returning communication outputs.

2. **RULE OF SILENT CANON SYNCHRONIZATION**
   - The agent must **CONTINUOUSLY AND AUTOMATICALLY update the whitepapers** (e.g., `01-core-lineum.md`, `02-core-equation.md`) whenever discussions or code analyses lead to the clarification of principles, the discovery of new connections, or the refutation of previous hypotheses.
   - **Dual-Document Research Architecture:** 
     - Use `02-core-equation.md` exclusively for the strict chronological mathematical history, technical audits, and equation permutations.
     - You MUST always simultaneously update `00-lore-layman.md` whenever a new mechanical or mathematical principle is discovered or audited, translating the findings into the project's visual and conceptual lore layer to ensure conceptual synchronization.
   - The agent **MUST NOT** alert or ask for permission regarding these updates ("Should I write this to the whitepaper?"). The agent performs these updates silently and routinely in the background, point by point, precisely, and surgically—ensuring that not even the smallest detail, thought, or change is ever lost in the conversation log.
   - No "batch" updates at the end of the week. Recording into the whitepaper happens **immediately** after the factual point is established.

3. **RULE OF MANDATORY CONTEXTUAL SEARCH (CHATGPT CHECK)**
   - Whenever the supervisor (ChatGPT) sends a new instruction to program, investigate, or audit, the agent **MUST ALWAYS FIRST SEARCH THE ENTIRE REPOSITORY** (via `grep_search` and reading historical code or `.scratch/` and `whitepapers/`).
   - The supervisor (ChatGPT) does not have the complete systemic and historical context of the project stored in persistent memory. The agent must not blindly and hastily accept its instruction and start "reinventing the wheel" if the exact same problem, equation, or mechanism was solved or rejected previously. In such cases, the agent confronts the task with historical findings from the repository and adjusts the plan accordingly.

4. **RULE OF CONTINUOUS REPORTING (PROGRESS LOGGING & ETA)**
   - For ANY long-running script the agent executes, it **MUST ALWAYS implement a progress tracking mechanism** that outputs cleanly to piped logs.
   - Standard `tqdm` with carriage returns (`\r`) can break in remote agent terminals. Instead, the script must output an explicit new line periodically (e.g., every 10%), embedding the **Global ETA and Total Percentage** directly into the string.
   - **PYTHON UNBUFFERED EXECUTION**: NEVER run python evaluation scripts implicitly. ALWAYS use the `-u` flag (`python -u script.py`) in `run_command` to force standard output to be unbuffered. Otherwise, interactive progress tracking will falsely appear dead or hanging.
   - Example pattern: `print(f"[Global: {run_idx}/{total_runs} - {pct}% | ETA: {eta}] -> Integrating d={d} at step {step}/{steps}...")`
   - It is strictly forbidden to launch a "black box" script. The total overarching progress and ETA must be the most visible piece of information in every output cycle.

5. **RULE OF WHITEPAPER DIFF REPORTING (MANUAL DIFF BLOCK)**
   - Whenever the agent silently and automatically updates the whitepapers or docs (as per Rule 2), it **MUST ALWAYS output a strict markdown `diff` block** of that change directly into the chat.
   - Do NOT use the `render_diffs` UI macro since it frequently fails to parse. Produce the raw markdown diff explicitly in the text response so the supervisor can read it.
   - This explicitly printed diff ensures that the supervisor (ChatGPT) can continuously review, cross-verify, and audit all autonomous canonical changes made by the agent.

6. **RULE OF PROXY PLANNING (CHATGPT INTEGRATION)**
   - When acting in "Planning Mode" (creating an `implementation_plan.md` artifact), the agent **MUST ALWAYS** echo the full content of the proposed implementation plan directly into the chat immediately after generating the artifact.
   - The user's supervisor (ChatGPT) does not have persistent background access to the agent's internal workspace artifacts (like `implementation_plan.md` or `task.md`) and receives context purely through the chat interface.
   - If the implementation plan is only saved as an artifact, the supervisor is blinded and cannot approve or reject it. The plan must be actively submitted in the chat loop.

7. **RULE OF SUPERVISOR PRE-APPROVAL**
   - If the user provides a prompt from the Supervisor (ChatGPT) that explicitly contains an "APPROVED" decision or a clear, mandated engineering instruction, the agent **MUST treat this as implicit approval from the user**.
   - The agent should generate the `implementation_plan.md` (as required by the system) but is authorized to immediately proceed to the Execution and Verification phases without blocking the chat to ask the user "Can I proceed?". The Supervisor's mandate serves as the green light.

8. **RULE OF DIAGNOSTIC PROGRESS STREAMING**
   - Whenever the agent executes a heavy mathematical or loop-intensive script (especially PDE solvers running thousands of steps for state generation or phase collision), the script **MUST NOT** run completely silently across major blocks.
   - The agent must embed explicit and frequent `print()` statements inside any setup or execution loop (e.g., `if step % 500 == 0: print(...)`), logging the exact current phase, the current step, and the total target steps. This ensures that the background process provides constant, readable telemetry indicating that it is actively computing and has not frozen or fallen into a silent infinite loop.

9. **RULE OF EMPIRICAL COMPLETENESS (NO ORPHANED CLAIMS)**
   - The whitepaper is the ultimate, self-contained Registry of Truth. The project does NOT rely on separate, external `constants.json` files or `.scratch` scripts to store historical parameters because they are easily unlinked or forgotten.
   - If the agent writes an empirical conclusion into a whitepaper (e.g., "The node survives" or "Equation X fails"), the agent **MUST immediately append a localized Reproduction Block** directly beneath it.
   - This block must explicitly list the absolute floating-point parameters used (`alpha=1.0`, `lam=0.01`, etc.), the explicit mathematical formula evaluated, and the exact spatial/temporal integration limits (`N=64`, `dt=0.04`, `steps=10000`).
   - A claim without a directly attached reproduction matrix is considered a "fairy tale" and is invalid. Ensure any future AI can instantly reconstruct the environment reading only the whitepaper.
