# Question playbook

How to ask the fewest, sharpest questions to extract maximum design intent — and
what to infer instead of asking. The job of this plugin is to move the idea in
the user's head onto a screen as fast as possible. Questions are a cost. Spend
them only where the answer changes what you build, and where you genuinely cannot
infer it. Everywhere else: infer, show, and let critique correct you.

Read alongside its siblings:
- [`design-knowledge.md`](./design-knowledge.md) — the design principles you apply once intent is captured.
- [`style-taxonomy.md`](./style-taxonomy.md) — the named visual styles you map taste answers onto.
- [`screenshot-protocol.md`](./screenshot-protocol.md) — how to ingest and read screenshots/references.
- [`parallel-brainstorm.md`](./parallel-brainstorm.md) — how to turn captured intent into 2–3 parallel directions.

---

## Maximize signal per question

Every question must earn its place. Apply these rules in order:

1. **Concrete choices beat open prompts.** Don't ask "what style do you want?"
   Ask "Closer to (A) clean and minimal like Linear, (B) warm and editorial
   like Stripe's marketing, or (C) dense and utilitarian like a trading
   terminal?" A/B/C answers are fast to give and unambiguous to act on.
2. **Show references instead of asking for adjectives.** Adjectives are lossy
   ("modern" means ten different things). A screenshot or named product is a
   high-bandwidth, low-ambiguity signal. Prefer "point me at one app you'd be
   happy to be compared to" over "describe the vibe."
3. **Never ask what you can infer.** If the codebase, a screenshot, or the
   product type already answers it, do not ask. See [Infer, don't ask](#infer-dont-ask).
   Asking a question you could have answered yourself reads as not paying attention.
4. **Batch related questions — max ~5 per message.** One tight, scannable block
   the user can answer in one pass. Never drip questions one at a time across
   many turns; never dump 15 at once.
5. **Always offer an exit on every question.** Each question must accept
   "decide for me", "unknown", or "not relevant" as a valid answer. Make this
   explicit. A user who can't answer should never be blocked — that's your cue
   to apply a default and move.
6. **Default to motion.** When in doubt, generate something and ask the user to
   react to it. A concrete wrong direction is corrected faster than a blank page
   is filled.

---

## The fast path (idea → first screen)

This is the default ladder. In most cases these five questions — often fewer —
are enough to start producing. Send them as one batched message. If the user
answers "decide for me" to any, apply the default and proceed.

**(1) What + who.** What are we building, and who opens it?
> "In one line: what is this, and who's the main person using it? (e.g.
> 'a habit tracker for busy parents', 'an internal admin for support agents').
> Not sure who? Say 'decide for me' and I'll assume the obvious user."

**(2) The one anchor screen/flow.** The single screen that, if it's right,
the product feels right.
> "If we nail ONE screen first, which is it? The dashboard? The create flow?
> The list? Pick the screen you picture in your head when you imagine this app."

**(3) 2–5 reference signals OR screenshots.** Positive references, anti-references,
or images.
> "Drop 2–5 signals: apps/sites you love (and why in 3 words each), plus 1
> you'd hate to look like. Screenshots or sketches are even better than names —
> paste anything you've got. None handy? Say so and I'll propose from your
> product type."

**(4) The feeling + the anti-feeling.** Where you're heading and what to avoid.
> "Two words: how should it FEEL (calm? energetic? premium? playful?) — and
> one feeling to actively AVOID (e.g. 'not corporate', 'not childish')."

**(5) One hard constraint.** The single non-negotiable.
> "One hard constraint I must respect? (brand color, must work on mobile, dark
> only, ships in your existing stack, accessibility target). If none, say
> 'none' and I'll use sensible defaults."

After this, stop asking and produce. If the user gave thin answers, lean harder
on inference and bias toward [generating directions](./parallel-brainstorm.md).

---

## Question bank by dimension

Pull from here only when the fast path left a real gap. Every question is
choice-oriented and copy-ready. Pick the 1–3 that matter for this project; don't
run the whole bank.

### Product & user
- "Is the primary user (A) a first-time consumer, (B) a returning power user,
  or (C) an internal/admin operator?"
- "Is success 'they did the thing once' (conversion) or 'they come back daily'
  (retention)? This changes how much we optimize first-run vs. density."
- "Single user, or do multiple people share/collaborate in here?"

