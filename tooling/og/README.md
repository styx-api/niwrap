# Open Graph card

`build_og.py` renders the 1200x630 social-share card published at
`https://niwrap.dev/niwrap/og-image.png` and referenced by the landing page's
`og:image` / `twitter:image` meta tags.

The package and tool counts are read from the hosted catalog (`index.json` ->
`<version>/catalog.json`), so the card stays in lockstep with each Pages deploy
instead of drifting stale.

## CI

`publish-pages.yaml` renders the card into `_site/og-image.png` right before the
Pages artifact is uploaded. The build assets (the two OFL fonts and the
rasterized logo) are fetched on a cache miss and cached via `actions/cache`,
keyed on `logo.svg` - so a normal deploy does no network work for them.

## Run locally

```bash
# 1. assets (one-time): fonts + a rasterized logo
mkdir -p tooling/og/.assets && cd tooling/og/.assets
curl -sSfL -o Inter.ttf "https://github.com/google/fonts/raw/main/ofl/inter/Inter%5Bopsz,wght%5D.ttf"
curl -sSfL -o JetBrainsMono.ttf "https://github.com/google/fonts/raw/main/ofl/jetbrainsmono/JetBrainsMono%5Bwght%5D.ttf"
npx -y sharp-cli -i ../../../logo.svg --density 500 -o logo.png resize 720 900
cd -

# 2. a catalog to read counts from (a built _site, or fetch the live one)
mkdir -p _site/1.0.0
curl -sSfL -o _site/index.json https://niwrap.dev/niwrap/index.json
curl -sSfL -o _site/1.0.0/catalog.json https://niwrap.dev/niwrap/1.0.0/catalog.json

# 3. render
uv --directory tooling run --with pillow python og/build_og.py \
  --catalog-dir ../_site --logo og/.assets/logo.png --fonts-dir og/.assets \
  --out ../_site/og-image.png
```

Fonts ([Inter](https://github.com/rsms/inter),
[JetBrains Mono](https://github.com/JetBrains/JetBrainsMono)) are SIL OFL 1.1.
