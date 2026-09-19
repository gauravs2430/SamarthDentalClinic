"""About, Doctor, Services index and Gallery pages."""

from chrome import STARS, banner, hours_block, icon
from data_clinic import CLINIC
from pages_home import TECH, WHY

GALLERY_ALL = [
    ("images/clinic-interior.jpg", "Treatment room at Samarth Dental Clinic, Vavol", "wide"),
    ("images/operatory.jpg", "Dental operatory with modern chair and overhead light", ""),
    ("images/reception.jpg", "Reception and waiting area", ""),
    ("images/dental-chair.jpg", "Dental chair prepared for the next patient", ""),
    ("images/clinic-room.jpg", "Second treatment room with monitor for digital records", ""),
    ("images/clinic-office.jpg", "Bright, clean clinic interior", "wide"),
    ("images/clinic-chair.jpg", "Treatment chair and instrument tray in daylight", ""),
    ("images/digital-scanner.jpg", "Digital intraoral scanning in progress", ""),
    ("images/xray-review.jpg", "Reviewing digital dental X-rays", ""),
    ("images/digital-scan.jpg", "A digital scan of a patient's teeth on screen", ""),
    ("images/dental-xray.jpg", "Digital dental X-ray examination", ""),
    ("images/examining.jpg", "Examination under the overhead light", ""),
    ("images/clear-aligners.jpg", "Clear aligners and their storage case", ""),
    ("images/sterile-surgery.jpg", "Sterile instruments laid out before a procedure", ""),
    ("images/oral-surgery.jpg", "Surgical extraction carried out under local anaesthesia", ""),
    ("images/treatment-plan.jpg", "Explaining a treatment plan to a patient", "wide"),
    ("images/consultation.jpg", "Consultation with a model used to explain treatment", ""),
    ("images/kids-dentistry.jpg", "A child's dental check-up", ""),
    ("images/kids-checkup.jpg", "A young patient having his teeth checked", ""),
    ("images/happy-kid.jpg", "A child leaving the clinic happy", ""),
    ("images/oral-care.jpg", "Home oral-care guidance for patients", ""),
    ("images/smile-closeup.jpg", "Close-up of a finished cosmetic dental result", ""),
    ("images/happy-patient.jpg", "A patient after completing treatment", ""),
    ("images/patient-male.jpg", "A patient during a routine check-up", ""),
]


# --------------------------------------------------------------------------- #

