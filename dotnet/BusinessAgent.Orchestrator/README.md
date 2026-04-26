# Business Agent Orchestrator

Basic .NET orchestrator agent for this repository.

What it does:

- loads local JSON config from `orchestrator.config.json`
- discovers configured A2A agents at startup from their published agent cards
- discovers configured MCP tools at startup through the MCP C# SDK
- builds a Semantic Kernel `ChatCompletionAgent` that can:
  - call MCP tools directly
  - delegate subtasks to discovered A2A agents
- exposes:
  - `AG-UI` at `POST /`
  - `A2A JSON-RPC` at `POST /a2a/jsonrpc`
  - `A2A HTTP+JSON REST` under `/a2a/rest`
  - agent card at `/.well-known/agent-card.json`
  - discovery catalog at `GET /catalog`

## Runtime requirements

- .NET 8 SDK or newer
- `CHAT_BASE_URL`
- `CHAT_MODEL`
- `CHAT_API_KEY` when your chat endpoint requires authentication

Example:

```powershell
$env:CHAT_BASE_URL="http://127.0.0.1:8001/v1"
$env:CHAT_API_KEY="lm-studio"
$env:CHAT_MODEL="Qwen/Qwen3-4B-Instruct-2507"
dotnet run --project .\dotnet\BusinessAgent.Orchestrator\BusinessAgent.Orchestrator.csproj
```

Useful environment overrides:

- `ORCHESTRATOR_BIND_URL`
  Default: `http://0.0.0.0:10110`
- `ORCHESTRATOR_PUBLIC_BASE_URL`
  Default: `http://localhost:10110`
- `ORCHESTRATOR_CONFIG_PATH`
  Default: project-local `orchestrator.config.json`

The config file supports `${ENV_VAR:-fallback}` expansion, so it can stay local now and move to another provider later.
