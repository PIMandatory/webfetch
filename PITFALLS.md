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
