# Core Patterns

## Models and validation entry points

- Use `BaseModel` for named contracts and reusable payload shapes.
- Use `model_validate()` for Python objects, `model_validate_json()` for raw JSON strings or bytes, and `model_validate_strings()` when input is a string-keyed/string-valued mapping.
- Expect `ValidationError` to aggregate multiple failures into one exception.
- Remember that Pydantic guarantees the output shape after validation, not that the original input was already well typed. Coercion is part of the default behavior.
- Avoid `model_construct()` unless the data is already trusted; it skips normal validation.
- Avoid custom `__init__()` on models. The docs recommend validators or `model_post_init()` instead because custom constructors lose normal validation controls.

## Validators

- Use `field_validator` for field-local rules and `model_validator` for cross-field invariants.
- Treat `mode="after"` as the default choice when you want typed values.
- Use `mode="before"` only when you must normalize raw input before Pydantic parses it.
- Always return the validated or transformed value.
- Use `ValidationInfo.context` when rules depend on request-specific runtime context.

## TypeAdapter

- Use `TypeAdapter` when the target type is not naturally a `BaseModel`, such as `list[MyModel]`, `TypedDict`, primitives, or dataclasses.
- Reach for `validate_python()`, `validate_json()`, `dump_json()`, and `json_schema()` instead of inventing throwaway wrapper models.
- Prefer `TypeAdapter` over tiny one-off models when the schema is a simple collection or union.

## Strict mode

- Pydantic is lax by default and often coerces values like strings into integers, dates, or URLs.
- Enable strictness when agent or tool outputs must fail fast instead of being silently normalized.
- Apply strictness at the call level, field level, or config level depending how broad the requirement is.
- Re-check type-specific JSON behavior before assuming strict Python-input rules apply identically to JSON.

## JSON Schema

- Use `BaseModel.model_json_schema()` for models and `TypeAdapter.json_schema()` for adapted types.
- Do not confuse schema generation with `model_dump_json()` or `dump_json()`, which serialize instances.
- Add `Field(description=...)`, bounds, enums, `Literal`, and nested models to sharpen downstream contracts.
- Prefer deriving runtime schemas from the same models used for validation so the code and wire contract cannot drift apart.
