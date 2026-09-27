# Install plan & registry — T2 · SearXNG · T3

> **Règle** : rien n'est installé sans accord explicite, **dans un dossier isolé et
> réversible**, et consigné ici. Rien de « définitif » (Stow/PATH) avant validation.
> Faits vérifiés sur la machine le **2026-09-27**.

## 1. État de la machine (vérifié, rien à installer pour autant)

| Élément | État |
|---|---|
| `uv` | présent (0.12.19) — exécute les scripts PEP 723 sans install système |
| libs Chromium (`libnss3`, `libatk`, `libgbm`, `libasound`, `libxkbcommon`, `libatk-bridge`, `libcups`, `libdrm`) | **toutes présentes** → Chromium Playwright devrait tourner sans dépendance supplémentaire |
| Navigateur système | Firefox seulement (pas de Chromium/Chrome) |
| `docker` | **absent** |
| `podman` | présent (6.1.2), **rootless** (images déjà utilisées pour d'autres projets) |
| espace disque `/home` | 722 Go libres |
| cache `~/.cache/uv` | 523 Mo (cache jetable, pas une install) |
| `~/.cache/ms-playwright` | absent |

**Point clé** : tout ce qui suit est **réversible** et n'écrit **pas** dans le système
(pas de `sudo`, pas de paquet distro, pas de `/usr`).

## 2. T2 — Playwright headless Chromium

### But
Rendre les pages **JS/SPA** (contenu injecté côté client) que T1 ne voit pas.

### Ce qui est installé, et où (avec notre isolation)
- **Paquet Python `playwright`** : résolu par `uv` dans **son cache** (`~/.cache/uv`),
  jamais dans le Python système. Jetable (`uv cache clean`).
- **Navigateur Chromium** : par défaut `~/.cache/ms-playwright` → **on force**
  `PLAYWRIGHT_BROWSERS_PATH=~/dev/webfetch/.browsers`, donc **confiné dans l'étude**.

### Tailles (vérifiées via les en-têtes du CDN, chiffres exacts)
| Composant | Téléchargement |
|---|---|
| Chrome for Testing 153 (complet) | **187 Mo** |
| Chrome Headless Shell 153 | **115 Mo** |
| FFmpeg | 2,3 Mo |
| **Total avec `--only-shell`** (recommandé, suffit en headless) | **≈ 118 Mo** |

Extrait sur disque : compter ~1,5 à 2× l'archive (~250–400 Mo) — on a largement la place.

### Commandes exactes (isolées)
```sh
export PLAYWRIGHT_BROWSERS_PATH=$HOME/dev/webfetch/.browsers
uv run --with playwright playwright install --only-shell chromium
```
> `--only-shell` n'installe que le shell headless (pas le Chrome complet ni l'UI) :
> plus léger et suffisant pour extraire du contenu.

### Vérification (avant tout caractère définitif)
```sh
PLAYWRIGHT_BROWSERS_PATH=$HOME/dev/webfetch/.browsers \
  uv run --with playwright --script /path/to/webfetch --render <URL_SPA>
```
> Le `--script` est **obligatoire** : le shebang PEP 723 du script empêche un
> `uv run --with … <script>` simple de propager Playwright (voir `PITFALLS.md`).
Comparer la sortie T1 (souvent vide/partielle) vs T2 (complète) → c'est le **test**.

**Résultat 2026-09-27** : installé dans `.browsers/` (**266 Mo** extraits),
T2 **validé** sur `quotes.toscrape.com/js/` (citations injectées en JS, invisibles
en T1, restituées en T2). Arch non « officiellement supporté » → build de repli
ubuntu24.04, fonctionnel.

### Contraintes / limites
- Chrome for Testing ~187 Mo à chaque montée de version Playwright (nettoyage auto des
  anciennes versions).
- Poids en RAM/CPU par lancement (un Chromium par requête en headless) → ok pour un
  usage ponctuel, pas pour du crawl massif.
- **Ne contourne pas** les anti-bot durs (Cloudflare/DataDome) : ça, c'est T3.

### Désinstallation (retour à zéro)
```sh
rm -rf ~/dev/webfetch/.browsers      # navigateurs
uv cache clean playwright            # paquet Python (optionnel)
```

## 3. T3 — FlareSolverr (anti-bot dur : Cloudflare, DataDome…)

> **Non retenu** (course anti-bot + conteneur à maintenir) ; gardé « en réserve » uniquement si un site l'exige.

