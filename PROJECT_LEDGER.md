# SOLSWELL — Project Ledger

**Status:** Working baseline for review, 2026-10-11. **Not a token-launch announcement or deployment approval.**  
**Repository:** https://github.com/solswell/solswell.github.io  
**Public website:** https://solswell.github.io/  
**Public X:** https://x.com/SolSwellOcean  
**Existing art/website review:** [Draft PR #1](https://github.com/solswell/solswell.github.io/pull/1) (`review/master-wave-2026-10-09`).  
**Asset provenance:** [ARTWORK_REGISTER.md](ARTWORK_REGISTER.md). **Agent working rules:** [AGENTS.md](AGENTS.md).

## 1. Business objective and decision roles

**Actual goal:** Launch a distinctive SOLSWELL meme coin on Solana, grow community interest and participation, and seek a commercially viable creator/project income stream **without promising profits or returns**. Keep upfront spending and avoidable AI/tool usage low. Branding, site, token mechanics and launch preparation serve this goal; none is an end in itself.

- **Project owner:** Establishes vision, approves major decisions, final brand assets, public communications, deployment and token-related actions.
- **ChatGPT/planner:** Maintain project context, research and verify dependencies, coordinate tasks, review deliverables against *all* requirements, and report actual status with evidence.
- **Codex/implementer:** Execute bounded, approved tasks. Do not independently change creative direction or treat experimental output as approved.
- **Recordkeeping:** A user decision is not equivalent to a shipped implementation. A new commit, generated image or crop is not an approval.

## 2. Repository and production state — observed 2026-10-11

| Surface | Observed state | Interpretation / remaining verification |
| --- | --- | --- |
| `main` | HEAD `48dc2edc27d0f011455fcba5b32f6f8e969073a4` at audit. `index.html` still says “Get ready for the next SOLSWELL,” includes “Meet Sol,” uses `assets/04-launch-poster.webp` as hero poster and `assets/solswell-avatar.webp` for its shark character. The hero background is CSS gradients. | This is the **production-source branch**, not the approved new identity. Confirm exact GitHub Pages deployment SHA separately if needed. |
| Public site | https://solswell.github.io/ | Previously observed with older branding. Exact live-deployed SHA was **not independently pinned** in this baseline audit. Do not assume the latest review art is live. |
| PR #1 | OPEN, DRAFT, not merged; head `4618d27566c1149995da3060740d8a44fb85c9d0` at audit; 30 commits and 157 changed files. | Experiments, review files and proposed site redesign **only**. Do not merge/deploy without owner's approval. |
| PR #1 website HTML | Has the newer slogan and proposed Engine section, but **still contains the “Meet Sol” section**. | Review branch is **not** yet internally consistent with the wave-first direction. |
| X profile | https://x.com/SolSwellOcean | Public account identified; current live imagery and bio **not reverified** in this audit. Draft X assets/copy do not establish actual X changes. |
| Recent ChatGPT-made images | Square and wide ocean brand candidates were generated directly in chat around Oct 10–11. | **Not verified present in GitHub and not approved as final masters.** Transfer to repo only after owner selects/approves an actual file. |

Nothing in this baseline approves PR #1, the most recent generated images, an X update, a website launch, or a token launch.

## 3. Brand decisions (owner-established direction; implementation may lag)

- **Name:** SOLSWELL.
- **Slogan:** **“Ride the chop. Catch the swell.”** Retire the older “Get ready for the next SOLSWELL” from a future approved redesign.
- **Master identity:** **The wave itself is the brand**, not a shark mascot. “Sol the shark” belongs only to superseded material; marine creatures are secondary ecosystem archetypes.
- **Ecosystem:** Whales/investors, sharks/traders, turtles/liquidity providers, squids/builders, minnows/smaller participants, and the storm/degen energy. Small supporting visual details, not primary marks.
- **Palette and feel:** Deep ocean blues with emerald green, cyan/teal and restrained purple. Premium cinematic natural-water realism; believable foam, spray and liquid translucency. Avoid faceted, broken-glass or cellular water texture.
- **Hero/banner visual hierarchy:** TWO **separate, unmistakable breaking barrel waves** traveling left to right. **SOL leads** as the huge foreground/forward wave; **RAY trails behind** as a smaller, still recognizable separate barrel. A water ridge does **not** fulfill the second-wave requirement.
- **Motifs:** A rising, legible sequence of green candlesticks integrated with wave momentum; a recognizable Solana-inspired compact staggered three-parallelogram emblem within the SOL barrel, **not** generic horizontal lines; subtle RAY symbolism associated with its trailing barrel. Do not imply official project endorsement or partnership; verify trademark/branding usage before public launch.
- **Underwater world:** Quiet silhouettes or depictions of whale, shark, turtle, squid and schooling minnows below the waterline, subordinate to both waves.
- **Profile direction:** “Cool Mist V4” was selected as the working/approved **profile direction** in discussion; its repo README still labels it review-only. This does **not** authorize publishing it or supersede any later explicit approval.
- **Approval distinction:** The two directly chat-generated images are **review candidates**, not automatic replacements for Cool Mist V4, a new website master, or the X header.

## 4. Product and launch mechanics — proposed, NOT verified/live

- **Working launch venue:** PERPSPAD; do not claim platform support for launch options without checking an actual compatible transaction path/current documentation.
- **Working pool/quote pairing:** SOLSWELL / JitoSOL. JitoSOL has reportedly appeared in the token selector; that alone **does not prove** Meteora bonding curve compatibility or dividend eligibility.
- **Working perp exposure:** Equal collateral across **SOL 2× LONG** and **RAY 1× LONG** legs (combined initial gross exposure approximately 1.5× collateral). This is **a proposal, not a trade**; margin, liquidation and maintenance rules need verification.
- **Working rewards/fees concept:** Intended JitoSOL holder distributions and distinct creator/platform/buyback/collateral flows, subject to verified PERPSPAD rules and economic risk review. Do not promise dividends, APY, price support, earnings or sustainability.
- **Launch state:** Prelaunch. No verified live SOLSWELL token mint, live rewards engine, executed perp basket, or approved token launch is documented here. Do not invent token addresses, trading links or financial results.

## 5. Workstreams and gates

| Workstream | Current gate | Next authorized type of work |
| --- | --- | --- |
| Brand assets | Direction established; final banner still **unapproved** | Compare actual candidates against full spec; owner approves the exact master asset |
| Website | Existing production-source site reflects older identity; draft redesign partly inconsistent | Audit preview and remove superseded messaging **only after scoped approval** |
| X | Draft copy/crops in PR #1; live state not checked | Verify live profile; update only after asset + copy approval |
| Token mechanics | Proposed, financially risky, several dependencies unverified | Read-only verification of venue, pool, fee/reward and margin requirements |
| Launch operations | Not launched | Develop launch checklist, budgets and safety disclosures; require explicit owner go/no-go |
| Documentation | This branch introduces `PROJECT_LEDGER.md`, `ARTWORK_REGISTER.md`, `AGENTS.md` | Review and merge docs separately from artwork PR, with approval |

## 6. Immediate priorities (no implicit permission to execute)

1. Review this baseline and correct any owner decisions that were misclassified.
2. Keep docs-only baseline separate from PR #1; if approved, merge documentation independently.
3. Complete an evidence-based art inventory/provenance review before selecting a definitive master.
4. Confirm live website Pages SHA and X account imagery before proposing updates.
5. Verify PERPSPAD/JitoSOL/perp mechanics before promising them publicly.

## 7. Evidence and uncertainty rules

- Repository file contents and commits are **observed evidence**; readme claims about how an image was generated are **producer reports**, unless independently checked against actual generation inputs.
- Track **planned / review / approved / merged / deployed / verified live** as separate states.
- Update this ledger when a material decision or GitHub state changes. Record date, relevant link/SHA, what was checked, and what remains uncertain.
- Never silently promote an experiment to a milestone.
