#!/usr/bin/env python3
"""Generate the 5 inner pages."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_pages import page

# =============================================================
# ABOUT
# =============================================================
ABOUT_BODY = """
<section class="page-hero">
  <div class="page-hero-bg"><img src="images/about-hero.jpg" alt="" /></div>
  <div class="container">
    <div class="crumbs"><a href="index.html">Home</a><span class="sep">/</span><span>About</span></div>
    <h1>A growth-oriented commercial <span class="alt">facility partner.</span></h1>
    <p>Hill Country Facility Services LLC is a Texas-based commercial facility services contractor built to support large, multi-property portfolios with the operational discipline enterprise clients expect.</p>
  </div>
</section>

<section class="intro">
  <div class="container">
    <div class="intro-grid">
      <div class="intro-text reveal">
        <span class="eyebrow">Our Company</span>
        <h2>Engineered for commercial scale, <span class="alt">accountable in every detail.</span></h2>
        <p class="lede">We exist to be the commercial facility partner that property managers and facility executives can trust with their most demanding portfolios.</p>
        <p>From the day we mobilize an account, we operate to documented standards: site books, scoped SOPs, supervisor walk-throughs, and light-touch check-ins by email or call &mdash; whichever the client prefers. We don't sell cleaning &mdash; we sell operational reliability.</p>
        <p>Our service model is intentionally focused on commercial environments. We do not chase residential, single-storefront, or one-off retail work. That focus is what allows us to deliver the consistency, compliance posture, and supervisory depth that enterprise clients require.</p>
      </div>
      <div class="intro-visual reveal">
        <img src="images/team-meeting.jpg" alt="Hill Country Facility Services leadership team in working session" />
        <div class="badge">
          <span class="dot"></span>
          <span class="txt">Building <strong>long-term commercial partnerships</strong></span>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="services">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Our Operating Principles</span>
      <h2>Five disciplines that define how we operate.</h2>
    </div>
    <div class="services-grid reveal-stagger">
      <article class="service-card">
        <span class="num">01</span>
        <div class="service-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 3v18h18"/><path d="M7 14l4-4 4 4 5-6"/></svg></div>
        <h3>Operationally Structured</h3>
        <p>Every account runs on documented SOPs, site books, and a recurring quality cadence &mdash; not crew habit.</p>
      </article>
      <article class="service-card">
        <span class="num">02</span>
        <div class="service-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><path d="M8 12l3 3 5-6"/></svg></div>
        <h3>Reliability First</h3>
        <p>Show up. Do the work. Report the result. The simplest commitment, and the hardest to deliver consistently.</p>
      </article>
      <article class="service-card">
        <span class="num">03</span>
        <div class="service-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 12h18M3 6h18M3 18h12"/></svg></div>
        <h3>Scalable Infrastructure</h3>
        <p>Routing, supervision, and quality programs that scale from a single property to a 50-site portfolio.</p>
      </article>
      <article class="service-card">
        <span class="num">04</span>
        <div class="service-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 2l9 4v6c0 5-4 9-9 10-5-1-9-5-9-10V6l9-4z"/></svg></div>
        <h3>Compliance &amp; Safety</h3>
        <p>Insurance, OSHA training, and E-Verify documentation maintained.</p>
      </article>
      <article class="service-card">
        <span class="num">05</span>
        <div class="service-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/></svg></div>
        <h3>Long-Term Partnership</h3>
        <p>We invest in account managers and supervisors so our client relationships are measured in years, not contracts.</p>
      </article>
      <article class="service-card">
        <span class="num">06</span>
        <div class="service-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 21l9-18 9 18M7 14h10"/></svg></div>
        <h3>Growth-Oriented</h3>
        <p>A company built to grow with its clients &mdash; new properties, new service lines, new geographies.</p>
      </article>
    </div>
  </div>
</section>

