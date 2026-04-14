import matplotlib.pyplot as plt

# Lists to store data from CSV
x_values = []
y_values = []

# Open CSV file (no pandas)
with open('data.csv', 'r', encoding="latin-1") as file:
    next(file)  # skip header row (remove if no header)

    for line in file:
        # Remove whitespace and split by comma
        parts = line.strip().split(',')

        # Assuming first column = x, second column = y
        x_values.append(float(parts[0]))
        y_values.append(float(parts[1]))

# Create figure and axes
fig, ax = plt.subplots(figsize=(8, 5))

# Plot line graph
ax.plot(x_values, y_values)

# Labels and title
ax.set_title('Line Graph from CSV File')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.legend()

# Grid for clarity
ax.grid(True)

# Improve layout
fig.tight_layout()

# Show plot
plt.show()

