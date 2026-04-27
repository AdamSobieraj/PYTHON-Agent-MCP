# CopilotKit Integration Patterns

## Common Architecture

- A common setup is:
  - a React or Next.js UI wrapped in `CopilotKit`
  - a chat surface such as `CopilotChat`
  - a runtime route built with `CopilotRuntime`
  - an `HttpAgent` or similar backend bridge
- Keep `runtimeUrl`, `agent`, and `threadId` aligned across the UI and runtime layers.

## Important Integration Pattern

- A thin proxy runtime is often the simplest design:
  - CopilotKit UI in the frontend
  - a route using `CopilotRuntime`
  - `HttpAgent` forwarding to an AG-UI or custom backend

If the backend already speaks AG-UI, prefer this thin-proxy approach unless there is a clear reason to add more runtime logic.

## Version And Package Checks

- Inspect the target application's `package.json`, lockfile, or installed package tree before relying on examples from the latest docs.
- Re-check live docs when exact hook names, package names, or route helpers matter.

## Good Search Targets

- `CopilotKit`
- `CopilotChat`
- `CopilotRuntime`
- `copilotRuntimeNextJSAppRouterEndpoint`
- `HttpAgent`
- `runtimeUrl`
- `threadId`
- `agent=\"orchestrator\"`
