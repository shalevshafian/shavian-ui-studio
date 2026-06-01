# Style taxonomy

A working catalog of UI/visual styles — what each one *is*, what it *signals*, and how to *execute* it without it looking cheap. This file is the matching layer of Shavian UI Studio: when a user describes intent ("trustworthy", "playful", "expensive"), use this to map that intent to one or two concrete directions you can actually build.

Read this alongside its siblings:
- `design-knowledge.md` — the underlying mechanics (type scale, spacing, color theory, contrast) that every style here depends on.
- `question-playbook.md` — how to extract intent signals from the user before you commit to a style.
- `screenshot-protocol.md` — how to read a reference image and reverse-engineer which style(s) it's using.

A style is not a theme or a color. A style is a *coherent set of decisions* about type, color, radius, shadow, density, and motion that together produce a single emotional read. Pick the read first, then the tokens follow.

---

## How to pick a style

Start from the user's *intent signals*, not their stated style preference. People say "make it modern" and mean six different things. Translate words into candidate directions:

| Intent signal (what they say / want) | Primary candidates | Accent / alternative |
|---|---|---|
| "Trustworthy", "fintech", "banking", "handle my money" | Minimal/Functional, Luxury/Premium | Swiss typographic for the marketing site |
| "Modern SaaS", "clean", "professional" | Minimal/Functional, Flat/Material-like | Bento grid for the landing page |
| "Creative tool", "for designers/devs", "powerful" | Dark-mode-first / developer, Editorial | Brutalism as an accent on marketing |
| "Consumer social", "fun", "for everyone" | Playful/Friendly, Claymorphism | Maximalism for brand moments |
| "Premium", "luxury", "high-end", "expensive" | Luxury/Premium, Editorial | Minimal as the app-side fallback |
| "Editorial", "content-first", "publication", "blog" | Editorial/Magazine, Swiss typographic | Minimal for reading view |
| "Bold", "stand out", "we're different" | Brutalism/Neo-brutalism, Maximalism | Aurora/gradient-mesh for hero |
| "Dashboard", "lots of data", "trading", "ops" | Data-dense/Enterprise, Minimal/Functional | Dark-mode-first for the pro tier |
| "Nostalgic", "retro", "90s/Y2K", "vibe" | Retro/Vaporwave, Maximalism | Hand-drawn for warmth |
| "Friendly", "approachable", "human", "soft" | Playful/Friendly, Claymorphism, Hand-drawn | Neumorphism (sparingly) |
| "Futuristic", "AI", "next-gen" | Aurora/gradient-mesh, Dark-mode-first | Glassmorphism as an accent |
| "Tactile", "realistic", "physical product" | Skeuomorphism, Neumorphism | Claymorphism for a softer take |

Three questions that disambiguate fastest (see `question-playbook.md`):
1. **Who is the user and what's the stakes?** High-stakes/financial → restrained. Low-stakes/expressive → bold.
2. **Content or chrome?** Content-heavy → Editorial/Swiss/Minimal. Interaction-heavy → Functional/Flat/Data-dense.
3. **Differentiation budget?** Established/conservative market → safe & functional. Crowded/commodity market → a distinctive style is a feature, not a risk.

Default when unsure: **Minimal/Functional with one accent**. It is the hardest to get *wrong*, and you can always layer personality on top. A boring-but-correct interface beats an expressive-but-broken one every time.

---

## The catalog

### 1. Minimal / Functional

- **Signature traits:** Neutral grayscale base + one accent; generous whitespace; type does the hierarchy work (weight + size, not color); small-to-medium radii (4–8px); shadows subtle or absent; restrained, fast micro-motion (150–200ms ease-out).
- **Feels like / signals:** Calm, competent, trustworthy, "we have nothing to hide." Suits productivity tools, fintech, B2B SaaS, healthcare.
- **Use when:** The content or the task is the point; you need credibility; you want longevity over a trend.
- **Avoid when:** The brand needs to feel exciting or differentiated in a crowded consumer space — minimal can read as generic/forgettable.
- **Common failure modes:** Becomes *anemic* (no hierarchy, everything gray, nothing pops); whitespace turns into emptiness with no rhythm; "minimal" used as an excuse to skip states and polish.
- **Token implications:** Radius 4–8px; shadow `0 1px 2px rgba(0,0,0,.06)` and one elevated step; palette neutral-9-step + single accent; type pairing one humanist sans (e.g. a clean grotesque) across the board; motion subtle, ease-out.
- **Exemplars:** Modern collaboration/productivity apps, developer billing dashboards, project trackers.

