#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Builds the site.

    python3 build/generate.py
    python3 build/check.py

Writes every .html page in both languages, plus sitemap.xml and robots.txt.
The output is committed and served directly; there is no runtime.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import brand as B
import shell
import ui
from articles import ARTICLES
from brand import NAV, t, url
from pagecopy import COPY
from photos import BY_SERVICE, PHOTOS
from services import FEATURED, SERVICES, BY_SLUG
from shell import esc, faq_schema

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOOTER_SERVICES = FEATURED[:6]
WRITTEN = []


def write(path, html_text):
    disk = os.path.join(ROOT, B.file_for(path))
    os.makedirs(os.path.dirname(disk), exist_ok=True)
    with open(disk, "w", encoding="utf-8") as f:
        f.write(html_text)
    WRITTEN.append(path)


def nav_label(pid, lang):
    return dict(NAV)[pid][lang]


def home_crumb(lang):
    return (url("home", lang), nav_label("home", lang))


# ===========================================================================
# Components used across pages
# ===========================================================================
def service_card(s, lang, num=None):
    idx = ('<span class="card__idx">%02d</span>' % num) if num else ""
    return """<a class="card card--service" href="{href}">
        {idx}
        <span class="card__icon">{icon}</span>
        <span class="card__body">
          <span class="card__title">{name}</span>
          <span class="card__text">{short}</span>
        </span>
        <span class="card__go" aria-hidden="true">&rarr;</span>
      </a>""".format(
        href=esc(url("service", lang, s["slug"])), idx=idx, icon=ui.icon(s["icon"]),
        name=esc(s[lang]["name"]), short=esc(s[lang]["desc"].split(".")[0] + "."))


def article_card(a, lang):
    return """<a class="card card--article" href="{href}">
        <span class="card__meta"><time datetime="{date}">{date}</time><span>{mins} {reading}</span></span>
        <span class="card__title">{title}</span>
        <span class="card__text">{excerpt}</span>
        <span class="card__go" aria-hidden="true">&rarr;</span>
      </a>""".format(
        href=esc(url("article", lang, a["slug"])), date=a["date"], mins=a["reading"],
        reading=esc(t(lang, "reading")), title=esc(a[lang]["title"]),
        excerpt=esc(a[lang]["excerpt"]))


def cta_band(lang, c):
    return """<section class="band band--cta">
  <div class="wrap band__inner">
    <div>
      <h2>{h2}</h2>
      <p>{p}</p>
    </div>
    <div class="band__actions">
      <a class="btn btn--accent btn--lg" href="{contact}">{cta}</a>
      <a class="btn btn--ghost btn--lg" href="tel:{tel}">{call} {phone}</a>
    </div>
  </div>
</section>""".format(
        h2=esc(c["cta_h2"]), p=esc(c["cta_p"]), contact=esc(url("contact", lang)),
        cta=esc(t(lang, "cta_quote_long")), tel=B.PHONE_E164,
        call=esc(t(lang, "cta_call")), phone=B.PHONE_HUMAN)


