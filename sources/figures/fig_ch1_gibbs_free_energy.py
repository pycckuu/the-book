"""
Figure: Gibbs free energy — the usable fraction
Chapter 1, The Budget of the Universe
Clean minimal style — bars, text, arrows. Matched palette to other figures.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle
import numpy as np

fig, ax = plt.subplots(figsize=(10, 5.5))
fig.patch.set_facecolor('white')
ax.set_xlim(-0.8, 10.8)
ax.set_ylim(-0.9, 6.4)
ax.set_aspect('equal')
ax.axis('off')

blue    = '#2E6B8A'
blue_bg = '#D4E8F0'
red     = '#B5452A'
red_bg  = '#F2DDD5'
green   = '#4A7C59'
green_bg = '#D8E8D8'
grey    = '#333333'

# ═══════════════════════════════════════════════════════════
#  LAYOUT GRID
# ═══════════════════════════════════════════════════════════
fig_cy   = 2.75
bar_cx   = 2.1
pump_cx  = 8.2
bar_w    = 1.8
bar_h    = 4.6
dg_frac  = 0.60
dg_h     = bar_h * dg_frac
ts_h     = bar_h - dg_h

bar_left = bar_cx - bar_w / 2
bar_bot  = fig_cy - bar_h / 2
dg_bot   = bar_bot
dg_top   = dg_bot + dg_h
ts_bot   = dg_top
ts_top   = ts_bot + ts_h
dg_cy    = (dg_bot + dg_top) / 2
ts_cy    = (ts_bot + ts_top) / 2

# ═══════════════════════════════════════════════════════════
#  ΔG / TΔS STACKED BAR
# ═══════════════════════════════════════════════════════════
ax.add_patch(FancyBboxPatch((bar_left, dg_bot), bar_w, dg_h,
             boxstyle='round,pad=0.06', fc=blue_bg, ec=blue, lw=2, zorder=2))
ax.add_patch(FancyBboxPatch((bar_left, ts_bot), bar_w, ts_h,
             boxstyle='round,pad=0.06', fc=red_bg, ec=red, lw=2, zorder=2))

ax.text(bar_cx, dg_cy + 0.2, r'$\Delta G$',
        fontsize=24, fontweight='bold', ha='center', va='center', color=blue, zorder=3)
ax.text(bar_cx, dg_cy - 0.5, 'usable work',
        fontsize=11, ha='center', va='center', color=blue, zorder=3)

ax.text(bar_cx, ts_cy + 0.1, r'$T\Delta S$',
        fontsize=18, fontweight='bold', ha='center', va='center', color=red, zorder=3)
ax.text(bar_cx, ts_cy - 0.4, 'entropy tax',
        fontsize=10, ha='center', va='center', color=red, zorder=3)

# ═══════════════════════════════════════════════════════════
#  ΔH BRACKET (left)
# ═══════════════════════════════════════════════════════════
bx   = bar_left - 0.3
tick = 0.12
mid  = fig_cy
notch = 0.18

ax.plot([bx, bx], [bar_bot, mid - notch], color=grey, lw=1.5, solid_capstyle='round')
ax.plot([bx, bx], [mid + notch, ts_top], color=grey, lw=1.5, solid_capstyle='round')
ax.plot([bx, bx + tick], [bar_bot, bar_bot], color=grey, lw=1.5, solid_capstyle='round')
ax.plot([bx, bx + tick], [ts_top, ts_top], color=grey, lw=1.5, solid_capstyle='round')
ax.plot([bx, bx - tick], [mid - notch, mid], color=grey, lw=1.5, solid_capstyle='round')
ax.plot([bx, bx - tick], [mid + notch, mid], color=grey, lw=1.5, solid_capstyle='round')

ax.text(bx - 0.6, mid, r'$\Delta H$',
        fontsize=24, fontweight='bold', ha='center', va='center', color=grey)

# ═══════════════════════════════════════════════════════════
#  WAVY HEAT LINES (radiate right from TΔS block)
#  Deterministic fan: a few clean, non-crossing damped wavelets.
# ═══════════════════════════════════════════════════════════
x0 = bar_left + bar_w + 0.1
# Fan strokes out from a common pivot so they never cross.
# Each stroke: fixed launch angle (monotonic), modest length, gentle wiggle.
wave_specs = [
    {'y0': ts_bot + 0.30, 'angle': -16.0, 'length': 1.45, 'freq': 6.5, 'amp': 0.085},
    {'y0': ts_bot + 0.95, 'angle': -5.0,  'length': 1.60, 'freq': 6.5, 'amp': 0.085},
    {'y0': ts_top - 0.55, 'angle':  6.0,  'length': 1.60, 'freq': 6.5, 'amp': 0.085},
    {'y0': ts_top - 0.05, 'angle': 16.0,  'length': 1.45, 'freq': 6.5, 'amp': 0.085},
]

for spec in wave_specs:
    y0 = spec['y0']
    rad = np.radians(spec['angle'])
    length = spec['length']
    freq = spec['freq']
    amp = spec['amp']

    t = np.linspace(0, length, 120)
    # Wiggle amplitude ramps from 0 so each stroke leaves the bar smoothly,
    # keeping the launch points apart and the strokes from tangling.
    ramp = np.clip(t / 0.35, 0.0, 1.0)
    wiggle = amp * ramp * np.sin(freq * t)

    wx = x0 + t * np.cos(rad) - wiggle * np.sin(rad)
    wy = y0 + t * np.sin(rad) + wiggle * np.cos(rad)

    alpha = np.linspace(0.65, 0.0, len(t))
    for j in range(len(t) - 1):
        ax.plot(wx[j:j+2], wy[j:j+2],
                color=red, alpha=float(alpha[j]), lw=1.8,
                solid_capstyle='round', zorder=1)

ax.text(bar_left + bar_w + 1.5, ts_top + 0.45,
        'dissipated as heat',
        fontsize=10, ha='center', va='center', color=red, style='italic')

# ═══════════════════════════════════════════════════════════
#  "DRIVES" ARROW
# ═══════════════════════════════════════════════════════════
arr_x0 = bar_left + bar_w + 0.2
arr_x1 = pump_cx - 1.8

ax.add_patch(FancyArrowPatch(
    (arr_x0, dg_cy), (arr_x1, dg_cy),
    arrowstyle='->', mutation_scale=25, color=blue, linewidth=3, zorder=4))

ax.text((arr_x0 + arr_x1) / 2, dg_cy + 0.35,
        'drives', fontsize=12, ha='center', va='center',
        color=blue, style='italic')

# ═══════════════════════════════════════════════════════════
#  ION PUMP & MEMBRANE
#  Cluster is centred on the bar's vertical centre (fig_cy) for balance.
#  Membrane is symmetric about the pump and ends cleanly INSIDE the axes.
# ═══════════════════════════════════════════════════════════
pump_cy = fig_cy

# Membrane as two parallel lines (bilayer), sized to sit inside the axes
# with a symmetric margin top and bottom.
mem_w = 0.4
mem_margin = 0.45  # gap between membrane end and the axis limits
# Symmetric about the pump, sized to span a little past the bar yet stay
# inside the axes with a clean margin top and bottom.
mem_half = min(pump_cy - (ax.get_ylim()[0] + mem_margin),
               (ax.get_ylim()[1] - mem_margin) - pump_cy,
               bar_h / 2 + 0.45)
mem_top = pump_cy + mem_half
mem_bot = pump_cy - mem_half
mem_x = pump_cx - mem_w / 2

# Background for membrane
ax.add_patch(Rectangle((mem_x, mem_bot), mem_w, mem_top - mem_bot,
             fc='#F0E8D8', ec='none', zorder=1))

# Two vertical lines
ax.plot([mem_x, mem_x], [mem_bot, mem_top],
        color='#B8A888', lw=2, zorder=2)
ax.plot([mem_x + mem_w, mem_x + mem_w], [mem_bot, mem_top],
        color='#B8A888', lw=2, zorder=2)

ax.text(pump_cx, mem_top + 0.18,
        'membrane', fontsize=10, ha='center', va='bottom',
        color='#999977', style='italic')

# Pump
pump_r = 0.7
ax.add_patch(plt.Circle((pump_cx, pump_cy), pump_r,
             fc=green_bg, ec=green, lw=2.5, zorder=3))
ax.text(pump_cx, pump_cy, 'pump',
        fontsize=12, fontweight='bold', ha='center', va='center',
        color=green, zorder=4)

# Ion arrows
ion_dx = 1.6
ion_dy_label = 1.2
ion_dy_tip   = 0.3

ion_kw = dict(arrowstyle='->', mutation_scale=18, linewidth=2, zorder=4)

# Left arrow (in)
ax.add_patch(FancyArrowPatch(
    (pump_cx - ion_dx, pump_cy + ion_dy_label - 0.2),
    (pump_cx - pump_r - 0.1, pump_cy + ion_dy_tip),
    connectionstyle='arc3,rad=-0.15', color=green, **ion_kw))

# Right arrow (out)
ax.add_patch(FancyArrowPatch(
    (pump_cx + pump_r + 0.1, pump_cy + ion_dy_tip),
    (pump_cx + ion_dx, pump_cy + ion_dy_label - 0.2),
    connectionstyle='arc3,rad=-0.15', color=green, **ion_kw))

ax.text(pump_cx - ion_dx, pump_cy + ion_dy_label,
        'ion', fontsize=11, fontweight='bold', ha='center', va='center', color=green)
ax.text(pump_cx + ion_dx, pump_cy + ion_dy_label,
        'ion', fontsize=11, fontweight='bold', ha='center', va='center', color=green)

ax.text(pump_cx - ion_dx, pump_cy - 0.6,
        'low\nconc.', fontsize=9, ha='center', va='center', color='#888888', linespacing=1.2)
ax.text(pump_cx + ion_dx, pump_cy - 0.6,
        'high\nconc.', fontsize=9, ha='center', va='center', color='#888888', linespacing=1.2)

# ═══════════════════════════════════════════════════════════
#  CAPTION (Removed - handled in markdown)
# ═══════════════════════════════════════════════════════════
# fig.text(0.5, 0.01,
#          'Not all energy is equal. Gibbs free energy is the fraction that can do work.',
#          ha='center', fontsize=11, style='italic', color='#666666')

plt.tight_layout(rect=[0.0, 0.05, 1.0, 0.98])

out_dir = Path(__file__).resolve().parents[1] / "img"
out_dir.mkdir(parents=True, exist_ok=True)
base = out_dir / "ch1_gibbs_free_energy"
plt.savefig(base.with_suffix(".png"),
            dpi=300, bbox_inches="tight", facecolor="white")
plt.savefig(base.with_suffix(".pdf"),
            bbox_inches="tight", facecolor="white")
plt.close(fig)
print(f"Saved {base.with_suffix('.png')} and {base.with_suffix('.pdf')}")
