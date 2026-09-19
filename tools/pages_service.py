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
    cards = "".join(f"""        <article class="service-card" data-reveal>
          <div class="service-thumb"><img src="{s['img']}" alt="{s['name'].replace('&amp;', 'and')}" loading="lazy"></div>
          <div class="service-body">
            <h3>{s['name']}</h3>
            <p>{s['card']}</p>
            <a class="link-arrow" href="{s['slug']}.html">Learn more</a>
          </div>
        </article>
""" for s in picks)
    return f"""  <section class="section bg-sky">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="kicker">Related treatments</span>
        <h2 class="h-lg">You may also be looking for</h2>
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
    steps = "".join(f"""        <article class="step" data-reveal data-reveal-delay="{i * 80}">
          <h3>{title}</h3>
          <p>{text}</p>
        </article>
""" for i, (title, text) in enumerate(service["steps"]))
    facts = "".join(f"<tr><th scope='row'>{k}</th><td>{v}</td></tr>" for k, v in service["facts"])

    body = banner(
        plain,
        service["card"],
        [("Services", "services.html"), (plain, None)],
        service["banner"],
    ) + f"""  <section class="section">
    <div class="container with-side">
      <article class="prose" data-reveal>
        <figure class="fig">
          <img src="{service['img']}" alt="{plain} at Samarth Dental Clinic, Vavol, Gandhinagar">
          <figcaption>{plain} at Samarth Dental Clinic &mdash; Vavol, Gandhinagar.</figcaption>
        </figure>

        <h2 class="h-md">What it is</h2>
        {intro}

        <h3>Signs you may need this treatment</h3>
        <ul class="ticks two">{signs}</ul>

        <h3>At a glance</h3>
        <div class="table-wrap">
          <table class="tbl">
            <caption class="sr-only">Key facts about {plain}</caption>
            <tbody>{facts}</tbody>
          </table>
        </div>

        <h3>What you gain</h3>
        <ul class="ticks">{benefits}</ul>

        <div class="callout">
          <p><strong>Not sure this is what you need?</strong> That is exactly what a consultation is
          for. Come in, let us look properly, and you will leave knowing what the problem is and what
          your options cost &mdash; with no obligation to start that day.</p>
        </div>

        <h3>Booking your appointment</h3>
        <p>Call or WhatsApp <a href="tel:{CLINIC['phone_link']}">{CLINIC['phone_display']}</a> and we
        will find you a slot, usually the same day. The clinic is at {CLINIC['street']},
        {CLINIC['area']} {CLINIC['pin']} &mdash; {CLINIC['landmark'].lower()} &mdash; open Monday to Saturday,
        mornings and evenings.</p>
      </article>

      <aside class="side-stack" data-reveal data-reveal-delay="120">
        <div class="side-card">
          <h3>All treatments</h3>
          {_side_nav(services, service['slug'])}
        </div>
        <div class="side-card contrast">
          <h3>Book {plain}</h3>
          <p>Speak to us about your case and what it will involve.</p>
          <a class="phone" href="tel:{CLINIC['phone_link']}">{CLINIC['phone_display']}</a>
          <a class="btn btn-gold btn-block" href="appointment.html">Book an appointment</a>
        </div>
        <div class="side-card">
          <h3>Clinic hours</h3>
          {hours_block()}
        </div>
        <div class="side-card">
          <h3>Find us</h3>
          <p style="display:flex;gap:12px">{icon('pin', 18)} <span>{CLINIC['street']},<br>{CLINIC['area']} {CLINIC['pin']}<br>({CLINIC['landmark']})</span></p>
          <p style="margin-top:18px"><a class="link-arrow" href="contact.html">Directions</a></p>
        </div>
      </aside>
    </div>
  </section>

  <section class="section bg-cream">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="kicker">The procedure</span>
        <h2 class="h-lg">How {plain.lower()} is done here</h2>
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
