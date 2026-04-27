# Official A2A Python SDK

## Snapshot

- Package: `a2a-sdk`
- Official API index: `https://a2a-protocol.org/latest/sdk/python/api/index.html`
- Repository: `https://github.com/a2aproject/a2a-python`
- Installation:
  - `uv add a2a-sdk`
  - `pip install a2a-sdk`
- The upstream README documents Python 3.10+ and optional extras for HTTP server, gRPC, telemetry, encryption, and SQL backends.

## Compatibility Cues

- The official README says the SDK implements the A2A `1.0` specification.
- The same README also documents compatibility mode for `0.3`.
- Use compatibility paths only when the project intentionally interoperates with older A2A behavior.

## Package Map

- `a2a.types`
  - Core protocol models and enums
- `a2a.client.*`
  - `card_resolver`
  - `client`
  - `client_factory`
  - `client_task_manager`
  - transport modules for `jsonrpc`, `rest`, and `grpc`
  - auth, middleware, and helper modules
- `a2a.server.agent_execution.*`
  - agent executor and request-context building
- `a2a.server.apps.*`
  - JSON-RPC helpers
  - REST helpers
  - FastAPI and Starlette app modules
- `a2a.server.tasks.*`
  - `task_manager`
  - in-memory and database-backed task stores
  - push notification config and sending helpers
- `a2a.compat.v0_3.*`
  - legacy compatibility surfaces for older protocol behavior

## Practical Workflow

1. Read the spec first for semantics.
2. Use `a2a.types` to anchor model names and expected shapes.
3. For clients, inspect the resolver, client, and transport modules before inventing request plumbing.
4. For servers, inspect the app helpers, request handlers, executor surfaces, and task store manager before building custom routing.
5. Check whether the target implementation is using current `1.0` surfaces or compatibility namespaces before refactoring.

## Good Search Targets

- `from a2a.types import`
- `A2AClient`
- `A2ACardResolver`
- `task_manager`
- `inmemory_task_store`
- `fastapi_app`
- `jsonrpc`
- `rest`
- `grpc`
- `compat.v0_3`

## Use The Live Docs For

- Exact module contents
- Current class or function names
- Transport-specific helpers
- Compatibility namespaces and migration details
