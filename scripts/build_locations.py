"""Generate location-based SEO pages for Hill Country Facility Services.

Each city page has unique copy framed for that local market. Pages share the
site's header/footer chrome so they look and feel like the rest of the site.
"""

import os
import re
from pathlib import Path

# ----------------------------------------------------------------------------
# Per-city content. Each city gets its own market framing, business district
# mentions, and slightly different lead paragraph so we are not publishing
# duplicate content across pages.
# ----------------------------------------------------------------------------

CITIES = [
    {
        "slug": "san-antonio",
        "name": "San Antonio",
        "region": "South Central Texas",
        "metro": "San Antonio metro",
        "districts": "downtown, the Pearl, Stone Oak, Northwest Side, the Medical Center, and the I-10 / I-35 corridors",
        "industries": "tourism and hospitality, healthcare systems, military and defense, manufacturing, and Class A office",
        "lead": "From the Medical Center to Stone Oak and downtown, San Antonio commercial properties run on tight operational standards. We deliver disciplined janitorial, floor restoration, and facility maintenance programs scoped to your portfolio.",
        "why": "San Antonio's mix of hospitality, healthcare, and corporate campuses requires a contractor that runs documented programs across very different operating environments. Our supervisors and crews are trained for each.",
        "hero_image": "corporate-interior.jpg",
        "metro_keywords": "San Antonio, Bexar County, Stone Oak, Medical Center, Pearl District, Northwest San Antonio",
    },
    {
        "slug": "austin",
        "name": "Austin",
        "region": "Central Texas",
        "metro": "Austin metro",
        "districts": "downtown, the Domain, East Austin, the tech corridor along Mopac, and the 183 / 290 industrial belts",
        "industries": "technology, life sciences, creative office, advanced manufacturing, and multi-tenant commercial",
        "lead": "Austin's commercial real estate market moves quickly — from new Class A office in the Domain to flex space in East Austin and tech campuses along Mopac. We bring the operational rigor expected by enterprise tenants.",
        "why": "We staff and supervise programs across Austin's busiest corporate corridors, with documented routes and a single accountable account manager per property.",
        "hero_image": "tech-facility.jpg",
        "metro_keywords": "Austin, Travis County, the Domain, East Austin, downtown Austin, Mopac corridor, Williamson County",
    },
    {
        "slug": "round-rock",
        "name": "Round Rock",
        "region": "Austin Metro / Williamson County",
        "metro": "Austin metro",
        "districts": "the I-35 corridor, La Frontera, the Round Rock Premium Outlets area, and the Dell Diamond / Kalahari corridor",
        "industries": "technology manufacturing, distribution, healthcare, retail, and corporate headquarters",
        "lead": "Round Rock has become one of Texas's most active commercial growth corridors. From Dell's footprint to new distribution and tech operations along I-35, we deliver facility services tuned for high-volume, high-standard environments.",
        "why": "Manufacturing and distribution centers in Round Rock need consistent industrial cleaning, floor care, and pressure-wash programs. Our crews are scoped and supervised for those operating conditions.",
        "hero_image": "warehouse.jpg",
        "metro_keywords": "Round Rock, Williamson County, La Frontera, I-35 corridor, Dell Diamond area",
    },
    {
        "slug": "cedar-park",
        "name": "Cedar Park",
        "region": "Austin Metro / Williamson County",
        "metro": "Austin metro",
        "districts": "Whitestone Boulevard, the 1431 corridor, Bell Boulevard, and the Parmer Lane tech belt",
        "industries": "technology, healthcare, multi-tenant office, retail, and light industrial",
        "lead": "Cedar Park's growth along Parmer Lane and Whitestone has brought new corporate campuses, medical buildings, and multi-tenant properties. We provide disciplined, documented facility services across that footprint.",
        "why": "Cedar Park's mixed-use commercial inventory benefits from a single accountable vendor that can scope janitorial, floor care, and maintenance under one program.",
        "hero_image": "office-interior.jpg",
        "metro_keywords": "Cedar Park, Williamson County, Parmer Lane, Whitestone Boulevard, 1431 corridor",
    },
    {
        "slug": "pflugerville",
        "name": "Pflugerville",
        "region": "Austin Metro / Travis County",
        "metro": "Austin metro",
        "districts": "the SH-130 corridor, Stone Hill, Heatherwilde, and the Pecan Street industrial belt",
        "industries": "distribution and logistics, advanced manufacturing, technology, and corporate office",
        "lead": "Pflugerville is a critical distribution and manufacturing hub along the SH-130 corridor. We deliver industrial-grade janitorial, floor restoration, and pressure-wash programs scaled for facilities operating at volume.",
        "why": "Logistics and manufacturing operators in Pflugerville need vendors that show up on schedule with documented procedures. That is how we run every account.",
        "hero_image": "industrial.jpg",
        "metro_keywords": "Pflugerville, Travis County, SH-130 corridor, Stone Hill, Heatherwilde",
    },
    {
        "slug": "georgetown",
        "name": "Georgetown",
        "region": "Austin Metro / Williamson County",
        "metro": "Austin metro",
        "districts": "the historic downtown square, Wolf Ranch, the Sun City corridor, and the I-35 commercial belt",
        "industries": "healthcare, professional services, retail, education, and corporate office",
        "lead": "Georgetown's mix of historic downtown commercial, growing medical office, and new corporate campuses calls for a contractor that adapts standards by property type. We do.",
        "why": "From medical office to retail center maintenance, we deliver a consistent, supervised program across the Georgetown commercial footprint.",
        "hero_image": "medical-facility.jpg",
        "metro_keywords": "Georgetown, Williamson County, Wolf Ranch, Sun City, downtown Georgetown square",
    },
    {
        "slug": "san-marcos",
        "name": "San Marcos",
        "region": "Austin / San Antonio Corridor",
        "metro": "I-35 corridor",
        "districts": "the Texas State University area, the Premium Outlets, the Centerpoint Road industrial belt, and downtown",
        "industries": "higher education, retail, distribution, and corporate office",
        "lead": "San Marcos sits at the center of the Austin–San Antonio I-35 corridor. We provide commercial facility services for educational, retail, and industrial properties operating in that fast-growing market.",
        "why": "We scope and supervise programs across the I-35 corridor with crews that operate to the same documented standards in San Marcos that we apply in Austin and San Antonio.",
        "hero_image": "educational.jpg",
        "metro_keywords": "San Marcos, Hays County, Texas State University area, I-35 corridor",
    },
    {
        "slug": "new-braunfels",
        "name": "New Braunfels",
        "region": "South Central Texas / Comal County",
        "metro": "Austin–San Antonio corridor",
        "districts": "the I-35 industrial corridor, downtown New Braunfels, and the Creekside / FM 306 commercial belts",
        "industries": "manufacturing, distribution, hospitality, healthcare, and corporate office",
        "lead": "New Braunfels is one of the fastest-growing commercial markets in Texas. Manufacturing, distribution, and hospitality operators here need facility programs that match the pace.",
        "why": "Industrial and hospitality clients in New Braunfels rely on us for documented routes, supervised crews, and predictable scope across multiple shifts.",
        "hero_image": "industrial.jpg",
        "metro_keywords": "New Braunfels, Comal County, I-35 industrial corridor, Creekside",
    },
    {
        "slug": "dallas",
        "name": "Dallas",
        "region": "North Texas / DFW",
        "metro": "DFW metroplex",
        "districts": "downtown, Uptown, the Galleria, the Stemmons / I-35E corridor, Las Colinas, and the Dallas Design District",
        "industries": "financial services, corporate headquarters, healthcare, technology, and multi-tenant office",
        "lead": "Dallas runs on Class A office, corporate campuses, and a deep industrial belt. We deliver facility programs scaled for portfolios that span downtown, Uptown, and the surrounding submarkets.",
        "why": "Dallas property managers expect documented programs, accountable supervisors, and consistent crew performance across multiple buildings. That is how we operate every account.",
        "hero_image": "hero-office-tower.jpg",
        "metro_keywords": "Dallas, Dallas County, downtown Dallas, Uptown, Galleria, Stemmons corridor, Design District",
    },
    {
        "slug": "fort-worth",
        "name": "Fort Worth",
        "region": "North Texas / DFW",
        "metro": "DFW metroplex",
        "districts": "downtown, the Cultural District, Alliance, the Stockyards corridor, and the West 7th business district",
        "industries": "aerospace and defense, energy, healthcare, logistics, and corporate office",
        "lead": "From Alliance industrial to downtown Class A and the medical district, Fort Worth's commercial properties require a contractor that operates across very different facility types with the same standard.",
        "why": "We supervise programs across Fort Worth's most active corridors with named account managers and documented routes per property.",
        "hero_image": "corporate-interior.jpg",
        "metro_keywords": "Fort Worth, Tarrant County, Alliance, downtown Fort Worth, Cultural District, West 7th",
    },
    {
        "slug": "plano",
        "name": "Plano",
        "region": "North Texas / DFW",
        "metro": "DFW metroplex",
        "districts": "Legacy West, the Dallas North Tollway corridor, Granite Park, the Shops at Legacy, and Plano's corporate campuses",
        "industries": "technology, financial services, telecommunications, corporate headquarters, and Class A office",
        "lead": "Plano hosts more Fortune 500 footprint per square mile than most North Texas cities. Corporate campuses here demand vendors who behave like operators, not contractors.",
        "why": "Legacy West tenants and the broader Plano corporate corridor run on documented programs and accountable supervision. That is our standard.",
        "hero_image": "tech-facility.jpg",
        "metro_keywords": "Plano, Collin County, Legacy West, Dallas North Tollway, Granite Park",
    },
    {
        "slug": "frisco",
        "name": "Frisco",
        "region": "North Texas / DFW",
        "metro": "DFW metroplex",
        "districts": "The Star, Frisco Station, the Dallas North Tollway, Hall Park, and the Stonebriar area",
        "industries": "sports and entertainment, corporate headquarters, healthcare, technology, and multi-tenant office",
        "lead": "Frisco's growth has produced some of the country's most ambitious mixed-use developments — from The Star to Frisco Station. Facility standards here are set by the tenants, and we meet them.",
        "why": "From corporate offices in Hall Park to medical and entertainment properties, we deliver a single, supervised facility program per portfolio.",
        "hero_image": "office-interior.jpg",
        "metro_keywords": "Frisco, Collin County, The Star, Frisco Station, Dallas North Tollway, Hall Park",
    },
    {
        "slug": "arlington",
        "name": "Arlington",
        "region": "North Texas / DFW",
        "metro": "DFW metroplex",
        "districts": "the Entertainment District, the Great Southwest Industrial District, and the I-30 / I-20 corridors",
        "industries": "sports and entertainment, distribution, manufacturing, healthcare, and corporate office",
        "lead": "Arlington sits at the center of DFW's logistics and entertainment economy. Distribution operators and stadium-adjacent commercial properties need consistent, documented service.",
        "why": "Our crews are scoped for both high-volume industrial cleaning in the Great Southwest district and Class A maintenance in Arlington's corporate corridors.",
        "hero_image": "warehouse.jpg",
        "metro_keywords": "Arlington, Tarrant County, Entertainment District, Great Southwest Industrial District, I-30 corridor",
    },
    {
        "slug": "irving",
        "name": "Irving",
        "region": "North Texas / DFW",
        "metro": "DFW metroplex",
        "districts": "Las Colinas, the DFW Airport corridor, the Urban Center, and the SH-114 office belt",
        "industries": "corporate headquarters, financial services, technology, hospitality, and Class A office",
        "lead": "Las Colinas and the Irving SH-114 corridor host some of the largest corporate campuses in North Texas. We deliver documented facility programs for those tenants and their landlords.",
        "why": "Property managers across Las Colinas and the Airport corridor benefit from a single accountable contractor handling janitorial, floor restoration, and maintenance in one supervised program.",
        "hero_image": "office-meeting.jpg",
        "metro_keywords": "Irving, Dallas County, Las Colinas, DFW Airport corridor, SH-114, Urban Center",
    },
    {
        "slug": "houston",
        "name": "Houston",
        "region": "Southeast Texas / Gulf Coast",
        "metro": "Houston metro",
        "districts": "downtown, the Energy Corridor, the Galleria / Uptown, the Texas Medical Center, Westchase, and Greenway Plaza",
        "industries": "energy, healthcare, petrochemical, logistics, professional services, and Class A office",
        "lead": "From the Energy Corridor to the Texas Medical Center, Houston's commercial footprint is one of the largest and most demanding in the country. We deliver facility services scoped for that scale.",
        "why": "Houston's medical, energy, and corporate properties run on uncompromising standards. We staff, train, and supervise crews accordingly.",
        "hero_image": "medical-facility.jpg",
        "metro_keywords": "Houston, Harris County, Energy Corridor, Galleria, Uptown Houston, Texas Medical Center, Westchase, Greenway Plaza",
    },
]

