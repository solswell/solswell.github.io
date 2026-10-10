# SOLSWELL final branding and website review

This review build preserves the approved Cool Mist V4 profile source and V9 master-banner source under `brand-review/` and integrates non-destructive copies into `assets/`.

## High-resolution V10 delivery pass

The V9 source/export dimensions were 1536 × 1024 (master), 1920 × 900 (website hero), and 1500 × 500 (X banner). The website was also rendering a second `background-size: cover` copy behind the visible hero image. V10 removes that duplicate render and uses a constrained enhancement candidate plus responsive delivery assets:

- `assets/solswell-master-banner-v10-hero-2x.png` — 3840 × 1800 desktop hero
- `assets/solswell-master-banner-v10-hero-1920x900.png` — standard desktop preview
- `assets/solswell-master-banner-v10-x-2x.png` — 3000 × 1000 X banner
- `assets/solswell-master-banner-v10-x-1500x500.png` — standard X banner preview
- `assets/solswell-master-banner-v10-mobile.png` — 900 × 1200 mobile crop
- `assets/solswell-v9-v10-quality-comparison.png` — native-crop before/after review

The enhancement reduces visible stair-stepping and raster noise in currents, candles and spray, but it does not create true new photographic detail. The remaining cellular/honeycomb texture is inherited from the approved artwork and may need a future direct art retouch if it remains unacceptable at 100% zoom.

## Included

- V9 cinematic hero with approved slogan: **Ride the chop. Catch the swell.**
- One Ocean / Many Currents positioning and six participant archetypes
- Proposed SOLSWELL Engine section for SOLSWELL / JitoSOL, SOL 2× LONG + RAY 1× LONG, 50/50 collateral, intended JitoSOL rewards and separate revenue flows
- Cross-margin, leverage, liquidation and unverified-mechanics disclosures
- Prelaunch FAQ and review-only roadmap
- X banner/avatar composition preview and proposed bio/pinned post in `x-package/`

## QA

- Verified required assets, HTML content anchors, internal X links, prelaunch labels and `git diff --check`.
- Layout uses the existing responsive CSS plus mobile breakpoints for the Engine and FAQ grids.
- No local browser executable was available in this environment, so desktop/mobile image screenshots are represented by the responsive `x-package/x-header-preview.html` and the V10 mobile/desktop assets; browser-level screenshot capture remains an approval-stage check.

## Guardrails

No token address, APY, returns, completed payouts, or live launch claim is included. PERPSPAD, JitoSOL and RAY mechanics are explicitly proposed and subject to verification. No live website or X account was changed.
