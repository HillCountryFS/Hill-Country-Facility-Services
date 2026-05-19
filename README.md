# Hill Country Facility Services — Website

Static marketing site for Hill Country Facility Services LLC, a commercial janitorial and facility services company serving Texas.

**Contact:** Contact@hillcountryfacilityservices.com · (512) 893-4012

---

## Project Structure

```
├── index.html                  Home
├── about.html                  About us
├── services.html               Services overview
├── industries.html             Industries served
├── locations.html              Locations overview
├── careers.html                Careers
├── contact.html                Contact
├── privacy.html                Privacy policy
├── terms.html                  Terms of service
├── accessibility.html          Accessibility statement
│
├── locations/                  Per-city landing pages (15 Texas cities)
│   ├── austin.html
│   ├── san-antonio.html
│   ├── dallas.html
│   └── ... (12 more)
│
├── css/                        Stylesheets
├── js/                         JavaScript
├── images/                     Photos, logos, map SVG
│
├── capabilities-overview.pdf   Downloadable capabilities one-pager
├── legal-drafts.md             Source notes for legal pages
│
├── sitemap.xml                 SEO sitemap
├── robots.txt
│
└── scripts/                    Python build / regeneration scripts
    ├── build_all.py
    ├── build_pages.py
    ├── build_locations.py
    ├── build_legal_pages.py
    ├── build_capabilities_pdf.py
    ├── build_map.py
    ├── add_capabilities_link.py
    └── update_existing_pages.py
```

---

## Running Locally

This is a plain static site — no build step required to view it.

```bash
# Any static server works. Two easy options:
python3 -m http.server 8000
# then open http://localhost:8000

# or
npx serve .
```

---

## Build Scripts (optional)

The `scripts/` directory contains the Python generators originally used to scaffold the site. They are not required to deploy or view it — the generated HTML files are committed directly. Use them if you want to regenerate pages programmatically.

```bash
# regenerate everything
python3 scripts/build_all.py

# rebuild only location pages
python3 scripts/build_locations.py

# rebuild the capabilities PDF
python3 scripts/build_capabilities_pdf.py
```

Scripts that need PDF generation depend on `reportlab`:

```bash
pip install reportlab
```

---

## Deploying

The site is pure static HTML/CSS/JS plus images and one PDF. It can be hosted on:

- **GitHub Pages** — push to a `gh-pages` branch or enable Pages on `main`
- **Netlify / Vercel / Cloudflare Pages** — point at the repo root, no build command needed
- **Any S3 / CDN bucket** — sync the directory as-is

---

## License & Photo Credits

- Site code: © Hill Country Facility Services LLC
- Photography: licensed from Pexels (royalty-free, commercial use)
- Texas locations SVG map: custom, built via `scripts/build_map.py`
