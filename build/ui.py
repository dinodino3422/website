#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reusable markup: technical line-art icons, section wrappers, cards.

The icons are drawn as schematic symbols rather than generic UI glyphs — a
generator is the IEC circle-and-sine, a busbar is a busbar. That is the visual
register the brief asked for, and it is the one this audience reads fluently.

No photographs are invented here. Where the client's real onboard photography
belongs, `photo_slot()` renders a clearly marked placeholder.
"""
from shell import esc
from brand import t

# --- Icons ------------------------------------------------------------------
_ICON_OPEN = ('<svg class="icon" viewBox="0 0 48 48" aria-hidden="true" focusable="false" '
              'fill="none" stroke="currentColor" stroke-width="1.6" '
              'stroke-linecap="round" stroke-linejoin="round">')

ICONS = {
 # Generator — IEC single-line symbol.
 "generator": '<circle cx="24" cy="24" r="14"/>'
              '<path d="M14 24c0-3.3 1.9-5 4.4-5s4.4 1.7 4.4 5 1.9 5 4.4 5 4.4-1.7 4.4-5"/>',

 # Closed control loop: process, sensor feedback, controller.
 "automation": '<rect x="6" y="16" width="14" height="12" rx="1"/>'
               '<rect x="28" y="16" width="14" height="12" rx="1"/>'
               '<path d="M20 22h8"/><path d="M25 19l3 3-3 3"/>'
               '<path d="M35 28v7H13v-7"/><path d="M16 31l-3 4 3 4" transform="translate(0,-8)"/>',

 # Controller front panel: display, indicator row, keypad.
 "deif": '<rect x="9" y="8" width="30" height="32" rx="2"/>'
         '<rect x="14" y="13" width="20" height="9" rx="1"/>'
         '<path d="M15 27h4M22 27h4M29 27h4M15 33h4M22 33h4M29 33h4"/>',

 # Power management: busbar with two infeeds and a metering scale.
 "pms": '<path d="M8 20h32"/><path d="M14 20v-8M24 20v-8M34 20v-8"/>'
        '<path d="M8 20v6M40 20v6"/>'
        '<path d="M12 32h24"/><path d="M12 32v4M18 32v3M24 32v5M30 32v3M36 32v4"/>',

 # Synchronizing: two phase-shifted waveforms converging.
 "sync": '<path d="M6 24c3-9 6-9 9 0s6 9 9 0"/>'
         '<path d="M15 28c3-9 6-9 9 0s6 9 9 0" opacity=".55"/>'
         '<path d="M38 16v16"/><path d="M34 20l4-4 4 4"/>',

 # Alarm: a trend crossing a dashed limit line.
 "alarm": '<path d="M6 34l7-4 6 3 5-11 6 14 5-9 7 3"/>'
          '<path d="M6 18h36" stroke-dasharray="3 3"/>'
          '<circle cx="30" cy="26" r="2.6" fill="currentColor" stroke="none"/>',

 # Fault: a broken conductor with an arc.
 "fault": '<path d="M6 24h11"/><path d="M31 24h11"/>'
          '<path d="M17 24l6-8-2 8h6l-6 8 2-8z"/>'
          '<path d="M22 34v5M26 34v5" opacity=".5"/>',

 # Retrofit: legacy unit replaced by a current one.
 "retrofit": '<rect x="5" y="15" width="13" height="18" rx="1" stroke-dasharray="3 3"/>'
             '<rect x="30" y="15" width="13" height="18" rx="1"/>'
             '<path d="M20 24h8"/><path d="M25 21l3 3-3 3"/>',

 # Electrical distribution: three-phase feeder to terminals.
 "electrical": '<path d="M8 12h32M8 20h32M8 28h32"/>'
               '<path d="M16 12v22M28 20v14M36 28v6"/>'
               '<circle cx="16" cy="37" r="2.4"/><circle cx="28" cy="37" r="2.4"/>'
               '<circle cx="36" cy="39" r="2.4"/>',

 # Ladder logic: a rung with a contact and a coil.
 "code": '<path d="M9 10v28M39 10v28"/>'
         '<path d="M9 19h9M23 19h16"/><path d="M18 15v8M23 15v8"/>'
         '<path d="M9 30h11M31 30h8"/><circle cx="25.5" cy="30" r="5.5"/>',

 # Switchboard: cabinet with three breaker cubicles.
 "switchboard": '<rect x="6" y="9" width="36" height="30" rx="2"/>'
                '<path d="M18 9v30M30 9v30"/>'
                '<path d="M10 18l4-4M14 18h-4M22 18l4-4M26 18h-4M34 18l4-4M38 18h-4"/>'
                '<path d="M11 30h2M23 30h2M35 30h2"/>',

 # PLC rack with I/O modules.
 "plc": '<rect x="6" y="12" width="36" height="24" rx="2"/>'
        '<path d="M15 12v24M24 12v24M33 12v24"/>'
        '<path d="M9 18h3M9 22h3M18 18h3M18 22h3M27 18h3M27 22h3M36 18h3M36 22h3"/>',

 # Commissioning: a signed checklist against a recorded trace.
 "trials": '<rect x="8" y="7" width="24" height="34" rx="2"/>'
           '<path d="M13 16h9M13 22h14M13 28h11"/>'
           '<path d="M30 33l4 4 8-11"/>',

 # Bus network: trunk with nodes and terminating resistors.
 "network": '<path d="M8 24h32"/>'
            '<path d="M8 20v8M40 20v8"/>'
            '<path d="M17 24v-8M31 24v8"/>'
            '<rect x="12" y="9" width="10" height="7" rx="1"/>'
            '<rect x="26" y="32" width="10" height="7" rx="1"/>',

 # Component with pins.
 "parts": '<rect x="14" y="14" width="20" height="20" rx="1"/>'
          '<path d="M8 19h6M8 24h6M8 29h6M34 19h6M34 24h6M34 29h6"/>'
          '<path d="M19 19h10v10H19z" opacity=".45"/>',
}


def icon(name):
    return _ICON_OPEN + ICONS[name] + "</svg>"


# --- Hero diagram -----------------------------------------------------------
def _wave(cx, cy, r):
    """The sine mark of an AC machine, drawn to a circle of radius `r` centred
    on (cx, cy). Gen-sets and consumers then carry the same symbol at their own
    size; the ratios are the ones the gen-sets were originally drawn with."""
    def n(v):
        return ("%.4f" % v).rstrip("0").rstrip(".")
    return "M%s %sc0 %s %s %s %s %sS%s %s %s %ss%s %s %s %sS%s %s %s %s" % (
        n(cx - 0.681818 * r), n(cy),
        n(-0.236364 * r), n(0.136364 * r), n(-0.354545 * r),
        n(0.309091 * r), n(-0.354545 * r),
        n(cx - 0.063636 * r), n(cy - 0.236364 * r), n(cx - 0.063636 * r), n(cy),
        n(0.136364 * r), n(0.354545 * r), n(0.309091 * r), n(0.354545 * r),
        n(cx + 0.554545 * r), n(cy + 0.236364 * r), n(cx + 0.554545 * r), n(cy),
    )


def single_line_diagram():
    """A simplified marine single-line: three gen-sets onto a main busbar, a tie
    breaker, the emergency board, and the outgoing feeders.

    The elements are grouped into energisation layers (`sld__l--1` … `--5`) so
    the stylesheet can bring the drawing up the way a switchboard actually comes
    up: machines first, then breakers, then the bus, then the load. The
    `sld__flow` paths carry the marching-dash current animation. All of it is
    decorative motion on top of a diagram that is complete and legible without
    it, and it is switched off under prefers-reduced-motion."""
    return """<svg class="sld" viewBox="0 0 460 300" role="img"
     aria-label="Single-line diagram: three generators paralleled onto a main busbar, tie breaker and emergency switchboard">
  <g class="sld__g" fill="none" stroke="currentColor" stroke-width="1.4"
     stroke-linecap="round" stroke-linejoin="round">

    <!-- 1 — generators -->
    <g class="sld__l sld__l--1">
      <circle class="sld__gen" cx="70" cy="46" r="22"/>
      <path d="%s"/>
      <text x="70" y="20" class="sld__lbl">DG 1</text>
      <circle class="sld__gen sld__gen--2" cx="200" cy="46" r="22"/>
      <path d="%s"/>
      <text x="200" y="20" class="sld__lbl">DG 2</text>
      <circle class="sld__gen sld__gen--3" cx="330" cy="46" r="22"/>
      <path d="%s"/>
      <text x="330" y="20" class="sld__lbl">DG 3</text>
    </g>

    <!-- 2 — feeders down to the incoming breakers -->
    <g class="sld__l sld__l--2">
      <path d="M70 68v22M200 68v22M330 68v22"/>
      <rect class="sld__brk" x="61" y="90" width="18" height="18"/>
      <rect class="sld__brk sld__brk--2" x="191" y="90" width="18" height="18"/>
      <rect class="sld__brk sld__brk--i3" x="321" y="90" width="18" height="18"/>
      <path d="M70 108v24M200 108v24M330 108v24"/>
      <path class="sld__flow" d="M70 68v64"/>
      <path class="sld__flow sld__flow--b" d="M200 68v64"/>
      <path class="sld__flow sld__flow--b3" d="M330 68v64"/>
    </g>

    <!-- 3 — main busbar, tie breaker, emergency board -->
    <g class="sld__l sld__l--3">
      <path class="sld__bus" d="M40 132h300" stroke-width="4"/>
      <path class="sld__flow sld__flow--bus" d="M40 132h300"/>
      <text x="40" y="124" class="sld__lbl sld__lbl--l">MAIN SWITCHBOARD 440V</text>

      <path d="M340 132h34"/>
      <rect class="sld__brk sld__brk--tie" x="374" y="123" width="18" height="18"/>
      <path d="M392 132h28"/>
      <path class="sld__bus" d="M420 100v90" stroke-width="4"/>
      <text x="404" y="212" class="sld__lbl">EMCY</text>
    </g>

    <!-- 4 — outgoing feeders -->
    <g class="sld__l sld__l--4">
      <path d="M80 132v40M140 132v40M200 132v40M260 132v40M320 132v40"/>
      <rect class="sld__brk" x="71" y="172" width="18" height="18"/>
      <rect class="sld__brk sld__brk--2" x="131" y="172" width="18" height="18"/>
      <rect class="sld__brk sld__brk--3" x="191" y="172" width="18" height="18"/>
      <rect class="sld__brk sld__brk--4" x="251" y="172" width="18" height="18"/>
      <rect class="sld__brk sld__brk--5" x="311" y="172" width="18" height="18"/>
      <path d="M80 190v22M140 190v22M200 190v22M260 190v22M320 190v22"/>
      <path class="sld__flow sld__flow--c" d="M80 132v80M140 132v80M200 132v80M260 132v80M320 132v80"/>
    </g>

    <!-- 5 — consumers -->
    <g class="sld__l sld__l--5">
      <circle class="sld__load" cx="80" cy="224" r="12"/><path d="%s"/>
      <circle class="sld__load sld__load--2" cx="140" cy="224" r="12"/><path d="%s"/>
      <circle class="sld__load sld__load--3" cx="200" cy="224" r="12"/><path d="%s"/>
      <circle class="sld__load sld__load--4" cx="260" cy="224" r="12"/><path d="%s"/>
      <circle class="sld__load sld__load--5" cx="320" cy="224" r="12"/><path d="%s"/>
      <text x="200" y="258" class="sld__lbl">CONSUMERS</text>
    </g>

    <!-- synchronizing annotation -->
    <g class="sld__l sld__l--sync">
      <path class="sld__sync" d="M92 99h86M212 99h96" stroke-dasharray="4 4"/>
      <text x="135" y="92" class="sld__lbl sld__lbl--accent">SYNC</text>
    </g>
  </g>
