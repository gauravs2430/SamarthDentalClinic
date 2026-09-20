"""Reviews, Contact, Appointment, FAQ, Dental Tips and 404 pages."""

from chrome import STARS, banner, hours_block, icon
from data_clinic import CLINIC, FAQS, REVIEWS

TIPS = [
    ("Brush twice a day",
     "Brush for two minutes, morning and night, with a soft brush. Use small circles and angle the "
     "brush towards the gum line."),
    ("Clean between the teeth",
     "A toothbrush cannot reach between teeth. Floss or use an interdental brush once a day."),
    ("Do not rinse after brushing",
     "Spit out the toothpaste and leave the fluoride on the teeth. Rinsing with water washes it away."),
    ("Bleeding gums",
     "Healthy gums should not bleed when you brush. Bleeding usually means gum inflammation. A "
     "cleaning and better brushing often settles it if treated early."),
    ("Sugar and teeth",
     "How often you have sugar matters more than how much. Keep sweets and sweet drinks to mealtimes."),
    ("Tooth sensitivity",
     "Pain with cold, sweet food or air can mean a cavity, a crack or receding gums. Mention it at "
     "your check-up rather than only using sensitive toothpaste."),
    ("Cracked or chipped teeth",
     "Enamel does not heal. A small chip can often be filled. Left alone it may need a crown or a "
     "root canal."),
    ("Regular check-ups",
     "A check-up every six months helps catch a cavity while it still needs a filling, not a root "
     "canal."),
]


def reviews(services):
    cards = "".join(f"""        <article class="quote-card">
          <p class="stars" aria-label="Rated 5 out of 5">{STARS}</p>
          <blockquote>{text}</blockquote>
          <div class="quote-who">
            <span class="avatar" aria-hidden="true">{initials}</span>
            <span><strong>{name}</strong><span>Google review</span></span>
          </div>
        </article>
""" for name, initials, text in REVIEWS)

    body = banner(
        "Patient Reviews",
        f"Rated {CLINIC['rating']} out of 5 by {CLINIC['reviews']}+ patients on Google.",
        [("Reviews", None)],
        "images/happy-patient.jpg",
    ) + f"""  <section class="section">
    <div class="container">
      <div class="section-head center">
        <h2>What Patients Say</h2>
        <p>Reviews left on Google, shown as written apart from trimming for length.</p>
      </div>
      <div class="service-grid">
{cards}      </div>
      <div class="block-cta">
        <a class="btn btn-ink" href="https://www.google.com/maps/search/?api=1&amp;query={CLINIC['maps_query']}" target="_blank" rel="noopener">See Google Reviews</a>
      </div>
    </div>
  </section>

  <section class="section bg-sky">
    <div class="container" style="text-align:center">
      <h2>Leave a Review</h2>
      <p style="margin:12px auto 24px;max-width:520px">If you have been treated here, a Google review
      helps other patients decide.</p>
      <div class="hero-actions" style="justify-content:center">
        <a class="btn" href="https://www.google.com/maps/search/?api=1&amp;query={CLINIC['maps_query']}" target="_blank" rel="noopener">Write a Google Review</a>
        <a class="btn btn-outline" href="appointment.html">Book Appointment</a>
      </div>
    </div>
  </section>
"""
    return (
        f"Patient Reviews | {CLINIC['name']}, Vavol, Gandhinagar",
        f"Read {CLINIC['reviews']}+ patient reviews of Samarth Dental Clinic, Vavol, Gandhinagar — "
        f"rated {CLINIC['rating']} out of 5 on Google.",
        body,
        None,
    )


