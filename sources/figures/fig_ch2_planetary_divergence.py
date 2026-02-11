"""
Figure: Planetary divergence at ~3.5 Ga
Chapter 2, The Stage
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

fig, axes = plt.subplots(1, 3, figsize=(12, 6), sharey=True)
fig.patch.set_facecolor('white')

planets = [
    {
        'name': 'Venus',
        'color': '#D4511E',
        'light': '#F4A460',
        'temp_low': 0,
        'temp_high': 460,
        'temp_best': None,  # no best estimate -- that's the point
        'pressure': '~1 to ~90 atm',
        'atmosphere': 'CO$_2$, N$_2$, H$_2$O(?)',
        'magnetic': 'No',
        'water': 'Oceans? Or\nalready lost',
        'note': 'D/H ratio proves\nmassive water loss;\ntiming unknown',
    },
    {
        'name': 'Earth',
        'color': '#2E6B8A',
        'light': '#87CEEB',
        'temp_low': 0,
        'temp_high': 70,
        'temp_best': 25,
        'pressure': '~1 atm',
        'atmosphere': 'CO$_2$, N$_2$, CH$_4$\nno free O$_2$',
        'magnetic': 'Yes',
        'water': 'Global ocean\n(confirmed)',
        'note': 'Stromatolites by 3.5 Ga;\nzircons confirm liquid\nwater to 4.4 Ga',
    },
    {
        'name': 'Mars',
        'color': '#A0522D',
        'light': '#DEB887',
        'temp_low': -60,
        'temp_high': 20,
        'temp_best': None,
        'pressure': '0.5--2 atm(?)',
        'atmosphere': 'CO$_2$, N$_2$',
        'magnetic': 'Recently lost',
        'water': 'Rivers, lakes,\npossibly ocean',
        'note': 'Late Noachian;\nwarm-wet vs.\ncold-with-thaw debated',
    },
]

for ax, p in zip(axes, planets):
    # Temperature uncertainty bar
    bar_width = 0.4
    bar_x = 0.5

    # Draw the uncertainty range as a colored bar
    ax.bar(bar_x, p['temp_high'] - p['temp_low'],
           bottom=p['temp_low'], width=bar_width,
           color=p['light'], edgecolor=p['color'], linewidth=2,
           alpha=0.7, zorder=2)

    # Best estimate marker (if known)
    if p['temp_best'] is not None:
        ax.plot(bar_x, p['temp_best'], 'o', color=p['color'],
                markersize=10, zorder=3, markeredgecolor='white', markeredgewidth=1.5)
        ax.annotate(f"{p['temp_best']}°C",
                    xy=(bar_x, p['temp_best']),
                    xytext=(bar_x + 0.32, p['temp_best']),
                    fontsize=9, color=p['color'], fontweight='bold',
                    va='center')

    # Range labels
    ax.annotate(f"{p['temp_high']}°C",
                xy=(bar_x, p['temp_high']),
                xytext=(bar_x + 0.32, p['temp_high']),
                fontsize=8, color='#444444', va='center')
    ax.annotate(f"{p['temp_low']}°C",
                xy=(bar_x, p['temp_low']),
                xytext=(bar_x + 0.32, p['temp_low']),
                fontsize=8, color='#444444', va='center')

    # Planet name
    ax.set_title(p['name'], fontsize=16, fontweight='bold', color=p['color'], pad=12)

    # Data annotations on the right side
    info_x = 1.15
    info_items = [
        ('Pressure', p['pressure']),
        ('Atmosphere', p['atmosphere']),
        ('Magnetic field', p['magnetic']),
        ('Liquid water', p['water']),
    ]

    y_start = 420
    for label, value in info_items:
        ax.text(info_x, y_start, label, fontsize=7.5, fontweight='bold',
                color='#333333', transform=ax.transData, va='top')
        ax.text(info_x, y_start - 22, value, fontsize=8,
                color='#555555', transform=ax.transData, va='top',
                linespacing=1.3)
        y_start -= 75

    # Note at bottom
    ax.text(info_x, -100, p['note'], fontsize=7, color='#777777',
            transform=ax.transData, va='top', style='italic',
            linespacing=1.3)

    # Formatting
    ax.set_xlim(0, 2.2)
    ax.set_xticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    # Reference lines
    ax.axhline(y=0, color='#CCCCCC', linewidth=0.5, linestyle='--', zorder=1)
    ax.axhline(y=100, color='#CCCCCC', linewidth=0.5, linestyle='--', zorder=1)

# Y-axis label (only on first panel)
axes[0].set_ylabel('Surface temperature (°C)', fontsize=11)
axes[0].set_ylim(-120, 500)

# Add 0°C and 100°C reference labels (on right side of last panel to avoid overlap)
axes[2].text(2.35, 0, '0°C\n(freezing)', fontsize=7, color='#999999',
             va='center', ha='left', transform=axes[2].transData)
axes[2].text(2.35, 100, '100°C\n(boiling)', fontsize=7, color='#999999',
             va='center', ha='left', transform=axes[2].transData)

# Suptitle
fig.suptitle('The divergence at ~3.5 Ga', fontsize=14, fontweight='bold',
             y=0.98, color='#222222')

# Caption
fig.text(0.5, 0.01,
         'Same raw materials, same physics, three different outcomes — but only one is well constrained.',
         ha='center', fontsize=10, style='italic', color='#555555')

plt.tight_layout(rect=[0.02, 0.04, 0.98, 0.94])
plt.savefig('/Users/igor/conductor/workspaces/the-book/abu-dhabi/sources/img/ch2_planetary_divergence.png',
            dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig('/Users/igor/conductor/workspaces/the-book/abu-dhabi/sources/img/ch2_planetary_divergence.pdf',
            bbox_inches='tight', facecolor='white')
print("Figure saved.")