### 2. Swiss / International typographic

- **Signature traits:** Grid-driven layout (visible columns); a single neutral grotesque at multiple weights; flush-left, ragged-right text; heavy reliance on alignment and white space; near-zero decoration; color used as bold flat blocks, often red/black/white.
- **Feels like / signals:** Rigorous, intellectual, authoritative, design-literate. Suits agencies, cultural institutions, publications, premium B2B.
- **Use when:** Typography and structure *are* the brand; content is text-heavy and you want it to feel considered.
- **Avoid when:** You need warmth, playfulness, or hand-holding for non-expert users.
- **Common failure modes:** Cold and unapproachable; the grid becomes rigid and breaks on real content; without true typographic skill it just looks plain rather than disciplined.
- **Token implications:** Radius 0–2px; shadows none; palette black/white + one saturated primary; type pairing single grotesque (e.g. Helvetica-lineage / Inter / a neo-grotesque) in 3–4 weights; motion minimal, snappy.
- **Exemplars:** Design studio portfolios, museum sites, editorial product marketing.

### 3. Editorial / Magazine

- **Signature traits:** Strong serif or display type for headlines; mixed column widths; pull quotes, drop caps, large hero imagery; asymmetric, expressive layouts; rich type scale with dramatic size contrast; restrained color so imagery and type lead.
- **Feels like / signals:** Premium, narrative, curated, opinionated. Suits long-form content, fashion/lifestyle brands, premium product launches, storytelling marketing.
- **Use when:** You're telling a story or selling through narrative; content quality is high and you want to frame it.
- **Avoid when:** Building a dense utility app — editorial flourishes get in the way of repetitive tasks.
- **Common failure modes:** Form over readability (line lengths too long, contrast too low for fancy serifs); breaks down in templated/CMS reality; flourishes applied evenly instead of saved for moments.
- **Token implications:** Radius small/none; shadows subtle; palette muted neutrals + one editorial accent; type pairing display serif + readable body serif or clean sans; motion gentle reveal/parallax used sparingly.
- **Exemplars:** Online magazines, premium DTC brand stories, conference/event sites.

### 4. Bento grid

- **Signature traits:** Modular grid of rounded "boxes" of varying sizes (the bento-box metaphor); each cell is a self-contained feature/stat/visual; consistent gutters and corner radius; mixes text, mini-charts, icons, and product shots; strong on landing/marketing surfaces.
- **Feels like / signals:** Modern, organized, feature-rich-but-digestible, "tech company in 2024." Suits product landing pages, feature overviews, dashboards.
- **Use when:** You have several distinct things to show at once and want them scannable and visually balanced.
- **Avoid when:** Content has a strong linear narrative, or cells would be near-empty — sparse bento looks unfinished.
- **Common failure modes:** Cells with mismatched visual weight; everything the same size (loses the rhythm that makes bento work); decorative cells with no real content; over-rounded into childishness.
- **Token implications:** Radius 12–24px (consistent across cells); shadows soft or flat with borders; palette neutral cards on a slightly tinted background, accent per category; type pairing functional sans; motion staggered entrance, subtle hover lift.
- **Exemplars:** SaaS feature sections, hardware/product pages, personal dev portfolios.

### 5. Brutalism / Neo-brutalism

- **Signature traits:** Raw, high-contrast; hard black borders (2–4px); solid drop shadows with hard edges (no blur); clashing saturated colors; system or monospace type; visible structure, sharp corners or aggressively chunky radii; intentionally "undesigned."
- **Feels like / signals:** Bold, irreverent, anti-corporate, confident, "we don't follow the rules." Suits creative tools, indie products, crypto/web3, youth brands, portfolios.
- **Use when:** Differentiation is the goal and the audience reads polish as boring; you want memorable over safe.
- **Avoid when:** Trust and calm matter (finance, health, enterprise); accessibility is a hard requirement and the palette fights contrast rules.
- **Common failure modes:** Crosses from "intentional" to "broken/cheap"; unreadable color combos; the joke wears off and usability suffers; everyone in the niche now looks identical.
- **Token implications:** Radius 0px or 2px (or one chunky 16px+ used consistently); shadow hard-offset `4px 4px 0 #000`; palette loud, often primary-color or near-neon on white; type pairing grotesque/mono, big and tight; motion snappy, sometimes deliberately abrupt.
- **Exemplars:** Indie SaaS marketing, design-tool landing pages, experimental portfolios.

