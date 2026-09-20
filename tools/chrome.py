"""Shared page chrome: <head>, top bar, header, footer, banners, CTA band."""

import json

from data_clinic import CLINIC, HOURS

# --------------------------------------------------------------------------- #
# Icons
# --------------------------------------------------------------------------- #

_ICONS = {
    "phone": '<path d="M7 3h3l1.6 4-2.1 1.3a12 12 0 0 0 5.2 5.2L16 11.4 20 13v3.2A1.8 1.8 0 0 1 18 18 15.6 15.6 0 0 1 4 4 1.8 1.8 0 0 1 5.8 2H7z"/>',
    "clock": '<circle cx="12" cy="12" r="8.4"/><path d="M12 7.6V12l3 2"/>',
    "pin": '<path d="M12 21s-6.6-4.6-6.6-9.8A6.6 6.6 0 0 1 12 4.6a6.6 6.6 0 0 1 6.6 6.6C18.6 16.4 12 21 12 21z"/><circle cx="12" cy="11" r="2.4"/>',
    "mail": '<rect x="3" y="5.5" width="18" height="13" rx="1.4"/><path d="m3.6 6.6 8.4 6 8.4-6"/>',
    "calendar": '<rect x="3.6" y="5" width="16.8" height="15" rx="1.4"/><path d="M3.6 10h16.8M8.5 3.4v3.2M15.5 3.4v3.2"/>',
    "shield": '<path d="M12 3.2 5.4 5.8v5.4c0 4.2 2.8 7.5 6.6 9.6 3.8-2.1 6.6-5.4 6.6-9.6V5.8z"/><path d="m9.2 11.8 2 2.1 3.6-3.8"/>',
    "smile": '<circle cx="12" cy="12" r="8.6"/><path d="M8.2 13.6a4.4 4.4 0 0 0 7.6 0M9.2 9.4h.01M14.8 9.4h.01"/>',
    "wallet": '<rect x="3" y="6" width="18" height="13" rx="1.6"/><path d="M3 10h18M16.4 14.6h1.8"/>',
    "users": '<circle cx="9.4" cy="8.6" r="3.4"/><path d="M3.4 19.4a6 6 0 0 1 12 0M16.6 5.8a3.4 3.4 0 0 1 0 5.6M18 19.4a5.6 5.6 0 0 0-1.6-3.9"/>',
    "tooth": '<path d="M12 3.4c-2.1 0-3 1-4.8 1S4 6.1 4 8.9c0 2.2.7 3.9 1.3 6.2.6 2 .8 3.8 1.2 5.6.3 1.6.8 2.4 1.8 2.4s1.5-1 1.8-2.6c.3-1.7.6-3.6 2.5-3.6s2.2 1.9 2.5 3.6c.3 1.6.7 2.6 1.8 2.6s1.5-.8 1.8-2.4c.4-1.8.6-3.6 1.2-5.6C20.3 12.8 21 11.1 21 8.9c0-2.8-1.4-4.5-3.7-4.5-1.8 0-2.7-1-4.8-1z" transform="scale(0.92) translate(1 -0.4)"/>',
    "sparkle": '<path d="M12 3.4 13.9 9l5.6 1.9-5.6 1.9L12 18.4 10.1 12.8 4.5 10.9 10.1 9z"/><path d="M18.4 3.6v2.8M17 5h2.8"/>',
    "star": '<path d="m12 3.6 2.6 5.5 6 .8-4.4 4.2 1.1 6-5.3-2.9-5.3 2.9 1.1-6L3.4 9.9l6-.8z"/>',
    "chat": '<path d="M20.4 12.4a7.9 7.9 0 0 1-11.6 7l-4.6 1.4 1.4-4.4A7.9 7.9 0 1 1 20.4 12.4z"/><path d="M9 11.6h.01M12.4 11.6h.01M15.8 11.6h.01"/>',
    "arrow-up": '<path d="M12 19V5.6M6 11.4 12 5.4l6 6"/>',
    "clipboard": '<rect x="5.4" y="4.6" width="13.2" height="15.4" rx="1.4"/><path d="M9.2 4.6V3.4h5.6v1.2M9 11h6M9 14.6h4"/>',
    "scan": '<path d="M4 8.4V5.6A1.6 1.6 0 0 1 5.6 4h2.8M15.6 4h2.8A1.6 1.6 0 0 1 20 5.6v2.8M20 15.6v2.8a1.6 1.6 0 0 1-1.6 1.6h-2.8M8.4 20H5.6A1.6 1.6 0 0 1 4 18.4v-2.8"/><path d="M7.6 12h8.8"/>',
}

