# Use case — achat d'un mini PC (recherche multi-sources)

> **Cas d'usage de référence de `webfetch`** : trouver un mini PC, **garantir des liens
> vivants**, récupérer les specs, **croiser avec des tests**, comparer les revendeurs et
> décider. Recherche **étendue hors AliExpress** (mise à jour **2026-09-27**).
> Les prix sont indicatifs (TVA selon boutique) et datés du 2026-09-27.

## Besoin

Mini PC **8C/16T, 32 Go**, charge CPU/mémoire — **frais, silencieux, NPU ≥ 40 TOPS** (Copilot+).

## 🎯 Retenu — profil idéal 8C/16T + silencieux

| Modèle | CPU | Config | Prix | Lien |
|---|---|---|---|---|
| **Beelink SER9 MAX** | **Ryzen AI 7 H 350** (8C/16T, NPU 50 TOPS, Radeon 860M) | **32 Go + 1 To** | **1 029 €** | https://www.bee-link.com/fr/products/beelink-ser9-max-amd-ryzen-7-h-255 |
| Beelink SER9 MAX | idem | 64 Go + 1 To | 1 369 € | (même fiche, variante 64 Go) |
| ASUS ExpertCenter PN54 | Ryzen AI 7 350 (cTDP 40 W) | 32 Go max, pro/barebone | à confirmer | https://www.asus.com/fr/displays-desktops/mini-pcs/pn-series/asus-expertcenter-pn54/ |

## Alternatives (12C/24T — plus de cœurs que le besoin)

| Modèle | CPU | Config | Prix | Lien |
|---|---|---|---|---|
| Minisforum AI X1 | AI 9 HX 370 | 32 Go + 1 To (barebone 699 €) | 1 139 € | https://minisforumpc.fr/products/minisforum-ai-x1 |
| Minisforum AI X1 Pro-370 | AI 9 HX 370 | 32 Go + 1 To | 1 249 € | https://minisforumpc.fr/products/minisforum-ai-x1-pro-370 |
| GMKtec EVO-X1 | AI 9 HX 370 | 32 Go + 1 To | 1 199,95 € | https://www.ldlc.com/fiche/PB00707684.html |
| GMKtec EVO-X1 (officiel) | AI 9 HX 370 | 32 Go + 1 To | 1 149,99 $ | https://www.gmktec.com/products/amd-ryzen%E2%84%A2-ai-9-hx-370-evo-x1-ai-mini-pc |
| Geekom A9 Max | AI 9 HX 470 | — | 1 699–1 999 € | https://www.geekom.fr/geekom-a9-max-mini-pc/ |
| ACEMAGIC F3A | AI 9 HX 370 | — | 614 € (promo) | https://www.minimachines.net/actu/acemagic-f3a-ryzen-ai-9-hx-370-132269 |
| Minisforum EliteMini AI370 | AI 9 HX 370 | — | ~949 € | https://www.minimachines.net/actu/minisforum-elitemini-ai370-le-minipc-ryzen-ai-9-hx-370-a-949e-130713 |

## AI 9 365 (10C/20T) et Lunar Lake

| Modèle | CPU | Config | Prix | Lien |
|---|---|---|---|---|
| MINIX Elite ER936-AI | AI 9 365 | 32 Go | Amazon.fr | https://www.amazon.fr/MINIX-ER936-AI-DDR5-5600-cr%C3%A9ation-entreprise/dp/B0FMF4W5CX |
| Firebat A8 | AI 9 365 (RAM SODIMM extensible) | 32 Go + 1 To | 1 009 € | https://www.aliexpress.com/item/1005012261652447.html |
| Firebat A8 (officiel) | AI 9 365 | 24 Go (config) | 1 399 $ | https://www.firebatpc.com/products/firebat-mini-pc-a8-amd-ryzen-ai-9-365 |
| CHUWI AuBox X | Ultra 7 256V (Lunar Lake) | 16 Go | 762 € | https://www.aliexpress.com/item/1005005102829277.html |

