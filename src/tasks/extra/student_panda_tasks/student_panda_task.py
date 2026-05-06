import pandas as pd

# A)

# Les fil
df = pd.read_csv("Elever-fag-redigert.csv")

# År-kolonner
år = ["2022-23", "2023-24", "2024-25"]

# Gjør om til tall
for col in år:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Gruppér etter fagområde
resultat = df.groupby("Fagomraadenavn")[år].sum()

print("\nAntall elever per fagområde:\n")
print(resultat)

# B)

# Vis tilgjengelige fagområder
print("\nTilgjengelige fagområder:")
print(df["Fagomraadenavn"].unique())

valg = input("\nVelg fagområde: ")

# Filtrer
filtrert = df[df["Fagomraadenavn"] == valg]

# Velg relevante kolonner
resultat = filtrert[["Opplaeringsfagnavn"] + år]

print(f"\nFag i {valg}:\n")
print(resultat.to_string(index=False))

# C)

valg = input("\nVelg fagområde for analyse: ")

filtrert = df[df["Fagomraadenavn"] == valg].copy()

# Endring
filtrert["endring"] = filtrert["2024-25"] - filtrert["2022-23"]

# Prosentendring
filtrert["prosent"] = (filtrert["endring"] / filtrert["2022-23"]) * 100

# Finn fag
størst_oppgang = filtrert.loc[filtrert["endring"].idxmax()]
størst_prosent = filtrert.loc[filtrert["prosent"].idxmax()]
størst_nedgang = filtrert.loc[filtrert["endring"].idxmin()]
størst_prosent_nedgang = filtrert.loc[filtrert["prosent"].idxmin()]

print("\nResultat:\n")

print("1. Størst absolutt oppgang:")
print(størst_oppgang["Opplaeringsfagnavn"])

print("\n2. Størst prosentvis oppgang:")
print(størst_prosent["Opplaeringsfagnavn"])

print("\n3. Størst absolutt nedgang:")
print(størst_nedgang["Opplaeringsfagnavn"])

print("\n4. Størst prosentvis nedgang:")
print(størst_prosent_nedgang["Opplaeringsfagnavn"])