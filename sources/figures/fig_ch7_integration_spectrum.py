"""
Figure: Different forms of symbiotic integration
Chapter 7, The Merger

Four categorical examples, not stages of one lineage or an integration metric.
Genome labels identify selected chromosomes/reference mtDNA; no proportional bars.
Elysia represents acquired plastids, not an inherited symbiont chromosome.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

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
    "Different forms of symbiotic integration",
    fontsize=14,
    fontweight="bold",
    y=0.97,
    color=grey,
)

# Four categorical examples; genome sizes are organism-specific labels.
stations = [
    {
        "x": 2.55, "fc": green_bg, "ec": green,
        "name": "Ruthia magnifica",
        "desc": "Clam endosymbiont;\ncore metabolic pathways encoded",
        "basis": "Strain Cm chromosome\n1.16 Mb",
        "italic": True,
    },
    {
        "x": 5.35, "fc": blue_bg, "ec": blue,
        "name": "Elysia chlorotica",
        "desc": "Plastids from V. litorea;\nacquired anew by feeding",
        "basis": "No inherited symbiont\nchromosome represented",
        "italic": True,
    },
    {
        "x": 8.15, "fc": sand_bg, "ec": sand,
        "name": "Carsonella ruddii",
        "desc": "Obligate psyllid symbiont;\nstrong genome reduction",
        "basis": "Strain PV chromosome\n160 kb",
        "italic": True,
    },
    {
        "x": 10.95, "fc": red_bg, "ec": red,
        "name": "Human mitochondrion",
        "desc": "Organelle; depends on\nnuclear-encoded proteins",
        "basis": "Human reference mtDNA\n16.6 kb",
        "italic": False,
    },
]

BOX_W, BOX_H = 2.46, 2.02
box_cy = 5.05
label_y = box_cy - 0.60

# Equal cards and ordinary labels do not encode genome length or integration.
for s in stations:
    sx, ec = s["x"], s["ec"]

    # station card
    ax.add_patch(FancyBboxPatch(
        (sx - BOX_W / 2, box_cy - BOX_H / 2), BOX_W, BOX_H,
        boxstyle="round,pad=0.02,rounding_size=0.10",
        facecolor=s["fc"], edgecolor=ec, linewidth=1.8, zorder=3))

    # species name (italic) and description
    ax.text(sx, box_cy + 0.66, s["name"], ha="center", va="center",
            fontsize=10.5, fontweight="bold",
            fontstyle="italic" if s["italic"] else "normal",
            color=ec, zorder=6)
    ax.text(sx, box_cy + 0.16, s["desc"], ha="center", va="center",
            fontsize=8.2, color=grey, linespacing=1.25, zorder=6)

    # Labels are not bars or scores.
    ax.text(sx, label_y, s["basis"], ha="center", va="center",
            fontsize=8.2, fontweight="bold", color=ec, linespacing=1.25, zorder=6)

ax.text(6.75, 2.55, "Different associations, not evolutionary stages",
        ha="center", va="center", fontsize=9.5, color=mid_grey)

# Caption and organism/reference-sequence evidence are supplied in Markdown.

out_dir = Path(__file__).resolve().parents[1] / "img"
out_dir.mkdir(parents=True, exist_ok=True)
base = out_dir / "ch7_integration_spectrum"

plt.tight_layout(rect=(0.02, 0.03, 0.98, 0.95))
plt.savefig(base.with_suffix(".png"), dpi=300, bbox_inches="tight", facecolor="white")
plt.savefig(base.with_suffix(".pdf"), bbox_inches="tight", facecolor="white")
plt.close(fig)

print(f"Saved {base.with_suffix('.png')} and {base.with_suffix('.pdf')}")
