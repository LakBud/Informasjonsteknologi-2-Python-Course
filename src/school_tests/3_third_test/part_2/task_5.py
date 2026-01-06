# Enheter


class Enhet:
    total_enheter: int = 0

    def __init__(self, navn: str, enhet_id: int) -> None:
        self._navn = navn
        self._enhet_id = enhet_id
        self.status = False

        Enhet.total_enheter += 1

    def sla_pa(self) -> None:
        self.status = True

    def sla_av(self) -> None:
        self.status = False


class LysEnhet(Enhet):
    def __init__(self, navn: str, enhet_id: int, lysstyrke: int) -> None:
        super().__init__(navn, enhet_id)
        self.lysstyrke = lysstyrke


class VarmEnhet(Enhet):
    def __init__(self, navn: str, enhet_id: int, temperatur: int) -> None:
        super().__init__(navn, enhet_id)
        self.temperatur = temperatur



# Smarthub


class Smarthub:
    def __init__(self, hub_id: int) -> None:
        self.hub_id = hub_id
        self.enheter: list[Enhet] = []
        self.aktive_enheter: list[Enhet] = []

    def legg_til_enhet(self, enhet: Enhet) -> None:
        if enhet not in self.enheter:
            self.enheter.append(enhet)
            if enhet.status:
                self.aktive_enheter.append(enhet)

    def fjern_enhet(self, navn: str) -> None:
        for enhet in self.enheter:
            if enhet._navn == navn:
                self.enheter.remove(enhet)
                if enhet in self.aktive_enheter:
                    self.aktive_enheter.remove(enhet)
                return
        print("Fant ingen enhet med dette navnet")

    def skru_av_alt(self) -> None:
        for enhet in self.aktive_enheter:
            enhet.sla_av()
        self.aktive_enheter.clear()

    def system_status(self) -> None:
        print(f"Totale enheter i systemet: {len(self.enheter)}")
        print(f"Aktive enheter: {len(self.aktive_enheter)}\n")

        print("Lys-enheter:")
        for enhet in self.enheter:
            if isinstance(enhet, LysEnhet):
                print(
                    f"Navn: {enhet._navn:<12} "
                    f"Lysstyrke: {enhet.lysstyrke:<4} "
                    f"Status: {'På' if enhet.status else 'Av'}"
                )

        print("\nVarme-enheter:")
        for enhet in self.enheter:
            if isinstance(enhet, VarmEnhet):
                print(
                    f"Navn: {enhet._navn:<12} "
                    f"Temperatur: {enhet.temperatur:<4} "
                    f"Status: {'På' if enhet.status else 'Av'}"
                )



# Test


sh = Smarthub(204)

ac = VarmEnhet("AC", 201, 21)
varmer = VarmEnhet("Varmer", 202, 22)
heater = VarmEnhet("Heater", 203, 57)

lampe = LysEnhet("Lampe", 200, 40)
rgb = LysEnhet("RGB Hexagons", 205, 65)
lyspaere = LysEnhet("Lyspære", 206, 82)

ac.sla_pa()
heater.sla_pa()
lampe.sla_pa()

sh.legg_til_enhet(ac)
sh.legg_til_enhet(lampe)
sh.legg_til_enhet(rgb)
sh.legg_til_enhet(varmer)
sh.legg_til_enhet(lyspaere)

sh.system_status()

sh.fjern_enhet("Lampe")
sh.system_status()

sh.skru_av_alt()
sh.system_status()
