"""Build the Hill Country Facility Services Capabilities Overview one-page PDF.

Outputs: /home/user/workspace/hcfs/capabilities-overview.pdf
"""
import urllib.request
from pathlib import Path

from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

# ----------------------------- Fonts ---------------------------------------
FONT_DIR = Path("/tmp/fonts")
FONT_DIR.mkdir(exist_ok=True)

FONTS = {
    "DMSans": "https://github.com/google/fonts/raw/main/ofl/dmsans/DMSans%5Bopsz%2Cwght%5D.ttf",
    "DMSans-Italic": "https://github.com/google/fonts/raw/main/ofl/dmsans/DMSans-Italic%5Bopsz%2Cwght%5D.ttf",
    "Inter": "https://github.com/google/fonts/raw/main/ofl/inter/Inter%5Bopsz%2Cwght%5D.ttf",
}
for name, url in FONTS.items():
    path = FONT_DIR / f"{name}.ttf"
    if not path.exists():
        urllib.request.urlretrieve(url, path)
    pdfmetrics.registerFont(TTFont(name, str(path)))

# Aliases so we can request "bold" easily — Inter & DM Sans are variable fonts,
# so we approximate weight by using the same TTF and letting ReportLab draw
# bold-style via setFont; for our purposes Inter and DMSans handle this fine.
# We'll just use the same registration for "bold" calls (it still renders).
pdfmetrics.registerFont(TTFont("DMSans-Bold", str(FONT_DIR / "DMSans.ttf")))
pdfmetrics.registerFont(TTFont("Inter-Bold", str(FONT_DIR / "Inter.ttf")))

# ----------------------------- Palette -------------------------------------
NAVY = HexColor("#0e1b33")        # var(--navy-900)
NAVY_DEEP = HexColor("#0a1428")   # var(--navy-950)
GOLD = HexColor("#b08a3e")        # var(--gold-600)
GOLD_LIGHT = HexColor("#d4ae66")  # var(--gold-400)
OLIVE = HexColor("#6b7a4f")       # var(--olive-600)
GRAY_BG = HexColor("#f5f6f8")     # var(--gray-50)
GRAY_LINE = HexColor("#dfe3e9")   # var(--gray-200)
TEXT = HexColor("#0e1b33")        # navy as body color
TEXT_MUTED = HexColor("#5e6878")  # var(--gray-500)

# ----------------------------- Page set up ---------------------------------
PAGE_W, PAGE_H = letter
MARGIN_X = 0.55 * inch
OUT_PATH = "/home/user/workspace/hcfs/capabilities-overview.pdf"

c = canvas.Canvas(OUT_PATH, pagesize=letter)
c.setTitle("Capabilities Overview — Hill Country Facility Services")
c.setAuthor("Perplexity Computer")

# ============================================================================
# HEADER BAND (navy)
# ============================================================================
HEADER_H = 0.85 * inch
c.setFillColor(NAVY)
c.rect(0, PAGE_H - HEADER_H, PAGE_W, HEADER_H, fill=1, stroke=0)

# Left: brand
c.setFillColor(white)
c.setFont("DMSans-Bold", 14)
c.drawString(MARGIN_X, PAGE_H - HEADER_H + 0.42 * inch, "HILL COUNTRY")
c.setFont("DMSans", 9)
c.setFillColor(GOLD_LIGHT)
c.drawString(MARGIN_X, PAGE_H - HEADER_H + 0.22 * inch, "FACILITY SERVICES LLC")

# Center: title
c.setFillColor(white)
c.setFont("DMSans-Bold", 11)
title_text = "CAPABILITIES OVERVIEW"
title_w = c.stringWidth(title_text, "DMSans-Bold", 11)
c.drawString((PAGE_W - title_w) / 2, PAGE_H - HEADER_H + 0.42 * inch, title_text)
# small underline accent
c.setStrokeColor(GOLD)
c.setLineWidth(1)
c.line(
    (PAGE_W - title_w) / 2,
    PAGE_H - HEADER_H + 0.36 * inch,
    (PAGE_W + title_w) / 2,
    PAGE_H - HEADER_H + 0.36 * inch,
)
c.setFont("DMSans", 8.5)
c.setFillColor(HexColor("#c2c9d3"))
subtitle = "Commercial facility services across Texas"
sub_w = c.stringWidth(subtitle, "DMSans", 8.5)
c.drawString((PAGE_W - sub_w) / 2, PAGE_H - HEADER_H + 0.18 * inch, subtitle)

