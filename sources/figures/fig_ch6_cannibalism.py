"""
Figure: The B. subtilis cannibalism decision tree
Chapter 6, Cannibals and Voters

Same genome, same signal, two fates. A stochastic Spo0A~P split sends one
subpopulation to kill (SdpC toxin) and feed on its lysed siblings, delaying
sporulation, while sporulation waits as the deferred alternative. Clean
left -> right schematic; deterministic coordinates (no RNG) for reproducible
output. Palette matched to the other figures.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, FancyBboxPatch

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
cell_grey_bg = "#ECECEC"

fig, ax = plt.subplots(figsize=(12.0, 7.2), dpi=300)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")
ax.set_xlim(0, 13.2)
ax.set_ylim(0, 8.0)
ax.set_aspect("equal")
ax.axis("off")

fig.suptitle(
    "The cannibalism decision tree",
    fontsize=14,
    fontweight="bold",
    y=0.965,
    color=grey,
)

# ── helpers ────────────────────────────────────────────────────────────
ROD_W, ROD_H = 0.70, 0.30


def rod(cx, cy, fc, ec):
    """A bacterial cell drawn as a horizontal capsule."""
    ax.add_patch(
        FancyBboxPatch(
            (cx - ROD_W / 2, cy - ROD_H / 2),
            ROD_W,
            ROD_H,
            boxstyle="round,pad=0.02,rounding_size=0.15",
            facecolor=fc,
            edgecolor=ec,
            linewidth=1.4,
            zorder=4,
        )
    )


def rod_column(cx, cy, n, fc, ec, gap=0.46):
    """A vertical stack of n identical rods centered on (cx, cy)."""
    top = cy + (n - 1) * gap / 2
    for i in range(n):
        rod(cx, top - i * gap, fc, ec)


def labeled_arrow(p0, p1, color, label, lx, ly, ha="center", va="center",
                  sub=None, slx=None, sly=None, rad=0.0, ls="solid", lw=2.2,
                  mut=18, label_fs=10, sub_fs=8.5):
    """Draw an arrow plus a label (and optional italic sub-label)."""
    cs = f"arc3,rad={rad}" if rad else None
    ax.add_patch(
        FancyArrowPatch(
            p0, p1, arrowstyle="-|>", mutation_scale=mut,
            linewidth=lw, color=color, linestyle=ls,
            connectionstyle=cs, zorder=3, shrinkA=0, shrinkB=0,
        )
    )
    if label:
        ax.text(lx, ly, label, ha=ha, va=va, fontsize=label_fs,
                fontweight="bold", color=color, zorder=6, linespacing=1.12)
    if sub:
        ax.text(slx, sly, sub, ha=ha, va="top", fontsize=sub_fs,
                color=mid_grey, style="italic", zorder=6, linespacing=1.15)


# ── layout anchors (deterministic) ─────────────────────────────────────
y_mid = 4.55      # axis of the uniform population / switch
y_high = 6.35     # high Spo0A~P (deciders) row
y_low = 2.55      # low Spo0A~P (victims) row

x_pop = 1.30      # uniform population
x_switch = 3.55   # stochastic switch column position (split origin)
x_high = 6.10     # decider cell cluster
x_low = 6.10      # victim cell cluster

# ── stage 1: a starving, uniform population ────────────────────────────
rod_column(x_pop, y_mid, 5, cell_grey_bg, mid_grey)
ax.text(x_pop, y_mid + 1.55, "identical cells", ha="center", va="bottom",
        fontsize=11, fontweight="bold", color=grey)
ax.text(x_pop, y_mid - 1.58, "uniform, starving", ha="center", va="top",
        fontsize=9, color=mid_grey, style="italic")

# ── the stochastic switch ──────────────────────────────────────────────
ax.add_patch(FancyArrowPatch((x_pop + 0.85, y_mid), (x_switch - 0.32, y_mid),
             arrowstyle="-|>", mutation_scale=18, linewidth=2.2,
             color=grey, zorder=3))
ax.text((x_pop + 0.85 + x_switch - 0.32) / 2, y_mid + 0.42, r"Spo0A~P",
        ha="center", va="bottom", fontsize=10.5, fontweight="bold", color=grey)
ax.text((x_pop + 0.85 + x_switch - 0.32) / 2, y_mid - 0.40, "stochastic switch",
        ha="center", va="top", fontsize=9, color=mid_grey, style="italic")

# small dial node marking the branch point
ax.add_patch(Circle((x_switch, y_mid), 0.20, facecolor="white",
             edgecolor=grey, linewidth=1.8, zorder=5))
ax.add_patch(Circle((x_switch, y_mid), 0.055, facecolor=grey,
             edgecolor="none", zorder=6))

# split into two fates — two clearly-headed branch arrows
ax.add_patch(FancyArrowPatch((x_switch + 0.18, y_mid + 0.12),
             (x_high - 0.50, y_high - 0.18),
             arrowstyle="-|>", mutation_scale=18, linewidth=2.2,
             connectionstyle="arc3,rad=-0.20", color=blue, zorder=3))
ax.add_patch(FancyArrowPatch((x_switch + 0.18, y_mid - 0.12),
             (x_low - 0.50, y_low + 0.18),
             arrowstyle="-|>", mutation_scale=18, linewidth=2.2,
             connectionstyle="arc3,rad=0.20", color=mid_grey, zorder=3))

# ── upper fate: high Spo0A~P deciders (killers) ────────────────────────
rod_column(x_high, y_high, 3, blue_bg, blue)
ax.text(x_high, y_high + 1.05, r"high Spo0A~P", ha="center", va="bottom",
        fontsize=11, fontweight="bold", color=blue)
ax.text(x_high, y_high + 0.78, "deciders", ha="center", va="bottom",
        fontsize=9, color=blue, style="italic")

# ── lower fate: low Spo0A~P (victims) ──────────────────────────────────
rod_column(x_low, y_low, 3, cell_grey_bg, mid_grey)
ax.text(x_low, y_low - 0.78, r"low Spo0A~P", ha="center", va="top",
        fontsize=11, fontweight="bold", color=mid_grey)
ax.text(x_low, y_low - 1.05, "victims", ha="center", va="top",
        fontsize=9, color=mid_grey, style="italic")

# ── SdpC toxin: secreted by the deciders, kills the victims ────────────
# Dotted arrow runs in a clean vertical LANE just left of the clusters,
# clearly headed downward from the high row to the low row. Its label sits
# to the LEFT in open space, so toxin owns its own lane (no crossings).
toxin_x = x_high - 0.62
toxin_top = y_high - 0.52
toxin_bot = y_low + 0.52
ax.add_patch(FancyArrowPatch((toxin_x, toxin_top), (toxin_x, toxin_bot),
             arrowstyle="-|>", mutation_scale=16, color=red,
             linewidth=1.8, linestyle=(0, (1.2, 1.4)), zorder=4))
# toxin dots hug the lane (small deterministic offsets), evenly spaced and
# kept clear of the arrowhead at the bottom
n_dots = 5
d_top, d_bot = toxin_top - 0.33, toxin_bot + 0.55   # evenly spaced, clear of head
for k in range(n_dots):
    ty = d_top - k * (d_top - d_bot) / (n_dots - 1)
    off = -0.045 if k % 2 == 0 else 0.045
    ax.add_patch(Circle((toxin_x + off, ty), 0.056,
                 facecolor=red, edgecolor="none", zorder=5))
ax.text(toxin_x - 0.30, y_mid, "SdpC\ntoxin", ha="right", va="center",
        fontsize=10, fontweight="bold", color=red, linespacing=1.12, zorder=6)

# ── lysis releases nutrients ───────────────────────────────────────────
x_nutri = 8.85
ax.add_patch(FancyArrowPatch((x_low + 0.55, y_low), (x_nutri - 0.95, y_low),
             arrowstyle="-|>", mutation_scale=18, linewidth=2.2,
             color=mid_grey, zorder=3))
ax.text((x_low + 0.55 + x_nutri - 0.95) / 2, y_low + 0.38, "lysis",
        ha="center", va="bottom", fontsize=9.5, color=mid_grey, style="italic")

# nutrient cloud: a small cluster of translucent green disks
for dx, dy, r in [(-0.34, 0.12, 0.36), (0.26, 0.20, 0.32),
                  (0.34, -0.22, 0.29), (-0.20, -0.24, 0.28), (0.02, 0.0, 0.42)]:
    ax.add_patch(Circle((x_nutri + dx, y_low + dy), r, facecolor=green_bg,
                 edgecolor=green, linewidth=1.3, alpha=0.9, zorder=4))
ax.text(x_nutri, y_low - 0.92, "nutrients released", ha="center", va="top",
        fontsize=10, fontweight="bold", color=green, zorder=6)

# ── nutrients feed the deciders (feedback) ─────────────────────────────
# Routed through the open mid-right space and into the decider cluster's
# RIGHT edge, staying clear of the toxin lane (left of clusters) and below
# the blue outcome arrow — so nothing crosses.
ax.add_patch(FancyArrowPatch((x_nutri - 0.20, y_low + 0.78),
             (x_high + 0.48, y_high - 0.55),
             arrowstyle="-|>", mutation_scale=18, linewidth=2.2,
             connectionstyle="arc3,rad=0.26", color=green, zorder=3))
ax.text(7.35, y_mid + 0.30, "consumed", ha="center", va="center",
        fontsize=9.5, fontweight="bold", color=green, style="italic", zorder=6,
        bbox=dict(boxstyle="round,pad=0.15", facecolor="white", edgecolor="none",
                  alpha=0.85))

# ── decider outcome: delay sporulation / keep growing ──────────────────
box_x, box_y = 9.95, y_high
box_w, box_h = 3.0, 1.0
ax.add_patch(FancyArrowPatch((x_high + 0.55, y_high), (box_x - 0.12, y_high),
             arrowstyle="-|>", mutation_scale=18, linewidth=2.2,
             color=blue, zorder=3))
ax.add_patch(
    FancyBboxPatch((box_x, box_y - box_h / 2), box_w, box_h,
                   boxstyle="round,pad=0.06,rounding_size=0.12",
                   facecolor=green_bg, edgecolor=green, linewidth=2.0, zorder=4))
ax.text(box_x + box_w / 2, box_y, "delay sporulation\nkeep growing",
        ha="center", va="center", fontsize=10.5, fontweight="bold",
        color=green, linespacing=1.22, zorder=5)

# ── the deferred alternative: sporulation ──────────────────────────────
spore_cx, spore_cy = box_x + box_w / 2, 3.65
ax.add_patch(Ellipse((spore_cx, spore_cy), 1.85, 1.0, facecolor=sand_bg,
             edgecolor=sand, linewidth=1.6, alpha=0.85, zorder=3))
ax.text(spore_cx, spore_cy, "sporulation\n(deferred)", ha="center", va="center",
        fontsize=9.5, color=sand, style="italic", linespacing=1.2, zorder=4)
ax.add_patch(FancyArrowPatch((spore_cx, box_y - box_h / 2 - 0.06),
             (spore_cx, spore_cy + 0.55),
             arrowstyle="-|>", mutation_scale=15, color=sand,
             linewidth=1.8, linestyle=(0, (4, 3)), zorder=3))
ax.text(spore_cx + 0.18, (box_y - box_h / 2 + spore_cy + 0.55) / 2,
        "the deferred\nalternative", ha="left", va="center", fontsize=8.5,
        color=sand, style="italic", linespacing=1.15, zorder=5)

# Caption handled in markdown:
# "Same genome, same signal, two fates. The stochastic switch is the strategy."

out_dir = Path(__file__).resolve().parents[1] / "img"
out_dir.mkdir(parents=True, exist_ok=True)
base = out_dir / "ch6_cannibalism"

plt.savefig(base.with_suffix(".png"), dpi=300, bbox_inches="tight", facecolor="white")
plt.savefig(base.with_suffix(".pdf"), bbox_inches="tight", facecolor="white")
plt.close(fig)

print(f"Saved {base.with_suffix('.png')} and {base.with_suffix('.pdf')}")