# ===========================================================================
# Pages
# ===========================================================================
def page_home(lang):
    c = COPY[lang]
    path, alt = url("home", lang), url("home", "en" if lang == "el" else "el")

    hero = """<section class="hero">
  <div class="wrap hero__inner">
    <div class="hero__copy">
      <p class="eyebrow eyebrow--accent">{eyebrow}</p>
      <h1>{h1}</h1>
      <p class="hero__lead">{lead}</p>
      <div class="hero__actions">
        <a class="btn btn--accent btn--lg" href="{contact}">{cta}</a>
        <a class="btn btn--ghost btn--lg" href="{services}">{all_s}</a>
      </div>
    </div>
    <div class="hero__figure" aria-hidden="false">
      {sld}
      <p class="hero__figcap">{figcap}</p>
    </div>
  </div>
  <div class="wrap">{stats}</div>
</section>""".format(
        eyebrow=esc(c["hero_eyebrow"]), h1=esc(c["hero_h1"]), lead=esc(c["hero_lead"]),
        contact=esc(url("contact", lang)), cta=esc(t(lang, "cta_quote")),
        services=esc(url("services", lang)), all_s=esc(t(lang, "all_services")),
        sld=ui.single_line_diagram(),
        figcap=esc("Παραλληλισμός γεννητριών σε κύριο πίνακα, tie breaker και πίνακας ανάγκης — "
                   "το πεδίο στο οποίο δουλεύουμε."
                   if lang == "el" else
                   "Generators paralleled onto a main switchboard, tie breaker and emergency board — "
                   "the field we work in."),
        stats=ui.stat_strip(c["hero_stats"]))

    intro = ui.section(
        """<div class="split">
      <div class="split__l">
        %s
      </div>
      <div class="split__r">
        %s
      </div>
    </div>""" % (
            ui.head(c["intro_eyebrow"], c["intro_h2"]),
            "\n        ".join("<p>%s</p>" % esc(p) for p in c["intro_p"])),
        cls="section--intro")

    featured = ui.section(
        ui.head(None, c["services_featured_h2"], c["services_lead"]) +
        '\n    <div class="grid grid--3">\n      ' +
        "\n      ".join(service_card(s, lang) for s in FEATURED) +
        '\n    </div>\n    <p class="sec-more"><a class="link-arrow" href="%s">%s &rarr;</a></p>'
        % (esc(url("services", lang)), esc(t(lang, "all_services"))),
        cls="section--services")

    why_items = "\n      ".join(
        '<div class="feature"><span class="feature__no">%02d</span>'
        '<h3>%s</h3><p>%s</p></div>' % (i + 1, esc(h), esc(p))
        for i, (h, p) in enumerate(c["why_items"]))
    why = ui.section(
        ui.head(c["why_eyebrow"], c["why_h2"]) +
        '\n    <div class="grid grid--4 grid--features">\n      %s\n    </div>' % why_items,
        cls="section--dark")

    sectors_items = "\n      ".join(
        '<div class="tile"><h3>%s</h3><p>%s</p></div>' % (esc(h), esc(p))
        for h, p in c["sectors_items"])
    sectors = ui.section(
        ui.head(c["sectors_eyebrow"], c["sectors_h2"], c["sectors_p"]) +
        '\n    <div class="grid grid--4">\n      %s\n    </div>' % sectors_items)

    steps = "\n      ".join(
        '<li class="step"><span class="step__no">%02d</span>'
        '<h3 class="step__h">%s</h3><p>%s</p></li>' % (i + 1, esc(h), esc(p))
        for i, (h, p) in enumerate(c["process_steps"]))
    process = ui.section(
        ui.head(c["process_eyebrow"], c["process_h2"]) +
        '\n    <ol class="steps">\n      %s\n    </ol>' % steps,
        cls="section--process")

    arts = ui.section(
        ui.head(c["articles_eyebrow"], c["articles_h2"], c["articles_p"]) +
        '\n    <div class="grid grid--3">\n      ' +
        "\n      ".join(article_card(a, lang) for a in ARTICLES[:3]) +
        '\n    </div>\n    <p class="sec-more"><a class="link-arrow" href="%s">%s &rarr;</a></p>'
        % (esc(url("insights", lang)), esc(nav_label("insights", lang))))

    faq = ui.section(
        '<div class="faq-wrap">\n    %s\n    </div>'
        % ui.faq_block(c["home_faq"], lang, c["home_faq_h2"]),
        cls="section--faq")

    body = "\n".join([hero, intro, featured, why, sectors, process, arts, faq,
                      cta_band(lang, c)])

    return shell.page(
        path, lang, c["home_title"], c["home_desc"], body, alt,
        active="home", footer_services=FOOTER_SERVICES,
        schemas=[faq_schema(c["home_faq"])])


def page_services(lang):
    c = COPY[lang]
    path, alt = url("services", lang), url("services", "en" if lang == "el" else "el")
    trail = [home_crumb(lang), (path, nav_label("services", lang))]

    intro = """<section class="page-head">
  <div class="wrap">
    <h1>{h1}</h1>
    <p class="page-head__lead">{lead}</p>
  </div>
</section>""".format(h1=esc(c["services_h1"]), lead=esc(c["services_lead"]))

    featured = ui.section(
        ui.head(None, c["services_featured_h2"]) +
        '\n    <div class="grid grid--3">\n      ' +
        "\n      ".join(service_card(s, lang) for s in FEATURED) +
        "\n    </div>")

    rest = [s for s in SERVICES if s not in FEATURED]
    all_rows = "\n      ".join(
        service_card(s, lang, num=i + 1) for i, s in enumerate(rest))
    everything = ui.section(
        ui.head(None, c["services_all_h2"]) +
        '\n    <div class="grid grid--3">\n      %s\n    </div>' % all_rows,
        cls="section--alt")

    item_list = {
        "@context": "https://schema.org", "@type": "ItemList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": s[lang]["name"],
             "url": B.BASE + url("service", lang, s["slug"])}
            for i, s in enumerate(SERVICES)],
    }

    body = "\n".join([intro, featured, everything, cta_band(lang, c)])
    return shell.page(path, lang, c["services_title"], c["services_desc"], body, alt,
                      trail=trail, active="services", footer_services=FOOTER_SERVICES,
                      schemas=[item_list])


