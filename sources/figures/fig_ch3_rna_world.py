"""
Figure: The chicken-and-egg problem, resolved.
Chapter 3, The Spark
Clean minimal style — circles, text, arrows. No crude icons.

Single-axes composition: the "problem" cluster (DNA/Proteins) on the left and
the "resolution" (RNA) on the right read as ONE argument, joined by a bridging
"resolved by" connector across the middle. RNA carries a self-replication loop
that closes the chicken-and-egg deadlock.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

# Palette — shared book theme
blue = "#2E6B8A"      # information
blue_bg = "#D4E8F0"
red = "#B5452A"       # catalysis
red_bg = "#F2DDD5"
green = "#4A7C59"      # RNA / resolution
green_bg = "#D8E8D8"
grey = "#333333"
mid_grey = "#8E8E8E"
arrow_c = "#888888"

fig, ax = plt.subplots(figsize=(10, 4.6))
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

ax.set_xlim(-2.4, 9.4)
ax.set_ylim(-2.6, 2.6)
ax.set_aspect("equal")
ax.axis("off")

fig.suptitle(
    "The chicken-and-egg problem, resolved",
    fontsize=15,
    fontweight="bold",
    y=0.97,
    color=grey,
)

# ══════════════════════════════════════
# LEFT CLUSTER — The chicken-and-egg problem
# ══════════════════════════════════════
lx = -0.55  # left-cluster center x

ax.text(lx, 2.18, "The problem", fontsize=13, fontweight="bold",
        ha="center", va="center", color=grey)

# DNA circle (top)
ax.add_patch(plt.Circle((lx, 1.15), 0.75, fc=blue_bg, ec=blue, lw=2, zorder=2))
ax.text(lx, 1.15, "DNA", fontsize=16, fontweight="bold", ha="center",
        va="center", color=blue, zorder=3)

# Protein circle (bottom)
ax.add_patch(plt.Circle((lx, -1.15), 0.75, fc=red_bg, ec=red, lw=2, zorder=2))
ax.text(lx, -1.15, "Proteins", fontsize=13, fontweight="bold", ha="center",
        va="center", color=red, zorder=3)

# Curved arrows between DNA and Proteins
arr_kw = dict(arrowstyle="->", mutation_scale=20, color=arrow_c,
              linewidth=1.8, zorder=4)
ax.add_patch(FancyArrowPatch((lx + 0.6, 0.4), (lx + 0.6, -0.4),
             connectionstyle="arc3,rad=-0.5", **arr_kw))
ax.add_patch(FancyArrowPatch((lx - 0.6, -0.4), (lx - 0.6, 0.4),
             connectionstyle="arc3,rad=-0.5", **arr_kw))

# Arrow labels — moved inward to hug their arrows
ax.text(lx + 1.02, 0, "encodes", fontsize=11, ha="center", va="center",
        color=arrow_c, rotation=-90, style="italic")
ax.text(lx - 1.02, 0, "copies", fontsize=11, ha="center", va="center",
        color=arrow_c, rotation=90, style="italic")

# Question mark — the unresolved deadlock
ax.text(lx, 0, "?", fontsize=40, ha="center", va="center",
        color=red, fontweight="bold", alpha=0.5, zorder=5)

# ══════════════════════════════════════
# BRIDGE — the two halves form ONE argument
# ══════════════════════════════════════
bridge_y = 0.0
ax.add_patch(FancyArrowPatch((lx + 1.55, bridge_y), (3.35, bridge_y),
             arrowstyle="-|>", mutation_scale=22, color=green,
             linewidth=2.6, zorder=4))
ax.text((lx + 1.55 + 3.35) / 2, bridge_y + 0.42, "resolved by",
        fontsize=12, ha="center", va="center", color=green,
        fontweight="bold", style="italic")

# ══════════════════════════════════════
# RIGHT CLUSTER — RNA resolves the deadlock
# ══════════════════════════════════════
rx = 4.55  # right-cluster (RNA) center x

ax.text(rx + 0.5, 2.18, "The resolution", fontsize=13, fontweight="bold",
        ha="center", va="center", color=grey)

# RNA circle (center)
ax.add_patch(plt.Circle((rx, 0), 0.85, fc=green_bg, ec=green, lw=2.5, zorder=3))
ax.text(rx, 0, "RNA", fontsize=18, fontweight="bold", ha="center",
        va="center", color=green, zorder=4)

# Self-replication loop — closes the chicken-and-egg
loop = FancyArrowPatch(
    (rx - 0.62, 0.58), (rx + 0.62, 0.58),
    connectionstyle="arc3,rad=-1.45",
    arrowstyle="-|>", mutation_scale=15, color=green,
    linewidth=1.8, zorder=5,
)
ax.add_patch(loop)
ax.text(rx, 1.78, "replicates\nitself", fontsize=10.5, ha="center",
        va="center", color=green, fontweight="bold", style="italic",
        linespacing=1.25, zorder=5)

# Function labels with bbox
box_blue = dict(boxstyle="round,pad=0.35", fc=blue_bg, ec=blue, lw=1.5)
box_red = dict(boxstyle="round,pad=0.35", fc=red_bg, ec=red, lw=1.5)

info_xy = (rx + 2.45, 1.25)
cat_xy = (rx + 2.45, -1.25)

ax.text(*info_xy, "stores\ninformation", fontsize=11.5, ha="center",
        va="center", color=blue, fontweight="bold", linespacing=1.3,
        bbox=box_blue, zorder=4)
ax.text(*cat_xy, "catalyzes\nreactions", fontsize=11.5, ha="center",
        va="center", color=red, fontweight="bold", linespacing=1.3,
        bbox=box_red, zorder=4)

# Connector arrows from RNA to its two jobs
ax.add_patch(FancyArrowPatch((rx + 0.62, 0.5), (rx + 1.55, 1.0),
             arrowstyle="-|>", mutation_scale=16, color=blue,
             linewidth=1.8, zorder=4))
ax.add_patch(FancyArrowPatch((rx + 0.62, -0.5), (rx + 1.55, -1.0),
             arrowstyle="-|>", mutation_scale=16, color=red,
             linewidth=1.8, zorder=4))

# ══════════════════════════════════════
# Save (portable, into THIS repo's sources/img)
# ══════════════════════════════════════
plt.subplots_adjust(left=0.02, right=0.98, top=0.88, bottom=0.04)

out_dir = Path(__file__).resolve().parents[1] / "img"
out_dir.mkdir(parents=True, exist_ok=True)
base = out_dir / "ch3_rna_world"

plt.savefig(base.with_suffix(".png"), dpi=300, bbox_inches="tight",
            facecolor="white")
plt.savefig(base.with_suffix(".pdf"), bbox_inches="tight", facecolor="white")
plt.close(fig)

print(f"Saved {base.with_suffix('.png')} and {base.with_suffix('.pdf')}")
