# Session — Récupération web / scraping (webfetch)

> Dernière mise à jour : 2026-09-28.
>
> **Projet** (git + remote GitHub `PIMandatory/webfetch`). Le CLI est un **outil durable** ;
> **SearXNG est géré automatiquement en one-shot** (démarré/arrêté par `webfetch --search`, arrêté hors usage).
> **Versionnage** : le **tag git = la version de l'outil** (`webfetch --version`).

## En bref (sujets)
- **Projet** : outillage fiable de récupération / scraping web pour mes recherches & achats.
- **CLI `webfetch`** (PEP 723/`uv`, paquet Stow `scripts`) — version **`2.0.0`**.
- Modes : extraction (markdown / texte / html / links / json), **`--check`** (+ **`--render`**),
  **`--search`** (+ `--engines`).
- Paliers : T1 (`curl_cffi` + `trafilatura`), T2 (Playwright), recherche (**SearXNG** local).
- **Cas d'usage inclus** (tous deux **clos**) : mini PC → `docs/use-cases/mini-pc-purchase.md` ;
  **Realme GT7** → `docs/use-cases/realme-gt7.md` (**promo AliExpress ~370 €**).
- État : outil stable ; installs **isolées** (Playwright, SearXNG) ; docs à jour.

## Objectif
Méthode fiable pour récupérer, extraire et **valider** le contenu de sites (y compris
protégés par anti-bot basique) lors des recherches et des achats — sans confondre un
lien vivant avec un lien périmé.

## Décisions actées
- 2026-09-27 : **CLI `webfetch`** retenue ; cœur = **curl_cffi + trafilatura** (T1) ;
  script **PEP 723** exécuté par `uv` (aucune install système).
- 2026-09-27 : `--check` = mode de premier ordre (soft-404 + challenge + Wayback) ;
  `--check --render` pour les pages JS.
- 2026-09-27 : recherche = **SearXNG** auto-hébergé (podman rootless, JSON) ;
  **scraper les SERP = écarté** (bloqué T1/T2). API (Brave/Serper/Tavily) en alternative.
- 2026-09-27 : installs **isolées et réversibles** uniquement ; registre `docs/install-plan.md`.
- 2026-09-27 : **cas mini PC = cas d'usage inclus** (`docs/use-cases/`), plus un sujet autonome.
- 2026-09-27 : seuil réaliste — en **marque connue + UE + 32 Go**, plancher ≈ **800 €**.

## État / données clés (2026-09-27)
- **CLI** : `~/.local/bin/webfetch` (source `~/dev/dotfiles-cachyos/scripts/`), `--version` = `2.0.0`.
- **Invocations** : T2 = `uv run --with playwright --script webfetch --render URL`
  (+ `PLAYWRIGHT_BROWSERS_PATH`) ; recherche = `webfetch --search "…" [--engines google,bing]`
  (**one-shot** : démarre/arrête SearXNG ; `--no-autostart` pour gérer à la main).
- **Installs isolées** : Playwright headless-shell **266 Mo** (`.browsers/`) ;
  SearXNG en conteneur **93 Mo** (`127.0.0.1:8888`, config `.searxng/`).
- **SearXNG** : les moteurs **s'auto-suspendent ~180 s** après une rafale (DDG reste en captcha
  plus longtemps) → `--engines` pour router autour d'un moteur bloqué.
- **Cas mini PC** : **clos** — 32 Go ≤700 € sans douane = **intenable** (pénurie DDR5).
  Détails, candidats écartés et verdicts marques : `docs/use-cases/mini-pc-purchase.md`.
- Bloqués : g2.com (403) ; DDG-html (202) ; Darty/Amazon (403/captcha).
- Env : Python 3.14.7, uv 0.12.19, podman rootless (docker absent), 722 Go libres.
- Versions outils (vérif. 2026-09-27) : table dans `docs/tooling.md`.

## Fichiers de référence
- `~/.local/bin/webfetch` — le CLI (source : `~/dev/dotfiles-cachyos/scripts/.local/bin/webfetch`).
- `CHANGELOG.md` — histoire du sujet/outil.
- `docs/tooling.md` — paysage des outils, paliers T0–T4, protocole, versions.
- `docs/pipeline.md` — **état des briques** (testées/nécessaires).
- `docs/install-plan.md` — prérequis, tailles, commandes isolées, retrait, registre installs.
- `docs/use-cases/mini-pc-purchase.md` — **cas d'usage** achat mini PC, multi-sources (clos).
- `docs/use-cases/realme-gt7.md` — **cas d'usage** achat Realme GT7 (12 Go), **clos/archivé**.
- `examples/aliexpress_search.py` — exemple d'extraction d'un listing.
- `PITFALLS.md` — pièges de scraping déjà rencontrés.
- `~/dev/dotfiles-cachyos/scripts/README.md` — usage du CLI (section « webfetch »).

## TODO
- [x] **Realme GT7** : **clos/archivé** — promo **AliExpress ~370 €** (offre 402 € + **promo panier**).
- [x] **mini PC** : **clos** — 32 Go ≤700 € sans douane **intenable** (pénurie DDR5). Reprendre si la RAM baisse.
- [ ] **Décider** : formaliser l'adaptateur AliExpress (`--products`) dans `webfetch` ou garder en script.
- [ ] **Décider T3** (FlareSolverr via podman) — seulement si un site l'exige.
- [ ] `--archive` : **récupérer** le snapshot, pas seulement l'afficher.
- [ ] Si T2 devient courant : `playwright` en dépendance + `browsers_path` en config.