def page_service(lang, s):
    c, d = COPY[lang], s[lang]
    path = url("service", lang, s["slug"])
    alt = url("service", "en" if lang == "el" else "el", s["slug"])
    trail = [home_crumb(lang), (url("services", lang), nav_label("services", lang)),
             (path, d["name"])]

    intro = """<section class="page-head page-head--service">
  <div class="wrap page-head__inner">
    <div>
      <p class="eyebrow eyebrow--accent">{kicker}</p>
      <h1>{h1}</h1>
      {lead}
    </div>
    <div class="page-head__icon" aria-hidden="true">{icon}</div>
  </div>
</section>""".format(
        kicker=esc(nav_label("services", lang)), h1=esc(d["name"]),
        lead="\n      ".join('<p class="page-head__lead">%s</p>' % esc(p) for p in d["lead"]),
        icon=ui.icon(s["icon"]))

    aside = """<aside class="aside">
        <div class="aside__card">
          <h2 class="aside__h">{panel_h}</h2>
          <p>{panel_p}</p>
          <a class="btn btn--accent btn--full" href="{contact}">{cta}</a>
          <a class="btn btn--ghost btn--full" href="tel:{tel}">{phone}</a>
          <p class="aside__note">{emergency}</p>
        </div>
        <div class="aside__card aside__card--plain">
          <h2 class="aside__h">{related}</h2>
          <ul class="aside__list">
          {rel}
          </ul>
          <p class="aside__more"><a class="link-arrow" href="{services}">{all_s} &rarr;</a></p>
        </div>
      </aside>""".format(
        panel_h=esc(t(lang, "contact_panel_title")), panel_p=esc(t(lang, "contact_panel_text")),
        contact=esc(url("contact", lang)), cta=esc(t(lang, "cta_quote")),
        tel=B.PHONE_E164, phone=B.PHONE_HUMAN, emergency=esc(t(lang, "emergency")),
        related=esc(t(lang, "related")),
        rel="\n          ".join(
            '<li><a href="%s">%s</a></li>'
            % (esc(url("service", lang, r)), esc(BY_SLUG[r][lang]["name"]))
            for r in s["related"]),
        services=esc(url("services", lang)), all_s=esc(t(lang, "all_services")))

    blocks = [
        ("scope", d["scope"], "ul"),
        ("symptoms", d["symptoms"], "ul"),
        ("deliverables", d["deliverables"], "ul"),
        ("equipment", d["equipment"], "ul"),
    ]
    article = []
    for key, items, kind in blocks:
        article.append('<section class="block">\n      <h2>%s</h2>\n      %s\n    </section>'
                       % (t(lang, key), ui.ul(items)))
    shots = BY_SERVICE.get(s["slug"])
    if shots:
        # Real photographs of this exact work, so the page is not only prose.
        article.append(
            '<section class="block">\n      <h2>%s</h2>\n      %s\n    </section>'
            % (t(lang, "from_field"),
               ui.photo_grid(lang, shots, "4 / 3",
                             "grid grid--2" if len(shots) > 1 else "photo-solo")))
    article.append('<section class="block">\n    %s\n    </section>'
                   % ui.faq_block(d["faq"], lang, t(lang, "faq")))

    main = """<div class="wrap layout">
      <article class="layout__main">
      {article}
      </article>
      {aside}
    </div>""".format(article="\n      ".join(article), aside=aside)

    service_schema = {
        "@context": "https://schema.org", "@type": "Service",
        "name": d["name"], "description": d["desc"],
        "serviceType": s["en"]["name"],
        "provider": {"@id": B.BASE + "/#organization"},
        "areaServed": [{"@type": "Country", "name": "Greece"},
                       {"@type": "Place", "name": "Worldwide marine service"}],
        "url": B.BASE + path,
        "hasOfferCatalog": {
            "@type": "OfferCatalog", "name": d["name"],
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": item}}
                for item in d["scope"]],
        },
    }

    body = '<section class="section section--service">%s</section>' % main
    body = "\n".join([intro, body, cta_band(lang, c)])
    return shell.page(path, lang, d["title"], d["desc"], body, alt, trail=trail,
                      active="services", footer_services=FOOTER_SERVICES,
                      schemas=[service_schema, faq_schema(d["faq"])])


