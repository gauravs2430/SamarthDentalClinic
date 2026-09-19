"""Reviews, Contact, Appointment, FAQ, Dental Tips and 404 pages."""

from chrome import STARS, banner, hours_block, icon
from data_clinic import CLINIC, FAQS, REVIEWS

TIPS = [
    ("Brush for two minutes, twice &mdash; and mean it",
     "Most people brush for under 45 seconds and believe it was two minutes. Use a timer or a song "
     "once and you will see the gap. Two minutes, soft bristles, small circles, and angle the brush "
     "towards the gum line rather than scrubbing straight across it."),
    ("The gaps between teeth are where trouble starts",
     "A brush cleans three of the five surfaces of a tooth. The two it cannot reach are exactly where "
     "decay and gum disease begin. Floss or an interdental brush once a day does more for your teeth "
     "than upgrading your toothbrush ever will."),
    ("Do not rinse straight after brushing",
     "Rinsing with water washes away the fluoride your toothpaste just deposited. Spit, and leave it. "
     "It is the single easiest improvement most people can make to their routine."),
    ("Bleeding gums are a signal, not a normal event",
     "Healthy gums do not bleed when brushed, any more than a healthy scalp bleeds when combed. "
     "Bleeding means inflammation &mdash; and at the early stage it is completely reversible with a "
     "cleaning and better technique. Ignored, it becomes bone loss that does not come back."),
    ("Sugar frequency matters more than sugar quantity",
     "One dessert does less damage than sipping a sweet drink over three hours. Every exposure starts "
     "an acid attack lasting roughly 20 minutes. Keep sugar to mealtimes and let your teeth recover in "
     "between."),
    ("Sensitivity is worth mentioning early",
     "A twinge at cold air or sweet food can mean a cavity, a crack, receding gums or worn enamel &mdash; "
     "all of which are simpler and cheaper to treat early. Sensitive toothpaste masks the symptom; it "
     "does not fix the cause."),
    ("A cracked tooth will not heal itself",
     "Enamel is not bone &mdash; it cannot repair. A small chip is a filling; the same tooth left for a year "
     "becomes a crown or a root canal. Get it looked at while it is still the cheap version."),
    ("Six-monthly check-ups are the cheapest dentistry there is",
     "The point of a check-up is not the check-up. It is catching a cavity while it still needs a "
     "20-minute filling instead of a root canal and a crown. Almost every expensive treatment we do "
     "started as something small that nobody looked at."),
]


# --------------------------------------------------------------------------- #