<section class="counters">
  <div class="container">
    <div class="counters-grid">
      <div class="counter">
        <div class="counter-num"><span class="num" data-target="2.4" data-decimals="1">0</span><span class="suffix">M</span></div>
        <div class="counter-label">Sq Ft Serviced Weekly</div>
        <div class="counter-line"></div>
      </div>
      <div class="counter">
        <div class="counter-num"><span class="num" data-target="180" data-decimals="0">0</span><span class="suffix">+</span></div>
        <div class="counter-label">Commercial Accounts</div>
        <div class="counter-line"></div>
      </div>
      <div class="counter">
        <div class="counter-num"><span class="num" data-target="8" data-decimals="0">0</span><span class="suffix"></span></div>
        <div class="counter-label">Verticals Served</div>
        <div class="counter-line"></div>
      </div>
      <div class="counter">
        <div class="counter-num"><span class="num" data-target="98" data-decimals="0">0</span><span class="suffix">%</span></div>
        <div class="counter-label">Account Retention</div>
        <div class="counter-line"></div>
      </div>
    </div>
  </div>
</section>

<section class="cta">
  <div class="cta-bg"><img src="images/handshake.jpg" alt="" /></div>
  <div class="container">
    <div class="cta-inner">
      <div class="reveal">
        <span class="eyebrow">Talk to Our Team</span>
        <h2>Let's build a <span class="alt">long-term partnership.</span></h2>
        <p>Reach out for a discovery conversation. We'll walk your property, scope the work, and propose a structured service program.</p>
      </div>
      <div class="cta-actions reveal">
        <a href="contact.html#quote" class="btn btn-primary">Request a Proposal
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </a>
        <a href="services.html" class="btn btn-outline-light">View Services</a>
      </div>
    </div>
  </div>
</section>
"""

# =============================================================
# SERVICES
# =============================================================
SERVICES = [
    ("janitorial","Commercial Janitorial Services","Recurring, scope-based janitorial programs for commercial properties of every size — built on documented SOPs, supervisor-led walks, and monthly quality audits.","M3 21h18M5 21V7l7-4 7 4v14M9 9h.01M9 13h.01M9 17h.01M15 9h.01M15 13h.01M15 17h.01"),
    ("office","Office Cleaning","Daily, evening, and weekend office cleaning calibrated to corporate environments, tenant standards, and after-hours access protocols.","M3 4h18v14H3z M3 18l4-4 4 4 M11 14l4-4 4 4"),
    ("dayporter","Day Porter Services","On-site daytime presence covering lobbies, restrooms, common areas, conference rooms, and tenant-facing presentation through business hours.","M12 2v20M2 12h20"),
    ("carpet","Carpet Cleaning","Hot-water extraction, encapsulation, traffic-lane treatment, and emergency spot response for commercial carpet of every soil category.","M3 20h18M5 20V8h14v12M8 8V4h8v4"),
    ("vct","VCT Floor Stripping & Waxing","Full strip-and-recoat cycles, scrub-and-recoat programs, and burnishing to restore VCT to a durable, high-gloss commercial finish.","M3 12h18M3 6h18M3 18h18M7 3v18M17 3v18"),
    ("epoxy","Epoxy Floor Coatings","Industrial-grade epoxy systems engineered for warehouses, manufacturing floors, and back-of-house commercial environments.","M2 18l5-5 4 4 5-5 6 6M2 18v3h20v-3"),
    ("concrete","Concrete Staining","Polished and stained concrete finishes that deliver an upscale aesthetic with minimal lifecycle maintenance for retail anchors and corporate floors.","M3 3h18v18H3z M3 9h18 M9 21V9 M15 21V9"),
    ("painting","Interior Painting","Commercial interior repainting scheduled around tenant operations, with low-VOC, durable wall systems suited to high-traffic commercial spaces.","M3 21l9-18 9 18M7 14h10"),
    ("pressure","Pressure Washing","Exterior pressure washing for sidewalks, building façades, parking structures, dumpster pads, and loading-dock areas.","M12 2v6M12 22v-4M4 12H2M22 12h-2M5 5l2 2M17 17l2 2M5 19l2-2M17 7l2-2"),
    ("postconstruction","Post-Construction Cleanup","Rough, final, and white-glove post-construction cleaning programs that deliver a turnover-ready space for general contractors and owners.","M2 20h20M5 20V8l4-3 6 5v10M19 20v-7l-3-2"),
    ("maintenance","Facility Maintenance","General upkeep, light repairs, and recurring maintenance programs designed to extend asset lifecycle and reduce reactive spend.","M12 2v20M4 6l16 12M4 18L20 6"),
    ("disinfection","Disinfection Services","EPA-registered disinfection programs for high-touch surfaces, medical environments, and rapid post-incident response.","M12 2l9 4v6c0 5-4 9-9 10-5-1-9-5-9-10V6l9-4z M9 12l2 2 4-4"),
]

SERVICES_BODY = """
<section class="page-hero">
  <div class="page-hero-bg"><img src="images/floor-polish.jpg" alt="" /></div>
  <div class="container">
    <div class="crumbs"><a href="index.html">Home</a><span class="sep">/</span><span>Services</span></div>
    <h1>A complete commercial <span class="alt">service catalog.</span></h1>
    <p>Twelve disciplined capabilities delivered by a single, accountable contractor — so your portfolio runs on one vendor, one standard, one point of contact.</p>
  </div>