## Bruit — mesures croisées (décisif)

| Modèle | Repos | Charge | Verdict | Test |
|---|---|---|---|---|
| **Beelink SER9 MAX** | ~32 dB | continu, **sans pics** (« quasi inaudible ») | ✅ **le plus silencieux** (chambre à vapeur MSC 2.0) | https://minipc-review.com/fr/beelink-ser9-max-analyse |
| Minisforum AI X1 Pro | 28 dB | 38,4–41,8 dB (**mode Silence : 36,1 dB**) | 🟡 correct (réglable BIOS) | https://www.notebookcheck.net/Minisforum-AI-X1-Pro-review-An-all-round-mini-PC-for-the-office-multimedia-gaming-and-creative-tasks.973433.0.html |
| GMKtec EVO-X1 | 27,8–30,4 dB | **44,6–46,1 dB** | ❌ bruyant | https://www.notebookcheck.biz/Test-du-GMKtec-EVO-X1-nouveau-design-compact-avec-Oculink-et-Ryzen-AI-9.964782.0.html |
| ASUS PN54 | 25 dB | **42,6–47,1 dB** | ❌ bruyant en charge | https://www.notebookcheck.net/Asus-ExpertCenter-PN54-Business-mini-PC-with-AMD-Ryzen-AI-7-and-modern-features-in-the-review.1096722.0.html |

## Budget ≤ 700 € (NPU assoupli) — 8C/16T + 32 Go + silencieux

Critères revus : on garde **8C/16T, 32 Go, silencieux** ; on **abandonne le NPU fort**
(Hawk Point / Zen 4, NPU ~16 TOPS).

| Modèle | CPU | Config | Prix | Lien |
|---|---|---|---|---|
| **Minisforum AI X1** | **Ryzen 7 260** (8C/16T, Hawk Point, NPU ~16 TOPS) | **32 Go + 1 To** | **699 €** | https://minisforumpc.fr/products/minisforum-ai-x1 |
| GMKtec K8 Plus | Ryzen 7 8845HS (8C/16T) | 32 Go + 1 To | 729,99 € (officiel) ; moins cher sur AliExpress | https://gmktec.fr/products/gmktec-nucbox-k8-plus-amd-ryzen-7-8845hs |
| Beelink SER8 | Ryzen 7 8845HS (8C/16T) | 32 Go + 1 To | ~899 € (**hors budget**) | https://www.idealo.fr/prix/205489945/beelink-ser8.html |

- **Bruit** : AI X1 → chambre à vapeur « grand ventilateur silencieux » ; SER8 mesuré
  **~34,6 dB(A)** en charge ; K8 Plus refroidissement revu « bruit réduit ».
- **Ryzen 7 260 = Hawk Point (Zen 4)**, 8C/16T, quasi identique au 8845HS → **NPU faible**
  (conforme au compromis). Radeon 780M.
- ⚠️ `idealo` : 669 € = config **inférieure** ; la **32 Go/1 To est à ~899 €**.

### Fiche d'achat — Minisforum AI X1 (Ryzen 7 260, 32 Go + 1 To) ✅ **retenu**

- **Lien** : https://minisforumpc.fr/products/minisforum-ai-x1 — variante *AMD Ryzen 7 260 /
  32GB RAM + 1TB SSD* (SKU **X131EU**).
- **Prix** : **699 €** · **en stock** (`InStock`).
- **Garantie** : **2 ans** (réparation, MINISFORUM ; retour aux frais du client, réexpédition à leur charge).
- **Livraison** : gratuite, mais **expédiée hors UE** — boutique opérée par **Econ Technology Ltd
  (Manchester, UK)** ; transporteurs cités : **EMS / China Post / HongKong Post**. La politique
  mentionne explicitement la **douane/TVA d'importation** (remboursées par Minisforum sur justificatif
  si vous les payez, + option « assurance tarifaire » 30 €). **Délais longs** possibles.
