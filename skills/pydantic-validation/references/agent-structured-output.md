# Agent Structured Output

## Model-first pattern

- Define the output contract with Pydantic models before wiring the agent runtime.
- Add `Field(description=...)` and real constraints such as `gt`, `ge`, `min_length`, `Literal`, or enums so the schema is useful to both validators and model providers.
- Validate raw tool or model output with `model_validate()` before treating it as trusted application data.

## Official Pydantic AI example

- The Pydantic Validation docs include an agent example that defines a `City` model and sets `output_type=list[City]`.
- That example uses `field_validator('country')` plus `ValidationInfo.context` to reject countries that are not in a runtime-provided allowlist.
- The validation context is applied after model generation and is not sent to the LLM, which makes it a good fit for policy or environment-specific checks.

## Applying the pattern outside Pydantic AI

- The same approach works with LangGraph, LangChain, MCP tools, or custom agent loops.
- If a downstream system needs JSON Schema, generate it from the same model instead of maintaining a second hand-written contract.
- Prefer one canonical model per output shape, then derive validation, serialization, and schema generation from that model.

## Failure strategy

- Use strict mode or explicit validators when coercion would hide tool or model mistakes.
- Surface `ValidationError` details to logs and tests, but keep user-facing summaries concise.
- When a model needs runtime context, keep that context out of the schema and pass it through validation context instead.
