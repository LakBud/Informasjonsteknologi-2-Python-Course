import matplotlib.pyplot as plt

# Data
traffic_per_hour = {}

with open("data/5/traffic_data.csv", encoding="latin-1") as file:
    next(file) # Skip header
    
    for line in file:
        row = line.strip().split(";")
        
        if row[8].isdigit():
            time = row[7]
            traffic = int(row[9])
            
            if time in traffic_per_hour:
                traffic_per_hour[time] += traffic
            else:
                traffic_per_hour[time] = traffic
        

# Data for graph

times = sorted(traffic_per_hour.keys())

traffic_values = []
for t in times:
    traffic_values.append(traffic_per_hour[t])

# Graph setup
fig, axes = plt.subplots()
bars = axes.bar(times, traffic_values, label="Traffic")

# Annotate bars
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

# Graph styling
plt.xticks(rotation=50)
plt.title("Traffic per hour")
plt.ylabel("Number of cars")
plt.xlabel("Time")
plt.grid(axis="y")
plt.legend()
plt.tight_layout()

# Show
plt.savefig("images/5/traffic_bar_chart.png", dpi=300)
plt.show()