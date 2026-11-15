#!/usr/bin/env python3
"""Static site builder: posts/*.md (YAML front matter) -> dist/."""
import json, re, shutil, datetime, html
from pathlib import Path
import markdown, yaml

ROOT = Path(__file__).parent
DIST = ROOT / "dist"
CFG = json.loads((ROOT / "site.json").read_text())
URL = CFG["url"].rstrip("/")
from urllib.parse import urlparse
BASE = urlparse(URL).path.rstrip("/")


def load_posts():
    posts = []
    for f in sorted((ROOT / "posts").glob("*.md")):
        raw = f.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
        meta, body = yaml.safe_load(m.group(1)), m.group(2)
        if meta.get("draft"):
            continue
        # {{aff:frase}} -> affiliate link
        body = re.sub(r"\{\{aff:(\w+)\}\}", lambda x: CFG["affiliate_links"].get(x.group(1), "#"), body)
        meta["slug"] = meta.get("slug") or f.stem
        meta["date"] = str(meta["date"])
        meta["html"] = markdown.markdown(body, extensions=["tables", "toc", "attr_list", "sane_lists", "md_in_html"])
        posts.append(meta)
    return sorted(posts, key=lambda p: p["date"], reverse=True)


def page(title, desc, body, path, extra_head=""):
    canonical = f"{URL}{path}"
    return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canonical}"><meta property="og:type" content="article">
<link rel="stylesheet" href="/style.css"><link rel="alternate" type="application/rss+xml" href="/feed.xml">
{extra_head}
</head><body>
<header class="top"><div class="wrap"><a class="logo" href="/">{CFG['name']}</a>
<nav><a href="/">Reviews</a><a href="/about/">About</a><a href="/disclosure/">Disclosure</a></nav></div></header>
<main class="wrap">{body}</main>
<footer><div class="wrap"><p>{CFG['name']} is reader-supported. Some links are affiliate links: if you buy through them we may earn a commission at no extra cost to you. <a href="/disclosure/">Learn more</a>.</p>
<p>&copy; {datetime.date.today().year} {CFG['name']} · <a href="/privacy/">Privacy</a></p></div></footer>
</body></html>"""


def write(path, content):
    out = DIST / path.lstrip("/") / "index.html" if path.endswith("/") else DIST / path.lstrip("/")
    out.parent.mkdir(parents=True, exist_ok=True)
    content = content.replace('href="/', f'href="{BASE}/').replace('src="/', f'src="{BASE}/')
    out.write_text(content, encoding="utf-8")


def card(p):
    return f"""<article class="card"><span class="tag">{html.escape(p.get('type','Review'))}</span>
<h2><a href="/{p['slug']}/">{html.escape(p['title'])}</a></h2>
<p>{html.escape(p['description'])}</p><time>{p['date']}</time></article>"""


def build():
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    shutil.copytree(ROOT / "static", DIST, dirs_exist_ok=True)
    posts = load_posts()

    for p in posts:
        schema = {"@context": "https://schema.org", "@type": "Article", "headline": p["title"],
                  "description": p["description"], "datePublished": p["date"],
                  "dateModified": str(p.get("updated", p["date"])),
                  "author": {"@type": "Organization", "name": CFG["author"]}}
        head = f'<script type="application/ld+json">{json.dumps(schema)}</script>'
        notice = ('<p class="notice">Disclosure: this article contains affiliate links. '
                  'We may earn a commission if you buy through them, at no extra cost to you.</p>')
        upd = f" · Updated {p['updated']}" if p.get("updated") else ""
        body = (f'<article class="post"><h1>{html.escape(p["title"])}</h1>'
                f'<p class="meta">By {CFG["author"]} · {p["date"]}{upd}</p>{notice}{p["html"]}</article>')
        write(f"/{p['slug']}/", page(f"{p['title']} | {CFG['name']}", p["description"], body, f"/{p['slug']}/", head))

    hero = f'<section class="hero"><h1>{CFG["tagline"]}</h1><p>{CFG["description"]}</p></section>'
    write("/", page(f"{CFG['name']} – {CFG['tagline']}", CFG["description"],
                    hero + '<div class="grid">' + "".join(card(p) for p in posts) + "</div>", "/"))

    for slug in ("about", "disclosure", "privacy"):
        f = ROOT / "pages" / f"{slug}.md"
        if f.exists():
            raw = f.read_text(encoding="utf-8")
            title = raw.splitlines()[0].lstrip("# ").strip()
            write(f"/{slug}/", page(f"{title} | {CFG['name']}", title,
                                    f'<article class="post">{markdown.markdown(raw)}</article>', f"/{slug}/"))

    urls = ["/"] + [f"/{p['slug']}/" for p in posts] + ["/about/", "/disclosure/", "/privacy/"]
    (DIST / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        + "".join(f"<url><loc>{URL}{u}</loc></url>" for u in urls) + "</urlset>")
    (DIST / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {URL}/sitemap.xml\n")
    items = "".join(f"<item><title>{html.escape(p['title'])}</title><link>{URL}/{p['slug']}/</link>"
                    f"<description>{html.escape(p['description'])}</description><pubDate>{p['date']}</pubDate></item>"
                    for p in posts[:20])
    (DIST / "feed.xml").write_text(f'<?xml version="1.0"?><rss version="2.0"><channel><title>{CFG["name"]}</title>'
                                   f"<link>{URL}</link><description>{CFG['description']}</description>{items}</channel></rss>")
    if not BASE and "github.io" not in URL and "example.com" not in URL:
        (DIST / "CNAME").write_text(URL.split("://")[1])
    print(f"Built {len(posts)} posts -> {DIST}")


if __name__ == "__main__":
    build()
