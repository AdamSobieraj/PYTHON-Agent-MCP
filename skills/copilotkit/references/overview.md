# CopilotKit Overview

## What CopilotKit Is

CopilotKit is a set of tools for letting users work alongside LLMs directly inside an application. It supports both:

- Standard mode
  - use CopilotKit's built-in agentic run loop
- CoAgents
  - use fuller agent-native infrastructure when you need more control over the run loop

## Standard Vs CoAgents

- Choose Standard when you want to get a copilot into the app quickly.
- Choose CoAgents when you need richer orchestration and deeper app-agent collaboration.

## CoAgents Building Blocks

The official CoAgents overview highlights these building blocks:

- agentic chat UI
- shared state
- generative UI
- frontend tools
- multi-agent coordination
- human-in-the-loop

Use those concepts as the main design vocabulary when shaping advanced CopilotKit experiences.

## Practical Decision Rule

- If the task is about chat UI, runtime wiring, or basic app copilots, start with Standard surfaces.
- If the task is about app state collaboration, interrupts, dynamic UI, or richer agent workflows, start with CoAgents surfaces.

## Good Search Targets

- `CopilotKit`
- `CopilotChat`
- `CopilotRuntime`
- `useCopilotAction`
- `useCopilotReadable`
- `useCoAgent`
- `shared state`
- `generative UI`
- `frontend actions`
- `human-in-the-loop`
