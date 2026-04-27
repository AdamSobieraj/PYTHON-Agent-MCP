# AG-UI Python SDK Notes

## Snapshot

- Package: `ag-ui-protocol`
- Install with:
  - `pip install ag-ui-protocol`
- Core Python docs:
  - `ag_ui.core`
  - `ag_ui.encoder`

## `ag_ui.core`

The Python SDK models AG-UI as a streaming event architecture with strongly typed data structures.

Key types called out in the docs:

- `RunAgentInput`
- `Message`
- `Context`
- `Tool`
- `State`

Key event families called out in the docs:

- lifecycle events
- text message events
- tool call events
- state management events
- special events

## `ag_ui.encoder`

Use the encoder when turning typed AG-UI events into HTTP-stream output.

Key points from the docs:

- `EventEncoder` encodes `BaseEvent` objects
- the current implementation encodes events as SSE
- the encoded wire format is `data: {json}\n\n`

Use it for Python streaming endpoints instead of hand-rolling slightly different serialization rules.

## Practical Workflow

1. Define or validate the `RunAgentInput` contract first.
2. Keep internal code working with typed AG-UI events as long as possible.
3. Encode only at the HTTP boundary.
4. Validate `Accept` handling, SSE framing, and client consumption.

## Good Search Targets

- `RunAgentInput`
- `thread_id`
- `run_id`
- `ag_ui.core`
- `EventEncoder`
- `text/event-stream`
- `STATE_SNAPSHOT`
- `STATE_DELTA`
