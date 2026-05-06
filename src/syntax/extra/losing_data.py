import pandas as pd
# .isnull()

df = pd.read_csv("data/extra/loss_of_data.csv")

# print(df.isnull().sum())

# how="all" | "any"
# inplace=False
df_cleaned = df.dropna(subset=["Fravær_Timer", "Karakter"])

print(df_cleaned)
