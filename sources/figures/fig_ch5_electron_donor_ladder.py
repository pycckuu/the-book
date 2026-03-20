from pathlib import Path

import matplotlib.pyplot as plt
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

donors = [
    {
        "name": r"H$_2$",
        "electrons": r"2 e$^-$",
        "y": -0.42,
        "fc": green_bg,
        "ec": green,
        "tc": green,
    },
    {
        "name": r"H$_2$S",
        "electrons": r"8 e$^-$",
        "y": -0.27,
        "fc": sand_bg,
        "ec": sand,
        "tc": sand,
    },
    {
        "name": r"Fe$^{2+}$",
        "electrons": r"1 e$^-$",
        "y": 0.20,
        "fc": blue_bg,
        "ec": blue,
        "tc": blue,
    },
    {
        "name": r"NO$_2^-$",
        "electrons": r"2 e$^-$",
        "y": 0.43,
        "fc": violet_bg,
        "ec": violet,
        "tc": violet,
    },
    {
        "name": r"H$_2$O",
        "electrons": r"4 e$^-$",
        "y": 0.82,
        "fc": red_bg,
        "ec": red,
        "tc": red,
    },
]

fig, ax = plt.subplots(figsize=(11.4, 7.7), dpi=300)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

ax.set_xlim(0, 11.6)
ax.set_ylim(0.96, -0.56)
ax.set_xticks([])
ax.set_yticks([-0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8])
ax.tick_params(axis="y", labelsize=9.5, colors="#666666", length=0)
ax.set_ylabel(
    r"standard reduction potential $E_0^\prime$ (V)",
    fontsize=11,
    color=grey,
)

for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

ax.spines["left"].set_color(light_grey)
ax.spines["left"].set_linewidth(1.2)

fig.suptitle(
    "The electron donor ladder",
    fontsize=14,
    fontweight="bold",
    y=0.97,
    color=grey,
)

ladder_x = 2.75
box_x = 4.10
box_width = 3.55
box_height = 0.082
pill_width = 0.92
pill_height = 0.054

ax.plot(
    [ladder_x, ladder_x],
    [-0.42, 0.82],
    color=light_grey,
    linewidth=6.2,
    solid_capstyle="round",
    zorder=1,
)
ax.plot(
    [ladder_x, ladder_x],
    [-0.42, 0.82],
    color="#F8F8F8",
    linewidth=2.4,
    solid_capstyle="round",
    zorder=2,
)

ax.text(
    0.92,
    -0.46,
    "easier\nto oxidize",
    ha="left",
    va="top",
    fontsize=10,
    color=green,
    style="italic",
    linespacing=1.2,
)
ax.text(
    0.92,
    0.86,
    "harder\nto oxidize",
    ha="left",
    va="top",
    fontsize=10,
    color=red,
    style="italic",
    linespacing=1.2,
)

for donor in donors:
    y = float(donor["y"])

    ax.plot(
        [ladder_x - 0.30, ladder_x + 0.30],
        [y, y],
        color=mid_grey,
        linewidth=1.6,
        solid_capstyle="round",
        zorder=3,
    )
    ax.plot(
        [ladder_x + 0.30, box_x - 0.18],
        [y, y],
        color="#A7A7A7",
        linewidth=0.95,
        linestyle=(0, (3, 4)),
        zorder=2,
    )

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
        fontsize=14,
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

barrier_y = 0.62
ax.plot(
    [3.15, 8.65],
    [barrier_y, barrier_y],
    color=red,
    linewidth=1.8,
    linestyle=(0, (6, 4)),
    zorder=2,
)
ax.text(
    8.92,
    0.59,
    "water barrier",
    ha="left",
    va="bottom",
    fontsize=12,
    fontweight="bold",
    color=red,
    zorder=5,
)
ax.text(
    8.92,
    0.69,
    "two linked photosystems\nrequired",
    ha="left",
    va="top",
    fontsize=9.5,
    color=red,
    style="italic",
    linespacing=1.22,
    zorder=5,
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
