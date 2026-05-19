"""Generate the Texas service-area map SVG.

Uses real Texas state boundary GeoJSON simplified to ~200 points,
then projects city lat/long onto the SVG viewBox.
"""
import json
from pathlib import Path

CITIES = [
    # (slug, name, lat, lon, region, priority)
    ("austin",         "Austin",        30.2672, -97.7431, "austin",  "primary"),
    ("round-rock",     "Round Rock",    30.5083, -97.6789, "austin",  "secondary"),
    ("cedar-park",     "Cedar Park",    30.5052, -97.8203, "austin",  "secondary"),
    ("pflugerville",   "Pflugerville",  30.4394, -97.6200, "austin",  "secondary"),
    ("georgetown",     "Georgetown",    30.6333, -97.6779, "austin",  "secondary"),
    ("san-marcos",     "San Marcos",    29.8833, -97.9414, "austin",  "secondary"),
    ("dallas",         "Dallas",        32.7767, -96.7970, "dfw",     "primary"),
    ("fort-worth",     "Fort Worth",    32.7555, -97.3308, "dfw",     "primary"),
    ("plano",          "Plano",         33.0198, -96.6989, "dfw",     "secondary"),
    ("frisco",         "Frisco",        33.1507, -96.8236, "dfw",     "secondary"),
    ("arlington",      "Arlington",     32.7357, -97.1081, "dfw",     "secondary"),
    ("irving",         "Irving",        32.8140, -96.9489, "dfw",     "secondary"),
    ("san-antonio",    "San Antonio",   29.4241, -98.4936, "south",   "primary"),
    ("new-braunfels",  "New Braunfels", 29.7030, -98.1245, "south",   "secondary"),
    ("houston",        "Houston",       29.7604, -95.3698, "gulf",    "primary"),
]

# Load Texas geometry
TX = json.loads(Path("/tmp/tx.geojson").read_text())

# Find the largest polygon (mainland Texas) - skip island/exclave bits
def all_rings(geom):
    """Yield all (ring) polygon coordinate lists from a Feature or geometry."""
    if "geometry" in geom:
        geom = geom["geometry"]
    t = geom["type"]
    coords = geom["coordinates"]
    if t == "Polygon":
        yield from coords  # each ring
    elif t == "MultiPolygon":
        for poly in coords:
            yield from poly

# Pick the ring with the most points (mainland Texas outer ring)
rings = list(all_rings(TX["features"][0] if "features" in TX else TX))
mainland = max(rings, key=len)
print(f"Mainland ring: {len(mainland)} points")

# Simplify (Douglas-Peucker-ish): keep every Nth point
def simplify_step(ring, target=180):
    n = len(ring)
    if n <= target:
        return ring
    step = max(1, n // target)
    out = ring[::step]
    if out[-1] != ring[-1]:
        out.append(ring[-1])
    return out

ring = simplify_step(mainland, 200)
print(f"Simplified to {len(ring)} points")

# Get bounding box from ring
lons = [p[0] for p in ring]
lats = [p[1] for p in ring]
LON_MIN, LON_MAX = min(lons), max(lons)
LAT_MIN, LAT_MAX = min(lats), max(lats)

# Add a touch of padding
PAD = 0.4
LON_MIN -= PAD; LON_MAX += PAD
LAT_MIN -= PAD; LAT_MAX += PAD

print(f"Bounds: lon {LON_MIN:.2f}..{LON_MAX:.2f}, lat {LAT_MIN:.2f}..{LAT_MAX:.2f}")

# SVG viewBox - tight to the state aspect ratio
ASPECT = (LON_MAX - LON_MIN) / (LAT_MAX - LAT_MIN)
H = 760
W = int(H * ASPECT)
print(f"SVG {W} x {H} (aspect {ASPECT:.3f})")

def project(lat, lon):
    x = (lon - LON_MIN) / (LON_MAX - LON_MIN) * W
    # latitude correction at ~31N to keep horizontal scale proportional
    y = (LAT_MAX - lat) / (LAT_MAX - LAT_MIN) * H
    return x, y

def outline_path(ring):
    pts = [project(p[1], p[0]) for p in ring]
    d = f"M {pts[0][0]:.1f} {pts[0][1]:.1f}"
    for x, y in pts[1:]:
        d += f" L {x:.1f} {y:.1f}"
    d += " Z"
    return d


def build_svg():
    outline = outline_path(ring)

    # Manual label offsets (dx, dy, anchor) for primary metros to avoid overlap
    # Push labels far enough to clear the secondary-pin cluster around each metro
    LABEL_OFFSETS = {
        "austin":      (-16, 4, "end"),       # left of pin
        "dallas":      (18, 4, "start"),      # right of pin
        "fort-worth":  (-18, 4, "end"),       # left of pin
        "san-antonio": (-16, 4, "end"),       # left of pin
        "houston":     (18, 4, "start"),      # right of pin
    }

    pins = []
    for slug, name, lat, lon, region, prio in CITIES:
        x, y = project(lat, lon)
        size = 7 if prio == "primary" else 4.5
        if prio == "primary":
            dx, dy, anchor = LABEL_OFFSETS.get(slug, (0, -16, "middle"))
            lx, ly = x + dx, y + dy
            # Render twice for halo effect: outer stroke + inner fill
            label_html = (
                f'<text x="{lx:.1f}" y="{ly:.1f}" class="pin-label pin-label-primary pin-label-halo" text-anchor="{anchor}">{name}</text>'
                f'<text x="{lx:.1f}" y="{ly:.1f}" class="pin-label pin-label-primary" text-anchor="{anchor}">{name}</text>'
            )
        else:
            label_html = f'<text x="{x:.1f}" y="{y - size - 8:.1f}" class="pin-label pin-label-secondary" text-anchor="middle">{name}</text>'
        pin = f'''<a href="locations/{slug}.html" class="map-pin map-pin-{prio} map-pin-{region}" aria-label="{name}">
          <circle cx="{x:.1f}" cy="{y:.1f}" r="{size + 8}" class="pin-halo"/>
          <circle cx="{x:.1f}" cy="{y:.1f}" r="{size}" class="pin-dot"/>
          {label_html}
        </a>'''
        pins.append(pin)

    pins_html = "\n        ".join(pins)

    return f'''<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Texas service area map" class="tx-map">
        <defs>
          <linearGradient id="texasFill" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#10243a"/>
            <stop offset="100%" stop-color="#0a1a2c"/>
          </linearGradient>
        </defs>
        <path d="{outline}" fill="url(#texasFill)" stroke="#c9a64b" stroke-width="1.5" stroke-linejoin="round" />
        {pins_html}
      </svg>'''


if __name__ == "__main__":
    svg = build_svg()
    out = Path("/home/user/workspace/hcfs/images/texas-map.svg")
    out.write_text(svg)
    print(f"wrote {out} ({len(svg)} bytes)")
