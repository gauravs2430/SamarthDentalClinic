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


def about(services):
    body = banner(
        "About Us",
        "Samarth Dental Clinic, Vavol, Gandhinagar.",
        [("About Us", None)],
        "images/clinic-interior.jpg",
    ) + f"""  <section class="section">
    <div class="container split">
      <div class="split-media">
        <img src="images/operatory.jpg" alt="Treatment room at Samarth Dental Clinic, Vavol" loading="lazy">
      </div>
      <div class="split-body">
        <h2>About the Clinic</h2>
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
        <a class="btn" href="appointment.html">Book Appointment</a>
      </div>
    </div>
  </section>

  <section class="section bg-sky">
    <div class="container">
      <div class="section-head center">
        <h2>Why Patients Visit Us</h2>
      </div>
      <div class="feature-grid">
        <article class="feature-card">
          <span class="feature-icon">{icon('chat', 26)}</span>
          <h3>Clear explanation</h3>
          <p>We explain the problem, the treatment and the cost before any work starts. X-rays are
          shown to you and questions are welcome.</p>
        </article>
        <article class="feature-card">
          <span class="feature-icon">{icon('wallet', 26)}</span>
          <h3>Cost in writing</h3>
          <p>You receive a written plan with the cost of each step. Where there is more than one option,
          we tell you the difference.</p>
        </article>
        <article class="feature-card">
          <span class="feature-icon">{icon('shield', 26)}</span>
          <h3>Sterilisation</h3>
          <p>Instruments are autoclaved between patients. Needles, gloves and suction tips are
          single-use.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head center">
        <h2>Clinic Facilities</h2>
      </div>
      <div class="mini-grid">
{"".join(f'''        <article class="mini-tile">
          <span class="mini-icon">{icon(ico, 24)}</span>
          <h3>{title}</h3>
          <p>{text}</p>
        </article>
''' for ico, title, text in TECH)}      </div>
    </div>
  </section>

  <section class="section bg-sky">
    <div class="container split">
      <div class="split-media doctor-media">
        <img src="images/doctor-dhvani.jpg" alt="{CLINIC['doctor']}, dental surgeon and founder" loading="lazy">
      </div>
      <div class="split-body">
        <h2>{CLINIC['doctor']}</h2>
        <p class="doctor-role">Dental Surgeon &amp; Founder</p>
        <p>{CLINIC['doctor']} is the dentist at Samarth Dental Clinic. She treats implants, root canals,
        braces, crowns, gum problems and children&rsquo;s teeth.</p>
        <a class="btn" href="doctor.html">Doctor Profile</a>
      </div>
    </div>
  </section>
"""
    return (
        f"About Us | {CLINIC['name']}, Vavol, Gandhinagar",
        "About Samarth Dental Clinic, Vavol, Gandhinagar — dental clinic founded by "
        "Dr. Dhvani Joshi.",
        body,
        None,
    )