def reviews(services):
    cards = "".join(f"""        <article class="quote-card" data-reveal data-reveal-delay="{i % 3 * 80}">
          <p class="stars" aria-label="Rated 5 out of 5">{STARS}</p>
          <blockquote>{text}</blockquote>
          <div class="quote-who">
            <span class="avatar" aria-hidden="true">{initials}</span>
            <span><strong>{name}</strong><span>Google review</span></span>
          </div>
        </article>
""" for i, (name, initials, text) in enumerate(REVIEWS))

    body = banner(
        "Patient Reviews",
        f"Rated {CLINIC['rating']} out of 5 by {CLINIC['reviews']}+ patients on Google.",
        [("Reviews", None)],
        "images/happy-patient.jpg",
    ) + f"""  <section class="section">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="kicker">In our patients' words</span>
        <h2 class="h-lg">{CLINIC['reviews']}+ reviews, and an average of {CLINIC['rating']}</h2>
        <p>These are reviews left by patients on Google, reproduced as written apart from trimming for
        length.</p>
      </div>
      <div class="service-grid">
{cards}      </div>
      <div style="text-align:center;margin-top:52px" data-reveal>
        <a class="btn btn-ink" href="https://www.google.com/maps/search/?api=1&amp;query={CLINIC['maps_query']}" target="_blank" rel="noopener">See our Google listing</a>
      </div>
    </div>
  </section>

  <section class="section-sm bg-ink">
    <div class="container">
      <div class="counter-row" data-reveal>
        <div class="counter-cell"><strong data-count="5.0">5.0</strong><span>Average rating</span></div>
        <div class="counter-cell"><strong data-count="158" data-suffix="+">158+</strong><span>Total reviews</span></div>
        <div class="counter-cell"><strong data-count="157">157</strong><span>Five-star reviews</span></div>
        <div class="counter-cell"><strong data-count="6">6</strong><span>Days open weekly</span></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container" style="text-align:center">
      <span class="kicker" style="justify-content:center" data-reveal>Been treated here?</span>
      <h2 class="h-lg" style="margin-inline:auto;max-width:680px" data-reveal>A review helps the next
      nervous patient decide</h2>
      <p style="margin:18px auto 32px;max-width:560px" data-reveal>If your treatment went well, saying so
      publicly is the kindest thing you can do for someone sitting at home putting off a phone call.</p>
      <div class="hero-actions" style="justify-content:center" data-reveal>
        <a class="btn" href="https://www.google.com/maps/search/?api=1&amp;query={CLINIC['maps_query']}" target="_blank" rel="noopener">Leave a Google review</a>
        <a class="btn btn-outline" href="appointment.html">Book an appointment</a>
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


# --------------------------------------------------------------------------- #

def contact(services):
    body = banner(
        "Contact Samarth Dental Clinic",
        "Vavol, Gandhinagar &mdash; call, WhatsApp or simply walk in during clinic hours.",
        [("Contact", None)],
        "images/reception.jpg",
    ) + f"""  <section class="section">
    <div class="container">
      <div class="info-strip-grid" data-reveal>
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
            <h3>Clinic address</h3>
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
      <div data-reveal>
        <div class="section-head">
          <span class="kicker">Send us a message</span>
          <h2 class="h-lg">Tell us what is troubling you</h2>
          <p>Fill this in and it opens WhatsApp with your message ready to send, so we can reply
          quickly. Prefer to talk? Just call the clinic.</p>
        </div>
        <div class="form-card">
          <form data-form data-form-title="Website enquiry — Samarth Dental Clinic" novalidate>
            <div class="form-alert">
              <span>{icon('smile', 20)}</span>
              <span>Thank you &mdash; your message has been prepared in WhatsApp. If it did not open, please
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
                <label for="c-subject">What is it about?</label>
                <select id="c-subject" name="Subject">
                  <option>General enquiry</option>
                  <option>Toothache or emergency</option>
                  <option>Cost of a treatment</option>
                  <option>Second opinion</option>
                  <option>Appointment timing</option>
                </select>
              </div>
              <div class="field full">
                <label for="c-message">Your message <span class="req">*</span></label>
                <textarea id="c-message" name="Message" placeholder="Describe the problem, how long it has been going on, and anything you have already been told." required></textarea>
              </div>
            </div>
            <p class="form-note">We use your details only to reply to this enquiry.</p>
            <div style="margin-top:24px">
              <button class="btn" type="submit">{icon('chat', 18)} Send via WhatsApp</button>
            </div>
          </form>
        </div>
      </div>

      <aside class="side-stack" data-reveal data-reveal-delay="120">
        <div class="side-card contrast">
          <h3>Call the clinic</h3>
          <p>Fastest way to get an appointment confirmed.</p>
          <a class="phone" href="tel:{CLINIC['phone_link']}">{CLINIC['phone_display']}</a>
          <a class="btn btn-gold btn-block" href="https://wa.me/{CLINIC['whatsapp']}" target="_blank" rel="noopener">Chat on WhatsApp</a>
        </div>
        <div class="side-card">
          <h3>Clinic hours</h3>
          {hours_block()}
        </div>
        <div class="side-card">
          <h3>Getting here</h3>
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
      <div class="map-frame" data-reveal>
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


# --------------------------------------------------------------------------- #

def appointment(services):
    options = "".join(
        f'<option>{s["name"].replace("&amp;", "and")}</option>' for s in services
    )
    body = banner(
        "Book an Appointment",
        "Monday to Saturday, mornings and evenings. Most requests are confirmed the same day.",
        [("Book Appointment", None)],
        "images/consultation.jpg",
    ) + f"""  <section class="section">
    <div class="container with-side">
      <div data-reveal>
        <div class="section-head">
          <span class="kicker">Request a slot</span>
          <h2 class="h-lg">Pick a day and we will confirm the time</h2>
          <p>Submitting this opens WhatsApp with your request written out, so all you do is press send.
          We reply with a confirmed time &mdash; usually within clinic hours the same day.</p>
        </div>
        <div class="form-card">
          <form data-form data-form-title="Appointment request — Samarth Dental Clinic" novalidate>
            <div class="form-alert">
              <span>{icon('calendar', 20)}</span>
              <span>Your appointment request is ready in WhatsApp. If it did not open, call us on
              {CLINIC['phone_display']} and we will book you in.</span>
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
                <textarea id="a-notes" name="Notes" placeholder="Describe your symptoms, any medical conditions or medication, and whether you are nervous about treatment — it genuinely helps us prepare."></textarea>
              </div>
            </div>
            <p class="form-note">Sunday is a clinic holiday, so please choose Monday to Saturday.
            Emergencies are fitted in outside the listed slots wherever possible.</p>
            <div style="margin-top:24px">
              <button class="btn" type="submit">{icon('calendar', 18)} Send appointment request</button>
            </div>
          </form>
        </div>
      </div>

      <aside class="side-stack" data-reveal data-reveal-delay="120">
        <div class="side-card contrast">
          <h3>Rather just call?</h3>
          <p>Ring the clinic and we will book you in there and then.</p>
          <a class="phone" href="tel:{CLINIC['phone_link']}">{CLINIC['phone_display']}</a>
          <a class="btn btn-gold btn-block" href="https://wa.me/{CLINIC['whatsapp']}" target="_blank" rel="noopener">Chat on WhatsApp</a>
        </div>
        <div class="side-card">
          <h3>Clinic hours</h3>
          {hours_block()}
        </div>
        <div class="side-card">
          <h3>Bring with you</h3>
          <ul class="ticks" style="gap:11px">
            <li>Any previous X-rays or dental reports</li>
            <li>A list of medicines you take</li>
            <li>Details of medical conditions such as diabetes</li>
            <li>Your questions &mdash; written down if it helps</li>
          </ul>
        </div>
        <div class="side-card">
          <h3>Payments accepted</h3>
          <p style="font-size:15px">Cash, UPI, cards and NFC mobile payments. You will have the cost of
          your treatment in writing before it starts.</p>
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


# --------------------------------------------------------------------------- #

def faq(services):
    items = "".join(f"""        <div class="ac-item{' open' if i == 0 else ''}">
          <button class="ac-head" type="button" aria-expanded="{'true' if i == 0 else 'false'}">
            <span>{q}</span><span class="ac-sign" aria-hidden="true"></span>
          </button>
          <div class="ac-panel"><div><p>{a}</p></div></div>
        </div>
