# Threat Model

## Assets to protect

- source code;
- design files;
- user credentials;
- OAuth tokens;
- private references;
- customer information;
- approved design decisions;
- existing project instructions.

## Main risks

### Prompt injection from external content

A design file, MCP result, pasted reference, or linked page can contain text that attempts to override instructions. The workflow treats external content as reference data only.

### Unintended external writes

Native Figma writes can modify shared files. The workflow requires explicit approval before any external write and uses separate exploration sections before approved sections.

### Accidental overwrites

The scaffold creates missing files only and backs up `CLAUDE.md` before appending a marked section.

### Supply-chain risk

The plugin does not bundle third-party MCP servers or hooks. Friends install optional integrations themselves after reviewing the commands.

### Sensitive asset leakage

The workflow asks before uploading assets and recommends redaction or placeholders for private material.

## Deliberate omissions

Hooks and monitors are powerful, but they broaden the attack surface and can create hidden side effects. They are not enabled by default. Add them only after a project-specific security review.
