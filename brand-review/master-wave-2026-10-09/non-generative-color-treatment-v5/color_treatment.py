from pathlib import Path
import math
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "solswell-clean-water-source.png"
OUTPUT = ROOT / "solswell-color-treated-master.png"
COMPARISON = ROOT / "solswell-color-treatment-comparison.png"

base = Image.open(SOURCE).convert("RGBA")
width, height = base.size
scale = 3
overlay_hi = Image.new("RGBA", (width * scale, height * scale), (0, 0, 0, 0))

def curved_path(anchors, steps_per_arc=42):
    """Smoothly pass through waypoints so current follows the swell contour."""
    points = []
    for segment in range(len(anchors) - 1):
        p0 = anchors[max(0, segment - 1)]
        p1 = anchors[segment]
        p2 = anchors[segment + 1]
        p3 = anchors[min(len(anchors) - 1, segment + 2)]
        for index in range(steps_per_arc + 1):
            if segment and index == 0:
                continue
            t = index / steps_per_arc
            t2, t3 = t*t, t*t*t
            x = 0.5 * ((2*p1[0]) + (-p0[0]+p2[0])*t +
                       (2*p0[0]-5*p1[0]+4*p2[0]-p3[0])*t2 +
                       (-p0[0]+3*p1[0]-3*p2[0]+p3[0])*t3)
            y = 0.5 * ((2*p1[1]) + (-p0[1]+p2[1])*t +
                       (2*p0[1]-5*p1[1]+4*p2[1]-p3[1])*t2 +
                       (-p0[1]+3*p1[1]-3*p2[1]+p3[1])*t3)
            points.append((round(x*scale), round(y*scale)))
    return points

# Energy climbs vertically up the outside of the barrel-like swell. Each
# separate updraft curves with the turning surface and terminates at a candle.
ribbons = [
    # Each filament has little sideways drift: it rises from the lower face
    # and ends at the lower wick/body of one successive candle.
    ([(640,565),(628,525),(642,486),(650,448)],
     (25,220,245), 0.31, 1.4, 11, 15),
    ([(725,552),(744,512),(735,467),(754,414)],
     (63,245,118), 0.33, 1.4, 12, 16),
    ([(810,520),(828,477),(817,425),(835,365)],
     (25,220,245), 0.34, 1.4, 13, 17),
    ([(895,475),(916,430),(908,375),(927,310)],
     (63,245,118), 0.35, 1.4, 15, 19),
    ([(980,415),(997,365),(987,315),(1004,264)],
     (25,220,245), 0.36, 1.4, 17, 21),
    ([(1045,350),(1062,308),(1052,262),(1068,218)],
     (63,245,118), 0.37, 1.4, 18, 22),
    # Restrained purple remains a low supporting current on the wave face.
    ([(535,574),(590,568),(640,565)],
     (151,100,248), 0.12, 0.6, 4, 7),
    # A quiet arc-following echo sits on the distant RAY swell.
    ([(24,500),(85,490),(150,470),(210,450),(255,438),(300,429)],
     (45,210,236), 0.16, 0.6, 5, 7),
    ([(270,512),(310,502),(350,493),(375,488),(397,485)],
     (151,100,248), 0.12, 0.5, 3.5, 6),
]

def paint_tapered_ribbon(draw, points, color, opacity, start_width, max_width, glow_px=0):
    count = len(points)
    for index in range(count - 1):
        t = index / (count - 1)
        edge = min(1.0, t / 0.16, (1.0-t) / 0.12)
        edge = max(0.0, edge)
        width_px = (start_width + (max_width-start_width)*t) * edge
        alpha = round(255 * opacity * (0.24 + 0.76*t) * edge)
        if alpha <= 0:
            continue
        segment = [points[index], points[index+1]]
        width_hi = max(1, round(width_px*scale))
        if glow_px:
            draw.line(segment, fill=(*color, round(alpha*0.38)),
                      width=width_hi + round(glow_px*scale), joint="curve")
        else:
            draw.line(segment, fill=(*color, alpha), width=width_hi, joint="curve")

# Paint smooth, tapered bands on transparent layers; no source texture is drawn.
glow = Image.new("RGBA", overlay_hi.size, (0,0,0,0))
glow_draw = ImageDraw.Draw(glow)
core_draw = ImageDraw.Draw(overlay_hi)
for controls, color, opacity, start_width, max_width, glow_px in ribbons:
    points = curved_path(controls)
    paint_tapered_ribbon(glow_draw, points, color, opacity, start_width, max_width, glow_px)
    paint_tapered_ribbon(core_draw, points, color, opacity, start_width, max_width)

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

