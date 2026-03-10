import matplotlib.pyplot as plt

total_x_values = 10
x_value = [x for x in range(1,total_x_values+1)]

# 5 colors
color = ["r","g","b","k","c"]

total_functions = 5
for m in range (1,total_functions+1):
    plt.plot(x_value,[m*x for x in x_value], color[m-1], label=f"f(x)={m}x")

# Forces the graph to have all x values
plt.xticks(x_value)

# Show info which is with the label param in the plot function 
plt.legend()

plt.show()