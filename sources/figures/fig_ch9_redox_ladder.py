"""
Figure: The terminal electron acceptor hierarchy  (Chapter 9, Cities Without Sunlight)

A qualitative sediment column of six contiguous acceptor zones, depth increasing
downward, each labeled with its dominant metabolism. Zone thicknesses are not
measurements. No energy values or quantitative energy comparison are shown.
The shared zone colors (O2/NO3/Fe) are reused by the Chapter 10 aquifer figure.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch

# ── palette (shared with the other figures) ───────────────────────────
blue = "#2E6B8A"
blue_bg = "#D4E8F0"
red = "#B5452A"
red_bg = "#F2DDD5"
green = "#4A7C59"
green_bg = "#D8E8D8"
sand = "#C08A52"
sand_bg = "#F2E4D3"
violet = "#6D6AA8"
violet_bg = "#E5E6F4"
grey = "#333333"
mid_grey = "#8E8E8E"
light_grey = "#D9D9D9"

# ── zones, top -> bottom (the six acceptors of the governing equation) ──
# height = qualitative zone thickness (O2 thin, sulfate broad); not to scale.
zones = [
    {"acc": r"O$_2$",        "meta": "aerobic respiration", "h": 0.74,
     "fc": blue_bg,   "ec": blue},
    {"acc": r"NO$_3^-$",     "meta": "denitrification",     "h": 0.92,
     "fc": green_bg,  "ec": green},
    {"acc": r"Mn(IV)",       "meta": "Mn reduction",        "h": 0.92,
     "fc": violet_bg, "ec": violet},
    {"acc": r"Fe(III)",      "meta": "Fe reduction",        "h": 1.02,
     "fc": sand_bg,   "ec": sand},
    {"acc": r"SO$_4^{2-}$",  "meta": "sulfate reduction",   "h": 1.66,
     "fc": red_bg,    "ec": red},
    {"acc": r"CO$_2$",       "meta": "methanogenesis",      "h": 1.24,
     "fc": "#E8E8E8", "ec": mid_grey},
]

fig, ax = plt.subplots(figsize=(8.2, 7.8), dpi=300)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")
ax.set_xlim(0, 8.2)
ax.set_ylim(-0.55, 8.2)
ax.axis("off")

fig.suptitle("The terminal electron acceptor hierarchy",
             fontsize=14, fontweight="bold", y=0.97, color=grey)

# ── layout ──────────────────────────────────────────────────────────────
band_L, band_R = 2.65, 7.35      # the sediment column

y_top = 6.95
y_cur = y_top
for z in zones:
    h = z["h"]
    y0 = y_cur - h
    cy = y_cur - h / 2

    # contiguous band with SQUARE joins so the stack reads as one continuous
    # sediment column (not stacked rounded cards)
    ax.add_patch(mpatches.Rectangle(
        (band_L, y0), band_R - band_L, h,
        facecolor=z["fc"], edgecolor=z["ec"], linewidth=1.8, zorder=2))
    # subtle bottom strip, as in ch4
    ax.add_patch(mpatches.Rectangle(
        (band_L + 0.06, y0), (band_R - band_L) - 0.12, h * 0.15,
        facecolor=z["ec"], alpha=0.06, edgecolor="none", zorder=2.1))

    # acceptor (left, bold mathtext) + metabolism (center)
    ax.text(band_L + 0.32, cy, z["acc"], ha="left", va="center",
            fontsize=14.5, fontweight="bold", color=z["ec"], zorder=4)
    ax.text((band_L + band_R) / 2 + 0.62, cy, z["meta"], ha="center",
            va="center", fontsize=11, color=grey, zorder=4)

    y_cur = y0

y_bot = y_cur

# ── left: depth increases downward ─────────────────────────────────────
depth_x = 1.55
ax.add_patch(FancyArrowPatch((depth_x, y_top - 0.04), (depth_x, y_bot + 0.04),
             arrowstyle="-|>", mutation_scale=20, color=mid_grey,
             linewidth=2.4, zorder=3))
ax.text(depth_x - 0.42, (y_top + y_bot) / 2, "depth", ha="center", va="center",
        rotation=90, fontsize=12, color=mid_grey, style="italic",
        fontweight="bold")

# Caption handled in markdown by the course editor:
# Idealized acceptor zonation; real zones can overlap. Thickness is not to scale.
# No quantitative energy yield or conserved-ATP comparison is represented.

out_dir = Path(__file__).resolve().parents[1] / "img"
out_dir.mkdir(parents=True, exist_ok=True)
base = out_dir / "ch9_redox_ladder"

plt.savefig(base.with_suffix(".png"), dpi=300, bbox_inches="tight", facecolor="white")
plt.savefig(base.with_suffix(".pdf"), bbox_inches="tight", facecolor="white")
plt.close(fig)

print(f"Saved {base.with_suffix('.png')} and {base.with_suffix('.pdf')}")
