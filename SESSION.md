# Session — Récupération web / scraping (webfetch)

> Dernière mise à jour : 2026-09-27.

## En bref (sujets)
- Sujet : outillage fiable de récupération / scraping web pour mes recherches & achats.
- **CLI `webfetch` livré et testé** (PEP 723 via `uv`, paquet Stow `scripts`).
- Pipeline T1 prouvé : `curl_cffi` (impersonation Chrome) + `trafilatura` → markdown.
- Mode **`--check`** : statut, redirections, **soft-404**, **challenge anti-bot**, repli Wayback.
- Lecteur hébergé gratuit `r.jina.ai` opérationnel (rend le JS, sans clé).
- 4 paliers définis (T0 statique → T3 anti-bot → T4 API managées) ; **T2 validé**, T3 écarté (non viable).
- **Brique recherche retenue** : **SearXNG** local (conteneur podman) → `webfetch --search`.
- État : T1 + `--check` + `--check --render` + **`--search`** opérationnels.
- **Version stable `v1.0.0`** figée ; le **cas mini PC** est intégré comme **cas d'usage** (plus un sujet séparé).

## Objectif
Disposer d'une méthode fiable pour récupérer, extraire et **valider** le contenu
lisible de sites (y compris protégés par anti-bot basique) lors des recherches et
des achats — sans confondre un lien vivant avec un lien périmé.

## Décisions actées
- 2026-09-27 : **CLI `webfetch`** retenue (auto-escalade) plutôt qu'une simple recette manuelle.
- 2026-09-27 : cœur = **curl_cffi + trafilatura** (T1) ; escalade uniquement sur échec.
- 2026-09-27 : script **PEP 723** exécuté par `uv` → aucune install système.
- 2026-09-27 : `--check` est un mode de premier ordre (soft-404 + challenge + Wayback).
- 2026-09-27 : privilégier local/gratuit ; API payantes en dernier recours.
- 2026-09-27 : brique **recherche** = **SearXNG** auto-hébergé (podman rootless, sortie JSON) ;
  API (Brave/Serper/Tavily) en alternative. **Scraper les SERP = écarté** (bloqué T1/T2).
- 2026-09-27 : **outil figé en `v1.0.0`** (stable). Le **cas mini PC** devient un
  **cas d'usage inclus** dans ce sujet (`docs/use-cases/`), plus un sujet autonome.
- 2026-09-27 : **rien n'est installé** sans validation ; installs éventuelles **isolées**
  et réversibles (`~/dev/webfetch/.browsers`), jamais dans le système. Plan + registre :
  `docs/install-plan.md`.
- Paysage + protocole : `docs/tooling.md`.

## État / données clés (tests du 2026-09-27)
- **Emplacement** : `~/.local/bin/webfetch` (Stow → `dotfiles-cachyos/scripts/`).
- Marche : T1 markdown/texte/html/links/json ; `--check` (OK / dead 404 / redirect /
  **soft-404** / **challenge** / archive) ; `--check --render` (validation de pages JS,
  ex. liens produit AliExpress) ; `--from-file` ; cache opt-in.
- **Cas d'usage de référence = achat d'un mini PC** (recherche **multi-sources**, inclus dans ce
  sujet) : `docs/use-cases/mini-pc-purchase.md`. **Retenu : Beelink SER9 MAX (AI 7 350, 8C/16T,
  32 Go, 1 029 €, silencieux)** ; Minisforum AI X1 Pro (mode silence 36 dB, 1 249 €) ;
  **à éviter** : GMKtec EVO-X1 / ASUS PN54 (~42–47 dB). **≤ 700 € (NPU assoupli) :
  Minisforum AI X1 — Ryzen 7 260, 32 Go, 699 €** (8C/16T, chambre à vapeur).
- Détection validée : Reddit sous-reddit inexistant = **200 « prove your humanity » → challenge** ;
  wikipedia/Shopify 404 → dead ; le monde/Shopfiy 404 OK.
- Bloqués : g2.com (403) ; DDG-html (202).
- **Install à ce jour** : Playwright `chromium-headless-shell` **266 Mo** dans
  `~/dev/webfetch/.browsers/` (isolé, réversible) — T2 validé sur page JS. Registre : `docs/install-plan.md`.
- **T2 validé** : `quotes.toscrape.com/js/` vide en T1 → restitué en T2. Invocation :
  `uv run --with playwright --script webfetch --render URL` (+ `PLAYWRIGHT_BROWSERS_PATH`).
- **Recherche** : **SearXNG** conteneur `127.0.0.1:8888` (image 93 Mo) ; `webfetch --search` opérationnel.
  A permis de croiser les avis (bruit) et de trouver les tests/revendeurs.
- Env : Python 3.14.7, uv 0.12.19, Firefox (pas de Chromium) ; curl_cffi déjà installé.
- `podman` rootless présent, `docker` absent, toutes les libs Chromium présentes, 722 Go libres.
- Versions vérifiées (PyPI/npm/GitHub) : trafilatura 2.2.0, curl_cffi 0.16.3,
  playwright 1.63.0, scrapling 0.4.15, FlareSolverr 3.5.2, camoufox 0.5.6, firecrawl-py 4.44.0.

## Fichiers de référence
- `~/.local/bin/webfetch` — le CLI (source : `dotfiles-cachyos/scripts/.local/bin/webfetch`).
- `CHANGELOG.md` — histoire du sujet/outil.
- `docs/tooling.md` — paysage des outils, paliers T0–T4, protocole, versions.
- `docs/pipeline.md` — **état des briques** (testées/nécessaires) pour le cas d'usage réel.
- `docs/install-plan.md` — prérequis, tailles, commandes isolées, retrait, registre installs.
- `docs/use-cases/mini-pc-purchase.md` — **cas d'usage de référence** (achat mini PC, multi-sources).
- `examples/aliexpress_search.py` — exemple d'extraction d'un listing (prototype promu).
- `PITFALLS.md` — pièges de scraping déjà rencontrés.
- `dotfiles-cachyos/scripts/README.md` — usage du CLI (section « webfetch »).

## TODO
- [x] **Recherche mini-pc** via le prototype (filtres CPU/RAM) → 8 candidats, liens validés (2026-09-27).
- [ ] **Décider** : formaliser l'adaptateur AliExpress dans `webfetch` ou garder en script séparé.
- [ ] **Décider T3** : FlareSolverr via podman rootless (seulement si T2 insuffisant).
- [ ] Si T2 devient courant : intégrer `playwright` aux deps + `browsers_path` en config.
- [x] Brique **recherche** (SearXNG local) intégrée : `webfetch --search` (2026-09-27).
- [ ] Option `--archive` qui **récupère** le snapshot au lieu de seulement l'afficher.
- [ ] **Décider** : formaliser l'adaptateur AliExpress (`--products`) ou garder en script séparé.
