# AG-UI Integration Patterns

## Common AG-UI Surfaces

- An agent service may publish AG-UI on a dedicated route such as `POST /ag-ui`, or on a general chat endpoint that accepts AG-UI payloads.
- A standalone adapter may translate another protocol or runtime into AG-UI events without changing the core agent logic.
- A frontend or runtime proxy may forward requests to an AG-UI backend while preserving thread and run identifiers.

## Important Integration Patterns

- Validate that each AG-UI request contains the minimum required user context before starting the run.
- Support accept-aware encoding when clients negotiate between:
  - `text/event-stream`
  - `application/x-ndjson`
- Map task state, tool activity, and final output from the underlying runtime into typed AG-UI events.
- Treat AG-UI as the interaction layer on top of the backend orchestration or agent framework you already have.

## Good Search Targets

- `RunAgentInput`
- `AG_UI_MEDIA_TYPE`
- `EventEncoder`
- `text/event-stream`
- `STATE_SNAPSHOT`
- `TEXT_MESSAGE_CONTENT`
- `run_ag_ui`
- `agentic_chat_endpoint`