### 6. Glassmorphism

- **Signature traits:** Frosted-glass panels (background blur + translucency); subtle white/colored borders to catch "light"; layered depth over a colorful or photographic background; soft shadows; works best in dark or vivid contexts.
- **Feels like / signals:** Sleek, modern, premium-tech, "OS-level." Suits widgets, music/media players, dashboards over imagery, AI products.
- **Use when:** You have a rich background to blur and want depth without heavy chrome; for overlays, cards, and nav that float above content.
- **Avoid when:** Backgrounds are plain (the effect disappears); accessibility-critical text sits on glass (contrast is fragile); heavy use tanks performance on low-end devices.
- **Common failure modes:** Illegible text over busy blur; contrast failures; overused until every surface is glass and depth flattens; blur performance jank.
- **Token implications:** Radius 16–24px; shadow soft + inner highlight border `1px rgba(255,255,255,.2)`; palette vivid/gradient background, translucent surfaces (`rgba` 8–20% alpha); backdrop-blur 12–24px; type pairing clean sans, high weight for legibility; motion smooth parallax/scale.
- **Exemplars:** Media-player UIs, dashboard overlays on photography, AI assistant panels.

### 7. Neumorphism

- **Signature traits:** Soft UI — elements extruded from or pressed into a single-color surface using paired light/dark shadows; very low contrast; monochromatic; subtle, pillowy; rounded shapes.
- **Feels like / signals:** Soft, tactile, calm, "future-minimal." Suits niche dashboards, music/IoT controls, concept work.
- **Use when:** A small, contained, low-information surface needs a soft physical feel and you can control the background color exactly.
- **Avoid when:** Anywhere accessibility matters — borderless low-contrast controls fail contrast and discoverability. This is the riskiest mainstream style.
- **Common failure modes:** Buttons that don't look tappable; total contrast failure; falls apart on any background that isn't the exact base color; looks like a 2020 fad.
- **Token implications:** Radius 12–20px; shadow *paired* `-6px -6px 12px light, 6px 6px 12px dark`; palette single desaturated base (light gray / dark slate); type pairing soft geometric sans; motion gentle press/inset transition.
- **Exemplars:** Smart-home control concepts, audio app concepts. Use sparingly and never for primary CTAs.

### 8. Skeuomorphism

- **Signature traits:** Realistic textures and materials (leather, paper, metal, felt); detailed lighting and gradients; real-world object metaphors; rich, often heavy shadows; literal affordances (switches look like switches).
- **Feels like / signals:** Familiar, tactile, premium-craft, nostalgic. Suits creative/music tools (synths, mixers), games, kids' apps, brand-rich experiences.
- **Use when:** A real-world metaphor genuinely aids understanding (an audio mixer, a notebook), or for deliberate craft/nostalgia.
- **Avoid when:** Building modern utility UI at scale — it's heavy, hard to maintain, and dated outside its niches.
- **Common failure modes:** Gaudy and dated; textures fight content; inconsistent "physics" across the UI; huge asset/maintenance cost.
- **Token implications:** Radius varies by "material"; shadows rich, multi-layer; palette material-driven (wood, metal, paper tones); type pairing often serif or characterful; motion mimics physical action.
- **Exemplars:** Music production tools, e-reader/notebook apps, certain games and toys.

### 9. Flat / Material-like

- **Signature traits:** Solid fills, no skeuomorphic texture; clear color system with semantic roles; elevation expressed through tonal layers and soft shadows; consistent components and spacing; bold, legible sans; purposeful motion tied to elevation.
- **Feels like / signals:** Friendly-professional, systematic, accessible, "from a real design system." Suits Android-first apps, large product suites, anything needing consistency at scale.
- **Use when:** You need a proven, accessible, component-driven system many people can build against consistently.
- **Avoid when:** You want to stand out — Material-like UIs read as familiar to the point of generic; brand personality needs extra work.
- **Common failure modes:** Looks like every other Material app; over-relying on the default theme; FAB/shadow conventions misused; "flat" taken so far that affordances vanish.
- **Token implications:** Radius 4–16px (consistent); shadow tonal elevation scale (1–5 levels); palette primary/secondary/surface/error semantic tokens; type pairing one versatile sans (Roboto-lineage / Inter); motion standard easing curves, shared-element transitions.
- **Exemplars:** Cross-platform consumer apps, internal tools, Google-ecosystem-adjacent products.

