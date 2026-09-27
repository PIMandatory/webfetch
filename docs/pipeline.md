# Pipeline — briques testées & nécessaires

> État au **2026-09-27**. Cas d'usage concret : **recherche produit sur site protégé
> (AliExpress) → candidats → liens validés → specs → décision d'achat**.
> Légende : ✅ testé OK · ⚠️ partiel · ❌ manquant · ➖ non nécessaire (à ce jour).

## La chaîne du besoin

```
recherche produit
  1. TROUVER      → URL de recherche / candidats ........ ← ❌ BRIQUE MANQUANTE (SERP)
  2. FETCH (T1)   → HTML brut ........................... ✅ curl_cffi
  3. EXTRAIRE     → liste structurée (JSON embarqué) .... ✅ parseur dédié (trafilatura ✗)
  4. VALIDER      → liens vivants ....................... ✅ --check  (--render si JS)
  5. RENDRE (T2)  → page produit réelle (JS) ............ ✅ Playwright (isolé)
  6. SPECS        → CPU/RAM/TDP/ports ................... ✅ fiche AliExpress + constructeur
  7. CROISER      → bruit/avis/fiabilité ................ ← ❌ BRIQUE MANQUANTE (SERP/API)
  8. ARCHIVER     → lien mort → snapshot ................ ✅ Wayback (affichage ; récupération à faire)
```

## Table des briques

| # | Brique | Outil | État | Preuve (2026-09-27) | Limite / note |
|---|---|---|---|---|---|
| 1 | Fetch HTTP | `curl_cffi` (impersonate chrome) | ✅ | AliExpress search 714 Ko ; wikipedia, HN, lemonde | ne voit pas le JS (page produit = « browser does not support JS ») |
| 2 | Rendu JS | Playwright `chromium-headless-shell` | ✅ | `quotes.toscrape.com/js/` ; pages produit AliExpress | 266 Mo isolés ; 1 Chromium par requête |
| 3 | Extraction article | `trafilatura` | ⚠️ | parfait sur articles (wikipedia/HN) | **jette les listings/produits** → à réserver aux articles |
| 4 | Extraction liste | parseur JSON embarqué (dédié) | ✅ | ~60 produits/requête (ID, titre, prix, prix 30 j) | spécifique au site |
| 5 | Extraction specs | parseur DOM (`li.specification--line`) | ✅ | fiche Firebat/GMKtec | dépend du layout de la page |
| 6 | Validation liens | `webfetch --check` (+ `--render`) | ✅ | bidon→`SOFT404`, réels→`OK`, reddit→`CHALLENGE`, 404→`DEAD` | T2 requis pour les sites 100 % JS |
| 7 | Anti-bot dur | FlareSolverr (non installé) | ➖ | g2.com → 403 non résolu | pas nécessaire jusqu'ici (AliExpress passe en T1/T2) |
| 8 | Fiches constructeur | fetch direct | ✅ | `gmktec.com` (TDP 15–54 W), `firebatpc.com` (24 Go) | URL à trouver (pas toujours indexée) |
| 9 | **Recherche web** | *aucune* | ❌ | DDG/Bing/Brave bloquent **T1 ET T2** (captcha) ; Jina bloqué | **bloque le croisement avis/bruit et la découverte** |
| 10 | Archive liens morts | Wayback API | ⚠️ | disponibilité OK (affiche le snapshot) | ne **récupère** pas encore le contenu |
| 11 | Cache / throttle | `webfetch --cache`, `sleep` | ⚠️ | cache opt-in implémenté | non stress-testé |

## Ce qu'il manque pour boucler le besoin

- **Brique 9 (recherche)** — le vrai verrou. Sans elle : ni croisement avec des
  tests/avis (donc pas de jugement « bruit/silence »), ni découverte au-delà des
  URLs déjà connues. Options : **SearXNG auto-hébergé** (podman, local, sans clé)
  ou **API** (Brave / Serper / Tavily).
- **Brique 10** — récupérer effectivement le snapshot Wayback (pas seulement l'afficher).
- **Brique 7** — uniquement si un site cible bloque réellement (aucun cas à ce jour).

## Bilan pour le cas mini-pc

| Attendu | État |
|---|---|
| Trouver des candidats | ✅ 8 mini PC (0 AI 7 350 sur AliExpress) |
| Liens garantis vivants | ✅ validés (`--check --render`) |
| Specs (CPU / RAM / TDP) | ✅ GMKtec TDP publié ; Firebat RAM contradictoire (24 vs 32 Go) |
| Bruit / silence | ❌ faute de brique 9 |