# Service catalog — same 12 services used everywhere else on the site
SERVICES = [
    ("Commercial Janitorial Services", "Recurring nightly, daytime, or shift-based janitorial programs scoped to your facility class.", "M3 12l3-3 4 4 6-8 5 5"),
    ("Office Cleaning", "Disciplined office cleaning routines that protect tenant experience and asset value.", "M3 21h18M5 21V8l7-5 7 5v13"),
    ("Day Porter Services", "On-site day porters who handle restrooms, lobby presentation, spill response, and tenant requests.", "M12 2a5 5 0 1 0 0 10 5 5 0 0 0 0-10zM4 22a8 8 0 0 1 16 0"),
    ("Carpet Cleaning", "Hot-water extraction, encapsulation, and spot programs for corporate carpet inventories.", "M3 6h18M3 12h18M3 18h18"),
    ("VCT Floor Stripping & Waxing", "Strip, scrub, and refinish programs that restore VCT, vinyl, and resilient floors.", "M3 12s4-7 9-7 9 7 9 7-4 7-9 7-9-7-9-7z"),
    ("Epoxy Floor Coatings", "Industrial-grade epoxy systems for warehouses, manufacturing, and back-of-house surfaces.", "M3 21h18M3 17h18M5 17l3-9 4 6 4-9 3 12"),
    ("Concrete Staining", "Decorative and architectural concrete staining for showrooms, lobbies, and feature spaces.", "M4 4h16v16H4z M8 4v16 M16 4v16"),
    ("Interior Painting", "Commercial interior repaint programs scoped for occupied buildings on documented schedules.", "M3 21l9-9 4 4-9 9H3v-4z M14 7l4-4 3 3-4 4"),
    ("Pressure Washing", "Exterior pressure-wash programs for storefronts, sidewalks, loading docks, and parking structures.", "M3 18c3-2 6-2 9 0s6 2 9 0 M3 12c3-2 6-2 9 0s6 2 9 0 M3 6c3-2 6-2 9 0s6 2 9 0"),
    ("Post-Construction Cleanup", "Final clean, rough clean, and turnover programs for general contractors and owner reps.", "M3 21h18 M6 21V11l6-5 6 5v10 M9 21v-6h6v6"),
    ("Facility Maintenance", "Recurring maintenance routines that protect the building envelope and reduce reactive spend.", "M14 6l2-2 4 4-2 2 M14 6l-7 7-3 7 7-3 7-7"),
    ("Disinfection Services", "Disinfection programs for medical, educational, and high-traffic commercial environments.", "M12 2a8 8 0 1 0 0 16 8 8 0 0 0 0-16z M9 12l2 2 4-4"),
]