### 10. Claymorphism

- **Signature traits:** Soft, puffy 3D shapes; large rounded corners; light pastel palettes; subtle double inner+outer shadows giving a "clay/inflated" look; playful icons and blobs; bright and friendly.
- **Feels like / signals:** Cheerful, approachable, soft, low-stakes, "for humans." Suits onboarding, kids/education, wellness, friendly consumer apps, illustrative landing pages.
- **Use when:** You want warmth and delight without going full maximalist; great for empty states, onboarding, marketing.
- **Avoid when:** Conveying seriousness, density, or authority; clay everywhere makes a product feel like a toy.
- **Common failure modes:** Toy-like when applied to serious tasks; pastel-on-pastel contrast failures; inflated shapes that waste space; cuteness fatigue.
- **Token implications:** Radius 20–32px; shadow soft outer + soft inner highlight; palette bright pastels + saturated accents; type pairing rounded geometric sans; motion bouncy/spring easing.
- **Exemplars:** Wellness and habit apps, education products, friendly fintech for younger users.

### 11. Dark-mode-first / "developer" aesthetic

- **Signature traits:** Dark or near-black base; high-contrast text; monospace accents and code-friendly type; saturated neon/cyan/green accents on dark; tight, information-rich layouts; subtle gridlines, terminal/IDE references; precise, fast motion.
- **Feels like / signals:** Technical, powerful, insider, "built by people who use it." Suits developer tools, infra, analytics, AI products, crypto.
- **Use when:** Your audience is technical or works in low-light/long-session contexts; dark is the default not an afterthought.
- **Avoid when:** Mainstream consumer audiences who expect light mode; content-heavy reading (dark long-form is fatiguing for many).
- **Common failure modes:** Pure-black with pure-white text (harsh halation); neon accents with poor contrast; "dark = just inverted light" without re-tuning elevation and color; over-busy with gridlines.
- **Token implications:** Radius 6–12px; elevation via lighter surfaces not shadows (`#0a0a0a → #1a1a1a → #2a2a2a`); palette dark neutrals + 1–2 saturated accents; type pairing UI sans + monospace; motion fast, precise, ease-out.
- **Exemplars:** Developer dashboards, observability tools, terminal-adjacent products, AI playgrounds.

### 12. Maximalism

- **Signature traits:** Abundance — many colors, layered textures, mixed type, dense decoration, overlapping elements; intentional visual noise; expressive and personality-forward; more is more.
- **Feels like / signals:** Energetic, expressive, brave, cultural, "we have a point of view." Suits music/entertainment, fashion, events, creative brands, campaigns.
- **Use when:** Brand expression and memorability outrank efficiency; one-off marketing moments and hero experiences.
- **Avoid when:** Task-focused product UI; accessibility-critical flows; anything users do repeatedly (noise becomes fatigue).
- **Common failure modes:** Chaos without hierarchy (eye has nowhere to land); accessibility wreckage; performance bloat from heavy assets; impresses once, exhausts forever.
- **Token implications:** Radius mixed intentionally; shadows/effects layered; palette 4+ colors with a clear dominant; type pairing 2–3 contrasting families with one anchor; motion plentiful but choreographed, with calm focal points.
- **Exemplars:** Album/artist sites, festival pages, fashion lookbooks, agency showcases.

### 13. Retro / Vaporwave

- **Signature traits:** Period-specific cues (80s/90s/Y2K) — chrome, gradients, pixel/dot-matrix type, neon pinks and cyans, grids and sunsets, glitch effects; nostalgia as the primary lever.
- **Feels like / signals:** Nostalgic, playful, subcultural, ironic-cool. Suits music, gaming, NFT/web3, niche merch, event/launch microsites.
- **Use when:** The audience shares the nostalgia and the product can lean into a vibe; short-lived campaigns and brand moments.
- **Avoid when:** Building durable utility UI; broad audiences who don't get the reference; anything needing to feel current rather than throwback.
- **Common failure modes:** Costume rather than design (theme with no substance); legibility sacrificed to effects; the reference is wrong for the audience; ages instantly once the trend turns.
- **Token implications:** Radius era-dependent (sharp for Y2K chrome, soft for 90s); shadows neon glows; palette neon gradients (magenta/cyan/purple) or muted retro pastels; type pairing pixel/display + readable body; motion glitch, scanline, CRT-style.
- **Exemplars:** Synthwave music sites, retro-gaming brands, nostalgia-driven launch pages.

