from pathlib import Path

import matplotlib.pyplot as plt

plt.rcParams["pdf.fonttype"] = 42
from matplotlib.patches import FancyBboxPatch


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

# Positions below are unscaled layout coordinates, not electrode potentials.
donors = [
    {
        "name": r"H$_2$ $\rightarrow$ 2 H$^+$",
        "electrons": r"2 e$^-$",
        "y": 0.10,
        "fc": green_bg,
        "ec": green,
        "tc": green,
    },
    {
        "name": r"H$_2$S $\rightarrow$ SO$_4^{2-}$",
        "electrons": r"8 e$^-$",
        "y": 0.30,
        "fc": sand_bg,
        "ec": sand,
        "tc": sand,
    },
    {
        "name": r"Fe(II) $\rightarrow$ Fe(III)",
        "electrons": r"1 e$^-$",
        "y": 0.50,
        "fc": blue_bg,
        "ec": blue,
        "tc": blue,
    },
    {
        "name": r"NO$_2^-$ $\rightarrow$ NO$_3^-$",
        "electrons": r"2 e$^-$",
        "y": 0.70,
        "fc": violet_bg,
        "ec": violet,
        "tc": violet,
    },
    {
        "name": r"2 H$_2$O $\rightarrow$ O$_2$",
        "electrons": r"4 e$^-$",
        "y": 0.90,
        "fc": red_bg,
        "ec": red,
        "tc": red,
    },
]

fig, ax = plt.subplots(figsize=(11.4, 7.7), dpi=300)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

ax.set_xlim(0, 11.6)
ax.set_ylim(1.04, -0.04)
ax.set_axis_off()

fig.suptitle(
    "Доноры электронов: выбранные конечные продукты окисления",
    fontsize=14,
    fontweight="bold",
    y=0.97,
    color=grey,
)

box_x = 4.10
box_width = 3.55
box_height = 0.082
pill_width = 0.92
pill_height = 0.054

for donor in donors:
    y = float(donor["y"])

    ax.add_patch(
        FancyBboxPatch(
            (box_x, y - box_height / 2),
            box_width,
            box_height,
            boxstyle="round,pad=0.02,rounding_size=0.06",
            facecolor=str(donor["fc"]),
            edgecolor=str(donor["ec"]),
            linewidth=1.8,
            zorder=4,
        )
    )

    pill_x = box_x + box_width - pill_width - 0.16
    ax.add_patch(
        FancyBboxPatch(
            (pill_x, y - pill_height / 2),
            pill_width,
            pill_height,
            boxstyle="round,pad=0.02,rounding_size=0.04",
            facecolor="white",
            edgecolor=str(donor["ec"]),
            linewidth=1.0,
            zorder=5,
        )
    )

    ax.text(
        box_x + 0.20,
        y,
        str(donor["name"]),
        ha="left",
        va="center",
        fontsize=11,
        fontweight="bold",
        color=str(donor["tc"]),
        zorder=6,
    )
    ax.text(
        pill_x + pill_width / 2,
        y,
        str(donor["electrons"]),
        ha="center",
        va="center",
        fontsize=9.5,
        fontweight="bold",
        color=str(donor["tc"]),
        zorder=6,
    )

ax.text(
    8.20,
    0.90,
    "Окисление воды в PSII;\nв кислородном потоке PSII\nи PSI работают последовательно",
    ha="left",
    va="center",
    fontsize=9.5,
    color=red,
    linespacing=1.22,
)

out_dir = Path(__file__).resolve().parents[1] / "img"
out_dir.mkdir(parents=True, exist_ok=True)
base = out_dir / "ch5_electron_donor_ladder"

plt.tight_layout(rect=(0.05, 0.05, 0.98, 0.95))
plt.savefig(
    base.with_suffix(".png"),
    dpi=300,
    bbox_inches="tight",
    facecolor="white",
)
plt.savefig(base.with_suffix(".pdf"), bbox_inches="tight", facecolor="white")
plt.close(fig)

print(f"Saved {base.with_suffix('.png')} and {base.with_suffix('.pdf')}")
