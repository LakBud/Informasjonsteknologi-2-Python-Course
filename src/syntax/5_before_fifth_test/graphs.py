# Import matplotlib for plotting graphs
import matplotlib.pyplot as plt

# Import NumPy for efficient numerical calculations and arrays
import numpy as np


# -----------------------------
# 1. Define the function
# -----------------------------
# This function will be plotted on the graph
def f(x):
    return np.sqrt(x)


# -----------------------------
# 2. Generate x and y values
# -----------------------------
# A graph needs x-values (input) and y-values (output)

# Recommended method:
# np.linspace(start, stop, number_of_points)
# This creates evenly spaced values between start and stop
x_values = np.linspace(0, 25, 25)

# Apply the function to all x-values to compute y-values
y_values = f(x_values)


# Alternative (less efficient) method using a loop:
# x_values = []
# y_values = []
#
# for x in range(1, 26):
#     x_values.append(x)
#     y_values.append(f(x))


# -----------------------------
# 3. Create the figure and axes
# -----------------------------
# fig = the full figure
# ax = the axes (the coordinate system where the graph is drawn)
fig, ax = plt.subplots()


# -----------------------------
# 4. Configure the graph
# -----------------------------
# Enable grid lines
plt.grid()

# Title of the graph (LaTeX formatting is supported with $...$)
plt.title("Function: $f(x) = \\sqrt{x}$")

# Axis labels
plt.xlabel("$x$")
plt.ylabel("$y$")

# Set visible range of the axes
plt.xlim(-10, 25)
plt.ylim(-10, 25)

# Draw x-axis and y-axis lines
plt.axhline(y=0, color="black")
plt.axvline(x=0, color="black")


# -----------------------------
# 5. Plot the data
# -----------------------------
# Plot a continuous line through the points
plt.plot(x_values, y_values)

# Plot the individual points as dots
plt.scatter(x_values, y_values)


# -----------------------------
# 6. Display the graph
# -----------------------------
# This opens the graph window
plt.show()