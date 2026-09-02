# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A speculative pitch preview — an unsolicited concept redesign built by Upscale
Qatar to win the club's business. It is not commissioned work and is not
affiliated with the club; every page carries that disclaimer in the footer, and
it must stay there.

Single-page static site. Plain HTML/CSS/vanilla JS, no build step, no
dependencies, no tests, no linter. `index.html` is fully self-contained: inline
`<style>` and one inline IIFE `<script>`.

## Two brandings, one per branch

| Branch | Branding | Location copy |
| --- | --- | --- |
| `main` | **The Dome Padel Club** — the real, named client | Qatar Foundation, Ar-Rayyan, plus a live Google Maps link to the venue |
| `padel-club-doha` | **Padel Club Doha** — anonymized replica | generic "Doha", no Qatar Foundation, no maps query |

`padel-club-doha` is a straight rebrand of the same site (commit `018d5f3`),
reverted off `main` by `2ad7a1f`. Use it when the site needs to be shown without
naming the real business.

Consequence when editing: branding strings differ between the two branches, so
`tools/make-ar.py` differs too. A copy change cherry-picked across branches will
fail the Arabic build with `expected N hit(s), found M` until the corresponding
`sub()` is retargeted to that branch's wording.

**`main` is what the public sees**, under the real club's name and address — see
Deploy below.

## Commands

```bash
python3 tools/make-ar.py       # regenerate ar/index.html — REQUIRED after any index.html edit
python3 -m http.server 8000    # local preview; must be HTTP, not file:// (the hero fetches video bytes)
```

## The Arabic page is generated

`ar/index.html` is built from `index.html` by `tools/make-ar.py`. **Never
hand-edit `ar/index.html`** — it will be overwritten.

The script is a list of `sub(old, new, n)` string swaps, each asserting an exact
hit count. So:

- Editing any English string that `make-ar.py` substitutes breaks the build with
  `expected N hit(s), found M`. Update the corresponding `sub()` call in
  `tools/make-ar.py` in the same change.
- Adding new user-visible copy to `index.html` means adding a matching `sub()`,
  or the Arabic page ships English text.
- Three post-build assertions also fail the script: exactly two
  `letter-spacing` rules may survive (the `dir="ltr"` wordmark and the English
  language toggle — tracking breaks Arabic cursive joining), those two elements
  must still exist verbatim, and no `Archivo` / `IBM+Plex+Mono` / `font-stretch`
  tokens may remain.
- Asset paths shift one level up on the Arabic page (`assets/…` →
  `../assets/…`); the script handles the known ones. New asset references need
  their own swap.

Use logical CSS properties (`inline-size`, `inset-inline-start`, `padding-inline`)
throughout — the whole stylesheet is direction-neutral so RTL needs almost no
overrides. Only a handful of rules in `make-ar.py` are direction-specific.

## The hero scrub, and its triplicated device gates

The hero video scrubs frame-by-frame with scroll position. Two cuts exist:

- `assets/hero.mp4` — landscape, ~5s, ~5.5MB
- `assets/hero-mobile-tall.mp4` — portrait, ~4s, ~2MB

Which cut loads is decided by **four device gates that appear in three places and
must match character for character**:

1. The `@media` block in `<style>` (`.hero{--hero-vh:300}` and band layout)
2. The first `<source media="…">` inside the hero `<picture>`
3. The `DEVICE_GATES` array in the JS

`prefers-reduced-motion: reduce` is held separately and is the **only** gate that
means "no video at all" — a phone that asked for less motion loses the scrub
rather than gaining a smaller one.

Other load-bearing details in that IIFE:

- Video is fetched as a **blob**, not streamed. Many static hosts answer Range
  requests with the whole file, which clamps every seek to zero. There is a
  3000ms `LOAD_BUDGET_MS`; past that the fetch aborts and the poster still is
  what the session gets — the page is complete without the video.
- Blobs are cached per-URL for the session so rotating a tablet reattaches
  rather than refetches.
- Seeks are gated by `seekBusy`/`pending` because a seek to the current head
  never fires `seeked` and would deadlock the queue.
- Hero scroll runway is `--hero-vh`: 600 desktop, 300 mobile.

## Events

To add, change, or remove an event, edit **only** the JSON array in
`<script type="application/json" id="events-data">` near the top of `<body>`.
An empty array (`[]`) removes the Events section and its nav link automatically.
Events must be added to both `index.html` and (via a `make-ar.py` swap) the
Arabic page, or they show in one language only.

Section eyebrow numbers (`01 /`, `02 /`, …) are renumbered at runtime over
non-hidden sections. Do not hardcode them — with an empty events array they
would otherwise read 04, 06, 07.

## Deploy

Served by **GitHub Pages from `main`** at
`https://abdallahdarwazeh.github.io/TheDome/`. On a free GitHub account Pages
only publishes from a public repo, so **making this repo private takes the live
site down** — which matters while the pitch is in front of the client. The
tradeoff is that the concept sits publicly under the real club's name and
location; the footer disclaimer is the mitigation.

The path prefix `/TheDome/` is hardcoded in `hreflang` links, `og:url`, and the
language toggle in both pages and in `make-ar.py`. Consequence: served from a
plain localhost root, the language toggle and footer language links 404 — that
is expected locally, not a bug to "fix".

### The legacy-URL redirects are not live

`vercel.json` declares permanent (301) redirects preserving the old site's URLs
— `/our-academy`, `/about-us`, `/events-page`, `/events`, `/contact` → the
matching hash anchors — plus `cleanUrls` and a long cache on `/assets/*`.

**None of it runs on the current deploy.** GitHub Pages never reads
`vercel.json`; it is a static file host with no redirect engine, and `main`
carries no `404.html`, no `_redirects`, and no per-path stub pages. Today
`…/TheDome/about-us` returns a plain Pages 404, not a redirect.

So the redirects are a design intent staged for a Vercel deploy, not a working
feature — do not describe them to the client as live without testing them. To
actually preserve those URLs on Pages, either revive Vercel hosting or add a
`404.html` that maps the legacy path to its anchor client-side.

## Not part of the site

`app.js`, `10k-websites/`, and `.DS_Store` are gitignored scratch and must stay
out of the repo — it is public. `app.js` is an unrelated
product-search demo carrying a fake hardcoded API key — do not ship it or treat
it as site code. `10k-websites/` is an extracted skill bundle (reference docs
for the cinematic-site workflow, including ffmpeg recipes for regenerating the
hero cuts).
