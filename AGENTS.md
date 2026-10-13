# SOLSWELL — Instructions for Coding and Agent Work

> **Scope:** All work in this repository, on any branch. First read [PROJECT_LEDGER.md](PROJECT_LEDGER.md) and [ARTWORK_REGISTER.md](ARTWORK_REGISTER.md) if available on the working branch. If they are absent, inspect the baseline documentation PR/branch and verify the actual repository state instead of assuming an old chat summary is current.

## Roles and source of truth

- The **owner** decides brand direction, approves assets, token actions and public-facing changes.
- **ChatGPT/planning** researches, verifies, maintains an accurate ledger, evaluates delivery against the *complete* specification, and delegates bounded tasks.
- **Codex/implementation** performs specifically authorized coding, file preparation, and review changes. Never independently redefine the product.
- Preserve previous owner decisions unless explicitly revisited. If a decision is missing or contradictory, report the conflict **before** acting.
- The actual branch, file content, commit SHA, PR state and deployment evidence outrank assumptions. The ledger records decisions and expectations, but does not override contradictory facts about what is currently deployed.

## Mandatory work protocol

1. Inspect `main`, the task branch, relevant PRs, and ledger/asset register before editing.
2. State task **objective, exact inputs, output paths, acceptance criteria, safety boundaries and stop condition**.
3. Select the **lowest practical cost model** capable of completing the task and specify reasoning effort when applicable. Use actual available model names; do not invent model availability.
4. Make the **smallest reversible change** that meets the objective. One focused task per change where possible.
5. Validate against **every** mandatory requirement, not just the most recently discussed problem. Report passes, failures and unverified criteria separately.
6. Record exact paths, commit SHA, branch, PR URL, and whether anything was **merged, deployed or published**. Unless directly verified, say "not verified."
7. Stop at any missing permission, ambiguous requirement, failed gate, contradictory input, or risk of unapproved publication. Do not repeatedly retry while consuming credits.

## Git / publishing safety

- **Never commit to `main`, merge PRs, publish a website or X content, delete or overwrite approved originals, deploy or initiate token/financial operations without the owner's explicit authorization for that specific action.**
- Use a dedicated review branch and a **draft PR** for proposals.
- Preserve all old asset files for provenance. No destructive cleanup until a verified inventory and explicit approval.
- Do not conflate a repo upload, branch commit, review crop, pull request or merged commit with an actual GitHub Pages deployment.
- Do not treat draft website copy, token economics or candidate images as published facts.
- Solmate/SOLMATE is an independent older project under a different organization; do not modify or merge its assets without an explicitly scoped task.

## Image creation: strict fresh-generation boundary

When the user requests a **new image or new generation**:

- Create **from text only**: zero previous generated images, failed versions, profiles, banners, hidden visual references, reference attachments, or inherited image pixels.
- A filename change, crop, resize, composite, inpaint, reference-guided recreation and upscale **are not** a fresh generation.
- Do **not** include older SOLSWELL imagery as a palette or layout reference unless the user **explicitly overrides this rule** for that particular job.
- One planned generation per authorization. Do not chain corrections or variants without a new decision.
- Record exact prompt, any image inputs (expected **none**), generating tool/model when available, time, **native** pixel dimensions, generation ID where available, and file hash/path. Distinguish any separately derived crops.
- If actual image inputs cannot be inspected, say "input provenance unverified" instead of claiming text-only.
- Create images directly in ChatGPT when available; send only **owner-approved** finished files to Codex for file organization, transparent exports, crop previews and website integration. Do not route image creation through Codex by default.

If the owner explicitly authorizes an **edit** instead, label it an edit and log the exact source image and all transformations. Preserve the original unchanged.

## SOLSWELL art review: mandatory criteria

A candidate banner **fails overall** if any of these are absent or unresolved:

- Two visually distinct, recognizable **breaking barrels**, not one main wave and a distant ridge.
- The huge **SOL** wave leads as foreground/forward barrel; the smaller **RAY** barrel trails and remains recognizable.
- Natural-looking liquid ocean water, spray, foam, readable green/cyan/purple identity, no obvious broken-glass/cellular water material.
- Rising green candlestick progression integrated with the wave.
- An actually recognizable **staggered Solana-inspired three-parallelogram motif**, not three arbitrary horizontal bars, with understated RAY-associated imagery on the secondary barrel.
- Whale, shark, turtle, squid and school of minnows subtly below the waterline.
- Usable crops for website hero and X header. Check required details **in the actual crop**, not just in the full master.
- No false claims of official affiliation. Verify external visual-mark usage rights before publication.

For a profile/avatar candidate, check wave-first recognition, small circular crop (128/64/32px), no unintended mascot dominance, and the approved palette.

**Do not call partial technical improvement a successful final design.** Grade every required criterion. Clearly separate (a) improved from prior experiment, (b) compliant with design spec, and (c) explicitly owner-approved.

## Current economic/disclosure safety

SOLSWELL/JitoSOL pairing, holder rewards, PERPSPAD mechanics and the proposed SOL/RAY leveraged legs remain **unverified proposed mechanics**; do not announce them as live or promise profits, yields, incentives or buybacks. Do not invent mint addresses. Financial actions require separate authorization and preflight verification.

## Documentation discipline

- At the end of every meaningful milestone, update `PROJECT_LEDGER.md` and `ARTWORK_REGISTER.md` as relevant **on the same review branch** and include evidence links.
- Record status with distinct values: **candidate / direction approved / asset approved / merged / deployed / live verified**.
- Keep unverified facts marked unverified. Preserve exact source paths, SHAs and generation provenance instead of vague version names.
- If an audit discovers previously missed requirements, update the acceptance criteria before another attempt.

**Efficiency rule:** Do not spend new tool/image credits to repeat a known failed experiment when no causal variable or input changed.