### 14. Playful / Friendly (rounded, illustrative)

- **Signature traits:** Generous rounding; bright but controlled palette; custom illustrations/characters; soft shadows; friendly rounded sans; delightful micro-interactions and mascot moments; approachable copy paired tightly with visuals.
- **Feels like / signals:** Welcoming, human, optimistic, easy. Suits consumer social, education, kids, wellness, onboarding, friendly fintech.
- **Use when:** Lowering the barrier to entry matters; you want users to feel safe, encouraged, and a little delighted.
- **Avoid when:** Authority/seriousness is required; dense professional tools where cuteness undermines competence.
- **Common failure modes:** Generic stock-illustration look ("Corporate Memphis"); delight that slows down power users; inconsistent illustration style; cute but uninformative.
- **Token implications:** Radius 12–24px; shadow soft and friendly; palette bright primaries/secondaries with white space; type pairing rounded geometric sans + same for headings; motion springy, celebratory at milestones.
- **Exemplars:** Language-learning apps, kids/education products, community and habit apps.

### 15. Luxury / Premium (restrained, high-contrast, serif)

- **Signature traits:** Lots of negative space; high contrast (often black/white/cream); elegant serif or refined sans display type; tight, deliberate type; gold/muted metallic or single jewel accent; slow, graceful motion; restraint as a flex.
- **Feels like / signals:** Expensive, exclusive, considered, timeless. Suits luxury goods, premium services, high-end DTC, private banking, fine hospitality.
- **Use when:** Price point and brand demand restraint and refinement; "we don't need to shout."
- **Avoid when:** Mass-market, value-driven, or feature-comparison contexts where restraint reads as sparse/empty.
- **Common failure modes:** Sparse mistaken for empty; "luxury = gold gradient" (gaudy, the opposite of premium); low-contrast elegance failing accessibility; slow motion that feels sluggish rather than graceful.
- **Token implications:** Radius 0–4px; shadows minimal; palette black/cream/white + one restrained accent (deep jewel or muted gold); type pairing high-contrast serif display + understated sans body; motion slow, eased, refined fades.
- **Exemplars:** Luxury fashion/jewelry sites, premium hospitality, high-end editorial commerce.

### 16. Data-dense / Enterprise (Bloomberg-like)

- **Signature traits:** Maximum information density; tight rows, small type, monospace numerals; minimal whitespace; functional color coding (red/green, status); fixed headers, sortable tables, dense charts; little decoration; speed and scannability over beauty.
- **Feels like / signals:** Serious, powerful, "for professionals who live in this all day." Suits trading, analytics, admin/ops consoles, monitoring, CRMs.
- **Use when:** Expert users need to see and act on a lot at once; screen real estate is precious; efficiency beats elegance.
- **Avoid when:** Casual/occasional users; mobile-first contexts; onboarding-heavy products — density overwhelms newcomers.
- **Common failure modes:** Illegible density (too small, too tight); color coding without legend or accessibility; no hierarchy so everything competes; intimidating to all but experts.
- **Token implications:** Radius 0–4px; shadows minimal (borders/dividers carry structure); palette neutral + functional status colors + tabular numerals; type pairing compact UI sans + monospace numbers; motion near-zero (instant feedback, no decorative delay).
- **Exemplars:** Trading terminals, observability/analytics consoles, enterprise admin panels.

### 17. Aurora / gradient-mesh

- **Signature traits:** Soft, multi-color blurred gradient backgrounds (the "aurora"/mesh look); luminous, dreamy color blends; often paired with dark base and glass/translucent cards; glow accents; minimal foreground chrome so the gradient leads.
- **Feels like / signals:** Modern, optimistic, premium-tech, "AI/future." Suits AI products, modern SaaS heroes, launch pages, creative tools.
- **Use when:** You want a contemporary, atmospheric hero without heavy imagery; great for marketing surfaces and empty backgrounds.
- **Avoid when:** Dense functional screens (gradients fight content); brand needs precision/seriousness; contrast over the mesh can't be guaranteed.
- **Common failure modes:** Muddy color blends; foreground text contrast failing over the mesh; the same "purple-blue AI gradient" everyone uses (instant cliché); banding on low-bit displays.
- **Token implications:** Radius 12–24px; shadows soft glows; palette 3–4 harmonious hues blended, on dark or off-white; type pairing clean sans; motion slow drifting/animated gradients (respect reduced-motion).
- **Exemplars:** AI product landing pages, modern SaaS hero sections, creative-tool marketing.

