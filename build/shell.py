#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The document shell: <head>, header, footer, schema.org, link rewriting.

Nothing here runs at request time. generate.py stitches this together with the
content modules and writes plain HTML; the deployed site has no dependencies.
"""
import html
import json
import re

import brand as B
from brand import t, url

# ---------------------------------------------------------------------------
def esc(s):
    return html.escape(str(s), quote=True)


def jsonld(obj):
    return ('<script type="application/ld+json">'
            + json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
            + "</script>")


# --- Schema -----------------------------------------------------------------
def organization_schema(lang):
    desc = {
     "el": ("Ναυτιλιακά ηλεκτρολογικά και συστήματα αυτοματισμού για πλοία και σκάφη: "
            "γεννήτριες, power management, DEIF, παραλληλισμός, alarm monitoring, "
            "switchboards, PLC/SCADA, retrofit και onboard troubleshooting."),
     "en": ("Marine electrical and automation systems for ships and yachts: generators, "
            "power management, DEIF, synchronizing, alarm monitoring, switchboards, "
            "PLC/SCADA, retrofit and onboard troubleshooting."),
    }[lang]
    return {
        "@context": "https://schema.org",
        "@type": ["Organization", "ProfessionalService", "LocalBusiness"],
        "@id": B.BASE + "/#organization",
        "name": B.BRAND,
        "alternateName": B.BRAND_SHORT,
        "slogan": B.TAGLINE_EN,
        "url": B.BASE + "/",
        "logo": {"@type": "ImageObject", "url": B.BASE + B.OG_IMAGE},
        "image": B.BASE + B.OG_IMAGE,
        "description": desc,
        "foundingDate": str(B.FOUNDED),
        "email": B.EMAIL,
        "telephone": B.PHONE_E164,
        "priceRange": "$$",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": B.STREET if lang == "el" else B.STREET_EN,
            "addressLocality": B.CITY_EL if lang == "el" else B.CITY_EN,
            "addressRegion": B.REGION_EL if lang == "el" else B.REGION_EN,
            "addressCountry": B.COUNTRY,
        },
        "hasMap": B.MAP_LINK,
        "areaServed": [
            {"@type": "Country", "name": "Greece"},
            {"@type": "Place", "name": "Piraeus"},
            {"@type": "Place", "name": "Perama"},
            {"@type": "Place", "name": "Elefsina"},
            {"@type": "Place", "name": "Worldwide marine service"},
        ],
        "knowsAbout": [
            "Marine electrical systems", "Marine automation", "Power management systems",
            "Generator synchronizing", "Load sharing", "DEIF generator controllers",
            "Alarm monitoring systems", "Marine switchboards", "PLC HMI SCADA",
            "Marine troubleshooting", "Commissioning and sea trials", "Modbus", "CAN bus",
        ],
        "knowsLanguage": ["el", "en"],
        "founder": {
            "@type": "Person",
            "name": B.CONTACT_NAME_EL if lang == "el" else B.CONTACT_NAME_EN,
            "jobTitle": "Founder & Technical Director",
        },
        "contactPoint": [{
            "@type": "ContactPoint",
            "contactType": "technical support",
            "telephone": B.PHONE_E164,
            "email": B.EMAIL,
            "availableLanguage": ["el", "en"],
            "areaServed": "Worldwide",
        }],
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "opens": "08:00", "closes": "18:00",
        }],
    }


def website_schema(lang):
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "@id": B.BASE + "/#website-" + lang,
        "url": B.BASE + url("home", lang),
        "name": B.BRAND_SHORT,
        "inLanguage": B.HTML_LANG[lang],
        "publisher": {"@id": B.BASE + "/#organization"},
    }


def breadcrumb_schema(trail):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": label, "item": B.BASE + path}
            for i, (path, label) in enumerate(trail)
        ],
    }


def faq_schema(pairs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in pairs
        ],
    }


# --- Markup fragments -------------------------------------------------------
def crumbs_html(trail, lang):
    if len(trail) < 2:
        return ""
    items = []
    for i, (path, label) in enumerate(trail):
        if i == len(trail) - 1:
            items.append('<li><span aria-current="page">%s</span></li>' % esc(label))
        else:
            items.append('<li><a href="%s">%s</a></li>' % (esc(path), esc(label)))
    return ('<nav class="crumbs" aria-label="%s"><div class="wrap"><ol>%s</ol></div></nav>'
            % (esc(t(lang, "crumbs_label")), "".join(items)))


def logo_svg():
    """Wordmark glyph: the IEC single-line symbol for a generator — a circle with
    a sine wave. Chosen because it is what this trade actually draws, not a
    decorative icon."""
    return ('<svg class="brand__mark" viewBox="0 0 40 40" aria-hidden="true" focusable="false">'
            '<circle cx="20" cy="20" r="17" fill="none" stroke="currentColor" stroke-width="2"/>'
            '<path d="M10 20c0-4 2.2-6 5-6s5 2 5 6 2.2 6 5 6 5-2 5-6" fill="none" '
            'stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>')


def header_html(active_id, lang, alt_url):
    links = []
    for pid, labels in B.NAV:
        cur = ' aria-current="page"' if pid == active_id else ""
        links.append('<li><a class="nav__link" href="%s"%s>%s</a></li>'
                     % (esc(url(pid, lang)), cur, esc(labels[lang])))
    other = "en" if lang == "el" else "el"
    return """<div class="topbar">
  <div class="wrap topbar__inner">
    <p class="topbar__alert"><span class="pulse" aria-hidden="true"></span>{emergency}</p>
    <div class="topbar__links">
      <a href="tel:{phone_e164}">{phone_human}</a>
      <a href="mailto:{email}">{email}</a>
      <a class="topbar__lang" href="{alt_url}" hreflang="{other}" lang="{other}"
         aria-label="{lang_label}: {lang_other}">{lang_other}</a>
    </div>
  </div>
