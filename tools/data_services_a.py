"""Service pages, part 1 of 2. See data_services_b.py for the rest."""

SERVICES_A = [
    {
        "slug": "dental-implants",
        "name": "Dental Implants",
        "nav": "Dental Implants",
        "img": "images/dental-implants.jpg",
        "banner": "images/dental-implants.jpg",
        "card": "A titanium root placed in the jaw to carry a single crown, a bridge or a full arch "
                "&mdash; the closest thing there is to getting your own tooth back.",
        "meta": "Dental implants in Vavol, Gandhinagar at Samarth Dental Clinic. Single tooth, "
                "multiple teeth and full-arch implant treatment by Dr. Dhvani Joshi.",
        "intro": [
            "An implant is a small titanium screw that takes the place of a missing tooth's root. "
            "Once the bone has grown around it, a crown is fixed on top &mdash; and from that point on you "
            "brush it, bite with it and forget about it, because nothing is clipped in or taken out "
            "at night.",
            "It is the only replacement that does not rely on the teeth beside the gap. A bridge has "
            "to be cemented onto healthy neighbouring teeth, which means grinding them down. An "
            "implant stands on its own and, just as importantly, keeps the jawbone underneath it in "
            "use so it does not shrink away.",
        ],
        "signs": [
            "A tooth has been lost, extracted or knocked out",
            "You do not want healthy teeth trimmed to hold a bridge",
            "An existing denture slips, clicks or rubs",
            "Several teeth are missing in the same area",
            "A tooth is beyond saving and needs to be replaced",
        ],
        "steps": [
            ("Assessment and X-ray", "We check bone height and width on a digital X-ray, look at "
             "your bite, and confirm the site is suitable. You get the full plan and cost in writing."),
            ("Placing the implant", "Under local anaesthesia the implant is placed into the bone. "
             "It is a quiet, roughly 45-minute appointment and most people go back to work the "
             "following day."),
            ("Healing", "Over the next few months the bone fuses to the implant surface. A temporary "
             "tooth keeps the gap filled and lets you eat normally while that happens."),
            ("Fitting the crown", "An impression or digital scan is taken, and a crown is made to "
             "match the shade and shape of your own teeth before being fixed onto the implant."),
        ],
        "benefits": [
            "Looks and functions like a natural tooth",
            "Healthy neighbouring teeth are left untouched",
            "Preserves the jawbone in the gap",
            "Fixed in place &mdash; never removed for cleaning",
            "Can support a single crown, a bridge or a full arch",
        ],
        "facts": [
            ("Visits", "3 to 4 across the treatment"),
            ("Anaesthesia", "Local &mdash; you stay awake and comfortable"),
            ("Healing time", "Usually 3 to 6 months before the final crown"),
            ("Care needed", "Normal brushing, flossing and six-monthly check-ups"),
        ],
    },
    {
        "slug": "root-canal",
        "name": "Root Canal Treatment",
        "nav": "Root Canal Treatment",
        "img": "images/treatment.jpg",
        "banner": "images/treatment.jpg",
        "card": "The treatment that saves a badly decayed or infected tooth instead of removing it "
                "&mdash; usually finished in one or two comfortable sittings.",
        "meta": "Painless root canal treatment (RCT) in Vavol, Gandhinagar. Single-sitting RCT and "
                "crowns at Samarth Dental Clinic by Dr. Dhvani Joshi.",
        "intro": [
            "When decay or a crack reaches the nerve inside a tooth, that nerve becomes inflamed or "
            "infected &mdash; which is what produces the throbbing, keeps-you-awake kind of toothache. A "
            "root canal removes the infected tissue from inside the tooth, disinfects the space and "
            "seals it, so the outer tooth can stay and keep doing its job.",
            "Root canals have an unfair reputation. The pain people associate with them is the pain "
            "of the infection, not the treatment &mdash; the treatment is what takes it away. Under proper "
            "anaesthesia, most patients are surprised by how uneventful the appointment is.",
        ],
        "signs": [
            "Severe or throbbing toothache, often worse at night",
            "Lingering sensitivity to hot or cold",
            "Pain when biting down on one particular tooth",
            "Swelling of the gum or face near a tooth",
            "A tooth that has darkened after an injury",
            "A deep cavity that has reached the nerve",
        ],
        "steps": [
            ("Diagnosis", "A digital X-ray shows how far the infection has travelled and how many "
             "canals the tooth has."),
            ("Numbing the tooth", "Local anaesthesia is given and we wait until the tooth is fully "
             "numb before touching it."),
            ("Cleaning the canals", "The infected tissue is removed and the canals are shaped, "
             "disinfected and dried."),
            ("Sealing and crowning", "The canals are filled and sealed. Because a treated tooth is "
             "more brittle, a crown is then fitted to protect it from cracking."),
        ],
        "benefits": [
            "Keeps your own tooth instead of extracting it",
            "Ends the toothache and clears the infection",
            "Most cases finished in one or two visits",
            "Avoids the cost of replacing a missing tooth",
            "Restores normal chewing on that side",
        ],
        "facts": [
            ("Visits", "1 to 2 for most teeth"),
            ("Appointment length", "About 45 to 90 minutes"),
            ("Anaesthesia", "Local &mdash; the tooth is fully numbed"),
            ("Afterwards", "A crown is strongly recommended to protect the tooth"),
        ],
    },
    {
        "slug": "braces-aligners",
        "name": "Braces &amp; Clear Aligners",
        "nav": "Braces &amp; Aligners",
        "img": "images/braces-metal.jpg",
        "banner": "images/braces-metal.jpg",
        "card": "Straighten crowded, gapped or protruding teeth with metal braces, ceramic braces or "
                "near-invisible clear aligners.",
        "meta": "Braces and clear aligner treatment in Vavol, Gandhinagar. Metal, ceramic and "
                "invisible options at Samarth Dental Clinic.",
        "intro": [
            "Crooked and crowded teeth are not only a cosmetic matter. Overlapping teeth trap plaque "
            "in places a brush cannot reach, which leads to decay and gum problems, and a bite that "
            "does not meet evenly wears certain teeth down faster than the rest.",
            "Orthodontic treatment moves teeth into a position where they clean easily and meet "
            "properly. We will talk you through metal braces, tooth-coloured ceramic braces and "
            "removable clear aligners, including what each one costs and how visible it is day to day.",
        ],
        "signs": [
            "Crowded or overlapping teeth",
            "Noticeable gaps between teeth",
            "Upper front teeth that protrude",
            "Lower teeth biting ahead of the upper ones",
            "Upper and lower teeth that do not meet when you bite",
            "Difficulty cleaning between certain teeth",
        ],
        "steps": [
            ("Records and planning", "Photographs, X-rays and impressions or a digital scan are "
             "taken so we can map out exactly how the teeth need to move."),
            ("Choosing the appliance", "We compare metal braces, ceramic braces and clear aligners "
             "against your case, your budget and how visible you are willing for it to be."),
            ("Fitting", "Braces are bonded to the teeth in a single appointment, or your first set "
             "of aligners is issued with instructions on wear time."),
            ("Regular adjustments", "You are seen every four to six weeks for adjustments, and at "
             "the end a retainer holds the new position permanently."),
        ],
        "benefits": [
            "Teeth that are far easier to keep clean",
            "An even bite that spreads chewing forces properly",
            "Tooth-coloured and invisible options available",
            "Suitable for teenagers and adults alike",
            "A noticeably more confident smile",
        ],
        "facts": [
            ("Treatment time", "Commonly 12 to 24 months, depending on the case"),
            ("Visits", "Every 4 to 6 weeks"),
            ("Options", "Metal braces, ceramic braces, clear aligners"),
            ("Afterwards", "A retainer must be worn to hold the result"),
        ],
    },
    {
        "slug": "smile-design",
        "name": "Smile Design &amp; Veneers",
        "nav": "Smile Design &amp; Veneers",
        "img": "images/smile-closeup.jpg",
        "banner": "images/smile-closeup.jpg",
        "card": "A planned combination of veneers, crowns, whitening and reshaping that corrects the "
                "colour, shape and proportion of your front teeth.",
        "meta": "Smile design and dental veneers in Vavol, Gandhinagar. Planned cosmetic dentistry "
                "at Samarth Dental Clinic by Dr. Dhvani Joshi.",
        "intro": [
            "Smile design is cosmetic dentistry done in the right order. Rather than fixing one "
            "tooth at a time, we look at your whole smile &mdash; tooth colour, length, width, the shape "
            "of the gum line, how much shows when you talk &mdash; and plan the changes as a set.",
            "The work itself might be veneers, crowns, whitening, tooth-coloured bonding, gum "
            "contouring or a mix of those. What matters is that it is planned against your own face, "
            "so the finished smile looks like it belongs to you rather than being obviously done.",
        ],
        "signs": [
            "Front teeth that are chipped, worn or uneven in length",
            "Deep staining that whitening alone will not lift",
            "A gap between the front teeth",
            "Teeth that look too small for the smile",
            "Old fillings or crowns that no longer match",
            "Too much gum showing when you smile",
        ],
        "steps": [
            ("Listening first", "We start with what you actually dislike about your smile, and "
             "photographs help make that concrete."),
            ("The plan", "You are shown what can be changed, what it will involve and what each part "
             "costs &mdash; before anything is started."),
            ("Preparation", "Depending on the plan, minimal tooth surface is prepared and a scan or "
             "impression goes to the laboratory."),
            ("Fitting and refining", "Veneers or crowns are tried in, the shade and shape are "
             "adjusted with you looking in the mirror, and then they are bonded."),
        ],
        "benefits": [
            "The whole smile is planned, not patched piecemeal",
            "Colour, shape and proportion corrected together",
            "Minimal removal of natural tooth in most cases",
            "Long-lasting, stain-resistant materials",
            "Approved by you before it is made permanent",
        ],
        "facts": [
            ("Visits", "Typically 2 to 4"),
            ("Materials", "Ceramic veneers, zirconia and layered composite"),
            ("Longevity", "Well-maintained veneers last many years"),
            ("Care needed", "Normal brushing; avoid biting nails or hard objects"),
        ],
    },
    {
        "slug": "teeth-whitening",
        "name": "Teeth Whitening",
        "nav": "Teeth Whitening",
        "img": "images/teeth-whitening.jpg",
        "banner": "images/teeth-whitening.jpg",
        "card": "Professional bleaching that lifts years of tea, coffee and tobacco staining in a "
                "single appointment, without damaging the enamel.",
        "meta": "Professional teeth whitening in Vavol, Gandhinagar. Safe in-clinic bleaching at "
                "Samarth Dental Clinic.",
        "intro": [
            "Teeth pick up colour slowly from tea, coffee, tobacco and simply from age. Professional "
            "whitening uses a controlled-strength gel, applied with your gums properly protected, to "
            "lift that staining out of the enamel rather than scrubbing at the surface.",
            "The results are considerably more predictable than anything bought over a counter, and "
            "far safer. Before we whiten, we check for decay, gum inflammation and exposed roots &mdash; "
            "whitening over untreated problems is what causes the horror stories about sensitivity.",
        ],
        "signs": [
            "Teeth that have yellowed gradually over the years",
            "Staining from tea, coffee, red wine or tobacco",
            "A wedding, interview or event coming up",
            "Teeth that look dull next to a new crown",
            "Over-the-counter whitening kits that did nothing",
        ],
        "steps": [
            ("Check-up first", "Decay, gum disease and sensitivity are treated first, because "
             "whitening over them is uncomfortable and ineffective."),
            ("Cleaning", "A scaling and polishing removes surface deposits so the gel works on the "
             "enamel itself."),
            ("Protecting the gums", "A barrier is placed over the gums and lips before the "
             "whitening gel is applied."),
            ("Whitening", "The gel is activated in short cycles, with the shade checked between "
             "each one so we stop at a result that suits your face."),
        ],
        "benefits": [
            "A visible change in one appointment",
            "Enamel-safe, dentist-supervised strength",
            "Gums protected throughout the procedure",
            "Shade checked as we go, not set blindly",
            "Top-up options for later, if you want them",
        ],
        "facts": [
            ("Appointment length", "About 60 to 90 minutes"),
            ("Visits", "Usually 1"),
            ("How long it lasts", "Commonly 1 to 2 years with care"),
            ("Good to know", "Crowns and fillings do not change shade"),
        ],
    },
    {
        "slug": "crowns-bridges",
        "name": "Crowns &amp; Bridges",
        "nav": "Crowns &amp; Bridges",
        "img": "images/digital-scan.jpg",
        "banner": "images/digital-scan.jpg",
        "card": "Zirconia and ceramic crowns that rebuild a broken or root-treated tooth, and "
                "bridges that close a gap without surgery.",
        "meta": "Dental crowns and bridges in Vavol, Gandhinagar. Zirconia, ceramic and metal-free "
                "options at Samarth Dental Clinic.",
        "intro": [
            "A crown is a cap that covers a tooth completely. It is what you need when a tooth has "
            "broken, has been root-treated, or has so little structure left that another filling "
            "would simply fall out. It holds the remaining tooth together and takes the force of "
            "chewing off it.",
            "A bridge replaces a missing tooth by joining crowns on the teeth either side of the "
            "gap. It is fixed, needs no surgery, and is often the quickest way to get a gap closed &mdash; "
            "though it does mean preparing the neighbouring teeth, which is why we always compare it "
            "with an implant before you decide.",
        ],
        "signs": [
            "A tooth that has cracked or broken",
            "A tooth that has had root canal treatment",
            "A filling so large the tooth flexes when you bite",
            "A single missing tooth with healthy teeth either side",
            "An old metal crown you want replaced with a natural shade",
            "Heavily worn-down back teeth",
        ],
        "steps": [
            ("Preparing the tooth", "Under local anaesthesia the tooth is shaped so the crown will "
             "sit flush and not feel bulky."),
            ("Scan or impression", "A digital scan or impression records the shape precisely and is "
             "sent to the laboratory with your shade."),
            ("Temporary crown", "A temporary is fitted so you can eat and smile normally while the "
             "permanent one is made."),
            ("Fitting", "The crown is tried in, the fit and bite are checked and adjusted, and then "
             "it is cemented in place."),
        ],
        "benefits": [
            "Rebuilds a tooth that is too weak to fill",
            "Metal-free zirconia and ceramic options",
            "Shade matched to your surrounding teeth",
            "Restores full chewing strength",
            "Closes a gap without any surgery",
        ],
        "facts": [
            ("Visits", "2 in most cases"),
            ("Materials", "Zirconia, all-ceramic, metal-ceramic"),
            ("Longevity", "Many years with good hygiene"),
            ("Anaesthesia", "Local, for the preparation appointment"),
        ],
    },
]
