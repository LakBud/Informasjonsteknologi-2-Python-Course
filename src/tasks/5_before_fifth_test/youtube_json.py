import json

with open("data/5/Global YouTube Statistics.json", encoding="utf-8") as file:
    data = json.load(file)

country_count = {}

for item in data:
    country = item["Country"]
    
    if country in country_count:
        country_count[country] += 1
    else:
        country_count[country] = 1

sorted_country_count = dict(sorted(country_count.items(), key=lambda x: x[1], reverse=True))

max_count = 0
top_10 = []

print()

for key, value in sorted_country_count.items():
    if max_count < 10 and key != "nan":
        print(f"Country: {key:^15} | Total Youtubers: {value}")
        top_10.append(key)
        max_count += 1

print()

for country in top_10:
    total_subs = 0
    total_views = 0
    count = 0
    
    for item in data:
        if item["Country"] == country:
            total_subs += item["subscribers"]
            total_views += item["video views"]
            count += 1
    
    avg_subs = total_subs / count
    avg_views = total_views / count

    print(f"{country}:")
    print(f"  Avg subscribers: {round(avg_subs)}")
    print(f"  Avg views: {round(avg_views)}\n")