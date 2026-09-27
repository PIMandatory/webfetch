# Pipeline — briques viables & outils conseillés

> État au **2026-09-27**. Cas d'usage : **recherche produit sur site protégé (AliExpress)
> → candidats → liens validés → specs → décision d'achat**.
> Objectif : ne garder que les **briques viables**, avec pour chacune l'**outil conseillé**,
> **pour quel usage**, et les **alternatives viables**. ✅ = testé en vrai.

## La chaîne (briques retenues)

```
recherche produit
  1. TROUVER    → candidats / URL de recherche ......... SearXNG (local)
  2. FETCH      → HTML brut ............................. curl_cffi
  3. RENDRE JS  → page dynamique ........................ Playwright
  4. EXTRAIRE   → article | liste | specs ............... trafilatura | parseur
  5. VALIDER    → lien vivant / mort .................... --check
  6. SPECS OFF. → fiche constructeur .................... fetch direct
  7. ARCHIVER   → lien mort → snapshot .................. Wayback
```

## Briques retenues — outil conseillé & alternatives

| Brique | Pour quoi | Outil conseillé | Alternatives viables | ✅ testé |
|---|---|---|---|---|
| **Fetch HTTP** | récupérer le HTML, sites légers/protégés basiques | **`curl_cffi`** (`--impersonate chrome`) | `httpx`, `requests`, `r.jina.ai` (lecteur hébergé) | ✅ |
| **Rendu JS** | pages dynamiques (SPA, fiche produit JS) | **Playwright** `chromium-headless-shell` | **Camoufox** (furtif), `r.jina.ai` (rendu côté serveur, zéro install) | ✅ |
| **Extraction article** | blog / presse / doc → texte propre | **`trafilatura`** | `readability-lxml`, `markitdown` (Microsoft) | ✅ |
| **Extraction liste/specs** | produits, prix, grille de specs | **parseur dédié** (JSON embarqué / DOM) | `Crawlee`, `Scrapy` (volumineux), `Playwright.evaluate` | ✅ |
| **Validation de liens** | « vivant » vs « mort / périmé » | **`webfetch --check`** (+ `--render` si JS) | `lychee`, `muffet`, `linkchecker` (CLI génériques) | ✅ |
| **Recherche / croisement** | trouver, recouper avis/bruit | **SearXNG** auto-hébergé (local, conteneur) | **API** Brave/Serper, `Tavily`, `Exa` | ✅ |
| **Fiches constructeur** | specs officielles (TDP, RAM) | **fetch direct** (`curl_cffi`) | `r.jina.ai`, sitemap produit | ✅ |
| **Archive** | récupérer un lien mort | **Wayback Machine API** | `archive.today` | ✅ (affichage) |

## Écartées — contraintes non viables

| Brique / outil | Pourquoi écarté |
|---|---|
| **Scraping direct des SERP** (DuckDuckGo / Bing / Brave) | bloqué en **T1 ET T2** (captcha) → aucun résultat fiable, ni en HTTP ni en rendu |
| **FlareSolverr** (anti-bot dur) | **course permanente** anti-bot + conteneur à maintenir, pour un seul cas (g2.com) → non viable en perso. *À garder « en réserve » uniquement si un site précis l'exige.* |

> Note : `trafilatura` n'est **pas** écarté, mais **restreint aux articles** — pas aux
> pages de liste (il en jette le contenu).

## Bilan pour le cas mini-pc

| Attendu | État |
|---|---|
| Trouver des candidats | ✅ 8 mini PC (0 AI 7 350 sur AliExpress) |
| Liens garantis vivants | ✅ validés (`--check --render`) |
| Specs (CPU / RAM / TDP) | ✅ GMKtec TDP 15–54 W ; Firebat RAM = SODIMM extensible (24/32/64 Go) |
| Bruit / silence | ✅ via recherche : **EVO-X1 ≈ 45 dB(A) en charge (bruyant)** ; Firebat A8 discret |
