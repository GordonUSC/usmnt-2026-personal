# USMNT expansion · ready for review

This pass starts from published commit a6da597 (PR #2). It is a separate local review revision. No push, merge or deployment is included.

## What to try first
1. Open squad.html. Switch among the current 28, the 19-profile watchlist, and withdrawn players. Compare Hall and Downs; filter by official group, age, caps or club/name.
2. Open canada.html. Read the reconciled availability notes, change the three tactical viewing lenses, and inspect the 13 selected opponent profiles.
3. Open kits.html. Browse 28 historical studies, inspect collar/pattern detail, and compare 1994 Denim with 2026 Stars. Use the era and design-family filters.
4. Open arcade/belamini27.html. Start the 45-second drill. Call a runner with E, play C into his path, then hold/release X after the first touch settles. Touch equivalents are on the pad. Try the five fictional challenges and replay for stars.
5. Open arcade/longgame.html. Choose the eight-era run or practice a stage. Each has an objective, three chances, score, loss/retry and a different control problem. Free exploration and Gordon’s original story remain available.

## Verified behavior
- Isolated Chromium: the complete eight-stage Club campaign won through actual keyboard events, with score restored after reload. All eight stages also passed deterministic simulation on Club and Pro. Final renderer refinements changed drawing only.
- BelaMini27: actual keyboard and touch runner → through pass → settled shot at 390/320 pixels; one complete real-time Protect the Lead scenario reached the result screen and saved/restored its attempt and stars. All five scenarios terminate in simulation; scoring, sprint, pressing and deterministic replay were checked there.
- Old BelaMini26 storage stayed byte-identical. New records use belamini27_v1. Long Game challenge records use longgame_trials_v1; original discoveries remain separate. Existing favorites retain their key and identifiers.
- Real Web Audio graph checks confirmed initial silence, zero output after goal → mute, whistle → pause and the hidden-state handler, and no queued effects resuming. This is not an independent listening review.
- Eight main/new pages fit both 390 and 320 pixels. Roster filters, comparisons, search/no-results, all 28 kit selections, detail modes, keyboard navigation and favorite restoration passed. No-JavaScript profile/source reading remains available.
- Compatibility URLs next/kits.html and next/arcade/longgame.html redirect to the current edition and retain fragments. Original BelaMini26 remains at its URL.
- Post-kickoff checks on home/current-team/Canada pages show an unverified-result state, never an inferred score or “live” claim. Old snapshots receive an archive notice.
- Local link/anchor/duplicate-ID audit: 48 HTML files, zero errors. Browser tests reported no JavaScript errors.

## Evidence boundaries
The roster is the October 5 current 28, including Downs replacing Pepi. Camp inclusion is not fitness clearance or a projected XI. The 2030 watchlist contains 13 emerging/new senior options and six youth-pathway names; it is not ranked. Canada’s camp page is reconciled with later withdrawals and additions; no exhaustive final bench is claimed. Club/stat dates and individual sources are attached to profiles. Neil Pierre’s age is used without the disputed exact birth date or height.

Kit identity and drawing references are distinguished. These are original historical-design studies with simplified marks and patterns, not licensed replicas. The 2025 USWNT-only Brilliant design is excluded.

The Long Game uses historical-style rendering grammars, not hardware emulation or equivalence to commercial-era engines. The polygon challenge is explicitly early-3D-inspired 2.5D; HD is an articulated vector interpretation; anime is a stylistic branch. The 1974 story date is not Pong’s release date. BelaMini27 scenarios, opponents and outcomes are fictional.

## Remaining limits
No physical-phone, Safari/Firefox, controller, screen-reader gameplay or extended human balance study. Native controls and readable status help access but do not make the canvas games fully nonvisual. Audio has not been independently heard. No comprehensive film grading, player health clearance, measured potential scores or lineup probabilities were obtained. Current fixtures remain a dated snapshot.

## Maintenance
The notebook source data is in squad-data.json. build-scout.py emits squad.html using the shared header/footer from now.html. build-canada.py contains the sourced Canada dossier and emits canada-data.json/canada.html. Run from any directory with Python 3. Recheck official sources and dates when updating; no build step is needed to serve the completed static site.
