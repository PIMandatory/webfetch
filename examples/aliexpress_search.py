#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["curl_cffi>=0.7"]
# ///
"""Example — AliExpress search -> filtered, deduped shortlist.

Throwaway sandbox script (NOT part of webfetch yet). Parses the product JSON
embedded in the search-result HTML (trafilatura would discard it).

Usage:
  ali_search.py --must "ai 9 365,ai 7 350" --exclude "cpu,ventilateur" \
                --ram 32 --sort orders "query 1" "query 2" ...
Writes a dated snapshot under .sandbox/snapshots/.
"""
from __future__ import annotations
import json, re, sys, time, datetime, argparse
from pathlib import Path
from urllib.parse import quote_plus

from curl_cffi import requests as creq

HERE = Path(__file__).resolve().parent
SNAP = HERE / "snapshots"
SORT = {"relevance": None, "orders": "total_tranpro_desc", "price_asc": "price_asc", "price_desc": "price_desc"}


def slug(q: str) -> str:
    return quote_plus(q.strip().lower().replace(" ", "-"))


def first(pat, s):
    m = re.search(pat, s)
    return m.group(1) if m else None


def jstr(raw):
    if raw is None:
        return None
    try:
        return json.loads('"' + raw + '"')
    except Exception:
        return raw


def parse_products(html: str):
    out, seen = [], set()
    for m in re.finditer(r'"productId":"(\d+)"', html):
        pid = m.group(1)
        if pid in seen:
            continue
        seg = html[m.start(): m.start() + 2600]
        title = jstr(first(r'"displayTitle":"(.*?)"', seg))
        price = first(r'"salePrice":\{[^}]*?"minPrice":([\d.]+)', seg)
        currency = first(r'"salePrice":\{[^}]*?"currencyCode":"(\w+)"', seg)
        low = first(r'Prix le plus bas des 30 derniers jours:\s*([\d\s.,]+)€', seg)
        if not title:
            continue
        seen.add(pid)
        out.append({"id": pid, "title": title,
                    "price": float(price) if price else None, "currency": currency,
                    "low_30d": low.strip() if low else None,
                    "url": f"https://www.aliexpress.com/item/{pid}.html"})
    return out


def search(query: str, sort: str):
    url = f"https://fr.aliexpress.com/w/wholesale-{slug(query)}.html"
    if SORT.get(sort):
        url += f"?SortType={SORT[sort]}"
    r = creq.get(url, impersonate="chrome", timeout=30)
    return url, r.status_code, parse_products(r.text)


def keep(p, must, exclude, ram):
    t = p["title"].lower()
    if must and not any(k.strip().lower() in t for k in must if k.strip()):
        return False
    if exclude and any(k.strip().lower() in t for k in exclude if k.strip()):
        return False
    if ram and not re.search(rf"{ram}\s*(go|gb|g)\b", t):
        return False
    return True


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("queries", nargs="+")
    ap.add_argument("--sort", default="orders", choices=list(SORT))
    ap.add_argument("--must", default="")
    ap.add_argument("--exclude", default="")
    ap.add_argument("--ram", type=int, default=0)
    args = ap.parse_args(argv)
    must = args.must.split(",") if args.must else []
    exclude = args.exclude.split(",") if args.exclude else []

    combined, raw = {}, {}
    for q in args.queries:
        try:
            url, code, prods = search(q, args.sort)
        except Exception as exc:  # noqa: BLE001
            print(f"! {q}: {type(exc).__name__}: {exc}")
            continue
        raw[q] = prods
        kept = [p for p in prods if keep(p, must, exclude, args.ram)]
        print(f"### {q}  [{code}, {len(prods)} → {len(kept)} retenus]")
        for p in kept:
            combined[p["id"]] = p
        time.sleep(1.5)

    items = sorted(combined.values(), key=lambda p: (p["price"] is None, p["price"] or 0))
    print(f"\n===== SHORTLIST dédupliquée : {len(items)} produits =====")
    for p in items:
        price = f"{p['price']:.2f} {p['currency']}" if p["price"] else "?"
        low = f" (30j {p['low_30d']}€)" if p["low_30d"] else ""
        print(f"{price:>12}{low:24} {p['title'][:80]}")
        print(f"{'':38} {p['url']}")

    SNAP.mkdir(parents=True, exist_ok=True)
    stamp = datetime.date.today().isoformat()
    out = {"queries": args.queries, "filters": {"must": must, "exclude": exclude, "ram": args.ram},
           "shortlist": items, "raw": raw}
    path = SNAP / f"aliexpress-{stamp}-{args.sort}-filtered.json"
    path.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(f"\n[snapshot] {path}")


if __name__ == "__main__":
    main(sys.argv[1:])