_SOCIAL = {
    "facebook": '<path d="M14.3 8.6h2.3V5.7h-2.6c-2.3 0-3.8 1.5-3.8 3.9v1.6H8v3h2.2V21h3.1v-6.8h2.4l.4-3h-2.8V9.8c0-.8.4-1.2 1-1.2z" fill="currentColor" stroke="none"/>',
    "instagram": '<rect x="4.4" y="4.4" width="15.2" height="15.2" rx="4.2"/><circle cx="12" cy="12" r="3.6"/><path d="M16.8 7.4h.01"/>',
    "google": '<path d="M20.4 12.2c0-.6-.06-1.2-.16-1.7H12v3.3h4.7a4.1 4.1 0 0 1-1.8 2.7v2.2h2.9a8.6 8.6 0 0 0 2.6-6.5z" fill="currentColor" stroke="none"/><path d="M12 21a8.7 8.7 0 0 0 6-2.2l-2.9-2.2a5.4 5.4 0 0 1-8.1-2.9H4v2.3A9 9 0 0 0 12 21z" fill="currentColor" stroke="none"/><path d="M7 13.7a5.4 5.4 0 0 1 0-3.4V8H4a9 9 0 0 0 0 8z" fill="currentColor" stroke="none"/><path d="M12 6.6a4.9 4.9 0 0 1 3.4 1.3l2.6-2.5A8.7 8.7 0 0 0 4 8l3 2.3A5.4 5.4 0 0 1 12 6.6z" fill="currentColor" stroke="none"/>',
}


def icon(name, size=20, stroke=1.7):
    """Inline icon. Kept inline so the site needs no icon font or CDN request.

    Pass stroke=0 for the solid icons ("tooth", "star", "sparkle"), which are
    drawn as filled shapes rather than outlines.
    """
    body = _ICONS.get(name) or _SOCIAL.get(name, "")
    if stroke:
        paint = f'fill="none" stroke="currentColor" stroke-width="{stroke}"'
    else:
        paint = 'fill="currentColor" stroke="none"'
    return (
        f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" {paint} '
        f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>'
    )


STARS = "&#9733;&#9733;&#9733;&#9733;&#9733;"


# --------------------------------------------------------------------------- #
# Navigation
# --------------------------------------------------------------------------- #

NAV = [
    ("index.html", "Home"),
    ("about.html", "About Us"),
    ("__services__", "Services"),
    ("doctor.html", "Doctor"),
    ("gallery.html", "Gallery"),
    ("reviews.html", "Reviews"),
    ("contact.html", "Contact"),
]


def _drop(services):
    items = "".join(
        f'<a href="{s["slug"]}.html">{s["nav"]}</a>' for s in services
    )
    return (
        '<div class="drop">'
        + items
        + '<div class="drop-all"><a href="services.html">View all services &rarr;</a></div>'
        + "</div>"
    )


def _nav(services):
    out = ['<button class="nav-close" type="button" aria-label="Close menu">&times;</button>']
    for href, label in NAV:
        if href == "__services__":
            out.append(
                '<div class="has-drop"><a class="nav-link" href="services.html">'
                f'Services <span class="caret"></span></a>{_drop(services)}</div>'
            )
        else:
            out.append(f'<a class="nav-link" href="{href}">{label}</a>')
    return '<nav class="nav" aria-label="Primary">' + "".join(out) + "</nav>"


# --------------------------------------------------------------------------- #
# Structured data
# --------------------------------------------------------------------------- #

