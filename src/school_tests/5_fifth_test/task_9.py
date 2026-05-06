import csv
import matplotlib.pyplot as plt

filnavn = "strom_forbruk.csv" #Evt endre dette slik at du får lest inn fila
strom_data = []               #Dette er bare et forslag til datastruktur

# Åpne fila og les inn data
header = []
ny_data = []

with open(filnavn, encoding="utf-8") as file:
    data = csv.reader(file, delimiter=",")
    
    header = next(data)
    
    for linje in data:
        ny_data.append(linje)



##################################
#####--- Start: Oppgave a ---#####

# skriv ut strøm dataene lettlest måte, med overskrift

print("\n-----------------------------------------------")
print("a) Oversikt over strømdata\n")

#####--- Slutt: Oppgave a ---#####
##################################

print(f"{"år":^15} | {"Måned":^15} | {"forbruk_kWh":^15} | {"pris_ore_per_kWh":^15}")

print("-" * 75)

for rad in ny_data:
    print(f"{rad[0]:^15} | {rad[1]:^15} | {rad[2]:^15} | {rad[3]:^15}")




##################################
#####--- Start: Oppgave b ---#####

#Skriv ut den totale kostnaden for hvert år på en lettlest måte

print("\n-----------------------------------------------")
print("b) Total kostnad pr år\n")

total = []

for rad in ny_data:
    total.append((rad[0], (int(rad[2]) * int(rad[3]))))





#####--- Slutt: Oppgave b ---#####
##################################


##################################
#####--- Start: Oppgave c ---#####

#Skriv ut måneden med høyest forbruk (hvilket år, hvilken måned og forbruket) på en lettlest måte

print("\n-----------------------------------------------")
print("c) Måned med høyest forbruk\n")


    

#####--- Slutt: Oppgave c ---#####
##################################


##################################
#####--- Start: Oppgave d ---#####

#Lag et plot/graf som viser utviklingen i strømkostnad for hele perioden 

print("\n-----------------------------------------------")
print("d) Her bør det dukke opp en graf\n")

plt.show()

#####--- Slutt: Oppgave d ---#####
##################################