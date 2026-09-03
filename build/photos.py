#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The client's own onboard photography.

One entry per file in assets/img/projects/. `service` is the slug of the
service page the photo belongs to, which is what puts each shot in front of
the right copy instead of in an undifferentiated gallery; the projects page
shows the whole set. Dimensions are recorded here so every <img> ships with
width/height and the page does not shift while the photo loads.

Adding a photo: drop the optimised JPEG in assets/img/projects/, add an entry
below with its real pixel size, and rerun the generator. Captions are written
in both languages — they are used as the alt text as well, so they must
describe the picture, not sell the service.
"""

DIR = "/assets/img/projects/"

PHOTOS = [
 {"file": "deif-generator-panel-synchronising.jpg",
  "service": "generator-synchronizing-load-sharing", "w": 1280, "h": 1280,
  "el": "Παραλληλισμός γεννήτριας στον κύριο πίνακα: synchroscope σε μονάδα DEIF, "
        "50.36 Hz / 402 V στη γεννήτρια έναντι 50.02 Hz / 401 V στο busbar",
  "en": "Synchronising a generator onto the main switchboard: synchroscope on a DEIF "
        "unit, 50.36 Hz / 402 V on the machine against 50.02 Hz / 401 V on the busbar"},

 {"file": "deif-ppu3-commissioning.jpg",
  "service": "deif-controller-programming", "w": 1280, "h": 1280,
  "el": "Παραμετροποίηση DEIF PPU-3 από το utility software κατά το commissioning, "
        "με ζωντανή εικόνα ισχύος, συχνότητας και τάσης",
  "en": "DEIF PPU-3 parameter work from the utility software during commissioning, "
        "with live power, frequency and voltage readings"},

 {"file": "deif-governor-output-parameters.jpg",
  "service": "deif-power-management", "w": 1280, "h": 1280,
  "el": "Ρυθμίσεις εξόδων governor — GOV ON time, περίοδος και relays αύξησης/μείωσης "
        "στροφών — σε λειτουργία island",
  "en": "Governor output settings — GOV on time, period and the increase/decrease "
        "relays — configured for island mode"},

 {"file": "switchboard-controller-installation.jpg",
  "service": "switchboards", "w": 1280, "h": 1280,
  "el": "Εγκατάσταση και καλωδίωση μονάδας ελέγχου γεννήτριας μέσα στον πίνακα, "
        "με τα υπάρχοντα current transformers σε λειτουργία",
  "en": "Generator control unit installed and wired inside the switchboard, "
        "reusing the existing current transformers"},

 {"file": "vfd-inverter-cargo-pump-fan.jpg",
  "service": "marine-electrical-systems", "w": 1280, "h": 1280,
  "el": "Inverter (VFD) drivers για cargo pump fan, εγκατεστημένοι onboard δίπλα "
        "στον φορτιστή συσσωρευτών",
  "en": "Inverter (VFD) drives for the cargo pump fan, installed onboard next to "
        "the battery charger"},

 {"file": "excitation-avr-board-repair.jpg",
  "service": "troubleshooting-repairs", "w": 1280, "h": 1280,
  "el": "Έλεγχος πλακέτας διέγερσης και ρύθμισης τάσης γεννήτριας κατά τη διάγνωση "
        "βλάβης onboard",
  "en": "Inspecting a generator excitation and voltage-regulation board during "
        "onboard fault diagnosis"},

 {"file": "avr-d510c-voltage-regulator.jpg",
  "service": "marine-generators", "w": 959, "h": 1280,
  "el": "Ρυθμιστής τάσης (AVR) D510C πριν την τοποθέτηση στη γεννήτρια — "
        "sensing, διέγερση και CAN bus στην ίδια μονάδα",
  "en": "A D510C automatic voltage regulator before fitting — sensing, excitation "
        "and CAN bus on the one unit"},

 {"file": "dse-8610-mkii-controller.jpg",
  "service": "spare-parts", "w": 720, "h": 1280,
  "el": "Controller γεννήτριας Deep Sea Electronics DSE 8610 MKII, καινούριος και "
        "έτοιμος για αντικατάσταση onboard",
  "en": "A Deep Sea Electronics DSE 8610 MKII generator controller, new and ready "
        "to go in as a replacement"},

 {"file": "esd5500e-speed-control-unit.jpg",
  "service": "spare-parts", "w": 1280, "h": 1280,
  "el": "Μονάδα ελέγχου στροφών ESD5500E — ανταλλακτικό governor για γεννήτρια πλοίου",
  "en": "An ESD5500E speed control unit — governor spare for a marine generator"},
]

BY_SERVICE = {}
for _p in PHOTOS:
    BY_SERVICE.setdefault(_p["service"], []).append(_p)
