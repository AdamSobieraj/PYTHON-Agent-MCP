---
name: pydantic-validation
description: Official Pydantic Validation guidance for implementing, debugging, reviewing, or extending Pydantic-powered Python services, data contracts, config models, structured outputs, aliases, settings, and JSON schemas. Use when Codex works with `BaseModel`, `Field`, `ConfigDict`, `AliasChoices`, `field_validator`, `model_validator`, `TypeAdapter`, `create_model`, `model_validate`, `model_dump`, `model_json_schema`, `pydantic_settings`, or `pydantic.v1` compatibility.
---

# Pydantic Validation

## Overview

Use the official Pydantic Validation docs as the source of truth for model semantics, validators, strictness, schema generation, and settings behavior. Start by deciding whether the task is about wire payload models, config parsing, dynamic schema generation, structured agent output, or `pydantic.v1` compatibility.

## Quick Start

1. Classify the task:
   - request or response models
   - aliases and wire-format compatibility
   - validators or cross-field invariants
   - settings or environment parsing
   - dynamic schemas or structured output
   - `pydantic.v1` compatibility
2. Read the matching reference first:
   - `references/core-patterns.md`
   - `references/settings-and-aliases.md`
   - `references/agent-structured-output.md`
   - `references/integration-patterns.md`
   - `references/official-links.md`
3. Inspect the target implementation for the relevant surface:
   - `BaseModel`
   - `ConfigDict`
   - `Field(`
   - `AliasChoices`
   - `field_validator`
   - `model_validator`
   - `TypeAdapter`
   - `create_model`
   - `model_validate`
   - `model_dump`
   - `model_json_schema`
   - `patch_pydantic`
4. Implement the smallest consistent change across validation, serialization, and schema generation.
5. Validate with focused tests or at least instantiate and dump representative models.

## Workflow

### 1. Choose the right validation surface

- Use `BaseModel` for named request, response, config, or event contracts.
- Use `TypeAdapter` for `list[Model]`, `TypedDict`, primitives, or ad-hoc validation without wrapping everything in a model.
- Use `create_model` only when schemas are genuinely dynamic, such as tool argument models built from JSON Schema.

### 2. Keep Python names and wire names aligned

- Prefer `Field(default_factory=...)` for mutable defaults.
- Preserve existing aliases when an external protocol already expects camelCase, kebab-case, or multiple spellings.
- When a model is serialized onto the wire, pair alias-aware fields with the existing `model_dump(by_alias=True, exclude_none=True)` pattern unless the caller intentionally wants Python field names.

### 3. Prefer validators over custom constructors

- Use `field_validator` for field-local rules and `model_validator` for cross-field invariants.
- Use `ValidationInfo.context` when validation depends on runtime facts that should not become part of the schema.
- Avoid custom `__init__` methods. The docs warn they bypass validation parameters such as strictness, `extra`, and context. Use validators or `model_post_init` instead.

### 4. Decide strictness intentionally

- Pydantic is lax by default and will coerce many values.
- Turn on strict mode when silent coercion would hide agent, tool, or protocol mistakes.
- Re-check JSON behavior before assuming Python-input strictness applies identically to JSON input.

### 5. Keep schemas and settings honest

- Generate contracts with `model_json_schema()` or `TypeAdapter.json_schema()`, not dump helpers that serialize instances.
- Use `pydantic-settings` when config should come from env vars, dotenv files, secrets, or CLI flags.
- If a surface already performs manual env expansion, decide clearly whether parsing belongs to that pre-processing layer or to Pydantic.

### 6. Watch version boundaries

- Some applications use Pydantic v2 patterns while still depending on `pydantic.v1` compatibility layers for older libraries or newer Python runtimes.
- Read `references/integration-patterns.md` before changing import order, validation behavior, or dependency versions.
- Reopen the live docs when the user asks for the latest behavior or when exact API defaults matter.

## Reference Map

- Read `references/core-patterns.md` for the main Pydantic model, validator, strictness, `TypeAdapter`, and schema rules.
- Read `references/settings-and-aliases.md` for env-driven config, alias strategy, and compatibility rules.
- Read `references/agent-structured-output.md` for model-first agent output design and validation-context patterns.
- Read `references/integration-patterns.md` for common application patterns, version checks, and compatibility considerations.
- Read `references/official-links.md` for the canonical upstream URLs, including the `llms.txt` and `llms-full.txt` sources.
