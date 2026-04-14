import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# Read data from CSV (NO PANDAS)
# -----------------------------
years = []
AP = []
HOYRE = []
FRP = []

with open("data.csv", "r") as file:
    next(file)  # skip header

    for line in file:
        parts = line.strip().split(",")

        years.append(int(parts[0]))
        AP.append(int(parts[1]))
        HOYRE.append(int(parts[2]))
        FRP.append(int(parts[3]))

# -----------------------------
# Setup x-axis positions
# -----------------------------
total_datapoints = len(years)
x_values = np.arange(total_datapoints)

x_width = 0.25
x_offset = x_width

# -----------------------------
# Create figure and axes
# -----------------------------
fig, axes = plt.subplots(figsize=(10, 6))

# -----------------------------
# Bars (grouped)
# -----------------------------
bars_AP = axes.bar(
    x_values - x_offset,
    AP,
    width=x_width,
    color="red",
    edgecolor="black",
    alpha=0.85,
    label="AP"
)

bars_HOYRE = axes.bar(
    x_values,
    HOYRE,
    width=x_width,
    color="blue",
    edgecolor="black",
    alpha=0.85,
    label="Høyre"
)

bars_FRP = axes.bar(
    x_values + x_offset,
    FRP,
    width=x_width,
    color="yellow",
    edgecolor="black",
    alpha=0.85,
    label="FRP"
)

# -----------------------------
# Axis formatting
# -----------------------------
axes.set_xticks(x_values)
axes.set_xticklabels(years)

axes.set_title("Representanter i Stortinget")
axes.set_xlabel("År")
axes.set_ylabel("Representanter")

axes.grid(axis="y", linestyle="--", alpha=0.5)
axes.legend()

# -----------------------------
# Annotate bars
# -----------------------------
def annotate_bars(bars):
    for bar in bars:
        height = bar.get_height()

        axes.annotate(
            f"{height}",
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 3),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=9
        )

annotate_bars(bars_AP)
annotate_bars(bars_HOYRE)
annotate_bars(bars_FRP)

# -----------------------------
# Layout
# -----------------------------
fig.tight_layout()

plt.show()