def about(services):
    body = banner(
        "About Samarth Dental Clinic",
        "A single-roof dental practice in Vavol, Gandhinagar, founded by "
        + CLINIC["doctor"] + ".",
        [("About Us", None)],
        "images/clinic-interior.jpg",
    ) + f"""  <section class="section">
    <div class="container split">
      <div class="split-media media-stack" data-reveal>
        <img src="images/operatory.jpg" alt="Treatment room at Samarth Dental Clinic, Vavol" loading="lazy">
        <div class="stat-card"><strong>{CLINIC['rating']}</strong><span>Google rated</span></div>
      </div>
      <div class="split-body" data-reveal data-reveal-delay="120">
        <span class="kicker">Who we are</span>
        <h2 class="h-lg">One clinic, one dentist, every treatment your family needs</h2>
        <p class="lead">Samarth Dental Clinic was started by {CLINIC['doctor']} with a straightforward
        ambition &mdash; to provide the best possible dental treatment under one roof.</p>
        <p>In practice that ambition shows up as something quite ordinary but surprisingly rare: you are
        not passed around. The dentist who diagnoses your problem is the one who treats it, and she
        remembers your mouth next time you come in. A root canal and the crown that follows it, an
        implant on the other side, your child's check-up and your father's denture all happen here.</p>
        <p>The clinic sits in ShantiNagar Shopping in Vavol, close to Hotel Leela, and is equipped for
        digital X-rays, surgical work, orthodontics and cosmetic dentistry. It is open six days a week,
        mornings and evenings, so appointments fit around work rather than the other way round.</p>
      </div>
    </div>
  </section>

  <section class="section bg-sky">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="kicker">How we work</span>
        <h2 class="h-lg">Three commitments we do not bend on</h2>
      </div>
      <div class="feature-grid">
        <article class="feature-card" data-reveal>
          <span class="feature-icon">{icon('chat', 26)}</span>
          <h3>You will understand your own treatment</h3>
          <p>Nothing is done to your teeth before you know what it is, why it is needed and what happens
          if you wait. Jargon is translated, X-rays are turned towards you, and questions are welcome
          for as long as you have them.</p>
        </article>
        <article class="feature-card" data-reveal data-reveal-delay="90">
          <span class="feature-icon">{icon('wallet', 26)}</span>
          <h3>The price is agreed before we start</h3>
          <p>You get a written plan, stage by stage, with costs. Where there is a cheaper option and a
          longer-lasting one, we tell you the difference honestly and the decision stays yours.</p>
        </article>
        <article class="feature-card" data-reveal data-reveal-delay="180">
          <span class="feature-icon">{icon('shield', 26)}</span>
          <h3>Sterilisation is not negotiable</h3>
          <p>Instruments are scrubbed, pouched and autoclaved between patients. Needles, gloves, blades
          and suction tips are single-use and opened in front of you. Surfaces are disinfected between
          every appointment.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container split media-right">
      <div class="split-media" data-reveal>
        <img src="images/treatment-plan.jpg" alt="Explaining a dental treatment plan to a patient" loading="lazy">
      </div>
      <div class="split-body" data-reveal data-reveal-delay="120">
        <span class="kicker">What that means for you</span>
        <h2 class="h-lg">The bits patients actually notice</h2>
        <p>Read the reviews this clinic has collected and the compliments are rarely about equipment.
        They are about being treated gently, being told the truth, and not being kept waiting.</p>
        <ul class="ticks">
          <li>Appointment-based scheduling, so waiting time stays short</li>
          <li>Local anaesthesia used properly &mdash; procedures should not hurt</li>
          <li>A pause the moment you raise your hand</li>
          <li>Written aftercare and a number you can actually call</li>
          <li>Parents welcome beside the chair for children's visits</li>
          <li>Cash, UPI, cards and NFC mobile payments accepted</li>
        </ul>
        <a class="btn" href="reviews.html">Read patient reviews</a>
      </div>
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
        <span class="kicker">In the clinic</span>
        <h2 class="h-lg">Equipped for the job</h2>
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

  <section class="section bg-cream">
    <div class="container split">
      <div class="split-media doctor-media" data-reveal>
        <img src="images/doctor-dhvani.jpg" alt="{CLINIC['doctor']}, dental surgeon and founder" loading="lazy">
      </div>
      <div class="split-body" data-reveal data-reveal-delay="120">
        <span class="kicker">Meet your dentist</span>
        <h2 class="h-lg">{CLINIC['doctor']}</h2>
        <p class="doctor-role">Dental Surgeon &amp; Founder</p>
        <p>An experienced dental surgeon whose patients consistently describe her as polite, patient and
        professional &mdash; and whose treatments they consistently describe as painless.</p>
        <a class="btn" href="doctor.html">Read her full profile</a>
      </div>
    </div>
  </section>
"""
    return (
        f"About Us | {CLINIC['name']}, Vavol, Gandhinagar",
        "About Samarth Dental Clinic, Vavol, Gandhinagar — a single-roof dental practice founded by "
        "Dr. Dhvani Joshi, rated 5.0 by 158+ patients.",
        body,
        None,
    )


# --------------------------------------------------------------------------- #

