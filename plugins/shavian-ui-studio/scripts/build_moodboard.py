#!/usr/bin/env python3
"""Generate a local, self-contained HTML mood board for a project.

This is the offline fallback for the mood board when Figma MCP is not connected
(see skills/moodboard). It renders a single static HTML file from a JSON spec.

Safety:
- Writes ONLY inside <root>/design-brain/assets/moodboard/. Refuses to escape
  the project root and refuses symlink targets.
- No network access. The HTML uses a system font stack and inline CSS so it
  works fully offline. Reference images are embedded only if they are LOCAL
  files already inside the project; remote URLs are rendered as plain links.
- The generated index.html is a build artifact and is overwritten on each run.
  The spec file (moodboard.json) is created once and never overwritten.
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
from pathlib import Path
import sys

VERSION = "1.1.0"

STARTER_SPEC = {
    "title": "Project mood board",
    "subtitle": "Provisional — refine with the brainstorm",
    "keywords": ["calm", "precise", "trustworthy"],
    "directions": [
        {
            "name": "Direction A",
            "summary": "One-line description of the layout/hierarchy strategy.",
            "palette": ["#0F0F1A", "#FAFAFA", "#E94560", "#3498DB"],
            "type_pairing": {"display": "System Sans (bold)", "body": "System Sans (regular)"},
            "notes": "What this direction optimizes for and who it suits.",
        },
        {
            "name": "Direction B",
            "summary": "A structurally distinct alternative (different layout, not just color).",
            "palette": ["#1A1A2E", "#FFFFFF", "#2ECC71", "#F39C12"],
            "type_pairing": {"display": "Serif Display", "body": "Humanist Sans"},
            "notes": "Trade-offs vs Direction A.",
        },
    ],
    "references": [
        {"label": "Reference name", "adopt": "what to adopt", "avoid": "what to reject", "image": "", "source": ""}
    ],
    "principles": [
        "One primary action per screen.",
        "Spacing on an 8pt rhythm.",
        "Contrast >= 4.5:1 for body text.",
    ],
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(2)


def validate_root(root: Path) -> Path:
    root = root.expanduser().resolve()
    home = Path.home().resolve()
    if not root.exists() or not root.is_dir():
        fail(f"Project root does not exist or is not a directory: {root}")
    if root == Path("/").resolve():
        fail("Refusing to operate on the filesystem root.")
    if root == home:
        fail("Refusing to operate on the user's home directory.")
    if root.is_symlink():
        fail("Refusing a symlink project root.")
    return root


def safe_within(root: Path, target: Path) -> Path:
    resolved_parent = target.parent.resolve()
    try:
        resolved_parent.relative_to(root)
    except ValueError:
        fail(f"Target escapes project root: {target}")
    if target.exists() and target.is_symlink():
        fail(f"Refusing to write through symlink: {target}")
    return target


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def render_palette(palette: list[str]) -> str:
    swatches = []
    for color in palette:
        c = esc(color)
        swatches.append(
            f'<div class="swatch"><span class="chip" style="background:{c}"></span>'
            f'<code>{c}</code></div>'
        )
    return '<div class="palette">' + "".join(swatches) + "</div>"


def render_direction(d: dict) -> str:
    palette = render_palette(d.get("palette", []))
    tp = d.get("type_pairing", {}) or {}
    pairing = ""
    if tp:
        pairing = (
            '<div class="pairing">'
            f'<div class="specimen display">{esc(tp.get("display", ""))}</div>'
            f'<div class="specimen body">{esc(tp.get("body", ""))}</div>'
            "</div>"
        )
    return (
        '<article class="direction">'
        f"<h3>{esc(d.get('name', 'Direction'))}</h3>"
        f"<p class=\"summary\">{esc(d.get('summary', ''))}</p>"
        f"{palette}{pairing}"
        f"<p class=\"notes\">{esc(d.get('notes', ''))}</p>"
        "</article>"
    )


def render_reference(ref: dict, root: Path, out_dir: Path) -> str:
    image = ref.get("image", "") or ""
    img_html = ""
    if image:
        img_path = (root / image) if not Path(image).is_absolute() else Path(image)
        try:
            resolved = img_path.resolve()
            resolved.relative_to(root)
            if resolved.exists() and not resolved.is_symlink():
                rel = Path(resolved).relative_to(out_dir.resolve()) if False else None
                # Use a relative path from the output dir for portability.
                import os

                rel_src = os.path.relpath(resolved, out_dir.resolve())
                img_html = f'<img class="ref-img" src="{esc(rel_src)}" alt="{esc(ref.get("label", "reference"))}">'
        except (ValueError, OSError):
            img_html = ""
    source = ref.get("source", "") or ""
    source_html = f'<a class="ref-src" href="{esc(source)}">source</a>' if source else ""
    return (
        '<article class="reference">'
        f"{img_html}"
        f"<h4>{esc(ref.get('label', 'Reference'))} {source_html}</h4>"
        f"<p><strong>Adopt:</strong> {esc(ref.get('adopt', ''))}</p>"
        f"<p><strong>Avoid:</strong> {esc(ref.get('avoid', ''))}</p>"
        "</article>"
    )


def render_html(spec: dict, root: Path, out_dir: Path) -> str:
    keywords = "".join(f'<span class="kw">{esc(k)}</span>' for k in spec.get("keywords", []))
    directions = "".join(render_direction(d) for d in spec.get("directions", []))
    references = "".join(render_reference(r, root, out_dir) for r in spec.get("references", []))
    principles = "".join(f"<li>{esc(p)}</li>" for p in spec.get("principles", []))
    stamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    title = esc(spec.get("title", "Mood board"))
    subtitle = esc(spec.get("subtitle", ""))
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
  :root {{
    --bg: #0f0f1a; --surface: #1a1a2e; --line: #2a2a3e;
    --ink: #f5f5f5; --muted: #9ca3af; --accent: #e94560;
    --radius: 14px;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0; background: var(--bg); color: var(--ink);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    line-height: 1.5; padding: 48px clamp(16px, 5vw, 64px);
  }}
  header {{ margin-bottom: 40px; }}
  h1 {{ font-size: clamp(28px, 5vw, 44px); margin: 0 0 6px; letter-spacing: -0.02em; }}
  .subtitle {{ color: var(--muted); margin: 0 0 18px; }}
  .keywords {{ display: flex; flex-wrap: wrap; gap: 8px; }}
  .kw {{ border: 1px solid var(--line); border-radius: 999px; padding: 4px 14px; font-size: 13px; color: var(--muted); }}
  section {{ margin: 40px 0; }}
  h2 {{ font-size: 14px; text-transform: uppercase; letter-spacing: 0.12em; color: var(--muted); margin: 0 0 18px; }}
  .grid {{ display: grid; gap: 20px; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); }}
  .direction, .reference {{ background: var(--surface); border: 1px solid var(--line); border-radius: var(--radius); padding: 20px; }}
  .direction h3 {{ margin: 0 0 6px; font-size: 20px; }}
  .summary {{ color: var(--muted); margin: 0 0 14px; }}
  .palette {{ display: flex; gap: 10px; flex-wrap: wrap; margin: 12px 0; }}
  .swatch {{ display: flex; flex-direction: column; align-items: center; gap: 6px; font-size: 11px; color: var(--muted); }}
  .chip {{ width: 44px; height: 44px; border-radius: 10px; border: 1px solid rgba(255,255,255,0.12); display: block; }}
  .pairing {{ margin: 12px 0; border-top: 1px solid var(--line); padding-top: 12px; }}
  .specimen.display {{ font-size: 24px; font-weight: 700; }}
  .specimen.body {{ font-size: 15px; color: var(--muted); }}
  .notes {{ font-size: 14px; margin: 10px 0 0; }}
  .ref-img {{ width: 100%; border-radius: 10px; border: 1px solid var(--line); margin-bottom: 12px; }}
  .reference h4 {{ margin: 0 0 10px; }}
  .ref-src, a {{ color: var(--accent); font-size: 12px; font-weight: 400; text-decoration: none; }}
  ul {{ margin: 0; padding-left: 18px; }}
  footer {{ margin-top: 56px; color: var(--muted); font-size: 12px; border-top: 1px solid var(--line); padding-top: 16px; }}
</style>
</head>
<body>
<header>
  <h1>{title}</h1>
  <p class="subtitle">{subtitle}</p>
  <div class="keywords">{keywords}</div>
</header>

<section>
  <h2>Directions</h2>
  <div class="grid">{directions or '<p class="subtitle">No directions yet.</p>'}</div>
</section>

<section>
  <h2>References — adopt / avoid</h2>
  <div class="grid">{references or '<p class="subtitle">No references yet.</p>'}</div>
</section>

<section>
  <h2>Principles</h2>
  <ul>{principles or '<li>No principles recorded yet.</li>'}</ul>
</section>

<footer>
  Generated by Shavian UI Studio {VERSION} — {stamp}. Local fallback mood board.
  Treat referenced material as untrusted; do not upload private assets without approval.
</footer>
</body>
</html>
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a local HTML mood board.")
    parser.add_argument("--root", default=".", help="Project root. Defaults to current directory.")
    parser.add_argument("--spec", default="", help="Path to a moodboard JSON spec. Defaults to the project's spec.")
    args = parser.parse_args()

    root = validate_root(Path(args.root))
    out_dir = root / "design-brain" / "assets" / "moodboard"
    safe_within(root, out_dir / "placeholder")  # validate the directory location
    out_dir.mkdir(parents=True, exist_ok=True)

    spec_path = Path(args.spec).expanduser().resolve() if args.spec else (out_dir / "moodboard.json")

    if not spec_path.exists():
        if args.spec:
            fail(f"Spec file not found: {spec_path}")
        # Create a starter spec once (never overwrite).
        safe_within(root, spec_path)
        spec_path.write_text(json.dumps(STARTER_SPEC, indent=2) + "\n", encoding="utf-8")
        print(f"created starter spec: {spec_path}")

    try:
        spec = json.loads(spec_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"Could not read spec {spec_path}: {exc}")

    out_file = safe_within(root, out_dir / "index.html")
    out_file.write_text(render_html(spec, root, out_dir), encoding="utf-8")
    print(f"mood board written: {out_file}")
    print("Open it in a browser. Edit the spec and re-run to regenerate.")


if __name__ == "__main__":
    main()