</section>

<section class="services">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Our Capabilities</span>
      <h2>Every service we deliver, end to end.</h2>
      <p>Click any service to learn how we approach it on commercial accounts.</p>
    </div>
    <div class="services-grid reveal-stagger">
"""
for i, (sid, title, desc, path) in enumerate(SERVICES, start=1):
    SERVICES_BODY += f"""
      <article class="service-card" id="{sid}">
        <span class="num">{i:02d}</span>
        <div class="service-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="{path}"/></svg></div>
        <h3>{title}</h3>
        <p>{desc}</p>
      </article>
"""
SERVICES_BODY += """
    </div>
  </div>
</section>

<section class="whyus">
  <div class="container">
    <div class="whyus-grid">
      <div class="whyus-text reveal">
        <span class="eyebrow">How We Deliver</span>
        <h2>A consistent operating model <span class="alt">across every service.</span></h2>
        <p>Our service lines are different. Our discipline is not. Every account runs through the same operational architecture.</p>
        <div class="whyus-list">
          <div class="whyus-item">
            <div class="ico"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M9 13h6M9 17h6M9 9h2"/></svg></div>
            <div><h4>Scoped Proposal</h4><p>Every engagement starts with a walk-through and a written scope of work tailored to the property.</p></div>
          </div>
          <div class="whyus-item">
            <div class="ico"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="8" r="5"/><path d="M5 21v-2a4 4 0 0 1 4-4h6a4 4 0 0 1 4 4v2"/></svg></div>
            <div><h4>Mobilization Plan</h4><p>Documented onboarding with site book, SOPs, supervisor introductions, and access protocols.</p></div>
          </div>
          <div class="whyus-item">
            <div class="ico"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 3v18h18"/><path d="M7 14l4-4 4 4 5-6"/></svg></div>
            <div><h4>Quality Cadence</h4><p>Routine inspections, corrective action plans, and light-touch check-ins on the client's preferred channel.</p></div>
          </div>
          <div class="whyus-item">
            <div class="ico"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg></div>
            <div><h4>Transparent Reporting</h4><p>Photo audits and named accountability on both sides.</p></div>
          </div>
        </div>
      </div>
      <div class="whyus-visual reveal">
        <div class="whyus-img">
          <img src="images/cleaning-pro.jpg" alt="Commercial cleaning crew" />
        </div>
        <div class="whyus-stat">
          <div class="num">12</div>
          <div class="lbl">Service Lines</div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="cta">
  <div class="cta-bg"><img src="images/corporate-interior.jpg" alt="" /></div>
  <div class="container">
    <div class="cta-inner">
      <div class="reveal">
        <span class="eyebrow">Scope Your Program</span>
        <h2>Need more than one service? <span class="alt">That's our specialty.</span></h2>
        <p>Bundle multiple service lines into a single account managed by one team. Less vendor overhead, more accountability.</p>
      </div>
      <div class="cta-actions reveal">
        <a href="contact.html#quote" class="btn btn-primary">Request a Multi-Service Quote
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </a>
        <a href="industries.html" class="btn btn-outline-light">See Industries Served</a>
      </div>
    </div>
  </div>