# Header / footer chrome shared with the rest of the site. We render this with
# the .active flag on the Locations link.
def header_html():
    return """
<header class="header">
  <div class="container">
    <a href="index.html" class="brand">
      <img src="images/logo.webp?v=4" alt="Hill Country Facility Services" />
      <span class="brand-text">
        <span class="b1">Hill Country</span>
        <span class="b2">Facility Services</span>
      </span>
    </a>
    <nav class="nav" aria-label="Primary">
      <a href="index.html">Home</a>
      <a href="about.html">About</a>
      <a href="services.html">Services</a>
      <a href="industries.html">Industries</a>
      <div class="nav-drop">
        <a href="locations.html" class="active">Locations <svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg></a>
        <div class="nav-drop-menu">
          __DROPDOWN_LINKS__
        </div>
      </div>
      <a href="careers.html">Careers</a>
      <a href="contact.html">Contact</a>
      <a href="contact.html#quote" class="btn btn-primary">Request Quote
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </a>
    </nav>
    <button class="menu-btn" aria-label="Menu" aria-expanded="false">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
    </button>
  </div>
</header>
"""


def dropdown_links():
    # Group cities by metro for the dropdown
    groups = {
        "San Antonio": ["san-antonio", "new-braunfels"],
        "Austin Metro": ["austin", "round-rock", "cedar-park", "pflugerville", "georgetown", "san-marcos"],
        "DFW Metroplex": ["dallas", "fort-worth", "plano", "frisco", "arlington", "irving"],
        "Houston": ["houston"],
    }
    parts = []
    for group_name, slugs in groups.items():
        parts.append(f'<div class="nav-drop-group"><div class="nav-drop-label">{group_name}</div>')
        for slug in slugs:
            city = next(c for c in CITIES if c["slug"] == slug)
            parts.append(f'<a href="locations/{slug}.html">{city["name"]}</a>')
        parts.append('</div>')
    parts.append('<div class="nav-drop-group"><a href="locations.html" class="nav-drop-all">View all locations →</a></div>')
    return "\n          ".join(parts)


