# PITFALLS — webfetch / scraping

> Registre *symptôme → cause → correctif*. Lu en reprise, mis à jour en fin de session.
> Dernière mise à jour : 2026-10-03.

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
  trouvée :(* » → marqueur soft-404 **ajouté** dans `webfetch` ; valider via
  `webfetch --check --render <url>`.
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

## Moteurs de recherche : bloqués en T1 **et** T2 (2026-09-27)
- **Symptôme** : DuckDuckGo / Bing / Brave renvoient un captcha ou « Enable JavaScript and
  cookies to continue » via `curl_cffi` **et** via `--render` ; `r.jina.ai` sur ces URLs aussi.
- **Cause** : protection anti-bot des SERP.
- **Correctif** : passer par une **API de recherche** (Brave / Serper / Tavily) ou un
  **SearXNG auto-hébergé**. Sans cette brique, impossible de croiser les specs avec des
  tests/avis (bloque notamment l'évaluation « bruit/silence »).
- **Mots-clés** : search, serp, duckduckgo, bing, brave, captcha, 202.

## HTTP 200 ≠ produit achetable (2026-09-27)
- **Symptôme** : `webfetch --check` renvoie `OK` sur une fiche produit, mais le produit est
  **indisponible / en rupture**, ou la config par défaut **n'est pas** celle voulue (ex.
  16 Go au lieu de 32 Go), ou la référence a changé.
- **Cause** : le statut HTTP valide **la page**, pas la **disponibilité produit** ni la config ;
  les **URLs produit sont volatiles** (refs changées, stock écoulé, variantes).
- **Correctif** : vérifier le **contenu** (chercher `indisponible` / `rupture` / `out of stock`,
  et les **variantes/prix**) ; **privilégier des pages de recherche/catégorie stables** ;
  **ne jamais livrer une URL produit** sans vérifier stock + config au moment de l'envoyer.
- **Mots-clés** : disponibilité, rupture, stock, fiche produit, variantes, liens morts.

## SearXNG : moteurs auto-suspendus ~180 s (2026-09-27)
- **Symptôme** : `webfetch --search` renvoie **0 résultat** alors qu'il marchait un peu plus tôt.
- **Cause** : les moteurs amont limitent SearXNG (logs : `suspended_time=180` pour **Brave/Google** ;
  **DDG** part en **CAPTCHA**, plus longtemps). Le conteneur SearXNG, lui, n'est pas bloqué.
- **Correctif** : `--engines google,bing` (route autour du moteur bloqué, cf. option ajoutée) ;
  attendre **~3 min de calme** ; ne pas requêter en rafale.
- **Mots-clés** : searxng, suspended_time, 180, rate limit, captcha, --engines.

## Recommandation produit donnée « de mémoire », non sourcée (2026-10-03)
- **Symptôme** : une fiche de recherche produit est close, ou un achat est déclenché, sur des
  **prix / poids / specs issus de la mémoire du modèle**, sans aucun passage par `webfetch`.
- **Cause** : la conversation dérive vers le conseil/la comparaison (réponse « de base de
  connaissances » légitime), puis l'achat est décidé avant que la campagne de vérification
  ne démarre → la recherche se termine sans source.
- **Correctif** : dès qu'une fourchette de prix ou une spec devient **décisionnelle**, la
  **marquer comme non vérifiée** et la sourcer (`webfetch --search`, `--check --render`) ; sinon
  la fiche doit porter un bandeau explicite « chiffres non sourcés » (cf.
  `docs/use-cases/keyboard-mouse-windows.md`).
- **Mots-clés** : prix indicatif, non vérifié, mémoire, fiche produit, décision d'achat.
