# Long Game art edition 02 — review branch

The live site had two distinct render pipelines. The walk loaded the existing stadium/anime plates; the run's renderer received only the final photograph and drew independent simpler scenes. Live requests loaded the current module, with no service worker. This is an integration/design gap, not evidence of stale cached JavaScript.

The campaign now loads `longgame-visuals.js` and passes its actual art assets. Both modes use the shared character renderer and the same raster profiles. The arcade's run link opens the run (or an existing checkpoint), not the free walk. Plain old URLs and chapter links still open the walk. Existing journey/discovery, Couva and campaign storage keys are preserved.

## Eight visual treatments

- Paddle / 1974 memory: monochrome rectilinear court, block scoring and no modern type inside the playfield. Pong itself dates to 1972; 1974 is Gordon's personal story marker.
- VCS / 1982: 160×192 authored raster shown at 4:3, wide pixels, solid line colors, eight-pixel figures, two-frame stepping. Deliberately simplified, not a cycle-accurate TIA emulator.
- 8-bit / 1988: 256×240 authored raster, tile-built ground/crowd and three-color sprite clusters with stepped run/jump poses.
- 16-bit / 1994: 320×224 authored raster, shaded pixel clusters, layered crowd, elevated soccer pitch and passing choices in the scene.
- Early polygons / 1997: 320×240 raster, actual projected 3D geometry and depth-sorted flat faces; hard edges and snapped screen vertices. No claim of a particular console emulator or commercial game's assets.
- HD / 2010: the existing commissioned stadium plate with articulated, shaded players and broadcast-style selection feedback.
- Anime / 2020: the existing commissioned painted environment with shared inked character poses and stepped animation. This is a stylistic branch, not a hardware generation.
- Real / 2026: Gordon's existing dated photograph is fitted whole, with the game viewfinder mapped into the photo rather than cropping the portrait into a landscape frame.

Raster sizes are choices for these homages, not complete hardware specifications. Buffers through early polygons are presented at 4:3; later scenes at 16:9. Original code-drawn sprites and geometry are used; no ripped commercial game assets.

Historical context: [Computer History Museum's graphics/games timeline](https://www.computerhistory.org/timeline/graphics-games/) and [Pong collection](https://www.computerhistory.org/revolution/story/183). These distinguish 1972's Pong and 1977's Atari VCS release from the dates of Gordon's memories.

The existing AI environment plates are identified in `assets/art/MANIFEST.md`; they are game art, never factual match or player photography.
