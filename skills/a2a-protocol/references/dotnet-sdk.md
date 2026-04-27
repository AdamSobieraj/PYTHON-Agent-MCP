# Official A2A .NET SDK

## Snapshot

- Core package: `A2A`
- ASP.NET Core package: `A2A.AspNetCore`
- Repository: `https://github.com/a2aproject/a2a-dotnet`
- NuGet landing page: `https://www.nuget.org/packages/A2A`

## Version Notes

- The official repository README documents the `A2A` package as the v1.0 SDK line and calls out a transition package named `A2A.V0_3`.
- NuGet exposes multiple preview streams for `A2A`.
- Do not assume the generic package landing page matches the version used by the target application.
- Inspect the exact `PackageReference` or exact version page before applying migration advice or copying sample code.

## Core Classes

- `A2AClient`
  - Primary client surface for sending requests, including streaming and task-oriented flows.
- `A2ACardResolver`
  - Discovers agent cards from A2A-compatible endpoints.
- `TaskManager`
  - Central server-side task lifecycle manager.
- `ITaskStore`
  - Storage abstraction for tasks.
- `InMemoryTaskStore`
  - Simple development and test storage.
- `AgentTask`
  - Task model with status, history, artifacts, and metadata.
- `AgentCard`
  - Discovery document describing the agent.
- `Message`
  - Protocol message model.

## ASP.NET Core Hosting Surfaces

- `MapA2A()`
  - Map A2A endpoints for JSON-RPC-style interaction.
- `MapHttpA2A()`
  - Map HTTP+JSON REST endpoints.
- `MapWellKnownAgentCard()`
  - Publish the agent card for discovery.

## Typical Server Flow

1. Create an `ITaskStore`, often `InMemoryTaskStore` during development.
2. Create a `TaskManager`.
3. Implement message handling, commonly through `TaskManager.OnSendMessage`.
4. Build an `AgentCard` whose interfaces, protocol version, capabilities, and skills match the real server behavior.
5. Map A2A routes and publish the well-known agent card.

## Typical Client Flow

1. Resolve the remote `AgentCard` with `A2ACardResolver`.
2. Choose the advertised endpoint from `SupportedInterfaces`.
3. Create `A2AClient` with the chosen URL.
4. Send `SendMessageRequest`.
5. Handle either a direct message result or a task-oriented result.

## Good Search Targets

- `using A2A`
- `using A2A.AspNetCore`
- `A2AClient`
- `A2ACardResolver`
- `TaskManager`
- `InMemoryTaskStore`
- `MapA2A`
- `MapHttpA2A`
- `MapWellKnownAgentCard`
- `SendMessageAsync`

## Use The Live Repo Or Package Page For

- Exact preview-version APIs
- Migration guidance
- Sample project layout
- Any behavior that may have changed between preview releases
