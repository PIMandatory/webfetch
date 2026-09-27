# PITFALLS — webfetch / scraping

> Registre *symptôme → cause → correctif*. Lu en reprise, mis à jour en fin de session.
> Dernière mise à jour : 2026-09-27.

## trafilatura CLI ignore `-i <file>` (2026-09-27)
- **Symptôme** : `trafilatura -i /tmp/x.html` produit une sortie vide (code 1).
- **Cause** : le mode fichier ne reconstruit pas le contexte/URL ; l'extraction
  cible l'article et échoue silencieusement sur des pages non-articles.
- **Correctif** : utiliser `-u <URL>` (fetch interne) **ou** l'API Python
  `trafilatura.extract(html, output_format="markdown")`. Pour un fetch anti-bot :
  récupérer le HTML avec `curl_cffi` puis le passer à l'API Python.
- **Mots-clés** : trafilatura, `-i`, empty output, input-file.

## DuckDuckGo HTML endpoint renvoie 202 (2026-09-27)
- **Symptôme** : `html.duckduckgo.com/html/?q=...` → HTTP 202, 0 résultat (`result__a` absent).
- **Cause** : challenge anti-bot.
- **Correctif** : passer par une API de recherche (SearXNG / Brave / Serper) ou un
  lecteur (`r.jina.ai`) sur une page de résultats d'un autre moteur.
- **Mots-clés** : duckduckgo, 202, search, serp.

## g2.com → 403 malgré l'impersonation (2026-09-27)
- **Symptôme** : `curl_cffi` `impersonate=chrome` → HTTP 403.
- **Cause** : protection DataDome/Cloudflare dure.
- **Correctif** : FlareSolverr / Camoufox, ou accepter la limite.
- **Mots-clés** : 403, g2, datadome.

## Reddit sert un challenge anti-bot en HTTP 200 (2026-09-27)
- **Symptôme** : un sous-reddit inexistant renvoie **200** avec « Prove your humanity » →
  un simple contrôle de statut le déclarerait vivant à tort.
- **Cause** : mur anti-bot servi avec un code 200.
- **Correctif** : classifier sur le **contenu**, pas seulement le statut ; marqueurs
  `prove your humanity`, `verify you are human`, `just a moment`, `cf-chl`…
  (voir `webfetch --check`).
- **Mots-clés** : reddit, challenge, 200, anti-bot, soft-block.

## `r.history` de curl_cffi peut être vide malgré une redirection (2026-09-27)
- **Symptôme** : `https://google.com` → `r.url` = `https://www.google.com/` mais `len(r.history) == 0`.
- **Cause** : l'historique de redirection n'est pas toujours peuplé par curl_cffi.
- **Correctif** : détecter une redirection en comparant l'**URL d'origine** et l'**URL finale**
  (en ignorant le `/` final), pas via `r.history`.
- **Mots-clés** : curl_cffi, history, redirect, r.url.

## `uv run --with X <script>` ignoré à cause du shebang PEP 723 (2026-09-27)
- **Symptôme** : `uv run --with playwright webfetch --render` → « playwright not installed »,
  alors que `uv run --with playwright python -c 'import playwright'` marche.
- **Cause** : le script porte un shebang `uv run --script` ; le `--with` externe n'est pas
  propagé à l'environnement PEP 723 du script.
- **Correctif** : invoquer explicitement `uv run --with playwright --script webfetch --render URL`.
- **Mots-clés** : uv, --with, --script, PEP 723, shebang, playwright.

## Playwright : Arch non « officiellement supporté » (2026-09-27)
- **Symptôme** : à l'install, « BEWARE: your OS is not officially supported by Playwright;
  downloading fallback build for ubuntu24.04-x64 ».
- **Cause** : Playwright ne cible pas Arch/CachyOS officiellement.
- **Correctif** : le build de repli ubuntu24.04 **fonctionne** (libs système présentes) ;
  le T2 a été validé sur une page JS. Ne pas s'inquiéter de l'avertissement.
- **Mots-clés** : playwright, arch, unsupported, fallback, ubuntu24.04.

## AliExpress : un ID produit inexistant renvoie HTTP 200 (2026-09-27)
- **Symptôme** : `/item/1005000000000000.html` (ID bidon) renvoie **200** + redirection
  `gatewayAdapt`, exactement comme un vrai produit → `--check` (T1) le croit vivant.
- **Cause** : AliExpress ne renvoie pas 404 ; il sert une page « introuvable » en 200,
  et la page produit *réelle* n'est visible qu'en **JS**.
- **Correctif** : valider un lien produit avec **T2 (`--render`)**. La page morte a un
  **titre vide** et le texte « *Désolé, la page que vous essayez d'atteindre n'a pu être
  trouvée :(* » → ajouter `n'a pu être trouvée` / `could not be found` aux marqueurs soft-404.
- **Mots-clés** : aliexpress, 200, soft-404, page introuvable, gatewayAdapt.

## AliExpress : la liste de résultats est un JSON embarqué, pas un « article » (2026-09-27)
- **Symptôme** : `trafilatura` (T1/T2) ne renvoie que le texte marketing de la page de
  recherche, **aucun produit**.
- **Cause** : trafilatura cible le contenu « article » et **jette la grille produits**
  (JSON dans le HTML).
- **Correctif** : parser le HTML brut (**curl_cffi suffit**) — `"productId":"…"`,
  `"title":{"displayTitle":…}`, `"prices":{"salePrice":{"minPrice":…}}`, et le prix
  mini 30 j dans `sellingPoints`.
- **Mots-clés** : aliexpress, search, productId, displayTitle, trafilatura, listing.
