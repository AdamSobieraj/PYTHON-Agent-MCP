# CopilotKit Runtime And UI Notes

## Main Package Families

- `@copilotkit/react-core`
- `@copilotkit/react-ui`
- `@copilotkit/runtime`

The API reference also groups the docs into:

- UI components
- hooks
- classes
- LLM adapters
- SDKs

## High-Value Surfaces

- `CopilotKit`
  - top-level provider and integration surface in React
- `CopilotChat`
  - batteries-included chat UI
- `CopilotRuntime`
  - runtime and backend integration surface
- `useCopilotAction`
  - frontend action hook
- `useCopilotReadable`
  - expose app state to the copilot
- `useCoAgent`
  - CoAgent-oriented state and coordination surface

## Integration Heuristics

- Keep the React provider, runtime route, and selected agent name aligned.
- Prefer thin runtime routes when the backend already exposes the right protocol.
- Use hooks intentionally:
  - readable state for context
  - actions for app-side capability
  - CoAgent hooks for stateful agent-native UX

## CoAgents Notes

When working in CoAgents mode, expect to think in terms of:

- agentic chat UI
- shared state
- generative UI
- frontend tools
- multi-agent coordination
- human-in-the-loop

## Validate These First

- `runtimeUrl`
- selected `agent`
- `threadId`
- backend endpoint availability
- whether the backend already speaks AG-UI or another compatible surface
