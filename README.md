# CL★Q! — Split GitHub Pages Build

This version separates the original monolithic HTML into:

- `index.html` — structure/markup
- `css/cliq.css` — all extracted CSS
- `js/cliq.js` — all extracted JavaScript
- `assets/` — place external image/audio/font assets here
  - `assets/frames/` contains frame PNGs
  - `assets/stickers/` contains the sticker category folders
  - `assets/asset-manifest.json` is the only catalog the UI needs

## GitHub Pages

Keep `index.html` at the repository root.

Enable:

- Settings → Pages
- Deploy from a branch
- Branch: `main`
- Folder: `/ (root)`

## Important

The original application is preserved as closely as possible. Inline CSS and JavaScript were extracted rather than rewritten, so functionality should remain equivalent.

If the original HTML references embedded `data:` assets, those remain embedded. External files should use relative paths such as:

```text
assets/frames/example.png
assets/stickers/aqua/example.webp
assets/sounds/click.mp3
```

To add a frame or sticker, put it in the appropriate folder and add it to
`assets/asset-manifest.json`. The editor loads the catalog at startup, so no
JavaScript changes are needed when the asset library changes.


## Local file:// support
The sticker manifest is embedded into `js/cliq.js`, so opening `index.html` directly from Finder/Downloads does not require `fetch()` and works without CORS restrictions. GitHub Pages still uses the same relative `assets/stickers/...` URLs.
