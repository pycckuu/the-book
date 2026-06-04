"""
Figure: The spectrum of integration
Chapter 7, The Merger

Four symbioses placed along an Independence -> Organelle axis, with a schematic
genome bar that shrinks as integration tightens. Numeric genome sizes are shown
only where the manuscript provides them (Carsonella 160 kb, mitochondrion ~16 kb);
the bars are schematic, not to scale. Palette matched to the other figures.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle

# ── palette (shared with the other figures) ───────────────────────────
blue = "#2E6B8A"
blue_bg = "#D4E8F0"
red = "#B5452A"
red_bg = "#F2DDD5"
green = "#4A7C59"
green_bg = "#D8E8D8"
sand = "#C08A52"
sand_bg = "#F2E4D3"
grey = "#333333"
mid_grey = "#8E8E8E"
light_grey = "#D9D9D9"

fig, ax = plt.subplots(figsize=(11.6, 5.6), dpi=300)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")
ax.set_xlim(0, 12.8)
ax.set_ylim(1.4, 6.6)
ax.axis("off")

fig.suptitle(
    "The spectrum of integration",
    fontsize=14,
    fontweight="bold",
    y=0.97,
    color=grey,
)

# ── four stations ───────────────────────────────────────────────────────
# Genome bars are SCHEMATIC (not to scale); numeric size is given only for
# Carsonella and the mitochondrion, where the manuscript provides one.
stations = [
    {
        "x": 2.55, "fc": green_bg, "ec": green,
        "name": "Ruthia magnifica",
        "desc": "retains free-living metabolism;\nmetabolically autonomous",
        "gw": 1.70, "glabel": "large genome",
    },
    {
        "x": 5.35, "fc": blue_bg, "ec": blue,
        "name": "Elysia chlorotica",
        "desc": "steals chloroplasts;\nnon-heritable",
        "gw": 1.18, "glabel": "borrowed parts",
    },
    {
        "x": 8.15, "fc": sand_bg, "ec": sand,
        "name": "Carsonella ruddii",
        "desc": "cannot replicate alone",
        "gw": 0.66, "glabel": "160 kb",
    },
    {
        "x": 10.95, "fc": red_bg, "ec": red,
        "name": "Mitochondrion",
        "desc": "fully integrated organelle",
        "gw": 0.30, "glabel": "~16 kb",
    },
]

BOX_W, BOX_H = 2.46, 2.02
box_cy = 5.05
box_bottom = box_cy - BOX_H / 2

# genome-track geometry inside each card
track_y = box_cy - 0.52          # vertical centre of the schematic bar
track_h = 0.20
track_inset = 0.34               # margin of the track from the card edges
track_w = BOX_W - 2 * track_inset

# ── the axis: independence -> organelle ────────────────────────────────
axis_y = 2.55
ax.add_patch(FancyArrowPatch(
    (1.0, axis_y), (12.05, axis_y),
    arrowstyle="-|>", mutation_scale=24, color=mid_grey,
    linewidth=2.8, zorder=2))

ax.text(1.0, axis_y - 0.50, "Independence", ha="left", va="top",
        fontsize=11.5, fontweight="bold", color=green)
ax.text(12.05, axis_y - 0.50, "Organelle", ha="right", va="top",
        fontsize=11.5, fontweight="bold", color=red)
ax.text(6.75, axis_y - 0.50, "increasing integration", ha="center", va="top",
        fontsize=9.5, color=mid_grey, style="italic")

# ── stations: leaders, axis dots, cards, genome bars ──────────────────────
for s in stations:
    sx, ec = s["x"], s["ec"]

    # leader: a clean solid stub straight down from the card to the axis dot
    ax.plot([sx, sx], [box_bottom - 0.02, axis_y],
            color=ec, linewidth=1.6, linestyle=(0, (1, 1.6)),
            alpha=0.9, zorder=2, solid_capstyle="round")

    # axis marker (drawn last per-station so the leader tucks underneath)
    ax.plot(sx, axis_y, "o", markersize=11, color=ec,
            markeredgecolor="white", markeredgewidth=1.8, zorder=5)

    # station card
    ax.add_patch(FancyBboxPatch(
        (sx - BOX_W / 2, box_cy - BOX_H / 2), BOX_W, BOX_H,
        boxstyle="round,pad=0.02,rounding_size=0.10",
        facecolor=s["fc"], edgecolor=ec, linewidth=1.8, zorder=3))

    # species name (italic) and description
    ax.text(sx, box_cy + 0.66, s["name"], ha="center", va="center",
            fontsize=10.5, fontweight="bold", fontstyle="italic",
            color=ec, zorder=6)
    ax.text(sx, box_cy + 0.16, s["desc"], ha="center", va="center",
            fontsize=8.2, color=grey, linespacing=1.25, zorder=6)

    # ── schematic genome bar (shrinking left -> right; NOT to scale) ──
    track_x = sx - track_w / 2
    # white track gives every bar a clean, equal-length frame to read against
    ax.add_patch(FancyBboxPatch(
        (track_x, track_y - track_h / 2), track_w, track_h,
        boxstyle="round,pad=0.0,rounding_size=0.04",
        facecolor="white", edgecolor=light_grey, linewidth=1.0, zorder=5))
    # the filled portion uses the card's full edge colour (solid, no alpha)
    gw = min(s["gw"], track_w)
    ax.add_patch(Rectangle(
        (track_x, track_y - track_h / 2 + 0.012), gw, track_h - 0.024,
        facecolor=ec, edgecolor="none", zorder=6))

    # genome-size / status label below the bar
    ax.text(sx, track_y - 0.30, s["glabel"], ha="center", va="top",
            fontsize=8.2, fontweight="bold", color=ec, zorder=6)

# ── row label for the genome track, anchored to the first card ────────────
# Sits just left of the first card, vertically aligned with the bars, with a
# short connector so it clearly belongs to the genome row (no longer orphaned).
first = stations[0]
label_x = first["x"] - BOX_W / 2 - 0.18
ax.annotate(
    "schematic\ngenome",
    xy=(first["x"] - track_w / 2, track_y),
    xytext=(label_x, track_y),
    ha="right", va="center",
    fontsize=8.2, color=mid_grey, style="italic", linespacing=1.2,
    arrowprops=dict(arrowstyle="-", color=light_grey, linewidth=1.0,
                    shrinkA=2, shrinkB=2),
    zorder=6,
)

# Caption handled in markdown:
# "Genome reduction tightens the bond, but only a handful of symbioses have
#  crossed the threshold to organelle."

out_dir = Path(__file__).resolve().parents[1] / "img"
out_dir.mkdir(parents=True, exist_ok=True)
base = out_dir / "ch7_integration_spectrum"

plt.tight_layout(rect=(0.02, 0.03, 0.98, 0.95))
plt.savefig(base.with_suffix(".png"), dpi=300, bbox_inches="tight", facecolor="white")
plt.savefig(base.with_suffix(".pdf"), bbox_inches="tight", facecolor="white")
plt.close(fig)

print(f"Saved {base.with_suffix('.png')} and {base.with_suffix('.pdf')}")