</section>
"""

# =============================================================
# INDUSTRIES
# =============================================================
INDUSTRIES = [
    ("office","Office Buildings","Class A office towers, professional-services buildings, and corporate headquarters where presentation is part of the brand. We program our service to tenant expectations, security protocols, and after-hours access — and run day porter coverage that keeps lobbies and common areas executive-ready.","office-interior.jpg"),
    ("medical","Medical Facilities","Outpatient clinics, medical office buildings, and specialty practices that require compliance-grade protocols. Trained crews, EPA-registered disinfectants, color-coded equipment, and documented procedures aligned to healthcare operating environments.","medical-facility.jpg"),
    ("industrial","Industrial Facilities","Manufacturing plants, processing facilities, and heavy-use industrial environments. We deliver janitorial programs scoped to industrial soil categories, plus epoxy floor coatings and pressure-wash programs for back-of-house operations.","industrial.jpg"),
    ("warehouse","Warehouses","Distribution centers and high-volume warehouse environments where floors take a beating. Routine janitorial for office and breakroom zones, plus epoxy systems, concrete polishing, and recurring floor restoration on the operations side.","warehouse.jpg"),
    ("education","Educational Facilities","Private schools, universities, training campuses, and continuing-education facilities. We run our service windows around your academic calendar — overnight, weekend, and break-period programs that protect the learning environment.","educational.jpg"),
    ("multi-tenant","Multi-Tenant Properties","Mixed-use, retail-mixed, and multi-tenant commercial properties with shared common-area cleaning requirements. We coordinate with property management to deliver consistent standards across every tenant touchpoint.","multi-tenant.jpg"),
    ("construction","Construction Projects","Rough, final, and turnover-ready post-construction cleaning for general contractors and owner's reps. We mobilize fast, scale crews to deadline, and deliver punch-list-ready spaces on schedule.","construction.jpg"),
    ("corporate","Corporate Facilities","Corporate campuses, enterprise headquarters, and large multi-building footprints. Dedicated account management, on-site supervisors, and the operational depth needed to run executive-grade presentation across a full campus.","corporate-interior.jpg"),
]

INDUSTRIES_BODY = """
<section class="page-hero">
  <div class="page-hero-bg"><img src="images/multi-tenant.jpg" alt="" /></div>
  <div class="container">
    <div class="crumbs"><a href="index.html">Home</a><span class="sep">/</span><span>Industries</span></div>
    <h1>Built for the demands of <span class="alt">commercial environments.</span></h1>
    <p>Eight commercial verticals — each with its own compliance posture, scheduling rhythm, and operating standard. Handled by crews trained for the environment they serve.</p>
  </div>
</section>

<section class="intro" style="padding-bottom: 2rem;">
  <div class="container">
"""
for i, (iid, title, desc, img) in enumerate(INDUSTRIES, start=1):
    reverse = i % 2 == 0
    INDUSTRIES_BODY += f"""
    <div class="intro-grid reveal" id="{iid}" style="margin-bottom: 4rem;{' direction: rtl;' if reverse else ''}">
      <div class="intro-text" style="direction: ltr;">
        <span class="eyebrow">Vertical {i:02d}</span>
        <h2>{title}</h2>
        <p class="lede">{desc}</p>
        <a href="contact.html#quote" class="link-arrow">Request a proposal for this vertical
          <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </a>
      </div>
      <div class="intro-visual" style="direction: ltr; aspect-ratio: 5/4;">
        <img src="images/{img}" alt="{title}" />
      </div>
    </div>
"""
INDUSTRIES_BODY += """
  </div>
</section>

<section class="cta">
  <div class="cta-bg"><img src="images/tech-facility.jpg" alt="" /></div>
  <div class="container">
    <div class="cta-inner">
      <div class="reveal">
        <span class="eyebrow">Talk to Our Team</span>
        <h2>Don't see your vertical? <span class="alt">We probably serve it.</span></h2>
        <p>If your facility is commercial, we can program a service line for it. Contact our team to discuss your environment.</p>
      </div>
      <div class="cta-actions reveal">
        <a href="contact.html#quote" class="btn btn-primary">Start a Conversation
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </a>
        <a href="services.html" class="btn btn-outline-light">View Services</a>
      </div>
    </div>
  </div>
</section>
"""

# =============================================================
# CAREERS
# =============================================================
CAREERS_BODY = """
<section class="page-hero">
  <div class="page-hero-bg"><img src="images/careers-hero.jpg" alt="" /></div>
  <div class="container">
    <div class="crumbs"><a href="index.html">Home</a><span class="sep">/</span><span>Careers</span></div>
    <h1>Build a career with a <span class="alt">growth-oriented contractor.</span></h1>
    <p>We hire for reliability, attention to detail, and pride of work. In return, we offer stable schedules, real supervision, and a path to grow with the company.</p>
  </div>
</section>

