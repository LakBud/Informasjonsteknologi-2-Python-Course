import matplotlib.pyplot as plt
import numpy as np

# Data
YEARS = [2005,2009,2013,2017,2021]

# Political parties
AP = [61,64,55,49,48]
HOYRE = [23,30,48,45,26]
FRP = [15,10,12,20,18]

total_datapoints = len(YEARS)
x_values = np.arange(total_datapoints)

x_width = 0.2
x_offset = x_width / 2

fig, axes = plt.subplots()


bars_AP = axes.bar(x_values-(x_offset*2), AP, width=x_width, color="red", label="AP")
bars_HOYRE = axes.bar(x_values + (x_offset*2), HOYRE, width=x_width, color="blue", label="Høyre")
bars_FRP = axes.bar(x_values, FRP, width=x_width, color="yellow", label="FRP")

#viser du ulike fargene i en boks øverst til høyre
plt.legend()

# Set x-ticks
axes.set_xticks(x_values)
axes.set_xticklabels(YEARS)

plt.title("Representanter i Stortinget")
plt.grid(axis="y")
plt.ylabel("Representanter")
plt.xlabel("År")

# --- Annotate all bars ---
def annotate_bars(bars):
    for bar in bars:
        height = bar.get_height()
        axes.annotate(
            f'{height}',                # Text is the height
            xy=(bar.get_x() + bar.get_width() / 2, height),  # At top center of the bar
            xytext=(0, 3),             # 3 points vertical offset
            textcoords="offset points",
            ha='center',               # Center horizontally
            va='bottom'                # Vertical alignment at the bottom of text
        )

annotate_bars(bars_AP)
annotate_bars(bars_HOYRE)
annotate_bars(bars_FRP)

# -----------------------------------------------------
# Saving the figure
# -----------------------------------------------------
# savefig() saves the current figure as an image file.
# dpi controls the resolution (300 dpi is good quality).

plt.savefig("my_figure.png", dpi=300)

# Show the figure on screen
plt.show()