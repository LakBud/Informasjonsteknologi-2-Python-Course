# ============================================================
# Bestillingssystem for nettbutikk - musikkinstrumenter
# Kontaktperson: Kaja Lund, tlf: 91 00 00 00
# ============================================================


##################################
#####--- Start: Oppgave a ---#####

# Her koder du alle klassene du skal bruke i oppgaven

# HANDEL


class Person:
    def __init__(self, navn: str, tlf: str):
        self._navn = navn
        self._tlf = tlf

class Kunde(Person):
    def __init__(self, navn, tlf):
        super().__init__(navn, tlf)
        self._order = []

class Butikk(Person):
    def __init__(self, navn, tlf):
        super().__init__(navn, tlf)
        
        self._kunder = []
        self._varer = []
        self._order = []
    
    def legg_kunde(self, kunde: Kunde):
        self._kunder.append(kunde)
    
    
    def legg_vare(self, vare):
        self._varer.append(vare)
    
    def legg_order(self, order):
        self._order.append(order)
        order._kunde._order.append(order)
    
    
    def register_bestilling(self, kunde: Kunde, vare):
        order = Order(kunde, vare)
        self.legg_order(order)
        self.legg_kunde(kunde)
        self.legg_vare(vare)
        
        vare._produkt.legg_til_solgt(vare._mengde)
    
    def vis_total_bestilt(self):
        for order in self._order:
            print(f"\nNavn: {order._kunde._navn} | Tlf: {order._kunde._tlf}")
            
            print("\nProdukter:")
            print(f"Instrument: {order._vare._produkt._navn} | Pris: {order._vare._produkt._pris} kr | Mengde: {order._vare._mengde}")
            
            print("\nTotal pris:")
            print(f"{order._vare.finn_antall_pris()} kr")
    
    def vis_salgsstatistikk(self):
        totalt_tjent = 0
        for order in self._order:
            totalt_tjent += order._vare.finn_antall_pris()
            
            print(f"Instrument: {order._vare._produkt._navn} | Antall solgte enheter: {order._vare._produkt.antall_solgt()}")
        
        print()
        print(f"Totalt tjent: {totalt_tjent} kr")

    def finn_instrument_type(self, input_var: str):
        for vare in self._varer:
            if input_var == "blase instrument" and vare._produkt._type == input_var:
                print(f"Type: {vare._produkt._type} | {vare._produkt._navn} | Pris: {vare._produkt._pris} | Materiale: {vare._produkt._materiale}")
            elif input_var == "strenge instrument" and vare._produkt._type == input_var:
                print(f"Type: {vare._produkt._type} | {vare._produkt._navn} | Pris: {vare._produkt._pris} | Antall stenger: {vare._produkt._antall_strenger}")
            elif input_var == "slagverk" and vare._produkt._type == input_var:
                print(f"Type: {vare._produkt._type} | {vare._produkt._navn} | Pris: {vare._produkt._pris} | Farge: {vare._produkt._farge}")

# INSTRUMENT

class Instrument:
    def __init__(self, navn: str, pris: float):
        self._navn = navn
        self._pris = pris
        self._antall_solgt = 0
    
    def legg_til_solgt(self, mengde: int):
        self._antall_solgt += mengde
    
    def antall_solgt(self):
        return self._antall_solgt

class BlåseInstrument(Instrument):
    def __init__(self, navn, pris, materiale: str):
        super().__init__(navn, pris)
        self._materiale = materiale
        self._type = "blase instrument"
        

class StrengeInstrument(Instrument):
    def __init__(self, navn, pris, antall_strenger: int):
        super().__init__(navn, pris)
        self._antall_strenger = antall_strenger
        self._type = "strenge instrument"

class Slagverk(Instrument):
    def __init__(self, navn, pris, farge: str):
        super().__init__(navn, pris)
        self._farge = farge
        self._type = "slagverk"


# ORDER

class Vare:
    def __init__(self, produkt: Instrument, mengde: int):
        self._produkt = produkt
        self._mengde = mengde
    
    def finn_antall_pris(self):
        return self._produkt._pris * self._mengde

class Order:
    def __init__(self, kunde: Kunde, vare: Vare):
        self._kunde = kunde
        self._vare = vare
    
    def legg_til_order(self, instrument: Instrument, mengde: float):
        self._varer.append(Vare(instrument, mengde))
        instrument.legg_til_solgt(mengde)

#####--- Slutt: Oppgave a ---#####
##################################



##################################
#####--- Start: Oppgave b ---#####

# Her legger du inn koden som legger inn produktene i systemet
Gitar = StrengeInstrument("Guitar", 2000, 6)
Floyte = BlåseInstrument("Floyte", 2500, "Tre")
Cajon = Slagverk("Cajon", 1200, "Brun")

#####--- Slutt: Oppgave b ---#####
##################################



##################################
#####--- Start: Oppgave c ---#####

# Her skriver du inn koden som registrerer bestillinger
nett_butikk = Butikk("Lars Holm", "98 76 54 32")

k1 = Kunde("Max", "47+ 32 92 29 27")
floyte_vare = Vare(Floyte, 5)

nett_butikk.register_bestilling(k1, floyte_vare)



k2 = Kunde("Timmy", "47+ 32 92 29 27")
gitar_vare = Vare(Gitar, 10)

nett_butikk.register_bestilling(k2, gitar_vare)

#####--- Slutt: Oppgave c ---#####
##################################


##################################
#####--- Start: Oppgave d ---#####

# Skriv ut oversikt over hva hver kunde har bestilt og totalpris per kunde på en ryddig/lettlest måte

print("\n------------------------------------------------------")
print("d) Bestillingsoversikt\n")

nett_butikk.vis_total_bestilt()


#####--- Slutt: Oppgave d ---#####
##################################



##################################
#####--- Start: Oppgave e ---#####

# Skriv ut en salgsstatistikk for butikken

print("\n------------------------------------------------------")
print("e) Salgsstatistikk\n")


#####--- Slutt: Oppgave e ---#####
##################################

nett_butikk.vis_salgsstatistikk()


##################################
#####--- Start: Oppgave f ---#####

# Skriv kode som lar deg søke etter en instrumenttype

print("\n------------------------------------------------------")
print("f) Søkefunksjonalitet\n")

instrument_type = input("Hva søker du etter: ")

nett_butikk.finn_instrument_type(instrument_type)

#####--- Slutt: Oppgave f ---#####
##################################