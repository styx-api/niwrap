"""Render the niwrap.dev Open Graph card (1200x630).

Reads the live package/tool counts from the hosted catalog so the card stays in
lockstep with each Pages deploy. Rendered at 2x and downscaled (LANCZOS) for
crisp anti-aliasing. Palette and type mirror the landing page.

Usage:
    python build_og.py --catalog-dir _site --logo logo.png --fonts-dir fonts \
        --out _site/og-image.png [--languages 2]
"""

import argparse
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageFilter

S = 2  # supersample factor
W, H = 1200 * S, 630 * S

# palette (from the landing page dark theme)
BG = (13, 17, 23)  # #0d1117
TEXT = (240, 246, 252)  # #f0f6fc
MUTED = (139, 148, 158)  # #8b949e
BLUE = (88, 166, 255)  # #58a6ff
GREEN = (63, 185, 80)  # #3fb950

TAGLINE = "Type-safe neuroimaging tools"
DESCRIPTION = (
    "Use FSL, ANTs, AFNI, FreeSurfer and more directly from Python and "
    "TypeScript - with autocompletion, type checking, and structured outputs."
)
URL = "niwrap.dev"


def counts_from_catalog(catalog_dir: Path) -> tuple[int, int]:
    """Return (tools, packages) from the hosted index.json -> catalog.json."""
    index = json.loads((catalog_dir / "index.json").read_text())
    entry = next(
        (v for v in index["versions"] if v["version"] == index["latest"]),
        index["versions"][0],
    )
    catalog = json.loads((catalog_dir / entry["catalog"]).read_text())
    packages = catalog["packages"]
    tools = sum(len(p.get("apps", [])) for p in packages)
    return tools, len(packages)


def render(tools: int, packages: int, languages: int, logo_path: Path, fonts_dir: Path, out: Path):
    inter = str(fonts_dir / "Inter.ttf")
    mono = str(fonts_dir / "JetBrainsMono.ttf")

    def font(path, size, weight):
        f = ImageFont.truetype(path, int(size * S))
        f.set_variation_by_name(weight)
        return f

    def px(v):
        return int(v * S)

    img = Image.new("RGB", (W, H), BG)

    # soft brand glow behind the logo
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    cx, cy, r = px(960), px(300), px(360)
    gd.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(35, 134, 54, 70))
    glow = glow.filter(ImageFilter.GaussianBlur(px(90)))
    img = Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB")
    draw = ImageDraw.Draw(img)

    # logo on the right, vertically centered
    logo = Image.open(logo_path).convert("RGBA")
    lh = px(360)
    lw = int(lh * logo.width / logo.height)
    logo = logo.resize((lw, lh), Image.LANCZOS)
    img.paste(logo, (px(1200 - 96) - lw, (H - lh) // 2), logo)

    x = px(96)
    draw.text((x, px(96)), "NiWrap", font=font(inter, 70, "Bold"), fill=TEXT)
    draw.text((x, px(196)), TAGLINE, font=font(inter, 38, "SemiBold"), fill=BLUE)

    def wrap(text, fnt, max_w):
        words, lines, cur = text.split(), [], ""
        for w in words:
            trial = (cur + " " + w).strip()
            if draw.textlength(trial, font=fnt) <= max_w:
                cur = trial
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        return lines

    desc_f = font(inter, 25, "Regular")
    y = px(272)
    for line in wrap(DESCRIPTION, desc_f, px(640)):
        draw.text((x, y), line, font=desc_f, fill=MUTED)
        y += px(37)

    stats = [(f"{tools:,}", "tools"), (str(packages), "packages"), (str(languages), "languages")]
    num_f = font(mono, 46, "Bold")
    lab_f = font(inter, 22, "Medium")
    sx, sy = x, px(452)
    for num, lab in stats:
        draw.text((sx, sy), num, font=num_f, fill=BLUE)
        nw = draw.textlength(num, font=num_f)
        draw.text((sx, sy + px(58)), lab, font=lab_f, fill=MUTED)
        lw2 = draw.textlength(lab, font=lab_f)
        sx += int(max(nw, lw2)) + px(56)

    draw.text((x, px(560)), URL, font=font(inter, 26, "SemiBold"), fill=GREEN)

    # bottom accent bar (green -> blue)
    bar_h = px(8)
    for i in range(W):
        t = i / W
        draw.line(
            [(i, H - bar_h), (i, H)],
            fill=(
                int(GREEN[0] + (BLUE[0] - GREEN[0]) * t),
                int(GREEN[1] + (BLUE[1] - GREEN[1]) * t),
                int(GREEN[2] + (BLUE[2] - GREEN[2]) * t),
            ),
        )

    out.parent.mkdir(parents=True, exist_ok=True)
    img.resize((1200, 630), Image.LANCZOS).save(out, optimize=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--catalog-dir", required=True, type=Path, help="dir with index.json + <ver>/catalog.json")
    ap.add_argument("--logo", required=True, type=Path)
    ap.add_argument("--fonts-dir", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--languages", type=int, default=2)
    args = ap.parse_args()

    tools, packages = counts_from_catalog(args.catalog_dir)
    render(tools, packages, args.languages, args.logo, args.fonts_dir, args.out)
    print(f"wrote {args.out} ({tools:,} tools, {packages} packages, {args.languages} languages)")


if __name__ == "__main__":
    main()