def page_projects(lang):
    c = COPY[lang]
    path, alt = url("projects", lang), url("projects", "en" if lang == "el" else "el")
    trail = [home_crumb(lang), (path, nav_label("projects", lang))]

    intro = """<section class="page-head">
  <div class="wrap">
    <h1>{h1}</h1>
    <p class="page-head__lead">{lead}</p>
  </div>
</section>""".format(h1=esc(c["projects_h1"]), lead=esc(c["projects_lead"]))

    note = """<section class="section section--tight">
  <div class="wrap">
    <div class="callout">
      <h2 class="callout__h">{h}</h2>
      <p>{p}</p>
    </div>
  </div>
</section>""".format(h=esc(c["projects_note_h"]), p=esc(c["projects_note"]))

    cards = []
    for i, (title, desc, points, slug) in enumerate(c["projects_types"], 1):
        cards.append("""<article class="project">
        <p class="project__no">{no:02d}</p>
        <div class="project__body">
          <h2>{title}</h2>
          <p class="project__desc">{desc}</p>
          {ul}
          <p class="project__link"><a class="link-arrow" href="{href}">{label} &rarr;</a></p>
        </div>
      </article>""".format(
            no=i, title=esc(title), desc=esc(desc), ul=ui.ul(points, "list list--tight"),
            href=esc(url("service", lang, slug)),
            label=esc(BY_SLUG[slug][lang]["name"])))

    grid = ui.section('<div class="projects">\n      %s\n    </div>' % "\n      ".join(cards))

    photos = ui.section(
        ui.head(None,
                "Φωτογραφικό υλικό έργων" if lang == "el" else "Project photography",
                "Φωτογραφίες από πραγματικές εργασίες onboard και στον πάγκο."
                if lang == "el" else
                "Photographs from real work onboard and on the bench.") +
        "\n    " + ui.photo_grid(lang, PHOTOS),
        cls="section--alt")

    item_list = {
        "@context": "https://schema.org", "@type": "ItemList",
        "name": c["projects_h1"],
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": title}
            for i, (title, _, _, _) in enumerate(c["projects_types"])],
    }

    body = "\n".join([intro, note, grid, photos, cta_band(lang, c)])
    return shell.page(path, lang, c["projects_title"], c["projects_desc"], body, alt,
                      trail=trail, active="projects", footer_services=FOOTER_SERVICES,
                      schemas=[item_list])


def page_insights(lang):
    c = COPY[lang]
    path, alt = url("insights", lang), url("insights", "en" if lang == "el" else "el")
    trail = [home_crumb(lang), (path, nav_label("insights", lang))]

    intro = """<section class="page-head">
  <div class="wrap">
    <h1>{h1}</h1>
    <p class="page-head__lead">{lead}</p>
  </div>
</section>""".format(h1=esc(nav_label("insights", lang)), lead=esc(c["articles_p"]))

    grid = ui.section(
        '<div class="grid grid--3">\n      %s\n    </div>'
        % "\n      ".join(article_card(a, lang) for a in ARTICLES))

    blog = {
        "@context": "https://schema.org", "@type": "Blog",
        "name": nav_label("insights", lang), "url": B.BASE + path,
        "inLanguage": B.HTML_LANG[lang],
        "publisher": {"@id": B.BASE + "/#organization"},
        "blogPost": [
            {"@type": "BlogPosting", "headline": a[lang]["title"],
             "url": B.BASE + url("article", lang, a["slug"]),
             "datePublished": a["date"]}
            for a in ARTICLES],
    }

    body = "\n".join([intro, grid, cta_band(lang, c)])
    return shell.page(path, lang, c["articles_h2"] + " | " + B.BRAND_SHORT,
                      ("Τεχνικές σημειώσεις για marine electrical, generator control, PMS, "
                       "DEIF, alarm monitoring και onboard troubleshooting. Γραμμένες για μηχανικούς."
                       if lang == "el" else
                       "Engineering notes on marine electrical, generator control, PMS, DEIF, "
                       "alarm monitoring and onboard troubleshooting. Written for engineers."),
                      body, alt, trail=trail, active="insights",
                      footer_services=FOOTER_SERVICES, schemas=[blog])


