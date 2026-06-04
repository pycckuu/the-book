"""
Figure: A contaminated aquifer  (Chapter 10, The Water Planet)

A hydrocarbon plume in a sandy aquifer with groundwater flowing left to right.
Concentric redox zones nest around the source and stream downstream: an aerobic
fringe (blue, outermost), then nitrate-reducing (green), iron-reducing (sand),
and a combined sulfate-reducing / methanogenic core (grey, as the chapter
specifies), then the dark hydrocarbon source. Dissolved species flow in from the
surrounding aquifer (O2, NO3-, SO4(2-)) and reduced products stream out
downstream (Fe2+, CH4, HCO3-). Zone colors for O2/NO3/Fe match the Chapter 9
ladder so the two figures read as the same redox sequence. Zones are named by a
clean legend (no leader lines), keeping the only lines in the plume purposeful
flux arrows.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyArrowPatch, FancyBboxPatch, Rectangle

# ── palette (shared with the other figures) ───────────────────────────
blue = "#2E6B8A"
blue_bg = "#D4E8F0"
red = "#B5452A"
green = "#4A7C59"
green_bg = "#D8E8D8"
sand = "#C08A52"
sand_bg = "#F2E4D3"
grey = "#333333"
mid_grey = "#8E8E8E"
light_grey = "#D9D9D9"
core_fill = "#DDDDDD"
core_tc = "#5F5F5F"

fig, ax = plt.subplots(figsize=(13.0, 7.4), dpi=300)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")
ax.set_xlim(0, 14.7)
ax.set_ylim(0, 8.1)
ax.axis("off")

fig.suptitle("A contaminated aquifer", fontsize=14, fontweight="bold",
             y=0.975, color=grey)

# ── zone key: a clean horizontal legend in the top margin (NO leaders) ──
# Naming the zones with a tidy color key keeps the plume itself free of the
# label-leader lines that otherwise clutter the top of the figure.
legend = [
    (0.85,  blue_bg,  blue,     blue,    "aerobic fringe"),
    (4.05,  green_bg, green,    green,   "nitrate-reducing"),
    (7.15,  sand_bg,  sand,     sand,    "iron-reducing"),
    (10.20, core_fill, mid_grey, core_tc, "sulfate / methanogenic\ncore"),
]
key_y = 7.35
for sx, fc, ec, tc, name in legend:
    ax.add_patch(FancyBboxPatch(
        (sx, key_y - 0.17), 0.36, 0.34,
        boxstyle="round,pad=0.02,rounding_size=0.06",
        facecolor=fc, edgecolor=ec, linewidth=1.8, zorder=6))
    ax.text(sx + 0.50, key_y, name, ha="left", va="center", fontsize=9.5,
            fontweight="bold", color=tc, linespacing=1.12, zorder=6)

# ── aquifer body + water table ─────────────────────────────────────────
AQ_LEFT, AQ_RIGHT = 0.45, 13.55
AQ_BOT, AQ_TOP = 0.85, 6.35
ax.add_patch(Rectangle((AQ_LEFT, AQ_BOT), AQ_RIGHT - AQ_LEFT, AQ_TOP - AQ_BOT,
             facecolor=sand_bg, edgecolor=sand, linewidth=1.2, alpha=0.5,
             zorder=0))
ax.plot([AQ_LEFT, AQ_RIGHT], [AQ_TOP, AQ_TOP], color=blue, linewidth=1.3,
        linestyle=(0, (5, 3)), alpha=0.75, zorder=1)
ax.text(AQ_RIGHT - 0.10, AQ_TOP + 0.09, "water table", ha="right", va="bottom",
        fontsize=8.5, color=blue, style="italic", zorder=1)
ax.text(AQ_LEFT + 0.12, AQ_BOT + 0.14, "sandy aquifer", ha="left", va="bottom",
        fontsize=8.5, color=sand, style="italic", zorder=1)

# ── nested redox plume (outer -> inner; centers shift downstream) ──────
cy = 3.30
plume = [
    {"cx": 7.65, "w": 9.0, "h": 4.0, "fc": blue_bg,   "ec": blue},
    {"cx": 6.95, "w": 7.2, "h": 3.25, "fc": green_bg,  "ec": green},
    {"cx": 6.25, "w": 5.4, "h": 2.55, "fc": sand_bg,   "ec": sand},
    {"cx": 5.55, "w": 3.6, "h": 1.9, "fc": core_fill,  "ec": mid_grey},
]
for i, p in enumerate(plume):
    ax.add_patch(Ellipse((p["cx"], cy), p["w"], p["h"], facecolor=p["fc"],
                 edgecolor=p["ec"], linewidth=2.0, alpha=0.94, zorder=2 + i))


def ellipse_top_y(p, x):
    dx = max(-0.999, min(0.999, (x - p["cx"]) / (p["w"] / 2.0)))
    return cy + (p["h"] / 2.0) * (1 - dx * dx) ** 0.5


def ellipse_bot_y(p, x):
    dx = max(-0.999, min(0.999, (x - p["cx"]) / (p["w"] / 2.0)))
    return cy - (p["h"] / 2.0) * (1 - dx * dx) ** 0.5


# hydrocarbon source (dark, innermost)
src_x = 4.85
ax.add_patch(Ellipse((src_x, cy), 1.45, 1.0, facecolor=grey,
             edgecolor="black", linewidth=1.0, zorder=7))
ax.text(src_x, cy, "source", ha="center", va="center", fontsize=8.5,
        fontweight="bold", color="white", zorder=8)
# Label the whole zoned plume by pointing at its OUTER envelope (lower-left),
# so the leader never crosses the inner rings and does not duplicate "source".
ax.annotate("hydrocarbon plume", xy=(4.0, ellipse_bot_y(plume[0], 4.0)),
            xytext=(1.7, 1.35),
            fontsize=10, fontweight="bold", color=grey, ha="left", va="center",
            zorder=8,
            arrowprops=dict(arrowstyle="-", color=mid_grey, lw=1.1,
                            connectionstyle="arc3,rad=-0.15"))

# ── groundwater flow (left margin, three parallel arrows pointing right) ─
flow_arrow = dict(arrowstyle="-|>", mutation_scale=18, color=blue,
                  linewidth=2.4, alpha=0.85, zorder=3)
for fy in (2.30, 3.30, 4.30):
    ax.add_patch(FancyArrowPatch((0.80, fy), (2.25, fy), **flow_arrow))
ax.text(1.45, 4.92, "groundwater\nflow", ha="center", va="bottom",
        fontsize=9.5, color=blue, style="italic", fontweight="bold",
        linespacing=1.15, zorder=4)

# ── dissolved species IN (clean flux arrows; O2/NO3 from above, SO4 below) ─
in_arrow = dict(arrowstyle="-|>", mutation_scale=19, linewidth=2.3, zorder=6)

# O2 / NO3- enter from above; labels sit ABOVE the water-table line (not on it).
ax.add_patch(FancyArrowPatch((10.05, 6.30), (10.05, ellipse_top_y(plume[0], 10.05) - 0.04),
             color=blue, **in_arrow))
ax.text(10.05, 6.52, r"O$_2$", ha="center", va="bottom", fontsize=12.5,
        fontweight="bold", color=blue, zorder=7)

ax.add_patch(FancyArrowPatch((9.0, 6.30), (9.0, ellipse_top_y(plume[1], 9.0) - 0.04),
             color=green, **in_arrow))
ax.text(9.0, 6.52, r"NO$_3^-$", ha="center", va="bottom", fontsize=12.5,
        fontweight="bold", color=green, zorder=7)

# SO4(2-) is drawn down into the sulfate / methanogenic CORE (innermost grey
# zone, so it parallels O2->aerobic and NO3->nitrate); label below the frame.
so4_x = 5.4
ax.add_patch(FancyArrowPatch((so4_x, 1.02), (so4_x, ellipse_bot_y(plume[3], so4_x) + 0.04),
             color=red, **in_arrow))
ax.text(so4_x, 0.66, r"SO$_4^{2-}$", ha="center", va="top", fontsize=12.5,
        fontweight="bold", color=red, zorder=7)

ax.text(8.6, 0.62, "dissolved species in", ha="center", va="center",
        fontsize=9.0, color=mid_grey, style="italic", zorder=6)

# ── reduced products OUT (downstream, right margin) ────────────────────
out_arrow = dict(arrowstyle="-|>", mutation_scale=18, linewidth=2.4, zorder=6)
ax.text(13.3, 5.15, "products out", ha="center", va="bottom", fontsize=9.5,
        color=mid_grey, style="italic", zorder=6)
products = [
    (4.40, sand,    r"Fe$^{2+}$"),
    (3.50, grey,    r"HCO$_3^-$"),
    (2.60, core_tc, r"CH$_4$"),
]
for py, col, lab in products:
    # arrows cross the right aquifer wall (AQ_RIGHT=13.55) and exit; labels live
    # fully outside the aquifer so the frame line never runs through them.
    ax.add_patch(FancyArrowPatch((12.2, py), (13.9, py), color=col, **out_arrow))
    ax.text(14.05, py, lab, ha="left", va="center", fontsize=12.5,
            fontweight="bold", color=col, zorder=7)

# Caption handled in markdown:
# "The same redox ladder from sediments, replayed in an aquifer. The
#  conservation equation reads both."

out_dir = Path(__file__).resolve().parents[1] / "img"
out_dir.mkdir(parents=True, exist_ok=True)
base = out_dir / "ch10_aquifer_rtm"

plt.savefig(base.with_suffix(".png"), dpi=300, bbox_inches="tight", facecolor="white")
plt.savefig(base.with_suffix(".pdf"), bbox_inches="tight", facecolor="white")
plt.close(fig)

print(f"Saved {base.with_suffix('.png')} and {base.with_suffix('.pdf')}")
