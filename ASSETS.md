# CL★Q! assets

The browser runtime does not fetch `asset-manifest.json`. The manifest is embedded in `js/cliq.js`, so opening `index.html` directly with `file://` does not require a network request.

For GitHub Pages, run `tools/generate_asset_manifest.py` after adding assets, or use the included workflow to regenerate the embedded manifest.