def page_article(lang, a):
    c, d = COPY[lang], a[lang]
    path = url("article", lang, a["slug"])
    alt = url("article", "en" if lang == "el" else "el", a["slug"])
    trail = [home_crumb(lang), (url("insights", lang), nav_label("insights", lang)),
             (path, d["title"])]
    svc = BY_SLUG[a["service"]]

    intro = """<section class="page-head page-head--article">
  <div class="wrap">
    <p class="article__meta">
      <time datetime="{date}">{date}</time>
      <span>{mins} {reading}</span>
    </p>
    <h1>{h1}</h1>
    <p class="page-head__lead">{excerpt}</p>
  </div>
</section>""".format(date=a["date"], mins=a["reading"], reading=esc(t(lang, "reading")),
                     h1=esc(d["title"]), excerpt=esc(d["excerpt"]))

    parts = []
    for kind, val in d["body"]:
        if kind == "p":
            parts.append("<p>%s</p>" % esc(val))
        elif kind == "h2":
            parts.append("<h2>%s</h2>" % esc(val))
        elif kind == "h3":
            parts.append("<h3>%s</h3>" % esc(val))
        elif kind == "ul":
            parts.append(ui.ul(val))
        elif kind == "ol":
            parts.append(ui.ol(val))
        elif kind == "note":
            parts.append('<aside class="pull"><p>%s</p></aside>' % esc(val))

    others = [x for x in ARTICLES if x is not a][:3]
    aside = """<aside class="aside">
        <div class="aside__card aside__card--plain">
          <h2 class="aside__h">{related}</h2>
          <ul class="aside__list">
            <li><a href="{svc_url}">{svc_name}</a></li>
          </ul>
        </div>
        <div class="aside__card">
          <h2 class="aside__h">{panel_h}</h2>
          <p>{panel_p}</p>
          <a class="btn btn--accent btn--full" href="{contact}">{cta}</a>
        </div>
      </aside>""".format(
        related=esc(t(lang, "related")), svc_url=esc(url("service", lang, svc["slug"])),
        svc_name=esc(svc[lang]["name"]), panel_h=esc(t(lang, "contact_panel_title")),
        panel_p=esc(t(lang, "contact_panel_text")), contact=esc(url("contact", lang)),
        cta=esc(t(lang, "cta_quote")))

    main = """<div class="wrap layout">
      <article class="layout__main prose">
      {parts}
      </article>
      {aside}
    </div>""".format(parts="\n      ".join(parts), aside=aside)

    more = ui.section(
        ui.head(None, "Περισσότερα άρθρα" if lang == "el" else "More articles") +
        '\n    <div class="grid grid--3">\n      %s\n    </div>'
        % "\n      ".join(article_card(x, lang) for x in others),
        cls="section--alt")

    posting = {
        "@context": "https://schema.org", "@type": "BlogPosting",
        "headline": d["title"], "description": d["desc"],
        "inLanguage": B.HTML_LANG[lang],
        "datePublished": a["date"], "dateModified": a["date"],
        "author": {"@id": B.BASE + "/#organization"},
        "publisher": {"@id": B.BASE + "/#organization"},
        "mainEntityOfPage": {"@type": "WebPage", "@id": B.BASE + path},
        "image": B.BASE + B.OG_IMAGE,
        "about": {"@type": "Thing", "name": svc["en"]["name"]},
    }

    body = "\n".join([intro, '<section class="section section--article">%s</section>' % main,
                      more, cta_band(lang, c)])
    return shell.page(path, lang, d["meta_title"], d["desc"], body, alt, trail=trail,
                      active="insights", footer_services=FOOTER_SERVICES,
                      schemas=[posting], og_type="article")


