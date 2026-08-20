#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generates the two raster assets the HTML references.

    python3 build/images.py

These are real brand assets, not placeholders: the Open Graph card social
platforms need (they do not render SVG) and the iOS home-screen icon. Both are
drawn from the same marks as the site so they stay in step with it.

Photography placeholders are a different thing entirely — those are rendered
in the page by ui.photo_slot() and are meant to be replaced by the client.
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "assets", "img")

NAVY = (10, 26, 38)
NAVY_DEEP = (6, 17, 25)
CYAN = (51, 201, 221)
STEEL = (139, 154, 164)
WHITE = (255, 255, 255)

FONTS = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/Library/Fonts/Arial Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]


def font(size, bold=True):
    for p in FONTS:
        if os.path.exists(p) and (bold == ("Bold" in p or "-Bold" in p)):
            return ImageFont.truetype(p, size)
    for p in FONTS:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def generator_mark(d, cx, cy, r, width, colour):
    """The IEC single-line generator symbol: a circle with a sine inside."""
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=colour, width=width)
    span = r * 0.72   # keeps the sine inside the circle
    pts = []
    steps = 120
    for i in range(steps + 1):
        x = -span + (2 * span) * i / steps
        y = -math.sin(x / span * math.pi * 2) * r * 0.34
        pts.append((cx + x, cy + y))
    d.line(pts, fill=colour, width=width, joint="curve")


def blueprint_grid(w, h, step=56, colour=(255, 255, 255), alpha=14):
    layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    for x in range(0, w, step):
        ld.line([(x, 0), (x, h)], fill=colour + (alpha,), width=1)
    for y in range(0, h, step):
        ld.line([(0, y), (w, y)], fill=colour + (alpha,), width=1)
    return layer


def og_card():
    w, h = 1200, 630
    im = Image.new("RGB", (w, h), NAVY)
    im = Image.alpha_composite(im.convert("RGBA"), blueprint_grid(w, h)).convert("RGB")
    d = ImageDraw.Draw(im)

    # accent rule along the bottom
    d.rectangle([0, h - 8, w, h], fill=CYAN)

    generator_mark(d, 118, 128, 44, 6, CYAN)

    d.text((186, 96), "GM MARINE", font=font(40, True), fill=WHITE)
    d.text((186, 142), "AUTOMATION", font=font(40, True), fill=WHITE)

    d.text((72, 272), "Marine Electrical &", font=font(66, True), fill=WHITE)
    d.text((72, 348), "Automation Systems", font=font(66, True), fill=CYAN)

    d.text((72, 452),
           "Generators · Power Management · DEIF · Synchronizing · Alarm Monitoring",
           font=font(24, False), fill=STEEL)
    d.text((72, 490), "Retrofit · Commissioning · Onboard Troubleshooting",
           font=font(24, False), fill=STEEL)

    d.text((72, 552), "gmmarineautomation.gr", font=font(24, True), fill=CYAN)
    d.text((w - 72 - d.textlength("24/7 EMERGENCY SUPPORT", font=font(22, True)), 554),
           "24/7 EMERGENCY SUPPORT", font=font(22, True), fill=STEEL)

    im.save(os.path.join(IMG, "og-gm-marine-automation.jpg"), "JPEG",
            quality=88, optimize=True, progressive=True)


def touch_icon():
    s = 180
    im = Image.new("RGB", (s, s), NAVY)
    d = ImageDraw.Draw(im)
    generator_mark(d, s / 2, s / 2, 58, 11, CYAN)
    im.save(os.path.join(IMG, "apple-touch-icon.png"), "PNG", optimize=True)


def main():
    os.makedirs(IMG, exist_ok=True)
    og_card()
    touch_icon()
    print("Wrote og-gm-marine-automation.jpg (1200x630) and apple-touch-icon.png (180x180)")


if __name__ == "__main__":
    main()