### Anchor flow
- "What's the one action this screen exists to make easy?"
- "What does the user see the very first time, before they have any data?
  (drives the empty state)"
- "Walk me through the happy path in 3 steps — arrive → do X → see Y?"
- "Is this screen mostly (A) consume/read, (B) create/input, or (C) monitor/scan?"

### Taste / references
- "Name 1–3 products you'd be flattered to be compared to."
- "Name 1 you never want to look like."
- "For your favorite reference: is it the (A) layout/structure, (B) color, (C)
  typography, (D) spacing/calm, or (E) motion you actually want? Pick the ones
  that matter." (see [Reference-first elicitation](#reference-first-elicitation))

### Visual style
Map answers to named styles in [`style-taxonomy.md`](./style-taxonomy.md).
- "Pick a lane: (A) minimal/Swiss, (B) soft/friendly (rounded, pastel), (C)
  bold/editorial (big type, high contrast), (D) technical/dense, (E) playful/
  expressive, (F) glass/depth?"
- "Corners: sharp, slightly rounded, or pill-soft?"
- "Density: airy (lots of whitespace) or compact (more on screen)?"
- "Light, dark, or both? Default if you don't care: both, light-first."

### Brand / content
- "Got a brand color / logo / existing palette? Paste it. If not, I'll choose
  and you can swap later."
- "Tone of the copy: plain and direct, warm and human, or precise and formal?
  (see also UX copy in `design-knowledge.md`)"
- "Real content I should use, or should I write realistic placeholder copy?
  (placeholder by default — never lorem ipsum)"

### Data & states
- "What's the realistic shape of the data — roughly how many items, longest
  label, biggest number? (so layouts survive real content)"
- "Which states matter here: empty, loading, error, success, partial,
  over-limit? Default: I'll design empty + loading + the populated happy path."
- "Anything async/slow the user waits on? (drives skeletons vs. spinners)"

### Constraints & accessibility
- "Hard constraints: required brand color, font license, framework, component
  library, ship date? List any; say 'none' otherwise."
- "Accessibility bar: (A) just be reasonable, (B) WCAG AA target, (C) strict AA+
  / known users with low vision? Default: AA."
- "RTL / localization needed now, or English-only for v1?"

### Platform / viewport
- "Primary surface: (A) desktop web, (B) mobile web, (C) native iOS/Android,
  (D) responsive must-do-both? Default: responsive, design at desktop + 390px."
- "Touch, mouse, or both? (affects target sizes and hover affordances)"
- "Any fixed frame I'm designing into (embedded panel, set canvas size)?"

---

## Reference-first elicitation

References are your highest-bandwidth signal. A single screenshot answers a dozen
adjective questions at once. Treat references as the primary input and questions
as the thin layer that disambiguates them. For ingestion mechanics see
[`screenshot-protocol.md`](./screenshot-protocol.md).

**Always collect both polarities.** A positive reference says "head here." An
anti-reference ("I'd hate to look like X") prunes the space just as fast and is
often more decisive. Ask for at least one of each.

**For every reference, pin down exactly WHAT to adopt.** "I like Linear" is not
actionable — Linear is many decisions. Ask the user (or, if they can't say,
decide and state your read) which layers transfer:

| Layer        | What you'd be borrowing                          | Disambiguating question |
|--------------|--------------------------------------------------|--------------------------|
| Structure    | layout grid, where things live, nav model        | "The layout/where things sit, or just the look?" |
| Hierarchy    | what's loud vs. quiet, focal order               | "Same sense of what's emphasized first?" |
| Spacing      | density, breathing room, rhythm                  | "The calm/airy feel, or denser?" |
| Type         | typeface character, scale, weight contrast       | "The typography specifically?" |
| Color        | palette, contrast level, accent use              | "The exact colors, or just the energy?" |
| Motion       | transitions, easing, micro-interactions          | "The way it moves/animates?" |
| Tone         | copy voice, labels, personality                  | "The wording/voice too?" |

**And what to reject.** For anti-references, name the offending layer:
> "When you say 'not corporate' about that one — is it the stock-photo imagery,
> the cramped density, the blue-gray palette, or the stiff copy? Pin the part
> you're reacting to so I don't import it by accident."

**Default read when the user can't specify.** State your inference in one line
and proceed: "I'll take Linear's *structure + spacing* (calm, keyboard-first
layout) but your brand color, not its palette — shout if that's wrong."

