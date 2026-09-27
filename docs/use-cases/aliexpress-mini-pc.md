# Use case — recherche mini PC sur AliExpress (2026-09-27)

> **Cas d'usage de référence de `webfetch`** : acheter un mini PC sur un site protégé,
> trouver des candidats, **garantir des liens vivants**, récupérer les specs, **croiser
> avec des tests** et décider. Ce cas a servi à valider toute la chaîne de briques.

## Besoin

Mini PC **8C/16T, 32 Go**, charge CPU/mémoire — **frais, silencieux, NPU ≥ 40 TOPS** (Copilot+).
Pistes : AMD Ryzen AI 7 350 / AI 9 365 (Strix Point) ou Intel Core Ultra 7 256V/258V (Lunar Lake).

## Bricks utilisées

| Étape | Brique | Outil |
|---|---|---|
| Chercher | recherche | **SearXNG** (`webfetch --search`) |
| Lister | fetch + extraction liste | `curl_cffi` + `examples/aliexpress_search.py` |
| Valider | liens vivants | `webfetch --check --render` |
| Spécifier | fetch fiche + constructeur | `webfetch --text/--html` |
| Croiser | bruit/avis | `webfetch --search` + fetch |

## Candidats retenus (liens vérifiés vivants)

| Prix | Modèle | CPU | RAM | NPU |
|---|---|---|---|---|
| 762 € | CHUWI AuBox X | Ultra 7 **256V** (Lunar Lake) | 16 Go | 47 TOPS |
| 800 € | MINISFORUM X1-470 | **AI 9 HX470** | ? | 86 TOPS |
| 1 009 € | **Firebat A8** | **AI 9 365** | **32 Go** (SODIMM) | 50 TOPS |
| 1 011 € | **GMKtec EVO-X1** | **AI 9 HX 370** | **32 Go** (soudés) | 50 TOPS |
| 1 044–1 174 € | MINISFORUM N5 Pro (NAS) | AI 9 HX PRO 370 | ? | 80 TOPS |

- **Aucun mini PC Ryzen AI 7 350** trouvé sur AliExpress.fr (0 résultat).

## Specs constructeur & bruit (décisif)

- **GMKtec EVO-X1** : AI 9 HX 370, **12C/24T**, **TDP 15–54 W (pic 65 W)**, 32 Go soudés,
  2× M.2, 2× 2,5G, USB4/OCuLink, garantie 1 an.
  → **Bruit (notebookcheck)** : « point faible », **≈ 45 dB(A) en charge**, 28–30 au repos
  → **disqualifié** pour l'objectif « silencieux ».
- **Firebat A8** : AI 9 365 (10C/20T), **RAM SODIMM extensible** (24/32/64 Go),
  **double ventilateur + 3 caloducs** (65 W), « discret en usage courant » (pas de dB chiffré).

## Conclusion

Pour le critère « silencieux », l'**EVO-X1 est écarté en charge** ; le **Firebat A8** paraît
le meilleur profil (**RAM extensible, refroidissement à caloducs**) mais **sans mesure dB**.
Reste à confirmer le bruit du A8 et le prix/dispo FR.

## Reproduire

```sh
# 1. candidats (nécessite le conteneur SearXNG pour la recherche, sinon filtres directs)
webfetch --search "mini pc ryzen ai 9 365"
# 2. extraction structurée du listing AliExpress
examples/aliexpress_search.py --sort orders --ram 32 \
  --must "ai 9 365,hx 370,hx470" --exclude "processeur,ventirad,souris" \
  "mini pc ryzen ai 9 365"
# 3. valider un lien produit (rendu JS requis)
PLAYWRIGHT_BROWSERS_PATH=~/dev/webfetch/.browsers \
  uv run --with playwright --script webfetch --check --render \
  https://www.aliexpress.com/item/1005012261652447.html
```
