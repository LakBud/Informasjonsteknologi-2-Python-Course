import json
import matplotlib.pyplot as plt
import numpy as np

file_name = "data/5/wage_bracket.json"

x_values = []
men_wages = []
women_wages = []

with open(file_name, encoding="utf-8") as file:
    data = json.load(file)

# Get years sorted by their index 
years_dict = data["dataset"]["dimension"]["Tid"]["category"]["index"]
x_values = [year for year, idx in sorted(years_dict.items(), key=lambda x: x[1])]

# Get wages
wages = data["dataset"]["value"]
men_wages = wages[0:len(x_values)]
women_wages = wages[len(x_values):]


# Task 2 - line diagrams
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# # Men Graph
# ax1.plot(x_values, men_wages, color="blue", marker="o", label="Men")
# ax1.grid(True)
# ax1.set_title("Men Wages")
# ax1.set_xlabel("Year")
# ax1.set_ylabel("Monthly Wage (kr)")
# ax1.legend()

# # Women Graph
# ax2.plot(x_values, women_wages, color="red", marker="o", label="Women")
# ax2.grid(True)
# ax2.set_title("Women Wages")
# ax2.set_xlabel("Year")
# ax2.set_ylabel("Monthly Wage (kr)")
# ax2.legend()


# Task 3 - bar diagrams
fig2, ax3 = plt.subplots(figsize=(10, 5))

x_pos = np.arange(len(x_values))  # positions for groups
width = 0.35  # width of each bar

ax3.bar(x_pos - width/2, men_wages, width, color='blue', label='Men')
ax3.bar(x_pos + width/2, women_wages, width, color='red', label='Women')

ax3.set_xticks(x_pos)
ax3.set_xticklabels(x_values)
ax3.set_xlabel('Year')
ax3.set_ylabel('Monthly Wage (kr)')
ax3.set_title('Monthly Wages by Gender')
ax3.legend()
ax3.grid(True, axis='y')

# Show
plt.tight_layout()
plt.show()
