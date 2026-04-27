# Official A2A Specification

## Open This File When

- Defining or reviewing wire behavior
- Building or debugging task lifecycles
- Implementing agent discovery or agent cards
- Checking streaming, push notifications, or version negotiation
- Comparing local code to the canonical protocol model

## Canonical Mental Model

- A client sends a `Message`.
- The agent returns either a direct `Message` or a `Task`.
- If the agent returns a `Task`, the client can observe progress through polling, streaming, or push notifications.
- Task outputs belong in `Artifact` objects, not in conversational `Message` objects.

## Core Operations

- `SendMessage`
- `SendStreamingMessage`
- `GetTask`
- `ListTasks`
- `CancelTask`
- Push notification configuration methods
- `GetExtendedAgentCard`

## Core Data Model

- `Task`
  - Carries `id`, optional `contextId`, current `status`, optional `artifacts`, optional `history`, and optional `metadata`.
- `TaskStatus`
  - Holds a `state`, optional status `message`, and optional timestamp.
- `TaskState`
  - `TASK_STATE_SUBMITTED`
  - `TASK_STATE_WORKING`
  - `TASK_STATE_COMPLETED`
  - `TASK_STATE_FAILED`
  - `TASK_STATE_CANCELED`
  - `TASK_STATE_INPUT_REQUIRED`
  - `TASK_STATE_REJECTED`
  - `TASK_STATE_AUTH_REQUIRED`
- `Message`
  - Carries `messageId`, optional `contextId`, optional `taskId`, `role`, `parts`, and optional metadata.
- `Part`
  - Exactly one of `text`, `raw`, `url`, or `data`.
- `Artifact`
  - Represents task output and contains one or more `Part` items.

## High-Value Rules

- Keep message and artifact responsibilities separate.
- Treat `StreamResponse` as a one-of wrapper: only one of `task`, `message`, `statusUpdate`, or `artifactUpdate` is valid per item.
- Honor `historyLength` exactly:
  - unset: let the server choose its default amount
  - `0`: omit history
  - positive integer: cap returned history to that many most recent messages
- Send `A2A-Version` on client requests when using modern protocol behavior.
- Match versions by `Major.Minor`; patch versions are not part of compatibility negotiation.
- Return `VersionNotSupportedError` when the requested version is unsupported.

## Discovery And Capabilities

- `AgentCard` is the canonical discovery document.
- Keep `supportedInterfaces`, protocol version declarations, capabilities, and security schemes aligned with what the endpoint really supports.
- Validate streaming, push notifications, and extended agent cards against declared capabilities before using them.

## Streaming And Async Work

- A streamed interaction can be:
  - a single direct `Message`
  - a `Task` followed by `TaskStatusUpdateEvent` and `TaskArtifactUpdateEvent` items until the task reaches a terminal state
- Push notifications reuse the same conceptual event shapes as streaming updates.

## Read These Spec Areas First

- `3.1` Core operations
- `3.2.4` History length semantics
- `3.2.6` Service parameters
- `3.6` Versioning
- `3.7` Messages and artifacts
- `4.1` Core objects
- `4.2` Streaming events
- `4.4` Agent discovery objects
- `8` Agent discovery and agent cards
- `9` JSON-RPC binding
- `10` gRPC binding

## Review Checklist

- Does the code return the right top-level shape: direct `Message` vs `Task`?
- Are task states valid and semantically correct?
- Are final outputs emitted as `Artifact` objects?
- Does streaming stop at a terminal state?
- Does the agent card advertise only real capabilities, interfaces, and versions?
- Does the client or server preserve `A2A-Version` behavior correctly?
