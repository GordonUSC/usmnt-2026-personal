# The Long Game — eight-era challenge implementation

Owned repository changes only:
- `arcade/longgame.html`
- `arcade/longgame-trials.js` (new, about21KB, no dependency/network)

## Contract

Free exploration remains the default. Its original story, photographs, deep links, 28 toys, `longgame_couva`, and `longgame_journey_v2` remain. An optional campaign adds8 independently playable stages, Club/Pro difficulty, explicit start screens, per-stage objectives,3 chances, timers, score, failure, retry, stage completion, full-run completion, per-era bests, and full-run best. `longgame_trials_v1` owns all new records and the resumable campaign checkpoint. Retry keeps earlier cleared stages. Practice does not replace the campaign checkpoint. No personal memory is gated by winning.

Stages: paddle returns; three-lane gap selection with an early-dash bonus; timed jumping with sprint bonus; reading changing defensive routes; combined aim/hold/release power; safe75-point recycling vs150-point line-breaking passes; direction+timing combinations; steady viewfinder photography.

All challenges are explicitly fictional training games, with historical-style visuals, not real matches or hardware emulation. The1974 story begins in a Pong-inspired paddle era, not a claim that Pong launched in1974. Anime2020 is explicitly a stylistic branch.

## Renderer proof

Production buffers and aspect ratios:
1.160×120 monochrome bars/squareball, 4:3
2.160×120 limited palette, wide block8px two-pose actor, coarse field, 4:3
3.256×192 tile/parallax world and12×18 pixel sprite poses, 4:3
4.320×240 behind-goal pitch, route windows, sprite scaling/shadows, 4:3
5.480×360 early-3D-inspired2.5D: perspective projection, goal depth, faceted player limbs, 4:3
6.960×540 smooth articulated athletes, directional shadows, passing lanes, 16:9
7.640×360 long-limb outlined cel figure, hair mass,2-tone torso, timing rings and strike pose, 16:9
8.960×540 existing real photograph, viewfinder framing, contact sheet, 16:9

The first5 are letterboxed within the page's wide canvas. Changes are actual drawing primitives, resolution, pose and composition, without CSS filters. Buffer dimensions are labeled as production choices.

## Controls/accessibility

Arrows/WASD plus Space; stage-specific native touch pads and action button. Action taps are buffered for one simulation frame, while the polygon shot uses held/released input. Enter starts/advances stages; R retries; Escape pauses. Focus-aware keyboard handlers preserve native controls. Readable HTML instructions and selected/open-route, receiver-risk and anime-direction cues supplement canvas graphics. Calm motion suppresses discretionary anime lines; there are no flashing impacts in the challenge renderer. Sound remains opt-in using the existing master-gain/voice cleanup. Pause/blur cancels charged input and uses the existing audio shutdown path.

## Checks completed (no browser launched)

`node /tmp/longgame-trials-check.cjs` -> `/tmp/longgame-trials-results.json`:
- All8 stages won on both Club and Pro through input-driven deterministic simulation:16 stage runs.
- Every stage reaches a loss under idle input.
- Fresh retry restores3 chances and0 hits.
- Held action cannot repeatedly score.
- Pause/release cancels charge without a ghost shot.
- All8 native renderers smoke-tested with a mock2D context in ready, playing and won states.
- Bad shot costs exactly1 life and0 points.
- Safe/risky HD pass awards75/150.
- All8 aspect ratios verified.
- Embedded HTML JS syntax compiled; referenced DOM IDs exist and are unique.

These are logic checks, not visual browser playtesting. Parent owns the sole browser and must verify actual rendering, touch controls, focus behavior, audio lifecycle and storage/checkpoint UI. Suggested visual check: final stage's common center-clear overlay may compete with the face; if observed, move that final clear banner to the top edge.

## QA shortcuts

Use the Practice selector to test each stage without replaying the campaign. Stage3 (16-bit): Start, Left then Space promptly reaches the initial openA. Stage4 (polygon): holdLeft~610ms, holdSpace~800ms, release; first target is left. Stage5 (HD): immediate Space from the center safely recycles for75. Stage6 (anime): matchLeft, then strike around1.09s after the round begins. Stage7: align the viewfinder to the gold mark, release directions, settle, thenSpace.

Verify pause on background, return from blur, quick touch taps, release outside pad/action, phase retry, full campaign next-stage, record resume after reload, and return to free exploration without losing original discoveries.

## Design review

Experience goal: read a new sports-game grammar in each era and execute a short meaningful action. MDA: movement, selection, charge, timing and framing produce distinct tactical decisions and earned progression. Achiever: scores/Pro mode/bests; Explorer: practice all8 and compare primitives; Socializer: local pass-the-device score attempts; competitive hook is personal best only, with no invented network players. Weakest unverified element is real-player tuning, especially tiny-screen scene legibility; parent browser review remains required.

No publish, commits, next-mirror edits or shared-navigation edits performed.
