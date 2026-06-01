# Design knowledge

Core design intelligence for the Shavian UI Studio workflow. This file holds the principles **and the relationships between them** — the dependency chains that turn a pile of rules into coherent, non-generic UI. Read it before generating any interface. Sibling references: [style-taxonomy.md](style-taxonomy.md) (named aesthetics), [question-playbook.md](question-playbook.md) (what to ask before designing), [screenshot-protocol.md](screenshot-protocol.md) (reading references), [parallel-brainstorm.md](parallel-brainstorm.md) (generating divergent directions).

The thesis: good UI is not a checklist of best practices applied independently. The variables constrain each other. Change the type scale and you change line-length, column width, and spacing rhythm. Pick an accent and you've implicitly chosen a contrast budget. Design the *system of relationships*, not the parts.

---

## 1. Visual hierarchy

Hierarchy is the answer to "where do I look, and in what order?" You have five levers. Use the fewest that work.

- **Size** — the bluntest, strongest signal. A 2× size jump reads as "more important" instantly. Reserve the largest size for exactly one thing per view.
- **Weight** — cheaper than size. Going from 400 → 600 creates emphasis without disrupting layout. Prefer weight over size for inline emphasis.
- **Color** — saturation and lightness draw the eye before hue does. A single saturated element on a muted field wins attention. Don't color everything; color is a spotlight, and two spotlights cancel.
- **Spacing** — isolation creates importance. Whitespace around an element is hierarchy. A lonely button outranks a crowded one.
- **Position** — top-left in LTR (top-right in RTL) is read first; the optical center and the bottom-right "terminal" carry weight. Sticky/fixed position elevates permanently.

**The squint test.** Blur your eyes (or literally apply a 8–12px blur). The composition should still have an obvious focal point and a readable order of regions. If everything turns to uniform grey mush, you have no hierarchy — every element is fighting at the same level. Fix by *removing* emphasis from secondary elements, not adding more to the primary.

**One primary action per view.** Each screen has a single highest-priority action rendered as the one filled/accent button. Everything else is secondary (outline/tonal) or tertiary (text/ghost). Two primary buttons side by side means you haven't decided what the screen is for. If genuinely two equal actions exist, that's a sign the screen should split.

Hierarchy is *relative*. There is no "big" — only bigger-than. Establish 3–4 distinct levels (e.g. page title / section heading / body / caption) and hold the line. A fourth and fifth level dilute the first three.

---

## 2. Spacing & rhythm

Spacing is the invisible skeleton. Inconsistent spacing reads as "broken" even when users can't name why.

**Use a 4 / 8pt grid.** Pick a base unit (8px) and a half-step (4px) for fine adjustments. Reasons: (1) most screen densities and @2x/@3x assets divide cleanly by 4/8, avoiding sub-pixel blur; (2) a constrained set of values forces decisions and produces visual rhythm; (3) it composes — 8 + 8 = 16, the math stays clean.

**Spacing scale** (geometric-ish, not linear): `4, 8, 12, 16, 24, 32, 48, 64`. Note the jumps grow — adjacent values are distinguishable. A linear scale (`4, 8, 12, 16, 20, 24…`) gives too many near-identical options and muddy results. Treat the scale as the *only* legal spacing values. "16px or 24px" is a real decision; "19px" is a bug.

**Proximity = relationship.** This is the load-bearing principle. The space *between* groups must exceed the space *within* a group, or grouping collapses. A label 4px from its input but 24px from the next field reads as paired. Reverse those numbers and it reads as orphaned. Concretely: intra-group < inter-group by at least ~1.5×. A card with 16px internal padding should sit ≥24px from its neighbors.

**Vertical rhythm.** Stack spacing on a consistent baseline so text and components feel like they share a grid. Line-height and vertical margins should be multiples of the base unit where practical. Rhythm is what makes a long page feel composed rather than assembled.

**Padding vs margin discipline.** Internal padding belongs to the component; external spacing is the parent's job. Don't bake outer margins into reusable components — it breaks reuse and double-spaces.

Spacing depends on **density tier** (see §5) and **type scale** (§3): denser UIs compress the scale, larger type demands larger gaps. These are linked, not independent.

---

