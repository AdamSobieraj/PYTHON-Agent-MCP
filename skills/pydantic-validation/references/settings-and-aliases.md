# Settings and Aliases

## Settings management

- Use `BaseSettings` and `SettingsConfigDict` from `pydantic_settings` when configuration should load from environment variables, dotenv files, secret stores, or CLI arguments.
- Keep in mind that default values are validated too.
- Useful built-in features include nested environment parsing, dotenv support, file-based secrets, customizable source priority, and optional CLI parsing.
- Prefer `BaseSettings` when the main problem is configuration loading. Prefer plain `BaseModel` when the main problem is validating already-collected data.

## Alias strategy

- Use `alias` when a field should have one shared external name.
- Use `validation_alias` when input names should differ from Python attribute names.
- Use `serialization_alias` when output names should differ from Python attribute names.
- Use `AliasChoices` when a model must accept multiple external spellings during a migration or cross-protocol integration.
- Use `AliasPath` when the incoming value lives at a nested path.
- Use an `alias_generator` or `AliasGenerator` when the whole model follows a consistent naming convention.

## Default behavior to remember

- Validation uses aliases by default.
- Serialization by alias is opt-in unless configuration or per-call flags enable it.
- The docs note that alias-related defaults may change in Pydantic v3, so re-check live docs before relying on future behavior.

## Integration implications

- Preserve compatibility by adding aliases instead of renaming fields unless the upstream contract is changing too.
- Some applications pre-expand environment variables before or alongside Pydantic validation.
- Do not mix manual env expansion and `BaseSettings` on the same surface without deciding which layer owns defaults, interpolation, and type parsing.
