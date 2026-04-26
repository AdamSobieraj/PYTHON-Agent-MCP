# AG-UI Playground for Business Agent Orchestrator

This app is a small Next.js + CopilotKit frontend for the .NET Business Agent Orchestrator in this repository.

It uses:

- `CopilotKit` as the chat UI
- `@ag-ui/client` `HttpAgent` to talk to the orchestrator over AG-UI
- the orchestrator's `/catalog` endpoint to show discovered A2A agents and MCP tools

## What it connects to

The .NET orchestrator exposes:

- `POST /` for AG-UI
- `GET /catalog` for the live startup catalog
- `POST /a2a/jsonrpc` for A2A JSON-RPC
- `GET /.well-known/agent-card.json` for the agent card

By default this playground expects the orchestrator at:

```env
ORCHESTRATOR_URL=http://localhost:10111
NEXT_PUBLIC_ORCHESTRATOR_URL=http://localhost:10111
```

## Setup

1. Start the .NET orchestrator first:

```powershell
cd E:\agent2

$env:CHAT_BASE_URL="http://localhost:8001/v1"
$env:CHAT_API_KEY="lm-studio"
$env:CHAT_MODEL="Qwen/Qwen3-4B-Instruct-2507"
$env:ORCHESTRATOR_BIND_URL="http://0.0.0.0:10111"
$env:ORCHESTRATOR_PUBLIC_BASE_URL="http://localhost:10111"

dotnet run --project .\dotnet\BusinessAgent.Orchestrator\BusinessAgent.Orchestrator.csproj
```

2. In a second terminal, start the UI:

```powershell
cd E:\agent2\ui-playground\ag-playground
npm install
npm run dev
```

3. Open:

- `http://localhost:3000`

## Notes

- The CopilotKit API route is in `app/api/copilotkit/route.ts`.
- The chat UI is in `components/chat.tsx`.
- The catalog panel is in `app/page.tsx`.
- If you move the orchestrator to another port, update `.env`.