<section class="intro">
  <div class="container">
    <div class="intro-grid">
      <div class="intro-text reveal">
        <span class="eyebrow">Working at HCFS</span>
        <h2>Disciplined teams. <span class="alt">Real careers.</span></h2>
        <p class="lede">We don't run our crews like a temporary labor pool. We invest in supervision, training, and equipment because our clients depend on the people who show up.</p>
        <p>From entry-level janitorial positions to account-management roles, we hire people who want to do the work well and grow into something larger.</p>
      </div>
      <div class="intro-visual reveal">
        <img src="images/team-pro.jpg" alt="Hill Country team" />
        <div class="badge">
          <span class="dot"></span>
          <span class="txt"><strong>Now hiring</strong> &mdash; multiple positions across Texas</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="services">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Open Positions</span>
      <h2>Roles we're currently hiring for.</h2>
      <p>If you don't see your role listed, submit a general application below — we hire continuously.</p>
    </div>
    <div class="services-grid reveal-stagger">
      <article class="service-card">
        <span class="num">FT</span>
        <div class="service-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 21h18M5 21V7l7-4 7 4v14"/></svg></div>
        <h3>Commercial Cleaning Technician</h3>
        <p>Evening and overnight shifts. Office, medical, and corporate accounts across the Hill Country and major Texas metros.</p>
      </article>
      <article class="service-card">
        <span class="num">FT</span>
        <div class="service-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 2v20M2 12h20"/></svg></div>
        <h3>Day Porter</h3>
        <p>Daytime, single-site coverage. Lobby, restroom, common-area, and tenant-facing presentation responsibilities.</p>
      </article>
      <article class="service-card">
        <span class="num">FT</span>
        <div class="service-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 12h18M3 6h18M3 18h12"/></svg></div>
        <h3>Floor Care Specialist</h3>
        <p>VCT stripping/waxing, carpet extraction, and concrete polishing crews. Equipment experience required.</p>
      </article>
      <article class="service-card">
        <span class="num">FT</span>
        <div class="service-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M2 18l5-5 4 4 5-5 6 6"/></svg></div>
        <h3>Coatings Crew Lead</h3>
        <p>Lead epoxy floor coating and concrete staining installations. Project planning and crew oversight responsibilities.</p>
      </article>
      <article class="service-card">
        <span class="num">FT</span>
        <div class="service-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div>
        <h3>On-Site Supervisor</h3>
        <p>Multi-account or single-site supervision. Quality audits, crew leadership, and client communication ownership.</p>
      </article>
      <article class="service-card">
        <span class="num">FT</span>
        <div class="service-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 3v18h18"/><path d="M7 14l4-4 4 4 5-6"/></svg></div>
        <h3>Account Manager</h3>
        <p>Client-facing portfolio management. Account onboarding, retention, expansion, and operational reporting.</p>
      </article>
    </div>
  </div>
</section>

