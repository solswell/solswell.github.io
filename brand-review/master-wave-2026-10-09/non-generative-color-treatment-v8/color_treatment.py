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

# Each trail is anchored at a candle's bottom wick, then wraps down and around
# the curved outside of the swell until it rejoins the surrounding water.
ribbons = [
    # Reverse V6's handedness: each path sweeps around the opposite side of
    # the tube, matching the visible curl of the wave from wick to water.
    ([(668,476),(644,486),(632,502),(648,519),(675,532)],
     (25,220,245), 0.31, 1.2, 13, 16),
    ([(786,438),(760,452),(746,474),(763,491),(795,510)],
     (63,245,118), 0.33, 1.2, 14, 17),
    ([(892,389),(866,403),(850,425),(872,445),(910,462)],
     (25,220,245), 0.34, 1.2, 15, 18),
    ([(958,354),(932,367),(914,389),(934,411),(974,432)],
     (63,245,118), 0.35, 1.2, 16, 19),
    ([(999,320),(973,334),(958,356),(978,380),(1020,400)],
     (25,220,245), 0.36, 1.2, 17, 20),
    ([(1074,290),(1048,303),(1034,325),(1053,348),(1090,370)],
     (63,245,118), 0.37, 1.2, 18, 22),
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
        # Keep a small visible contact at the wick anchor, then taper at the
        # water-surface endpoint; the path should visibly begin at the candle.
        edge = min(1.0, max(0.42, t / 0.12), (1.0-t) / 0.12)
        edge = max(0.0, edge)
        width_px = (start_width + (max_width-start_width)*t) * edge
        alpha = round(255 * opacity * (0.65 + 0.35*(1.0-t)) * edge)
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