### But
Résoudre le cas g2.com (403) et les « managed challenges » : proxy HTTP local qui
pilote un navigateur furtif et renvoie le HTML + cookies.

### Ce qui est installé, et où
- **Image conteneur** `ghcr.io/flaresolverr/flaresolverr:latest` via **podman rootless**
  (aucun démon privilégié, contenu confiné). Taille image : à confirmer au `pull`
  (compter quelques centaines de Mo).
- Pas de port ouvert au réseau : on publie seulement en **local** (`127.0.0.1:8191`).

### Commandes exactes (isolées)
```sh
podman run -d --name flaresolverr -p 127.0.0.1:8191:8191 \
  ghcr.io/flaresolverr/flaresolverr:latest
curl -s http://127.0.0.1:8191/health
```
Puis `webfetch` appellerait `POST http://127.0.0.1:8191/v1` (intégration à coder).

### Contraintes / limites
- Nécessite de **maintenir l'image** à jour (crée un suivi).
- Peut casser quand Cloudflare évolue (course outillage/anti-bot, sans garantie).
- Léger surcoût disque + un conteneur à gérer.

### Désinstallation
```sh
podman rm -f flaresolverr && podman rmi ghcr.io/flaresolverr/flaresolverr:latest
```

## 4. Brique recherche — SearXNG (retenu, 2026-09-27)

### But
Trouver des pages (tests/avis, revendeurs) et croiser les infos — la brique qui manquait.

### Ce qui est installé, et où
- Image conteneur **`docker.io/searxng/searxng:latest`** (**93 Mo**) via **podman rootless**.
- Config isolée : `~/dev/webfetch/.searxng/settings.yml` (sortie **JSON** activée, `limiter: false`).
- Exposé **`127.0.0.1:8888`** uniquement.

### Commandes
```sh
podman run -d --name searxng -p 127.0.0.1:8888:8080 \
  -v ~/dev/webfetch/.searxng:/etc/searxng docker.io/searxng/searxng:latest
```
**Politique d'usage (SearXNG « à la demande », automatique)** :
- `webfetch --search` **démarre** le conteneur s'il est arrêté, fait la requête, puis **l'arrête**
  (**one-shot**) → « fonctionnel à la demande, arrêté sinon ».
- `--no-autostart` pour gérer à la main (`podman start searxng` / `podman stop searxng`).
- Le conteneur reste **arrêté hors usage** ; `webfetch` (fetch / `--check`) marche **sans** SearXNG.

### Contraintes
- Conteneur **à (re)démarrer** (`podman start searxng`), mise à jour occasionnelle.
- Moteurs amont parfois rate-limités (email à privilégier DDG/Bing/Brave/Startpage).

### Désinstallation
```sh
podman rm -f searxng && podman rmi docker.io/searxng/searxng:latest
```

## 5. Protocole « tester avant de rendre définitif »

1. **Bac à sable isolé** : tout dans `~/dev/webfetch/.browsers` et `.sandbox/`
   (ignorés par git — voir `.gitignore`).
2. **Corpus de test** (URLs connues, un cas par catégorie) :
   - T1 déjà OK : wikipedia, lemonde, HN.
   - SPA/JS : à choisir (ex. une app publique rendue côté client).
   - Anti-bot : g2.com (403), reddit (« prove your humanity »).
3. **Mesure** : pour chaque URL, comparer T1 vs T2/T3 (statut, longueur, présence du
   contenu attendu). On **vérifie qu'on n'obtient pas que des liens/contenus morts**.
4. **Décision** : on ne « fige » un outil (Stow/PATH, config) que si le test est
   concluant ; sinon on retire le dossier isolé. Résultats consignés dans `SESSION.md`.

## 6. Registre de ce que NOUS avons installé

| Date | Composant | Emplacement | Taille | Statut |
|---|---|---|---|---|
| 2026-09-27 | Playwright `chromium-headless-shell` 153 + ffmpeg | `~/dev/webfetch/.browsers/` | 266 Mo | installé, **T2 validé** (page JS) ; retrait : `rm -rf ~/dev/webfetch/.browsers` |
| 2026-09-27 | **SearXNG** (métamoteur, conteneur podman rootless) | config `~/dev/webfetch/.searxng/`, port `127.0.0.1:8888` | 93 Mo | **actif**, recherche testée ; retrait : `podman rm -f searxng && podman rmi docker.io/searxng/searxng` |

> Le cache `~/.cache/uv` (523 Mo) préexiste à ce sujet ; c'est un cache jetable,
> pas une installation. Aucun paquet système, aucun `sudo` n'a été utilisé.