def _schema(services):
    return {
        "@context": "https://schema.org",
        "@type": "Dentist",
        "name": CLINIC["name"],
        "image": CLINIC["base_url"] + "/images/clinic-interior.jpg",
        "url": CLINIC["base_url"] + "/",
        "telephone": CLINIC["phone_display"],
        "priceRange": "₹₹",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Shop No. S09, ShantiNagar Shopping, Vavol",
            "addressLocality": CLINIC["city"],
            "addressRegion": CLINIC["state"],
            "postalCode": CLINIC["pin"],
            "addressCountry": "IN",
        },
        "openingHoursSpecification": [
            {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
                "opens": "10:00",
                "closes": "13:00",
            },
            {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
                "opens": "16:00",
                "closes": "19:00",
            },
        ],
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": CLINIC["rating"],
            "reviewCount": CLINIC["reviews"],
            "bestRating": "5",
        },
        "founder": {"@type": "Person", "name": CLINIC["doctor"], "jobTitle": "Dental Surgeon"},
        "availableService": [
            {"@type": "MedicalProcedure", "name": s["name"].replace("&amp;", "&")}
            for s in services
        ],
    }


# --------------------------------------------------------------------------- #
# Chrome blocks
# --------------------------------------------------------------------------- #

def topbar():
    return f"""  <div class="topbar">
    <div class="container topbar-inner">
      <ul class="topbar-list">
        <li class="topbar-hide-sm">{icon('pin', 15)}<span>{CLINIC['street']}, {CLINIC['area']}</span></li>
        <li>{icon('clock', 15)}<span class="topbar-hours-lg">Mon&ndash;Sat: 10&ndash;1 &amp; 4&ndash;7 &middot; Sun closed</span><span class="topbar-hours-sm">Mon&ndash;Sat &middot; 10&ndash;1 &amp; 4&ndash;7</span></li>
      </ul>
      <div class="topbar-rating">
        <span class="stars" aria-hidden="true">{STARS}</span>
        <span><strong>{CLINIC['rating']}</strong><span class="topbar-rating-extra"> from {CLINIC['reviews']}+ Google reviews</span></span>
      </div>
    </div>
  </div>
"""


def header(services):
    return f"""  <header class="site-header">
    <div class="container nav-wrap">
      <a class="logo" href="index.html" aria-label="{CLINIC['name']} home">
        <span class="logo-mark"><img src="images/logo-mark.png" alt=""></span>
        <span class="logo-text"><strong>{CLINIC['name']}</strong><small>Vavol &middot; Gandhinagar</small></span>
      </a>
{_nav(services)}
      <div class="header-actions">
        <a class="header-call" href="tel:{CLINIC['phone_link']}">
          <span class="header-call-icon">{icon('phone', 19)}</span>
          <span><span>Call the clinic</span><strong>{CLINIC['phone_display']}</strong></span>
        </a>
        <a class="btn" href="appointment.html">Book Appointment</a>
        <button class="menu-toggle" type="button" aria-label="Open menu" aria-expanded="false">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
        </button>
      </div>
    </div>
  </header>
  <div class="nav-backdrop" aria-hidden="true"></div>
"""


def cta_band():
    return f"""  <section class="cta-band">
    <div class="container cta-band-inner">
      <div>
        <h2>Book an Appointment</h2>
        <p>Call or WhatsApp the clinic and we will confirm a time that works for you.</p>
      </div>
      <div class="cta-band-actions">
        <a class="btn" href="appointment.html">Book Appointment</a>
        <a class="btn btn-ghost-light" href="tel:{CLINIC['phone_link']}">{icon('phone', 18)} Call Now</a>
      </div>
    </div>
  </section>
"""