def footer_html(prefix=""):
    """Footer rendered for the city pages. prefix is '../' when emitted from /locations/<slug>.html so relative links still work."""
    # Top-level city links grouped
    austin = ["austin", "round-rock", "cedar-park", "pflugerville", "georgetown", "san-marcos"]
    dfw = ["dallas", "fort-worth", "plano", "frisco", "arlington", "irving"]
    south = ["san-antonio", "new-braunfels"]
    houston = ["houston"]

    def make_links(slugs):
        return "".join(f'<li><a href="{prefix}locations/{s}.html">{next(c for c in CITIES if c["slug"]==s)["name"]}</a></li>' for s in slugs)

    return f"""
<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="{prefix}images/logo.webp?v=4" alt="Hill Country Facility Services" />
        <p>Premium commercial facility services for office, industrial, medical, educational, and multi-tenant properties across Texas.</p>
        <div class="badges">
          <span class="badge-pill">Licensed</span>
          <span class="badge-pill">Insured</span>
          <span class="badge-pill">OSHA Trained</span>
        </div>
      </div>
      <div class="footer-col">
        <h4>Company</h4>
        <ul>
          <li><a href="{prefix}about.html">About Us</a></li>
          <li><a href="{prefix}services.html">Services</a></li>
          <li><a href="{prefix}industries.html">Industries</a></li>
          <li><a href="{prefix}careers.html">Careers</a></li>
          <li><a href="{prefix}contact.html">Contact</a></li>
        </ul>
      </div>
      <div class="footer-col footer-locations">
        <h4>Locations</h4>
        <div class="footer-loc-group"><span class="footer-loc-label">Austin Metro</span><ul>{make_links(austin)}</ul></div>
        <div class="footer-loc-group"><span class="footer-loc-label">DFW</span><ul>{make_links(dfw)}</ul></div>
        <div class="footer-loc-group"><span class="footer-loc-label">South Central</span><ul>{make_links(south)}</ul></div>
        <div class="footer-loc-group"><span class="footer-loc-label">Gulf Coast</span><ul>{make_links(houston)}</ul></div>
        <a href="{prefix}locations.html" class="footer-loc-all">View all locations →</a>
      </div>
      <div class="footer-col footer-contact">
        <h4>Contact</h4>
        <div class="row">
          <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
          <div>Headquartered in the<br/>Texas Hill Country</div>
        </div>
        <div class="row">
          <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
          <div>(512) 893-4012<br/><span style="opacity:0.6">24/7 dispatch</span></div>
        </div>
        <div class="row">
          <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><path d="M22 6l-10 7L2 6"/></svg>
          <div>Contact@hillcountryfacilityservices.com</div>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <div>© <span data-year>2026</span> Hill Country Facility Services LLC. All rights reserved.</div>
      <div class="footer-bottom-links">
        <a href="#">Privacy</a>
        <a href="#">Terms</a>
        <a href="#">Accessibility</a>
      </div>
    </div>
  </div>
</footer>
<script src="{prefix}js/main.js"></script>
</body>
</html>
"""


