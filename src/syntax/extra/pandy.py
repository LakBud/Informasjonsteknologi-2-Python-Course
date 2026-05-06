import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/extra/electric_use.csv")

df["kostnad_kr"] = (df["forbruk_kWh"] * df["pris_ore_per_kWh"] / 100)
df["mnd_aar"] = df["maaned"] + " " + df["aar"].astype(str)

df.plot(x="mnd_aar", y="kostnad_kr", kind="line", figsize=(12, 5))

plt.title("Electric cost per month")
plt.xlabel("Year")
plt.ylabel("Cost")
plt.xticks(range(len(df["mnd_aar"])), df["mnd_aar"], rotation=90)

plt.tight_layout()
plt.legend()
plt.grid(True)

plt.show()