---

## Infer, don't ask

Before asking anything, mine what's already in front of you: the package
manifest, existing components, the repo's conventions, the screenshots, and the
product type. Infer, apply a safe default, and only confirm if confirming is
cheap and the cost of being wrong is high.

| Signal source                  | Infer this                                   | Safe default if absent                   | Confirm? |
|--------------------------------|----------------------------------------------|------------------------------------------|----------|
| `package.json` / lockfile      | framework, UI lib, CSS approach, icon set    | the stack the repo already uses          | No — match it |
| Existing components/tokens      | spacing scale, radius, color vars, type ramp | reuse them verbatim                       | No — reuse |
| Tailwind / theme config         | palette, breakpoints, font family            | follow the config                        | No |
| Product type (e.g. dashboard)   | likely screens, density, key states          | conventions from `design-knowledge.md`   | Only if ambiguous |
| Screenshots provided            | current style, layout, brand, density        | extract and continue                     | No — read it |
| Repo language / TS config       | language, strictness, naming conventions     | match existing files                     | No |
| Brand assets in repo (logo/css) | colors, logo, voice                          | derive palette from logo                 | Cheap to confirm color |
| No data shape given             | realistic placeholder content                | invent plausible, varied content         | No — never lorem ipsum |
| No accessibility ask            | sensible contrast + target sizes             | WCAG AA                                   | No |
| No viewport given               | responsive                                   | desktop + 390px mobile                    | No |
| No light/dark pref              | theme support                                | both, light-first                        | No |

Rule of thumb: **if the repo already decided, you don't get to ask.** Re-asking a
settled decision wastes the user's most limited resource — attention — and erodes
trust that you're paying attention.

---

## Precision techniques

Turn vague intent into decisions you can build against.

**Decompose adjectives into measurable choices.** A fuzzy word is a question in
disguise — replace it with a multiple-choice:
- "clean" → "more whitespace, fewer colors, lighter font weight, or simpler
  layout — which one (or more)?"
- "modern" → "flat + minimal, glassy + depth, or bold editorial type?"
- "professional" → "restrained palette, generous spacing, formal copy, or all
  three?"
- "fun" → "playful color, springy motion, illustration, or casual copy?"
- "premium" → "more whitespace, refined type, subtle motion, or deep/dark palette?"

**Use scales for anything continuous.** A 1–5 slider is faster than prose and
gives you a dial to tune:
- "Minimal ←1···5→ expressive — where are we?"
- "Calm/airy ←1···5→ dense/information-rich?"
- "Safe/conventional ←1···5→ bold/distinctive?"
- "Quiet motion ←1···5→ lively motion?"

**Restate intent back in one sentence, then proceed.** Don't ask "did I get it?"
and wait — assert your read and invite correction without blocking:
> "Got it — a calm, minimal habit tracker for busy parents, Linear-ish structure,
> warm accent, mobile-first, AA. Building two directions now; redirect me if any
> of that's off."

This confirms understanding, surfaces misreads early, and keeps momentum.

**Prefer reaction over specification.** When a choice is hard to articulate,
generate the two plausible options and ask the user to pick the one that feels
right. Choosing is faster and more accurate than describing.

---

## When to stop asking

You almost always have enough sooner than you think. Stop and produce when:

- You can name the **product + primary user + anchor screen**.
- You have **at least one taste signal** (reference, screenshot, or named style)
  OR a clear product-type default to lean on.
- You know the **one hard constraint** (or confirmed there is none).
- Further questions would only refine details that critique will surface anyway.

Conversely, keep asking only when a missing answer would make you **build the
wrong thing** (wrong platform, wrong user, a constraint you'd violate) — not when
it would merely make it slightly less tuned.

**Bias hard toward generating.** Once the bar above is met, move to
[`parallel-brainstorm.md`](./parallel-brainstorm.md): produce 2–3 distinct
directions and let the user critique real pixels. A concrete option is worth ten
clarifying questions — people are far better at reacting than at specifying.
Treat the first output as a question in itself: "here are two reads of your idea
— which is closer, and what's wrong?" Then refine against that, not against more
upfront interrogation.

Remember the goal: idea → screen, fast. Questions serve that goal. The moment
they stop accelerating it, stop asking and start building.