# ---------- City page template ----------
def city_page(city):
    name = city["name"]
    slug = city["slug"]
    services_grid = "\n".join(
        f'''<div class="service-card reveal">
          <span class="num">{i+1:02d}</span>
          <h3>{title}</h3>
          <p>{desc}</p>
          <a class="svc-cta" href="../services.html">Learn more <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg></a>
        </div>''' for i, (title, desc, _ico) in enumerate(SERVICES)
    )

    head_keywords = (
        f"commercial cleaning {name}, janitorial services {name}, "
        f"facility services {name}, office cleaning {name}, "
        f"floor stripping waxing {name}, epoxy coatings {name}, "
        f"post-construction cleanup {name}, {city['metro_keywords']}"
    )

    schema = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Hill Country Facility Services — {name}",
  "image": "https://hillcountryfacilityservices.com/images/logo-full.png",
  "description": "Commercial janitorial, floor restoration, epoxy coatings, and facility maintenance services for {name} commercial properties.",
  "telephone": "+1-512-893-4012",
  "email": "Contact@hillcountryfacilityservices.com",
  "areaServed": {{
    "@type": "City",
    "name": "{name}",
    "containedInPlace": "Texas"
  }},
  "address": {{
    "@type": "PostalAddress",
    "addressRegion": "TX",
    "addressCountry": "US"
  }},
  "priceRange": "$$"
}}
</script>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Commercial Facility Services in {name}, TX — Hill Country Facility Services</title>
<meta name="description" content="Commercial janitorial, floor restoration, epoxy coatings, and facility maintenance services for {name} commercial properties. Serving office, medical, industrial, and multi-tenant facilities across {city['region']}." />
<meta name="keywords" content="{head_keywords}" />
<meta property="og:title" content="Commercial Facility Services in {name}, TX — Hill Country Facility Services" />
<meta property="og:description" content="Disciplined janitorial, floor restoration, and facility maintenance programs for {name} commercial properties." />
<meta property="og:type" content="website" />
<link rel="canonical" href="https://hillcountryfacilityservices.com/locations/{slug}.html" />
<link rel="icon" type="image/png" href="../images/logo-full.png?v=2" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300;9..144,400;9..144,500&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="../css/styles.css" />
{schema}
</head>
<body>

