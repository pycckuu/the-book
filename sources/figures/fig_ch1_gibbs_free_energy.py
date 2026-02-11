"""
Figure: Gibbs free energy — the usable fraction
Chapter 1, The Budget of the Universe
Clean minimal style — bars, text, arrows. Matched palette to other figures.
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle
import numpy as np

fig, ax = plt.subplots(figsize=(10, 5.5))
fig.patch.set_facecolor('white')
ax.set_xlim(-0.8, 10.8)
ax.set_ylim(-0.5, 6.0)
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
# ═══════════════════════════════════════════════════════════
np.random.seed(11)
n_waves = 5
wave_origins_y = np.linspace(ts_bot + 0.2, ts_top - 0.2, n_waves)

for y0 in wave_origins_y:
    x0 = bar_left + bar_w + 0.1
    angle = np.random.uniform(-20, 20)
    length = np.random.uniform(1.2, 1.8)
    freq = np.random.uniform(6.0, 8.0)
    amp  = np.random.uniform(0.08, 0.12)
    rad  = np.radians(angle)

    t = np.linspace(0, length, 100)
    # Damped sine wave
    damping = np.exp(-1.5 * t / length) 
    # Actually we want it to start strong and fade, but amplitude constant or growing?
    # Let's keep amplitude constant but fade alpha
    
    wx = x0 + t * np.cos(rad) - amp * np.sin(freq * t) * np.sin(rad)
    wy = y0 + t * np.sin(rad) + amp * np.sin(freq * t) * np.cos(rad)

    alpha = np.linspace(0.6, 0.0, len(t))
    for j in range(len(t) - 1):
        ax.plot(wx[j:j+2], wy[j:j+2],
                color=red, alpha=float(alpha[j]), lw=1.8,
                solid_capstyle='round', zorder=1)

ax.text(bar_left + bar_w + 1.5, ts_top + 0.2,
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
# ═══════════════════════════════════════════════════════════
# Membrane as two parallel lines (bilayer)
mem_w = 0.4
mem_h = 5.2 # Taller than bar
mem_x = pump_cx - mem_w / 2

# Background for membrane
ax.add_patch(Rectangle((mem_x, dg_cy - mem_h/2), mem_w, mem_h,
             fc='#F0E8D8', ec='none', zorder=1))

# Two vertical lines
ax.plot([mem_x, mem_x], [dg_cy - mem_h/2, dg_cy + mem_h/2],
        color='#B8A888', lw=2, zorder=2)
ax.plot([mem_x + mem_w, mem_x + mem_w], [dg_cy - mem_h/2, dg_cy + mem_h/2],
        color='#B8A888', lw=2, zorder=2)

ax.text(pump_cx, dg_cy + mem_h / 2 + 0.25,
        'membrane', fontsize=10, ha='center', va='bottom',
        color='#999977', style='italic')

# Pump
pump_r = 0.7
ax.add_patch(plt.Circle((pump_cx, dg_cy), pump_r,
             fc=green_bg, ec=green, lw=2.5, zorder=3))
ax.text(pump_cx, dg_cy, 'pump',
        fontsize=12, fontweight='bold', ha='center', va='center',
        color=green, zorder=4)

# Ion arrows
ion_dx = 1.6
ion_dy_label = 1.2
ion_dy_tip   = 0.3

ion_kw = dict(arrowstyle='->', mutation_scale=18, linewidth=2, zorder=4)

# Left arrow (in)
ax.add_patch(FancyArrowPatch(
    (pump_cx - ion_dx, dg_cy + ion_dy_label - 0.2),
    (pump_cx - pump_r - 0.1, dg_cy + ion_dy_tip),
    connectionstyle='arc3,rad=-0.15', color=green, **ion_kw))

# Right arrow (out)
ax.add_patch(FancyArrowPatch(
    (pump_cx + pump_r + 0.1, dg_cy + ion_dy_tip),
    (pump_cx + ion_dx, dg_cy + ion_dy_label - 0.2),
    connectionstyle='arc3,rad=-0.15', color=green, **ion_kw))

ax.text(pump_cx - ion_dx, dg_cy + ion_dy_label,
        'ion', fontsize=11, fontweight='bold', ha='center', va='center', color=green)
ax.text(pump_cx + ion_dx, dg_cy + ion_dy_label,
        'ion', fontsize=11, fontweight='bold', ha='center', va='center', color=green)

ax.text(pump_cx - ion_dx, dg_cy - 0.6,
        'low\nconc.', fontsize=9, ha='center', va='center', color='#888888', linespacing=1.2)
ax.text(pump_cx + ion_dx, dg_cy - 0.6,
        'high\nconc.', fontsize=9, ha='center', va='center', color='#888888', linespacing=1.2)

# ═══════════════════════════════════════════════════════════
#  CAPTION (Removed - handled in markdown)
# ═══════════════════════════════════════════════════════════
# fig.text(0.5, 0.01,
#          'Not all energy is equal. Gibbs free energy is the fraction that can do work.',
#          ha='center', fontsize=11, style='italic', color='#666666')

plt.tight_layout(rect=[0.0, 0.05, 1.0, 0.98])
plt.savefig('/Users/igor/git/the-book/sources/img/ch1_gibbs_free_energy.png',
            dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig('/Users/igor/git/the-book/sources/img/ch1_gibbs_free_energy.pdf',
            bbox_inches='tight', facecolor='white')
print("Figure saved.")
