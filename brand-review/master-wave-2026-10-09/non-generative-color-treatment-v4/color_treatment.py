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

# Currents run as contour lines across the swell: they rise along its face,
# bend over the shoulder, then curl down toward the barrel, not along its axis.
ribbons = [
    # Long C-shaped paths climb the face and curl over the shoulder.
    ([(500,555),(650,520),(790,455),(900,370),(990,295),(1060,245),
      (1120,230),(1175,252),(1220,300),(1245,365)],
     (25,220,245), 0.26, 1.5, 16, 16),
    ([(520,575),(675,545),(810,485),(915,410),(1000,345),(1070,300),
      (1130,290),(1180,315),(1215,355)],
     (25,220,245), 0.19, 1.0, 11, 12),
    # Green flow bends with the curl beneath the rising candles.
    ([(545,562),(700,525),(835,455),(940,375),(1020,315),(1085,280),
      (1140,282),(1185,315)],
     (63,245,118), 0.24, 1.0, 13, 13),
    ([(575,548),(725,505),(855,430),(955,350),(1030,295),(1090,270),
      (1140,280),(1175,320)],
     (35,210,245), 0.19, 0.8, 9, 10),
    ([(500,585),(650,565),(785,520),(895,460),(990,410),(1070,385),
      (1135,398)],
     (151,100,248), 0.15, 0.8, 8, 10),
    # A curved leading trace continues around the barrel's outer shoulder.
    ([(1130,300),(1170,315),(1210,350),(1245,395),(1275,435)],
     (35,210,245), 0.18, 4.0, 10, 9),
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

