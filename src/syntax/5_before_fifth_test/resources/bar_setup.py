import matplotlib.pyplot as plt

# Lists for data
categories = []
values = []

# Open CSV file
with open('data.csv', 'r', encoding="latin-1") as file:
    next(file)  # skip header (remove if not needed)

    for line in file:
        parts = line.strip().split(',')

        # Assuming: column 1 = category, column 2 = value
        categories.append(parts[0])
        values.append(float(parts[1]))

# Create figure and axes
fig, ax = plt.subplots(figsize=(8, 5))

# Create bar chart
ax.bar(categories, values)

# Labels and title
ax.set_title('Bar Chart from CSV Data')
ax.set_xlabel('Categories')
ax.set_ylabel('Values')

# Rotate labels if they overlap (important for IT-2 clarity)
plt.xticks(rotation=45)

# Grid (y-axis only for readability)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Layout fix
fig.tight_layout()

# Show plot
plt.show()