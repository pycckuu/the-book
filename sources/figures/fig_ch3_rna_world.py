"""
Figure: The chicken-and-egg problem, resolved.
Chapter 3, The Spark
Clean minimal style — circles, text, arrows. No crude icons.
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import numpy as np

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5))
fig.patch.set_facecolor('white')

# Palette — matched to ch2_planetary_divergence
blue    = '#2E6B8A'   # Earth color
blue_bg = '#D4E8F0'
red     = '#B5452A'   # Venus-adjacent warm tone
red_bg  = '#F2DDD5'
green   = '#4A7C59'   # muted olive-green
green_bg = '#D8E8D8'
grey    = '#333333'
arrow_c = '#888888'


# ══════════════════════════════════════
# LEFT PANEL — The chicken-and-egg problem
# ══════════════════════════════════════

ax1.set_xlim(-2.2, 2.2)
ax1.set_ylim(-2.5, 2.5)
ax1.set_aspect('equal')
ax1.axis('off')
ax1.set_title('The problem', fontsize=14, fontweight='bold', color=grey, pad=12)

# DNA circle (top)
ax1.add_patch(plt.Circle((0, 1.15), 0.75, fc=blue_bg, ec=blue, lw=2, zorder=2))
ax1.text(0, 1.15, 'DNA', fontsize=16, fontweight='bold', ha='center', va='center',
         color=blue, zorder=3)

# Protein circle (bottom)
ax1.add_patch(plt.Circle((0, -1.15), 0.75, fc=red_bg, ec=red, lw=2, zorder=2))
ax1.text(0, -1.15, 'Proteins', fontsize=14, fontweight='bold', ha='center', va='center',
         color=red, zorder=3)

# Curved arrows
arr_kw = dict(arrowstyle='->', mutation_scale=20, color=arrow_c, linewidth=1.8, zorder=4)
ax1.add_patch(FancyArrowPatch((0.6, 0.4), (0.6, -0.4),
              connectionstyle='arc3,rad=-0.5', **arr_kw))
ax1.add_patch(FancyArrowPatch((-0.6, -0.4), (-0.6, 0.4),
              connectionstyle='arc3,rad=-0.5', **arr_kw))

# Arrow labels
ax1.text(1.55, 0, 'encodes', fontsize=12, ha='center', va='center',
         color=arrow_c, rotation=-90, style='italic')
ax1.text(-1.55, 0, 'copies', fontsize=12, ha='center', va='center',
         color=arrow_c, rotation=90, style='italic')

# Question mark
ax1.text(0, 0, '?', fontsize=40, ha='center', va='center',
         color='#B5452A', fontweight='bold', alpha=0.5, zorder=5)


# ══════════════════════════════════════
# RIGHT PANEL — RNA resolves the deadlock
# ══════════════════════════════════════

ax2.set_xlim(-1.5, 3.0)
ax2.set_ylim(-2.5, 2.5)
ax2.set_aspect('equal')
ax2.axis('off')
ax2.set_title('The resolution', fontsize=14, fontweight='bold', color=grey, pad=12)

# RNA circle (center)
ax2.add_patch(plt.Circle((0, 0), 0.85, fc=green_bg, ec=green, lw=2.5, zorder=2))
ax2.text(0, 0, 'RNA', fontsize=18, fontweight='bold', ha='center', va='center',
         color=green, zorder=3)

# Function labels with bbox
box_blue = dict(boxstyle='round,pad=0.35', fc=blue_bg, ec=blue, lw=1.5)
box_red  = dict(boxstyle='round,pad=0.35', fc=red_bg, ec=red, lw=1.5)

ax2.text(1.8, 1.3, 'stores\ninformation', fontsize=12, ha='center', va='center',
         color=blue, fontweight='bold', linespacing=1.3, bbox=box_blue, zorder=3)
ax2.text(1.8, -1.3, 'catalyzes\nreactions', fontsize=12, ha='center', va='center',
         color=red, fontweight='bold', linespacing=1.3, bbox=box_red, zorder=3)

# Connector arrows
arr_green = dict(arrowstyle='->', mutation_scale=18, color=green, linewidth=1.8, zorder=4)
ax2.add_patch(FancyArrowPatch((0.65, 0.5), (1.0, 0.9),
              connectionstyle='arc3,rad=-0.1', **arr_green))
ax2.add_patch(FancyArrowPatch((0.65, -0.5), (1.0, -0.9),
              connectionstyle='arc3,rad=0.1', **arr_green))

# Caption (Removed - handled in markdown)
# fig.text(0.5, 0.01, 'RNA broke the deadlock by doing both jobs.',
#          ha='center', fontsize=11, style='italic', color='#666666')

plt.subplots_adjust(wspace=-0.1, left=0.01, right=0.99, top=0.88, bottom=0.10)
plt.savefig('/Users/igor/git/the-book/sources/img/ch3_rna_world.png',
            dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig('/Users/igor/git/the-book/sources/img/ch3_rna_world.pdf',
            bbox_inches='tight', facecolor='white')
print("Figure saved.")
