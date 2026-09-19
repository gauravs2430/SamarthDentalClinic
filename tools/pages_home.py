"""Homepage body."""

from chrome import STARS, icon, hours_block
from data_clinic import CLINIC, REVIEWS, FAQS

WHY = [
    ("smile", "Genuinely painless",
     "Effective local anaesthesia, unhurried appointments and a warning before anything happens. "
     "Nervous patients are our speciality, not our problem."),
    ("shield", "Sterilised, every time",
     "Instruments are pouched and autoclaved after each patient. Needles, gloves and suction tips "
     "are single-use and opened in front of you."),
    ("wallet", "Costs agreed upfront",
     "You get a written plan with the price of each step before treatment starts. Where options "
     "exist, we explain the difference and let you choose."),
    ("tooth", "Everything under one roof",
     "Implants, root canals, braces, surgery and children's dentistry in one place &mdash; so you are "
     "not sent across town mid-treatment."),
    ("users", "A woman dentist, family-friendly",
     f"{CLINIC['doctor']} treats grandparents and toddlers in the same afternoon. Parents are "
     "welcome to stay beside the chair throughout."),
    ("star", "Rated 5.0 by real patients",
     f"{CLINIC['reviews']}+ Google reviews, and almost every one of them mentions the same two "
     "things: gentle hands and clear explanations."),
]

STEPS = [
    ("Consultation", "You tell us what is wrong. We examine, take a digital X-ray where it is "
     "needed, and actually listen before reaching for anything."),
    ("Diagnosis &amp; plan", "You get the findings in plain language and a written plan with the cost "
     "of each stage &mdash; including the option of doing nothing yet."),
    ("Treatment", "Carried out under proper anaesthesia at a pace that suits you, with a pause "
     "whenever you raise a hand."),
    ("Follow-up", "Written aftercare, a number you can call, and a review appointment to confirm "
     "everything has healed as it should."),
]

TECH = [
    ("scan", "Digital X-rays", "Lower radiation than film, and the image is on screen instantly so "
     "you can see what we are seeing."),
    ("clipboard", "Written treatment plans", "Every stage costed in writing before work starts, so "
     "nothing on the final bill is a surprise."),
    ("shield", "Autoclave sterilisation", "A full sterilisation cycle between patients, with "
     "single-use disposables for everything else."),
    ("wallet", "UPI, cards &amp; NFC", "Pay however is easiest &mdash; contactless mobile payments, cards, "
     "UPI or cash."),
]

GALLERY = [
    ("images/clinic-interior.jpg", "Treatment room at Samarth Dental Clinic, Vavol"),
    ("images/operatory.jpg", "Dental operatory with modern chair and overhead light"),
    ("images/reception.jpg", "Clinic reception and waiting area"),
    ("images/dental-chair.jpg", "Dental chair prepared for the next patient"),
    ("images/digital-scanner.jpg", "Digital intraoral scanning in progress"),
    ("images/xray-review.jpg", "Reviewing digital dental X-rays"),
    ("images/oral-care.jpg", "Oral hygiene and home-care guidance"),
    ("images/happy-patient.jpg", "A patient after completing treatment"),
]


def _service_cards(services):
    out = []
    for i, s in enumerate(services[:6], start=1):
        out.append(f"""        <article class="service-card" data-reveal data-reveal-delay="{(i - 1) % 3 * 90}">
          <div class="service-thumb">
            <span class="service-num">{i:02d}</span>
            <img src="{s['img']}" alt="{s['name'].replace('&amp;', 'and')} at Samarth Dental Clinic" loading="lazy">
          </div>
          <div class="service-body">
            <h3>{s['name']}</h3>
            <p>{s['card']}</p>
            <a class="link-arrow" href="{s['slug']}.html">Learn more</a>
          </div>
        </article>""")
    return "\n".join(out)


