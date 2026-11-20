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
        meta["body_md"] = body
        h = markdown.markdown(body, extensions=["tables", "toc", "attr_list", "sane_lists", "md_in_html"])
        meta["html"] = h.replace("<img ", '<img loading="lazy" decoding="async" ')
        posts.append(meta)
    return sorted(posts, key=lambda p: p["date"], reverse=True)


_V = CFG.get("verification", {})
VERIFY = "".join(f'<meta name="{n}" content="{html.escape(_V[k])}">' for k, n in
                 (("google", "google-site-verification"), ("bing", "msvalidate.01")) if _V.get(k))
SITE_SCHEMA = json.dumps([
    {"@context": "https://schema.org", "@type": "WebSite", "name": CFG["name"],
     "alternateName": [urlparse(URL).netloc, "Stack Verdict"], "url": f"{URL}/"},
    {"@context": "https://schema.org", "@type": "Organization", "name": CFG["name"], "url": f"{URL}/",
     "logo": f"{URL}/icon-512.png", "description": CFG["description"],
     **({"sameAs": CFG["same_as"]} if CFG.get("same_as") else {})}])


def page(title, desc, body, path, extra_head="", image=None, kind="website"):
    canonical = f"{URL}{path}"
    image = image or f"{URL}/og-default.png"
    return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="impact-site-verification" value="9945fcc8-ba51-42b7-b2d4-29688b8ca64f">
{VERIFY}
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canonical}"><meta property="og:type" content="{kind}"><meta property="og:site_name" content="{CFG['name']}">
<meta property="og:image" content="{image}"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{image}">
<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="stylesheet" href="/style.css"><link rel="alternate" type="application/rss+xml" href="/feed.xml">
{extra_head}
</head><body>
<header class="top"><div class="wrap"><a class="logo" href="/"><img src="/favicon.svg" alt="" width="30" height="30"><span>Stack<b>Verdict</b></span></a>
<nav><a href="/">Reviews</a><a href="/frase/">Frase</a><a href="/adcreative/">AdCreative</a><a href="/about/">About</a><a href="/disclosure/">Disclosure</a><a href="/contact/">Contact</a></nav></div></header>
<main class="wrap">{body}</main>
<footer><div class="wrap"><p>{CFG['name']} is reader-supported. Some links are affiliate links: if you buy through them we may earn a commission at no extra cost to you. <a href="/disclosure/">Learn more</a>.</p>
<p>&copy; {datetime.date.today().year} {CFG['name']} · <a href="/privacy/">Privacy</a> · <a href="/contact/">Contact</a></p></div></footer>
</body></html>"""


def signup_box():
    ml = CFG.get("mailerlite")
    if not ml:
        return ""
    action = f"https://assets.mailerlite.com/jsonp/{ml['account']}/forms/{ml['form']}/subscribe"
    return f"""<section class="signup" id="get-the-playbook">
