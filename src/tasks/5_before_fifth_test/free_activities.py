import csv

# activities = []

# with open("data/5/friluftsaktiviteter.csv", encoding="utf-8") as file:
#     file_data = csv.reader(file, delimiter=";")

#     headers = next(file_data)

#     for row in file_data:
#         activity = row[0]
#         values = row[1:]
        
#         total = 0
#         for v in values:
#             total += int(v)
        
#         activities.append((activity, total))

# print()
# print(f"{'Aktivitet':60} | Totalt")
# print("-" * 70)

# for activity, total in activities:
#     print(f"{activity:60} | {total}")

with open("data/5/friluftsaktiviteter.csv", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")
    
    headers = next(reader)
    regions = headers[1:]
    
    data = []
    
    for row in reader:
        activity = row[0]
        values = list(map(int, row[1:]))
        
        data.append((activity, values))


for i, r in enumerate(regions):
    print(f"{i}: {r}")

choice = int(input("\nSkriv inn nummer: "))
selected_region = regions[choice]

index = choice

results = []
total_sum = 0

for activity, values in data:
    value = values[index]
    total_sum += value
    results.append((activity, value))

results.sort(key = lambda x: x[1])


print(f"\nResultat for {selected_region}\n")
print(f"{'Aktivitet':60} | Antall | Prosent")
print("-" * 85)

for activity, value in results:
    percent = (value / total_sum) * 100
    print(f"{activity:60} | {value:6} | {percent:6.2f}%")