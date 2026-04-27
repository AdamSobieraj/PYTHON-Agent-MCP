# AG-UI Protocol Notes

## What AG-UI Is

- AG-UI is an open, lightweight, event-based protocol for connecting user-facing applications to agentic backends.
- It standardizes how agent state, UI intents, and user interactions flow between frontend and backend.
- It is the Agent-to-User layer, not the agent-to-tool or agent-to-agent layer.

## Relationship To MCP And A2A

- AG-UI: agent to user-facing application
- MCP: agent to tools and data
- A2A: agent to agent

Use AG-UI for the frontend interaction surface, even when the backend also uses MCP or A2A internally.

## Core Design Ideas

- Event-driven communication
- Bidirectional interaction
- Minimal protocol assumptions
- Transport agnosticism
- Compatibility through adaptation and middleware

## Architectural Pieces

- Application
- AG-UI client
- Agent
- Optional secure proxy or adapter

The common abstraction is effectively: run an agent with `RunAgentInput` and consume a stream of typed events.

## Key Input Shape

- `RunAgentInput` includes:
  - `threadId`
  - `runId`
  - optional `parentRunId`
  - `state`
  - `messages`
  - `tools`
  - `context`
  - `forwardedProps`

Treat this as the canonical payload for AG-UI execution.

## Standard Event Families

- Lifecycle events
  - `RUN_STARTED`
  - `RUN_FINISHED`
  - `RUN_ERROR`
  - `STEP_STARTED`
  - `STEP_FINISHED`
- Text message events
  - `TEXT_MESSAGE_START`
  - `TEXT_MESSAGE_CONTENT`
  - `TEXT_MESSAGE_END`
- Tool call events
  - `TOOL_CALL_START`
  - `TOOL_CALL_ARGS`
  - `TOOL_CALL_END`
- State events
  - `STATE_SNAPSHOT`
  - `STATE_DELTA`
  - `MESSAGES_SNAPSHOT`
- Special events
  - `RAW`
  - `CUSTOM`

## High-Value Rules

- Keep thread and run identifiers stable.
- Emit events in a consumer-friendly order.
- Use vendor-neutral message structures where possible.
- Preserve multimodal message content rather than flattening it too early.
- Use `STATE_DELTA` only when the consumer can correctly apply the patch semantics.
- Use middleware for adaptation, filtering, logging, or auth instead of contaminating the agent core.

## Message Model Cues

- Messages are vendor-neutral.
- Roles can include more than just user and assistant.
- AG-UI supports structured and multimodal content.
- The protocol is designed so client code can avoid provider-specific message formats.

## Transport Notes

- SSE is a common transport for event streaming.
- HTTP clients commonly post `RunAgentInput` and receive a stream of serialized AG-UI events.
- Client cancellation, buffering, and content negotiation matter for UX and correctness.