## 3. Typographic scale & pairing

**Modular scale.** Generate sizes by repeatedly multiplying a base by a ratio:
- `1.2` (minor third) — tight, good for dense/data UIs and small screens.
- `1.25` (major third) — the safe default; clear steps without drama.
- `1.333` (perfect fourth) — editorial, expressive, good when headlines should sing.

From base 16px at ratio 1.25: `16 → 20 → 25 → 31 → 39 → 49…` and down `16 → 12.8 → 10.24`. Round to sensible pixels (16, 20, 25→24/25, 31→32). The point is *proportion*, not exact values. A scale gives you 5–7 sizes total; resist inventing one-offs.

**Line length: 45–75 characters** per line for body text (≈66 is the sweet spot). Shorter and the eye jumps too often; longer and it loses the return. This is a hard constraint that *drives column width* (§5).

**Line-height ↔ font-size.** They move inversely. Body text wants `1.4–1.6` (looser for long reading). Large headings want `1.0–1.25` — tight, because big text already has air. A 48px heading at line-height 1.6 looks gappy and broken. Also: longer line length needs *more* line-height to help the eye find the next line. So line-height depends on both size and measure.

**Pairing strategies:**
- **Contrast** — pair a display/serif headline with a neutral sans body. The contrast must be obvious (different classification), not subtle (two similar sans fonts look like a mistake).
- **Harmony / superfamily** — one type family with multiple weights/widths/optical sizes (e.g. a sans with text + display cuts). Safest, most coherent.
- **When to use one typeface:** almost always for product UI. A single well-chosen family with a real weight range (400/500/600/700) covers 90% of needs. Reach for a second face only when there's an editorial or brand reason, and never a third.

Avoid the AI-generic move of grabbing two trendy Google fonts at random. Pairing is a deliberate contrast or deliberate harmony — never accidental.

Type scale is upstream of almost everything: it sets line-height, which sets line-length, which sets column width (§5), which interacts with the spacing scale (§2).

---

## 4. Color systems

**Think in semantic roles, not raw swatches.** Define tokens by *job*:
- `surface` (and surface-raised, surface-sunken) — backgrounds at different elevations.
- `content` (primary / secondary / muted) — text and icons *on* surfaces.
- `border` (subtle / strong) — dividers and outlines.
- `accent` — the brand/primary action color.
- `state` — success / warning / danger / info.

Designing roles first means dark mode, theming, and contrast all become token swaps instead of rewrites.

**60-30-10.** Roughly 60% dominant (usually a neutral surface), 30% secondary (supporting neutrals/containers), 10% accent. The accent earns its impact by being *scarce*. AI-generic UI floods accent everywhere and it stops meaning anything.

**Perceptual lightness — prefer OKLCH over HSL.** In HSL, equal lightness values look wildly different across hues (HSL yellow at 50% is far brighter than HSL blue at 50%). OKLCH lightness is perceptually uniform, so a tint ramp keeps even visual steps and accents at "the same L" actually match. Build palettes in OKLCH; you'll get consistent contrast and predictable dark-mode behavior.

**Contrast ratios (WCAG):** body and small text need **4.5:1** against their background; large text (≥24px, or ≥18.66px bold) and meaningful UI elements / icons / focus indicators need **3:1**. Treat these as floors, not goals. Muted-but-legible secondary text typically lands ~4.5–7:1; placeholder/disabled may go lower but then must not carry essential meaning.

**Building tints/shades.** Generate a ramp (e.g. 50–900) by holding hue and chroma roughly steady while stepping lightness in OKLCH. Slightly *increase* chroma at the dark end and *decrease* it near the extremes to avoid muddy or neon steps. Don't just mix with white/black in sRGB — it desaturates unevenly and the mids go grey.

**Dark mode is not inversion.** Flipping lightness produces harsh, vibrating screens. Rules:
- Don't use pure black (#000) surfaces — use a very dark desaturated neutral (e.g. ~12–16% L). Pure black + bright text causes halation.
- Don't use pure white text — drop to ~85–90% L to reduce glare.
- Desaturate accents slightly; saturated colors vibrate on dark fields.
- Elevation reverses: in light mode higher surfaces are *lighter* via shadow; in dark mode they get *lighter* (more L), since shadows barely read on dark.

