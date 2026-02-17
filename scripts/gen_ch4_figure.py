"""
Generate Ch4 mat cross-section figure — book-quality version.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import numpy as np

# ── palette ──────────────────────────────────────────────────────────
BG = "#FFFFFF"
GREEN_FILL = "#D8E8D8";  GREEN_EDGE = "#4A7C59";  GREEN_TXT = "#3E6B4A"
PINK_FILL  = "#F2DDD5";  PINK_EDGE  = "#C0756A";  PINK_TXT  = "#A05A50"
DARK_FILL  = "#C4B8A8";  DARK_EDGE  = "#8B7D6B";  DARK_TXT  = "#5A4E3E"
H2S_CLR    = "#D4824A"
SO4_CLR    = "#2E6B8A"
SUN_CLR    = "#E8B84B"
GREY       = "#555555"
LIGHT_GREY = "#AAAAAA"

# ── canvas (wider for breathing room) ────────────────────────────────
W, H = 14, 8
fig, ax = plt.subplots(figsize=(W, H), dpi=300)
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, W); ax.set_ylim(0, H)
ax.set_aspect("equal"); ax.axis("off")

# ── layout ───────────────────────────────────────────────────────────
mat_L  = 4.2;  mat_R = 9.8
mat_W  = mat_R - mat_L
mat_cx = (mat_L + mat_R) / 2

lh = 1.6          # taller layers for more padding
cr = 0.08

dark_b = 1.6;  dark_t = dark_b + lh
pink_b = dark_t;  pink_t = pink_b + lh
grn_b  = pink_t;  grn_t  = grn_b + lh

# ── layers ───────────────────────────────────────────────────────────
def draw_layer(y0, h, fc, ec):
    ax.add_patch(FancyBboxPatch(
        (mat_L, y0), mat_W, h,
        boxstyle=f"round,pad=0,rounding_size={cr}",
        facecolor=fc, edgecolor=ec, linewidth=1.8, zorder=2))
    # subtle bottom strip
    ax.add_patch(mpatches.Rectangle(
        (mat_L + cr, y0), mat_W - 2*cr, h*0.18,
        facecolor=ec, alpha=0.06, edgecolor="none", zorder=2.1))

draw_layer(dark_b, lh, DARK_FILL, DARK_EDGE)
draw_layer(pink_b, lh, PINK_FILL, PINK_EDGE)
draw_layer(grn_b,  lh, GREEN_FILL, GREEN_EDGE)

# ── light attenuation gradient ───────────────────────────────────────
n = 256
rgba = np.zeros((n, 1, 4))
rgba[:, 0, 3] = np.linspace(0.0, 0.10, n)
ax.imshow(rgba, extent=[mat_L + cr, mat_R - cr, dark_b, grn_t],
          aspect="auto", zorder=2.5, interpolation="bicubic")

# ── sunlight ─────────────────────────────────────────────────────────
sy_top = grn_t + 1.0
sy_bot = grn_t + 0.05
for sx in [5.8, 7.0, 8.2]:
    ax.annotate("", xy=(sx, sy_bot), xytext=(sx, sy_top),
                arrowprops=dict(arrowstyle="-|>", color=SUN_CLR,
                                lw=2.5, mutation_scale=18), zorder=4)
for st, sb in [(5.0, 5.2), (9.0, 8.8)]:
    ax.annotate("", xy=(sb, sy_bot + 0.05), xytext=(st, sy_top - 0.1),
                arrowprops=dict(arrowstyle="-|>", color=SUN_CLR,
                                lw=1.5, mutation_scale=14, alpha=0.4), zorder=4)
ax.text(7.0, sy_top + 0.2, "sunlight", ha="center", va="bottom",
        fontsize=13, fontstyle="italic", color=SUN_CLR, fontfamily="sans-serif")

# ── layer labels ─────────────────────────────────────────────────────
def label(ymid, title, sub, tc, sc):
    ax.text(mat_cx, ymid + 0.32, title, ha="center", va="center",
            fontsize=15, fontweight="bold", color=tc,
            fontfamily="sans-serif", zorder=6)
    ax.text(mat_cx, ymid - 0.28, sub, ha="center", va="center",
            fontsize=11, fontstyle="italic", color=sc,
            fontfamily="sans-serif", zorder=6)

label(grn_b  + lh/2, "Green canopy",
      "anoxygenic phototrophs (720\u2013750 nm)", GREEN_EDGE, GREEN_TXT)
label(pink_b + lh/2, "Pink middle",
      "purple bacteria (800\u2013900 nm)", PINK_EDGE, PINK_TXT)
label(dark_b + lh/2, "Dark basement",
      "fermenters \u00b7 sulfate reducers \u00b7 methanogens", DARK_TXT, DARK_TXT)

# ── chemistry boxes (left column) ─────────────────────────────────────
cbx = 1.9   # center x for chemistry boxes
leader_dot = dict(color=LIGHT_GREY, ms=3, zorder=3)
leader_line = dict(color=LIGHT_GREY, lw=0.8, ls=(0, (5, 4)), zorder=3)

# Green canopy
g_cy = grn_b + lh/2
box_g = dict(boxstyle="round,pad=0.4", fc=GREEN_FILL, ec=GREEN_EDGE,
             lw=1.0, alpha=0.9)
ax.text(cbx, g_cy,
        "CO\u2082 + 2H\u2082S \u2192 CH\u2082O + 2S\u2070 + H\u2082O",
        ha="center", va="center", fontsize=8.5, color=GREEN_TXT,
        fontfamily="sans-serif", fontweight="bold", bbox=box_g, zorder=5)
ax.plot([3.55, mat_L - 0.1], [g_cy, g_cy], **leader_line)
ax.plot(mat_L - 0.07, g_cy, "o", **leader_dot)

# Pink middle (same reaction, different wavelength)
p_cy = pink_b + lh/2
box_p = dict(boxstyle="round,pad=0.4", fc=PINK_FILL, ec=PINK_EDGE,
             lw=1.0, alpha=0.9)
ax.text(cbx, p_cy,
        "CO\u2082 + 2H\u2082S \u2192 CH\u2082O + 2S\u2070 + H\u2082O",
        ha="center", va="center", fontsize=8.5, color=PINK_TXT,
        fontfamily="sans-serif", fontweight="bold", bbox=box_p, zorder=5)
ax.plot([3.55, mat_L - 0.1], [p_cy, p_cy], **leader_line)
ax.plot(mat_L - 0.07, p_cy, "o", **leader_dot)

# Dark basement (three guilds, three reactions)
b_cy = dark_b + lh/2
box_d = dict(boxstyle="round,pad=0.4", fc="#EAE6E0", ec=DARK_EDGE,
             lw=1.0, alpha=0.9)
ax.text(cbx, b_cy,
        "CH\u2082O \u2192 H\u2082 + CO\u2082\n"
        "SO\u2084\u00b2\u207b + 4H\u2082 \u2192 H\u2082S\n"
        "CO\u2082 + 4H\u2082 \u2192 CH\u2084",
        ha="center", va="center", fontsize=8.5, color=DARK_TXT,
        fontfamily="sans-serif", fontweight="bold", bbox=box_d,
        linespacing=1.6, zorder=5)
ax.plot([3.25, mat_L - 0.1], [b_cy, b_cy], **leader_line)
ax.plot(mat_L - 0.07, b_cy, "o", **leader_dot)


# ── sulfur cycle (right — closed loop) ───────────────────────────────
ccx  = 11.8    # center of cycle
cw   = 0.8
y_lo = dark_b + 0.25
y_hi = grn_t  - 0.25

# H₂S rising (left arc)
ax.add_patch(FancyArrowPatch(
    (ccx - cw*0.12, y_lo), (ccx - cw*0.12, y_hi),
    connectionstyle="arc3,rad=-0.4",
    arrowstyle="-|>", mutation_scale=18,
    color=H2S_CLR, linewidth=2.5, zorder=4))

# SO₄²⁻ descending (right arc)
ax.add_patch(FancyArrowPatch(
    (ccx + cw*0.12, y_hi), (ccx + cw*0.12, y_lo),
    connectionstyle="arc3,rad=-0.4",
    arrowstyle="-|>", mutation_scale=18,
    color=SO4_CLR, linewidth=2.5, zorder=4))

# labels outside the loop
ax.text(ccx - cw - 0.5, (y_lo + y_hi)/2, "H\u2082S",
        ha="center", va="center", fontsize=13, fontweight="bold",
        color=H2S_CLR, fontfamily="sans-serif", zorder=5)
ax.text(ccx + cw + 0.5, (y_lo + y_hi)/2, "SO\u2084\u00b2\u207b",
        ha="center", va="center", fontsize=13, fontweight="bold",
        color=SO4_CLR, fontfamily="sans-serif", zorder=5)

# top/bottom annotations
ax.text(ccx, y_hi + 0.22, "oxidized", ha="center", va="bottom",
        fontsize=9, fontstyle="italic", color=GREY, fontfamily="sans-serif")
ax.text(ccx, y_lo - 0.22, "reduced", ha="center", va="top",
        fontsize=9, fontstyle="italic", color=GREY, fontfamily="sans-serif")

# cycle title
ax.text(ccx, y_hi + 0.7, "sulfur cycle", ha="center", va="bottom",
        fontsize=11, fontweight="bold", fontstyle="italic",
        color=GREY, fontfamily="sans-serif")

# ── organic C rain (subtle, inside mat) ──────────────────────────────
rain_kw = dict(arrowstyle="-|>", color=DARK_EDGE, lw=0.8,
               mutation_scale=7, alpha=0.15, ls="--")
for rx in [5.2, 6.2, 7.0, 7.8]:
    ax.annotate("", xy=(rx, dark_t + 0.05), xytext=(rx, pink_t - 0.05),
                arrowprops=rain_kw, zorder=2.8)

# ── save ─────────────────────────────────────────────────────────────
out = "/Users/igor/conductor/workspaces/the-book/accra-v3/sources/img/ch4_mat_cross_section"
fig.savefig(out + ".png", dpi=300, bbox_inches="tight", facecolor=BG, pad_inches=0.3)
fig.savefig(out + ".pdf", bbox_inches="tight", facecolor=BG, pad_inches=0.3)
plt.close()
print("Done")
