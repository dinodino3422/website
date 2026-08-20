#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Page copy for home, company, projects and contact, in both languages.

Nothing here was invented beyond what the intake brief supports. Where the
brief was silent — client references, certifications, team members, project
history — the copy says so plainly rather than filling the space. Those gaps
are listed in README §3 and flagged by check.py as [PLACEHOLDER] tokens.
"""

COPY = {

# ===========================================================================
"el": {

 # --- Home -------------------------------------------------------------
 "home_title": "GM Marine Automation | Ναυτιλιακά Ηλεκτρολογικά & Αυτοματισμοί",
 "home_desc": "Ναυτιλιακά ηλεκτρολογικά και αυτοματισμοί πλοίων: γεννήτριες, PMS, DEIF, παραλληλισμός, alarm monitoring, retrofit και troubleshooting onboard. Ελλάδα και διεθνώς.",
 "hero_eyebrow": "Marine Power, Automation & Control Solutions",
 "hero_h1": "Ηλεκτρολογικά και αυτοματισμοί πλοίων, από μηχανικό που έχει ταξιδέψει",
 "hero_lead": "Εγκατάσταση, αναβάθμιση και troubleshooting σε marine electrical systems, γεννήτριες, "
              "power management και συστήματα ελέγχου. Με 15+ χρόνια υπηρεσίας ως Αξιωματικός "
              "Ηλεκτρολόγος Εμπορικού Ναυτικού σε gas carriers — εμπειρία που μεταφέρεται σε κάθε έργο.",
 "hero_stats": [
  ("15+", "χρόνια εν πλω ως Αξιωματικός Ηλεκτρολόγος"),
  ("24/7", "τεχνική υποστήριξη για επείγοντα"),
  ("15", "τομείς εξειδίκευσης onboard"),
  ("GR + Worldwide", "κάλυψη σε Ελλάδα και διεθνώς"),
 ],

 "intro_eyebrow": "Ποιοι είμαστε",
 "intro_h2": "Τεχνική γνώση που αποκτήθηκε στο μηχανοστάσιο, όχι στην αίθουσα",
 "intro_p": [
  "Η GM Marine Automation & Electrical System εξειδικεύεται σε ηλεκτρολογικά και συστήματα "
  "αυτοματισμού για πλοία και σκάφη. Αναλαμβάνουμε εγκατάσταση, επισκευή και αναβάθμιση "
  "γεννητριών, ηλεκτρικών πινάκων, PLC/HMI, συστημάτων παραλληλισμού, alarm monitoring και "
  "power management.",
  "Η διαφορά μας δεν είναι εμπορική. Είναι ότι έχουμε ζήσει τη βλάβη από την άλλη πλευρά: "
  "ως πλήρωμα, εν πλω, με το πλοίο σε λειτουργία και χωρίς δυνατότητα να περιμένουμε τεχνικό. "
  "Αυτή η οπτική καθορίζει τι θεωρούμε ολοκληρωμένη δουλειά — τεκμηρίωση που μπορεί να "
  "χρησιμοποιήσει το πλήρωμα, ρυθμίσεις που εξηγούνται, και συστήματα που μπορούν να "
  "διαγνωστούν χωρίς εμάς.",
 ],

 "why_eyebrow": "Γιατί εμάς",
 "why_h2": "Τι σημαίνει στην πράξη «εμπειρία στη θάλασσα»",
 "why_items": [
  ("Διάγνωση πριν την αντικατάσταση",
   "Ξεκινάμε από μέτρηση, σχέδια και alarm logs. Η αντικατάσταση εξαρτημάτων μέχρι να σταματήσει "
   "το σύμπτωμα δεν είναι διάγνωση — είναι λογαριασμός."),
  ("Δουλεύουμε με το πλοίο σε λειτουργία",
   "Ο προγραμματισμός γίνεται γύρω από το port stay και το trade, σε φάσεις όπου χρειάζεται. "
   "Το downtime είναι μέρος του κόστους και το αντιμετωπίζουμε ως τέτοιο."),
  ("Τεκμηρίωση που παραδίδεται",
   "As-built σχέδια, parameter files, I/O lists και πρωτόκολλα δοκιμών. Το πλοίο δεν πρέπει να "
   "εξαρτάται από τη μνήμη ενός προμηθευτή."),
  ("Καθαρά όρια ευθύνης",
   "Λέμε τι είναι προσωρινή αποκατάσταση και τι μόνιμη, τι είναι ηλεκτρολογικό και τι μηχανολογικό, "
   "και τι δεν αναλαμβάνουμε."),
 ],

 "sectors_eyebrow": "Ποιους εξυπηρετούμε",
 "sectors_h2": "Ναυτιλιακές εταιρείες, τεχνικά τμήματα και ναυπηγεία",
 "sectors_p": "Απευθυνόμαστε σε οργανισμούς που αξιολογούν έναν τεχνικό συνεργάτη με βάση την τεκμηρίωση "
              "και τη συνέπεια, όχι την τιμή μονάδας.",
 "sectors_items": [
  ("Ναυτιλιακές εταιρείες & ship managers", "Τεχνική υποστήριξη στόλου, planned εργασίες και επείγοντα περιστατικά."),
  ("Τεχνικά τμήματα πλοίων", "Δεύτερη γνώμη, ανάλυση συμβάντων, υποστήριξη σε επιθεωρήσεις και προετοιμασία survey."),
  ("Πλοιοκτήτες", "Αξιολόγηση κατάστασης εγκατάστασης, μελέτη retrofit και έλεγχος εργασιών τρίτων."),
  ("Ναυπηγεία & marine service companies", "Εξειδικευμένη υποστήριξη σε automation και generator control κατά τη διάρκεια έργων."),
 ],

 "process_eyebrow": "Πώς δουλεύουμε",
 "process_h2": "Από το πρώτο μήνυμα μέχρι την παράδοση",
 "process_steps": [
  ("Περιγραφή & προαξιολόγηση",
   "Μας στέλνετε το πρόβλημα, τον τύπο του πλοίου και τον εξοπλισμό. Ζητάμε alarm logs, σχέδια και "
   "φωτογραφίες πινακίδων. Πολλά περιορίζονται ήδη σε αυτό το στάδιο."),
  ("Πρόταση με σαφές εύρος",
   "Λαμβάνετε πλάνο επέμβασης: τι ελέγχεται, τι απαιτείται από το πλοίο, εκτίμηση χρόνου και "
   "downtime, και τι δεν περιλαμβάνεται."),
  ("Εργασία onboard",
   "Επέμβαση με μετρήσεις και καταγραφή σε κάθε βήμα. Ενημέρωση του τεχνικού τμήματος καθημερινά, "
   "όχι μόνο στο τέλος."),
  ("Παράδοση & τεκμηρίωση",
   "Πρωτόκολλα δοκιμών, ενημερωμένα σχέδια, backups και λίστα προτεινόμενων ανταλλακτικών. "
   "Παραμένουμε διαθέσιμοι για υποστήριξη."),
 ],

 "home_faq_h2": "Συχνές ερωτήσεις",
 "home_faq": [
  ("Σε τι τύπους πλοίων δουλεύετε;",
   "Σε εμπορικά πλοία και σε επαγγελματικά ή ιδιωτικά σκάφη. Η εμπειρία μας προέρχεται κυρίως από "
   "gas carriers, όπου οι απαιτήσεις σε ηλεκτρολογικά και automation είναι από τις υψηλότερες."),
  ("Ταξιδεύετε εκτός Ελλάδας;",
   "Ναι. Εξυπηρετούμε την ελληνική και τη διεθνή ναυτιλιακή αγορά. Για διεθνή περιστατικά κανονίζουμε "
   "mobilization με το τεχνικό τμήμα και δίνουμε ρεαλιστικό χρόνο άφιξης."),
  ("Δουλεύετε μόνο σε DEIF;",
   "Όχι. Το DEIF είναι το πιο συχνό σύστημα generator control και power management στα πλοία που "
   "εξυπηρετούμε, αλλά αναλαμβάνουμε και εγκαταστάσεις άλλων κατασκευαστών."),
  ("Μπορείτε να επέμβετε ενώ το πλοίο είναι εν πλω;",
   "Εφόσον το επιτρέπουν οι διαδικασίες του διαχειριστή, ναι — ως riding squad ή με επιβίβαση σε "
   "ενδιάμεσο λιμάνι."),
  ("Πώς τιμολογείτε;",
   "Με βάση το εύρος της εργασίας, τον χρόνο onboard και τα υλικά. Δεν δημοσιεύουμε τιμοκατάλογο "
   "γιατί δύο πλοία με το ίδιο σύμπτωμα σπάνια χρειάζονται την ίδια εργασία. Κάθε προσφορά αναφέρει "
   "ρητά τι περιλαμβάνεται."),
  ("Τι χρειάζεστε για να δώσετε προσφορά;",
   "Τύπο και μέγεθος πλοίου, το σύστημα που αφορά, τον κατασκευαστή και το μοντέλο αν είναι γνωστά, "
   "περιγραφή του προβλήματος και το λιμάνι ή την περιοχή."),
 ],

 "cta_h2": "Στείλτε μας το πρόβλημα",
 "cta_p": "Περιγράψτε το σύστημα, το πλοίο και το τι παρατηρείτε. Απαντάμε με συγκεκριμένο πλάνο "
          "επέμβασης και σαφές εύρος εργασιών.",

 "articles_eyebrow": "Τεχνικά άρθρα",
 "articles_h2": "Σημειώσεις από το μηχανοστάσιο",
 "articles_p": "Γραμμένα για μηχανικούς, όχι για μηχανές αναζήτησης. Ό,τι συναντάμε συχνά και αξίζει να γραφτεί κάπου.",

 # --- Services hub ------------------------------------------------------
 "services_title": "Υπηρεσίες Marine Electrical & Automation | GM Marine Automation",
 "services_desc": "Δεκαπέντε τομείς σε marine electrical και automation: γεννήτριες, PMS, DEIF, παραλληλισμός, switchboards, AMS, PLC/SCADA, retrofit και commissioning.",
 "services_h1": "Υπηρεσίες",
 "services_lead": "Δεκαπέντε τομείς που καλύπτουν την ηλεκτρική ισχύ και τον αυτοματισμό ενός πλοίου, από τη "
                  "γεννήτρια μέχρι την οθόνη του μηχανικού. Κάθε σελίδα περιγράφει τι αναλαμβάνουμε, ποια "
                  "συμπτώματα αντιμετωπίζουμε και τι παραδίδουμε.",
 "services_featured_h2": "Κύριοι τομείς",
 "services_all_h2": "Όλες οι υπηρεσίες",

 # --- Company -----------------------------------------------------------
 "about_title": "Η Εταιρεία | GM Marine Automation & Electrical System",
 "about_desc": "Η GM Marine Automation ιδρύθηκε το 2022 από Αξιωματικό Ηλεκτρολόγο Ε.Ν. με 15+ χρόνια σε gas carriers. Ηλεκτρολογικά και αυτοματισμοί πλοίων, Ελλάδα και διεθνώς.",
 "about_h1": "Η Εταιρεία",
 "about_lead": "Μια μικρή τεχνική ομάδα με ναυτιλιακό υπόβαθρο, που δουλεύει σε συστήματα όπου το λάθος "
               "δεν διορθώνεται με ένα δεύτερο ραντεβού.",
 "about_story_h2": "Από το μηχανοστάσιο στην τεχνική υποστήριξη",
 "about_story": [
  "Η GM Marine Automation & Electrical System ιδρύθηκε το 2022. Πίσω της βρίσκονται περισσότερα από "
  "15 χρόνια υπηρεσίας ως Αξιωματικός Ηλεκτρολόγος Εμπορικού Ναυτικού σε gas carriers — πλοία με "
  "από τις πιο απαιτητικές εγκαταστάσεις σε marine electrical και automation systems.",
  "Στα χρόνια αυτά η δουλειά ήταν καθημερινά η ίδια: power generation and distribution, alarm "
  "monitoring, control systems και onboard troubleshooting, με το πλοίο σε λειτουργία και χωρίς "
  "τη δυνατότητα να περιμένει κανείς εξωτερικό τεχνικό. Ό,τι έπρεπε να λυθεί, λυνόταν επιτόπου, "
  "με τα μέσα που υπήρχαν.",
  "Αυτή η εμπειρία είναι σήμερα η βάση της εταιρείας. Δεν αλλάζει το τι κάνουμε — αλλάζει το πώς. "
  "Ξέρουμε τι σημαίνει να παραδίδεται ένα σύστημα χωρίς τεκμηρίωση, γιατί το έχουμε παραλάβει. "
  "Ξέρουμε ποια ρύθμιση θα δημιουργήσει πρόβλημα σε έξι μήνες, γιατί το έχουμε ζήσει.",
 ],
 "about_principles_h2": "Πώς δουλεύουμε",
 "about_principles": [
  ("Μετράμε πριν προτείνουμε",
   "Καμία πρόταση χωρίς αποτύπωση της υπάρχουσας κατάστασης. Μια προσφορά που γράφτηκε χωρίς μέτρηση "
   "είναι εκτίμηση, και πρέπει να δηλώνεται ως τέτοια."),
  ("Το πλοίο κρατά την τεκμηρίωση",
   "Parameter files, προγράμματα PLC, σχέδια και πρωτόκολλα παραδίδονται στον πλοιοκτήτη. Δεν "
   "χτίζουμε εξάρτηση από εμάς."),
  ("Δεν πειράζουμε προστασίες για να φύγει ένα alarm",
   "Οι ρυθμίσεις προστασίας αλλάζουν μόνο τεκμηριωμένα και σε συνεννόηση με το τεχνικό τμήμα και, "
   "όπου απαιτείται, τον νηογνώμονα."),
  ("Λέμε τι δεν αναλαμβάνουμε",
   "Η ειδίκευσή μας είναι το ηλεκτρολογικό και το automation μέρος. Όπου η εργασία περνά σε άλλη "
   "ειδικότητα, το δηλώνουμε και συνεργαζόμαστε καθαρά."),
 ],
 "about_facts_h2": "Στοιχεία",
 "about_capabilities_h2": "Πεδία εξειδίκευσης",
 "about_capabilities_p": "Οι τομείς στους οποίους αναλαμβάνουμε εργασίες, από την ισχύ μέχρι τον έλεγχο.",
 "about_equipment_h2": "Εξοπλισμός & κατασκευαστές",
 "about_equipment_p": "Διαθέτουμε εμπειρία και τεχνική υποστήριξη σε συστήματα και εξοπλισμό κορυφαίων "
                      "κατασκευαστών marine automation, generator control και power management. Για "
                      "συγκεκριμένο μοντέλο ή σειρά, επικοινωνήστε μαζί μας.",

 # --- Projects ----------------------------------------------------------
 "projects_title": "Έργα & Πεδίο Εφαρμογής | GM Marine Automation",
 "projects_desc": "Τυπικά έργα marine electrical και automation: retrofit generator control, εξυγίανση AMS, commissioning PMS, troubleshooting onboard και αναβάθμιση switchboards.",
 "projects_h1": "Έργα & πεδίο εφαρμογής",
 "projects_lead": "Οι τύποι έργων που αναλαμβάνουμε, με το πραγματικό τους εύρος: τι ζητείται, τι "
                  "συνήθως βρίσκουμε, και τι παραδίδεται στο τέλος.",
 "projects_note_h": "Σημείωση για τις αναφορές πελατών",
 "projects_note": "Οι παρακάτω περιγραφές αποτυπώνουν τυπικά έργα του κλάδου και το εύρος εργασιών που "
                  "αναλαμβάνουμε. Δεν παρουσιάζονται ονόματα πλοίων ή πελατών χωρίς τη ρητή συγκατάθεσή "
                  "τους. Για συγκεκριμένες αναφορές έργων και συστάσεις, επικοινωνήστε μαζί μας.",
 "projects_types": [
  ("Retrofit συστήματος ελέγχου γεννητριών",
   "Αντικατάσταση τερματισμένων generator controllers και μονάδων προστασίας σε main switchboard, "
   "με διατήρηση της υπάρχουσας καλωδίωσης και των CT/VT.",
   ["Αποτύπωση υπάρχουσας καλωδίωσης και λογικής", "Παραμετροποίηση νέων μονάδων και προστασιών",
    "Δοκιμές παραλληλισμού και load sharing", "Ενημερωμένο single-line και parameter files"],
   "deif-power-management"),
  ("Εξυγίανση Alarm Monitoring System",
   "Αποκατάσταση αξιοπιστίας σε AMS με μεγάλο αριθμό μόνιμων ή παρακαμφθέντων σημείων, χωρίς "
   "αντικατάσταση της πλατφόρμας.",
   ["Πλήρης εξαγωγή και έλεγχος alarm point list", "Φυσική επαλήθευση αισθητηρίων σε λειτουργία",
    "Επαναρύθμιση ορίων, καθυστερήσεων και ομαδοποίησης", "Πρωτόκολλο δοκιμής ανά σημείο"],
   "alarm-monitoring-systems"),
  ("Commissioning PMS και δοκιμές blackout",
   "Έλεγχος και τεκμηρίωση ολόκληρης της λογικής διαχείρισης ισχύος μετά από εγκατάσταση ή "
   "αναβάθμιση, με πραγματικές δοκιμές.",
   ["Έλεγχος ισοζυγίου ισχύος με τα σημερινά φορτία", "Δοκιμή load-dependent start και load shedding",
    "Ελεγχόμενη δοκιμή blackout και επαναφοράς", "Υπογεγραμμένα πρωτόκολλα ανά σενάριο"],
   "power-management-systems"),
  ("Επείγον περιστατικό onboard",
   "Επέμβαση σε πλοίο με βλάβη που περιορίζει τη λειτουργία του, με στόχο ασφαλή αποκατάσταση "
   "εντός του διαθέσιμου παραθύρου.",
   ["Άμεση αξιολόγηση από απόσταση με logs και φωτογραφίες", "Fault finding με μετρήσεις onboard",
    "Ασφαλής αποκατάσταση, προσωρινή ή μόνιμη με σαφή δήλωση", "Τεχνική αναφορά με ρίζα αιτίας"],
   "troubleshooting-repairs"),
  ("Αναβάθμιση main / emergency switchboard",
   "Στοχευμένη αναβάθμιση μέτρησης, προστασίας και αυτοματισμού πίνακα, χωρίς αντικατάσταση του "
   "κελύφους και των breakers όπου είναι υγιή.",
   ["Θερμογραφικός έλεγχος υπό φορτίο", "Έλεγχος και αποκατάσταση interlocks",
    "Αντικατάσταση οργάνων και relays προστασίας", "Μελέτη συντονισμού προστασιών όπου απαιτείται"],
   "switchboards"),
  ("Διάγνωση δικτύου αυτοματισμού",
   "Εντοπισμός περιοδικών απωλειών επικοινωνίας σε CAN bus ή Modbus, με μέτρηση στο φυσικό επίπεδο "
   "και ανάλυση κίνησης.",
   ["Μέτρηση τερματισμών και ελέγχου θωράκισης", "Καταγραφή και ανάλυση error frames",
    "Εντοπισμός κόμβου ή διαδρομής που προκαλεί το σφάλμα", "Διάγραμμα τοπολογίας και οδηγία επέκτασης"],
   "marine-networks"),
 ],

 # --- Contact -----------------------------------------------------------
 "contact_title": "Επικοινωνία & Αίτημα Προσφοράς | GM Marine Automation",
 "contact_desc": "Επικοινωνήστε με την GM Marine Automation για τεχνική προσφορά ή επείγον περιστατικό. Τηλέφωνο, WhatsApp, email και φόρμα αιτήματος. 24/7 emergency support.",
 "contact_h1": "Επικοινωνία",
 "contact_lead": "Για αίτημα προσφοράς, τεχνική ερώτηση ή επείγον περιστατικό. Όσο πιο συγκεκριμένη η "
                 "περιγραφή, τόσο πιο χρήσιμη η πρώτη απάντηση.",
 "contact_form_h2": "Αίτημα προσφοράς",
 "contact_form_p": "Συμπληρώστε όσα στοιχεία γνωρίζετε. Δεν είναι όλα απαραίτητα για μια πρώτη εκτίμηση.",
 "contact_direct_h2": "Άμεση επικοινωνία",
 "contact_emergency_h2": "Επείγοντα περιστατικά",
 "contact_emergency_p": "Για βλάβη που επηρεάζει τη λειτουργία του πλοίου, καλέστε απευθείας. Το τηλέφωνο "
                        "είναι διαθέσιμο και εκτός ωραρίου για επείγοντα.",
 "contact_what_h2": "Τι να μας στείλετε",
 "contact_what": [
  "Τύπο και μέγεθος πλοίου, και το λιμάνι ή την περιοχή",
  "Το σύστημα που αφορά — γεννήτρια, πίνακας, PMS, AMS, δίκτυο",
  "Κατασκευαστή και μοντέλο, ή φωτογραφία της πινακίδας",
  "Περιγραφή του συμπτώματος και πότε εμφανίζεται",
  "Alarm log ή screenshots από controller, αν υπάρχουν",
  "Σχέδια της εγκατάστασης, αν είναι διαθέσιμα",
 ],
 "form_fields": {
  "name": "Ονοματεπώνυμο", "company": "Εταιρεία", "email": "Email", "phone": "Τηλέφωνο",
  "vessel": "Πλοίο / τύπος σκάφους", "subject": "Αντικείμενο", "subject_ph": "Επιλέξτε υπηρεσία",
  "subject_other": "Άλλο / γενική ερώτηση",
  "message": "Περιγραφή", "message_ph": "Περιγράψτε το σύστημα, το σύμπτωμα και το χρονικό περιθώριο.",
  "urgency": "Είναι επείγον;", "urgency_no": "Όχι — προγραμματισμένη εργασία",
  "urgency_yes": "Ναι — το πλοίο επηρεάζεται",
  "consent": "Συναινώ στην επεξεργασία των στοιχείων μου για την απάντηση στο αίτημά μου.",
  "submit": "Αποστολή αιτήματος",
  "required": "υποχρεωτικό",
 },
 "form_note": "Η φόρμα δεν είναι ακόμη συνδεδεμένη — προς ενεργοποίηση πριν το launch. "
              "Στο μεταξύ χρησιμοποιήστε το τηλέφωνο, το WhatsApp ή το email.",

 # --- 404 ---------------------------------------------------------------
 "e404_title": "Η σελίδα δεν βρέθηκε | GM Marine Automation",
 "e404_h1": "Η σελίδα δεν βρέθηκε",
 "e404_p": "Ο σύνδεσμος που ακολουθήσατε δεν αντιστοιχεί σε σελίδα του site. Δοκιμάστε από τις υπηρεσίες "
           "ή επικοινωνήστε μαζί μας απευθείας.",
},
}

# ===========================================================================
COPY["en"] = {

 # --- Home -------------------------------------------------------------
 "home_title": "GM Marine Automation | Marine Electrical & Automation Systems",
 "home_desc": "Marine electrical & automation systems: generators, PMS, DEIF, synchronizing, alarm monitoring, retrofit and onboard troubleshooting. Greece & worldwide.",
 "hero_eyebrow": "Marine Power, Automation & Control Solutions",
 "hero_h1": "Marine electrical and automation, from an engineer who has sailed",
 "hero_lead": "Installation, upgrade and troubleshooting of marine electrical systems, generators, "
              "power management and control systems. Backed by 15+ years as an Electro-Technical "
              "Officer in the merchant marine on gas carriers — experience that goes into every job.",
 "hero_stats": [
  ("15+", "years at sea as an Electro-Technical Officer"),
  ("24/7", "emergency technical support"),
  ("15", "onboard fields of specialisation"),
  ("GR + Worldwide", "coverage in Greece and internationally"),
 ],

 "intro_eyebrow": "Who we are",
 "intro_h2": "Technical knowledge earned in the engine room, not in a classroom",
 "intro_p": [
  "GM Marine Automation & Electrical System specialises in electrical and automation systems for "
  "ships and yachts. We install, repair and upgrade generators, switchboards, PLC/HMI systems, "
  "paralleling equipment, alarm monitoring and power management.",
  "Our difference is not commercial. It is that we have lived the fault from the other side: as "
  "crew, at sea, with the vessel operating and no possibility of waiting for a technician. That "
  "perspective defines what we consider finished work — documentation the crew can actually use, "
  "settings that can be explained, and systems that can be diagnosed without us.",
 ],

 "why_eyebrow": "Why us",
 "why_h2": "What 'experience at sea' means in practice",
 "why_items": [
  ("Diagnosis before replacement",
   "We start from measurements, drawings and alarm logs. Swapping parts until the symptom stops is "
   "not diagnosis — it is an invoice."),
  ("We work around a trading vessel",
   "Scheduling follows the port stay and the trade, in phases where needed. Downtime is part of the "
   "cost and we treat it as such."),
  ("Documentation that is handed over",
   "As-built drawings, parameter files, I/O lists and test protocols. A vessel should not depend on "
   "one supplier's memory."),
  ("Clear boundaries of responsibility",
   "We state what is a temporary repair and what is permanent, what is electrical and what is "
   "mechanical, and what we do not take on."),
 ],

 "sectors_eyebrow": "Who we serve",
 "sectors_h2": "Shipping companies, technical departments and shipyards",
 "sectors_p": "We work with organisations that judge a technical partner on documentation and "
              "consistency, not on unit price.",
 "sectors_items": [
  ("Shipping companies & ship managers", "Fleet technical support, planned work and emergency attendance."),
  ("Vessel technical departments", "Second opinion, incident analysis, survey preparation and support during inspections."),
  ("Shipowners", "Condition assessment of the installation, retrofit studies and independent verification of third-party work."),
  ("Shipyards & marine service companies", "Specialist support in automation and generator control during projects."),
 ],

 "process_eyebrow": "How we work",
 "process_h2": "From the first message to handover",
 "process_steps": [
  ("Description & pre-assessment",
   "You send the fault, the vessel type and the equipment. We ask for alarm logs, drawings and "
   "photographs of nameplates. A great deal is narrowed down at this stage already."),
  ("A proposal with a defined scope",
   "You receive an intervention plan: what will be checked, what is required from the vessel, "
   "estimated time and downtime, and what is not included."),
  ("Work onboard",
   "Intervention with measurements and records at every step. The technical department is updated "
   "daily, not only at the end."),
  ("Handover & documentation",
   "Test protocols, updated drawings, backups and a recommended spares list. We stay available for "
   "support afterwards."),
 ],

 "home_faq_h2": "Frequently asked questions",
 "home_faq": [
  ("What vessel types do you work on?",
   "Commercial vessels and commercial or private yachts. Our experience comes primarily from gas "
   "carriers, where electrical and automation requirements are among the most demanding at sea."),
  ("Do you travel outside Greece?",
   "Yes. We serve both the Greek and the international shipping market. For international attendance "
   "we agree mobilization with the technical department and give a realistic ETA."),
  ("Do you only work on DEIF equipment?",
   "No. DEIF is the most common generator-control and power-management system on the vessels we "
   "serve, but we support installations from other manufacturers as well."),
  ("Can you attend while the vessel is trading?",
   "Where the manager's procedures allow it, yes — as a riding squad or by joining at an "
   "intermediate port."),
  ("How do you price work?",
   "On scope, time onboard and materials. We do not publish a price list, because two vessels with "
   "the same symptom rarely need the same work. Every quotation states explicitly what is included."),
  ("What do you need in order to quote?",
   "Vessel type and size, the system concerned, manufacturer and model if known, a description of "
   "the problem, and the port or area."),
 ],

 "cta_h2": "Send us the problem",
 "cta_p": "Describe the system, the vessel and what you are seeing. You get back a concrete "
          "intervention plan and a defined scope of work.",

 "articles_eyebrow": "Technical insights",
 "articles_h2": "Notes from the engine room",
 "articles_p": "Written for engineers, not for search engines. What we meet often and think is worth writing down.",

 # --- Services hub ------------------------------------------------------
 "services_title": "Marine Electrical & Automation Services | GM Marine Automation",
 "services_desc": "Fifteen fields in marine electrical and automation: generators, PMS, DEIF, synchronizing, switchboards, AMS, PLC/SCADA, retrofit and commissioning.",
 "services_h1": "Services",
 "services_lead": "Fifteen fields covering a vessel's electrical power and automation, from the generator "
                  "to the engineer's screen. Each page sets out what we take on, which symptoms we "
                  "address and what is delivered.",
 "services_featured_h2": "Core capabilities",
 "services_all_h2": "All services",

 # --- Company -----------------------------------------------------------
 "about_title": "Company | GM Marine Automation & Electrical System",
 "about_desc": "Founded in 2022 by an Electro-Technical Officer with 15+ years on gas carriers. Marine electrical & automation systems, in Greece and worldwide.",
 "about_h1": "Company",
 "about_lead": "A small technical team with a seagoing background, working on systems where a mistake "
               "cannot be fixed by booking a second appointment.",
 "about_story_h2": "From the engine room to technical support",
 "about_story": [
  "GM Marine Automation & Electrical System was founded in 2022. Behind it are more than 15 years "
  "of service as an Electro-Technical Officer in the merchant marine on gas carriers — vessels with "
  "some of the most demanding marine electrical and automation installations afloat.",
  "Through those years the work was the same every day: power generation and distribution, alarm "
  "monitoring, control systems and onboard troubleshooting, with the vessel operating and nobody to "
  "wait for. Whatever had to be solved was solved on the spot, with what was available.",
  "That experience is the basis of the company today. It does not change what we do — it changes "
  "how. We know what it means to be handed a system with no documentation, because we have been "
  "handed one. We know which setting will cause a problem in six months, because we have lived it.",
 ],
 "about_principles_h2": "How we work",
 "about_principles": [
  ("We measure before we propose",
   "No proposal without a survey of the existing condition. A quotation written without measurement "
   "is an estimate, and must be declared as one."),
  ("The vessel keeps the documentation",
   "Parameter files, PLC programs, drawings and protocols are handed to the owner. We do not build "
   "dependency on ourselves."),
  ("We do not weaken protections to clear an alarm",
   "Protection settings are changed only with documentation and in agreement with the technical "
   "department and, where required, class."),
  ("We say what we do not take on",
   "Our specialisation is the electrical and automation side. Where work crosses into another "
   "discipline we say so and cooperate cleanly."),
 ],
 "about_facts_h2": "Facts",
 "about_capabilities_h2": "Fields of specialisation",
 "about_capabilities_p": "The areas we take on work in, from power through to control.",
 "about_equipment_h2": "Equipment & manufacturers",
 "about_equipment_p": "We have experience with, and provide technical support for, systems and equipment "
                      "from leading manufacturers of marine automation, generator control and power "
                      "management. For a specific model or series, get in touch.",

 # --- Projects ----------------------------------------------------------
 "projects_title": "Projects & Scope of Work | GM Marine Automation",
 "projects_desc": "Typical marine electrical and automation projects: generator control retrofit, AMS rehabilitation, PMS commissioning and switchboard upgrades.",
 "projects_h1": "Projects & scope of work",
 "projects_lead": "The kinds of project we take on, with their real extent: what is asked for, what we "
                  "usually find, and what is delivered at the end.",
 "projects_note_h": "A note on client references",
 "projects_note": "The descriptions below set out typical projects in this sector and the scope of work "
                  "we take on. Vessel or client names are not published without their explicit consent. "
                  "For specific project references and testimonials, please get in touch.",
 "projects_types": [
  ("Generator control system retrofit",
   "Replacement of obsolete generator controllers and protection units in a main switchboard, "
   "retaining the existing wiring and CT/VT.",
   ["Survey of existing wiring and logic", "Parameter setup of new units and protections",
    "Paralleling and load-sharing tests", "Updated single-line and parameter files"],
   "deif-power-management"),
  ("Alarm Monitoring System rehabilitation",
   "Restoring reliability to an AMS carrying a large number of standing or inhibited points, without "
   "replacing the platform.",
   ["Full export and review of the alarm point list", "Physical verification of sensors in operation",
    "Limits, delays and grouping reset", "Test protocol per point"],
   "alarm-monitoring-systems"),
  ("PMS commissioning and blackout testing",
   "Verification and documentation of the entire power-management logic after installation or "
   "upgrade, against real tests.",
   ["Power balance checked against today's loads", "Load-dependent start and load-shedding tests",
    "Controlled blackout and recovery test", "Signed protocols per scenario"],
   "power-management-systems"),
  ("Emergency attendance onboard",
   "Attendance on a vessel with a fault limiting its operation, aimed at safe restoration within the "
   "available window.",
   ["Immediate remote assessment from logs and photographs", "Fault finding with measurements onboard",
    "Safe restoration, temporary or permanent and clearly stated", "Technical report with root cause"],
   "troubleshooting-repairs"),
  ("Main / emergency switchboard upgrade",
   "Targeted upgrade of a board's metering, protection and automation, without replacing the "
   "enclosure and breakers where they are sound.",
   ["Thermographic survey under load", "Interlock verification and restoration",
    "Instrument and protection relay replacement", "Protection coordination study where required"],
   "switchboards"),
  ("Automation network diagnosis",
   "Locating periodic communication loss on CAN bus or Modbus, with physical-layer measurement and "
   "traffic analysis.",
   ["Termination measurement and shielding checks", "Error-frame capture and analysis",
    "Identification of the node or route causing the fault", "Topology diagram and extension note"],
   "marine-networks"),
 ],

 # --- Contact -----------------------------------------------------------
 "contact_title": "Contact & Request a Quote | GM Marine Automation",
 "contact_desc": "Contact GM Marine Automation for a technical quotation or an emergency attendance. Phone, WhatsApp, email and request form. 24/7 emergency technical support.",
 "contact_h1": "Contact",
 "contact_lead": "For a quotation, a technical question or an emergency. The more specific the "
                 "description, the more useful the first reply.",
 "contact_form_h2": "Request a quote",
 "contact_form_p": "Fill in what you know. Not everything is required for a first assessment.",
 "contact_direct_h2": "Direct contact",
 "contact_emergency_h2": "Emergency attendance",
 "contact_emergency_p": "For a fault affecting the vessel's operation, call directly. The phone is "
                        "available outside office hours for emergencies.",
 "contact_what_h2": "What to send us",
 "contact_what": [
  "Vessel type and size, and the port or area",
  "The system concerned — generator, switchboard, PMS, AMS, network",
  "Manufacturer and model, or a photograph of the nameplate",
  "A description of the symptom and when it appears",
  "Alarm log or controller screenshots, if available",
  "Installation drawings, if available",
 ],
 "form_fields": {
  "name": "Full name", "company": "Company", "email": "Email", "phone": "Phone",
  "vessel": "Vessel / craft type", "subject": "Subject", "subject_ph": "Select a service",
  "subject_other": "Other / general enquiry",
  "message": "Description", "message_ph": "Describe the system, the symptom and your time window.",
  "urgency": "Is this urgent?", "urgency_no": "No — planned work",
  "urgency_yes": "Yes — the vessel is affected",
  "consent": "I consent to my details being processed in order to answer my enquiry.",
  "submit": "Send request",
  "required": "required",
 },
 "form_note": "The form is not connected yet — to be activated before launch. In the meantime "
              "please use the phone, WhatsApp or email.",

 # --- 404 ---------------------------------------------------------------
 "e404_title": "Page not found | GM Marine Automation",
 "e404_h1": "Page not found",
 "e404_p": "The link you followed does not match a page on this site. Try the services, or contact us "
           "directly.",
}