- **Pas d'entrepôt UE** : `minisforum.eu` est vide, `store.minisforum.com` = boutique globale ;
  **aucun revendeur FR identifié** pour l'AI X1.
- **Alternative sans douane** : GMKtec K8 Plus via **AliExpress** (TVA prépayée, ~600 € configs)
  ou **LDLC** (799,95 €, garantie locale mais > budget).

## Shortlist ≤ 700 € SANS douane (revendeurs fiables) — vérifiée 2026-09-27

Critères : **8C/16T · 32 Go · silencieux · ≤ 700 € · revendeur FR/EU (pas de douane)** · NPU assoupli.

| Modèle | CPU | Config | Bruit (mesuré) | Prix | Lien |
|---|---|---|---|---|---|
| **Ninkear M8** | Ryzen 7 **8745HS** (8C/16T) | **32 Go + 1 To** | **~37–38 dB max** | **599 €** | https://www.darty.com/nav/achat/ref/MC354196272.html · https://ninkear.com/fr/products/ninkear-m8 |
| Geekom A6 | Ryzen 7 **6800H** (8C/16T, Zen3+) | 32 Go (max 64) | à confirmer | 599–649 € | https://www.geekom.fr/geekom-a6-mini-pc/ · https://www.amazon.fr/GEEKOM-A6-Ordinateur-Affichage-Quadruple/dp/B0DRP2CPR1 |
| GMKtec K8 Plus | Ryzen 7 8845HS (8C/16T) | 32 Go + 1 To | silencieux (reviews) | ~690 € (deal) / **810 €** (officiel) | https://www.ldlc.com/fiche/PB00706845.html · https://gmktec.fr/products/gmktec-nucbox-k8-plus-amd-ryzen-7-8845hs |

### Écartés (défaut vs critères)
- **BMAX B8 A Power** (8845HS, 32 Go) — 494,99 € mais **« fan quite loud under heavy load »** → **échoue au silence** : https://fr.geekbuying.com/item/BMAX-B8-A-Power-AI-Mini-PC-AMD-Ryzen-7-Pro-8845HS-32-Go-1-To-10003838.html
- **Beelink SER8** (32 Go) — silencieux (~34,6 dB) mais **~1 050 €** → **hors budget** : https://www.idealo.fr/prix/205489945/beelink-ser8.html
- **Minisforum AI X1** — 699 € mais **expédié hors UE** → douane : https://minisforumpc.fr/products/minisforum-ai-x1

### Réserves de vérification
- **Darty bloque l'automatisation (403)** : le **599 €** du Ninkear M8 est issu d'un comparateur/snippet, **à revérifier sur la page** ; idem `Amazon.fr` (captcha) → prix SER8/K8 Plus partiellement non vérifiés en direct.

## Conclusion

- **Avec NPU fort** : **Beelink SER9 MAX** (AI 7 350, 8C/16T, 32 Go, silencieux) — **1 029 €**.
- **≤ 700 € (NPU assoupli)** : **Minisforum AI X1 — Ryzen 7 260, 32 Go, 699 €**
  (8C/16T, châssis à chambre à vapeur) ; alternative **GMKtec K8 Plus** (8845HS, 729,99 € officiel,
  moins cher sur AliExpress).
- **À écarter** : GMKtec EVO-X1 / ASUS PN54 (**~42–47 dB**, bruyants) ; Beelink SER8 32 Go (~899 €, hors budget).

## Reproduire

```sh
webfetch --search "mini pc ryzen ai 9 365 32 go France prix"
# prix + variantes d'une boutique Shopify (Minisforum, Beelink, GMKtec, Firebat) :
webfetch --html "https://minisforumpc.fr/products/minisforum-ai-x1.json" | jq -r '.product.variants[] | "\(.title) -> \(.price)"'
# prix LDLC (JSON-LD) :
webfetch --html "https://www.ldlc.com/fiche/PB00707684.html" | grep -o '"price"[^,]*'
```