def page_about(lang):
    c = COPY[lang]
    path, alt = url("about", lang), url("about", "en" if lang == "el" else "el")
    trail = [home_crumb(lang), (path, nav_label("about", lang))]

    intro = """<section class="page-head">
  <div class="wrap">
    <h1>{h1}</h1>
    <p class="page-head__lead">{lead}</p>
  </div>
</section>""".format(h1=esc(c["about_h1"]), lead=esc(c["about_lead"]))

    story = ui.section(
        """<div class="split">
      <div class="split__l">
        %s
      </div>
      <div class="split__r prose">
        %s
      </div>
    </div>""" % (ui.head(None, c["about_story_h2"]),
                 "\n        ".join("<p>%s</p>" % esc(p) for p in c["about_story"])))

    photo = ui.section(
        ui.photo_slot(lang, "founder-onboard.jpg",
                      "Ο ιδρυτής της εταιρείας εν ώρα εργασίας onboard" if lang == "el"
                      else "The founder at work onboard", "3 / 2", "photo-slot--wide"),
        cls="section--tight")

    principles = "\n      ".join(
        '<div class="feature"><span class="feature__no">%02d</span><h3>%s</h3><p>%s</p></div>'
        % (i + 1, esc(h), esc(p)) for i, (h, p) in enumerate(c["about_principles"]))
    princ = ui.section(
        ui.head(None, c["about_principles_h2"]) +
        '\n    <div class="grid grid--4 grid--features">\n      %s\n    </div>' % principles,
        cls="section--dark")

    facts = [
        (("Έτος ίδρυσης" if lang == "el" else "Founded"), str(B.FOUNDED)),
        (("Μέγεθος ομάδας" if lang == "el" else "Team size"), "4"),
        (("Έδρα" if lang == "el" else "Base"),
         "%s, %s" % (B.STREET if lang == "el" else B.STREET_EN,
                     B.CITY_EL if lang == "el" else B.CITY_EN)),
        (t(lang, "areas"), "Ελλάδα & worldwide" if lang == "el" else "Greece & worldwide"),
        (("Γλώσσες" if lang == "el" else "Languages"),
         "Ελληνικά, Αγγλικά" if lang == "el" else "Greek, English"),
        (("Επικοινωνία" if lang == "el" else "Contact"),
         (B.CONTACT_NAME_EL if lang == "el" else B.CONTACT_NAME_EN)
         + " — Founder &amp; Technical Director"),
    ]
    facts_html = "\n        ".join(
        "<div class=\"facts__row\"><dt>%s</dt><dd>%s</dd></div>" % (esc(k), v)
        for k, v in facts)
    facts_sec = ui.section(
        """<div class="split">
      <div class="split__l">
        %s
      </div>
      <div class="split__r">
        <dl class="facts">
        %s
        </dl>
      </div>
    </div>""" % (ui.head(None, c["about_facts_h2"]), facts_html))

    caps = "\n      ".join(
        '<li><a href="%s"><span class="caps__icon">%s</span><span>%s</span></a></li>'
        % (esc(url("service", lang, s["slug"])), ui.icon(s["icon"]), esc(s[lang]["name"]))
        for s in SERVICES)
    caps_sec = ui.section(
        ui.head(None, c["about_capabilities_h2"], c["about_capabilities_p"]) +
        '\n    <ul class="caps">\n      %s\n    </ul>' % caps,
        cls="section--alt")

    equip = ui.section(
        """<div class="callout">
      <h2 class="callout__h">%s</h2>
      <p>%s</p>
    </div>""" % (esc(c["about_equipment_h2"]), esc(c["about_equipment_p"])),
        cls="section--tight")

    about_schema = {
        "@context": "https://schema.org", "@type": "AboutPage",
        "name": c["about_h1"], "url": B.BASE + path,
        "inLanguage": B.HTML_LANG[lang],
        "mainEntity": {"@id": B.BASE + "/#organization"},
    }

    body = "\n".join([intro, story, photo, princ, facts_sec, caps_sec, equip,
                      cta_band(lang, c)])
    return shell.page(path, lang, c["about_title"], c["about_desc"], body, alt,
                      trail=trail, active="about", footer_services=FOOTER_SERVICES,
                      schemas=[about_schema])