def doctor(services):
    body = banner(
        CLINIC["doctor"],
        "Dental Surgeon &amp; Founder, Samarth Dental Clinic, Vavol.",
        [("Doctor", None)],
        "images/doctor-dhvani.jpg",
    ) + f"""  <section class="section">
    <div class="container with-side">
      <article class="prose">
        <h2>{CLINIC['doctor']}</h2>
        <p class="doctor-role">Dental Surgeon &amp; Founder</p>
        <p>{CLINIC['doctor']} is the dentist at Samarth Dental Clinic in Vavol, Gandhinagar. She
        treats implants, root canals, braces, crowns, gum problems and children&rsquo;s teeth.</p>
        <p>Treatment is explained before it starts, including the options and the cost. Procedures
        are done under local anaesthesia.</p>

        <h3>Treatments</h3>
        <ul class="ticks two">
          <li>Dental implants</li>
          <li>Root canal treatment</li>
          <li>Wisdom tooth removal</li>
          <li>Crowns and bridges</li>
          <li>Braces and clear aligners</li>
          <li>Smile design, veneers and whitening</li>
          <li>Gum disease treatment</li>
          <li>Kids dentistry</li>
        </ul>

        <div class="callout">
          <p>Bring previous X-rays or reports if you have them. After the check-up you will know
          what treatment is needed and what it costs.</p>
        </div>
      </article>

      <aside class="side-stack">
        <div class="side-card" style="padding:0;overflow:hidden">
          <img src="images/doctor-dhvani.jpg" alt="{CLINIC['doctor']}" style="width:100%;height:340px;object-fit:cover" loading="lazy">
          <div style="padding:24px 28px 28px">
            <h3 style="margin-bottom:6px">{CLINIC['doctor']}</h3>
            <p style="font-size:14.5px">Dental Surgeon &amp; Founder</p>
            <p class="stars" style="color:#c9a227;letter-spacing:2px;margin-top:12px">{STARS}</p>
            <p style="font-size:14px">{CLINIC['rating']} from {CLINIC['reviews']}+ Google reviews</p>
          </div>
        </div>
        <div class="side-card contrast">
          <h3>Book an Appointment</h3>
          <p>Monday to Saturday, mornings and evenings.</p>
          <a class="phone" href="tel:{CLINIC['phone_link']}">{CLINIC['phone_display']}</a>
          <a class="btn btn-block" href="appointment.html">Book Appointment</a>
        </div>
        <div class="side-card">
          <h3>Clinic Hours</h3>
          {hours_block()}
        </div>
      </aside>
    </div>
  </section>

  <section class="section bg-sky">
    <div class="container">
      <div class="section-head center">
        <h2>Patient Reviews</h2>
      </div>
      <div class="feature-grid">
        <article class="feature-card">
          <p class="stars" style="color:#c9a227;letter-spacing:2px;margin-bottom:12px">{STARS}</p>
          <p>&ldquo;She is very polite, skilled, and explains everything clearly. The treatment was
          smooth and almost pain-free.&rdquo;</p>
          <p style="margin-top:16px"><strong>Dipsa Mehta</strong></p>
        </article>
        <article class="feature-card">
          <p class="stars" style="color:#c9a227;letter-spacing:2px;margin-bottom:12px">{STARS}</p>
          <p>&ldquo;Extremely caring, patient and professional. Her guidance really helped reduce my
          fear and anxiety.&rdquo;</p>
          <p style="margin-top:16px"><strong>Ravina Vaishnav</strong></p>
        </article>
        <article class="feature-card">
          <p class="stars" style="color:#c9a227;letter-spacing:2px;margin-bottom:12px">{STARS}</p>
          <p>&ldquo;She handled each surgery step with care and accuracy. From now on she will be our
          family dentist.&rdquo;</p>
          <p style="margin-top:16px"><strong>Bunty Goswami</strong></p>
        </article>
      </div>
      <div class="block-cta">
        <a class="btn btn-ink" href="reviews.html">Read All Reviews</a>
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
        f"{CLINIC['doctor']}, dental surgeon at Samarth Dental Clinic, Vavol, "
        "Gandhinagar. Implants, root canals, braces and kids dentistry.",
        body,
        schema,
    )


def services_index(services):
    cards = "".join(f"""        <article class="service-card">
          <div class="service-thumb">
            <img src="{s['img']}" alt="{s['name'].replace('&amp;', 'and')} at Samarth Dental Clinic" loading="lazy">
          </div>
          <div class="service-body">
            <h3>{s['name']}</h3>
            <p>{s['card']}</p>
            <a class="link-arrow" href="{s['slug']}.html">Read More</a>
          </div>
        </article>
""" for s in services)

    body = banner(
        "Our Services",
        "Dental treatments at Samarth Dental Clinic, Vavol.",
        [("Services", None)],
        "images/dental-chair.jpg",
    ) + f"""  <section class="section">
    <div class="container">
      <div class="section-head center">
        <h2>Dental Treatments</h2>
        <p>Common treatments available at the clinic.</p>
      </div>
      <div class="service-grid">
{cards}      </div>
    </div>
  </section>

  <section class="section bg-sky">
    <div class="container">
      <div class="section-head center">
        <h2>Also Available</h2>
      </div>
      <div class="mini-grid">
        <article class="mini-tile">
          <span class="mini-icon">{icon('scan', 24)}</span>
          <h3>Digital X-rays</h3>
          <p>Taken in the clinic. The image is on screen in a few seconds.</p>
        </article>
        <article class="mini-tile">
          <span class="mini-icon">{icon('sparkle', 24)}</span>
          <h3>Emergency care</h3>
          <p>Toothache, swelling or a broken tooth &mdash; call and we will try to see you the same day.</p>
        </article>
        <article class="mini-tile">
          <span class="mini-icon">{icon('smile', 24)}</span>
          <h3>Mouthguards</h3>
          <p>Custom guards for sport and for grinding teeth at night.</p>
        </article>
        <article class="mini-tile">
          <span class="mini-icon">{icon('clipboard', 24)}</span>
          <h3>Second opinion</h3>
          <p>Bring another clinic&rsquo;s plan and X-rays and we will tell you what we would do.</p>
        </article>
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
"""
    return (
        f"Dental Services in Vavol, Gandhinagar | {CLINIC['name']}",
        "Dental implants, root canals, braces, crowns, whitening, kids dentistry and more at "
        "Samarth Dental Clinic, Vavol, Gandhinagar.",
        body,
        None,
    )


def gallery(services):
    items = "".join(f"""        <a class="gallery-item {cls}" href="{src}" data-lightbox="{src}">
          <img src="{src}" alt="{alt}" loading="lazy">
        </a>
""" for src, alt, cls in GALLERY_ALL)

    body = banner(
        "Gallery",
        "Photos of Samarth Dental Clinic, Vavol.",
        [("Gallery", None)],
        "images/clinic-office.jpg",
    ) + f"""  <section class="section">
    <div class="container">
      <div class="section-head center">
        <h2>Clinic Photos</h2>
        <p>Click a photo to view it larger.</p>
      </div>
      <div class="gallery-grid">
{items}      </div>
    </div>
  </section>
"""
    return (
        f"Clinic Gallery | {CLINIC['name']}, Vavol",
        "Photographs of Samarth Dental Clinic, Vavol, Gandhinagar.",
        body,
        None,
    )
