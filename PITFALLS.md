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
