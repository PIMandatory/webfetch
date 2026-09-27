# Use case — achat d'un mini PC (recherche multi-sources)

> **Cas d'usage de référence de `webfetch`** : trouver un mini PC, **garantir des liens
> vivants**, récupérer les specs, **croiser avec des tests**, comparer les revendeurs et
> décider. Recherche **étendue hors AliExpress** (mise à jour **2026-09-27**).

## Besoin

Mini PC **8C/16T, 32 Go**, charge CPU/mémoire — **frais, silencieux, NPU ≥ 40 TOPS** (Copilot+).

## Bricks utilisées

| Étape | Brique | Outil |
|---|---|---|
| Chercher | recherche multi-sources | **SearXNG** (`webfetch --search`) |
| Lister (AliExpress) | fetch + extraction liste | `examples/aliexpress_search.py` |
| Valider | liens vivants | `webfetch --check --render` |
| Spécifier | fiche + constructeur + **API Shopify `.json`** | `webfetch --text/--html` |
| Prix/dispo | JSON-LD / boutique `.json` | `webfetch --html` + `jq` |
| Croiser | bruit/avis | `webfetch --search` + fetch |

## Profil idéal (8C/16T) — disponible ✅

| Modèle | CPU | Config | Prix | Source |
|---|---|---|---|---|
| **Beelink SER9 MAX** | **Ryzen AI 7 H 350** (8C/16T, NPU 50 TOPS, Radeon 860M) | **32 Go + 1 To** | **1 029 €** | `bee-link.com/fr` |
| Beelink SER9 MAX | idem | 64 Go + 1 To | 1 369 € | `bee-link.com/fr` |
| ASUS ExpertCenter PN54 | **Ryzen AI 7 350** (cTDP 40 W) | 32 Go max (2×16), barebone/pro | à confirmer | `asus.com/fr` |

> Le SER9 MAX est le **seul profil strict 8C/16T + 32 Go + NPU 50 TOPS en stock** trouvé.

## Strix Point 12C/24T (plus de cœurs que le besoin)

| Modèle | CPU | Config | Prix | Source / dispo |
|---|---|---|---|---|
| **Minisforum AI X1** | AI 9 HX 370 | 32 Go + 1 To | **1 139 €** (barebone 699 €) | `minisforumpc.fr` — en stock |
| **Minisforum AI X1 Pro-370** | AI 9 HX 370 | 32 Go + 1 To | **1 249 €** | `minisforumpc.fr` — en stock |
| **GMKtec EVO-X1** | AI 9 HX 370 | 32 Go + 1 To | **1 199,95 €** | **LDLC — en stock** |
| Minisforum EliteMini AI370 | AI 9 HX 370 | — | ~949 € | (presse) |
| ACEMAGIC F3A | AI 9 HX 370 | — | 614 € (promo) | (presse) |
| Geekom A9 Max | AI 9 HX 470 | — | 1 699–1 999 € | `geekom.fr` |

## AI 9 365 (10C/20T) et Lunar Lake

| Modèle | CPU | Config | Prix | Source |
|---|---|---|---|---|
| MINIX Elite ER936-AI | **AI 9 365** | 32 Go | Amazon.fr | en stock |
| Firebat A8 | AI 9 365 (RAM SODIMM extensible) | 32 Go + 1 To | 1 009 € (AliExpress) | AliExpress / Amazon.fr |
| CHUWI AuBox X | Ultra 7 256V (Lunar Lake) | 16 Go | 762 € | AliExpress |

## Bruit (décisif, via recherche)

- **GMKtec EVO-X1** : « point faible », **≈ 45 dB(A) en charge** (notebookcheck) → **écarté** pour « silencieux ».
- **Firebat A8** : double ventilateur + 3 caloducs, « discret en usage courant » (pas de dB).
- **Minisforum AI X1** : refroidissement annoncé « grand ventilateur silencieux », 65 W.
- Beelink/ASUS/Geekom : **à confirmer** (pas encore de mesures croisées).

## Conclusion (provisoire)

- **8C/16T strict + 32 Go + NPU** : **Beelink SER9 MAX (AI 7 H 350, 1 029 €)** — meilleur profil disponible.
- **12C/24T silencieux à vérifier** : Minisforum AI X1 (1 139 €), GMKtec EVO-X1 (LDLC 1 200 €, mais **bruyant**).
- Reste à **croiser le bruit** du SER9 MAX et confirmer prix/dispo FR + garantie.

## Reproduire

```sh
webfetch --search "mini pc ryzen ai 9 365 32 go France prix"
# prix/stock d'une boutique Shopify :
webfetch --html "https://minisforumpc.fr/products/minisforum-ai-x1.json" | jq -r '.product.variants[] | "\(.title) -> \(.price)"'
# prix LDLC (JSON-LD) :
webfetch --html "https://www.ldlc.com/fiche/PB00707684.html" | grep -o '"price"[^,]*'
```
