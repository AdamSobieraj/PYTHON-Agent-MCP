# Pydantic Integration Patterns

## Common application surfaces

- Event and message models often use an alias generator, `populate_by_name=True`, `extra='allow'`, and `Field(default_factory=...)` for list and dict defaults.
- Protocol-facing config models often use `AliasChoices`, `ConfigDict`, and `model_validator(mode="after")` for cross-field rules.
- Tool or API argument models may be created dynamically with `create_model()` from JSON Schema fragments.
- Some applications ship an import-order-sensitive `pydantic.v1` compatibility shim for newer Python runtimes. Import that shim before libraries that still depend on `pydantic.v1`.

## Existing patterns to preserve

- Keep Python field names readable and use aliases for wire compatibility.
- Use `Field(default_factory=...)` for mutable defaults instead of bare `[]` or `{}`.
- Put cross-field invariants in `model_validator(mode="after")`.
- Keep dynamic schema generation narrow and explicit; map JSON Schema scalar types to Python primitives before calling `create_model()`.
- When serializing protocol payloads, follow the existing `by_alias=True` and `exclude_none=True` pattern unless the caller needs a different shape.

## Version notes

- Inspect the installed `pydantic` and `pydantic-settings` versions before relying on the live "latest stable" docs.
- Re-check the docs before adopting behavior introduced after the versions installed in the target environment, especially for alias defaults, validator behavior, and settings features.

## Search cues

- Search for `BaseModel`, `ConfigDict`, `Field(`, `AliasChoices`, `field_validator`, `model_validator`, `TypeAdapter`, `create_model`, `model_validate`, `model_dump`, `model_json_schema`, and `patch_pydantic`.
- Search for `by_alias=True` when a change might affect wire compatibility.
- Search for `ValidationError` when changing failure paths or test assertions.
