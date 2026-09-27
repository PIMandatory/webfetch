# Web fetch / scraping — landscape & protocol

> Verified **2026-09-27** (tool versions from PyPI / npm / GitHub APIs; behaviour
> tested on this machine). Sources: pypi.org, registry.npmjs.org, api.github.com.

## Goal

A reliable way to fetch and extract readable content (markdown / text) from
arbitrary web pages for research and purchase decisions, including sites with
basic anti-bot protection.

## The escalation tiers

### T0 — Built-in / zero-install readers
- `curl` / `wget` — raw fetch.
- `uvx trafilatura -u URL --markdown` — clean article text, ephemeral env, no install. ✅ tested.
- `yt-dlp` (installed) — video / social metadata + subtitles.
- Hosted reader: `curl https://r.jina.ai/<URL>` — markdown, renders JS, works
  without a key. ✅ tested (≈17 KB on Hacker News).

### T1 — Local workhorse (recommended default)
Pipeline: **`curl_cffi`** (TLS/JA3 impersonation) → **`trafilatura.extract(output_format="markdown")`**.
- `curl_cffi --impersonate chrome` passes many Cloudflare-fronted GETs.
- ✅ OK: wikipedia, lemonde.fr, news.ycombinator.com, arstechnica.com, reddit.com (200).
- ⚠️ g2.com → 403 (hard DataDome/Cloudflare).

### T2 — JS-rendered pages (SPA)
- **Playwright** (python 1.63.0 / npm 1.63.0): headless Chromium, wait for
  network-idle, then extract. Needs `playwright install chromium`.
- Zero-install alternative: `r.jina.ai` (renders server-side).

### T3 — Hard anti-bot (Cloudflare challenge, DataDome, Akamai)
- `curl_cffi` impersonate (sometimes enough for the "managed challenge").
- **FlareSolverr** v3.5.2 — self-hosted HTTP proxy that solves Cloudflare /
  DDoS-Guard challenges (Docker); returns HTML + cookies.
- **Camoufox** 0.5.6 — stealth Firefox (fingerprint-hardened).
- **nodriver** 0.50.3 / **Scrapling** 0.4.15 — stealth automation / all-in-one adaptive scraper.
- `cloudscraper` 1.2.71 — legacy (last release 2023), still fine for simple cases.

### T4 — Managed APIs (paid / freemium)
- **Firecrawl** (`firecrawl-py` 4.44.0) — scrape / crawl / LLM-extract.
- **Jina Reader** (`r.jina.ai`) — free tier; a key raises the limits.
- ScrapingBee / Zyte / Bright Data — residential proxies + unblocking.

## Decision protocol

1. Simple GET with browser headers / `curl_cffi` impersonate → `trafilatura` → markdown.
2. Empty or JS-only → `r.jina.ai`, else Playwright.
3. 403 / challenge → FlareSolverr (or Camoufox / Scrapling).
4. Need search → a search API (SearXNG / Brave / Serper). Raw DuckDuckGo HTML now
   returns 202 (challenge) — avoid.
5. Always: rate-limit, cache, respect `robots.txt`, identify honestly.

## What does NOT work (limits)

- Default `curl` UA → blocked (Reddit / Cloudflare / DDG-html).
- Login-walled / paywalled content (Instagram, LinkedIn, most paid media) — needs
  an authenticated session; ToS / legal grey area.
- Client-rendered SPAs with no server HTML and no reachable API.
- Aggressive per-request challenges on some e-commerce / ticketing sites.
- Raw DuckDuckGo HTML scraping (returns 202).

## Recommended toolkit (target)

`webfetch` CLI (Python; destined for the dotfiles `scripts` Stow package):
- `webfetch URL [--md|--text|--html|--links|--json]`, auto-escalating tiers.
- config `~/.config/webfetch/config.toml`; cache/state `~/.local/state/webfetch/`.
- optional FlareSolverr endpoint.

## Tool versions (verified 2026-09-27)

| Tool | Version | Date |
|---|---|---|
| trafilatura | 2.2.0 | 2026-07-31 |
| curl_cffi | 0.16.3 | 2026-09-02 |
| readability-lxml | 0.9 | 2026-08-27 |
| scrapy | 2.19.0 | 2026-09-10 |
| playwright (py/npm) | 1.63.0 | 2026-09-15 |
| selenium | 4.49.0 | 2026-09-09 |
| nodriver | 0.50.3 | 2026-05-13 |
| camoufox | 0.5.6 | 2026-09-06 |
| scrapling | 0.4.15 | 2026-08-23 |
| cloudscraper | 1.2.71 | 2023-04-25 |
| crawl4ai | 0.9.4 | 2026-09-23 |
| markitdown | 0.1.8 | 2026-09-21 |
| firecrawl-py | 4.44.0 | 2026-09-20 |
| FlareSolverr | v3.5.2 | — |
| puppeteer (npm) | 25.12.0 | — |
