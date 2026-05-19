"""Add Capabilities Overview PDF download links across the site:

1. Footer-bottom-links on every HTML page (root + locations/)
2. Inline download button on About page
3. Inline download button on Services page
4. Contact form thank-you state (handled in main.js)
"""
from pathlib import Path
import re

HCFS = Path("/home/user/workspace/hcfs")
PDF_NAME = "capabilities-overview.pdf"

# Pages at the root use "capabilities-overview.pdf";
# location pages use "../capabilities-overview.pdf".
ROOT_HTML = sorted(HCFS.glob("*.html"))
LOC_HTML = sorted((HCFS / "locations").glob("*.html"))

def patch_footer_link(path: Path, pdf_href: str) -> bool:
    text = path.read_text()
    if "capabilities-overview.pdf" in text:
        # Already patched in some prior run; skip
        return False
    # Insert Capabilities link before the Privacy link in footer-bottom-links
    pattern = re.compile(r'(<div class="footer-bottom-links">\s*)(<a href="(?:\.\./)?privacy\.html">Privacy</a>)')
    new_link = f'<a href="{pdf_href}" target="_blank" rel="noopener">Capabilities PDF</a>\n        '
    new_text, n = pattern.subn(rf'\1{new_link}\2', text, count=1)
    if n == 0:
        return False
    path.write_text(new_text)
    return True

for p in ROOT_HTML:
    patched = patch_footer_link(p, PDF_NAME)
    print(("[patched] " if patched else "[skip]    ") + p.relative_to(HCFS).as_posix())

for p in LOC_HTML:
    patched = patch_footer_link(p, f"../{PDF_NAME}")
    print(("[patched] " if patched else "[skip]    ") + p.relative_to(HCFS).as_posix())
