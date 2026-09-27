# Changelog — webfetch

> History of the `webfetch` subject (tool + study). Newest first.

## [1.2.0] — 2026-09-27

- **Reclassified as a project** (durable tool; GitHub `PIMandatory/webfetch`).
- `--search`: **auto one-shot SearXNG** — starts the container if stopped, runs the query,
  then stops it (options `--searxng-container`, `--no-autostart`). `--version` → `1.2.0`.

## [1.1.0] — 2026-09-27

- `--search`: added **`--engines`** (route around throttled SearXNG engines; config
  key `searxng_engines`). `--version` now reports `1.1.0`.
- **Use cases** (product research):
  - `docs/use-cases/mini-pc-purchase.md` — mini-PC, multi-source (**closed**: 32 GB ≤700 €
    impossible in the 2026 DDR5 shortage); brand verdicts, seller checks.
  - `docs/use-cases/realme-gt7.md` — Realme GT7 (12 GB) price research (**in progress**).
  - Documented the **2026 DDR5 shortage** price wall and the **“HTTP 200 ≠ purchasable”** pitfall.

## [1.0.0] — 2026-09-27 — stable

First stable release.

- **`webfetch` CLI** (self-contained PEP 723 script run by `uv`, no system install):
  - default = extract main article to **markdown**; `--text`, `--html`, `--links`, `--json`;
  - `--check` = link health (status, redirect chain, **soft-404**, anti-bot **challenge**,
    `--archive` Wayback fallback); same-path redirect counts as `OK`; non-zero exit if bad;
  - `--check --render` = validate JS-only pages (e.g. AliExpress item links);
  - `--search` = web search via a local **SearXNG** (`--searxng URL`, `--json`);
  - `--cache` (opt-in), config `~/.config/webfetch/config.toml`, `--version`.
- **Bricks validated end-to-end**: `search → fetch → validate → specs → cross-check → decide`.
- Docs: `docs/tooling.md` (landscape), `docs/pipeline.md` (bricks), `docs/install-plan.md`
  (isolated installs + registry), `PITFALLS.md`, `docs/use-cases/`.

## [0.8.0] — 2026-09-27 — search brick

- Added local **SearXNG** (podman rootless, JSON) + `webfetch --search`.
- Pipeline/install docs updated.

## [0.5.0] — 2026-09-27 — JS link validation

- `--check --render`; soft-404 marker for JS-only missing pages; same-path redirect = `OK`.

## [0.4.0] — 2026-09-27 — rendering (T2)

- Isolated Playwright `chromium-headless-shell` in `.browsers/`; validated on a JS page.

## [0.2.0] — 2026-09-27 — CLI

- First `webfetch`: T1 pipeline (`curl_cffi` + `trafilatura`) + link-health `--check`.

## [0.1.0] — 2026-09-27 — study

- Initial study: tool landscape (tiers T0–T4), tested pipeline, protocol.