def contact(services):
    body = banner(
        "Contact Us",
        "Call, WhatsApp or visit the clinic in Vavol, Gandhinagar.",
        [("Contact", None)],
        "images/reception.jpg",
    ) + f"""  <section class="section">
    <div class="container">
      <div class="info-strip-grid" style="border:1px solid var(--line)">
        <div class="info-tile">
          <span class="info-tile-icon">{icon('phone', 22)}</span>
          <div>
            <h3>Phone &amp; WhatsApp</h3>
            <p><a href="tel:{CLINIC['phone_link']}">{CLINIC['phone_display']}</a></p>
          </div>
        </div>
        <div class="info-tile">
          <span class="info-tile-icon">{icon('pin', 22)}</span>
          <div>
            <h3>Address</h3>
            <p>{CLINIC['street']},<br>{CLINIC['area']} {CLINIC['pin']}</p>
          </div>
        </div>
        <div class="info-tile">
          <span class="info-tile-icon">{icon('clock', 22)}</span>
          <div>
            <h3>Opening hours</h3>
            <p>Mon&ndash;Sat: 10 AM &ndash; 1 PM<br>&amp; 4 PM &ndash; 7 PM &middot; Sun closed</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="container with-side">
      <div>
        <div class="section-head">
          <h2>Send a Message</h2>
          <p>Fill the form and it opens WhatsApp with your message ready to send. You can also call
          the clinic.</p>
        </div>
        <div class="form-card">
          <form data-form data-form-title="Website enquiry — Samarth Dental Clinic" novalidate>
            <div class="form-alert">
              <span>{icon('smile', 20)}</span>
              <span>Thank you. Your message has been prepared in WhatsApp. If it did not open, please
              call us on {CLINIC['phone_display']}.</span>
            </div>
            <div class="form-grid">
              <div class="field">
                <label for="c-name">Your name <span class="req">*</span></label>
                <input id="c-name" name="Name" type="text" placeholder="Full name" required>
              </div>
              <div class="field">
                <label for="c-phone">Phone number <span class="req">*</span></label>
                <input id="c-phone" name="Phone" type="tel" placeholder="10-digit mobile number"
                       pattern="[0-9+ ]{{10,15}}" required>
              </div>
              <div class="field full">
                <label for="c-subject">Subject</label>
                <select id="c-subject" name="Subject">
                  <option>General enquiry</option>
                  <option>Toothache or emergency</option>
                  <option>Cost of a treatment</option>
                  <option>Second opinion</option>
                  <option>Appointment timing</option>
                </select>
              </div>
              <div class="field full">
                <label for="c-message">Message <span class="req">*</span></label>
                <textarea id="c-message" name="Message" placeholder="Describe the problem and how long it has been going on." required></textarea>
              </div>
            </div>
            <p class="form-note">We use your details only to reply to this enquiry.</p>
            <div style="margin-top:24px">
              <button class="btn" type="submit">{icon('chat', 18)} Send via WhatsApp</button>
            </div>
          </form>
        </div>
      </div>

      <aside class="side-stack">
        <div class="side-card contrast">
          <h3>Call the Clinic</h3>
          <p>Fastest way to confirm an appointment.</p>
          <a class="phone" href="tel:{CLINIC['phone_link']}">{CLINIC['phone_display']}</a>
          <a class="btn btn-block" href="https://wa.me/{CLINIC['whatsapp']}" target="_blank" rel="noopener">WhatsApp</a>
        </div>
        <div class="side-card">
          <h3>Clinic Hours</h3>
          {hours_block()}
        </div>
        <div class="side-card">
          <h3>How to Reach</h3>
          <p style="font-size:15px">{CLINIC['street']}, {CLINIC['area']}, {CLINIC['state']} {CLINIC['pin']}</p>
          <p style="font-size:15px;margin-top:12px"><strong>Landmark:</strong> {CLINIC['landmark']}</p>
          <p style="font-size:15px;margin-top:12px"><strong>Plus code:</strong> {CLINIC['plus_code']}</p>
          <p style="font-size:15px;margin-top:12px">Parking is available outside the shopping complex.</p>
          <p style="margin-top:18px"><a class="link-arrow" href="https://www.google.com/maps/search/?api=1&amp;query={CLINIC['maps_query']}" target="_blank" rel="noopener">Open in Maps</a></p>
        </div>
      </aside>
    </div>
  </section>

  <section class="section-sm bg-sky">
    <div class="container">
      <div class="map-frame">
        <iframe title="Map to Samarth Dental Clinic, Vavol, Gandhinagar" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
          src="https://maps.google.com/maps?q={CLINIC['maps_query']}&amp;t=&amp;z=16&amp;ie=UTF8&amp;iwloc=&amp;output=embed"></iframe>
      </div>
    </div>
  </section>
"""
    return (
        f"Contact &amp; Directions | {CLINIC['name']}, Vavol",
        f"Contact Samarth Dental Clinic, {CLINIC['street']}, {CLINIC['area']} {CLINIC['pin']}. "
        f"Call {CLINIC['phone_display']}. Open Mon-Sat, mornings and evenings.",
        body,
        None,
    )


