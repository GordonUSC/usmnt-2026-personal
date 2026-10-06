# Graphics, Canada guide and image review — October 6, 2026

Review branch: `codex/long-walk-graphics`. Base: `bda2412a463dd7bc1fc23d1dea3403b0216077c8`. This pass is not published.

## Reproduced problem and repair

The live walk and the eight-era run had different renderers. The walk loaded commissioned stadium/anime plates; the campaign renderer received only the final photograph and drew simpler scenes. The live campaign module was current and no service worker was present. The arcade's advertised run link also opened the free walk.

Both modes now use the shared visual module. The campaign receives the existing artwork, and every era has its own raster, palette, player construction and presentation. The early polygon scene uses projected 3D geometry. The final photo fits intact. Direct run entry resumes an existing checkpoint. Original walk, discovery and Couva storage keys remain intact. Era treatments are labeled as homages; their raster sizes are authored choices, not complete console specifications. See `ART-DIRECTION.md`.

## Canada: a welcoming visual guide

Three simple viewing questions lead to five scenes and fifteen inspectable stills: draw pressure, find the exit, attack the gap, cover the loss, and press together. All pitch diagrams identify themselves as tactical illustrations with selected roles, not a confirmed lineup, tracking data or a replay. Fixed attacking directions, team shapes and line styles distinguish passes, runs and pressure. The source explanation is separate from the editorial viewing question. Existing availability reconciliation and opponent profiles remain.

No autoplay or tutorial gate. Arrow/Home/End keys navigate the tabs; visible controls move through each still. All fifteen drawings remain readable without JavaScript and in print. The original `#duels` link still works.

## Image work and limits

- Twelve downloaded, inspected player photographs added to profile details with date, exact author/credit, source and license links. Their shirts are explicitly historical context, not a current-club claim. BY-SA derivatives retain the same license.
- Five researched originals/thumbnails were throttled by Wikimedia: Alex Freeman, Chris Richards, Matt Freese, Damion Downs and Frankie Westfield. They are not embedded. Neutral initials remain; `assets/players/credits.json` records candidate metadata and availability.
- Seven existing personal photographs were sideways. Upright WebP display copies are used while originals and author captions remain. No generative alteration to photographs.
- Intrinsic image dimensions corrected throughout the root pages; a public image-credit register is linked from the footer. The arcade preview is an actual capture of the revised HD stage.
- Every local raster was visually inspected in contact sheets; the inventory records dimensions, byte size, classification and referring pages in `image-audit.json`.
- All five legacy venue photographs now have verified source links, authors, dates and reuse terms in `assets/venue-credits.json` and the public image-credit page. Original image bytes are unchanged. The earlier audit overstated the gap: the original commit and surviving inline captions already recorded authors/licenses; the missing source-link verification is now complete.

## Verification

Evidence bundle: `evidence/graphics-fix/` in the delivery package.

- All eight actual campaign stages captured before and after; zero runtime errors after fixes.
- Real keyboard input completed all eight Club stages; the completed score persisted after reload.
- Deterministic Club and Pro runs: 16/16 passed; idle losses, retry state, held action and charged-shot cancellation checked.
- Deep link resumed an era-five checkpoint, retaining saved records and the exact original journey/Couva values.
- Guide: all 15 stills, all five show-all controls, keyboard tabs, no-JavaScript and print coverage.
- 390px and 320px layout and real touch checks; no horizontal overflow on the checked entry, squad, guide, credits and game pages.
- Static link/anchor/duplicate-ID audit: 49 HTML files, zero errors.
- Changed scripts pass syntax checks.

The unrelated `next/fall-2026.ics` working-tree normalization is excluded. No native Chrome, messages, credentials, deployment, merge or public push were used in this pass.

## Venue-source follow-up

SoFi: Troutfarm27, CC BY-SA 4.0 (2021-11-14). Levi’s: Matthew Roth, CC BY-SA 2.0 (2014-08-12). Azteca: AnatGutman, CC0 (2017-06-11). Olimpico: romazone, CC BY 2.0 (2014-05-11). Lumen: SounderBruce / Bruce Englehardt, CC BY-SA 4.0 (2019-07-20). All five match the existing assets visually; source metadata and local hashes are retained. A similarly named Lumen photograph was rejected because it did not match.

Audit lesson: inspect original commits, existing inline credits and embedded metadata before labeling an image unattributed. A missing central register is not the same as missing authorship or a missing license.

Follow-up checks: all five source photos visually matched; linked credit screens checked at 1440, 390 and 320 pixels; all five venue assets and existing player/art/display assets are byte-identical to the prior review. The compact review demos were exercised from `file://` with zero HTTP(S) requests and zero runtime errors. The Canada states, portrait decode, five venue images, actual game pass and HD/anime/photo rendering passed. The compact kit contains self-contained demos plus the complete production patch; it is explicitly not a deployment directory.
