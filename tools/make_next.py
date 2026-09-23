"""Copy the live site's pages into next/ so a preview edition can be edited
without touching the live pages. Assets and fonts stay where they are; the
copies point one level up to reach them. Run once to seed next/, never over
edited next/ pages (it refuses to overwrite)."""
import pathlib, re, shutil, sys
root = pathlib.Path(__file__).resolve().parent.parent
nxt = root / "next"; (nxt / "arcade").mkdir(parents=True, exist_ok=True)
files = [p for p in root.glob("*.html")] + [p for p in root.glob("*.css")] + [p for p in root.glob("*.js")]
files += list((root / "arcade").glob("*.html"))
def fix(text, depth):
    up = "../" * depth
    text = re.sub(r'''(["'(])(assets|fonts)/''', lambda m: m.group(1) + up + m.group(2) + "/", text)
    return text
for f in files:
    rel = f.relative_to(root); dest = nxt / rel
    if dest.exists() and "--force" not in sys.argv:
        print("skip (exists)", rel); continue
    depth = 1  # next/ is one level down; arcade pages already use ../assets
    t = f.read_text()
    if rel.parts[0] == "arcade":
        t = t.replace("../assets/", "../../assets/").replace("../fonts/", "../../fonts/")
    else:
        t = fix(t, depth)
    dest.write_text(t); print("seeded", rel)
