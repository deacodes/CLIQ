from pathlib import Path
import re, json, sys

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT/'index.html').read_text(encoding='utf-8')
JS = (ROOT/'js'/'cliq.js').read_text(encoding='utf-8')
CSS = (ROOT/'css'/'cliq.css').read_text(encoding='utf-8')

errors=[]

def require(cond,msg):
    if not cond: errors.append(msg)

require('<script src="js/cliq.js" defer></script>' in HTML, 'missing cliq.js script')
require('id="faceFilterGrid"' in HTML, 'missing separate face-filter grid')
require('id="homePaintCanvas"' in HTML, 'missing homepage paint canvas')
require('home-photo-pile' in HTML, 'missing homepage floating photo pile')
require('function setFaceFilter' in JS, 'missing setFaceFilter')
require('const FACE_FILTER_META' in JS, 'missing FACE_FILTER_META')
require('function bindHomePaint' in JS, 'missing bindHomePaint')
require('function downloadCanvas' in JS, 'missing downloadCanvas')
require('CL★Q! PRODUCTION REFINEMENT LAYER' in CSS, 'missing production CSS layer')
require("if (!pointerDragged) playAssetSound('clickEndAudio')" not in JS, 'legacy drag-release click sound still present')
require("state.filter === 'dog'" not in JS and "state.filter==='dog'" not in JS, 'dog still attached to normal filter state')
require("state.filter === 'hearts'" not in JS and "state.filter==='hearts'" not in JS, 'hearts still attached to normal filter state')

# Inline manifest integrity.
m = re.search(r'const __CLQ_INLINE_ASSET_MANIFEST = (\{.*?\});\n\n// Core DOM helper', JS)
if not m:
    errors.append('inline asset manifest not found')
else:
    try:
        manifest=json.loads(m.group(1))
        for fr in manifest.get('frames',[]):
            require((ROOT/fr['src']).exists(), f"missing frame asset: {fr['src']}")
        for pack in manifest.get('stickerPacks',[]):
            for fn in pack.get('files',[]):
                p=ROOT/pack['directory']/fn
                require(p.exists(), f"missing sticker asset: {p.relative_to(ROOT)}")
        print(f"manifest: {len(manifest.get('frames',[]))} frames, {len(manifest.get('stickerPacks',[]))} sticker packs")
    except Exception as exc:
        errors.append(f'manifest parse failed: {exc}')

# Duplicate HTML IDs.
ids=re.findall(r'\bid="([^"]+)"',HTML)
seen=set(); dups=[]
for i in ids:
    if i in seen: dups.append(i)
    seen.add(i)
require(not dups, f'duplicate HTML ids: {dups}')

if errors:
    print('SMOKE TEST: FAIL')
    for e in errors: print(' -',e)
    sys.exit(1)
print('SMOKE TEST: PASS')