def appointment(services):
    options = "".join(
        f'<option>{s["name"].replace("&amp;", "and")}</option>' for s in services
    )
    body = banner(
        "Book an Appointment",
        "Monday to Saturday, 10 AM&ndash;1 PM and 4 PM&ndash;7 PM.",
        [("Book Appointment", None)],
        "images/consultation.jpg",
    ) + f"""  <section class="section">
    <div class="container with-side">
      <div>
        <div class="section-head">
          <h2>Appointment Request</h2>
          <p>Submitting this form opens WhatsApp with your request written out. We reply with a
          confirmed time, usually the same day.</p>
        </div>
        <div class="form-card">
          <form data-form data-form-title="Appointment request — Samarth Dental Clinic" novalidate>
            <div class="form-alert">
              <span>{icon('calendar', 20)}</span>
              <span>Your appointment request is ready in WhatsApp. If it did not open, call us on
              {CLINIC['phone_display']}.</span>
            </div>
            <div class="form-grid">
              <div class="field">
                <label for="a-name">Patient name <span class="req">*</span></label>
                <input id="a-name" name="Patient name" type="text" placeholder="Full name" required>
              </div>
              <div class="field">
                <label for="a-phone">Phone number <span class="req">*</span></label>
                <input id="a-phone" name="Phone" type="tel" placeholder="10-digit mobile number"
                       pattern="[0-9+ ]{{10,15}}" required>
              </div>
              <div class="field">
                <label for="a-treatment">Treatment needed</label>
                <select id="a-treatment" name="Treatment">
                  <option>Not sure — please advise</option>
                  <option>Check-up and cleaning</option>
                  {options}
                  <option>Dental emergency</option>
                </select>
              </div>
              <div class="field">
                <label for="a-date">Preferred date <span class="req">*</span></label>
                <input id="a-date" name="Preferred date" type="date" required>
              </div>
              <div class="field">
                <label for="a-time">Preferred session</label>
                <select id="a-time" name="Preferred session">
                  <option>Morning (10:00 AM – 1:00 PM)</option>
                  <option>Evening (4:00 PM – 7:00 PM)</option>
                  <option>Either is fine</option>
                </select>
              </div>
              <div class="field">
                <label for="a-age">Patient age</label>
                <input id="a-age" name="Age" type="number" min="0" max="120" placeholder="e.g. 34">
              </div>
              <div class="field full">
                <label for="a-notes">Anything we should know</label>
                <textarea id="a-notes" name="Notes" placeholder="Symptoms, medical conditions or if you are nervous about treatment."></textarea>
              </div>
            </div>
            <p class="form-note">Sunday is a clinic holiday. Please choose Monday to Saturday.</p>
            <div style="margin-top:24px">
              <button class="btn" type="submit">{icon('calendar', 18)} Send Request</button>
            </div>
          </form>
        </div>
      </div>

      <aside class="side-stack">
        <div class="side-card contrast">
          <h3>Call to Book</h3>
          <p>Ring the clinic and we will book you in.</p>
          <a class="phone" href="tel:{CLINIC['phone_link']}">{CLINIC['phone_display']}</a>
          <a class="btn btn-block" href="https://wa.me/{CLINIC['whatsapp']}" target="_blank" rel="noopener">WhatsApp</a>
        </div>
        <div class="side-card">
          <h3>Clinic Hours</h3>
          {hours_block()}
        </div>
        <div class="side-card">
          <h3>Please Bring</h3>
          <ul class="ticks" style="gap:11px">
            <li>Previous X-rays or dental reports</li>
            <li>List of medicines you take</li>
            <li>Details of medical conditions such as diabetes</li>
          </ul>
        </div>
        <div class="side-card">
          <h3>Payments</h3>
          <p style="font-size:15px">Cash, UPI, cards and NFC mobile payments. Cost is given in writing
          before treatment starts.</p>
        </div>
      </aside>
    </div>
  </section>
"""
    return (
        f"Book a Dental Appointment in Vavol | {CLINIC['name']}",
        "Book a dental appointment at Samarth Dental Clinic, Vavol, Gandhinagar. Open Monday to "
        f"Saturday, mornings and evenings. Call {CLINIC['phone_display']}.",
        body,
        None,
    )


