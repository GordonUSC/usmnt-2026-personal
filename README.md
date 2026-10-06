# USA 26 with Gordon

A static personal soccer site. Open `index.html` through a local HTTP server:

```sh
python3 -m http.server 8766 --bind 127.0.0.1
```

No build step or npm dependencies are required by the site. All main fonts and existing images are local.

## Routes

- `index.html`: current front door, personal archive entrances and reading-route experiment.
- `now.html`: October6,2026 football snapshot, match status, viewing lens and November dates.
- `summer.html`: original home and memories, preserved as an archive.
- Existing narrative chapters retain their URLs. Historical roster and tactical notes remain dated.
- `kits.html`: interactive kit room and Gordon's original personal shirt photographs.
- `play.html`: arcade entrance. `arcade/belamini.html` and `arcade/longgame.html` are the games.
- `sources.html`: direct official sources, corrections and limits.
- `next/`: earlier September preview, explicitly archived; arcade and kit improvements are mirrored for old links.

## Updating football information

Verify against official match/venue/federation sources. Update the date and citations with the facts. Do not infer a result from a scheduled kickoff. Current fixture logic lives in `october.js`; its ISO kickoff is carried in HTML. Canada calendar UID is preserved from the earlier calendar. The match calendar is a public fixture, not a personal plan.

Private travel/ticket/message details must not be added from local memory. Existing personal authored context is preserved, not independently authenticated by public football sources.

## Interaction and storage

Navigation and core content work without JavaScript. Route selection is ephemeral. Games retain existing storage keys and add records without replacing previous achievements. Kit favorites and game progress stay in the browser; no analytics were added. Game audio is opt-in. Reduced motion is respected; game-specific pause/calm controls are available.

## Review

See `review/DECISIONS.md` and `review/CHANGELOG.md`. This revision was prepared locally for review; no deployment is implied by these files.
