import json

with open("data/5/activities.json", encoding="utf-8") as file:
    data_file = json.load(file)


# A
# a = "Activities"
# b = "Gender"
# c = "Time"


# print()
# print(f"{a:^50} | {b:^50} | {c:^50}")
# print("-" * 160)

# for data in data_file:
#     activities = data["alle aktiviteter"]
#     gender = data["kjønn"]
#     time = data["Tidsbruk 2000 I alt"]
    
    
#     print(f"{activities:^50} | {gender:^50} | {time:^50}")


# for data in data_file:
#     activities = data["alle aktiviteter"]
#     gender = data["kjønn"]
#     time = data["Tidsbruk 2000 I alt"]
    
    
#     print(f"{activities:^50} | {gender:^50} | {time:^50}")

# B)
# gender_selection = int(input("Which gender do you want (1. all, 2. women, 3. men): "))

# a = "Activities"
# b = "Gender"
# c = "Time"


# print()
# print(f"{a:^50} | {b:^50} | {c:^50}")
# print("-" * 160)


# for data in data_file:
#     activities = data["alle aktiviteter"]
#     gender = data["kjønn"]
#     time = data["Tidsbruk 2000 I alt"]
        
    
#     if gender_selection == 1:
#         print(f"{activities:^50} | {gender:^50} | {time:^50}")

#     elif gender_selection == 2 and gender == "Kvinner":
#         print(f"{activities:^50} | {gender:^50} | {time:^50}")

#     elif gender_selection == 3 and gender == "Menn":
#         print(f"{activities:^50} | {gender:^50} | {time:^50}")

# c
import matplotlib.pyplot as plt

gender_selection = int(input("Which gender do you want (1. all, 2. women, 3. men): "))

if gender_selection == 1:
    selected_gender = "Alle"
elif gender_selection == 2:
    selected_gender = "Kvinner"
elif gender_selection == 3:
    selected_gender = "Menn"

activities = []
times = []

for item in data_file:
    if item["kjønn"] == selected_gender and item["alle aktiviteter"] != "I alt":
        activities.append(item["alle aktiviteter"])
        times.append(item["Tidsbruk 2000 I alt"])

plt.figure(figsize=(12,6))
plt.bar(activities, times)

plt.title(f"Tidsbruk per aktivitet ({selected_gender})")
plt.xlabel("Aktivitet")
plt.ylabel("Timer")
plt.xticks(rotation=45, ha="right")


plt.figure(figsize=(7,7))
plt.pie(times, labels=activities, autopct="%1.1f%%", startangle=90)
plt.axis("equal")

plt.tight_layout()
plt.show()