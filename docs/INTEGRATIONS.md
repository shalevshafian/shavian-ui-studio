# Optional integrations

Shavian UI Studio works without external integrations, but its strongest workflow uses Figma MCP and Mobbin MCP.

## Figma

Preferred installation:

```bash
claude plugin install figma@claude-plugins-official
```

Manual fallback:

```bash
claude mcp add --scope user --transport http figma https://mcp.figma.com/mcp
```

Then open Claude Code and authenticate through:

```text
/mcp
```

### Capability matrix

Use capabilities only when relevant:

| Need | Preferred Figma MCP capability |
|---|---|
| Confirm connected identity | `whoami` |
| Inspect exact frame structure | `get_design_context` |
| Visually review a frame | `get_screenshot` |
| Inspect variables and styles | `get_variable_defs` |
| Inspect a large selection cheaply | `get_metadata` |
| Inspect available libraries | `get_libraries` |
| Search reusable UI-kit assets | `search_design_system` |
| Create a new design file | `create_new_file` |
| Write native frames, components, variables, variants, and Auto Layout | `use_figma` |
| Add a user-flow diagram in FigJam | `generate_diagram` |
| Capture live web UI into editable Figma layers | `generate_figma_design` |
| Inspect component-to-code mapping | `get_code_connect_map` |
| Suggest component mappings | `get_code_connect_suggestions` |
| Confirm suggested mappings | `send_code_connect_mappings` |
| Add an explicit code mapping | `add_code_connect_map` |
| Upload image assets | `upload_assets` |

### Write policy

- Read first.
- Search existing components and variables before creating anything.
- Ask before any external write.
- Write explorations to a separate page or section.
- Never silently overwrite approved frames.
- Ask before uploading assets.
- Log changed Figma URLs in `design-brain/12-handoff-log.md`.

## Mobbin

Register Mobbin MCP:

```bash
claude mcp add mobbin --scope user --transport http https://api.mobbin.com/mcp
```

Then authenticate through:

```text
/mcp
```

Use Mobbin for evidence-backed pattern research. Do not copy a complete screen. Synthesize patterns across multiple shipped products and log findings in `design-brain/03-reference-atlas.md`.

## Authentication

The bundled scripts never accept OAuth tokens or passwords. Authentication should happen through Claude Code's MCP flow.