""" for i, (q, a) in enumerate(FAQS))

    body = banner(
        "Frequently Asked Questions",
        "Costs, timings, pain, sterilisation and everything else patients ask before booking.",
        [("FAQs", None)],
        "images/treatment-plan.jpg",
    ) + f"""  <section class="section">
    <div class="container with-side">
      <div data-reveal>
        <div class="section-head">
          <span class="kicker">Before you book</span>
          <h2 class="h-lg">Questions we are asked most</h2>
        </div>
        <div class="accordion">
{items}        </div>
        <div class="callout" style="margin-top:36px">
          <p><strong>Still unsure about something?</strong> Call
          <a href="tel:{CLINIC['phone_link']}">{CLINIC['phone_display']}</a> and ask. We would much
          rather answer a question on the phone than have you put off a visit.</p>
        </div>
      </div>
      <aside class="side-stack" data-reveal data-reveal-delay="120">
        <div class="side-card contrast">
          <h3>Ask us directly</h3>
          <p>Call or WhatsApp during clinic hours.</p>
          <a class="phone" href="tel:{CLINIC['phone_link']}">{CLINIC['phone_display']}</a>
          <a class="btn btn-gold btn-block" href="contact.html">Send a message</a>
        </div>
        <div class="side-card">
          <h3>Clinic hours</h3>
          {hours_block()}
        </div>
        <div class="side-card">
          <h3>Popular treatments</h3>
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


# --------------------------------------------------------------------------- #

def dental_tips(services):
    cards = "".join(f"""        <article class="feature-card" data-reveal data-reveal-delay="{i % 3 * 80}">
          <span class="feature-icon">{icon('tooth', 26)}</span>
          <h3>{title}</h3>
          <p>{text}</p>
        </article>
""" for i, (title, text) in enumerate(TIPS))

    body = banner(
        "Dental Care Tips",
        "Practical advice we find ourselves repeating in the chair most days.",
        [("Dental Tips", None)],
        "images/oral-care.jpg",
    ) + f"""  <section class="section">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="kicker">Look after them at home</span>
        <h2 class="h-lg">Eight things that genuinely make a difference</h2>
        <p>None of this replaces a check-up, but it is the advice that saves our patients the most money
        over a lifetime.</p>
      </div>
      <div class="feature-grid">
{cards}      </div>
      <div class="callout" style="margin-top:52px" data-reveal>
        <p><strong>One caveat.</strong> General advice cannot diagnose your mouth. If something hurts,
        bleeds, feels loose or has changed, have it looked at rather than managed with a different
        toothpaste &mdash; call <a href="tel:{CLINIC['phone_link']}">{CLINIC['phone_display']}</a>.</p>
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


# --------------------------------------------------------------------------- #

def not_found(services):
    body = banner(
        "Page not found",
        "The page you were looking for has moved or no longer exists.",
        [("404", None)],
        "images/clinic-interior.jpg",
    ) + f"""  <section class="section">
    <div class="container" style="text-align:center">
      <span class="kicker" style="justify-content:center" data-reveal>Error 404</span>
      <h2 class="h-lg" style="margin-inline:auto;max-width:640px" data-reveal>Let us get you back on
      track</h2>
      <p style="margin:18px auto 34px;max-width:520px" data-reveal>Try our list of treatments, or simply
      call the clinic on {CLINIC['phone_display']} and we will help.</p>
      <div class="hero-actions" style="justify-content:center" data-reveal>
        <a class="btn" href="index.html">Back to home</a>
        <a class="btn btn-outline" href="services.html">All treatments</a>
      </div>
    </div>
  </section>
"""
    return "Page not found | " + CLINIC["name"], "Page not found.", body, None