</svg>""" % (
        _wave(70, 46, 22), _wave(200, 46, 22), _wave(330, 46, 22),
        _wave(80, 224, 12), _wave(140, 224, 12), _wave(200, 224, 12),
        _wave(260, 224, 12), _wave(320, 224, 12),
    )


# --- Section helpers --------------------------------------------------------
def section(inner, cls="", el="section", attrs=""):
    return '<%s class="section %s"%s>\n  <div class="wrap">\n%s\n  </div>\n</%s>' % (
        el, cls, attrs, inner, el)


def head(eyebrow, title, lead="", level=2, cls=""):
    parts = ['<div class="sec-head %s">' % cls]
    if eyebrow:
        parts.append('<p class="eyebrow">%s</p>' % esc(eyebrow))
    parts.append('<h%d>%s</h%d>' % (level, esc(title), level))
    if lead:
        parts.append('<p class="sec-head__lead">%s</p>' % esc(lead))
    parts.append("</div>")
    return "\n    ".join(parts)


def ul(items, cls="list"):
    return ('<ul class="%s">\n      %s\n    </ul>'
            % (cls, "\n      ".join("<li>%s</li>" % esc(i) for i in items)))


def ol(items, cls="list list--num"):
    return ('<ol class="%s">\n      %s\n    </ol>'
            % (cls, "\n      ".join("<li>%s</li>" % esc(i) for i in items)))


def faq_block(pairs, lang, heading=None, level=2):
    """Visible FAQ. Rendered as <details> so long pages stay scannable; the
    answers are in the DOM either way, which is what matters for indexing."""
    out = []
    if heading:
        out.append('<h%d class="faq__h">%s</h%d>' % (level, esc(heading), level))
    out.append('<div class="faq">')
    for q, a in pairs:
        out.append(
            '<details class="faq__item">'
            '<summary><span>%s</span></summary>'
            '<div class="faq__a"><p>%s</p></div>'
            "</details>" % (esc(q), esc(a)))
    out.append("</div>")
    return "\n    ".join(out)


def photo_slot(lang, name, alt, ratio="16 / 9", cls=""):
    """A marked slot for the client's real onboard photography.

    Deliberately not an invented image: it states what belongs here so the
    client can drop the file in without guessing, and check.py counts it as a
    launch TODO."""
    return ("""<figure class="photo-slot %s" style="--ratio:%s">
      <div class="photo-slot__box">
        <p class="photo-slot__tag">%s</p>
        <p class="photo-slot__name">%s</p>
      </div>
      <figcaption>%s</figcaption>
    </figure>""" % (cls, ratio, esc(t(lang, "img_placeholder")), esc(name), esc(alt)))


def stat_strip(stats):
    items = "\n      ".join(
        '<div class="stat"><span class="stat__v">%s</span>'
        '<span class="stat__l">%s</span></div>' % (esc(v), esc(l))
        for v, l in stats)
    return '<div class="stats">\n      %s\n    </div>' % items