def faq(services):
    items = "".join(f"""        <div class="ac-item{' open' if i == 0 else ''}">
          <button class="ac-head" type="button" aria-expanded="{'true' if i == 0 else 'false'}">
            <span>{q}</span><span class="ac-sign" aria-hidden="true"></span>
          </button>
          <div class="ac-panel"><div><p>{a}</p></div></div>
        </div>
""" for i, (q, a) in enumerate(FAQS))

    body = banner(
        "FAQs",
        "Common questions about treatment, timings and booking.",
        [("FAQs", None)],
        "images/treatment-plan.jpg",
    ) + f"""  <section class="section">
    <div class="container with-side">
      <div>
        <div class="section-head">
          <h2>Frequently Asked Questions</h2>
        </div>
        <div class="accordion">
{items}        </div>
        <div class="callout" style="margin-top:36px">
          <p>Still have a question? Call
          <a href="tel:{CLINIC['phone_link']}">{CLINIC['phone_display']}</a>.</p>
        </div>
      </div>
      <aside class="side-stack">
        <div class="side-card contrast">
          <h3>Ask Us</h3>
          <p>Call or WhatsApp during clinic hours.</p>
          <a class="phone" href="tel:{CLINIC['phone_link']}">{CLINIC['phone_display']}</a>
          <a class="btn btn-block" href="contact.html">Send a Message</a>
        </div>
        <div class="side-card">
          <h3>Clinic Hours</h3>
          {hours_block()}
        </div>
        <div class="side-card">
          <h3>Treatments</h3>
          <div class="side-nav">
{"".join(f'<a href="{s["slug"]}.html">{s["nav"]}</a>' for s in services[:6])}
          </div>
        </div>
      </aside>
    </div>
  </section>
"""
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q.replace("&mdash;", "—"),
                "acceptedAnswer": {"@type": "Answer", "text": a.replace("&mdash;", "—")},
            }
            for q, a in FAQS
        ],
    }
    return (
        f"Dental FAQs | {CLINIC['name']}, Vavol, Gandhinagar",
        "Answers about dental costs, clinic timings, pain, sterilisation and treatment at Samarth "
        "Dental Clinic, Vavol, Gandhinagar.",
        body,
        schema,
    )


def dental_tips(services):
    cards = "".join(f"""        <article class="feature-card">
          <span class="feature-icon">{icon('tooth', 26)}</span>
          <h3>{title}</h3>
          <p>{text}</p>
        </article>
""" for title, text in TIPS)

    body = banner(
        "Dental Care Tips",
        "Simple advice for looking after your teeth at home.",
        [("Dental Tips", None)],
        "images/oral-care.jpg",
    ) + f"""  <section class="section">
    <div class="container">
      <div class="section-head center">
        <h2>Home Care Tips</h2>
        <p>This does not replace a check-up. If something hurts or bleeds, call the clinic.</p>
      </div>
      <div class="feature-grid">
{cards}      </div>
      <div class="callout" style="margin-top:40px">
        <p>If a tooth hurts, feels loose or has changed, call
        <a href="tel:{CLINIC['phone_link']}">{CLINIC['phone_display']}</a>.</p>
      </div>
    </div>
  </section>
"""
    return (
        f"Dental Care Tips | {CLINIC['name']}",
        "Practical dental care tips from Samarth Dental Clinic, Vavol, Gandhinagar — brushing, "
        "flossing, sensitivity, bleeding gums and check-ups.",
        body,
        None,
    )


def not_found(services):
    body = banner(
        "Page not found",
        "The page you were looking for has moved or no longer exists.",
        [("404", None)],
        "images/clinic-interior.jpg",
    ) + f"""  <section class="section">
    <div class="container" style="text-align:center">
      <h2>Page not found</h2>
      <p style="margin:16px auto 28px;max-width:480px">Try the home page or our list of treatments.
      You can also call {CLINIC['phone_display']}.</p>
      <div class="hero-actions" style="justify-content:center">
        <a class="btn" href="index.html">Back to Home</a>
        <a class="btn btn-outline" href="services.html">All Services</a>
      </div>
    </div>
  </section>
"""
    return "Page not found | " + CLINIC["name"], "Page not found.", body, None
