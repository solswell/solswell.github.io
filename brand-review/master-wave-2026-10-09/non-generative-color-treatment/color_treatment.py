from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "solswell-clean-water-source.png"
OUTPUT = ROOT / "solswell-color-treated-master.png"
COMPARISON = ROOT / "solswell-color-treatment-comparison.png"

base = Image.open(SOURCE).convert("RGBA")
width, height = base.size
scale = 3
overlay_hi = Image.new("RGBA", (width * scale, height * scale), (0, 0, 0, 0))

def bezier(p0, p1, p2, p3, steps=100):
    points = []
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u**3*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t**3*p3[0]
        y = u**3*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t**3*p3[1]
        points.append((round(x*scale), round(y*scale)))
    return points

def path(controls):
    return bezier(*controls)

# Smooth, sparse ribbons follow the existing water flow. These are vector-like
# overlays composited above the untouched photograph; no source texture is drawn.
ribbons = [
    # Long cyan current follows the lower front of the dominant rising swell.
    ([(420,548),(570,538),(670,517),(785,501)],
     (25,220,245), 0.43, 2.8, 12),
    ([(785,501),(900,485),(1010,458),(1090,419)],
     (25,220,245), 0.43, 2.8, 12),
    ([(1090,419),(1135,399),(1172,378),(1200,350)],
     (25,220,245), 0.32, 2.5, 11),
    # A restrained green stream runs parallel on the darker face.
    ([(540,553),(650,548),(760,535),(865,516)],
     (63,245,118), 0.38, 2.5, 11),
    ([(865,516),(955,500),(1030,478),(1085,451)],
     (63,245,118), 0.38, 2.5, 11),
    # Purple accent is short and low on the main swell.
    ([(450,563),(555,577),(655,572),(746,555)],
     (151,100,248), 0.32, 2.4, 10),
    # Fine cyan and purple traces connect visually with the distant swell.
    ([(24,487),(102,476),(171,458),(237,438)],
     (45,210,236), 0.32, 2.0, 8),
    ([(330,518),(385,528),(440,528),(491,515)],
     (151,100,248), 0.25, 1.8, 7),
]

# Paint only continuous, smoothly sampled paths on transparent layers.
glow = Image.new("RGBA", overlay_hi.size, (0,0,0,0))
glow_draw = ImageDraw.Draw(glow)
core_draw = ImageDraw.Draw(overlay_hi)
for segments, color, opacity, width_px, glow_px in ribbons:
    points = path(segments)
    alpha = int(255 * opacity)
    glow_draw.line(points, fill=(*color, int(alpha * 0.48)), width=round(glow_px*scale), joint="curve")
    core_draw.line(points, fill=(*color, alpha), width=round(width_px*scale), joint="curve")

# Broad, gentle halo only; the sharp source water remains visible underneath.
glow = glow.filter(ImageFilter.GaussianBlur(10 * scale))
overlay_hi = Image.alpha_composite(glow, overlay_hi).resize((width,height), Image.Resampling.LANCZOS)
treated = Image.alpha_composite(base, overlay_hi).convert("RGB")
treated.save(OUTPUT)

# Comparison keeps the source and treatment side by side at native scale.
comparison = Image.new("RGB", (width*2, height), (8,16,31))
comparison.paste(base.convert("RGB"), (0,0))
comparison.paste(treated, (width,0))
comparison.save(COMPARISON)

print(f"Source: {width}x{height}")
print(f"Saved: {OUTPUT.name}, {COMPARISON.name}")

