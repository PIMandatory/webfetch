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

## Bruit — mesures croisées (décisif)

| Modèle | Repos | Charge | Note |
|---|---|---|---|
| **Beelink SER9 MAX** | ~32 dB (Beelink) | continu, **sans pics** ; « quasi inaudible » | chambre à vapeur MSC 2.0 → **le plus silencieux** |
| Minisforum AI X1 Pro | 28 dB | 38,4–41,8 dB (**mode Silence : 36,1 dB**) | correct, profil réglable au BIOS |
| GMKtec EVO-X1 | 27,8–30,4 dB | **44,6–46,1 dB** | **bruyant** |
| ASUS PN54 | 25 dB | **42,6–47,1 dB** | **bruyant** en charge |

*(notebookcheck, 15 cm ; SER9 MAX qualitatif via minipc-review/Beelink.)*

## Conclusion

- **8C/16T strict + 32 Go + silencieux** : **Beelink SER9 MAX (AI 7 350, 1 029 €)** — meilleur profil, gagne sur le bruit.
- **Plus de cœurs (12C/24T), silencieux en mode BIOS** : Minisforum AI X1 Pro (mode Silence 36 dB, 1 249 €).
- **À éviter (bruit)** : GMKtec EVO-X1 (LDLC 1 200 €) et ASUS PN54 (~42–47 dB).
- Reste à confirmer : **prix/dispo FR + garantie** du SER9 MAX.

## Reproduire

```sh
webfetch --search "mini pc ryzen ai 9 365 32 go France prix"
# prix/stock d'une boutique Shopify :
webfetch --html "https://minisforumpc.fr/products/minisforum-ai-x1.json" | jq -r '.product.variants[] | "\(.title) -> \(.price)"'
# prix LDLC (JSON-LD) :
webfetch --html "https://www.ldlc.com/fiche/PB00707684.html" | grep -o '"price"[^,]*'
```
