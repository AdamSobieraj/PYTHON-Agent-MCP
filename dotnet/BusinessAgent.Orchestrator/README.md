# Business Agent Orchestrator

Basic .NET orchestrator agent for this repository.

What it does:

- loads prompt + runtime config from Langfuse when configured
- falls back to local JSON from `orchestrator.config.json` when Langfuse is unavailable
- discovers configured A2A agents at startup from their published agent cards
- discovers configured MCP tools at startup through the MCP C# SDK
- builds a Semantic Kernel `ChatCompletionAgent` that can:
  - call MCP tools directly
  - delegate subtasks to discovered A2A agents
- exports traces to Langfuse over OTLP/OpenTelemetry when Langfuse credentials are configured
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

## Langfuse prompt/config

If these credentials are present, the orchestrator loads its prompt and config from Langfuse:

```powershell
$env:LANGFUSE_PUBLIC_KEY="pk-lf-..."
$env:LANGFUSE_SECRET_KEY="sk-lf-..."
$env:LANGFUSE_BASE_URL="http://dockge.home.arpa:3000"
```

Tracing notes:

- traces are exported to `${LANGFUSE_BASE_URL}/api/public/otel/v1/traces`
- self-hosted Langfuse must support the OTLP endpoint for local tracing ingestion

Prompt selection:

- `LANGFUSE_PROMPT_NAME`
  Default: `Analyst Manager`
- `LANGFUSE_PROMPT_LABEL`
  Default: `production`
- `LANGFUSE_PROMPT_VERSION`
  Optional. If set, it overrides the label lookup.
- `AGENT_SETTINGS`
  Optional compatibility fallback if `LANGFUSE_PROMPT_NAME` is not set.

Expected Langfuse setup:

1. Create a prompt in Langfuse named `Analyst Manager` or set `LANGFUSE_PROMPT_NAME`.
2. Put the system instructions in the prompt body.
3. Put the runtime JSON config in the prompt `config` field.
4. Assign the `production` label to the prompt version you want to serve, unless you fetch by explicit version.

The example config payload to paste into Langfuse is in [langfuse_config.example.json](/E:/agent2/dotnet/BusinessAgent.Orchestrator/langfuse_config.example.json:1).

## Local fallback

If Langfuse is disabled, unreachable, or the prompt fetch fails, the orchestrator falls back to [orchestrator.config.json](/E:/agent2/dotnet/BusinessAgent.Orchestrator/orchestrator.config.json:1).

The local config file supports `${ENV_VAR:-fallback}` expansion.

## Useful environment overrides

- `ORCHESTRATOR_BIND_URL`
  Default: `http://0.0.0.0:10110`
- `ORCHESTRATOR_PUBLIC_BASE_URL`
  Default: `http://localhost:10110`
- `ORCHESTRATOR_CONFIG_PATH`
  Default: project-local `orchestrator.config.json`
- `LANGFUSE_ENABLED`
  Set to `false` to disable Langfuse config loading and tracing explicitly.

## Verifying startup

After startup:

- `GET /catalog` shows whether the orchestrator booted from `langfuse` or `json`
- `GET /.well-known/agent-card.json` reflects `agent_card` overrides from the active runtime config
