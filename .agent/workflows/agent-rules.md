# Agent Communication and Canon Synchronization Rules

These rules are absolutely binding for any agent operating within this project.

1. **RULE OF DIRECT SUPERVISOR COMMUNICATION**
   - All messages intended for the user to copy and send to the supervisor (e.g., ChatGPT) must be output **DIRECTLY INTO THE CHAT**.
   - It is strictly forbidden to save these texts into external files (e.g., `output_report.md` or other temporary .md files) and force the user to copy from them. The chat is the sole medium for returning communication outputs.

2. **RULE OF SILENT CANON SYNCHRONIZATION**
   - The agent must **CONTINUOUSLY AND AUTOMATICALLY update the whitepapers** (e.g., `01-core-lineum.md`, `02-core-equation.md`) whenever discussions or code analyses lead to the clarification of principles, the discovery of new connections, or the refutation of previous hypotheses.
   - The agent **MUST NOT** alert or ask for permission regarding these updates ("Should I write this to the whitepaper?"). The agent performs these updates silently and routinely in the background, point by point, precisely, and surgically—ensuring that not even the smallest detail, thought, or change is ever lost in the conversation log.
   - No "batch" updates at the end of the week. Recording into the whitepaper happens **immediately** after the factual point is established.

3. **RULE OF MANDATORY CONTEXTUAL SEARCH (CHATGPT CHECK)**
   - Whenever the supervisor (ChatGPT) sends a new instruction to program, investigate, or audit, the agent **MUST ALWAYS FIRST SEARCH THE ENTIRE REPOSITORY** (via `grep_search` and reading historical code or `.scratch/` and `whitepapers/`).
   - The supervisor (ChatGPT) does not have the complete systemic and historical context of the project stored in persistent memory. The agent must not blindly and hastily accept its instruction and start "reinventing the wheel" if the exact same problem, equation, or mechanism was solved or rejected previously. In such cases, the agent confronts the task with historical findings from the repository and adjusts the plan accordingly.

4. **RULE OF CONTINUOUS REPORTING (PROGRESS LOGGING & ETA)**
   - For ANY long-running script the agent executes, it **MUST ALWAYS implement a progress tracking mechanism** that outputs cleanly to piped logs.
   - Standard `tqdm` with carriage returns (`\r`) can break in remote agent terminals. Instead, the script must output an explicit new line periodically (e.g., every 10%), embedding the **Global ETA and Total Percentage** directly into the string.
   - Example pattern: `print(f"[Global: {run_idx}/{total_runs} - {pct}% | ETA: {eta}] -> Integrating d={d} at step {step}/{steps}...")`
   - It is strictly forbidden to launch a "black box" script. The total overarching progress and ETA must be the most visible piece of information in every output cycle.

5. **RULE OF WHITEPAPER DIFF REPORTING**
   - Whenever the agent silently and automatically updates the whitepapers (as per Rule 2), it **MUST ALWAYS prepare a markdown diff** of that change and output it directly into the chat.
   - This diff ensures that the supervisor (ChatGPT) can continuously review, cross-verify, and audit all autonomous canonical changes made by the agent.

