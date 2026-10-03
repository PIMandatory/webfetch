# Use case — clavier + souris sans fil pour un poste de travail Windows

> Fiche de recherche produit (2026-09-27 → 2026-10-03).
> Contexte : équiper un **poste Windows tiers** (pas le mien) pour du **bureautique +
> graphisme/vidéo**, sessions de **4-6 h**, **sans jeu vidéo**. Budget **cumulé 90-130 €**.
>
> 🟡 **EN COURS (2026-10-03) — NON clos.** Recherche **ouverte** ; **aucune** campagne
> `webfetch` n'a encore tourné. ⚠️ Tous les chiffres ci-dessous viennent de ma **base de
> connaissances** : **prix, poids et D.P.I. indicatifs, NON vérifiés à la source**.

## Besoin et contraintes

| Critère | Valeur |
|---|---|
| Usage | bureautique, **graphisme / vidéo**, sessions 4-6 h |
| Jeu vidéo | non |
| Budget | **90-130 € cumulés** (clavier + souris) |
| Souris | **sans fil** souhaité (le critère le plus fort de l'acquéreur) |
| Clavier | sans fil **non** requis |
| OS | **Windows** (poste tiers → plug-and-play prioritaire, pas de logiciel imposé) |
| Disposition | **AZERTY FR** présumée — **jamais confirmée** |

## Fréquences sans fil — la question posée par l'utilisateur

Tout le sans-fil grand public est sur la bande **2,4 GHz (ISM)**, partagée avec le WiFi,
le Bluetooth et les dongles propriétaires. Ce n'est donc pas « une » fréquence, mais un
espace saturé.

- **Dongle propriétaire** (Logitech Unifying/**Bolt**, Lightspeed, HyperSpeed) : sauts de
  fréquence + protocole dédié → latence ~1 ms, très résistant. **Le bon choix**, y compris
  en bureautique. Un dongle peut souvent porter clavier **et** souris.
- **Bluetooth** : même bande, aussi avec sauts, mais *polling* plus lent (~10-30 ms) et
  appairage/multipoint à gérer → acceptable en bureautique, insuffisant pour du jeu.
- **Cause n°1 des vrais décrochages : l'USB 3.x**, pas la fréquence. Les ports/hubs USB 3
  émettent du bruit large bande autour de 2,4 GHz ; un dongle branché dessus, à l'arrière
  d'un boîtier métal ou derrière l'écran ⇒ micro-coupures et latence irrégulière.
  **Correctif : rallonge USB 30-100 cm** (ou port USB 2 dégagé) — ~5 €, règle l'essentiel.
- Autres perturbateurs : WiFi 2,4 GHz saturé (immeuble), micro-ondes, câbles HDMI/USB non
  blindés, accumulation de dongles 2,4 GHz.

**Conclusion** : souris sans fil = oui, en **2,4 GHz + dongle propriétaire** ; clavier sans
fil = apport faible (juste le câble en moins) au prix de la charge/pile et d'un point de
panne de plus.

## Clavier — qu'est-ce qui est vraiment « orienté travail » ?

Objection soulevée par l'utilisateur, et fondée : les claviers « enthusiast » (Keychron
Q/V, QMK, hot-swap, gasket, RGB) sont des critères de hobbyiste, pas de fiabilité.

| Famille | Marqueurs | Adapté au travail ? |
|---|---|---|
| **Bureau / office** | AZERTY FR dispo, silencieux, faible course, zéro logiciel obligatoire, SAV FR | **Oui — cible** |
| **Gamer** | RGB, 8000 Hz, « 1 ms », AZERTY souvent absent | Non |
| **Enthusiast / custom** | hot-swap, QMK/VIA, gasket, switches au choix | Non |

Contre-intuitif utile : le matériel **vraiment** orienté travail est souvent **moins cher**
(un clavier de bureau Cherry/Dell/Lenovo à 45-60 € est conçu pour 8 h/jour), là où un
Keychron à 150 € est conçu pour être démonté.

Checklist « travail » : **AZERTY FR disponible** (filtre n°1) · course courte et amortie
(scissor / low-profile → moins de fatigue et bien plus silencieux) · légendes **double-shot**
ou PBT · **USB-C détachable** · garantie/SAV France · **aucun logiciel obligatoire**. Inutile :
RGB, 8000 Hz, écran, molette de créativité.

## Souris — cible retenue : **M650 L**

- **Écarté** : le **vertical** (Lift, MX Vertical) — « déjà essayé, pas à l'aise ».
- **Retenu comme cible** : **Logitech M650 L** (version *Large* de la M650) — clics
  silencieux, ~4000 dpi, dongle **Bolt** + BT, plug-and-play.

| Souris | Poids avec pile (indicatif) | Verdict |
|---|---|---|
| MX Anywhere 3S | ~99 g | légère |
| M650 | ~101 g | moyenne |
| **M650 L** | **~115 g** | moyenne+, **pas lourde** |
| M720 Triathlon | **~135 g** | oui |
| MX Master 3S | **~141 g** | oui (référence) |

Deux réserves importantes vis-à-vis du critère « bonnes sensations » de l'acquéreur :

- **Le poids est réglable pour ~0 €** : la M650/M650 L fonctionne avec **1 pile AA** —
  lithium ≈ 15 g, **NiMH rechargeable (Eneloop) ≈ 30 g** → **+15 g** sans rien acheter.
- **Les clics « Silent Touch » sont amortis par conception** : si le vrai reproche est le
  **retour tactile** (et pas la masse), la M650 L est un mauvais pari. La **M720** est alors
  au-dessus (clics francs, molette à **défilement horizontal** utile en vidéo) — sa limite
  est son capteur **1000 dpi**, pénible au-delà du 1080p.
- Rappel : des **patins PTFE** en bon état et un **centre de gravité vers l'arrière**
  comptent autant que la masse dans la sensation de tenue.

## Recommandation provisoire (recherche ouverte)

| | Piste budget ~90-105 € | Piste qualité ~110-130 € |
|---|---|---|
| Clavier | Cherry KC 6000 Slim / Logitech K650 (AZERTY FR, full-size, silencieux) ~45-55 € | Logitech **MX Keys S** (promo ~75-90 €) — la référence travail |
| Souris | Logitech **M650 L** ~40-50 € (+ pile NiMH) | Logitech **M720** ~40-50 € ou **MX Master 3S** reconditionné ~50-60 € |
| Dépendance | aucune | *Options+* (droits admin) pour exploiter tout le potentiel |

Écartés d'office : 60 %/TKL (pas de pavé numérique ni de rangée F pour la vidéo), claviers
gaming, Keychron séries Q/V (enthusiast, AZERTY FR rare), verticale (déjà testée).

## Ce qui n'a PAS été vérifié (à faire — recherche ouverte)

- [ ] **Statut réel de l'achat** : annoncé « achat fait et recherche terminée » puis
      **« non clos »** → contradiction à trancher avant tout archivage.
- [ ] **Modèle réellement acheté** (non communiqué) → compléter la fiche.
- [ ] **Disposition AZERTY FR** du clavier — jamais confirmée.
- [ ] **Prix réels / disponibilité** de la M650 L, M720, MX Keys S, K650, KC 6000 Slim.
- [ ] **Poids et dpi exacts** (chiffres donnés de mémoire : ~115 g M650 L, 4000 dpi).
- [ ] **Silence du poste** (open space ?) — critère non tranché.

## Reproduire (si la recherche est rouverte)

```sh
webfetch --search "logitech m650 L prix France"
webfetch --search "logitech m720 triathlon prix" --engines google,bing
webfetch --check --render "https://www.logitech.com/fr-fr/products/mice/m650-signature-mouse.html"
```

## Note de méthode (leçon)

Ce cas d'usage s'est déroulé **sans `webfetch`** : les prix et specs ont été donnés de
mémoire, et la recherche **n'est pas close**. Conséquence assumée : la fiche est un
**raisonnement documenté**, pas un **relevé sourcé**. Ne pas réutiliser ses prix comme des
prix constatés (voir `PITFALLS.md`, entrée « Recommandation produit non vérifiée »).
