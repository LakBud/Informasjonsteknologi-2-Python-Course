import matplotlib.pyplot as plt

year = []
men = []
women = []
total = []

with open("data/5/uni_data.csv", encoding="latin-1") as file:
    for line in file:
        row = line.strip().split(",")
        
        a = int(row[0])
        m = int(row[2])
        w = int(row[3])
        
        year.append(a)
        men.append(m)
        women.append(w)
        
        total.append(m + w)

fig, ax = plt.subplots(figsize=(8, 5))


# b
minimum = min(total)
minimum_index = total.index(minimum)
print(f"In the year {2000 + minimum_index} was the lowest amount of students total with only {minimum} students")

# c
maximum = max(total)
maximum_index = total.index(maximum)
print(f"In the year {2000 + maximum_index} was the highest amount of students total with {maximum} students")

# d
tot_men = sum(men)
tot_women = sum(women)
total = tot_men + tot_women

andel_menn = tot_men / total * 100
andel_women = tot_women / total * 100

print(f"Andel menn: {andel_menn:.2f}%")
print(f"Andel women: {andel_women:.2f}%")

# e
tot_men_5 = sum(men[:5])
tot_women_5 = sum(women[:5])
total_5 = tot_men_5 + tot_women_5

andel_menn_5 = tot_men_5 / total_5 * 100
andel_women_5 = tot_women_5 / total_5 * 100

print(f"Andel menn in the first 5 years: {andel_menn_5:.2f}%")
print(f"Andel women in the first 5 years: {andel_women_5:.2f}%")


# f
last_tot_men_5 = sum(men[-5:])
last_tot_women_5 = sum(women[-5:])
last_total_5 = last_tot_men_5 + last_tot_women_5

last_andel_menn_5 = last_tot_men_5 / last_total_5 * 100
last_andel_women_5 = last_tot_women_5 / last_total_5 * 100

print(f"Andel menn in the last 5 years: {last_andel_menn_5:.2f}%")
print(f"Andel women in the last 5 years: {last_andel_women_5:.2f}%")

# ----

# Graph
ax.plot(year, men, label="Men", marker='o', linestyle='-', color='green')
ax.plot(year, women, label="Women", marker='o', linestyle='-', color='orange')

ax.set_xlabel("year")
ax.set_ylabel("Total Students")
plt.title("Total Students based on gender")
ax.legend()
ax.grid(True)

# Layout
plt.tight_layout()

plt.show()