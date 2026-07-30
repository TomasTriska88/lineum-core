---
description: How to run the test suite after code changes
---

# Running Tests

This project follows a strict **"No Temporary Tests"** policy. All tests must be integrated into the permanent test suites defined below.

## 1. Lineum (Python)
Located in the root directory. Tests cover physics, simulation logic, and output structure.
// turbo
```bash
pytest tests/ -v
```

## 2. Simulacrum (Lab)
Located in the `lab/` directory. Tests cover visualization components and harmonic analysis.
// turbo
```bash
cd lab
npm run test
```

## When to run
- **Always** after any code changes.
- **Always** before committing.
- After adding new features (you MUST add a permanent test in the corresponding `tests/` or `src/.../*.test.ts` file).

## 🤖 Mandatory AI Visual Comfort Audit
BEYOND automated Playwright tests, if you (the AI Agent) construct or modify UI layouts, you **MUST** spawn a `browser_subagent` session to visually evaluate the site on a mobile viewport (e.g. 390px) **before** establishing a Pull Request or Merge to `main`.
You must explicitly confirm to the user that:
1. Touch targets (buttons, links、tabs) are comfortably large enough.
2. Text scale prevents squinting.
3. No horizontally breaking elements exist.
Automated Playwright assertions do NOT replace this agentic visual sanity check.

## Policy: Reusable Tests
Never use temporary "scratch" or diagnostic scripts for verification if they can be implemented as a test case in the suites above. Using `.scratch/` is allowed for quick exploration ONLY, not for final verification of a task.
