"""
Update the 6 original pages (index, about, services, industries, careers, contact)
to:
  1. Insert the new Locations dropdown into the primary nav (between Industries and Careers).
  2. Replace the "Capabilities" footer column with a "Locations" column.

The dropdown markup matches build_locations.py header_html().
"""
from pathlib import Path
import re

ROOT = Path("/home/user/workspace/hcfs")
PAGES = ["index.html", "about.html", "services.html", "industries.html", "careers.html", "contact.html"]

# --- City data (must match build_locations.py grouping) ---
GROUPS = {
    "San Antonio": [("san-antonio", "San Antonio"), ("new-braunfels", "New Braunfels")],
    "Austin Metro": [
        ("austin", "Austin"), ("round-rock", "Round Rock"), ("cedar-park", "Cedar Park"),
        ("pflugerville", "Pflugerville"), ("georgetown", "Georgetown"), ("san-marcos", "San Marcos"),
    ],
    "DFW Metroplex": [
        ("dallas", "Dallas"), ("fort-worth", "Fort Worth"), ("plano", "Plano"),
        ("frisco", "Frisco"), ("arlington", "Arlington"), ("irving", "Irving"),
    ],
    "Houston": [("houston", "Houston")],
}

FOOTER_GROUPS = {
    "Austin Metro": ["austin", "round-rock", "cedar-park", "pflugerville", "georgetown", "san-marcos"],
    "DFW": ["dallas", "fort-worth", "plano", "frisco", "arlington", "irving"],
    "South Central": ["san-antonio", "new-braunfels"],
    "Gulf Coast": ["houston"],
}
SLUG_TO_NAME = {slug: name for slugs in GROUPS.values() for slug, name in slugs}


def build_dropdown():
    parts = []
    for group_name, slugs in GROUPS.items():
        parts.append(f'<div class="nav-drop-group"><div class="nav-drop-label">{group_name}</div>')
        for slug, name in slugs:
            parts.append(f'<a href="locations/{slug}.html">{name}</a>')
        parts.append('</div>')
    parts.append('<div class="nav-drop-group"><a href="locations.html" class="nav-drop-all">View all locations →</a></div>')
    return "\n          ".join(parts)


NAV_DROPDOWN_HTML = f"""      <div class="nav-drop">
        <a href="locations.html">Locations <svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg></a>
        <div class="nav-drop-menu">
          {build_dropdown()}
        </div>
      </div>
"""


def build_footer_locations_col():
    def make_links(slugs):
        return "".join(f'<li><a href="locations/{s}.html">{SLUG_TO_NAME[s]}</a></li>' for s in slugs)

    rows = "\n        ".join(
        f'<div class="footer-loc-group"><span class="footer-loc-label">{label}</span><ul>{make_links(slugs)}</ul></div>'
        for label, slugs in FOOTER_GROUPS.items()
    )
    return f"""      <div class="footer-col footer-locations">
        <h4>Locations</h4>
        {rows}
        <a href="locations.html" class="footer-loc-all">View all locations →</a>
      </div>"""


FOOTER_LOC_COL_HTML = build_footer_locations_col()


def update_nav(html: str) -> str:
    # Insert the dropdown right before the Careers link inside <nav class="nav">.
    # Match the Industries link followed by whitespace+Careers link, insert between them.
    pattern = re.compile(
        r'(<a href="industries\.html">Industries</a>\s*\n)\s*(<a href="careers\.html">Careers</a>)',
        re.MULTILINE,
    )
    if not pattern.search(html):
        # Already has the dropdown? Skip silently.
        if 'class="nav-drop"' in html:
            return html
        raise RuntimeError("Could not find the nav anchor (Industries → Careers) to insert dropdown.")
    return pattern.sub(r'\1' + NAV_DROPDOWN_HTML + r'      \2', html)


def update_footer(html: str) -> str:
    # Replace the entire "Capabilities" footer column with the new Locations column.
    # The Capabilities column starts at <div class="footer-col"> containing <h4>Capabilities</h4>
    # and ends at the closing </div> before the next <div class="footer-col ...">.
    pattern = re.compile(
        r'<div class="footer-col">\s*<h4>Capabilities</h4>.*?</div>\s*(?=<div class="footer-col)',
        re.DOTALL,
    )
    if 'footer-locations' in html:
        return html  # already updated
    new_html, n = pattern.subn(FOOTER_LOC_COL_HTML + "\n      ", html)
    if n != 1:
        raise RuntimeError("Could not find 'Capabilities' footer column to replace.")
    return new_html


def main():
    for page in PAGES:
        p = ROOT / page
        html = p.read_text()
        html = update_nav(html)
        html = update_footer(html)
        p.write_text(html)
        print(f"updated {p}")


if __name__ == "__main__":
    main()