def page_contact(lang):
    c, f = COPY[lang], COPY[lang]["form_fields"]
    path, alt = url("contact", lang), url("contact", "en" if lang == "el" else "el")
    trail = [home_crumb(lang), (path, nav_label("contact", lang))]

    intro = """<section class="page-head">
  <div class="wrap">
    <h1>{h1}</h1>
    <p class="page-head__lead">{lead}</p>
  </div>
</section>""".format(h1=esc(c["contact_h1"]), lead=esc(c["contact_lead"]))

    options = "\n            ".join(
        '<option value="%s">%s</option>' % (esc(s["slug"]), esc(s[lang]["name"]))
        for s in SERVICES)

    form = """<form class="form" action="#" method="post" novalidate>
        <p class="form__note" id="form-note">{note}</p>
        <div class="form__row">
          <p class="field">
            <label for="f-name">{name} <span class="req">({required})</span></label>
            <input id="f-name" name="name" type="text" autocomplete="name" required>
          </p>
          <p class="field">
            <label for="f-company">{company}</label>
            <input id="f-company" name="company" type="text" autocomplete="organization">
          </p>
        </div>
        <div class="form__row">
          <p class="field">
            <label for="f-email">{email} <span class="req">({required})</span></label>
            <input id="f-email" name="email" type="email" autocomplete="email" required>
          </p>
          <p class="field">
            <label for="f-phone">{phone}</label>
            <input id="f-phone" name="phone" type="tel" autocomplete="tel">
          </p>
        </div>
        <div class="form__row">
          <p class="field">
            <label for="f-vessel">{vessel}</label>
            <input id="f-vessel" name="vessel" type="text">
          </p>
          <p class="field">
            <label for="f-subject">{subject}</label>
            <select id="f-subject" name="subject">
              <option value="">{subject_ph}</option>
            {options}
              <option value="other">{subject_other}</option>
            </select>
          </p>
        </div>
        <fieldset class="field field--radios">
          <legend>{urgency}</legend>
          <label class="radio"><input type="radio" name="urgency" value="planned" checked> {urgency_no}</label>
          <label class="radio"><input type="radio" name="urgency" value="urgent"> {urgency_yes}</label>
        </fieldset>
        <p class="field">
          <label for="f-message">{message} <span class="req">({required})</span></label>
          <textarea id="f-message" name="message" rows="6" placeholder="{message_ph}" required></textarea>
        </p>
        <p class="field field--check">
          <label class="check"><input type="checkbox" name="consent" required> {consent}</label>
        </p>
        <p><button class="btn btn--accent btn--lg" type="submit">{submit}</button></p>
      </form>""".format(
        note=esc(c["form_note"]), required=esc(f["required"]), name=esc(f["name"]),
        company=esc(f["company"]), email=esc(f["email"]), phone=esc(f["phone"]),
        vessel=esc(f["vessel"]), subject=esc(f["subject"]), subject_ph=esc(f["subject_ph"]),
        options=options, subject_other=esc(f["subject_other"]), urgency=esc(f["urgency"]),
        urgency_no=esc(f["urgency_no"]), urgency_yes=esc(f["urgency_yes"]),
        message=esc(f["message"]), message_ph=esc(f["message_ph"]),
        consent=esc(f["consent"]), submit=esc(f["submit"]))

    aside = """<aside class="aside">
        <div class="aside__card">
          <h2 class="aside__h">{direct}</h2>
          <ul class="contact-list">
            <li><span>{tel_l}</span><a href="tel:{tel}">{phone}</a></li>
            <li><span>Email</span><a href="mailto:{email}">{email}</a></li>
            <li><span>WhatsApp / Viber</span><a href="https://wa.me/{wa}" rel="noopener">{phone}</a></li>
          </ul>
        </div>
        <div class="aside__card aside__card--alert">
          <h2 class="aside__h">{em_h}</h2>
          <p>{em_p}</p>
          <a class="btn btn--accent btn--full" href="tel:{tel}">{call}</a>
        </div>
        <div class="aside__card aside__card--plain">
          <h2 class="aside__h">{hours_h}</h2>
          <dl class="facts facts--sm">
            <div class="facts__row"><dt>{hours_week}</dt><dd>{hours_week_v}</dd></div>
            <div class="facts__row"><dt>{hours_sat}</dt><dd>{hours_sat_v}</dd></div>
            <div class="facts__row"><dt>{areas_l}</dt><dd>{areas_v}</dd></div>
          </dl>
        </div>
        <div class="aside__card aside__card--plain">
          <h2 class="aside__h">{addr_h}</h2>
          <address class="addr">{street}<br>{postcode} {city}<br>{country}</address>
        </div>
      </aside>""".format(
        direct=esc(c["contact_direct_h2"]), tel_l="Τηλέφωνο" if lang == "el" else "Phone",
        tel=B.PHONE_E164, phone=B.PHONE_HUMAN, email=B.EMAIL, wa=B.WHATSAPP,
        em_h=esc(c["contact_emergency_h2"]), em_p=esc(c["contact_emergency_p"]),
        call=esc(t(lang, "cta_call")), hours_h=esc(t(lang, "hours_title")),
        hours_week=esc(t(lang, "hours_week")), hours_week_v=esc(t(lang, "hours_week_v")),
        hours_sat=esc(t(lang, "hours_sat")), hours_sat_v=esc(t(lang, "hours_sat_v")),
        areas_l=esc(t(lang, "areas")), areas_v=t(lang, "areas_v"),
        addr_h="Έδρα" if lang == "el" else "Registered office",
        street=esc(B.STREET if lang == "el" else B.STREET_EN), postcode=esc(B.POSTCODE),
        city=esc(B.CITY_EL if lang == "el" else B.CITY_EN),
        country="Ελλάδα" if lang == "el" else "Greece")

    main = """<div class="wrap layout">
      <div class="layout__main">
        <h2 class="block__h">{form_h}</h2>
        <p class="block__lead">{form_p}</p>
        {form}
        <section class="block">
          <h2>{what_h}</h2>
          {what}
        </section>
        <section class="block">
          <h2>{map_h}</h2>
          <div class="map">
            <iframe src="{map_src}" title="{map_h}" width="640" height="360" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
          </div>
          <p class="map__link"><a class="link" href="{map_link}" target="_blank" rel="noopener">{map_dir}</a></p>
        </section>
      </div>
      {aside}
    </div>""".format(form_h=esc(c["contact_form_h2"]), form_p=esc(c["contact_form_p"]),
                     form=form, what_h=esc(c["contact_what_h2"]),
                     what=ui.ul(c["contact_what"]), aside=aside,
                     map_h=esc(t(lang, "map_h")), map_src=esc(B.MAP_EMBED),
                     map_link=esc(B.MAP_LINK), map_dir=esc(t(lang, "map_directions")))

    contact_schema = {
        "@context": "https://schema.org", "@type": "ContactPage",
        "name": c["contact_h1"], "url": B.BASE + path,
        "inLanguage": B.HTML_LANG[lang],
        "mainEntity": {"@id": B.BASE + "/#organization"},
    }

    body = "\n".join([intro, '<section class="section">%s</section>' % main])
    return shell.page(path, lang, c["contact_title"], c["contact_desc"], body, alt,
                      trail=trail, active="contact", footer_services=FOOTER_SERVICES,
                      schemas=[contact_schema])