# Right: contact block
c.setFillColor(white)
c.setFont("DMSans", 8.5)
right_x = PAGE_W - MARGIN_X
c.drawRightString(right_x, PAGE_H - HEADER_H + 0.55 * inch, "(512) 893-4012")
c.drawRightString(right_x, PAGE_H - HEADER_H + 0.40 * inch, "Contact@hillcountryfacilityservices.com")
c.drawRightString(right_x, PAGE_H - HEADER_H + 0.25 * inch, "hillcountryfacilityservices.com")
c.drawRightString(right_x, PAGE_H - HEADER_H + 0.10 * inch, "Austin, Texas")

# ============================================================================
# LEAD STATEMENT
# ============================================================================
lead_y = PAGE_H - HEADER_H - 0.45 * inch
c.setFillColor(NAVY)
c.setFont("DMSans-Bold", 13)
c.drawString(MARGIN_X, lead_y, "Professional facility services for commercial properties.")
c.setFillColor(TEXT_MUTED)
c.setFont("Inter", 9.5)
c.drawString(
    MARGIN_X,
    lead_y - 0.18 * inch,
    "Janitorial, floor restoration, specialty coatings, and facility maintenance \u2014 delivered to documented operational standards.",
)

# Thin gold rule under lead
c.setStrokeColor(GOLD)
c.setLineWidth(0.8)
c.line(MARGIN_X, lead_y - 0.32 * inch, PAGE_W - MARGIN_X, lead_y - 0.32 * inch)

# ============================================================================
# TWO COLUMNS  (start)
# ============================================================================
COL_TOP = lead_y - 0.55 * inch
COL_GAP = 0.30 * inch
LEFT_COL_W = 4.10 * inch
RIGHT_COL_X = MARGIN_X + LEFT_COL_W + COL_GAP
RIGHT_COL_W = PAGE_W - MARGIN_X - RIGHT_COL_X

# ----- LEFT COLUMN ---------------------------------------------------------
def section_header(x, y, label):
    c.setFillColor(NAVY)
    c.setFont("DMSans-Bold", 10)
    c.drawString(x, y, label.upper())
    c.setStrokeColor(GOLD)
    c.setLineWidth(1.2)
    c.line(x, y - 4, x + 28, y - 4)

# Core Services
sec_y = COL_TOP
section_header(MARGIN_X, sec_y, "Core Services")
services = [
    "Commercial Janitorial",
    "Floor Care & Restoration",
    "Carpet Care",
    "Window Cleaning",
    "Post-Construction Cleanup",
    "Specialty Coatings",
    "Disinfection & Sanitization",
    "Restroom Sanitation",
    "Day Porter Services",
    "Pressure Washing",
    "Hard Surface Restoration",
    "Facility Maintenance Support",
]
service_y = sec_y - 0.30 * inch
col_a_x = MARGIN_X
col_b_x = MARGIN_X + LEFT_COL_W / 2
row_h = 0.18 * inch
c.setFont("Inter", 9.2)
for i, svc in enumerate(services):
    col_x = col_a_x if i % 2 == 0 else col_b_x
    row = i // 2
    y = service_y - row * row_h
    # gold dot
    c.setFillColor(GOLD)
    c.circle(col_x + 3, y + 3, 1.5, fill=1, stroke=0)
    c.setFillColor(TEXT)
    c.drawString(col_x + 12, y, svc)

