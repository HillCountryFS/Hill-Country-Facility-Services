#!/usr/bin/env python3
"""Build the remaining HCFS pages with consistent header/footer."""
import os

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{desc}" />
<meta property="og:type" content="website" />
<link rel="icon" type="image/png" href="images/logo-trim.png" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300;9..144,400;9..144,500&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="css/styles.css" />
</head>
<body>
"""

HEADER = """
<header class="header">
  <div class="container">
    <a href="index.html" class="brand">
      <img src="images/logo-trim.png" alt="Hill Country Facility Services" />
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

FOOTER = """
<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="images/logo-trim.png" alt="Hill Country Facility Services" />
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
          <li><a href="about.html">About Us</a></li>
          <li><a href="services.html">Services</a></li>
          <li><a href="industries.html">Industries</a></li>
          <li><a href="careers.html">Careers</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Capabilities</h4>
        <ul>
          <li><a href="services.html#janitorial">Janitorial Programs</a></li>
          <li><a href="services.html#floors">Floor Restoration</a></li>
          <li><a href="services.html#coatings">Specialty Coatings</a></li>
          <li><a href="services.html#maintenance">Facility Maintenance</a></li>
          <li><a href="services.html#disinfection">Disinfection</a></li>
        </ul>
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
<script src="js/main.js"></script>
</body>
</html>
"""

def page(title, desc, body):
    return HEAD.format(title=title, desc=desc) + HEADER + body + FOOTER

# Pages will be defined in separate files and assembled by importing this builder
if __name__ == "__main__":
    print("Builder loaded. Use page(title, desc, body) to create pages.")
