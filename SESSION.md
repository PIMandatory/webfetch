# Session — Récupération web / scraping (webfetch)

> Dernière mise à jour : 2026-09-27.

## En bref (sujets)
- Sujet : outillage fiable de récupération / scraping web pour mes recherches & achats.
- **CLI `webfetch` livré et testé** (PEP 723 via `uv`, paquet Stow `scripts`).
- Pipeline T1 prouvé : `curl_cffi` (impersonation Chrome) + `trafilatura` → markdown.
- Mode **`--check`** : statut, redirections, **soft-404**, **challenge anti-bot**, repli Wayback.
- Lecteur hébergé gratuit `r.jina.ai` opérationnel (rend le JS, sans clé).
- 4 paliers définis (T0 statique → T3 anti-bot → T4 API managées) ; T2 (Playwright) non testé.
- État : code en place ; T2/T3 **planifiés et documentés**, **rien installé** (attente validation).

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
- 2026-09-27 : **rien n'est installé** sans validation ; installs éventuelles **isolées**
  et réversibles (`~/dev/webfetch/.browsers`), jamais dans le système. Plan + registre :
  `docs/install-plan.md`.
- Paysage + protocole : `docs/tooling.md`.

## État / données clés (tests du 2026-09-27)
- **Emplacement** : `~/.local/bin/webfetch` (Stow → `dotfiles-cachyos/scripts/`).
- Marche : T1 markdown/texte/html/links/json ; `--check` (OK / dead 404 / redirect /
  **soft-404** / **challenge** / archive) ; `--from-file` ; cache opt-in.
- Détection validée : Reddit sous-reddit inexistant = **200 « prove your humanity » → challenge** ;
  wikipedia/Shopify 404 → dead ; le monde/Shopfiy 404 OK.
- Bloqués : g2.com (403) ; DDG-html (202).
- Env : Python 3.14.7, uv 0.12.19, Firefox (pas de Chromium) ; curl_cffi déjà installé.
- **Install : RIEN à ce jour.** `podman` rootless présent, `docker` absent, toutes les
  libs Chromium présentes, 722 Go libres. T2 = ~118 Mo (shell headless, isolé en `.browsers`).
- Versions vérifiées (PyPI/npm/GitHub) : trafilatura 2.2.0, curl_cffi 0.16.3,
  playwright 1.63.0, scrapling 0.4.15, FlareSolverr 3.5.2, camoufox 0.5.6, firecrawl-py 4.44.0.

## Fichiers de référence
- `~/.local/bin/webfetch` — le CLI (source : `dotfiles-cachyos/scripts/.local/bin/webfetch`).
- `docs/tooling.md` — paysage des outils, paliers T0–T4, protocole, versions.
- `docs/install-plan.md` — prérequis, tailles, commandes isolées, retrait, registre installs.
- `PITFALLS.md` — pièges de scraping déjà rencontrés.
- `dotfiles-cachyos/scripts/README.md` — usage du CLI (section « webfetch »).

## TODO
- [ ] **Décider T2** : autoriser ou non l'install isolée (~118 Mo) + test sur une SPA.
- [ ] **Décider T3** : FlareSolverr via podman rootless (seulement si T2 insuffisant).
- [ ] Choisir le corpus de test (1 URL par catégorie) et consigner les résultats.
- [ ] Décider d'un repli auto en `--check` (challenge → tentative T2/T3) ?
- [ ] Ajouter une brique « recherche » (SearXNG local ou API) pour remplacer DDG-html.
- [ ] Option `--archive` qui **récupère** le snapshot au lieu de seulement l'afficher.