def doctor(services):
    body = banner(
        CLINIC["doctor"],
        "Dental Surgeon &amp; Founder, Samarth Dental Clinic, Vavol.",
        [("Doctor", None)],
        "images/doctor-dhvani.jpg",
    ) + f"""  <section class="section">
    <div class="container with-side">
      <article class="prose" data-reveal>
        <span class="kicker">Profile</span>
        <h2 class="h-lg">{CLINIC['doctor']}</h2>
        <p class="doctor-role">Dental Surgeon &amp; Founder</p>
        <p class="lead">{CLINIC['doctor']} is an experienced dental surgeon who founded Samarth Dental
        Clinic to bring every treatment a family might need under one roof &mdash; and to practise
        dentistry the way she believed it should be practised.</p>
        <p>Her patients tend to describe her in the same four words: polite, patient, caring,
        professional. What sits behind those words is a habit of explaining. Before anything is done,
        you are told what the problem is, what the options are, what each one costs and what happens if
        you choose to wait. Several reviews mention arriving braced for a difficult root canal and
        leaving having hardly felt it &mdash; which is mostly a matter of taking the time to anaesthetise
        properly and never rushing a nervous patient.</p>

        <h3>Treatments she carries out</h3>
        <ul class="ticks two">
          <li>Dental implants, single and multiple</li>
          <li>Root canal treatment and post-RCT crowns</li>
          <li>Surgical and wisdom tooth extractions</li>
          <li>Crowns, bridges and full-mouth rehabilitation</li>
          <li>Braces and clear aligner treatment</li>
          <li>Smile design, veneers and whitening</li>
          <li>Gum disease treatment and gum surgery</li>
          <li>Children's dentistry and preventive care</li>
        </ul>

        <h3>Her approach in the chair</h3>
        <p>Three things shape how she works. First, that a patient who understands their treatment is a
        calmer patient &mdash; so explanations come before instruments. Second, that pain is largely
        avoidable, and that anaesthesia given properly and unhurriedly is what makes the difference.
        Third, that money should never be a surprise, which is why plans are written down and costed
        before treatment begins.</p>
        <p>The result is a practice that a lot of families in Vavol now treat as their default. More
        than one review says some version of the same sentence: from now on, she is our family dentist.</p>

        <div class="callout">
          <p><strong>Consultations are unhurried by design.</strong> Bring your questions, and any
          X-rays or reports from previous dentists. You will leave knowing what is going on in your
          mouth and what your choices cost &mdash; whether or not you start treatment that day.</p>
        </div>
      </article>

      <aside class="side-stack" data-reveal data-reveal-delay="120">
        <div class="side-card" style="padding:0;overflow:hidden">
          <img src="images/doctor-dhvani.jpg" alt="{CLINIC['doctor']}" style="width:100%;height:340px;object-fit:cover" loading="lazy">
          <div style="padding:24px 28px 28px">
            <h3 style="margin-bottom:6px">{CLINIC['doctor']}</h3>
            <p style="font-size:14.5px">Dental Surgeon &amp; Founder</p>
            <p class="stars" style="color:#bd932f;letter-spacing:3px;margin-top:12px">{STARS}</p>
            <p style="font-size:14px">{CLINIC['rating']} from {CLINIC['reviews']}+ Google reviews</p>
          </div>
        </div>
        <div class="side-card contrast">
          <h3>Book with {CLINIC['doctor'].split()[1]}</h3>
          <p>Appointments Monday to Saturday, mornings and evenings.</p>
          <a class="phone" href="tel:{CLINIC['phone_link']}">{CLINIC['phone_display']}</a>
          <a class="btn btn-gold btn-block" href="appointment.html">Book an appointment</a>
        </div>
        <div class="side-card">
          <h3>Clinic hours</h3>
          {hours_block()}
        </div>
      </aside>
    </div>
  </section>

  <section class="section bg-sky">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="kicker">In her patients' words</span>
        <h2 class="h-lg">What people say after treatment</h2>
      </div>
      <div class="feature-grid">
        <article class="feature-card" data-reveal>
          <p class="stars" style="color:#bd932f;letter-spacing:3px;margin-bottom:14px">{STARS}</p>
          <p>&ldquo;She is very polite, skilled, and explains everything clearly. The treatment was
          smooth and almost pain-free.&rdquo;</p>
          <p style="margin-top:16px"><strong>Dipsa Mehta</strong></p>
        </article>
        <article class="feature-card" data-reveal data-reveal-delay="90">
          <p class="stars" style="color:#bd932f;letter-spacing:3px;margin-bottom:14px">{STARS}</p>
          <p>&ldquo;Extremely caring, patient and professional. Her guidance really helped reduce my
          fear and anxiety.&rdquo;</p>
          <p style="margin-top:16px"><strong>Ravina Vaishnav</strong></p>
        </article>
        <article class="feature-card" data-reveal data-reveal-delay="180">
          <p class="stars" style="color:#bd932f;letter-spacing:3px;margin-bottom:14px">{STARS}</p>
          <p>&ldquo;She handled each surgery step with care and accuracy. From now on she will be our
          family dentist.&rdquo;</p>
          <p style="margin-top:16px"><strong>Bunty Goswami</strong></p>
        </article>
      </div>
      <div style="text-align:center;margin-top:48px" data-reveal>
        <a class="btn btn-ink" href="reviews.html">Read all {CLINIC['reviews']}+ reviews</a>
      </div>
    </div>
  </section>
"""
    schema = {
        "@context": "https://schema.org",
        "@type": "Physician",
        "name": CLINIC["doctor"],
        "medicalSpecialty": "Dentistry",
        "jobTitle": "Dental Surgeon",
        "worksFor": {"@type": "Dentist", "name": CLINIC["name"]},
    }
    return (
        f"{CLINIC['doctor']} | Dentist in Vavol, Gandhinagar",
        f"{CLINIC['doctor']}, dental surgeon and founder of Samarth Dental Clinic, Vavol, "
        "Gandhinagar. Implants, root canals, braces, cosmetic and children's dentistry.",
        body,
        schema,
    )


