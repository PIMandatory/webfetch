# Session — Récupération web / scraping (webfetch)

> Dernière mise à jour : 2026-09-27.

## En bref (sujets)
- Nouveau sujet : outillage de récupération / scraping web pour mes recherches & achats.
- Constat de départ : rien d'intégré de fiable → besoin d'une méthode éprouvée.
- Pipeline T1 **prouvé localement** : `curl_cffi` (impersonation Chrome) + `trafilatura` → markdown.
- Lecteur hébergé gratuit `r.jina.ai` opérationnel (rend le JS, sans clé).
- 4 paliers définis : statique → JS → anti-bot → API managées.
- État : **étude** (pas un projet), git local, tag de jalon, pas de remote.
- Livrable visé : CLI `webfetch` (auto-escalade), à terme dans le paquet Stow `scripts`.

## Objectif
Disposer d'une méthode fiable pour récupérer et extraire le contenu lisible de sites
(y compris protégés par anti-bot basique) lors des recherches et des achats.

## Décisions actées
- 2026-09-27 : traiter comme **étude** (`~/dev/webfetch/`) — git local, tag de jalon, pas de remote.
- 2026-09-27 : cœur = **curl_cffi + trafilatura** (T1) ; escalade uniquement en cas d'échec.
- 2026-09-27 : privilégier les solutions locales/gratuites ; API payantes en dernier recours.
- Paysage + protocole de décision : `docs/tooling.md`.

## État / données clés (tests du 2026-09-27)
- En ligne OK. Python 3.14.7, uv 0.12.19, node 26 / npm 12, deno 2.9, Firefox (pas de Chromium).
- Déjà présents : requests, bs4, lxml, **curl_cffi**, jq, yt-dlp, curl/wget.
- T1 OK : wikipedia, lemonde, Hacker News, arstechnica, reddit.
- Bloqués : g2.com (403) ; DDG-html (202).
- `r.jina.ai` : contenu réel (≈17 Ko sur HN).
- Versions vérifiées (PyPI/npm/GitHub) : trafilatura 2.2.0, curl_cffi 0.16.3, playwright 1.63.0,
  scrapling 0.4.15, FlareSolverr 3.5.2, camoufox 0.5.6, firecrawl-py 4.44.0.

## Fichiers de référence
- `docs/tooling.md` — paysage des outils, paliers T0–T4, protocole, versions.
- `PITFALLS.md` — pièges de scraping déjà rencontrés.
- (à venir) `README.md` — usage de la CLI `webfetch` si on la construit.

## TODO
- [ ] Valider le périmètre : CLI robuste vs simple recette documentée.
- [ ] Tester T2 (Playwright) sur une SPA réelle.
- [ ] Tester T3 (FlareSolverr via Docker) sur g2.com ou équivalent.
- [ ] Décider où vit le code (paquet Stow `scripts`) et le nom (`webfetch`).
- [ ] Ajouter une brique « recherche » (SearXNG local ou API).
