---
name: a2a-protocol
description: Official Agent2Agent (A2A) protocol guidance for implementing, debugging, reviewing, or migrating A2A agents, clients, agent cards, task flows, streaming endpoints, and protocol bindings. Use when Codex needs the official A2A specification or the official Python SDK (`a2a-sdk`) and .NET SDK (`A2A`, `A2A.AspNetCore`) for JSON-RPC, HTTP+JSON REST, gRPC, task lifecycle, agent discovery, version negotiation, or v0.3-to-v1.0 compatibility questions.
---

# A2A Protocol

## Overview

Use the official A2A specification and SDK documentation as the source of truth for protocol behavior. Prefer spec-defined names, states, and field semantics over target-application conventions, and reopen the live official URLs when exact wire behavior or package versions matter.

## Quick Start

1. Determine whether the task is mainly about protocol semantics, the Python SDK, or the .NET SDK.
2. Read the matching reference file before editing code:
   - `references/specification.md`
   - `references/python-sdk.md`
   - `references/dotnet-sdk.md`
   - `references/official-links.md`
3. Inspect the target implementation for the relevant surface:
   - `AgentCard`
   - `A2AClient`
   - `A2ACardResolver`
   - `SendMessageRequest`
   - `TaskManager`
   - `TaskState`
   - `MapA2A`
   - `MapHttpA2A`
   - `A2A-Version`
4. Implement or review the change against the official model, not just the local code shape.
5. Validate the transport, task lifecycle, and version behavior after the change.

## Workflow

### 1. Classify the change

- Start with the specification for:
  - task semantics
  - task states
  - streaming or push updates
  - agent discovery and agent cards
  - JSON-RPC, REST, or gRPC bindings
  - `A2A-Version` handling
- Start with the SDK reference for:
  - package or module selection
  - client and server helper classes
  - framework integration
  - compatibility or migration details

### 2. Map the request to protocol surfaces

- Discovery: `AgentCard`, `AgentInterface`, `AgentCapabilities`, `AgentSkill`, security schemes.
- Execution: `SendMessage`, `SendStreamingMessage`, `GetTask`, `ListTasks`, `CancelTask`.
- Long-running work: `Task`, `TaskStatus`, `TaskState`, history, artifact updates, push notifications.
- Transport and versioning: JSON-RPC vs HTTP+JSON REST vs gRPC, `A2A-Version`, 1.0 vs 0.3 compatibility.

### 3. Keep these protocol rules intact

- Use messages for communication and artifacts for task outputs.
- Return either a direct `Message` or a `Task` and its lifecycle updates, depending on the interaction pattern.
- Treat `historyLength` consistently: unset means server default, `0` means omit history, positive values cap returned history.
- Use only valid task states and preserve the difference between terminal states and interrupted states.
- Keep agent cards aligned with the real endpoint, supported bindings, protocol versions, and capabilities.
- Validate streaming and push features against declared capabilities before using them.

### 4. Watch version drift carefully

- Re-check the official spec and package pages when the user asks for the latest behavior or package version.
- Do not assume the Python and .NET SDKs are on the same release train.
- In .NET projects, inspect the exact `PackageReference` version before applying migration advice.
- Use compatibility layers only when the project intentionally targets older A2A behavior.

## Reference Map

- Read `references/specification.md` for protocol semantics and the canonical data model.
- Read `references/python-sdk.md` for `a2a-sdk` package structure, transports, server helpers, and compatibility notes.
- Read `references/dotnet-sdk.md` for `A2A` and `A2A.AspNetCore` packages, core classes, hosting patterns, and migration cues.
- Read `references/official-links.md` for the canonical upstream URLs.
