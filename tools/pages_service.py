"""Service detail pages — one shared template, driven by the service data."""

from chrome import banner, hours_block, icon
from data_clinic import CLINIC


def _side_nav(services, current):
    parts = []
    for s in services:
        cls = ' class="active"' if s["slug"] == current else ""
        parts.append('<a href="%s.html"%s>%s</a>' % (s["slug"], cls, s["nav"]))
    return '<div class="side-nav">%s</div>' % "".join(parts)


def _related(services, current):
    picks = [s for s in services if s["slug"] != current][:3]
    cards = "".join(f"""        <article class="service-card">
          <div class="service-thumb"><img src="{s['img']}" alt="{s['name'].replace('&amp;', 'and')}" loading="lazy"></div>
          <div class="service-body">
            <h3>{s['name']}</h3>
            <p>{s['card']}</p>
            <a class="link-arrow" href="{s['slug']}.html">Read More</a>
          </div>
        </article>
""" for s in picks)
    return f"""  <section class="section bg-sky">
    <div class="container">
      <div class="section-head center">
        <h2>Related Treatments</h2>
      </div>
      <div class="service-grid">
{cards}      </div>
    </div>
  </section>
"""


def build(service, services):
    plain = service["name"].replace("&amp;", "and")

    intro = "".join(f"<p>{p}</p>" for p in service["intro"])
    signs = "".join(f"<li>{s}</li>" for s in service["signs"])
    benefits = "".join(f"<li>{b}</li>" for b in service["benefits"])
    steps = "".join(f"""        <article class="step">
          <h3>{title}</h3>
          <p>{text}</p>
        </article>
""" for title, text in service["steps"])
    facts = "".join(f"<tr><th scope='row'>{k}</th><td>{v}</td></tr>" for k, v in service["facts"])

    body = banner(
        plain,
        service["card"],
        [("Services", "services.html"), (plain, None)],
        service["banner"],
    ) + f"""  <section class="section">
    <div class="container with-side">
      <article class="prose">
        <figure class="fig">
          <img src="{service['img']}" alt="{plain} at Samarth Dental Clinic, Vavol, Gandhinagar">
          <figcaption>{plain} at Samarth Dental Clinic, Vavol.</figcaption>
        </figure>

        <h2>About this treatment</h2>
        {intro}

        <h3>When it is needed</h3>
        <ul class="ticks two">{signs}</ul>

        <h3>At a glance</h3>
        <div class="table-wrap">
          <table class="tbl">
            <caption class="sr-only">Key facts about {plain}</caption>
            <tbody>{facts}</tbody>
          </table>
        </div>

        <h3>Benefits</h3>
        <ul class="ticks">{benefits}</ul>

        <div class="callout">
          <p>Not sure this is what you need? Book a check-up. We will look at the tooth, explain
          the options and give you the cost before treatment starts.</p>
        </div>

        <h3>Book an appointment</h3>
        <p>Call or WhatsApp <a href="tel:{CLINIC['phone_link']}">{CLINIC['phone_display']}</a>.
        The clinic is at {CLINIC['street']}, {CLINIC['area']} {CLINIC['pin']},
        {CLINIC['landmark'].lower()}. Open Monday to Saturday, 10 AM&ndash;1 PM and 4 PM&ndash;7 PM.</p>
      </article>

      <aside class="side-stack">
        <div class="side-card">
          <h3>All Treatments</h3>
          {_side_nav(services, service['slug'])}
        </div>
        <div class="side-card contrast">
          <h3>Book Appointment</h3>
          <p>Call the clinic to confirm a time.</p>
          <a class="phone" href="tel:{CLINIC['phone_link']}">{CLINIC['phone_display']}</a>
          <a class="btn btn-block" href="appointment.html">Book Appointment</a>
        </div>
        <div class="side-card">
          <h3>Clinic Hours</h3>
          {hours_block()}
        </div>
        <div class="side-card">
          <h3>Find Us</h3>
          <p style="display:flex;gap:12px">{icon('pin', 18)} <span>{CLINIC['street']},<br>{CLINIC['area']} {CLINIC['pin']}<br>({CLINIC['landmark']})</span></p>
          <p style="margin-top:18px"><a class="link-arrow" href="contact.html">Directions</a></p>
        </div>
      </aside>
    </div>
  </section>

  <section class="section bg-cream">
    <div class="container">
      <div class="section-head center">
        <h2>How Treatment Is Done</h2>
      </div>
      <div class="steps">
{steps}      </div>
    </div>
  </section>

""" + _related(services, service["slug"])

    schema = {
        "@context": "https://schema.org",
        "@type": "MedicalProcedure",
        "name": plain,
        "howPerformed": " ".join(t for _, t in service["steps"]),
        "provider": {"@type": "Dentist", "name": CLINIC["name"]},
    }

    title = f"{plain} in Vavol, Gandhinagar | {CLINIC['name']}"
    return title, service["meta"], body, schema
