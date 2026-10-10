# SOLSWELL non-generative color treatment

This package applies SOLSWELL color accents to the clean realistic-water source with deterministic image processing. No image generation, resampling, sharpening, or water reconstruction was used.

## Deliverables

- `solswell-color-treated-master.png` — review result at the source's native **1672 × 941**.
- `solswell-color-treatment-comparison.png` — original on the left, treated version on the right, both at native size.
- `solswell-clean-water-source.png` — byte-for-byte copy of the clean source used as the base.
- `color_treatment.py` — reproducible overlay operation.

## What was applied

Eight smooth cubic paths were drawn on transparent high-resolution layers: one cyan current across the main swell in three continuous segments, two green traces, one restrained purple accent, one cyan trace on the distant swell, and one short purple accent in the valley. The paths were sampled smoothly, composited with low opacity and a soft 10 px blur, then blended over the source. No color grade or filter was applied to the whole image.

## Water pixel preservation

The original source file is preserved unchanged and used directly as the composite base. Its water shape, texture, foam, spray, reflections, symbols, candles, and underwater silhouettes were not regenerated, warped, sharpened, or resampled.

In the finished composite, RGB values change only where the translucent current ribbons and their soft halos blend over the source. Outside those overlay areas, the image pixels remain identical to the source. The comparison shows exactly where those accents sit.

This is a review candidate only. The approved V4 profile, website, X account, and live branding were not changed.

