#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Identity, routing and UI strings for the GM Marine Automation site.

Everything the client might want to change without touching markup lives here:
domain, phone, e-mail, opening hours, the navigation, and the small set of
recurring UI labels that exist in both Greek and English.

The site is bilingual. Greek sits at the root, English under /en/. Every page
is generated twice from the same builder, so the two trees cannot drift apart.
"""

# --- Identity ---------------------------------------------------------------
BASE = "https://www.gmmarineautomation.gr"   # change here if the domain differs

BRAND = "GM Marine Automation & Electrical System"
BRAND_SHORT = "GM Marine Automation"
TAGLINE_EN = "Marine Power, Automation & Control Solutions"

FOUNDED = 2022
SEA_YEARS = 15          # years sailing as ETO on gas carriers, per the brief

# Contact. PHONE_SITE in the brief was recorded as "9919782" — an incomplete
# entry of the same mobile given for WhatsApp/Viber. Confirm before launch.
PHONE_E164 = "+306989919782"
PHONE_HUMAN = "+30 698 991 9782"
WHATSAPP = "306989919782"
EMAIL = "gianment@hotmail.com"   # → replace with info@gmmarineautomation.gr
CONTACT_NAME_EL = "Γιάννης Μειντιάι"
CONTACT_NAME_EN = "Giannis Meintiai"

STREET = "Κανάρη 26"
STREET_EN = "26 Kanari Street"
CITY_EL = "Μοσχάτο"
CITY_EN = "Moschato"
POSTCODE = "[Τ.Κ.]"              # LAUNCH TODO — confirm postal code
REGION_EL = "Αττική"
REGION_EN = "Attica"
COUNTRY = "GR"
LAT_LON = None                   # add once the Google Business pin is confirmed

TIKTOK = "https://www.tiktok.com/@gmmarineautomation"   # confirm handle

OG_IMAGE = "/assets/img/og-gm-marine-automation.jpg"

# --- Locales ----------------------------------------------------------------
LOCALES = ("el", "en")

HTML_LANG = {"el": "el", "en": "en"}
OG_LOCALE = {"el": "el_GR", "en": "en_GB"}

# --- Routing ----------------------------------------------------------------
# One id per page kind; the builder asks for a URL by id + locale so the two
# language trees stay in lockstep and hreflang pairs are always valid.
ROUTES = {
    "home":     {"el": "/",                 "en": "/en/"},
    "services": {"el": "/ypiresies.html",   "en": "/en/services.html"},
    "service":  {"el": "/ypiresies/{}.html", "en": "/en/services/{}.html"},
    "projects": {"el": "/erga.html",        "en": "/en/projects.html"},
    "insights": {"el": "/arthra.html",      "en": "/en/insights.html"},
    "article":  {"el": "/arthra/{}.html",   "en": "/en/insights/{}.html"},
    "about":    {"el": "/etaireia.html",    "en": "/en/company.html"},
    "contact":  {"el": "/epikoinonia.html", "en": "/en/contact.html"},
}


def url(page_id, lang, slug=None):
    """Canonical path for a page id in a language."""
    pattern = ROUTES[page_id][lang]
    return pattern.format(slug) if slug is not None else pattern


def file_for(path):
    """Disk path (relative to project root) for a canonical URL path."""
    return (path + "index.html" if path.endswith("/") else path).lstrip("/")


# --- Navigation -------------------------------------------------------------
NAV = [
    ("home",     {"el": "Αρχική",       "en": "Home"}),
    ("services", {"el": "Υπηρεσίες",    "en": "Services"}),
    ("projects", {"el": "Έργα",         "en": "Projects"}),
    ("insights", {"el": "Τεχνικά Άρθρα", "en": "Technical Insights"}),
    ("about",    {"el": "Η Εταιρεία",   "en": "Company"}),
    ("contact",  {"el": "Επικοινωνία",  "en": "Contact"}),
]

# --- Recurring UI strings ---------------------------------------------------
UI = {
    "el": {
        "skip": "Μετάβαση στο περιεχόμενο",
        "menu_open": "Άνοιγμα μενού",
        "cta_quote": "Αίτημα προσφοράς",
        "cta_quote_long": "Ζητήστε τεχνική προσφορά",
        "cta_call": "Καλέστε μας",
        "cta_whatsapp": "WhatsApp",
        "emergency": "24/7 Emergency Technical Support",
        "emergency_short": "24/7 Επείγοντα",
        "crumbs_label": "Διαδρομή πλοήγησης",
        "nav_label": "Κύρια πλοήγηση",
        "lang_label": "Γλώσσα",
        "lang_other": "English",
        "all_services": "Όλες οι υπηρεσίες",
        "related": "Σχετικές υπηρεσίες",
        "scope": "Τι αναλαμβάνουμε",
        "symptoms": "Συνήθη συμπτώματα & βλάβες",
        "deliverables": "Τι παραδίδουμε",
        "equipment": "Εξοπλισμός & πρωτόκολλα",
        "faq": "Συχνές ερωτήσεις",
        "read_more": "Διαβάστε περισσότερα",
        "back_to_services": "Επιστροφή στις υπηρεσίες",
        "published": "Δημοσιεύτηκε",
        "reading": "λεπτά ανάγνωσης",
        "contact_panel_title": "Χρειάζεστε τεχνικό onboard;",
        "contact_panel_text": "Στείλτε μας το πρόβλημα, τον τύπο του πλοίου και τον εξοπλισμό. "
                              "Απαντάμε με συγκεκριμένο πλάνο επέμβασης — όχι με γενικόλογη προσφορά.",
        "hours_title": "Ωράριο",
        "hours_week": "Δευτέρα – Παρασκευή",
        "hours_week_v": "08:00 – 18:00",
        "hours_sat": "Σάββατο",
        "hours_sat_v": "Κατόπιν συνεννόησης",
        "areas": "Περιοχές εξυπηρέτησης",
        "areas_v": "Ελλάδα &amp; worldwide marine service",
        "footer_legal": "Με επιφύλαξη παντός δικαιώματος.",
        "footer_by": "Σχεδιασμός &amp; ανάπτυξη",
        "img_placeholder": "ΕΝΔΕΙΚΤΙΚΗ ΕΙΚΟΝΑ — ΠΡΟΣ ΑΝΤΙΚΑΤΑΣΤΑΣΗ",
        "on_this_page": "Σε αυτή τη σελίδα",
        "services_col": "Υπηρεσίες",
        "company_col": "Εταιρεία",
        "contact_col": "Επικοινωνία",
    },
    "en": {
        "skip": "Skip to content",
        "menu_open": "Open menu",
        "cta_quote": "Request a quote",
        "cta_quote_long": "Request a technical quote",
        "cta_call": "Call us",
        "cta_whatsapp": "WhatsApp",
        "emergency": "24/7 Emergency Technical Support",
        "emergency_short": "24/7 Emergency",
        "crumbs_label": "Breadcrumb",
        "nav_label": "Main navigation",
        "lang_label": "Language",
        "lang_other": "Ελληνικά",
        "all_services": "All services",
        "related": "Related services",
        "scope": "Scope of work",
        "symptoms": "Typical symptoms &amp; failures",
        "deliverables": "What you receive",
        "equipment": "Equipment &amp; protocols",
        "faq": "Frequently asked questions",
        "read_more": "Read more",
        "back_to_services": "Back to services",
        "published": "Published",
        "reading": "min read",
        "contact_panel_title": "Need an engineer onboard?",
        "contact_panel_text": "Send us the fault, the vessel type and the equipment involved. "
                              "You get a concrete intervention plan back — not a generic quote.",
        "hours_title": "Office hours",
        "hours_week": "Monday – Friday",
        "hours_week_v": "08:00 – 18:00",
        "hours_sat": "Saturday",
        "hours_sat_v": "By arrangement",
        "areas": "Areas served",
        "areas_v": "Greece &amp; worldwide marine service",
        "footer_legal": "All rights reserved.",
        "footer_by": "Design &amp; development",
        "img_placeholder": "PLACEHOLDER IMAGE — TO BE REPLACED",
        "on_this_page": "On this page",
        "services_col": "Services",
        "company_col": "Company",
        "contact_col": "Contact",
    },
}


def t(lang, key):
    return UI[lang][key]
