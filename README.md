# CL★Q!

> A tiny creative desktop for making things that feel like you. ♡

CL★Q! is a browser-based photo/video editor built around a playful, `.exe`-style desktop metaphor. Instead of a conventional editor UI, tools (camera, filters, stickers, frames, captions, export) live in draggable windows on a fake desktop.

**Repo:** https://github.com/deacodes/CL-Q_PHOTOBOOTH

---

## Table of Contents

- [Quick Start](#quick-start)
- [Features](#features)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Architecture](#architecture)
- [Asset Management](#asset-management)
- [Performance Notes](#performance-notes)
- [Deployment (GitHub Pages)](#deployment-github-pages)
- [Contributing](#contributing)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Quick Start

```bash
git clone https://github.com/deacodes/CL-Q.git
cd CL-Q
python3 -m http.server 8000
# or: npx serve .
```

Open **http://localhost:8000**.

**Requirements:** a modern browser (Chrome, Safari, Edge, or Firefox), Git, and Python 3 or Node.js to serve the app locally.

> ⚠️ **Do not open `index.html` directly via `file://`.** The app fetches assets at runtime, and browsers block `fetch()` on `file://` URLs. You'll see errors like `Fetch API cannot load file://...`. Always serve over HTTP — see [Troubleshooting](#troubleshooting) for details.

---

## Features

- Photo & video capture with live preview
- Image/video filters (applied consistently in preview *and* export)
- Custom frames
- Multiple sticker packs (themed folders + emoji-style assets), with tag/category filtering and an independently scrollable grid
- Multiline captions with configurable color
- Draggable `.exe`-style windows with a unified movement system
- Decorative custom cursor (non-blocking — doesn't intercept pointer events)
- Animated/parallax backgrounds
- Audio feedback for interactions
- Final export to image/video

---

## Project Structure

```
CL-Q/
├── index.html
├── css/
│   └── style.css
├── js/
│   └── clq.js
├── assets/
│   ├── frames/
│   │   ├── frame-01.png
│   │   └── ...
│   ├── stickers/
│   │   ├── cats/
│   │   ├── cute/
│   │   ├── emojis/
│   │   └── ...
│   └── backgrounds/
└── README.md
```

Application code (HTML/CSS/JS) and creative assets are kept strictly separate — this is intentional and should be preserved by any contribution.

---

## How It Works

**Editing flow:**

```
Capture / Select Media → Preview → Filters → Customize
  (stickers, frames, captions) → Final Preview → Export
```

**Rendering pipeline** (what actually produces the exported file):

```
Original Media → Filter → Frame/Layout → Stickers → Caption → Final Canvas → Preview/Export
```

Preview and export share the same state and rendering rules, so what you see while editing is what you get in the downloaded file. This matters most for filters: applying a CSS filter to an HTML element doesn't carry into a recorded video, so filters are baked in during canvas frame rendering, not just applied visually.

**Window movement model:**

1. Pointer down on a window's title bar → record current position.
2. Pointer moves → measure delta from the original position.
3. Window follows the pointer, constrained to the workspace bounds.
4. Pointer up → movement ends.

All draggable windows share this one implementation — there is no per-step drag logic.

---

## Architecture

```
Interface (HTML/CSS) ─┐
State (editing state) ─┼─→ JavaScript → Rendering → Preview / Export
Assets (frames, stickers, backgrounds) ─┘
```

Core principle: **one implementation per system.** Window movement, asset loading, preview rendering, filters, caption rendering, and export all have a single source of truth used everywhere they're needed. Before adding a new editing step, check whether it can reuse an existing system rather than forking a new one.

---

## Asset Management

Assets are organized by type, and each type is independently expandable:

```
assets/
├── frames/
│   └── frame-01.png
└── stickers/
    ├── cats/
    ├── cinnamoroll/
    ├── cute/
    ├── emojis/
    └── new-pack/
```

Adding a new sticker pack or frame means dropping files into the right directory — no changes to application logic required, assuming the asset-manifest/discovery system is enabled.

---

## Performance Notes

- Sticker/frame collections can get large; avoid eagerly loading every asset on startup. Lazy-load packs on demand.
- Compress large transparent PNGs (or convert to a modern format like WebP) without losing transparency/quality.
- Keep UI updates scoped — e.g., selecting a sticker should update state + preview, not re-render the whole sticker library.

---

## Deployment (GitHub Pages)

CL★Q! is a static site and deploys as-is. Requirements:

- Repo includes `index.html`, `css/`, `js/`, `assets/`
- **All asset paths are relative**, e.g. `fetch("./assets/asset-manifest.json")` — never an absolute local path like `/Users/you/Downloads/CL-Q/assets/`, which only works on your machine.

---

## Contributing

1. Check whether the functionality already exists (window movement, asset loading, preview rendering, filters, caption rendering, export, app state) before writing a new implementation — extend, don't duplicate.
2. Keep HTML/CSS/JS responsibilities separated.
3. Keep asset paths relative; keep frames/stickers in their correct directories.
4. Don't let decorative layers (e.g. the custom cursor) block pointer events.
5. Test at multiple window sizes.
6. Test both preview and export paths for any rendering change.
7. Run through the full workflow (capture → filter → customize → caption → export) after any non-trivial change.

Bug reports / feature requests: open a GitHub Issue with browser + OS, repro steps, expected vs. actual behavior, console errors, and a screenshot/recording if relevant.

---

## Troubleshooting

**`Fetch API cannot load file://...` or `Unsafe attempt to load URL file://...`**
You opened `index.html` directly from disk. Browsers block `fetch()` on `file://` origins. Fix: serve the project over HTTP —

```bash
python3 -m http.server 8000
# or
npx serve .
```

then visit the printed `localhost` URL.

---

## License

Not yet specified. 

---

**CL★Q! — a tiny creative desktop for making things that feel like you. ♡**
