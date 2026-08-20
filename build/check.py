#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Post-build checks. Run after generate.py.

    python3 build/check.py

Catches the failure modes that actually bite a static, bilingual SEO site:
broken internal links, missing assets, duplicate or over-long titles and
descriptions, malformed JSON-LD, heading-order mistakes, images without alt,
and — the one specific to this site — hreflang pairs that do not resolve or
do not point back at each other.
"""
import json
import os
import re
import sys
from collections import defaultdict
from html import unescape
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "gmmarineautomation.gr"
errors, warnings = [], []


def err(page, msg):
    errors.append("%s: %s" % (page, msg))


def warn(page, msg):
    warnings.append("%s: %s" % (page, msg))


class Doc(HTMLParser):
    VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
            "meta", "param", "source", "track", "wbr"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links, self.assets, self.imgs = [], [], []
        self.headings, self.stack = [], []
        self.jsonld, self._in_ld = [], False
        self.title, self._in_title = None, False
        self.unclosed = []
        self.lang = None
        self.labelled_controls, self.labels_for, self.control_ids = [], set(), []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag not in self.VOID:
            self.stack.append(tag)
        if tag == "html":
            self.lang = a.get("lang")
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if tag == "img":
            self.imgs.append(a)
            if a.get("src"):
                self.assets.append(a["src"])
        if tag in ("link", "script") and (a.get("href") or a.get("src")):
            self.assets.append(a.get("href") or a.get("src"))
        if tag == "script" and a.get("type") == "application/ld+json":
            self._in_ld = True
        if tag == "title":
            self._in_title = True
        if re.fullmatch(r"h[1-6]", tag):
            self.headings.append(int(tag[1]))
        if tag == "label" and a.get("for"):
            self.labels_for.add(a["for"])
        if tag in ("input", "select", "textarea"):
            if a.get("type") not in ("hidden", "submit", "button"):
                self.control_ids.append((tag, a.get("id"), a.get("type")))

    def handle_endtag(self, tag):
        if tag in self.VOID:
            return
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        elif tag in self.stack:
            while self.stack and self.stack[-1] != tag:
                self.unclosed.append(self.stack.pop())
            if self.stack:
                self.stack.pop()
        if tag == "script":
            self._in_ld = False
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_ld:
            self.jsonld.append(data)
        if self._in_title:
            self.title = (self.title or "") + data


def meta_of(html, name=None, prop=None, rel=None):
    if rel:
        m = re.search(r'<link[^>]+rel="%s"[^>]+href="([^"]*)"' % rel, html)
    elif prop:
        m = re.search(r'<meta[^>]+property="%s"[^>]+content="([^"]*)"' % prop, html)
    else:
        m = re.search(r'<meta[^>]+name="%s"[^>]+content="([^"]*)"' % name, html)
    return m.group(1) if m else None


def alternates_of(html):
    return dict(
        (lg, href) for lg, href in
        re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)">', html))


def collect_pages():
    pages = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames
                       if d not in ("build", "assets", "__pycache__", ".git", "node_modules")]
        for fn in filenames:
            if fn.endswith(".html"):
                pages.append(os.path.join(dirpath, fn))
    return sorted(pages)


def path_to_url(disk):
    rel = "/" + os.path.relpath(disk, ROOT).replace(os.sep, "/")
    return rel.replace("/index.html", "/") if rel.endswith("/index.html") else rel


def main():
    pages = collect_pages()
    titles, descs, canons = defaultdict(list), defaultdict(list), defaultdict(list)
    alt_map = {}          # canonical url -> {lang: url}
    canon_seen = set()

    for path in pages:
        rel = path_to_url(path)
        html = open(path, encoding="utf-8").read()
        d = Doc()
        d.feed(html)

        # --- structure ---
        if d.unclosed:
            err(rel, "mismatched tags: %s" % ", ".join(sorted(set(d.unclosed))))
        if d.stack:
            err(rel, "unclosed tags at EOF: %s" % ", ".join(d.stack))
        if not d.lang:
            err(rel, "no lang attribute on <html>")

        h1s = [h for h in d.headings if h == 1]
        if len(h1s) != 1:
            err(rel, "expected exactly one <h1>, found %d" % len(h1s))
        prev = 0
        for h in d.headings:
            if prev and h > prev + 1:
                warn(rel, "heading jump h%d → h%d" % (prev, h))
            prev = h

        # --- head / SEO ---
        title = (d.title or "").strip()
        if not title:
            err(rel, "missing <title>")
        else:
            titles[title].append(rel)
            if len(title) > 65:
                warn(rel, "title %d chars (>65, may truncate): %s" % (len(title), title))

        desc = meta_of(html, name="description")
        if not desc:
            err(rel, "missing meta description")
        else:
            descs[desc].append(rel)
            if not (70 <= len(desc) <= 165):
                warn(rel, "description %d chars (aim 70–165)" % len(desc))

        canon = meta_of(html, rel="canonical")
        if not canon:
            err(rel, "missing canonical")
        else:
            canons[canon].append(rel)
            expected = "https://www." + DOMAIN + rel
            if canon != expected:
                err(rel, "canonical %s does not match its own path (expected %s)"
                    % (canon, expected))
            canon_seen.add(canon)

        for prop in ("og:title", "og:description", "og:image", "og:url"):
            if not meta_of(html, prop=prop):
                err(rel, "missing %s" % prop)
        if not meta_of(html, name="robots"):
            warn(rel, "no robots meta")

        noindex = "noindex" in (meta_of(html, name="robots") or "")

        # --- hreflang ---
        alts = alternates_of(html)
        if noindex:
            if alts:
                err(rel, "noindex page must not declare hreflang alternates")
        else:
            for need in ("el", "en", "x-default"):
                if need not in alts:
                    err(rel, "missing hreflang=%s" % need)
            if alts.get("x-default") != alts.get("el"):
                err(rel, "x-default should point at the Greek URL")
            if canon and canon not in (alts.get("el"), alts.get("en")):
                err(rel, "hreflang set does not include this page's own canonical")
            alt_map[canon] = alts

        # --- JSON-LD ---
        if not d.jsonld:
            err(rel, "no JSON-LD")
        for blob in d.jsonld:
            try:
                obj = json.loads(blob)
            except json.JSONDecodeError as e:
                err(rel, "invalid JSON-LD: %s" % e)
                continue
            if "@context" not in obj:
                err(rel, "JSON-LD block without @context")
            if "@type" not in obj:
                err(rel, "JSON-LD block without @type")

        # --- images ---
        for a in d.imgs:
            if a.get("alt") is None:
                err(rel, "img without alt: %s" % a.get("src"))
            if not (a.get("width") and a.get("height")):
                warn(rel, "img without width/height (CLS risk): %s" % a.get("src"))

        # --- form controls must be labelled ---
        for tag, cid, ctype in d.control_ids:
            if ctype in ("radio", "checkbox"):
                continue        # wrapped in their <label> by construction
            if not cid:
                err(rel, "%s control without id (cannot be labelled)" % tag)
            elif cid not in d.labels_for:
                err(rel, "control #%s has no <label for>" % cid)

        # --- links and assets resolve on disk ---
        pagedir = os.path.dirname(path)
        for href in d.links + d.assets:
            if href.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:")):
                continue
            target = href.split("#")[0].split("?")[0]
            if not target:
                continue
            if target.startswith("/"):
                base, target = ROOT, (target.lstrip("/") or "index.html")
            else:
                base = pagedir
            disk = os.path.normpath(os.path.join(base, target))
            if os.path.isdir(disk):
                disk = os.path.join(disk, "index.html")
            if not os.path.exists(disk):
                err(rel, "broken link/asset: %s" % href)
            elif not os.path.abspath(disk).startswith(os.path.abspath(ROOT)):
                err(rel, "link escapes project root: %s" % href)

    # --- cross-page uniqueness ---
    for t, where in titles.items():
        if len(where) > 1:
            err("SITE", "duplicate <title> on %s → %r" % (", ".join(where), t))
    for t, where in descs.items():
        if len(where) > 1:
            err("SITE", "duplicate description on %s" % ", ".join(where))
    for c, where in canons.items():
        if len(where) > 1:
            err("SITE", "duplicate canonical %s on %s" % (c, ", ".join(where)))

    # --- hreflang must be reciprocal and must resolve ---
    for canon, alts in alt_map.items():
        for lg, target in alts.items():
            if lg == "x-default":
                continue
            if target not in canon_seen:
                err("SITE", "hreflang=%s on %s points at %s, which is not a page"
                    % (lg, canon, target))
                continue
            back = alt_map.get(target, {})
            if canon not in (back.get("el"), back.get("en")):
                err("SITE", "hreflang not reciprocal: %s → %s does not link back"
                    % (canon, target))

    # --- sitemap ---
    sm = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(sm):
        err("SITE", "sitemap.xml missing")
    else:
        smx = open(sm, encoding="utf-8").read()
        locs = re.findall(r"<loc>([^<]+)</loc>", smx)
        if len(locs) != len(set(locs)):
            err("SITE", "sitemap contains duplicate <loc> entries")
        indexable = set()
        for path in pages:
            h = open(path, encoding="utf-8").read()
            if "noindex" in (meta_of(h, name="robots") or ""):
                continue
            indexable.add(path_to_url(path))
        in_sitemap = {u.split(DOMAIN)[-1] or "/" for u in locs}
        for miss in sorted(indexable - in_sitemap):
            err("SITE", "indexable page missing from sitemap: %s" % miss)
        for extra in sorted(in_sitemap - indexable):
            err("SITE", "sitemap lists non-existent/noindex page: %s" % extra)

    # --- robots ---
    rb = os.path.join(ROOT, "robots.txt")
    if not os.path.exists(rb):
        err("SITE", "robots.txt missing")
    elif "Sitemap:" not in open(rb, encoding="utf-8").read():
        err("SITE", "robots.txt does not reference the sitemap")

    # --- launch readiness -------------------------------------------------
    todo = defaultdict(list)
    for path in pages:
        rel = path_to_url(path)
        body = re.sub(r"<script.*?</script>", "", open(path, encoding="utf-8").read(),
                      flags=re.S)
        body = unescape(body)
        for tok in re.findall(r"\[[Α-ΩΆΈΉΊΌΎΏA-Z][Α-ΩΆΈΉΊΌΎΏA-Z0-9 .&]*\]", body):
            todo[tok].append(rel)
    photo_slots = sum(
        open(p, encoding="utf-8").read().count('<figure class="photo-slot')
        for p in pages)

    if todo or photo_slots:
        print("LAUNCH TODO")
        for tok, where in sorted(todo.items()):
            print("  · %-18s %d page(s): %s" % (tok, len(where), ", ".join(sorted(where)[:4])))
        if photo_slots:
            print("  · photo placeholders  %d slot(s) awaiting the client's onboard photography"
                  % photo_slots)
        print()

    # --- report ---
    print("Checked %d pages." % len(pages))
    langs = defaultdict(int)
    for p in pages:
        m = re.search(r'<html lang="([^"]+)"', open(p, encoding="utf-8").read())
        if m:
            langs[m.group(1)] += 1
    print("  " + ", ".join("%s: %d" % (k, v) for k, v in sorted(langs.items())) + "\n")

    if warnings:
        print("WARNINGS (%d)" % len(warnings))
        for w in warnings:
            print("  ! " + w)
        print()
    if errors:
        print("ERRORS (%d)" % len(errors))
        for e in errors:
            print("  ✗ " + e)
        return 1
    print("No errors.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