def footer(services):
    service_links = "".join(
        f'<a href="{s["slug"]}.html">{s["nav"]}</a>' for s in services[:7]
    )
    more_links = "".join(
        f'<a href="{s["slug"]}.html">{s["nav"]}</a>' for s in services[7:]
    )
    quick = "".join(
        f'<a href="{href}">{label}</a>'
        for href, label in [
            ("about.html", "About Us"),
            ("doctor.html", "Our Doctor"),
            ("services.html", "All Services"),
            ("gallery.html", "Gallery"),
            ("reviews.html", "Patient Reviews"),
            ("faq.html", "FAQs"),
            ("dental-tips.html", "Dental Tips"),
            ("contact.html", "Contact Us"),
        ]
    )
    return f"""  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <div class="footer-brand">
            <span class="logo-mark"><img src="images/logo-mark.png" alt=""></span>
            <span><strong>{CLINIC['name']}</strong><small>Vavol &middot; Gandhinagar</small></span>
          </div>
          <p>Dental clinic in Vavol, Gandhinagar. Implants, root canal, braces, cleaning, fillings
          and kids dentistry.</p>
          <div class="socials">
            <a href="https://www.google.com/maps/search/?api=1&amp;query={CLINIC['maps_query']}" target="_blank" rel="noopener" aria-label="Find us on Google">{icon('google', 18)}</a>
            <a href="https://wa.me/{CLINIC['whatsapp']}" target="_blank" rel="noopener" aria-label="WhatsApp the clinic">{icon('chat', 18)}</a>
            <a href="tel:{CLINIC['phone_link']}" aria-label="Call the clinic">{icon('phone', 18)}</a>
          </div>
        </div>
        <div>
          <h3>Treatments</h3>
          <div class="footer-links">{service_links}</div>
        </div>
        <div>
          <h3>More &amp; Quick Links</h3>
          <div class="footer-links">{more_links}{quick}</div>
        </div>
        <div>
          <h3>Visit Us</h3>
          <ul class="footer-contact">
            <li>{icon('pin', 18)}<span>{CLINIC['street']},<br>{CLINIC['area']} {CLINIC['pin']}<br>({CLINIC['landmark']})</span></li>
            <li>{icon('phone', 18)}<span><a href="tel:{CLINIC['phone_link']}">{CLINIC['phone_display']}</a></span></li>
            <li>{icon('mail', 18)}<span><a href="mailto:{CLINIC['email']}">{CLINIC['email']}</a></span></li>
            <li>{icon('clock', 18)}<span>Mon&ndash;Sat: 10:00 AM &ndash; 1:00 PM<br>&amp; 4:00 PM &ndash; 7:00 PM<br>Sunday: Closed</span></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>&copy; <span data-year>2026</span> {CLINIC['name']}, Vavol, Gandhinagar. All rights reserved.</span>
        <span>Appointments recommended &middot; UPI, cards &amp; cash accepted</span>
      </div>
    </div>
  </footer>
"""


def floats():
    return f"""  <div class="floats">
    <button class="float-btn float-top" type="button" aria-label="Back to top">{icon('arrow-up', 20)}</button>
    <a class="float-btn float-call" href="tel:{CLINIC['phone_link']}" aria-label="Call the clinic">{icon('phone', 20)}</a>
    <a class="float-btn float-wa" href="https://wa.me/{CLINIC['whatsapp']}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{icon('chat', 22)}</a>
  </div>
  <div class="lightbox" role="dialog" aria-modal="true" aria-label="Image viewer">
    <button class="lightbox-close" type="button" aria-label="Close">&times;</button>
    <div><img alt=""><p class="lightbox-caption"></p></div>
  </div>
"""


def banner(title, subtitle, crumbs, img):
    """Inner-page hero. ``crumbs`` is a list of (label, href-or-None) tuples."""
    parts = ['<a href="index.html">Home</a>']
    for label, href in crumbs:
        parts.append('<span class="sep">/</span>')
        parts.append(f'<a href="{href}">{label}</a>' if href else f"<span>{label}</span>")
    sub = f"<p>{subtitle}</p>" if subtitle else ""
    return f"""  <section class="page-banner" style="--banner-img:url('{img}')">
    <div class="container">
      <p class="crumbs">{''.join(parts)}</p>
      <h1>{title}</h1>
      {sub}
    </div>
  </section>
"""


def page(filename, title, description, body, services, extra_schema=None):
    """Assemble a complete HTML document."""
    canonical = f"{CLINIC['base_url']}/{filename}"
    blocks = [_schema(services)]
    if extra_schema:
        blocks.append(extra_schema)
    ld = "\n".join(
        '  <script type="application/ld+json">' + json.dumps(b, ensure_ascii=False) + "</script>"
        for b in blocks
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical}">
  <meta name="theme-color" content="#0e8a80">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{CLINIC['name']}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{CLINIC['base_url']}/images/clinic-interior.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="favicon.png" type="image/png">
  <link rel="apple-touch-icon" href="images/apple-touch.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">
{ld}
</head>
<body>
{topbar()}{header(services)}
  <main>
{body}  </main>
{cta_band()}{footer(services)}{floats()}
  <script src="js/main.js"></script>
</body>
</html>
"""


def hours_block():
    rows = "".join(
        f'<li><span>{day}</span><span class="{"closed" if closed else ""}">{val}</span></li>'
        for day, val, closed in HOURS
    )
    return f'<ul class="hours-list">{rows}</ul>'