</div>

<header class="site-header">
  <div class="wrap site-header__inner">
    <a class="brand" href="{home}">
      {logo}
      <span class="brand__text">
        <span class="brand__name">GM <b>Marine Automation</b></span>
        <span class="brand__tag">&amp; Electrical System</span>
      </span>
    </a>

    <button class="nav-toggle" type="button" aria-expanded="false"
            aria-controls="primary-nav" aria-label="{menu_open}">
      <span class="nav-toggle__bars" aria-hidden="true"></span>
    </button>

    <nav class="nav" id="primary-nav" aria-label="{nav_label}">
      <ul class="nav__list">
        {links}
      </ul>
      <a class="btn btn--accent nav__cta" href="{contact}">{cta}</a>
    </nav>
  </div>
</header>""".format(
        emergency=esc(t(lang, "emergency")), phone_e164=B.PHONE_E164,
        phone_human=B.PHONE_HUMAN, email=B.EMAIL, alt_url=esc(alt_url), other=other,
        lang_label=esc(t(lang, "lang_label")), lang_other=esc(t(lang, "lang_other")),
        home=esc(url("home", lang)), logo=logo_svg(),
        menu_open=esc(t(lang, "menu_open")), nav_label=esc(t(lang, "nav_label")),
        links="\n        ".join(links), contact=esc(url("contact", lang)),
        cta=esc(t(lang, "cta_quote")))


def footer_html(lang, services):
    """`services` is the list of service dicts shown in the footer column."""
    svc = "\n        ".join(
        '<li><a href="%s">%s</a></li>'
        % (esc(url("service", lang, s["slug"])), esc(s[lang]["name_short"]))
        for s in services)
    pages = "\n        ".join(
        '<li><a href="%s">%s</a></li>' % (esc(url(pid, lang)), esc(labels[lang]))
        for pid, labels in B.NAV if pid != "home")
    addr_street = B.STREET if lang == "el" else B.STREET_EN
    addr_city = B.CITY_EL if lang == "el" else B.CITY_EN
    return """<footer class="site-footer">
  <div class="wrap">
    <div class="footer__grid">
      <div class="footer__brand">
        <a class="brand" href="{home}">
          {logo}
          <span class="brand__text">
            <span class="brand__name">GM <b>Marine Automation</b></span>
            <span class="brand__tag">&amp; Electrical System</span>
          </span>
        </a>
        <p class="footer__blurb">{tagline}</p>
        <dl class="footer__meta">
          <dt>{areas_l}</dt><dd>{areas_v}</dd>
          <dt>{hours_l}</dt><dd>{hours_week} {hours_week_v}<br>{hours_sat}: {hours_sat_v}</dd>
        </dl>
      </div>

      <div class="footer__col">
        <h2 class="footer__h">{services_col}</h2>
        <ul class="footer__list">
        {svc}
        </ul>
        <p class="footer__more"><a href="{services_url}">{all_services} &rarr;</a></p>
      </div>

      <div class="footer__col">
        <h2 class="footer__h">{company_col}</h2>
        <ul class="footer__list">
        {pages}
        </ul>
      </div>

      <div class="footer__col">
        <h2 class="footer__h">{contact_col}</h2>
        <ul class="footer__list footer__list--contact">
          <li><a href="tel:{phone_e164}">{phone_human}</a></li>
          <li><a href="mailto:{email}">{email}</a></li>
          <li><a href="https://wa.me/{whatsapp}" rel="noopener">WhatsApp / Viber</a></li>
          <li class="footer__addr">{street}<br>{city}, {country}</li>
        </ul>
        <p class="footer__emergency">{emergency}</p>
      </div>
    </div>

    <div class="footer__bottom">
      <p>&#169; <span data-year>2026</span> {brand}. {legal}</p>
      <p>{by}: <a href="https://braingroup.tech" rel="noopener">BRAIN GROUP</a></p>
    </div>
  </div>
