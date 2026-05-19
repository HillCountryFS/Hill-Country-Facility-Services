"""Generate Privacy / Terms / Accessibility pages from a shared template.

Pulls header/footer from about.html so layout stays in sync. V5 content.
"""

from pathlib import Path
import re

ROOT = Path(__file__).parent
ABOUT = (ROOT / "about.html").read_text()

header_match = re.search(r"<header class=\"header\">.*?</header>", ABOUT, re.S)
footer_match = re.search(r"<footer class=\"footer\">.*?</footer>", ABOUT, re.S)
assert header_match and footer_match
HEADER = header_match.group(0)
FOOTER = footer_match.group(0)


def page_html(title: str, description: str, h1: str, intro: str, body: str, effective: str = "May 13, 2026") -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title} — Hill Country Facility Services</title>
<meta name="description" content="{description}" />
<meta property="og:title" content="{title} — Hill Country Facility Services" />
<meta property="og:description" content="{description}" />
<meta property="og:type" content="website" />
<link rel="icon" type="image/png" href="images/logo-full.png?v=2" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300;9..144,400;9..144,500&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="css/styles.css" />
</head>
<body>

{HEADER}

<section class="page-hero page-hero-compact">
  <div class="container">
    <div class="crumbs"><a href="index.html">Home</a><span class="sep">/</span><span>{title}</span></div>
    <h1>{h1}</h1>
    <p>{intro}</p>
    <div class="legal-effective">Effective: {effective}</div>
  </div>
</section>

<section class="legal-section">
  <div class="container legal-container">
    {body}
  </div>
</section>

{FOOTER}
<script src="js/main.js"></script>
</body>
</html>
"""


TERMS_BODY = """
<p class="legal-lede">Use of this web site is subject to the following terms. By accessing or browsing the site, you confirm your acceptance of these terms and your agreement to comply with all applicable federal, state, and local laws. If you do not agree to any portion of these terms, please discontinue use of the site.</p>

<h2>1. Acceptance</h2>
<p>Your continued use of this web site constitutes acknowledgment that you have read, understood, and agreed to these Terms of Service. We may update or refine these terms periodically, and any revisions take effect upon publication on this page.</p>

<h2>2. Permitted Use</h2>
<p>Visitors are granted a limited, revocable right to access and view the contents of this site for informational and business-evaluation purposes only. You may save or print individual pages for internal reference. You may not, however:</p>
<ul>
  <li>Reproduce, republish, or redistribute any portion of the site in any form;</li>
  <li>Use site content for commercial gain, public display, or in any product or service;</li>
  <li>Attempt to access, alter, or interfere with the underlying code, systems, or infrastructure;</li>
  <li>Strip or obscure attribution, copyright notices, or branding;</li>
  <li>Mirror, frame, or rehost any portion of the site on a separate server or domain.</li>
</ul>
<p>Any conduct outside this permitted use immediately ends your right to access the site.</p>

<h2>3. Intellectual Property</h2>
<p>All written content, photography, branding elements, page design, and underlying code on this site are owned by Hill Country Facility Services or its licensors and are protected under United States and international intellectual-property law. Nothing on this site should be interpreted as granting rights to use any name, mark, or logo associated with our business without our prior written permission.</p>

<h2>4. No Warranty</h2>
<p>The information published on this site is offered in good faith and on an &ldquo;as is&rdquo; basis. We do not warrant the accuracy, completeness, or timeliness of any material posted, and we make no representations regarding any outcomes that may result from reliance on it. Service-specific commitments are documented exclusively in the written service agreement between us and the client.</p>

<h2>5. Limitation of Liability</h2>
<p>Hill Country Facility Services will not be liable for any loss, damage, or claim &mdash; direct, indirect, incidental, consequential, or otherwise &mdash; arising out of access to, use of, or inability to use this site, including any errors or omissions in its content. This limitation applies to the fullest extent permitted by law. Some jurisdictions restrict the exclusion of certain warranties or damages; in those jurisdictions, the corresponding portions of this section apply only as far as the law allows.</p>

<h2>6. Third-Party References</h2>
<p>This site may include references or links to outside resources for convenience. We do not control those resources and are not responsible for their content, accuracy, or practices. Accessing third-party material from this site is done at your own risk.</p>

<h2>7. Inquiries Are Not Agreements</h2>
<p>A submission through any form, contact email, or page on this site is treated as an inquiry only. It does not constitute an offer, acceptance, or binding commitment. Any service relationship begins only upon execution of a written agreement between us and the client.</p>

<h2>8. Governing Law</h2>
<p>These terms, and any matter arising from or related to this site, are governed by the laws of the State of Texas, without reference to its conflict-of-laws principles. Any dispute will be resolved in the state or federal courts located in Travis County, Texas.</p>