<section class="whyus" id="apply">
  <div class="container">
    <div class="whyus-grid">
      <div class="whyus-text reveal">
        <span class="eyebrow">Apply Now</span>
        <h2>Submit your <span class="alt">application.</span></h2>
        <p>Tell us about your experience and the type of role you're interested in. Our hiring team will reach out to qualified applicants.</p>
        <div class="whyus-list">
          <div class="whyus-item"><div class="ico"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><path d="M8 12l3 3 5-6"/></svg></div><div><h4>Competitive Pay</h4><p>Wages above local market with performance-based step increases.</p></div></div>
          <div class="whyus-item"><div class="ico"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></div><div><h4>Stable Schedules</h4><p>Documented routes and consistent shift assignments — no last-minute scrambles.</p></div></div>
          <div class="whyus-item"><div class="ico"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 3v18h18"/><path d="M7 14l4-4 4 4 5-6"/></svg></div><div><h4>Growth Path</h4><p>Crew-to-supervisor-to-account-manager progression with documented training.</p></div></div>
        </div>
      </div>
      <div class="reveal">
        <form data-quote class="form-grid" style="background: var(--bg); padding: 2.5rem; border: 1px solid var(--border); border-radius: 4px; box-shadow: var(--shadow-md);">
          <div class="form-row"><label>First name <span class="req">*</span></label><input type="text" required></div>
          <div class="form-row"><label>Last name <span class="req">*</span></label><input type="text" required></div>
          <div class="form-row"><label>Email <span class="req">*</span></label><input type="email" required></div>
          <div class="form-row"><label>Phone <span class="req">*</span></label><input type="tel" required></div>
          <div class="form-row full"><label>Position of interest <span class="req">*</span></label>
            <select required>
              <option value="">Select a role</option>
              <option>Commercial Cleaning Technician</option>
              <option>Day Porter</option>
              <option>Floor Care Specialist</option>
              <option>Coatings Crew Lead</option>
              <option>On-Site Supervisor</option>
              <option>Account Manager</option>
              <option>General Application</option>
            </select>
          </div>
          <div class="form-row full"><label>Years of relevant experience</label>
            <select>
              <option>Less than 1 year</option>
              <option>1–3 years</option>
              <option>3–5 years</option>
              <option>5–10 years</option>
              <option>10+ years</option>
            </select>
          </div>
          <div class="form-row full"><label>Tell us about your background</label><textarea placeholder="Brief summary of your experience and availability"></textarea></div>
          <div class="form-row full" style="margin-top: 0.5rem;">
            <button type="submit" class="btn btn-primary" style="width: 100%; justify-content: center;">Submit Application
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</section>
"""

# =============================================================
# CONTACT
# =============================================================
CONTACT_BODY = """
<section class="page-hero">
  <div class="page-hero-bg"><img src="images/corporate-interior.jpg" alt="" /></div>
  <div class="container">
    <div class="crumbs"><a href="index.html">Home</a><span class="sep">/</span><span>Contact</span></div>
    <h1>Request a commercial <span class="alt">facility quote.</span></h1>
    <p>Tell us about your property portfolio. Our team will follow up to schedule a walk-through and build a scoped proposal.</p>
  </div>
</section>

<section class="intro" id="quote">
  <div class="container">
    <div class="intro-grid" style="align-items: start;">
      <div class="intro-text reveal">
        <span class="eyebrow">Get in Touch</span>
        <h2>Direct lines to <span class="alt">our team.</span></h2>
        <p>Phone, email, or the request form &mdash; whichever fits your workflow. For active emergencies or after-hours dispatch, please call.</p>
        <div class="whyus-list" style="margin-top: 2rem;">
          <div class="whyus-item">
            <div class="ico"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg></div>
            <div><h4>Phone</h4><p style="font-family: var(--font-display); font-size: 1.25rem; color: var(--navy-900); margin: 0;">(512) 893-4012</p><p style="margin-top: 0.25rem;">Mon&ndash;Fri 7am&ndash;6pm CT &middot; 24/7 dispatch</p></div>
          </div>
          <div class="whyus-item">
            <div class="ico"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><path d="M22 6l-10 7L2 6"/></svg></div>
            <div><h4>Email</h4><p style="margin: 0;">Contact@hillcountryfacilityservices.com</p><p style="margin-top: 0.25rem;">For RFPs, multi-site bids, and account inquiries</p></div>
          </div>
          <div class="whyus-item">
            <div class="ico"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></div>
            <div><h4>Service Region</h4><p style="margin: 0;">Texas Hill Country &middot; Austin &middot; San Antonio</p><p style="margin-top: 0.25rem;">Houston, DFW, and statewide on multi-site contracts</p></div>
          </div>
        </div>
      </div>
      <div class="reveal">
        <form data-quote class="form-grid" style="background: var(--bg-alt); padding: 2.5rem; border: 1px solid var(--border); border-radius: 4px; box-shadow: var(--shadow-md);">
          <div class="form-row full">
            <span class="eyebrow" style="margin-bottom: 0.5rem;">Quote Request</span>
            <h3 style="font-family: var(--font-display); font-size: 1.625rem; margin: 0;">Tell us about your property</h3>
          </div>
          <div class="form-row"><label>First name <span class="req">*</span></label><input type="text" required></div>
          <div class="form-row"><label>Last name <span class="req">*</span></label><input type="text" required></div>
          <div class="form-row"><label>Company <span class="req">*</span></label><input type="text" required></div>
          <div class="form-row"><label>Role</label>
            <select>
              <option>Property Manager</option>
              <option>Facility Manager</option>
              <option>General Contractor</option>
              <option>Operations Lead</option>
              <option>Real Estate Owner / Operator</option>
              <option>Other</option>
            </select>
          </div>
          <div class="form-row"><label>Work email <span class="req">*</span></label><input type="email" required></div>
          <div class="form-row"><label>Phone <span class="req">*</span></label><input type="tel" required></div>
          <div class="form-row full"><label>Property type <span class="req">*</span></label>
            <select required>
              <option value="">Select property type</option>
              <option>Office Building</option>
              <option>Medical Facility</option>
              <option>Industrial Facility</option>
              <option>Warehouse</option>
              <option>Educational Facility</option>
              <option>Multi-Tenant Property</option>
              <option>Construction Project</option>
              <option>Corporate Facility</option>
              <option>Multiple Property Types</option>
            </select>
          </div>
          <div class="form-row"><label>Approx. square footage</label>
            <select>
              <option>Under 25,000</option>
              <option>25,000–100,000</option>
              <option>100,000–250,000</option>
              <option>250,000–1,000,000</option>
              <option>1,000,000+</option>
            </select>
          </div>
          <div class="form-row"><label>Number of properties</label>
            <select>
              <option>1</option>
              <option>2–5</option>
              <option>6–15</option>
              <option>16–50</option>
              <option>50+</option>
            </select>
          </div>
          <div class="form-row full"><label>Services needed <span class="req">*</span></label>
            <select required>
              <option value="">Select primary service</option>
              <option>Commercial Janitorial</option>
              <option>Office Cleaning</option>
              <option>Day Porter</option>
              <option>Floor Care (VCT, Carpet, Concrete)</option>
              <option>Epoxy Coatings</option>
              <option>Interior Painting</option>
              <option>Pressure Washing</option>
              <option>Post-Construction Cleanup</option>
              <option>Facility Maintenance</option>
              <option>Disinfection</option>
              <option>Multi-Service / Bundled Program</option>
            </select>
          </div>
          <div class="form-row full"><label>Additional details</label><textarea placeholder="Service frequency, target start date, current vendor situation, scope notes, or anything else our team should know."></textarea></div>
          <div class="form-row full" style="margin-top: 0.5rem;">
            <button type="submit" class="btn btn-primary" style="width: 100%; justify-content: center;">Request a Proposal
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </button>
            <p style="font-size: 0.75rem; color: var(--ink-muted); margin: 0.75rem 0 0; text-align: center;">Your information is confidential. We do not share or sell contact data.</p>
          </div>
        </form>
      </div>
    </div>
  </div>
