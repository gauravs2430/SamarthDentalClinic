"""Clinic facts, reviews and FAQs for Samarth Dental Clinic.

Everything a client would want to change lives here rather than in markup.
Update a value, re-run ``python3 tools/build.py``, and every page follows.
"""

CLINIC = {
    "name": "Samarth Dental Clinic",
    "short": "Samarth Dental",
    "tagline": "Dental Clinic in Vavol, Gandhinagar",
    "doctor": "Dr. Dhvani Joshi",
    "doctor_role": "Dental Surgeon &amp; Founder",
    "street": "Shop No. S09, ShantiNagar Shopping",
    "area": "Vavol, Gandhinagar",
    "landmark": "Near Hotel Leela, Vavol",
    "city": "Gandhinagar",
    "state": "Gujarat",
    "pin": "382016",
    "phone_display": "+91 63559 64694",
    "phone_link": "+916355964694",
    "whatsapp": "916355964694",
    "email": "care@samarthdentalclinic.in",
    "rating": "5.0",
    "reviews": "158",
    "hours_short": "Mon&ndash;Sat: 10:00 AM &ndash; 1:00 PM &amp; 4:00 PM &ndash; 7:00 PM",
    "maps_query": "Samarth+Dental+Clinic+ShantiNagar+Shopping+Vavol+Gandhinagar",
    "plus_code": "6JJF+P8 Gandhinagar",
    "base_url": "https://samarthdentalclinic.in",
}

CLINIC["address_line"] = "{street}, {area}, {state} {pin}".format(**CLINIC)

HOURS = [
    ("Monday", "10:00 AM &ndash; 1:00 PM, 4:00 &ndash; 7:00 PM", False),
    ("Tuesday", "10:00 AM &ndash; 1:00 PM, 4:00 &ndash; 7:00 PM", False),
    ("Wednesday", "10:00 AM &ndash; 1:00 PM, 4:00 &ndash; 7:00 PM", False),
    ("Thursday", "10:00 AM &ndash; 1:00 PM, 4:00 &ndash; 7:00 PM", False),
    ("Friday", "10:00 AM &ndash; 1:00 PM, 4:00 &ndash; 7:00 PM", False),
    ("Saturday", "10:00 AM &ndash; 1:00 PM, 4:00 &ndash; 7:00 PM", False),
    ("Sunday", "Closed", True),
]

# Verbatim Google reviews for the clinic, lightly trimmed for length.
REVIEWS = [
    ("Dipsa Mehta", "DM", "My husband received dental treatment at Samarth Dental Clinic from "
     "Dr. Dhvani Joshi, and we are very satisfied with the results. She is very polite, skilled, "
     "and explains everything clearly. The treatment was smooth and almost pain-free."),
    ("Ravina Vaishnav", "RV", "I had my root canal and tooth removal done here and my experience "
     "was truly excellent. Dr. Dhvani is extremely caring, patient and professional. She explained "
     "every procedure in detail and her guidance really helped reduce my fear and anxiety."),
    ("Jay Chauhan", "JC", "Dr. Dhvani Joshi was incredibly kind and attentive. She listened "
     "carefully, answered all my questions, and made me feel at ease. The staff is very cooperative "
     "and empathetic. That is the care we are getting at this clinic."),
    ("Karnavi Shukla", "KS", "I am so comfortable when I am there &mdash; Dr. Dhvani is friendly and "
     "you feel you are a priority to her. I got my root canal done here. The treatment is really "
     "good and the hygiene of the clinic is up to the mark."),
    ("Bunty Goswami", "BG", "Doctor is very polite and has empathetic behaviour for her patients. "
     "She handled each surgery step with care and accuracy. We are sure that from now on she will be "
     "our family dentist."),
    ("Manan Dave", "MD", "I had a great experience. Clean clinic, minimal wait time, and great care. "
     "I am very happy with my visit and would definitely recommend."),
    ("Safalata Saraswat", "SS", "Painless and comfortable experience, professional and friendly "
     "staff, and clear communication from Dr. Dhvani Joshi about the treatment plan and the costs."),
    ("Niralee Trivedi", "NT", "Excellent work done by Dr. Dhvani. Samarth Dental Clinic is the best "
     "place for dental treatment in our city."),
]

FAQS = [
    ("Do I need an appointment, or can I walk in?",
     "Appointments are recommended so you are seen at a fixed time with no waiting. Call or WhatsApp "
     "+91 63559 64694 and we will confirm a slot the same day. Walk-in patients are accommodated "
     "whenever the schedule allows, and genuine dental emergencies are always given priority."),
    ("Will the treatment hurt?",
     "Almost every procedure we carry out &mdash; fillings, root canals, extractions and implants &mdash; is "
     "done under effective local anaesthesia, so you should feel pressure but not pain. We also "
     "explain each step before we begin, which is what most nervous patients tell us made the "
     "difference."),
    ("What are your clinic timings?",
     "We are open Monday to Saturday, 10:00 AM to 1:00 PM in the morning and 4:00 PM to 7:00 PM in "
     "the evening. The clinic is closed on Sundays."),
    ("Where exactly is the clinic in Vavol?",
     "Shop No. S09, ShantiNagar Shopping, Vavol, Gandhinagar 382016 &mdash; close to Hotel Leela. There is "
     "parking available right outside the shopping complex."),
    ("How much will my treatment cost?",
     "You are given a written treatment plan with the cost of each step before any work starts, so "
     "there are no surprises later. Where more than one option exists, we explain the difference in "
     "price and longevity and let you choose."),
    ("Do you treat young children?",
     "Yes. We look after children's check-ups, fluoride application, sealants, milk-tooth fillings "
     "and extractions. First visits are deliberately kept short and friendly so that a child leaves "
     "without any fear of the dentist."),
    ("How do you sterilise your instruments?",
     "Instruments are scrubbed, pouched and autoclaved after every single patient. Needles, gloves, "
     "suction tips and other disposables are used once and discarded in front of you."),
    ("Which payment methods do you accept?",
     "Cash, UPI, cards and NFC mobile payments are all accepted at the clinic."),
    ("How many visits does a root canal take?",
     "Most root canals are completed in one or two sittings. A tooth with an active infection may "
     "need an extra visit so the infection can settle before the tooth is sealed and crowned."),
    ("How often should I come for a check-up?",
     "Once every six months for a check-up and cleaning. It is the cheapest dentistry there is &mdash; "
     "small problems get caught while they still only need a filling."),
]
