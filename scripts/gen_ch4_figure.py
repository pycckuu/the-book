"""
Generate Ch4 mat cross-section figure — book-quality version.
"""

from pathlib import Path

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
S0_CLR     = "#C08A52"   # elemental sulfur — sand/gold (palette family)
SUN_CLR    = "#E8B84B"
GREY       = "#555555"
GREY_TITLE = "#333333"
LIGHT_GREY = "#AAAAAA"

# ── canvas (wider for breathing room) ────────────────────────────────
W, H = 14, 8
fig, ax = plt.subplots(figsize=(W, H), dpi=300)
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, W); ax.set_ylim(0, H)
ax.set_aspect("equal"); ax.axis("off")

# ── bold grey suptitle (shared theme) ────────────────────────────────
fig.suptitle("Cross-section of an Archean bacterial mat",
             fontsize=16, fontweight="bold", color=GREY_TITLE, y=0.97)

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
      "anoxygenic phototrophs (720–750 nm)", GREEN_EDGE, GREEN_TXT)
label(pink_b + lh/2, "Pink middle",
      "purple bacteria (800–900 nm)", PINK_EDGE, PINK_TXT)
label(dark_b + lh/2, "Dark basement",
      "fermenters · sulfate reducers · methanogens", DARK_TXT, DARK_TXT)

# ── mathtext chemical strings ────────────────────────────────────────
EQ_PHOTO = r"CO$_2$ + 2H$_2$S $\rightarrow$ CH$_2$O + 2S$^0$ + H$_2$O"
EQ_FERM  = r"CH$_2$O + H$_2$O $\rightarrow$ 2H$_2$ + CO$_2$"
EQ_SRB   = r"SO$_4^{2-}$ + 4H$_2$ + 2H$^+$ $\rightarrow$ H$_2$S + 4H$_2$O"
EQ_METH  = r"CO$_2$ + 4H$_2$ $\rightarrow$ CH$_4$ + 2H$_2$O"

# ── chemistry boxes (left column) ─────────────────────────────────────
cbx = 1.9   # center x for chemistry boxes
leader_dot = dict(color=LIGHT_GREY, ms=3, zorder=3)
leader_line = dict(color=LIGHT_GREY, lw=0.8, ls=(0, (5, 4)), zorder=3)

# Green canopy
g_cy = grn_b + lh/2
box_g = dict(boxstyle="round,pad=0.4", fc=GREEN_FILL, ec=GREEN_EDGE,
             lw=1.0, alpha=0.9)
ax.text(cbx, g_cy, EQ_PHOTO,
        ha="center", va="center", fontsize=8.5, color=GREEN_TXT,
        fontfamily="sans-serif", fontweight="bold", bbox=box_g, zorder=5)
ax.plot([3.55, mat_L - 0.1], [g_cy, g_cy], **leader_line)
ax.plot(mat_L - 0.07, g_cy, "o", **leader_dot)

# Pink middle (same reaction, different wavelength)
p_cy = pink_b + lh/2
box_p = dict(boxstyle="round,pad=0.4", fc=PINK_FILL, ec=PINK_EDGE,
             lw=1.0, alpha=0.9)
ax.text(cbx, p_cy, EQ_PHOTO,
        ha="center", va="center", fontsize=8.5, color=PINK_TXT,
        fontfamily="sans-serif", fontweight="bold", bbox=box_p, zorder=5)
ax.plot([3.55, mat_L - 0.1], [p_cy, p_cy], **leader_line)
ax.plot(mat_L - 0.07, p_cy, "o", **leader_dot)

# Cue: canopy and middle run the SAME reaction, just at different light.
# A small bracket links the two identical equation boxes.
brk_x = cbx - 1.62
ax.annotate("", xy=(brk_x, p_cy + 0.05), xytext=(brk_x, g_cy - 0.05),
            arrowprops=dict(arrowstyle="-", color=LIGHT_GREY, lw=1.1,
                            connectionstyle="arc3,rad=-0.30"), zorder=3)
ax.text(brk_x - 0.22, (g_cy + p_cy)/2, "same\nreaction,\ndifferent\nlight",
        ha="right", va="center", fontsize=7.2, fontstyle="italic",
        color=GREY, fontfamily="sans-serif", linespacing=1.25, zorder=5)

# Dark basement (three guilds, three balanced reactions)
b_cy = dark_b + lh/2
box_d = dict(boxstyle="round,pad=0.4", fc="#EAE6E0", ec=DARK_EDGE,
             lw=1.0, alpha=0.9)
ax.text(cbx, b_cy,
        EQ_FERM + "\n" + EQ_SRB + "\n" + EQ_METH,
        ha="center", va="center", fontsize=7.4, color=DARK_TXT,
        fontfamily="sans-serif", fontweight="bold", bbox=box_d,
        linespacing=1.7, zorder=5)
