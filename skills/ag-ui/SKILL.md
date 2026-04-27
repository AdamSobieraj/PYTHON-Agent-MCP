---
name: ag-ui
description: Official Agent User Interaction (AG-UI) protocol guidance for implementing, debugging, reviewing, or adapting AG-UI agents, clients, event streams, message schemas, state updates, middleware, and streaming HTTP endpoints. Use when Codex works with `ag-ui-protocol`, `ag_ui.core`, `ag_ui.encoder`, `@ag-ui/client`, `HttpAgent`, `RunAgentInput`, `threadId`, `runId`, typed AG-UI events, or frontend-to-agent streaming integrations.
---

# AG-UI

## Overview

Use the official AG-UI docs as the source of truth for protocol semantics, event shapes, and SDK surfaces. Treat AG-UI as an event stream between a user-facing app and an agentic backend, not as a plain request-response API.

## Quick Start

1. Classify the task:
   - protocol semantics
   - Python SDK
   - JS client or `HttpAgent`
   - middleware or protocol adaptation
   - endpoint wiring or streaming integration
2. Read the matching reference first:
   - `references/protocol.md`
   - `references/python-sdk.md`
   - `references/integration-patterns.md`
   - `references/official-links.md`
3. Inspect the target implementation for the relevant surface:
   - `RunAgentInput`
   - `threadId`
   - `runId`
   - `HttpAgent`
   - `EventEncoder`
   - `TEXT_MESSAGE_CONTENT`
   - `STATE_DELTA`
   - `TOOL_CALL_START`
   - `RAW`
   - `CUSTOM`
4. Preserve the canonical event model instead of inventing local shapes.
5. Validate transport, event ordering, and state updates after the change.

## Workflow

### 1. Start from AG-UI architecture

- Model the system as:
  - application
  - AG-UI client
  - backend agent
  - optional secure proxy or adapter
- Prefer translating an existing backend to AG-UI events over rewriting the agent runtime from scratch.

### 2. Keep run identity stable

- Preserve `threadId` across a conversation.
- Preserve `runId` per execution.
- Preserve `parentRunId` when representing lineage or branching.
- Do not silently drop messages, state, tools, context, or forwarded properties from `RunAgentInput`.

### 3. Treat AG-UI as typed streaming

- Emit typed lifecycle, text, tool, state, and special events.
- Keep event order sensible for the consumer.
- Stream text incrementally instead of buffering everything to the end.
- Use snapshots and deltas intentionally:
  - snapshots for full state
  - deltas for incremental updates

### 4. Be explicit about transport

- AG-UI is transport-agnostic, but SSE over HTTP is a common delivery model.
- In Python integrations, use the encoder surface when converting typed events into HTTP stream output.
- Validate `Accept` handling, content type, buffering behavior, and client cancellation semantics.

### 5. Use middleware for adaptation

- Prefer middleware when bridging AG-UI to another protocol or framework.
- Keep protocol translation, filtering, logging, auth, and tool-call filtering out of the core agent logic when possible.

### 6. Re-check live docs when details matter

- AG-UI moves quickly.
- Re-open the official pages when you need exact event names, current SDK entry points, or transport behavior.

## Reference Map

- Read `references/protocol.md` for the event model and architectural rules.
- Read `references/python-sdk.md` for `ag_ui.core` and `ag_ui.encoder`.
- Read `references/integration-patterns.md` for common AG-UI endpoint, adapter, and streaming patterns.
- Read `references/official-links.md` for canonical upstream URLs.
