alder = int(input("Skriv ditt alder: "))

pris = 0

if alder >= 67:
    pris = 35
    print(f"Du har pensjonistbilett og må betale {pris} kr")
elif alder >= 16:
    pris = 50
    print(f"Du har Voksenbilett og må betale {pris} kr")
else:
    pris = 30
    print(f"Du har barnbilett og må betale {pris} kr")