ax.plot([3.25, mat_L - 0.1], [b_cy, b_cy], **leader_line)
ax.plot(mat_L - 0.07, b_cy, "o", **leader_dot)


# ── sulfur cycle (right — closed loop with S0 intermediate) ──────────
# Oxidative (upward) path:  H2S -> S0 -> SO4   (left side)
# Reductive (downward) path: SO4 -> H2S        (right side)
ccx  = 11.8                 # center of cycle
y_lo = dark_b + 0.30        # reduced  (H2S)  — bottom node
y_hi = grn_t  - 0.30        # oxidized (SO4)  — top node
y_mid = (y_lo + y_hi) / 2   # intermediate (S0) on the oxidative path
x_left  = ccx - 0.14
x_right = ccx + 0.14

# oxidative path, segment 1: H2S -> S0 (lower-left arc)
ax.add_patch(FancyArrowPatch(
    (x_left, y_lo), (x_left, y_mid),
    connectionstyle="arc3,rad=-0.40",
    arrowstyle="-|>", mutation_scale=16,
    color=H2S_CLR, linewidth=2.5, zorder=4))
# oxidative path, segment 2: S0 -> SO4 (upper-left arc)
ax.add_patch(FancyArrowPatch(
    (x_left, y_mid), (x_left, y_hi),
    connectionstyle="arc3,rad=-0.40",
    arrowstyle="-|>", mutation_scale=16,
    color=S0_CLR, linewidth=2.5, zorder=4))
# reductive path: SO4 -> H2S (right arc)
ax.add_patch(FancyArrowPatch(
    (x_right, y_hi), (x_right, y_lo),
    connectionstyle="arc3,rad=-0.40",
    arrowstyle="-|>", mutation_scale=16,
    color=SO4_CLR, linewidth=2.5, zorder=4))

# node labels (mathtext)
ax.text(ccx, y_lo - 0.14, r"H$_2$S",
        ha="center", va="top", fontsize=13, fontweight="bold",
        color=H2S_CLR, fontfamily="sans-serif", zorder=5)
ax.text(ccx, y_hi + 0.14, r"SO$_4^{2-}$",
        ha="center", va="bottom", fontsize=13, fontweight="bold",
        color=SO4_CLR, fontfamily="sans-serif", zorder=5)
# S0 intermediate — marker sits exactly at the arc junction where the
# H2S->S0 (orange) and S0->SO4 (gold) segments meet; label just to its left.
ax.plot(x_left, y_mid, "o", ms=7,
        markerfacecolor=S0_CLR, markeredgecolor="white",
        markeredgewidth=1.1, zorder=6)
ax.text(x_left - 0.30, y_mid, r"S$^0$",
        ha="right", va="center", fontsize=13, fontweight="bold",
        color=S0_CLR, fontfamily="sans-serif", zorder=6)

# path-role annotations (italic, alongside the arcs)
ax.text(ccx - 1.05, (y_lo + y_mid)/2 - 0.05, "oxidative",
        ha="center", va="center", fontsize=8, fontstyle="italic",
        color=GREY, fontfamily="sans-serif", rotation=90, zorder=5)
ax.text(ccx + 1.30, (y_lo + y_hi)/2, "reductive",
        ha="center", va="center", fontsize=8, fontstyle="italic",
        color=GREY, fontfamily="sans-serif", rotation=-90, zorder=5)

# cycle title
ax.text(ccx, y_hi + 0.82, "sulfur cycle", ha="center", va="bottom",
        fontsize=11, fontweight="bold", fontstyle="italic",
        color=GREY, fontfamily="sans-serif")

# ── organic C rain (subtle — runs canopy -> basement) ────────────────
rain_kw = dict(arrowstyle="-|>", color=DARK_EDGE, lw=0.9,
               mutation_scale=8, alpha=0.32, ls=(0, (3, 3)))
for rx in [5.2, 6.2, 7.0, 7.8]:
    ax.annotate("", xy=(rx, dark_b + 0.18), xytext=(rx, grn_t - 0.10),
                arrowprops=rain_kw, zorder=2.8)
ax.text(8.55, dark_t + lh*0.55, "organic C", ha="left", va="center",
        fontsize=7.5, fontstyle="italic", color=DARK_EDGE, alpha=0.7,
        rotation=90, fontfamily="sans-serif", zorder=2.8)

# ── save (portable: repo root / sources / img) ───────────────────────
out_dir = Path(__file__).resolve().parent.parent / "sources" / "img"
out_dir.mkdir(parents=True, exist_ok=True)
out = str(out_dir / "ch4_mat_cross_section")
fig.savefig(out + ".png", dpi=300, bbox_inches="tight", facecolor=BG, pad_inches=0.3)
fig.savefig(out + ".pdf", bbox_inches="tight", facecolor=BG, pad_inches=0.3)
plt.close()
print(f"Done -> {out}.png / .pdf")