def _quote_slides():
    out = []
    for name, initials, text in REVIEWS:
        out.append(f"""          <div class="slide">
            <article class="quote-card">
              <p class="stars" aria-label="Rated 5 out of 5">{STARS}</p>
              <blockquote>{text}</blockquote>
              <div class="quote-who">
                <span class="avatar" aria-hidden="true">{initials}</span>
                <span><strong>{name}</strong><span>Google review</span></span>
              </div>
            </article>
          </div>""")
    return "\n".join(out)


def _faq_items(limit=6):
    out = []
    for i, (q, a) in enumerate(FAQS[:limit]):
        out.append(f"""        <div class="ac-item{' open' if i == 0 else ''}">
          <button class="ac-head" type="button" aria-expanded="{'true' if i == 0 else 'false'}">
            <span>{q}</span><span class="ac-sign" aria-hidden="true"></span>
          </button>
          <div class="ac-panel"><div><p>{a}</p></div></div>
        </div>""")
    return "\n".join(out)


def build(services):
    return f"""  <section class="hero">
    <div class="container hero-grid">
      <div>
        <span class="hero-badge" data-reveal><span class="dot"></span>Rated {CLINIC['rating']} by {CLINIC['reviews']}+ patients</span>
        <h1 data-reveal data-reveal-delay="80">Exceptional dental care for <em>every stage</em> of your smile</h1>
        <p class="hero-text" data-reveal data-reveal-delay="160">Implants, root canals, braces and everyday
        dentistry under one roof in Vavol, Gandhinagar &mdash; explained before it begins, and priced before
        you agree to it.</p>
        <div class="hero-actions" data-reveal data-reveal-delay="240">
          <a class="btn" href="appointment.html">{icon('calendar', 18)} Book an Appointment</a>
          <a class="btn btn-outline" href="tel:{CLINIC['phone_link']}">{icon('phone', 18)} {CLINIC['phone_display']}</a>
        </div>
        <div class="hero-proof" data-reveal data-reveal-delay="320">
          <div><strong data-count="5.0">5.0</strong><span>Google rating</span></div>
          <div><strong data-count="158" data-suffix="+">158+</strong><span>Patient reviews</span></div>
          <div><strong data-count="12" data-suffix="+">12+</strong><span>Treatments offered</span></div>
        </div>
      </div>
      <div class="hero-media" data-reveal data-reveal-delay="120">
        <img src="images/hero-main.jpg" alt="A patient smiling after dental treatment at Samarth Dental Clinic" width="1000" height="700">
        <div class="hero-chip">
          <p class="stars" aria-hidden="true">{STARS}</p>
          <strong>{CLINIC['rating']} / 5</strong>
          <span>{CLINIC['reviews']}+ verified Google reviews</span>
        </div>
      </div>
    </div>
  </section>

  <section class="info-strip">
    <div class="container">
      <div class="info-strip-grid">
        <div class="info-tile">
          <span class="info-tile-icon">{icon('phone', 22)}</span>
          <div>
            <h3>Need a dentist?</h3>
            <p><a href="tel:{CLINIC['phone_link']}">{CLINIC['phone_display']}</a></p>
          </div>
        </div>
        <div class="info-tile">
          <span class="info-tile-icon">{icon('clock', 22)}</span>
          <div>
            <h3>Opening hours</h3>
            <p>Mon&ndash;Sat: 10 AM &ndash; 1 PM<br>&amp; 4 PM &ndash; 7 PM &middot; Sun closed</p>
          </div>
        </div>
        <div class="info-tile">
          <span class="info-tile-icon">{icon('pin', 22)}</span>
          <div>
            <h3>Visit the clinic</h3>
            <p><a href="https://www.google.com/maps/search/?api=1&amp;query={CLINIC['maps_query']}" target="_blank" rel="noopener">{CLINIC['street']}, {CLINIC['area']} {CLINIC['pin']}</a></p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container split">
      <div class="split-media media-stack" data-reveal>
        <img src="images/clinic-interior.jpg" alt="Inside the treatment room at Samarth Dental Clinic, Vavol" loading="lazy">
        <div class="stat-card"><strong>{CLINIC['rating']}</strong><span>Google rated</span></div>
      </div>
      <div class="split-body" data-reveal data-reveal-delay="120">
        <span class="kicker">About the clinic</span>
        <h2 class="h-lg">Where careful dentistry meets a calm chair</h2>
        <p class="lead">Samarth Dental Clinic was started by {CLINIC['doctor']} with one aim: to put every
        dental treatment a family needs under a single roof, done properly.</p>
        <p>That means you are not referred elsewhere halfway through a case. A root canal, the crown that
        follows it, the implant on the other side and your child's six-monthly check-up all happen in the
        same chair, with the same dentist who already knows your mouth.</p>
        <p>The clinic is equipped for digital X-rays, surgical work and cosmetic dentistry, and run to a
        simple rule &mdash; you should understand what is being done to your teeth, and what it costs, before
        it starts.</p>
        <ul class="ticks two">
          <li>Appointment-based, so you are seen on time</li>
          <li>Instruments autoclaved after every patient</li>
          <li>Written plans with upfront costs</li>
          <li>Open six days a week, mornings and evenings</li>
        </ul>
        <a class="btn" href="about.html">More about us</a>
      </div>
    </div>
  </section>

  <section class="section bg-sky">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="kicker">Our treatments</span>
        <h2 class="h-lg">Dentistry for the whole family, in one place</h2>
        <p>From a six-monthly cleaning to a full-arch implant case &mdash; here is what we do most often.</p>
      </div>
      <div class="service-grid">
{_service_cards(services)}
      </div>
      <div style="text-align:center;margin-top:52px" data-reveal>
        <a class="btn btn-ink" href="services.html">View all {len(services)} treatments</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="kicker">Why patients choose us</span>
        <h2 class="h-lg">Careful hands, clear answers, no surprises</h2>
      </div>
      <div class="feature-grid">
{"".join(f'''        <article class="feature-card" data-reveal data-reveal-delay="{i % 3 * 90}">
          <span class="feature-icon">{icon(ico, 26)}</span>
          <h3>{title}</h3>
          <p>{text}</p>
        </article>
''' for i, (ico, title, text) in enumerate(WHY))}      </div>
    </div>
  </section>

  <section class="section-sm bg-ink">
    <div class="container">
      <div class="counter-row" data-reveal>
        <div class="counter-cell"><strong data-count="5.0">5.0</strong><span>Google rating</span></div>
        <div class="counter-cell"><strong data-count="158" data-suffix="+">158+</strong><span>Patient reviews</span></div>
        <div class="counter-cell"><strong data-count="12" data-suffix="+">12+</strong><span>Treatments offered</span></div>
        <div class="counter-cell"><strong data-count="6">6</strong><span>Days open weekly</span></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="kicker">How a visit works</span>
        <h2 class="h-lg">Four steps, and you always know the next one</h2>
      </div>
      <div class="steps">
{"".join(f'''        <article class="step" data-reveal data-reveal-delay="{i * 90}">
          <h3>{title}</h3>
          <p>{text}</p>
        </article>
''' for i, (title, text) in enumerate(STEPS))}      </div>
    </div>
  </section>

  <section class="section bg-cream">
    <div class="container split media-right">
      <div class="split-media doctor-media" data-reveal>
        <img src="images/doctor-dhvani.jpg" alt="{CLINIC['doctor']}, dental surgeon and founder of Samarth Dental Clinic" loading="lazy">
        <div class="badge-card"><strong>{CLINIC['rating']} / 5</strong><span>from {CLINIC['reviews']}+ patients</span></div>
      </div>
      <div class="split-body" data-reveal data-reveal-delay="120">
        <span class="kicker">Meet your dentist</span>
        <h2 class="h-lg">{CLINIC['doctor']}</h2>
        <p class="doctor-role">Dental Surgeon &amp; Founder</p>
        <p>{CLINIC['doctor']} is an experienced dental surgeon who set up Samarth Dental Clinic to
        practise the way she thought dentistry should be practised &mdash; unhurried, explained, and priced
        honestly.</p>
        <p>Read her patient reviews and the same words keep coming back: polite, patient, professional,
        painless. Several mention arriving anxious about a root canal and leaving having barely felt it.
        That is largely down to how much time she spends explaining a procedure before starting it.</p>
        <p>Her day covers the full range &mdash; implants and surgical extractions, root canals and crowns,
        braces, cosmetic work and children's first check-ups.</p>
        <div class="hero-actions">
          <a class="btn" href="doctor.html">Read her profile</a>
          <a class="btn btn-outline" href="appointment.html">Book with her</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="kicker">What we provide</span>
        <h2 class="h-lg">Equipped for the job, run to a standard</h2>
        <p>None of this is exotic &mdash; it is simply what a clinic needs to diagnose accurately and treat
        safely, used consistently on every patient.</p>
      </div>
      <div class="mini-grid" data-reveal>
{"".join(f'''        <article class="mini-tile">
          <span class="mini-icon">{icon(ico, 24)}</span>
          <h3>{title}</h3>
          <p>{text}</p>
        </article>
''' for ico, title, text in TECH)}      </div>
    </div>
  </section>

  <section class="section bg-sky">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="kicker">Inside the clinic</span>
        <h2 class="h-lg">Have a look before you arrive</h2>
      </div>
      <div class="gallery-grid" data-reveal>
{"".join(f'''        <a class="gallery-item" href="{src}" data-lightbox="{src}">
          <img src="{src}" alt="{alt}" loading="lazy">
        </a>
''' for src, alt in GALLERY)}      </div>
      <div style="text-align:center;margin-top:44px" data-reveal>
        <a class="btn btn-outline" href="gallery.html">See the full gallery</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="kicker">Patient reviews</span>
        <h2 class="h-lg">{CLINIC['reviews']}+ reviews, {CLINIC['rating']} out of 5</h2>
        <p>Unedited reviews left by patients on Google.</p>
      </div>
      <div class="slider" data-slider data-reveal>
        <div class="slider-viewport">
          <div class="slider-track">
{_quote_slides()}
          </div>
        </div>
        <div class="slider-nav">
          <button class="slider-btn" type="button" data-slider-prev aria-label="Previous reviews">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 5l-7 7 7 7"/></svg>
          </button>
          <button class="slider-btn" type="button" data-slider-next aria-label="More reviews">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 5l7 7-7 7"/></svg>
          </button>
        </div>
      </div>
    </div>
  </section>

  <section class="section bg-cream">
    <div class="container with-side">
      <div>
        <div class="section-head" data-reveal>
          <span class="kicker">Common questions</span>
          <h2 class="h-lg">Things patients ask before booking</h2>
        </div>
        <div class="accordion" data-reveal>
{_faq_items()}
        </div>
        <p style="margin-top:32px"><a class="link-arrow" href="faq.html">All frequently asked questions</a></p>
      </div>
      <div class="side-stack" data-reveal data-reveal-delay="120">
        <div class="side-card">
          <h3>Clinic hours</h3>
          {hours_block()}
        </div>
        <div class="side-card contrast">
          <h3>Have a dental emergency?</h3>
          <p>Toothache, swelling or a broken tooth &mdash; call and we will fit you in.</p>
          <a class="phone" href="tel:{CLINIC['phone_link']}">{CLINIC['phone_display']}</a>
          <a class="btn btn-gold btn-block" href="https://wa.me/{CLINIC['whatsapp']}" target="_blank" rel="noopener">WhatsApp us</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section-sm">
    <div class="container">
      <div class="map-frame" data-reveal>
        <iframe title="Map to Samarth Dental Clinic, Vavol, Gandhinagar" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
          src="https://maps.google.com/maps?q={CLINIC['maps_query']}&amp;t=&amp;z=16&amp;ie=UTF8&amp;iwloc=&amp;output=embed"></iframe>
      </div>
    </div>
  </section>
"""
