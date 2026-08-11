#!/usr/bin/env python3
from pathlib import Path
import json, re

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"}
LABELS = {
    "random":"RANDOM ♡", "strawberry":"STRAWBERRY ♡", "cameras":"CAMERAS 📸",
    "music":"MUSIC 🎧", "redkawaii":"RED KAWAII 🎀", "cats":"CATS 🐱",
    "retro":"RETRO 📼", "japanese":"JAPANESE 🌸", "bakery":"BAKERY 🍰"
}

def clean(value):
    return re.sub(r"[^a-z0-9._-]+", "-", value.lower()).strip("-")

def labelize(value):
    value = value.replace("_", " ").replace("-", " ").strip()
    return " ".join(x.capitalize() for x in value.split()) or "Unnamed"

frames = []
for path in sorted((ASSETS / "frames").rglob("*")):
    if path.is_file() and path.suffix.lower() in IMAGE_EXTS and not path.name.startswith("._"):
        frames.append({
            "id": clean(path.stem),
            "label": labelize(path.stem),
            "src": path.relative_to(ROOT).as_posix(),
        })

seen = {}
for frame in frames:
    base = frame["id"]
    n = seen.get(base, 0) + 1
    seen[base] = n
    if n > 1:
        frame["id"] = f"{base}-{n}"

packs = []
sticker_root = ASSETS / "stickers"
for directory in sorted(p for p in sticker_root.iterdir() if p.is_dir() and not p.name.startswith(".")):
    files = [
        p.relative_to(directory).as_posix()
        for p in sorted(directory.rglob("*"))
        if p.is_file() and p.suffix.lower() in IMAGE_EXTS and not p.name.startswith("._")
    ]
    packs.append({
        "id": clean(directory.name),
        "label": LABELS.get(clean(directory.name), labelize(directory.name)),
        "directory": directory.relative_to(ROOT).as_posix(),
        "files": files,
    })

root_files = [
    p.name for p in sorted(sticker_root.iterdir())
    if p.is_file() and p.suffix.lower() in IMAGE_EXTS and not p.name.startswith("._")
]
if root_files:
    packs.insert(0, {"id":"misc","label":"MISC ✦","directory":"assets/stickers","files":root_files})

manifest = {
    "version": 2,
    "generatedBy": "tools/generate_asset_manifest.py",
    "frames": frames,
    "stickerPacks": packs,
}

manifest_json = json.dumps(manifest, ensure_ascii=False, separators=(",", ":"))
out = ASSETS / "asset-manifest.json"
out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# Keep the browser-safe inline copy in clq.js synchronized. This is what
# allows the app to work when index.html is opened directly via file://,
# where fetch() is blocked by browser security.
js_path = ROOT / "js" / "cliq.js"
js = js_path.read_text(encoding="utf-8")
pattern = re.compile(r"const __CLQ_INLINE_ASSET_MANIFEST = .*?;\n", re.S)
replacement = f"const __CLQ_INLINE_ASSET_MANIFEST = {manifest_json};\n"
js, count = pattern.subn(replacement, js, count=1)
if count != 1:
    raise SystemExit("Could not find inline manifest in js/cliq.js")
js_path.write_text(js, encoding="utf-8")

print(f"Generated {len(frames)} frames and {len(packs)} sticker packs -> {out}")
