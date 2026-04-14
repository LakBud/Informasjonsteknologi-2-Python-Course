import csv
import matplotlib.pyplot as plt

file_path = "data/5/friluftsaktiviteter.csv"

with open(file_path, encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")

    headers = next(reader)
    regions = headers[1:]

    data = []

    for row in reader:
        activity = row[0]
        values = list(map(int, row[1:]))
        data.append((activity, values))


# -----------------------------
# Velg fylke
# -----------------------------
print("Velg fylke:")
for i, r in enumerate(regions):
    print(f"{i}: {r}")

choice = int(input("\nSkriv inn nummer: "))
selected_region = regions[choice]


# -----------------------------
# Hent verdier for valgt fylke
# -----------------------------
results = []

for activity, values in data:
    results.append((activity, values[choice]))


# -----------------------------
# Finn topp 3
# -----------------------------
top3 = sorted(results, key=lambda x: x[1], reverse=True)[:3]


# -----------------------------
# Print topp 3
# -----------------------------
print(f"\nTopp 3 aktiviteter i {selected_region}:\n")

for activity, value in top3:
    print(f"{activity}: {value}")


# -----------------------------
# Stolpediagram
# -----------------------------
activities = [x[0] for x in top3]
values = [x[1] for x in top3]

plt.figure(figsize=(8, 5))
plt.bar(activities, values)

plt.title(f"Topp 3 friluftsaktiviteter i {selected_region}")
plt.ylabel("Antall personer (i 1000)")
plt.xticks(rotation=20, ha="right")

plt.tight_layout()
plt.show()