services_block_h = ((len(services) + 1) // 2) * row_h
industries_y = service_y - services_block_h - 0.18 * inch

# Industries Served
section_header(MARGIN_X, industries_y, "Industries Served")
industries = [
    "Office & Corporate",
    "Medical & Healthcare",
    "Industrial & Manufacturing",
    "Educational",
    "Multi-Tenant Properties",
    "Tech & Data Centers",
    "Construction",
    "Specialty / Mission-Critical",
]
ind_y = industries_y - 0.30 * inch
c.setFont("Inter", 9.2)
for i, ind in enumerate(industries):
    col_x = col_a_x if i % 2 == 0 else col_b_x
    row = i // 2
    y = ind_y - row * row_h
    c.setFillColor(OLIVE)
    c.circle(col_x + 3, y + 3, 1.5, fill=1, stroke=0)
    c.setFillColor(TEXT)
    c.drawString(col_x + 12, y, ind)

# Service standards block (fills bottom of left column)
ind_block_h = ((len(industries) + 1) // 2) * row_h
std_y = ind_y - ind_block_h - 0.22 * inch
section_header(MARGIN_X, std_y, "Service Standards")
standards = [
    "Green Seal / EcoLogo-certified chemicals available on request",
    "HEPA filtration & microfiber systems for sensitive environments",
    "Trained crews — OSHA, bloodborne pathogen, and chemical handling",
    "English- and Spanish-speaking field supervisors",
    "Light-touch check-ins by email or call — whichever the client prefers",
]
std_item_y = std_y - 0.30 * inch
c.setFont("Inter", 9)
for item in standards:
    c.setFillColor(GOLD)
    c.circle(MARGIN_X + 3, std_item_y + 3, 1.5, fill=1, stroke=0)
    c.setFillColor(TEXT)
    # wrap if needed
    max_w = LEFT_COL_W - 14
    words = item.split()
    line = ""
    line_y = std_item_y
    first = True
    for w in words:
        test = (line + " " + w).strip()
        if c.stringWidth(test, "Inter", 9) <= max_w:
            line = test
        else:
            c.drawString(MARGIN_X + 12, line_y, line)
            line_y -= 0.14 * inch
            line = w
            first = False
    if line:
        c.drawString(MARGIN_X + 12, line_y, line)
    std_item_y = line_y - 0.17 * inch

# ----- RIGHT COLUMN --------------------------------------------------------
# Photo at top (banner style)
PHOTO_H = 1.45 * inch
photo_y = COL_TOP - PHOTO_H + 0.10 * inch
try:
    img = ImageReader("/home/user/workspace/hcfs/images/corporate-lobby.jpg")
    c.drawImage(
        img,
        RIGHT_COL_X,
        photo_y,
        width=RIGHT_COL_W,
        height=PHOTO_H,
        preserveAspectRatio=True,
        mask="auto",
    )
except Exception:
    c.setFillColor(NAVY)
    c.rect(RIGHT_COL_X, photo_y, RIGHT_COL_W, PHOTO_H, fill=1, stroke=0)

# Why HCFS
why_y = photo_y - 0.30 * inch
section_header(RIGHT_COL_X, why_y, "Why HCFS")
why_items = [
    ("Commercial-only focus", "No residential or one-off retail. Built for offices, medical, industrial, and multi-tenant properties."),
    ("Single point of contact", "Dedicated account manager and on-site supervision \u2014 name-and-face accountability."),
    ("Documented standards", "Site books, scoped SOPs, and supervisor walk-throughs on every account."),
    ("24/7 dispatch", "Round-the-clock response for spills, biohazard, after-hours requests, and emergencies."),
]
why_item_y = why_y - 0.28 * inch
c.setFont("Inter", 9.2)
for head, body in why_items:
    # gold square bullet
    c.setFillColor(GOLD)
    c.rect(RIGHT_COL_X, why_item_y - 1, 4, 4, fill=1, stroke=0)
    # bold lead
    c.setFillColor(NAVY)
    c.setFont("DMSans-Bold", 9.2)
    c.drawString(RIGHT_COL_X + 10, why_item_y, head)
    # body wrapped
    c.setFillColor(TEXT_MUTED)
    c.setFont("Inter", 8.6)
    body_y = why_item_y - 0.14 * inch
    max_w = RIGHT_COL_W - 10
    words = body.split()
    line = ""
    for w in words:
        test = (line + " " + w).strip()
        if c.stringWidth(test, "Inter", 8.6) <= max_w:
            line = test
        else:
            c.drawString(RIGHT_COL_X + 10, body_y, line)
            body_y -= 0.13 * inch
            line = w
    if line:
        c.drawString(RIGHT_COL_X + 10, body_y, line)
    why_item_y = body_y - 0.18 * inch

# OUR PROCESS (right column, fills the empty space below Why HCFS)
process_y = why_item_y - 0.05 * inch
section_header(RIGHT_COL_X, process_y, "Our Process")
process_steps = [
    ("01", "On-site walkthrough & scope review"),
    ("02", "Written proposal with line-item detail"),
    ("03", "Mobilization — site book, SOPs, crew assignment"),
    ("04", "First 30 days — close oversight, responsive adjustments"),
    ("05", "Ongoing partnership — walk-throughs & client check-ins"),
]
step_y = process_y - 0.28 * inch
for num, label in process_steps:
    # gold number
    c.setFillColor(GOLD)
    c.setFont("DMSans-Bold", 9)
    c.drawString(RIGHT_COL_X, step_y, num)
    # label
    c.setFillColor(TEXT)
    c.setFont("Inter", 8.8)
    c.drawString(RIGHT_COL_X + 18, step_y, label)
    step_y -= 0.17 * inch

# ============================================================================
# FOOTER + COVERAGE constants (declared early so tagline can size to fit)
# ============================================================================
FOOTER_H = 0.85 * inch
COVERAGE_H = 1.00 * inch
COVERAGE_Y = FOOTER_H + 0.16 * inch

# ----- TAGLINE PANEL ---------------------------------------------------------
# Fills the gap between content above and coverage strip below with a substantial
# navy positioning panel.
lowest_content_y = min(step_y + 0.17 * inch, std_item_y + 0.17 * inch)
TAG_TOP = lowest_content_y - 0.18 * inch
TAG_BOTTOM = COVERAGE_Y + COVERAGE_H + 0.16 * inch
TAG_H = TAG_TOP - TAG_BOTTOM
TAG_Y = TAG_BOTTOM
c.setFillColor(NAVY)
c.rect(MARGIN_X, TAG_Y, PAGE_W - 2 * MARGIN_X, TAG_H, fill=1, stroke=0)
# vertical gold accent
c.setFillColor(GOLD)
c.rect(MARGIN_X, TAG_Y, 3, TAG_H, fill=1, stroke=0)

# Tagline content centered vertically
c.setFillColor(white)
c.setFont("DMSans-Bold", 13)
tag_pad_x = 18
c.drawString(MARGIN_X + tag_pad_x, TAG_Y + TAG_H - 0.32 * inch, "We don’t sell cleaning — we sell operational reliability.")
c.setFillColor(HexColor("#c2c9d3"))
c.setFont("Inter", 9)
c.drawString(
    MARGIN_X + tag_pad_x,
    TAG_Y + TAG_H - 0.52 * inch,
    "Documented standards. On-site supervision. 24/7 dispatch. Built for commercial facilities.",
)

# Three differentiator chips inside the panel (bottom half)
chip_y = TAG_Y + 0.22 * inch
chip_w = (PAGE_W - 2 * MARGIN_X - 2 * tag_pad_x - 24) / 3
chips = [
    ("COMMERCIAL ONLY", "No residential / one-off retail"),
    ("TEXAS-OWNED", "15+ cities, statewide coverage"),
    ("SINGLE POINT OF CONTACT", "Dedicated account manager"),
]
for i, (head, body) in enumerate(chips):
    cx = MARGIN_X + tag_pad_x + i * (chip_w + 12)
    c.setFillColor(GOLD)
    c.setFont("DMSans-Bold", 7.5)
    c.drawString(cx, chip_y + 0.14 * inch, head)
    c.setFillColor(white)
    c.setFont("Inter", 8.5)
    c.drawString(cx, chip_y, body)

# ============================================================================
# COVERAGE STRIP — full width, just above footer
# ============================================================================

c.setFillColor(GRAY_BG)
c.rect(MARGIN_X, COVERAGE_Y, PAGE_W - 2 * MARGIN_X, COVERAGE_H, fill=1, stroke=0)
c.setStrokeColor(GRAY_LINE)
c.setLineWidth(0.6)
c.rect(MARGIN_X, COVERAGE_Y, PAGE_W - 2 * MARGIN_X, COVERAGE_H, fill=0, stroke=1)

# Left half: Texas Coverage
cov_pad = 0.18 * inch
c.setFillColor(NAVY)
c.setFont("DMSans-Bold", 10)
c.drawString(MARGIN_X + cov_pad, COVERAGE_Y + COVERAGE_H - 0.22 * inch, "TEXAS COVERAGE")
c.setStrokeColor(GOLD)
c.setLineWidth(1.2)
c.line(MARGIN_X + cov_pad, COVERAGE_Y + COVERAGE_H - 0.26 * inch, MARGIN_X + cov_pad + 28, COVERAGE_Y + COVERAGE_H - 0.26 * inch)
cities = "Austin \u00b7 Round Rock \u00b7 Cedar Park \u00b7 Pflugerville \u00b7 Georgetown \u00b7 San Marcos \u00b7 New Braunfels \u00b7 San Antonio \u00b7 Dallas \u00b7 Fort Worth \u00b7 Plano \u00b7 Frisco \u00b7 Arlington \u00b7 Irving \u00b7 Houston"
c.setFillColor(TEXT)
c.setFont("Inter", 8.6)
# wrap city list within half-width
half_w = (PAGE_W - 2 * MARGIN_X) / 2 - cov_pad * 1.5
words = cities.split(" ")
line = ""
line_y = COVERAGE_Y + COVERAGE_H - 0.45 * inch
for w in words:
    test = (line + " " + w).strip()
    if c.stringWidth(test, "Inter", 8.6) <= half_w:
        line = test
    else:
        c.drawString(MARGIN_X + cov_pad, line_y, line)
        line_y -= 0.14 * inch
        line = w
if line:
    c.drawString(MARGIN_X + cov_pad, line_y, line)

# Right half: Compliance & Coverage
right_x = MARGIN_X + (PAGE_W - 2 * MARGIN_X) / 2 + cov_pad / 2
c.setFillColor(NAVY)
c.setFont("DMSans-Bold", 10)
c.drawString(right_x, COVERAGE_Y + COVERAGE_H - 0.22 * inch, "COMPLIANCE & COVERAGE")
c.setStrokeColor(GOLD)
c.setLineWidth(1.2)
c.line(right_x, COVERAGE_Y + COVERAGE_H - 0.26 * inch, right_x + 28, COVERAGE_Y + COVERAGE_H - 0.26 * inch)
compl_items = [
    "General Liability \u00b7 Workers\u2019 Compensation",
    "Non-Owned & Hired Auto Insurance",
    "COI and W-9 furnished upon request",
]
c.setFillColor(TEXT)
c.setFont("Inter", 8.6)
ci_y = COVERAGE_Y + COVERAGE_H - 0.45 * inch
for item in compl_items:
    c.setFillColor(GOLD)
    c.circle(right_x + 2, ci_y + 3, 1.3, fill=1, stroke=0)
    c.setFillColor(TEXT)
    c.drawString(right_x + 10, ci_y, item)
    ci_y -= 0.16 * inch

# ============================================================================
# FOOTER BAND (navy)
# ============================================================================
c.setFillColor(NAVY_DEEP)
c.rect(0, 0, PAGE_W, FOOTER_H, fill=1, stroke=0)

# Left: CTA
c.setFillColor(white)
c.setFont("DMSans-Bold", 11)
c.drawString(MARGIN_X, FOOTER_H - 0.30 * inch, "Request a walkthrough.")
c.setFillColor(HexColor("#c2c9d3"))
c.setFont("Inter", 8.8)
c.drawString(MARGIN_X, FOOTER_H - 0.48 * inch, "We will scope your facility on-site and respond with a written proposal.")

# Gold contact pill (right)
pill_w = 3.1 * inch
pill_h = 0.42 * inch
pill_x = PAGE_W - MARGIN_X - pill_w
pill_y = FOOTER_H / 2 - pill_h / 2
c.setFillColor(GOLD)
c.roundRect(pill_x, pill_y, pill_w, pill_h, 4, fill=1, stroke=0)
c.setFillColor(NAVY_DEEP)
c.setFont("DMSans-Bold", 9.5)
c.drawCentredString(pill_x + pill_w / 2, pill_y + pill_h / 2 + 2, "Contact@hillcountryfacilityservices.com")
c.setFont("Inter", 8.2)
c.drawCentredString(pill_x + pill_w / 2, pill_y + pill_h / 2 - 9, "(512) 893-4012  \u00b7  Mon\u2013Sun 7am\u20136pm CT")

# Tiny bottom credit line
c.setFillColor(HexColor("#7a8294"))
c.setFont("Inter", 7)
c.drawString(MARGIN_X, 0.10 * inch, "Hill Country Facility Services LLC  \u00b7  Austin, Texas  \u00b7  hillcountryfacilityservices.com")
# Hyperlink the email + website regions
c.linkURL(
    "mailto:Contact@hillcountryfacilityservices.com",
    (pill_x, pill_y, pill_x + pill_w, pill_y + pill_h),
    relative=0,
)
c.linkURL(
    "https://hillcountryfacilityservices.com",
    (MARGIN_X, 0.08 * inch, MARGIN_X + 3.8 * inch, 0.22 * inch),
    relative=0,
)

c.save()
print(f"Wrote {OUT_PATH}")