</footer>""".format(
        home=esc(url("home", lang)), logo=logo_svg(), tagline=esc(B.TAGLINE_EN),
        areas_l=esc(t(lang, "areas")), areas_v=t(lang, "areas_v"),
        hours_l=esc(t(lang, "hours_title")), hours_week=esc(t(lang, "hours_week")),
        hours_week_v=esc(t(lang, "hours_week_v")), hours_sat=esc(t(lang, "hours_sat")),
        hours_sat_v=esc(t(lang, "hours_sat_v")),
        services_col=esc(t(lang, "services_col")), svc=svc,
        services_url=esc(url("services", lang)), all_services=esc(t(lang, "all_services")),
        company_col=esc(t(lang, "company_col")), pages=pages,
        contact_col=esc(t(lang, "contact_col")), phone_e164=B.PHONE_E164,
        phone_human=B.PHONE_HUMAN, email=B.EMAIL, whatsapp=B.WHATSAPP,
        street=esc(addr_street), city=esc(addr_city),
        country="Greece" if lang == "en" else "Ελλάδα",
        emergency=esc(t(lang, "emergency")), brand=esc(B.BRAND),
        legal=esc(t(lang, "footer_legal")), by=t(lang, "footer_by"))


def whatsapp_fab(lang):
    label = "WhatsApp" if lang == "en" else "Επικοινωνία μέσω WhatsApp"
    return ('<a class="fab-whatsapp" href="https://wa.me/%s" rel="noopener" aria-label="%s">'
            '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" width="24" height="24">'
            '<path fill="currentColor" d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 '
            '4.95L2 22l5.25-1.38a9.86 9.86 0 0 0 4.79 1.22h.01c5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-'
            '5.14-2.9-7.01A9.82 9.82 0 0 0 12.04 2Zm0 18.15h-.01a8.2 8.2 0 0 1-4.19-1.15l-.3-.18-3.12.82'
            '.83-3.04-.2-.31a8.19 8.19 0 0 1-1.26-4.38c0-4.54 3.7-8.23 8.25-8.23 2.2 0 4.27.86 5.83 '
            '2.41a8.18 8.18 0 0 1 2.41 5.83c0 4.54-3.7 8.23-8.24 8.23Zm4.52-6.16c-.25-.12-1.47-.72-1.69'
            '-.81-.23-.08-.39-.12-.56.13-.16.24-.64.8-.78.97-.15.16-.29.18-.53.06-.25-.12-1.05-.39-1.99'
            '-1.23-.74-.66-1.23-1.47-1.38-1.72-.14-.25-.01-.38.11-.5.11-.11.25-.29.37-.43.12-.15.16-.25'
            '.25-.41.08-.17.04-.31-.02-.43-.06-.12-.56-1.34-.76-1.84-.2-.48-.4-.42-.56-.43h-.48c-.16 0-'
            '.43.06-.65.31-.22.25-.85.83-.85 2.02 0 1.19.87 2.34.99 2.5.12.16 1.71 2.61 4.14 3.66.58.25'
            '1.03.4 1.38.51.58.19 1.11.16 1.53.1.47-.07 1.47-.6 1.67-1.18.21-.58.21-1.07.15-1.18-.06-.1'
            '2-.22-.19-.47-.31Z"/></svg></a>' % (B.WHATSAPP, esc(label)))


# --- Link rewriting ---------------------------------------------------------
# Pages are authored with root-absolute internal links, which is the clearest
# way to write them. They are rewritten to page-relative links on output so the
# folder also opens by double-clicking index.html — under file:// a leading "/"
# resolves to the filesystem root. Relative links behave identically over HTTP.
# Absolute URLs (canonical, og:url, hreflang, JSON-LD) stay untouched.
_LINK_RE = re.compile(r'\b(href|src)="(/(?!/)[^"]*)"')


def relativize(html_text, file_path):
    """Rewrite root-absolute href/src into links relative to `file_path`."""
    depth = file_path.count("/")
    prefix = "../" * depth

    def swap(m):
        attr, u = m.group(1), m.group(2)
        target = (u + "index.html") if u.endswith("/") else u
        return '%s="%s%s"' % (attr, prefix, target.lstrip("/"))

    return _LINK_RE.sub(swap, html_text)


# --- Page shell -------------------------------------------------------------
def page(path, lang, title, description, body, alt_path, trail=None, schemas=None,
         active=None, og_image=None, footer_services=(), relative=True,
         noindex=False, og_type="website", extra_head=""):
    """Render one complete HTML document.

    `alt_path` is the same page in the other language — it drives hreflang, so
    it must always point at a page that exists.
    relative=False keeps root-absolute links, used for 404.html which the server
    serves at arbitrary request depths where relative paths would break.
    """
    file_path = B.file_for(path)
    canonical = B.BASE + path
    trail = trail or []
    og = og_image or B.OG_IMAGE
    other = "en" if lang == "el" else "el"

    graph = [organization_schema(lang), website_schema(lang)]
    if len(trail) >= 2:
        graph.append(breadcrumb_schema(trail))
    graph.extend(schemas or [])
    head_schema = "\n  ".join(jsonld(s) for s in graph)

    el_url = B.BASE + (path if lang == "el" else alt_path)
    en_url = B.BASE + (path if lang == "en" else alt_path)

    robots = ("noindex, follow" if noindex else
              "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1")
    alternates = "" if noindex else """
  <link rel="alternate" hreflang="el" href="{el}">
  <link rel="alternate" hreflang="en" href="{en}">
  <link rel="alternate" hreflang="x-default" href="{el}">""".format(el=el_url, en=en_url)

    doc = """<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- Marks the document as scripted before first paint, so the entrance
       animations can start hidden. Without JS the class never lands and every
       element is simply visible, which is the whole point of doing it here. -->
  <script>document.documentElement.className+=" js";</script>
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical}">
  <meta name="robots" content="{robots}">
  <meta name="author" content="{brand}">
  <meta name="geo.region" content="GR-A1">
  <meta name="geo.placename" content="{geocity}">{alternates}

  <meta property="og:type" content="{og_type}">
  <meta property="og:locale" content="{og_locale}">
  <meta property="og:site_name" content="{brand_short}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{base}{og}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="{brand_short} — marine electrical &amp; automation systems">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{base}{og}">

  <meta name="theme-color" content="#0a1a26">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;600;700&amp;family=Roboto+Mono:wght@400;500&amp;display=swap">
  <link rel="stylesheet" href="/assets/css/site.css">
{extra_head}
  {head_schema}
</head>
<body>
  <a class="skip-link" href="#main">{skip}</a>
{header}
{crumbs}
  <main id="main">
{body}
  </main>
{footer}
{fab}
  <script src="/assets/js/site.js" defer></script>
</body>
</html>
""".format(
        lang=B.HTML_LANG[lang], title=esc(title), description=esc(description),
        canonical=canonical, robots=robots, brand=esc(B.BRAND),
        brand_short=esc(B.BRAND_SHORT), alternates=alternates,
        geocity=esc(B.CITY_EN), og_type=og_type, og_locale=B.OG_LOCALE[lang],
        base=B.BASE, og=og, extra_head=extra_head, head_schema=head_schema,
        skip=esc(t(lang, "skip")),
        header=header_html(active, lang, alt_path),
        crumbs=crumbs_html(trail, lang), body=body,
        footer=footer_html(lang, footer_services), fab=whatsapp_fab(lang))

    return relativize(doc, file_path) if relative else doc