<h2>Get the free Frase Playbook by email</h2>
<p>A 21-page PDF: 7-day trial plan, 28 real screenshots, a plan-picker worksheet and an EEAT editing checklist. Plus occasional new reviews and tutorials.</p>
<form class="signup-form" action="{action}" method="post">
<input type="email" name="fields[email]" placeholder="you@gmail.com" required aria-label="Email address">
<input type="hidden" name="ml-submit" value="1"><input type="hidden" name="anticsrf" value="true">
<button type="submit">Send me the guide</button>
</form>
<p class="signup-ok" hidden>Thanks! Check your inbox. You can also <a href="/downloads/the-frase-playbook.pdf">download the PDF right now</a>.</p>
<p class="signup-small">No spam. Unsubscribe anytime with one click. See our <a href="/privacy/">privacy policy</a>.</p>
</section>
<script>
document.querySelectorAll('.signup-form').forEach(function(f){{f.addEventListener('submit',function(e){{
e.preventDefault();var b=f.querySelector('button');b.disabled=true;b.textContent='Sending…';
var done=function(){{f.hidden=true;f.parentNode.querySelector('.signup-ok').hidden=false;}};
fetch(f.action,{{method:'POST',body:new FormData(f),mode:'no-cors'}}).then(done,done);}});}});
</script>"""


def write(path, content):
    out = DIST / path.lstrip("/") / "index.html" if path.endswith("/") else DIST / path.lstrip("/")
    out.parent.mkdir(parents=True, exist_ok=True)
    content = content.replace('href="/', f'href="{BASE}/').replace('src="/', f'src="{BASE}/')
    out.write_text(content, encoding="utf-8")


HUBS = {
    "frase": ("Frase: Reviews, Tutorials and Comparisons",
              "Everything we've tested and written about Frase, the AI SEO and GEO content platform: our hands-on review, a step-by-step tutorial, pricing, and how it compares with Surfer, Clearscope, NeuronWriter, MarketMuse and Jasper.",
              lambda p: "frase" in p["slug"] or p["slug"] in ("best-content-brief-tools", "what-is-geo")),
    "adcreative": ("AdCreative.ai: Review, Pricing and Comparisons",
                   "Our research on AdCreative.ai, the AI ad-creative generator: an honest review, real cost per ad, alternatives, and how it compares with Canva and Predis.ai.",
                   lambda p: "adcreative" in p["slug"]),
    "ai-seo-tools": ("AI SEO and Content Tools: Comparisons and Buying Guides",
                     "Buying guides and alternatives for AI SEO writing, content brief and content optimization tools.",
                     lambda p: p["slug"] in ("best-ai-seo-writing-tools", "best-content-brief-tools", "surfer-seo-alternatives",
                                             "clearscope-alternatives", "what-is-geo") or "-vs-" in p["slug"] and "adcreative" not in p["slug"]),
}


def hub_of(p):
    if "adcreative" in p["slug"]:
        return "adcreative"
    if "frase" in p["slug"]:
        return "frase"
    return "ai-seo-tools"


def related(p, posts, n=4):
    hub = hub_of(p)
    linked = set(__import__("re").findall(r"\]\(/([a-z0-9-]+)/\)", p["body_md"]))
    pool = [q for q in posts if q["slug"] != p["slug"]]
    # prefer same hub, posts this one doesn't already link to, then least-linked (orphans) first
    pool.sort(key=lambda q: (hub_of(q) != hub, q["slug"] in linked, INBOUND.get(q["slug"], 0)))
    items = "".join(f'<li><a href="/{q["slug"]}/">{html.escape(q["title"])}</a></li>' for q in pool[:n])
    return f'<aside class="related"><h2>Related reading</h2><ul>{items}</ul></aside>'


def faq_schema(md):
    m = __import__("re").search(r"^## (?:FAQ|Frequently asked questions)\s*\n(.*?)(?=^## |\Z)", md, __import__("re").M | __import__("re").S)
    if not m:
        return None
    qa = __import__("re").findall(r"^\*\*(.+?\?)\*\*\s*\n(.+?)(?=\n\s*\n|\Z)", m.group(1), __import__("re").M | __import__("re").S)
    if not qa:
        return None
    clean = lambda t: __import__("re").sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t).replace("**", "").strip()
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": clean(q),
                            "acceptedAnswer": {"@type": "Answer", "text": clean(a)}} for q, a in qa]}


def breadcrumbs(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": f"{URL}{u}"}
                                for i, (n, u) in enumerate(items)]}


INBOUND = {}


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

    import re as _re
    for q in posts:
        for t in set(_re.findall(r"\]\(/([a-z0-9-]+)/\)", q["body_md"])):
            if t != q["slug"]:
                INBOUND[t] = INBOUND.get(t, 0) + 1

    for p in posts:
        img = _re.search(r"!\[[^\]]*\]\((/img/[^) ]+)", p["body_md"])
        p_img = f"{URL}{img.group(1)}" if img else None
        hub = hub_of(p)
        schema = {"@context": "https://schema.org", "@type": "Article", "headline": p["title"],
                  "mainEntityOfPage": f"{URL}/{p['slug']}/", **({"image": p_img} if p_img else {}),
                  "description": p["description"], "datePublished": p["date"],
                  "dateModified": str(p.get("updated", p["date"])),
                  "author": {"@type": "Organization", "name": CFG["author"]},
                  "publisher": {"@type": "Organization", "name": CFG["name"],
                                "logo": {"@type": "ImageObject", "url": f"{URL}/icon-512.png"}}}
        blocks = [schema, breadcrumbs([("Home", "/"), (HUBS[hub][0].split(":")[0], f"/{hub}/"), (p["title"], f"/{p['slug']}/")])]
        fq = faq_schema(p["body_md"])
        if fq:
            blocks.append(fq)
        head = "".join(f'<script type="application/ld+json">{json.dumps(b)}</script>' for b in blocks)
        crumb = (f'<nav class="crumbs"><a href="/">Home</a> › <a href="/{hub}/">{html.escape(HUBS[hub][0].split(":")[0])}</a></nav>')
        notice = ('<p class="notice">Disclosure: this article contains affiliate links. '
                  'We may earn a commission if you buy through them, at no extra cost to you.</p>')
        upd = f" · Updated {p['updated']}" if p.get("updated") else ""
        body = (f'{crumb}<article class="post"><h1>{html.escape(p["title"])}</h1>'
                f'<p class="meta">By {CFG["author"]} · {p["date"]}{upd}</p>{notice}{p["html"]}</article>'
                + related(p, posts) + signup_box())
        title = p.get("seo_title") or p["title"]
        if len(title) + 15 <= 65:
            title = f"{title} | {CFG['name']}"
        write(f"/{p['slug']}/", page(title, p.get("seo_description") or p["description"], body, f"/{p['slug']}/",
                                     head, image=p_img, kind="article"))

    for slug, (htitle, hdesc, match) in HUBS.items():
        hp = [q for q in posts if match(q)]
        hbody = (f'<nav class="crumbs"><a href="/">Home</a></nav><section class="hero"><h1>{html.escape(htitle)}</h1><p>{html.escape(hdesc)}</p></section>'
                 '<div class="grid">' + "".join(card(q) for q in hp) + "</div>")
        hschema = [breadcrumbs([("Home", "/"), (htitle.split(":")[0], f"/{slug}/")]),
                   {"@context": "https://schema.org", "@type": "CollectionPage", "name": htitle, "url": f"{URL}/{slug}/",
                    "hasPart": [{"@type": "Article", "headline": q["title"], "url": f"{URL}/{q['slug']}/"} for q in hp]}]
        write(f"/{slug}/", page(f"{htitle.split(':')[0]} Reviews & Guides | {CFG['name']}"[:65], hdesc[:158], hbody, f"/{slug}/",
                               "".join(f'<script type="application/ld+json">{json.dumps(b)}</script>' for b in hschema)))

    hero = f'<section class="hero"><h1>{CFG["tagline"]}</h1><p>{CFG["description"]}</p></section>'
    write("/", page(f"{CFG['name']} – {CFG['tagline']}", CFG["description"],
                    hero + '<div class="grid">' + "".join(card(p) for p in posts) + "</div>", "/",
                    f'<script type="application/ld+json">{SITE_SCHEMA}</script>'))

    for slug in ("about", "disclosure", "privacy", "contact"):
        f = ROOT / "pages" / f"{slug}.md"
        if f.exists():
            raw = f.read_text(encoding="utf-8")
            title = raw.splitlines()[0].lstrip("# ").strip()
            write(f"/{slug}/", page(f"{title} | {CFG['name']}", title,
                                    f'<article class="post">{markdown.markdown(raw)}</article>', f"/{slug}/"))

    newest = max((str(p.get("updated", p["date"])) for p in posts), default=None)
    urls = ([("/", newest)] + [(f"/{p['slug']}/", str(p.get("updated", p["date"]))) for p in posts]
            + [(f"/{h}/", newest) for h in HUBS] + [(u, None) for u in ("/about/", "/disclosure/", "/privacy/", "/contact/")])
    (DIST / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        + "".join(f"<url><loc>{URL}{u}</loc>" + (f"<lastmod>{d}</lastmod>" if d else "") + "</url>" for u, d in urls)
        + "</urlset>")
    (DIST / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {URL}/sitemap.xml\n")
    items = "".join(f"<item><title>{html.escape(p['title'])}</title><link>{URL}/{p['slug']}/</link>"
                    f"<description>{html.escape(p['description'])}</description><pubDate>{datetime.datetime.strptime(p['date'][:10], '%Y-%m-%d').strftime('%a, %d %b %Y 08:00:00 +0700')}</pubDate></item>"
                    for p in posts[:20])
    (DIST / "feed.xml").write_text(f'<?xml version="1.0"?><rss version="2.0"><channel><title>{CFG["name"]}</title>'
                                   f"<link>{URL}</link><description>{CFG['description']}</description>{items}</channel></rss>")
    if not BASE and "github.io" not in URL and "example.com" not in URL:
        (DIST / "CNAME").write_text(URL.split("://")[1])
    print(f"Built {len(posts)} posts -> {DIST}")


if __name__ == "__main__":
    build()
