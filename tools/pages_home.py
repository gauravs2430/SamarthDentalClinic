"""Homepage body."""

from chrome import STARS, icon, hours_block
from data_clinic import CLINIC, REVIEWS, FAQS

WHY = [
    ("smile", "Painless treatment",
     "Local anaesthesia is used for fillings, root canals, extractions and implants."),
    ("shield", "Clean and sterilised",
     "Instruments are autoclaved after every patient. Needles and gloves are single-use."),
    ("wallet", "Cost told in advance",
     "You receive a written plan with the cost of each step before treatment begins."),
    ("tooth", "All treatments here",
     "Implants, root canal, braces, cleaning, fillings and kids dentistry in one clinic."),
]

STEPS = [
    ("Check-up", "We examine your teeth and take a digital X-ray if needed."),
    ("Treatment plan", "We explain the problem, the options and the cost."),
    ("Treatment", "Treatment is done under local anaesthesia, at a comfortable pace."),
    ("Follow-up", "You get after-care advice and a review visit if required."),
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
    for s in services[:6]:
        out.append(f"""        <article class="service-card">
          <div class="service-thumb">
            <img src="{s['img']}" alt="{s['name'].replace('&amp;', 'and')} at Samarth Dental Clinic" loading="lazy">
          </div>
          <div class="service-body">
            <h3>{s['name']}</h3>
            <p>{s['card']}</p>
            <a class="link-arrow" href="{s['slug']}.html">Read More</a>
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
        <h1>Welcome to Samarth Dental Clinic</h1>
        <p class="hero-text">Dental clinic in Vavol, Gandhinagar. We provide implants, root canal,
        braces, cleaning, fillings, kids dentistry and other treatments under one roof.</p>
        <div class="hero-actions">
          <a class="btn" href="appointment.html">{icon('calendar', 18)} Book Appointment</a>
          <a class="btn btn-outline" href="tel:{CLINIC['phone_link']}">{icon('phone', 18)} {CLINIC['phone_display']}</a>
        </div>
        <div class="hero-proof">
          <div><strong>{CLINIC['rating']}</strong><span>Google rating</span></div>
          <div><strong>{CLINIC['reviews']}+</strong><span>Patient reviews</span></div>
          <div><strong>Mon&ndash;Sat</strong><span>10&ndash;1 &amp; 4&ndash;7</span></div>
        </div>
      </div>
      <div class="hero-media">
        <img src="images/hero-main.jpg" alt="A patient smiling after dental treatment at Samarth Dental Clinic" width="1000" height="700">
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
      <div class="split-media">
        <img src="images/clinic-interior.jpg" alt="Inside the treatment room at Samarth Dental Clinic, Vavol" loading="lazy">
      </div>
      <div class="split-body">
        <h2>Welcome to Our Clinic</h2>
        <p>Samarth Dental Clinic is a dental clinic in Vavol, Gandhinagar, run by {CLINIC['doctor']}.
        We treat the whole family &mdash; from a child&rsquo;s first check-up to implants, root canal,
        braces and dentures.</p>
        <p>The clinic is at Shop No. S09, ShantiNagar Shopping, near Hotel Leela. We are open Monday
        to Saturday, 10:00 AM to 1:00 PM and 4:00 PM to 7:00 PM.</p>
        <ul class="ticks two">
          <li>Appointments by phone or WhatsApp</li>
          <li>Digital X-rays in the clinic</li>
          <li>Written treatment cost before we start</li>
          <li>UPI, cards and cash accepted</li>
        </ul>
        <a class="btn" href="about.html">About the Clinic</a>
      </div>
    </div>
  </section>

  <section class="section bg-sky">
    <div class="container">
      <div class="section-head center">
        <h2>Our Services</h2>
        <p>Common dental treatments available at the clinic.</p>
      </div>
      <div class="service-grid">
{_service_cards(services)}
      </div>
      <div class="block-cta">
        <a class="btn btn-ink" href="services.html">View All Services</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head center">
        <h2>Why Choose Us</h2>
      </div>
      <div class="feature-grid four">
{"".join(f'''        <article class="feature-card">
          <span class="feature-icon">{icon(ico, 26)}</span>
          <h3>{title}</h3>
          <p>{text}</p>
        </article>
''' for ico, title, text in WHY)}      </div>
    </div>
  </section>

  <section class="section bg-sky">
    <div class="container">
      <div class="section-head center">
        <h2>How Treatment Works</h2>
      </div>
      <div class="steps">
{"".join(f'''        <article class="step">
          <h3>{title}</h3>
          <p>{text}</p>
        </article>
''' for title, text in STEPS)}      </div>
    </div>
  </section>

  <section class="section">
    <div class="container split media-right">
      <div class="split-media doctor-media">
        <img src="images/doctor-dhvani.jpg" alt="{CLINIC['doctor']}, dental surgeon and founder of Samarth Dental Clinic" loading="lazy">
      </div>
      <div class="split-body">
        <h2>{CLINIC['doctor']}</h2>
        <p class="doctor-role">Dental Surgeon &amp; Founder</p>
        <p>{CLINIC['doctor']} is the dentist at Samarth Dental Clinic. She treats implants, root canals,
        braces, crowns, gum problems and children&rsquo;s teeth.</p>
        <p>Patients often mention that treatment is explained clearly and that procedures are done
        gently under proper anaesthesia.</p>
        <div class="hero-actions">
          <a class="btn" href="doctor.html">Doctor Profile</a>
          <a class="btn btn-outline" href="appointment.html">Book Appointment</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section bg-sky">
    <div class="container">
      <div class="section-head center">
        <h2>Clinic Gallery</h2>
      </div>
      <div class="gallery-grid">
{"".join(f'''        <a class="gallery-item" href="{src}" data-lightbox="{src}">
          <img src="{src}" alt="{alt}" loading="lazy">
        </a>
''' for src, alt in GALLERY)}      </div>
      <div class="block-cta">
        <a class="btn btn-outline" href="gallery.html">View Gallery</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head center">
        <h2>Patient Reviews</h2>
        <p>{CLINIC['reviews']}+ Google reviews. Rated {CLINIC['rating']} out of 5.</p>
      </div>
      <div class="slider" data-slider>
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

  <section class="section bg-sky">
    <div class="container with-side">
      <div>
        <div class="section-head">
          <h2>Frequently Asked Questions</h2>
        </div>
        <div class="accordion">
{_faq_items()}
        </div>
        <p class="block-cta-left"><a class="link-arrow" href="faq.html">More questions</a></p>
      </div>
      <div class="side-stack">
        <div class="side-card">
          <h3>Clinic Hours</h3>
          {hours_block()}
        </div>
        <div class="side-card contrast">
          <h3>Dental emergency?</h3>
          <p>Toothache, swelling or a broken tooth &mdash; call and we will try to see you the same day.</p>
          <a class="phone" href="tel:{CLINIC['phone_link']}">{CLINIC['phone_display']}</a>
          <a class="btn btn-block" href="https://wa.me/{CLINIC['whatsapp']}" target="_blank" rel="noopener">WhatsApp Us</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section-sm">
    <div class="container">
      <div class="map-frame">
        <iframe title="Map to Samarth Dental Clinic, Vavol, Gandhinagar" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
          src="https://maps.google.com/maps?q={CLINIC['maps_query']}&amp;t=&amp;z=16&amp;ie=UTF8&amp;iwloc=&amp;output=embed"></iframe>
      </div>
    </div>
  </section>
"""
