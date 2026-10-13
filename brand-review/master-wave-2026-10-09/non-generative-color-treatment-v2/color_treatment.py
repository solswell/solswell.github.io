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

def bezier(p0, p1, p2, p3, steps=100):
    points = []
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u**3*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t**3*p3[0]
        y = u**3*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t**3*p3[1]
        points.append((round(x*scale), round(y*scale)))
    return points

# Surface currents begin in the surrounding ocean and gather under the
# existing candle progression as the swell rises.
ribbons = [
    ([(405,557),(620,544),(820,470),(1035,354)],
     (25,220,245), 0.24, 1.5, 13, 14),
    ([(468,563),(650,550),(830,505),(1000,433)],
     (25,220,245), 0.18, 1.0, 8, 11),
    ([(485,550),(680,515),(865,378),(1032,292)],
     (63,245,118), 0.23, 1.0, 10, 12),
    # Cyan upper stream converges toward the swell's leading curl.
    ([(535,532),(720,455),(895,330),(1058,258)],
     (35,210,245), 0.19, 0.8, 8, 9),
    ([(470,565),(635,565),(790,510),(930,440)],
     (151,100,248), 0.17, 0.8, 7, 9),
    # A short current follows the inner curl without crossing its symbol.
    ([(1120,274),(1190,292),(1218,360),(1275,405)],
     (35,210,245), 0.20, 4.0, 10, 9),
    # The distant RAY swell receives a much quieter echo of the same flow.
    ([(25,496),(116,482),(218,457),(300,429)],
     (45,210,236), 0.17, 0.6, 5, 7),
    ([(270,510),(316,516),(358,507),(397,485)],
     (151,100,248), 0.13, 0.5, 3.5, 6),
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
    points = bezier(*controls, steps=180)
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

