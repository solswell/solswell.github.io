# SOLSWELL Artwork Register — provenance and approval

**Audit date:** 2026-10-11. This register is a **classification of known assets**, not an approval. Direct generation records are not independently recoverable from saved readmes unless accompanied by original tool execution evidence. See [PROJECT_LEDGER.md](PROJECT_LEDGER.md).

## Rules and vocabulary

- **Fresh text-only generation:** A *new* image created from a text prompt with **no image inputs**. A saved prompt claiming this is a *documented claim*, not independently verified provenance.
- **Reference-guided generation:** A new rendered image that received one or more other images as inputs, even if the pixels were not copied literally.
- **Edit / composite:** An image derived by changing, drawing over, grading, inpainting or compositing an existing image; **not** a fresh generation.
- **Crop / resize / upscale:** A derived export; cannot turn a smaller native source into truly captured native image detail.
- **Approved direction** and **approved final asset** are distinct. Nothing becomes public by appearing in a review branch.

## Known history

| Asset / sequence | Repository evidence | Recorded origin | Current approval / caution |
| --- | --- | --- | --- |
| Initial profile concept boards and Cool Mist direction | `brand-review/master-wave-2026-10-09/` in draft PR #1 | Multiple concept generations and controlled refinements recorded in markdown. | Historic direction exploration. |
| Cool Mist profile V4 | `brand-review/master-wave-2026-10-09/profile-refinement-v4/solswell-cool-mist-profile-tight-v4.png` | Existing profile V3 reframed and polished; repo README says 1254×1254. | Owner-selected **profile direction** in chat; file still marked review-only; no confirmed live deployment. |
| Banner master V1–V9 | `brand-review/master-wave-2026-10-09/master-banner-2026-10-09/` | A generated master followed by multiple targeted edits/refinements and crop exports; README traces each. | Iterative visual experiments, **not nine proven independent fresh generations**. Not final approved. |
| V10 website/X delivery exports | `assets/solswell-master-banner-v10-*` and `WEBSITE-REVIEW.md` on PR #1 | Enlargements/enhancement/responsive crops derived from V9. The review notes explicitly deny creation of true original 4K detail. | Not a native photographic 4K master and not merged to production. |
| V12 and V13 candidates | `brand-review/master-wave-2026-10-09/master-banner-v12-r-and-upright-candles/`, `master-banner-v13-smooth-barrel/` | Stored prompts and readmes; V13 described as a targeted smoothing pass to V12. | Not approved; see originals for exact source claims. |
| V14 natural-water | `brand-review/master-wave-2026-10-09/master-banner-v14-natural-water/` | `GENERATION-PROMPT.md` claims a text-only built-in generation, no image input; README reports 1672×941 native. | **Reported fresh**, not independently authenticated generator payload; not native 4K, not approved. |
| V17 clean-current | `brand-review/master-wave-2026-10-09/master-banner-v17-clean-current/` | `GENERATION-PROMPT.md` explicitly identifies two reference inputs: realistic water and Cool Mist V4 palette; README reports 1672×941 native. | **Reference-guided**, not clean text-only; not approved. |
| Color treatment v1–v8 | `brand-review/master-wave-2026-10-09/non-generative-color-treatment*/` | Stored Python/process readmes documenting existing-image treatments and curves. | Derived experiments, **not independent new generations**. |
| V18 natural arcs | `brand-review/master-wave-2026-10-09/master-banner-v18-natural-arcs/` | README explicitly says V14 was the untouched base and `build_v18.py` drew three arcs without image generation. | **Composite/edit of V14**, never fresh. Not approved. |
| Recent square ChatGPT wave candidate | In conversation Oct 10–11, 2026; GitHub file **not established** | Image generated directly in chat; square composition, wave/candles/underwater ecosystem. | **Candidate**, not approved/repository-backed; require explicit source file transfer and decision. |
| Recent wide ChatGPT two-wave candidate | In conversation Oct 10–11, 2026; GitHub file **not established** | Image generated directly in chat, wide 1672×941 result; visible second wave, iconography and underwater creatures. | **Candidate**, not approved/repository-backed; do not silently replace existing site assets. |

### Evidence quality notes

- Repository source files and non-generative Python scripts can establish **which saved pixels were loaded and transformed**.
- Text prompts and readme statements establish **what a previous agent recorded**, **not conclusive proof** of the generation tool's actual hidden inputs.
- If reconstructing provenance for a candidate, seek original executed tool calls/image identifiers and hashes where available; otherwise label **unverified**.
- Do not infer missing version numbers correspond to lost independent generations or fabricate V15/V16 lineage.
- Live site `main` currently references an earlier poster (`assets/04-launch-poster.webp`); PR #1 HTML references V10 assets. Neither establishes a final approved brand image.

## Candidate gate before website/X use

For each proposed final file, append a dated record containing **full repo path, source tool and method, source image inputs (if any), SHA256, native dimensions, exact approved use(s), crop previews, reviewer decision and approval date**. Only **approved asset** status permits Codex to prepare a deployable website/X integration; **deploy still requires separate approval**.

Do not generate or edit images as part of updating this register.
