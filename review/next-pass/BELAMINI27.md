# BelaMini27 — implementation and game contract

## Scope
Only deliverable source: `arcade/belamini27.html`. No new external assets, libraries, font downloads or requests. Reuses the existing local Press Start font. Original `arcade/belamini.html` is untouched. Parent handles links, single-browser review and publication. No commits or browser launches by this worker.

## Design
Floodlit training ground built on the original top-down engine. More readable code-drawn players/kit shading and facing, bigger controlled marker, stamina bar, first-touch ring, striped turf, net shadows, corner flags, ball trails and tactical passing/run paths. A tactical briefing sits beside the pitch on desktop and below it on phones. Original 26 remains separately linked.

Every page introduction and the scoreboard identify a fictional2027 simulation. Five invented tactical opponents/scenarios have no real player ratings, fixtures, venues or results. This is an arcade experiment, not a calibrated model.

## Tactical contract
- Move: arrows/WASD. Sprint: hold Shift. Sprint is1.5x speed and consumes the controlled player's stamina, recovers when released. A sprint carries the ball farther and produces a less accurate shot.
- Z/Space: pass toward facing direction, or switch defender. Completed passes count only on receipt by another teammate. White dotted preview is the selected passing lane.
- E on the ball: call a teammate run, shown by teal dots and destination marker. C plays ahead along that runner's trajectory. The passer remains controlled during flight so AI can finish the run; control transfers on receipt. C without a called runner calls one first.
- E held without the ball: second-player press. User controls cover; the pressing teammate spends stamina. Winning a tackle in that role increments pressWins.
- X hold/release: charge/shot; left/right aims. Teal power zone35–80%. Amber first-touch ring fades after14 simulation frames. A settled, non-sprinting shot from within105 pitch units in the power zone earns setShot. Shot feedback distinguishes rushed, long, pressured, placed and power shots.
- Q: balanced/wide/compact shape changes actual home/support positions. V: tactical guides on/off. P: pause. Escape: circuit. Native equivalents exist for all controls, plus touch joystick.
- Existing simplified football rules retained: no offside/fouls/substitutions. Dribbling over touchlines now triggers the same restarts as a loose ball. Clock measures active-play seconds; restarts add wall time.
- Same seed per scenario controls gameplay randomness; identical inputs produce identical states. Cosmetic particles/audio noise are separate. This makes repeated starts comparable, not a promise of identical outcomes with different input timing.

## Circuit
All challenges open; three independent objectives in each, best total of0–3 stars preserved per scenario. Duration is active-play seconds.
1. Third player70s: three completed passes; a completed through ball; score.
2. Beat the press75s: four completed passes; receive a through ball beyond halfway; create a settled shot.
3. Transition65s: completed through ball; settled shot; score.
4. Protect the lead60s: ten players and a fictional1–0 lead; successful press/tackle, avoid losing, clean sheet.
5. Unlock the game90s: fictional0–1 deficit; five passes, draw level or better, win.
The45s drill uses easier opponents and never writes records. Stars earn rank labels; everyone can replay any test. Scores:100/objective,20/completed pass,60 additional/through,40/set shot,250/new goal,40/press or tackle. Best score and best stars are tracked independently.

## Storage/audio
New key `belamini27_v1`, schema version1; results/chapterBest/stars/attempts arrays and best sum. Validates loaded data. Old key `belamini_run_v2` is only read to display a legacy best/completion summary; never written. No fake import of old score into new challenges. Storage failures stay playable and show session-only feedback.
Latest masterGain + tracked voice cancellation from the parent's published26 fix is retained. Sound off initially. Mute/pause/hidden page cancel queued voices and ramp the master down. Resume does not replay cancelled sounds.

## Completed checks
`logic-test.mjs` runs the actual game script in a Node VM with a stubbed DOM/canvas. These are simulation/logic checks, not real browser playthroughs:
- Sprint drain, called runner, completed through pass, settled shot after receipt, shape cycle, second-player press stamina.
- Same-seed same-input replay equality.
- Complete drill, all five challenge completions, finite player coordinates and bounded stamina.
- Legacy record byte-identical after drill and five saves; new progress uses new namespace.
- Initial, drill-result and challenge-result render functions execute without runtime exceptions in the stub.
- JavaScript syntax and git diff whitespace checks pass. Original game has no diff.
Receipt: `logic-receipt.json`; exact full simulation scores are not evidence of human balance quality.

## Parent browser review
Prepared but NOT RUN: `node evidence/belamini27/browser-qa.mjs <server-origin> <evidence-directory>`.
Manual first-payoff sequence:45-second drill, wait1.5s for kickoff, tap E then C, wait0.75s for receipt, hold X about0.4s and release. Expect completed/through1 and a placed/settled shot. Verify guides, shape, pause, mute, desktop and390/320 screenshots. Keyboard control requires canvas focus (starting a scenario focuses it automatically). Mobile controls use pointer capture and support simultaneous joystick/button input.

## Remaining limits
Parent must inspect actual rendered graphics and real-input browser behavior. No worker browser launch was authorized in this pass. Physical device ergonomics, complete human playthrough of every challenge, and longer balance/retention studies remain untested. Canvas gameplay is visual; native instructions/status/navigation support assistive technology but are not a nonvisual playing mode.

Additional targeted checks completed after the main receipt:
- `storage-test.mjs`: both storage reads and writes throw; challenge still ends and UI explicitly reports “Storage unavailable: session only.”
- `audio-test.mjs`: stub AudioContext verifies master open, scheduled voices created, mute cancels/clears them, unmute does not revive them, pause closes/cancels. This supplements but does not replace the parent's real-browser audio check.