# --------------------------------------------------------------------------- #

def services_index(services):
    cards = "".join(f"""        <article class="service-card" data-reveal data-reveal-delay="{i % 3 * 80}">
          <div class="service-thumb">
            <span class="service-num">{i + 1:02d}</span>
            <img src="{s['img']}" alt="{s['name'].replace('&amp;', 'and')} at Samarth Dental Clinic" loading="lazy">
          </div>
          <div class="service-body">
            <h3>{s['name']}</h3>
            <p>{s['card']}</p>
            <a class="link-arrow" href="{s['slug']}.html">Learn more</a>
          </div>
        </article>
""" for i, s in enumerate(services))

    body = banner(
        "Our Dental Services",
        f"{len(services)} treatments carried out under one roof in Vavol, Gandhinagar.",
        [("Services", None)],
        "images/dental-chair.jpg",
    ) + f"""  <section class="section">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="kicker">What we treat</span>
        <h2 class="h-lg">Everything from a six-monthly cleaning to a full implant case</h2>
        <p>Because it all happens here, you are not sent elsewhere halfway through treatment &mdash; and the
        dentist who diagnosed the problem is the one who fixes it.</p>
      </div>
      <div class="service-grid">
{cards}      </div>
    </div>
  </section>

  <section class="section bg-sky">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="kicker">Also available</span>
        <h2 class="h-lg">Alongside the treatments above</h2>
      </div>
      <div class="mini-grid" data-reveal>
        <article class="mini-tile">
          <span class="mini-icon">{icon('scan', 24)}</span>
          <h3>Digital dental X-rays</h3>
          <p>Taken in the clinic, on screen in seconds, with far less radiation than film.</p>
        </article>
        <article class="mini-tile">
          <span class="mini-icon">{icon('sparkle', 24)}</span>
          <h3>Emergency dental care</h3>
          <p>Toothache, swelling, a broken tooth or a knocked-out tooth &mdash; call and we will fit you in.</p>
        </article>
        <article class="mini-tile">
          <span class="mini-icon">{icon('smile', 24)}</span>
          <h3>Mouthguards &amp; night guards</h3>
          <p>Custom guards for sport, and for grinding your teeth at night.</p>
        </article>
        <article class="mini-tile">
          <span class="mini-icon">{icon('clipboard', 24)}</span>
          <h3>Second opinions</h3>
          <p>Bring another clinic's plan and X-rays and we will tell you honestly what we would do.</p>
        </article>
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
"""
    return (
        f"Dental Services in Vavol, Gandhinagar | {CLINIC['name']}",
        "Dental implants, root canals, braces, crowns, whitening, kids dentistry and more at "
        "Samarth Dental Clinic, Vavol, Gandhinagar.",
        body,
        None,
    )


# --------------------------------------------------------------------------- #

def gallery(services):
    items = "".join(f"""        <a class="gallery-item {cls}" href="{src}" data-lightbox="{src}">
          <img src="{src}" alt="{alt}" loading="lazy">
        </a>
""" for src, alt, cls in GALLERY_ALL)

    body = banner(
        "Clinic Gallery",
        "A look inside Samarth Dental Clinic before you visit.",
        [("Gallery", None)],
        "images/clinic-office.jpg",
    ) + f"""  <section class="section">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="kicker">Inside the clinic</span>
        <h2 class="h-lg">The rooms, the equipment, the everyday work</h2>
        <p>Tap any photograph to open it larger.</p>
      </div>
      <div class="gallery-grid" data-reveal>
{items}      </div>
    </div>
  </section>

  <section class="section-sm bg-sky">
    <div class="container" style="text-align:center">
      <h2 class="h-md" data-reveal>Would you rather see it in person?</h2>
      <p style="margin:16px auto 30px;max-width:560px" data-reveal>Walk in during clinic hours and have a
      look around, or book a consultation and we will show you the place properly.</p>
      <div class="hero-actions" style="justify-content:center" data-reveal>
        <a class="btn" href="appointment.html">Book an appointment</a>
        <a class="btn btn-outline" href="contact.html">Get directions</a>
      </div>
    </div>
  </section>
"""
    return (
        f"Clinic Gallery | {CLINIC['name']}, Vavol",
        "Photographs of Samarth Dental Clinic, Vavol, Gandhinagar — treatment rooms, equipment and "
        "everyday dental care.",
        body,
        None,
    )