Accent → state → contrast is a dependency chain: choosing an accent constrains which state hues stay distinguishable from it, and every choice must clear the contrast floor against your surfaces.

---

## 5. Layout & grids

**12-column vs flexible.** The 12-col grid persists because 12 divides into 2/3/4/6 — most useful column counts. Use it for marketing pages and dense dashboards needing alignment across disparate widths. For component-driven product UI, **flexible/intrinsic layouts** (flexbox/grid with `min()`/`clamp()`/auto-fit) often beat a rigid 12-col — let content and container negotiate.

**Container widths.** Body text content caps around `60–75ch` (~640–720px) for readability (driven by §3's measure rule). Full-app shells go wider (1200–1440px) but keep *text columns* narrow inside them. Use a max-width + auto margins; never let prose run the full width of a 1920px monitor.

**Density tiers.** Decide the tier up front — it cascades into spacing and type:
- **Comfortable** — generous padding (16–24px), larger touch targets, marketing/consumer.
- **Cozy** — default product density.
- **Compact** — tight padding (4–8px), smaller type, data-heavy tools (tables, IDEs, admin).
Density is not a single knob; it pulls spacing scale (§2) and type scale (§3) together.

**Optical vs mathematical alignment.** Math says center it; the eye disagrees for non-rectangular shapes. A play triangle in a circular button must be nudged right to *look* centered. Round/pointed glyphs (O, A, triangles) must *overshoot* the cap-height baseline to look the same size as flat ones. Trust the eye over the measurement. Icon and avatar alignment, button label centering, and list bullets all need optical correction.

---

## 6. Depth & elevation

**Shadows model a light source.** Pick one consistent light direction (typically top, slightly front) and let every shadow obey it. A shadow is offset *down* (light from above), blurred proportional to elevation, and tinted toward the surface's hue (not pure black at full opacity — that looks like dirt). Higher = larger blur + larger Y-offset + lower opacity spread.

**Layering / z-system.** Define elevation tiers, not arbitrary shadows: `0` flat on page, `1` cards, `2` sticky bars / dropdowns, `3` modals, `4` toasts/popovers. Each tier has one canonical shadow. Consistency across tiers is what makes depth legible.

**A good shadow = two layers.** A tight, near-opaque short shadow (contact / ambient occlusion) plus a soft, wide, faint shadow (cast). One-layer shadows look flat or fake.

**When flat beats elevated.** Brutalist, editorial, and high-density UIs often read better with *borders* than shadows — borders are crisper at small sizes, render identically on any background, and survive dark mode without retuning. Use elevation to signal *interactivity and layering*; use borders to signal *separation and structure*. Don't pile both on the same element. Flat-with-borders is also the more honest choice in compact density (§5).

---

## 7. Motion

**Motion has three legitimate jobs.** If a transition doesn't serve one, cut it.
1. **Orientation** — show where something came from / went (a panel slides from the edge it's anchored to).
2. **Feedback** — confirm a tap/toggle/submit registered (press states, ripple, checkmark).
3. **Continuity** — preserve object identity across states (shared-element / layout transitions) so the user doesn't re-parse the screen.

**Durations.** Most UI motion lives in **150–300ms**. Micro-feedback (hover, small toggles) ~100–150ms. Entering elements ~200–300ms. Large/full-screen transitions up to ~400ms. Exits should be *faster* than entrances (get out of the way). Anything >500ms in product UI feels sluggish unless it's a deliberate, rare moment.

**Easing.** Almost never linear (linear reads mechanical, fine only for continuous spinners/progress). Use **ease-out** for entrances (fast start, gentle settle — feels responsive), **ease-in** for exits, **ease-in-out** for moves between two on-screen positions. Spring physics beat fixed curves for anything that should feel tactile (drags, sheets) — tune stiffness/damping, not duration.

**Reduced motion.** Respect `prefers-reduced-motion`. Don't kill *all* feedback — replace large translational/scaling/parallax motion with opacity fades or instant state changes. Motion sensitivity is an accessibility relationship (§8), not an on/off toggle.

Distance and duration are linked: a thing moving farther needs slightly more time, but velocity should feel constant-ish — don't make a small toggle take as long as a full-page slide.

---

## 8. Accessibility as design relationships

Accessibility isn't a post-hoc checklist; it's constraints that, satisfied early, make the design *better for everyone*. Frame each as a relationship:

- **Contrast ↔ palette.** Your color ramp (§4) must produce text/background pairs clearing 4.5:1 (3:1 large/UI). This *constrains* how light your muted text and how saturated your accents can be. Decide it when building tokens, not at QA.
- **Target size ↔ spacing & density.** Interactive targets ≥ **44×44px** (iOS) / ~48dp (Android); ~24px minimum with adequate spacing (WCAG 2.2). This sets a floor on your spacing scale (§2) and density tier (§5) — compact UIs must still give touch targets breathing room via padding even when the visual element is small.
- **Focus order ↔ layout & hierarchy.** Keyboard/tab order should follow visual reading order (§1). If DOM order and visual order diverge, focus jumps confusingly. Visible focus rings need 3:1 contrast and must not be removed. Hierarchy and focus order are the same ordering, expressed two ways.
- **Motion sensitivity ↔ motion design.** Every transition (§7) needs a reduced-motion fallback. Build motion as an *enhancement layer* so removing it degrades gracefully.
- **Content ↔ color.** Never encode meaning in color alone (status, required fields, errors). Pair color with icon/text/shape. This is the §4 state-color rule and §1 hierarchy rule meeting accessibility.

When these constraints fight your aesthetic, the constraint usually wins — but more often it just rules out the lazy option and pushes you somewhere more distinctive.

---

## How the variables relate

The whole point. Designing one variable in isolation breaks others. The major dependency chains:

**Type chain (the spine of everything):**
`base font-size → modular ratio → type scale → line-height (inverse to size) → line-length (45–75ch) → text column width → page container width → spacing scale (must harmonize with line-height for vertical rhythm)`
Change the base from 16→18 and every downstream value shifts. This is why you set type first.

**Color chain:**
`accent hue → state hues (must stay distinguishable from accent and each other) → tint/shade ramps (OKLCH, uniform L steps) → contrast pairs (≥4.5:1 / 3:1) → dark-mode variants (desaturate, lighten surfaces by elevation)`
Pick an accent and you've spent part of your contrast budget; the remaining colors must fit what's left.

**Density chain:**
`density tier → spacing scale (compress or expand) → component padding → type scale (compact wants ratio 1.2, comfortable tolerates 1.333) → touch-target floor (44px clamps how compact you can really go)`
Density is never one number — it's a coordinated move across spacing, type, and targets.

**Hierarchy ↔ everything:**
Hierarchy (§1) is *expressed through* type scale (size/weight), color (accent scarcity, 60-30-10), spacing (isolation), elevation (raised = important), and motion (entrance order). It's not a separate variable — it's the *purpose* the others serve. Focus order (§8) is hierarchy made keyboard-navigable.

**Elevation ↔ color ↔ mode:**
Shadow strength depends on surface color and reverses in dark mode (§4, §6). A shadow tuned on white is invisible on dark; dark mode substitutes *lightness* for shadow. So your elevation system and your color system co-design.

**Motion ↔ layout ↔ accessibility:**
Transition distance/direction (§7) come from layout anchoring (a sheet slides from the edge it lives on), and every motion needs a reduced-motion path (§8).

Rule of thumb: when in doubt about a value, trace which chain it's in and derive it from its upstream neighbor instead of guessing.

---

## Smart defaults

A safe, coherent starting kit. Override with intent — but start here, not from zero.

**Type**
- Base body: `16px`, line-height `1.5`.
- Scale ratio: `1.25` (major third).
- Steps: `12, 14, 16, 20, 25, 31, 39` (caption → display).
- Headings line-height: `1.1–1.25`; body `1.5`; long-form `1.6`.
- Measure: cap text columns at `~65ch` (≈680px).
- Weights: `400` body, `500` emphasis, `600/700` headings. One typeface.

**Spacing (8pt)**
- Scale: `4, 8, 12, 16, 24, 32, 48, 64`.
- Card padding: `16` (cozy) / `24` (comfortable).
- Inter-group gap ≥ `1.5×` intra-group gap.
- Section vertical rhythm: `48–64`.

**Radius tiers**
- `0` sharp / `4` controls (inputs, small buttons) / `8` cards / `12–16` large containers / `9999` pills & avatars.
- Pick *two or three* radii max and apply by role. Nest consistently: inner radius ≈ outer radius − padding.

**Shadow tiers** (light from top, tinted dark-neutral, two-layer)
- `sm`: `0 1px 2px rgba(0,0,0,.06), 0 1px 1px rgba(0,0,0,.04)` — cards.
- `md`: `0 4px 8px rgba(0,0,0,.08), 0 2px 4px rgba(0,0,0,.06)` — dropdowns/sticky.
- `lg`: `0 12px 24px rgba(0,0,0,.12), 0 4px 8px rgba(0,0,0,.08)` — modals.
- Dark mode: drop shadow opacity, raise surface lightness instead.

**Color**
- Build ramps in OKLCH, 9–11 steps.
- 60-30-10 split; accent ≤ ~10% of surface area.
- Contrast: body `≥4.5:1`, large/UI/focus `≥3:1`.
- Dark surface ~`12–16% L` (not #000); dark text ~`85–90% L` (not #fff).

**Motion**
- Default transition: `200ms ease-out`.
- Micro-feedback: `120ms`. Large/page: `300–400ms`. Exits faster than entrances.
- Always ship a `prefers-reduced-motion` fallback (fade or instant).

**Targets & focus**
- Interactive ≥ `44×44px`.
- Visible focus ring, `≥3:1`, never removed.

---

## Anti-generic checklist

Tells of "AI-generic" UI, and how to break out. If your draft hits these, it looks like everything else. (See [style-taxonomy.md](style-taxonomy.md) to commit to a real aesthetic, and [parallel-brainstorm.md](parallel-brainstorm.md) to force divergence.)

- **Default purple/blue gradient.** The `#6366f1 → #a855f7` indigo-violet gradient is the house style of generated UI. Break: pick a real palette from references ([screenshot-protocol.md](screenshot-protocol.md)); if you use a gradient, derive it from the brand and keep hue travel small, or drop gradients for flat color.
- **Uniform 8px radius on everything.** One radius on every element flattens hierarchy. Break: assign radii by role (sharp section, soft card, pill button) and nest them correctly.
- **Centered hero + three feature cards.** The reflexive landing layout. Break: try asymmetry, an off-center focal point, a left-aligned editorial column, a bento grid, or a single dominant element instead of three equal ones.
- **Even card grids with identical weight.** Everything the same size = no hierarchy (fails the squint test, §1). Break: vary card size/span by importance; let one item dominate.
- **Lorem-density everything.** Uniform paragraph blocks and placeholder filler hide real layout problems. Break: design with *real, varied-length content* — short labels, long descriptions, empty states, edge cases.
- **Accent color smeared everywhere.** Violates 60-30-10 (§4); the accent stops signaling. Break: ration accent to the single primary action + key data points.
- **Emoji as icons / generic stock glyphs.** Reads as low-effort. Break: one consistent icon set, optically aligned (§5), sized to the type scale.
- **No empty/loading/error states.** Generated UI shows only the happy path. Break: design the zero state and the failure state — they reveal whether the layout actually holds.
- **Shadows on a flat brand, or shadows + borders doubled up.** Decide depth strategy (§6): elevation *or* borders per element, not both.
- **Symmetric, mathematically-centered everything.** Ignores optical alignment (§5). Break: nudge icons/labels by eye; let the composition breathe asymmetrically.
- **Generic font pairing (two trendy Google sans).** Break: one strong family with a real weight range, or a *deliberate* contrast pairing (§3).
- **Pure-inversion dark mode.** Vibrating, harsh (§4). Break: retune surfaces, text, accents, and elevation for dark specifically.
- **Motion that animates for its own sake.** Decorative fades on everything. Break: keep only motion that orients, gives feedback, or maintains continuity (§7).

Before shipping a draft, run it past [question-playbook.md](question-playbook.md) (did you design for the actual user/content/constraints?) and the squint test (§1). If it could be any product's UI, it's not yet this product's UI.
