"""
Figure: A porewater profile  (Chapter 8, The Equation -- the book's title figure)

Oxygen, sulfate, and methane against depth, with depth increasing downward and
three shaded redox zones. The sulfate-methane transition (SMT) is computed from
the curves' crossing, not hardcoded. The curves are SCHEMATIC / illustrative
(smooth analytic functions, no measured data), consistent with the qualitative
description in the chapter text. Palette matched to the other figures.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
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
grey = "#333333"
mid_grey = "#8E8E8E"
light_grey = "#D9D9D9"

# ── schematic profiles (illustrative, not measured) ────────────────────
DEPTH_MAX = 120.0          # cm
SMT_GUESS = 80.0           # cm, where sulfate and methane curves cross
z = np.linspace(0, DEPTH_MAX, 600)
o2 = np.exp(-z / 1.4)                              # gone within the top few cm (oxic base ~5-6 cm)
so4 = 0.92 / (1 + np.exp((z - SMT_GUESS) / 9.0))   # plateau, then declines
ch4 = 0.95 / (1 + np.exp(-(z - SMT_GUESS) / 9.0))  # ~0 above SMT, rises below

# crossing depth derived from the arrays (so it stays correct if params change)
cross_idx = int(np.argmin(np.abs(so4 - ch4)))
smt_depth = float(z[cross_idx])
smt_x = float(so4[cross_idx])
oxic_base = float(z[np.argmax(o2 < 0.02)])         # depth where O2 is spent
o2 = np.where(o2 < 0.01, np.nan, o2)               # mask the spent tail so O2 does not trail down the axis

fig, ax = plt.subplots(figsize=(7.8, 8.8), dpi=300)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

X_MAX = 1.16

# ── three redox zones (shaded bands) ───────────────────────────────────
ax.axhspan(0, oxic_base, facecolor=blue_bg, alpha=0.7, zorder=0)
ax.axhspan(oxic_base, smt_depth, facecolor=sand_bg, alpha=0.7, zorder=0)
ax.axhspan(smt_depth, DEPTH_MAX, facecolor=green_bg, alpha=0.7, zorder=0)

# faint hairlines at the zone boundaries for a crisp read
ax.axhline(oxic_base, color="white", linewidth=1.0, zorder=1)


def zone_chip(x, y, text, color, ha="right"):
    """A soft rounded label chip naming a redox zone."""
    ax.text(
        x, y, text, ha=ha, va="center",
        fontsize=9.5, color=color, style="italic", linespacing=1.18, zorder=7,
        bbox=dict(boxstyle="round,pad=0.34,rounding_size=0.5",
                  facecolor="white", edgecolor=color, linewidth=1.0, alpha=0.95),
    )


# The oxic band is thin (top ~6 cm); label it directly inside the blue band
# (no leader needed) so the chip no longer floats down in the sulfate band.
zone_chip(X_MAX - 0.025, 4.0, "oxygen\nzone", blue)
zone_chip(X_MAX - 0.025, (oxic_base + smt_depth) / 2, "sulfate\nzone", sand)
zone_chip(X_MAX - 0.025, (smt_depth + DEPTH_MAX) / 2 + 8, "methane\nzone", green)

# ── curves ──────────────────────────────────────────────────────────────
ax.plot(o2, z, color=blue, linewidth=2.8, zorder=4, solid_capstyle="round")
ax.plot(so4, z, color=sand, linewidth=2.8, zorder=4, solid_capstyle="round")
ax.plot(ch4, z, color=green, linewidth=2.8, zorder=4, solid_capstyle="round")

# ── curve labels: each sits in clear space beside its own curve ─────────
# O2 collapses in the top few cm; label sits just right of the steep knee, with
# a short descending connector so it reads as O2 and not as part of the curve.
ax.text(0.40, 4.4, r"O$_2$", ha="left", va="center",
        fontsize=15, fontweight="bold", color=blue, zorder=7)
ax.add_patch(FancyArrowPatch(
    (0.40, 4.0), (0.205, 2.5),
    arrowstyle="-|>", mutation_scale=15, color=blue, linewidth=1.4,
    shrinkA=3, shrinkB=2, zorder=6,
))

# SO4 plateaus near x=0.92; place the label just LEFT of the plateau in open
# space so it does not sit on top of its own curve.
ax.text(0.84, 28, r"SO$_4^{2-}$", ha="right", va="center",
        fontsize=15, fontweight="bold", color=sand, zorder=7)

# CH4 rises on the right below the SMT; label it on its lower plateau.
ax.text(0.905, 104, r"CH$_4$", ha="left", va="center",
        fontsize=15, fontweight="bold", color=green, zorder=7)

# ── sulfate-methane transition (computed crossing) ─────────────────────
ax.axhline(smt_depth, color=red, linewidth=1.6, linestyle=(0, (6, 4)), zorder=3)
ax.plot(smt_x, smt_depth, "o", color=red, markersize=9,
        markeredgecolor="white", markeredgewidth=1.6, zorder=8)

# SMT label at the LEFT end of the red dashed line (the dashed line itself is
# the connector to the crossing marker), in clear space off both curves.
ax.text(0.04, smt_depth - 1.5, "sulfate–methane\ntransition (SMT)",
        ha="left", va="bottom", fontsize=9, fontweight="bold", color=red,
        linespacing=1.18, zorder=8)

# ── axes: depth increases downward; concentration is relative ──────────
ax.set_xlim(0, X_MAX)
ax.set_ylim(DEPTH_MAX, 0)            # inverted: 0 at top, deepest at bottom
ax.set_ylabel("depth (cm)", fontsize=11, color=grey)
ax.set_xlabel("relative concentration", fontsize=11, color=grey, labelpad=8)
ax.set_xticks([])                    # relative/schematic: no numeric x scale
ax.tick_params(axis="y", labelsize=9.5, colors="#666666", length=0)
ax.set_yticks(np.arange(0, DEPTH_MAX + 1, 20))

for spine in ("top", "right"):
    ax.spines[spine].set_visible(False)
for spine in ("left", "bottom"):
    ax.spines[spine].set_color(light_grey)
    ax.spines[spine].set_linewidth(1.2)

# "schematic" note tucked at the bottom-left, in clear space far from labels.
ax.text(0.02, DEPTH_MAX - 2.5, "schematic", ha="left", va="bottom",
        fontsize=8.5, color=mid_grey, style="italic", zorder=7)

fig.suptitle("A porewater profile", fontsize=14, fontweight="bold",
             y=0.965, color=grey)

# Caption handled in markdown.

out_dir = Path(__file__).resolve().parents[1] / "img"
out_dir.mkdir(parents=True, exist_ok=True)
base = out_dir / "ch8_porewater_profile"

plt.tight_layout(rect=(0.02, 0.02, 0.98, 0.95))
plt.savefig(base.with_suffix(".png"), dpi=300, bbox_inches="tight", facecolor="white")
plt.savefig(base.with_suffix(".pdf"), bbox_inches="tight", facecolor="white")
plt.close(fig)

print(f"Saved {base.with_suffix('.png')} and {base.with_suffix('.pdf')}")
print(f"  (SMT crossing at {smt_depth:.0f} cm; oxic base at {oxic_base:.0f} cm)")
