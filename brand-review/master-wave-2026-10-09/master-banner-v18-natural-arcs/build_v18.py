from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter


ROOT = Path(__file__).parent
SOURCE = ROOT.parent / "master-banner-v14-natural-water" / "solswell-v14-natural-water-master.png"
MASTER = ROOT / "solswell-master-banner-v18-natural-arcs.png"
HERO = ROOT / "solswell-master-banner-v18-website-hero-1600x900.png"
X_BANNER = ROOT / "solswell-master-banner-v18-x-1500x500.png"
COMPARISON = ROOT / "solswell-v14-vs-v18-natural-arcs.png"


def bezier(points: list[tuple[float, float]], steps: int = 160) -> list[tuple[int, int]]:
    """Sample a cubic Bezier path for a clean, continuous light ribbon."""
    a, b, c, d = points
    sampled: list[tuple[int, int]] = []
    for index in range(steps + 1):
        t = index / steps
        u = 1 - t
        x = u**3 * a[0] + 3 * u**2 * t * b[0] + 3 * u * t**2 * c[0] + t**3 * d[0]
        y = u**3 * a[1] + 3 * u**2 * t * b[1] + 3 * u * t**2 * c[1] + t**3 * d[1]
        sampled.append((round(x), round(y)))
    return sampled


def ribbon(size: tuple[int, int], points: list[tuple[float, float]], color: tuple[int, int, int], core_width: int, glow_width: int, opacity: int) -> Image.Image:
    """Create one isolated arc: a dim water-borne halo and a sharp core."""
    path = bezier(points)
    glow = Image.new("RGBA", size, (0, 0, 0, 0))
    ImageDraw.Draw(glow).line(path, fill=(*color, round(opacity * 0.30)), width=glow_width, joint="curve")
    glow = glow.filter(ImageFilter.GaussianBlur(radius=max(4, glow_width // 5)))
    core = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(core)
    draw.line(path, fill=(*color, opacity), width=core_width, joint="curve")
    draw.line(path, fill=(235, 255, 255, round(opacity * 0.52)), width=max(1, core_width // 4), joint="curve")
    return Image.alpha_composite(glow, core)


def crop_cover(image: Image.Image, target: tuple[int, int], focal: tuple[float, float]) -> Image.Image:
    """Crop around the barrel so all three arcs remain visible at banner sizes."""
    source_width, source_height = image.size
    target_width, target_height = target
    scale = max(target_width / source_width, target_height / source_height)
    resized = image.resize((round(source_width * scale), round(source_height * scale)), Image.Resampling.LANCZOS)
    width, height = resized.size
    center_x = focal[0] * scale
    center_y = focal[1] * scale
    left = max(0, min(round(center_x - target_width / 2), width - target_width))
    top = max(0, min(round(center_y - target_height / 2), height - target_height))
    return resized.crop((left, top, left + target_width, top + target_height))


def main() -> None:
    base = Image.open(SOURCE).convert("RGBA")
    size = base.size
    # Deliberately only three independent arcs. No water-wide texture or glow is applied.
    arcs = [
        ribbon(size, [(1105, 490), (1190, 320), (1325, 245), (1465, 345)], (54, 225, 255), 5, 28, 188),
        ribbon(size, [(1125, 510), (1215, 385), (1345, 315), (1450, 420)], (81, 255, 165), 4, 22, 166),
        ribbon(size, [(1085, 540), (1195, 505), (1305, 505), (1435, 555)], (142, 82, 255), 4, 22, 150),
    ]
    treated = base
    for arc in arcs:
        treated = Image.alpha_composite(treated, arc)
    treated.convert("RGB").save(MASTER, optimize=True)
    crop_cover(treated, (1600, 900), focal=(1010, 450)).convert("RGB").save(HERO, optimize=True)
    crop_cover(treated, (1500, 500), focal=(1010, 390)).convert("RGB").save(X_BANNER, optimize=True)
    comparison = Image.new("RGB", (size[0] * 2, size[1]), (8, 17, 34))
    comparison.paste(base.convert("RGB"), (0, 0))
    comparison.paste(treated.convert("RGB"), (size[0], 0))
    comparison.save(COMPARISON, optimize=True)


if __name__ == "__main__":
    main()