</section>

<section class="cta">
  <div class="cta-bg"><img src="images/office-meeting.jpg" alt="" /></div>
  <div class="container">
    <div class="cta-inner">
      <div class="reveal">
        <span class="eyebrow">Active emergency?</span>
        <h2>24/7 dispatch <span class="alt">always answers.</span></h2>
        <p>Water intrusion, biohazard response, post-incident cleanup, or any urgent commercial situation &mdash; call our dispatch line for immediate coordination.</p>
      </div>
      <div class="cta-actions reveal">
        <a href="tel:+15128934012" class="btn btn-primary">Call (512) 893-4012
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
        </a>
      </div>
    </div>
  </div>
</section>
"""

# Write all pages
pages = {
    "about.html": ("About — Hill Country Facility Services", "Growth-oriented commercial facility services contractor built for property managers, facility executives, and enterprise commercial portfolios.", ABOUT_BODY),
    "services.html": ("Services — Hill Country Facility Services", "Twelve commercial service capabilities — janitorial, floor restoration, epoxy coatings, painting, maintenance, and more — for commercial properties.", SERVICES_BODY),
    "industries.html": ("Industries — Hill Country Facility Services", "Commercial facility services for office, medical, industrial, warehouse, educational, multi-tenant, construction, and corporate environments.", INDUSTRIES_BODY),
    "careers.html": ("Careers — Hill Country Facility Services", "Open positions in commercial cleaning, floor care, coatings, supervision, and account management at a growing Texas facility services contractor.", CAREERS_BODY),
    "contact.html": ("Contact — Hill Country Facility Services", "Request a commercial facility services quote. Phone, email, or our quote form — our team will follow up to scope a walk-through and proposal.", CONTACT_BODY),
}

root = os.path.dirname(__file__) or "."
for name, (title, desc, body) in pages.items():
    with open(os.path.join(root, name), "w") as f:
        f.write(page(title, desc, body))
    print(f"Wrote {name}")
