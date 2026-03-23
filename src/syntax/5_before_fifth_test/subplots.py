# Demonstrates how to create multiple graphs in the same figure using matplotlib

import matplotlib.pyplot as plt
import numpy as np


# -----------------------------
# Define functions to plot
# -----------------------------
def f(x):
    """Square root function"""
    return np.sqrt(x)


def g(x):
    """Quadratic function"""
    return x**2


# Generate x values
# np.linspace(start, stop, number_of_points)
x_values = np.linspace(0, 25, 251)


# =====================================================
# METHOD 1: Using plt.subplot(rows, columns, index)
# =====================================================
# This method divides the figure into a grid and selects
# the subplot using its index.

# ---- Graph 1 ----
y_values = f(x_values)

plt.subplot(1, 2, 1)  # 1 row, 2 columns, position 1
plt.plot(x_values, y_values, color="blue")
plt.grid()
plt.title("Function $f(x)=\\sqrt{x}$")
plt.xlim(0, 25)
plt.ylim(0, 5)

# ---- Graph 2 ----
y_values = g(x_values)

plt.subplot(1, 2, 2)  # 1 row, 2 columns, position 2
plt.plot(x_values, y_values, color="blue")
plt.grid()
plt.title("Function $g(x)=x^2$")
plt.xlim(0, 5)
plt.ylim(0, 25)

plt.show()


# =====================================================
# METHOD 2: Using plt.subplots()
# =====================================================
# This is the recommended and more modern approach.
# It creates the figure and axes objects at the same time.

fig, (ax1, ax2) = plt.subplots(1, 2)

# ---- Graph 1 ----
y_values = f(x_values)

ax1.plot(x_values, y_values, color="blue")
ax1.grid()
ax1.set_title("Function $f(x)=\\sqrt{x}$")
ax1.set_xlim(0, 25)
ax1.set_ylim(0, 5)

# ---- Graph 2 ----
y_values = g(x_values)

ax2.plot(x_values, y_values, color="blue")
ax2.grid()
ax2.set_title("Function $g(x)=x^2$")
ax2.set_xlim(0, 5)
ax2.set_ylim(0, 25)


# -----------------------------------------------------
# Saving the figure
# -----------------------------------------------------
# savefig() saves the current figure as an image file.
# dpi controls the resolution (300 dpi is good quality).

plt.savefig("images/5/my_figure.png", dpi=300)

# Show the figure on screen
plt.show()