{header_html().replace('__DROPDOWN_LINKS__', dropdown_links()).replace('href="index.html"', 'href="../index.html"').replace('href="about.html"', 'href="../about.html"').replace('href="services.html"', 'href="../services.html"').replace('href="industries.html"', 'href="../industries.html"').replace('href="careers.html"', 'href="../careers.html"').replace('href="contact.html"', 'href="../contact.html"').replace('href="locations.html"', 'href="../locations.html"').replace('href="locations/', 'href="').replace('src="images/', 'src="../images/')}

<section class="page-hero">
  <div class="page-hero-bg"><img src="../images/{city['hero_image']}" alt="" /></div>
  <div class="container">
    <div class="crumbs"><a href="../index.html">Home</a><span class="sep">/</span><a href="../locations.html">Locations</a><span class="sep">/</span><span>{name}</span></div>
    <h1>Commercial Facility Services <span class="alt">in {name}.</span></h1>
    <p>{city['lead']}</p>
  </div>
</section>

<section class="intro">
  <div class="container">
    <div class="intro-grid">
      <div class="intro-text reveal">
        <div class="eyebrow">Serving {name}, TX</div>
        <h2>One contractor. One standard. <span class="alt">Across {city['metro']}.</span></h2>
        <p>{city['why']} We serve {city['districts']}.</p>
        <p>Our {name} client base operates across {city['industries']}. We scope each program to the building type, traffic pattern, and compliance profile of the facility — and we put a named account manager on every property.</p>
        <div class="intro-ctas">
          <a href="../contact.html#quote" class="btn btn-primary">Request a {name} Proposal
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
          <a href="../services.html" class="btn btn-ghost">View All Services</a>
        </div>
      </div>
      <div class="intro-meta reveal">
        <div class="meta-card">
          <div class="meta-row"><span class="meta-label">Service Area</span><span class="meta-value">{name} &amp; {city['metro']}</span></div>
          <div class="meta-row"><span class="meta-label">Direct Line</span><span class="meta-value">(512) 893-4012</span></div>
          <div class="meta-row"><span class="meta-label">Dispatch</span><span class="meta-value">24/7</span></div>
          <div class="meta-row"><span class="meta-label">Coverage</span><span class="meta-value">{city['region']}</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="services" id="services">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">Services in {name}</div>
      <h2>A full commercial catalog, delivered <span class="alt">locally.</span></h2>
      <p>Every service we offer is available across {name} and surrounding {city['metro']} markets — supervised by the same operations team, on documented routes.</p>
    </div>
    <div class="services-grid">
      {services_grid}
    </div>
  </div>