### 18. Hand-drawn / Organic

- **Signature traits:** Imperfect lines, sketchy borders, hand-lettered or humanist type, organic blobs and doodles, slight wobble/rotation; warm paper-like backgrounds; human, crafted imperfection as the point.
- **Feels like / signals:** Warm, human, honest, indie, approachable. Suits whiteboarding/creativity tools, indie brands, education, community, personal sites.
- **Use when:** You want to feel human and un-corporate; collaboration/ideation contexts where polish would feel cold.
- **Avoid when:** Authority, precision, or high-stakes trust is needed; large enterprise contexts; anything where "rough" reads as "unfinished/unreliable."
- **Common failure modes:** Inconsistent hand-style across screens; charm undermining clarity; hard to scale and systematize; "quirky" tipping into amateurish.
- **Token implications:** Radius organic/irregular; shadows soft, hand-offset; palette warm neutrals + a few friendly accents; type pairing hand/humanist display + readable body; motion subtle wobble/draw-on, used sparingly.
- **Exemplars:** Collaborative whiteboard tools, indie maker products, education and community sites.

---

## Mixing styles

Most real products are **one dominant style + one accent**, not a blend of equals. The dominant style governs the system tokens (radius, spacing, type, base palette) and ~80% of surfaces. The accent appears in *moments* — hero, empty states, brand pages, celebration — and never touches the parts users operate repeatedly.

**Anchor rule:** Pick the dominant style for the *most-used* surface (usually the app/product UI), and let the accent live on the *least-used, highest-attention* surface (usually marketing/onboarding). A Data-dense trading app can have an Aurora marketing site. A Minimal SaaS app can have a Maximalist launch page. The user never feels whiplash because the two never share a screen.

**Combinations that work:**
- **Minimal/Functional + Bento grid** — minimal app, bento landing. Same neutral palette, bento just arranges it. Very common, very safe.
- **Dark-mode-first + Aurora/gradient-mesh** — dark dev UI with an aurora hero. The gradient stays in marketing; the app stays precise.
- **Editorial + Minimal** — editorial marketing/story, minimal reading or app view. Shared serif can bridge them.
- **Luxury/Premium + Editorial** — natural siblings; both restrained, both type-led, both serif-friendly.
- **Swiss typographic + Brutalism** — both structure-forward and type-led; brutalism is essentially Swiss with the volume up. Easy to dial between.
- **Playful/Friendly + Claymorphism** — same warm, rounded DNA; clay adds depth to the friendly base.
- **Glassmorphism as an accent on almost anything dark** — glass cards work as an *accent layer* over Dark-mode-first or Aurora bases.

**Combinations that clash (avoid mixing as equals):**
- **Brutalism + Luxury/Premium** — opposite philosophies (raw/loud vs. restrained/refined). One cancels the other.
- **Neumorphism + Data-dense** — soft low-contrast controls vs. high-density legibility; neumorphism destroys scannability.
- **Skeuomorphism + Flat/Material** — competing depth metaphors; looks like two products stapled together.
- **Maximalism + Minimal** as equals — you must pick which one *wins*; "minimal-maximalism" usually just means a clean base with bold moments (i.e. minimal dominant, maximalist accent — which is fine, as long as you're explicit).
- **Three or more styles** — almost always incoherence. If you think you need three, you've probably mislabeled one style's *components* as a separate style.

**How to anchor cleanly:**
1. Name the dominant style and lock its tokens (radius, type pairing, base palette, motion curves) — see `design-knowledge.md` for the mechanics.
2. Name the single accent and restrict *where* it's allowed to appear (list the surfaces).
3. Ensure shared primitives — buttons, inputs, type ramp — follow the *dominant* style everywhere, including accent surfaces, so the product still feels like one thing.
4. Keep accessibility owned by the dominant style. Accent styles (glass, neumorphism, aurora, maximalism) are the ones that break contrast — never let them govern interactive, text-bearing, or critical surfaces.

When reverse-engineering a reference that *looks* mixed, use `screenshot-protocol.md` to separate the dominant system from the accent moment — they usually live on different surfaces, and identifying which is which tells you what to actually build.