def page_404():
    lang = "el"
    c = COPY[lang]
    links = "\n        ".join(
        '<li><a href="%s">%s</a></li>' % (esc(url(pid, lang)), esc(labels[lang]))
        for pid, labels in NAV)
    body = """<section class="page-head page-head--404">
  <div class="wrap">
    <p class="eyebrow eyebrow--accent">Error 404</p>
    <h1>{h1}</h1>
    <p class="page-head__lead">{p}</p>
    <ul class="list list--inline">
        {links}
    </ul>
  </div>
</section>""".format(h1=esc(c["e404_h1"]), p=esc(c["e404_p"]), links=links)
    return shell.page("/404.html", lang, c["e404_title"], c["e404_p"], body,
                      url("home", "en"), active=None,
                      footer_services=FOOTER_SERVICES, relative=False, noindex=True)


# ===========================================================================
# Sitemap / robots / static files
# ===========================================================================
def sitemap():
    prio = {"home": "1.0", "services": "0.9", "contact": "0.9", "service": "0.8",
            "projects": "0.7", "about": "0.7", "insights": "0.7", "article": "0.6"}
    rows = []
    for lang in B.LOCALES:
        other = "en" if lang == "el" else "el"
        entries = [("home", None), ("services", None), ("projects", None),
                   ("insights", None), ("about", None), ("contact", None)]
        entries += [("service", s["slug"]) for s in SERVICES]
        entries += [("article", a["slug"]) for a in ARTICLES]
        for pid, slug in entries:
            loc = B.BASE + url(pid, lang, slug)
            alt = B.BASE + url(pid, other, slug)
            el_u, en_u = (loc, alt) if lang == "el" else (alt, loc)
            rows.append(
                "  <url>\n"
                "    <loc>%s</loc>\n"
                '    <xhtml:link rel="alternate" hreflang="el" href="%s"/>\n'
                '    <xhtml:link rel="alternate" hreflang="en" href="%s"/>\n'
                '    <xhtml:link rel="alternate" hreflang="x-default" href="%s"/>\n'
                "    <changefreq>%s</changefreq>\n"
                "    <priority>%s</priority>\n"
                "  </url>" % (loc, el_u, en_u, el_u,
                              "weekly" if pid == "home" else "monthly", prio[pid]))
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
           '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
           + "\n".join(rows) + "\n</urlset>\n")
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(xml)


def robots():
    open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write(
        "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % B.BASE)


def favicon():
    """The same generator symbol as the wordmark, on the navy ground."""
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
           '<rect width="64" height="64" rx="8" fill="#0a1a26"/>'
           '<circle cx="32" cy="32" r="20" fill="none" stroke="#2ec4d6" stroke-width="4"/>'
           '<path d="M20 32c0-4.7 2.6-7 5.6-7s5.6 2.3 5.6 7 2.6 7 5.6 7 5.6-2.3 5.6-7" '
           'fill="none" stroke="#2ec4d6" stroke-width="4" stroke-linecap="round"/></svg>\n')
    open(os.path.join(ROOT, "favicon.svg"), "w", encoding="utf-8").write(svg)


def main():
    for lang in B.LOCALES:
        write(url("home", lang), page_home(lang))
        write(url("services", lang), page_services(lang))
        for s in SERVICES:
            write(url("service", lang, s["slug"]), page_service(lang, s))
        write(url("projects", lang), page_projects(lang))
        write(url("insights", lang), page_insights(lang))
        for a in ARTICLES:
            write(url("article", lang, a["slug"]), page_article(lang, a))
        write(url("about", lang), page_about(lang))
        write(url("contact", lang), page_contact(lang))
    write("/404.html", page_404())

    sitemap()
    robots()
    favicon()
    print("Wrote %d pages + sitemap.xml, robots.txt, favicon.svg" % len(WRITTEN))


if __name__ == "__main__":
    main()