<h2>9. Contact</h2>
<p>Questions about these Terms may be sent to <a href="mailto:Contact@hillcountryfacilityservices.com">Contact@hillcountryfacilityservices.com</a>.</p>
"""

PRIVACY_BODY = """
<p class="legal-lede">We take the privacy of every visitor seriously. This page describes how we approach the collection, handling, and protection of personal information shared with us through this site or in the course of communicating with our team.</p>

<p>Our practices are guided by the following commitments:</p>

<p>We collect personal information only when it serves a clearly defined purpose &mdash; typically responding to a quote request, scheduling a property walkthrough, or evaluating an employment inquiry &mdash; and we communicate that purpose at the time information is collected.</p>

<p>We use the information you provide solely for the purpose it was collected, for purposes reasonably related to that original use, or for purposes you separately consent to.</p>

<p>We retain personal information only for as long as it remains relevant to those purposes or as required by applicable law, and we periodically remove records that are no longer needed.</p>

<p>We collect information through lawful and transparent means, and where appropriate, with the knowledge or consent of the individual to whom the information relates.</p>

<p>We expect personal information in our possession to be accurate, relevant, and reasonably current, and we will correct or update information at the request of the individual it concerns.</p>

<p>We safeguard personal information with administrative, technical, and physical measures appropriate to its sensitivity, and we work to prevent unauthorized access, disclosure, alteration, or destruction.</p>

<p>We share information only with trusted service providers acting on our behalf &mdash; such as hosting, email, analytics, and professional advisors &mdash; and only to the extent necessary for those providers to perform their work. We do not sell personal information.</p>

<p>We make information about our privacy practices available to anyone who asks, and we respond to reasonable inquiries about the personal information we hold.</p>

<p>We conduct our business in accordance with these commitments and review our practices regularly to ensure they remain consistent with applicable laws and the expectations of the clients we serve.</p>
"""

ACCESSIBILITY_BODY = """
<p class="legal-lede">Hill Country Facility Services is committed to maintaining a web presence that can be used by as broad an audience as possible, including individuals who rely on assistive technology.</p>

<p>Our internal target is substantial conformance with the Web Content Accessibility Guidelines (WCAG) 2.1 at Level AA, as published by the World Wide Web Consortium. These guidelines exist to support people with a wide range of disabilities &mdash; including those affecting vision, hearing, mobility, and cognition &mdash; and they shape how we build and review the pages on this site.</p>

<p>Toward that goal, our site is developed using semantic page structure, descriptive headings and link text, scalable typography, color contrast appropriate to legibility, and keyboard-navigable interactive elements. Text alternatives are provided for non-text content where reasonably practicable, and accessibility considerations are part of the review process for new and updated pages.</p>

<p>Accessibility is a continuing effort rather than a one-time achievement. We recognize that some portions of the site may not yet meet our target in every respect, and we work to identify and resolve those issues as part of regular site maintenance. Where third-party services or embedded content appear on the site, we choose vendors that support accessibility, but we are not always able to guarantee their conformance.</p>

<p>If you encounter difficulty accessing any part of this site, or if you would like information from the site delivered in an alternative format, please contact us at <a href="mailto:Contact@hillcountryfacilityservices.com">Contact@hillcountryfacilityservices.com</a>. Including the page address, a brief description of the issue, and the device or assistive technology you are using will help us respond as quickly and effectively as possible.</p>
"""

pages = [
    {
        "slug": "privacy",
        "title": "Privacy Policy",
        "description": "How Hill Country Facility Services approaches the collection, use, and protection of personal information.",
        "h1": 'Privacy <span class="alt">Policy.</span>',
        "intro": "How we approach the collection, use, and protection of personal information.",
        "body": PRIVACY_BODY,
    },
    {
        "slug": "terms",
        "title": "Terms of Service",
        "description": "The terms governing your use of the Hill Country Facility Services web site.",
        "h1": 'Terms of <span class="alt">Service.</span>',
        "intro": "The terms that govern your use of this web site.",
        "body": TERMS_BODY,
    },
    {
        "slug": "accessibility",
        "title": "Accessibility Statement",
        "description": "Hill Country Facility Services' commitment to web accessibility and our WCAG 2.1 Level AA target.",
        "h1": 'Accessibility <span class="alt">Statement.</span>',
        "intro": "Our commitment to making this web site usable by as broad an audience as possible.",
        "body": ACCESSIBILITY_BODY,
    },
]

for p in pages:
    out = page_html(p["title"], p["description"], p["h1"], p["intro"], p["body"])
    (ROOT / f"{p['slug']}.html").write_text(out)
    print(f"wrote {p['slug']}.html")

print("done")
