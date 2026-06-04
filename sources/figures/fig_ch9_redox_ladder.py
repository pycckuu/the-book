"""
Figure: The terminal electron acceptor hierarchy  (Chapter 9, Cities Without Sunlight)

A sediment column of six contiguous redox zones, depth increasing downward, each
labeled with its dominant metabolism. A relative energy bar on the right shrinks
with depth: iron/sulfate reducers conserve roughly 4-5x more energy per mole of
electron donor than methanogens (Bethke 2011, per the chapter), so the bars are
calibrated to that ratio rather than to invented absolute kJ values. The shared
zone colors (O2/NO3/Fe) are reused by the Chapter 10 aquifer figure.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

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
# energy = RELATIVE yield per mole donor; Fe/SO4 ~ 4-5x the CO2 bar.
zones = [
    {"acc": r"O$_2$",        "meta": "aerobic respiration", "h": 0.74,
     "fc": blue_bg,   "ec": blue,     "energy": 1.00},
    {"acc": r"NO$_3^-$",     "meta": "denitrification",     "h": 0.92,
     "fc": green_bg,  "ec": green,    "energy": 0.92},
    {"acc": r"Mn(IV)",       "meta": "Mn reduction",        "h": 0.92,
     "fc": violet_bg, "ec": violet,   "energy": 0.80},
    {"acc": r"Fe(III)",      "meta": "Fe reduction",        "h": 1.02,
     "fc": sand_bg,   "ec": sand,     "energy": 0.62},
    {"acc": r"SO$_4^{2-}$",  "meta": "sulfate reduction",   "h": 1.66,
     "fc": red_bg,    "ec": red,      "energy": 0.55},
    {"acc": r"CO$_2$",       "meta": "methanogenesis",      "h": 1.24,
     "fc": "#E8E8E8", "ec": mid_grey, "energy": 0.13},
]

fig, ax = plt.subplots(figsize=(11.6, 7.8), dpi=300)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")
ax.set_xlim(0, 12.4)
ax.set_ylim(-0.55, 8.2)
ax.axis("off")

fig.suptitle("The terminal electron acceptor hierarchy",
             fontsize=14, fontweight="bold", y=0.97, color=grey)

# ── layout ──────────────────────────────────────────────────────────────
band_L, band_R = 2.65, 7.35      # the sediment column
ebar_x0 = 8.55                   # energy-bar track left edge (shared baseline)
ebar_max = 2.85                  # full-track width = 100% yield
bar_h = 0.30
track_pad = 0.10                 # padding around bars inside the panel

y_top = 6.95
y_cur = y_top
centers = []
for z in zones:
    h = z["h"]
    y0 = y_cur - h
    cy = y_cur - h / 2
    centers.append(cy)

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

# ── right: relative energy-yield panel ─────────────────────────────────
# A single framed track-and-bar panel so the bars read as ONE comparison
# that shrinks with depth. Shared left baseline + full-width grey track.
panel_x0 = ebar_x0 - track_pad
panel_x1 = ebar_x0 + ebar_max + track_pad
panel_top = y_top
panel_bot = y_bot

# enclosing panel (subtle), framing all the energy bars together
ax.add_patch(FancyBboxPatch(
    (panel_x0, panel_bot - 0.04), (panel_x1 - panel_x0), (panel_top - panel_bot) + 0.08,
    boxstyle="round,pad=0.05,rounding_size=0.10",
    facecolor="#FBFBFB", edgecolor=light_grey, linewidth=1.1, zorder=1.5))

for cy, z in zip(centers, zones):
    # full-width track (the "100%" reference), shared baseline at ebar_x0
    ax.add_patch(FancyBboxPatch(
        (ebar_x0, cy - bar_h / 2), ebar_max, bar_h,
        boxstyle="round,pad=0,rounding_size=0.05",
        facecolor="white", edgecolor=light_grey, linewidth=1.0, zorder=3))
    # filled bar = relative yield
    ax.add_patch(FancyBboxPatch(
        (ebar_x0, cy - bar_h / 2), ebar_max * z["energy"], bar_h,
        boxstyle="round,pad=0,rounding_size=0.05",
        facecolor=z["ec"], edgecolor=z["ec"], linewidth=0.0, alpha=0.92,
        zorder=4))

# panel header (clear, two lines well clear of the track frame)
ax.text((panel_x0 + panel_x1) / 2, panel_top + 0.62,
        "relative energy yield", ha="center", va="bottom",
        fontsize=11.5, fontweight="bold", color=grey)
ax.text((panel_x0 + panel_x1) / 2, panel_top + 0.40,
        "per mole of electron donor", ha="center", va="bottom",
        fontsize=9.5, color=mid_grey, style="italic")

# "high" / "low" anchors at top and bottom of the panel so the trend is explicit
ax.text(panel_x1 + 0.12, panel_top - 0.18, "high", ha="left", va="top",
        fontsize=9, color=mid_grey, style="italic")
ax.text(panel_x1 + 0.12, panel_bot + 0.18, "low", ha="left", va="bottom",
        fontsize=9, color=mid_grey, style="italic")

# "decreases" arrow on the far right, with clear breathing room
dec_x = panel_x1 + 0.62
ax.add_patch(FancyArrowPatch((dec_x, panel_top - 0.10),
             (dec_x, panel_bot + 0.10),
             arrowstyle="-|>", mutation_scale=18, color=mid_grey,
             linewidth=2.0, zorder=3))
ax.text(dec_x + 0.34, (panel_top + panel_bot) / 2, "decreases",
        ha="center", va="center", rotation=90, fontsize=10.5,
        color=mid_grey, style="italic", fontweight="bold")

# Caption handled in markdown:
# "The redox ladder, expressed in sediment. Each zone represents the cheapest
#  electron acceptor still available."

out_dir = Path(__file__).resolve().parents[1] / "img"
out_dir.mkdir(parents=True, exist_ok=True)
base = out_dir / "ch9_redox_ladder"

plt.savefig(base.with_suffix(".png"), dpi=300, bbox_inches="tight", facecolor="white")
plt.savefig(base.with_suffix(".pdf"), bbox_inches="tight", facecolor="white")
plt.close(fig)

print(f"Saved {base.with_suffix('.png')} and {base.with_suffix('.pdf')}")
