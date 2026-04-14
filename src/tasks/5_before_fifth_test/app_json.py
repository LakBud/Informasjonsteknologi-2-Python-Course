import json

with open("data/5/googleplaystore.json", encoding="utf-8") as file:
    data = json.load(file)

category_count = {}

apps_with_installs = []

# tell alle kategorier
for app in data:
    category = app["Category"]
    installs_str = app["Installs"].replace(",", "").replace("+", "")
    
    if installs_str.isdigit():
        installs = int(installs_str)
        
        apps_with_installs.append((app["App"], installs))
    
    if category in category_count:
        category_count[category] += 1
    else:
        category_count[category] = 1

# sorter etter antall (synkende)
sorted_categories = sorted(category_count.items(), key=lambda x: x[1], reverse=True)

sorted_apps = sorted(apps_with_installs, key=lambda x: x[1], reverse=True)

# print topp 3
for category, count in sorted_categories[:3]:
    print(category, count)

for name, installs in sorted_apps[:3]:
    print(name, installs)