---
name: copilotkit
description: Official CopilotKit guidance for building, debugging, reviewing, or integrating CopilotKit runtimes, chat UIs, CoAgents, shared state, generative UI, frontend actions, human-in-the-loop flows, and AG-UI-connected backends. Use when Codex works with `@copilotkit/react-core`, `@copilotkit/react-ui`, `@copilotkit/runtime`, `CopilotKit`, `CopilotChat`, `CopilotRuntime`, `useCopilotAction`, `useCopilotReadable`, `useCoAgent`, or CopilotKit frontends that proxy to AG-UI or agent backends.
---

# CopilotKit

## Overview

Use the official CopilotKit docs as the source of truth for product concepts, runtime surfaces, and UI patterns. Start by deciding whether the task is a simple CopilotKit UI/runtime integration or a fuller CoAgents workflow with shared state, generative UI, or human-in-the-loop behavior.

## Quick Start

1. Classify the task:
   - standard CopilotKit
   - CoAgents
   - UI components
   - runtime plumbing
   - hooks and actions
   - AG-UI-backed integration
2. Read the matching reference first:
   - `references/overview.md`
   - `references/runtime-ui.md`
   - `references/integration-patterns.md`
   - `references/official-links.md`
3. Inspect the target implementation for the relevant surface:
   - `CopilotKit`
   - `CopilotChat`
   - `CopilotRuntime`
   - `runtimeUrl`
   - `threadId`
   - `HttpAgent`
   - `useCopilotAction`
   - `useCopilotReadable`
   - `useCoAgent`
4. Keep frontend wiring, runtime wiring, and agent wiring aligned.
5. Validate the thread model, chosen agent name, and backend endpoint after the change.

## Workflow

### 1. Choose the right CopilotKit mode

- Use standard CopilotKit when the app mostly needs an in-app copilot or chat experience quickly.
- Use CoAgents when you need more control over the agentic run loop and richer user-interactive agent behavior.

### 2. Separate the layers

- UI layer:
  - `CopilotKit`
  - `CopilotChat`
  - related components and hooks
- Runtime layer:
  - `CopilotRuntime`
  - route handlers and adapters
- Agent layer:
  - direct LLM integration
  - CoAgent framework integration
  - AG-UI or other backend protocols

### 3. Keep thread and agent wiring consistent

- Use a stable `threadId` strategy for conversation continuity.
- Keep `runtimeUrl` consistent with the actual API route.
- Keep the selected `agent` name aligned with what the runtime exposes.
- If the backend already speaks AG-UI, prefer a thin CopilotKit runtime proxy over unnecessary extra orchestration.

### 4. Add richer behavior intentionally

- Use frontend actions when the agent should trigger app-side behavior.
- Use shared state when the app and the agent should collaborate over structured state.
- Use generative UI when the agent needs to drive UI rendering beyond plain chat text.
- Use human-in-the-loop checkpoints when user guidance or approval must interrupt the flow safely.

### 5. Re-open live docs when details matter

- CopilotKit moves quickly across components, hooks, runtimes, and framework integrations.
- Re-check the official docs when you need exact package names, hook names, or framework-specific setup steps.

## Reference Map

- Read `references/overview.md` for the Standard vs CoAgents split.
- Read `references/runtime-ui.md` for UI, runtime, hooks, and integration surfaces.
- Read `references/integration-patterns.md` for common CopilotKit runtime, proxy, and AG-UI integration patterns.
- Read `references/official-links.md` for canonical upstream docs and indexes.
