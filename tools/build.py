#!/usr/bin/env python3
"""Generate the static Samarth Dental Clinic site.

Run from the project root:

    python3 tools/build.py

Every .html file in the project root is produced by this script, so edit the
templates in tools/ rather than the generated markup.
"""

import os
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import chrome  # noqa: E402
import pages_forms  # noqa: E402
import pages_home  # noqa: E402
import pages_inner  # noqa: E402
import pages_service  # noqa: E402
from data_clinic import CLINIC  # noqa: E402
from data_services_a import SERVICES_A  # noqa: E402
from data_services_b import SERVICES_B  # noqa: E402

SERVICES = SERVICES_A + SERVICES_B

# Static pages: filename -> (builder, sitemap priority)
STATIC_PAGES = [
    ("about.html", pages_inner.about, "0.8"),
    ("doctor.html", pages_inner.doctor, "0.8"),
    ("services.html", pages_inner.services_index, "0.9"),
    ("gallery.html", pages_inner.gallery, "0.6"),
    ("reviews.html", pages_forms.reviews, "0.7"),
    ("contact.html", pages_forms.contact, "0.8"),
    ("appointment.html", pages_forms.appointment, "0.9"),
    ("faq.html", pages_forms.faq, "0.6"),
    ("dental-tips.html", pages_forms.dental_tips, "0.5"),
    ("404.html", pages_forms.not_found, None),
]

# Files left over from the previous (physiotherapy) site.
STALE = [
    "physiotherapy.html",
    "chiropractic.html",
    "visceral.html",
    "blog.html",
    "doctors.html",
    "_sheet.html",
]


def write(filename, html):
    path = os.path.join(ROOT, filename)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(html)
    return len(html)


def sitemap(urls):
    today = date.today().isoformat()
    entries = "".join(
        "  <url><loc>{base}/{loc}</loc><lastmod>{mod}</lastmod>"
        "<changefreq>monthly</changefreq><priority>{pri}</priority></url>\n".format(
            base=CLINIC["base_url"], loc=loc, mod=today, pri=pri
        )
        for loc, pri in urls
    )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + entries
        + "</urlset>\n"
    )


def main():
    written = []
    urls = [("", "1.0")]

    # Home
    html = chrome.page(
        "index.html",
        "Samarth Dental Clinic | Dentist in Vavol, Gandhinagar | Dr. Dhvani Joshi",
        "Samarth Dental Clinic, Vavol, Gandhinagar — dental implants, root canals, braces, crowns, "
        "whitening and kids dentistry by Dr. Dhvani Joshi. Rated 5.0 by 158+ patients.",
        pages_home.build(SERVICES),
        SERVICES,
    )
    write("index.html", html)
    written.append("index.html")

    # Static inner pages
    for filename, builder, priority in STATIC_PAGES:
        title, desc, body, schema = builder(SERVICES)
        write(filename, chrome.page(filename, title, desc, body, SERVICES, schema))
        written.append(filename)
        if priority:
            urls.append((filename, priority))

    # One page per treatment
    for service in SERVICES:
        filename = service["slug"] + ".html"
        title, desc, body, schema = pages_service.build(service, SERVICES)
        write(filename, chrome.page(filename, title, desc, body, SERVICES, schema))
        written.append(filename)
        urls.append((filename, "0.7"))

    write("sitemap.xml", sitemap(urls))

    # Clear out the previous site's pages
    removed = []
    for name in STALE:
        path = os.path.join(ROOT, name)
        if os.path.exists(path):
            os.remove(path)
            removed.append(name)

    print("Wrote %d pages + sitemap.xml" % len(written))
    for name in written:
        print("  ", name)
    if removed:
        print("Removed stale files:", ", ".join(removed))


if __name__ == "__main__":
    main()
