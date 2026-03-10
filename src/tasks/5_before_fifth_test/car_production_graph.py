import matplotlib.pyplot as plt

x_values = [
    "China", "Japan", "Germany", "USA", "South Korea", "India", "Spain", "Mexico",
    "Brazil", "UK", "France", "Czech Rep.", "Russia", "Iran", "Slovakia", "Indonesia",
    "Turkey", "Thailand", "Canada", "Italy", "Poland", "Hungary", "Malaysia", "Romania",
    "Belgium", "South Africa", "Taiwan", "Argentina", "Sweden", "Australia", "Slovenia",
    "Portugal", "Austria", "Uzbekistan", "Serbia", "Finland", "Netherlands", "Egypt",
    "Ukraine", "Others"
]

y_values = [
    24420744, 7873886, 5746808, 3934357, 3859991, 3677605, 2354117, 1993168,
    1778464, 1722698, 1626000, 1344182, 1124774, 1074000, 1040000, 968101,
    950888, 805033, 802057, 713182, 554600, 472000, 469720, 358861,
    354003, 335539, 251096, 241315, 205374, 149000, 133702,
    99200, 90000, 88152, 79360, 55280, 42150, 10930,
    4340, 781708
]

data = dict(zip(x_values, y_values))

sorted_data = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))


countries = list(sorted_data.keys())
values = list(sorted_data.values())

plt.figure(figsize=(12,8))
plt.barh(countries, values, color='skyblue')
plt.xlabel("Cars")
plt.title("Top Countries by Car Production")
plt.xscale('log')


plt.tight_layout()
plt.show()