</section>

<section class="cta">
  <div class="cta-bg"><img src="../images/hero-office-tower.jpg" alt="" /></div>
  <div class="container">
    <div class="cta-inner">
      <div class="reveal">
        <div class="eyebrow">{name}, TX</div>
        <h2>Ready to scope a program in <span class="alt">{name}?</span></h2>
        <p>Tell us about your {name} portfolio. Our team will follow up to schedule a walk-through and build a scoped proposal.</p>
      </div>
      <div class="cta-actions reveal">
        <a href="../contact.html#quote" class="btn btn-primary">Request a {name} Proposal
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </a>
        <a href="../services.html" class="btn btn-outline-light">View Capabilities</a>
      </div>
      <div class="cta-phone reveal">
        <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
        Direct dispatch: <strong>(512) 893-4012</strong>
      </div>
    </div>
  </div>
</section>

{footer_html(prefix='../')}
"""


# ---------- Locations index page ----------
def locations_index():
    tx_map_svg = Path("/home/user/workspace/hcfs/images/texas-map.svg").read_text()
    groups = [
        ("Austin Metro", ["austin", "round-rock", "cedar-park", "pflugerville", "georgetown", "san-marcos"]),
        ("DFW Metroplex", ["dallas", "fort-worth", "plano", "frisco", "arlington", "irving"]),
        ("South Central Texas", ["san-antonio", "new-braunfels"]),
        ("Gulf Coast", ["houston"]),
    ]
    cards = []
    for group_name, slugs in groups:
        items = []
        for s in slugs:
            c = next(x for x in CITIES if x["slug"] == s)
            items.append(f'''<a href="locations/{s}.html" class="loc-card reveal">
              <h3>{c["name"]}</h3>
              <p>{c["region"]}</p>
              <span class="loc-cta">Services in {c["name"]} <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg></span>
            </a>''')
        cards.append(f'''<div class="loc-group">
          <div class="loc-group-head reveal">
            <div class="eyebrow">Region</div>
            <h2>{group_name}</h2>
          </div>
          <div class="loc-grid">
            {''.join(items)}
          </div>
        </div>''')

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Locations We Serve — Hill Country Facility Services</title>
<meta name="description" content="Commercial facility services across San Antonio, Austin, DFW, Houston, and surrounding Texas markets. Janitorial, floor restoration, epoxy coatings, and facility maintenance." />
<meta property="og:title" content="Locations We Serve — Hill Country Facility Services" />
<meta property="og:description" content="Commercial facility services across San Antonio, Austin, DFW, Houston, and surrounding Texas markets." />
<meta property="og:type" content="website" />
<link rel="canonical" href="https://hillcountryfacilityservices.com/locations.html" />
<link rel="icon" type="image/png" href="images/logo-full.png?v=2" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300;9..144,400;9..144,500&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="css/styles.css" />
</head>
<body>

{header_html().replace('__DROPDOWN_LINKS__', dropdown_links())}

<section class="page-hero">
  <div class="page-hero-bg"><img src="images/hero-office-tower.jpg" alt="" /></div>
  <div class="container">
    <div class="crumbs"><a href="index.html">Home</a><span class="sep">/</span><span>Locations</span></div>
    <h1>Texas commercial markets <span class="alt">we serve.</span></h1>
    <p>From San Antonio to Houston and DFW, we deliver disciplined janitorial, floor restoration, and facility maintenance programs to commercial properties across Texas's most active corridors.</p>
  </div>
</section>

<section class="map-section">
  <div class="container">
    <div class="map-head reveal">
      <span class="eyebrow">Service Area</span>
      <h2>Statewide reach, <span class="alt">metro-level depth.</span></h2>
      <p>Four major Texas metros. Fifteen cities. One supervised, accountable service program.</p>
    </div>
    <div class="map-wrap reveal">
      {tx_map_svg}
      <div class="map-legend">
        <div class="legend-item"><span class="legend-dot legend-dot-primary"></span> Primary Metro</div>
        <div class="legend-item"><span class="legend-dot legend-dot-secondary"></span> Service Area City</div>
        <div class="legend-stat"><span>15</span> cities served</div>
      </div>
    </div>
  </div>
</section>

<section class="locations">
  <div class="container">
    {''.join(cards)}
  </div>
</section>

<section class="cta">
  <div class="cta-bg"><img src="images/corporate-interior.jpg" alt="" /></div>
  <div class="container">
    <div class="cta-inner">
      <div class="reveal">
        <div class="eyebrow">Statewide capability</div>
        <h2>Don't see your <span class="alt">market?</span></h2>
        <p>We support multi-site commercial portfolios across Texas. If your operation spans cities, we can scope a single, supervised program across all of them.</p>
      </div>
      <div class="cta-actions reveal">
        <a href="contact.html#quote" class="btn btn-primary">Request a Multi-Site Proposal
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </a>
        <a href="services.html" class="btn btn-outline-light">View Capabilities</a>
      </div>
    </div>
  </div>
</section>

{footer_html(prefix='')}
"""


def main():
    base = os.path.dirname(os.path.abspath(__file__))
    locations_dir = os.path.join(base, 'locations')
    os.makedirs(locations_dir, exist_ok=True)

    # Per-city pages
    for city in CITIES:
        path = os.path.join(locations_dir, f"{city['slug']}.html")
        with open(path, 'w') as f:
            f.write(city_page(city))
        print('wrote', path)

    # Locations index
    idx = os.path.join(base, 'locations.html')
    with open(idx, 'w') as f:
        f.write(locations_index())
    print('wrote', idx)


if __name__ == '__main__':
    main()
