import csv
import matplotlib.pyplot as plt

file_name = "data/5/population.csv"

x_values = []
y_values = []

with open(file_name, encoding="utf-8") as file:
    # A function which strips spaces and splits the values based on the delimiter -> returns a list
    file_data = csv.reader(file, delimiter=";")
    
    # Since file_data is an iterable, we can use next() to target the headers
    # next() jumps the current line
    headers = next(file_data)
    
    for line in file_data:
        x_values.append(int(line[0]))
        y_values.append(int(line[1]))


# Figure
fig, ax = plt.subplots(figsize=(8, 5))

# Plot
ax.plot(x_values, y_values, marker='o', linestyle='-', color='green', label='Data')

# Style
ax.set_title("Population over Years")
ax.set_xlabel("Years")
ax.set_ylabel("Population")
ax.grid(True)
ax.legend()

# Layout
plt.tight_layout()

# Show
plt.savefig("images/5/population_graph.png", dpi=300)
plt.show()

