# Session — Récupération web / scraping (webfetch)

> Dernière mise à jour : 2026-09-27.

## En bref (sujets)
- Sujet : outillage fiable de récupération / scraping web pour mes recherches & achats.
- **CLI `webfetch`** (PEP 723/`uv`, paquet Stow `scripts`) — version **`1.1.0`**.
- Modes : extraction (markdown / texte / html / links / json), **`--check`** (+ **`--render`**),
  **`--search`** (+ `--engines`).
- Paliers : T1 (`curl_cffi` + `trafilatura`), T2 (Playwright), recherche (**SearXNG** local).
- **Cas d'usage inclus** : achat mini PC → `docs/use-cases/mini-pc-purchase.md` (plus un sujet à part).
- Mur budgétaire : **pénurie DDR5 2026** → un 32 Go de marque connue, en UE, ≈ **800–960 €**.
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
- **CLI** : `~/.local/bin/webfetch` (source `dotfiles-cachyos/scripts/`), `--version` = `1.1.0`.
- **Invocations** : T2 = `uv run --with playwright --script webfetch --render URL`
  (+ `PLAYWRIGHT_BROWSERS_PATH`) ; recherche = `webfetch --search "…" [--engines google,bing]`.
- **Installs isolées** : Playwright headless-shell **266 Mo** (`.browsers/`) ;
  SearXNG en conteneur **93 Mo** (`127.0.0.1:8888`, config `.searxng/`).
- **SearXNG** : les moteurs **s'auto-suspendent ~180 s** après une rafale (DDG reste en captcha
  plus longtemps) → `--engines` pour router autour d'un moteur bloqué.
- **Cas mini PC** (`docs/use-cases/mini-pc-purchase.md`) :
  - Marque connue + UE + 32 Go : **GMKtec K8 Plus 799,95 €** (LDLC, en stock) ;
    **Beelink SER8 32 Go 959 €** (`eu.bee-link.com`).
  - **Aucun 8C/16T + 32 Go ≤ 700 €** (marque connue, sans douane) — mur = **prix de la RAM**.
  - Invalidés après vérif utilisateur : **Geekom A6** (16 Go only), **Ninkear** (marque inconnue/16 Go),
    **Minisforum AI X1** (hors UE → douane).
- Bloqués : g2.com (403) ; DDG-html (202) ; Darty/Amazon (403/captcha).
- Env : Python 3.14.7, uv 0.12.19, podman rootless (docker absent), 722 Go libres.
- Versions outils (vérif. 2026-09-27) : trafilatura 2.2.0, curl_cffi 0.16.3, playwright 1.63.0,
  scrapling 0.4.15, FlareSolverr 3.5.2, camoufox 0.5.6, firecrawl-py 4.44.0.

## Fichiers de référence
- `~/.local/bin/webfetch` — le CLI (source : `dotfiles-cachyos/scripts/.local/bin/webfetch`).
- `CHANGELOG.md` — histoire du sujet/outil.
- `docs/tooling.md` — paysage des outils, paliers T0–T4, protocole, versions.
- `docs/pipeline.md` — **état des briques** (testées/nécessaires).
- `docs/install-plan.md` — prérequis, tailles, commandes isolées, retrait, registre installs.
- `docs/use-cases/mini-pc-purchase.md` — **cas d'usage de référence** (achat mini PC, multi-sources).
- `examples/aliexpress_search.py` — exemple d'extraction d'un listing.
- `PITFALLS.md` — pièges de scraping déjà rencontrés.
- `dotfiles-cachyos/scripts/README.md` — usage du CLI (section « webfetch »).

## TODO
- [ ] **Reprendre la recherche** : 3 modèles 32 Go (boutique officielle **AliExpress**, **entrepôt EU**)
  **ou** un modèle précis (Beelink SER8 / GMKtec K8 Plus / Minisforum UM890 Pro).
- [ ] **Vérifier les marques** (Ninkear / Trigkey / AOOSTAR / BOSGAME…) si on élargit au-delà de Beelink/GMKtec/Minisforum.
- [ ] **Décider** : formaliser l'adaptateur AliExpress (`--products`) dans `webfetch` ou garder en script.
- [ ] **Décider T3** (FlareSolverr via podman) — seulement si un site l'exige.
- [ ] `--archive` : **récupérer** le snapshot, pas seulement l'afficher.
- [ ] Si T2 devient courant : `playwright` en dépendance + `browsers_path` en config.
