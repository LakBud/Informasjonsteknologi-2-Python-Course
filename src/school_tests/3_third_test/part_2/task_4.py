class Person:
    def __init__(self, navn: str, alder: int) -> None:
        
        """
        Docstring for __init__
        
        :param self: Description
        :param navn: Description
        :type navn: str
        :param alder: Description
        :type alder: int
        """
        
        
        self._navn = navn # Endrer denne til en privat variabel siden navn burde ikke bli manipulert 
        self._alder = alder # Samme grunnen som i navn


class Elev(Person):
    def __init__(self, navn: str, alder: int, elev_id: int) -> None:
        
        """
        Docstring for __init__
        
        :param self: Description
        :param navn: Description
        :type navn: str
        :param alder: Description
        :type alder: int
        :param elev_id: Description
        :type elev_id: int
        """
        
        
        super().__init__(navn, alder)
        self._elev_id = elev_id

class Laerer(Person):
    def __init__(self, navn: str, alder: int, stilling: str, fag_liste: list[str]) -> None:
        
        """
        Docstring for __init__
        
        :param self: Description
        :param navn: Description
        :type navn: str
        :param alder: Description
        :type alder: int
        :param stilling: Description
        :type stilling: str
        :param fag_liste: Description
        :type fag_liste: list[str]
        """
        
        
        super().__init__(navn, alder)
        self.stilling = stilling
        self.fag_liste = fag_liste if fag_liste is not None else [] # En sikring for at programmet skal kunne kjøres effektivt

class SkoleKlasse:

    """
    Docstring for SkoleKlasse
    
    Lokale og private variabler:
    _skolenavn: str
    """
    
    _skolenavn: str = "Lørenskog VGS"
    
    def __init__(self, klassenavn: str, laerere: list[Laerer], elever: list[Elev]) -> None:
        
        """
        Docstring for __init__
        
        :param self: Description
        :param klassenavn: Description
        :type klassenavn: str
        :param laerere: Description
        :type laerere: list[Laerer]
        :param elever: Description
        :type elever: list[Elev]
        """
        
        self._klassenavn = klassenavn
        self.laerere = laerere if laerere is not None else [] # En sikring for at programmet skal kunne kjøres effektivt
        self.elever = elever if elever is not None else [] # En sikring for at programmet skal kunne kjøres effektivt
    
    def legg_til_elev(self, ny_elev: Elev) -> None:
        
        """
        Docstring for legg_til_elev
        
        :param self: Description
        :param ny_elev: Description
        :type ny_elev: Elev
        
        Legger til en elev
        """
        
        if isinstance(ny_elev, Elev): # Denne koden sikrer at den nye eleven tilhører Elev klasse
            self.elever.append(ny_elev)
            
    def legg_til_laerer(self, ny_laerer: Laerer) -> None:
        
        """
        Docstring for legg_til_laerer
        
        :param self: Description
        :param ny_laerer: Description
        :type ny_laerer: Laerer
        
        Legger til en laerer
        """
        
        if isinstance(ny_laerer, Laerer):  # Denne koden sikrer at den nye læreren tilhører Laerer klassen
            self.laerere.append(ny_laerer)
            
    def hent_elevliste(self) -> None:
        
        """
        Docstring for hent_elevliste
        
        :param self: Description
        
        Printer ut skolenavn, klassenavn, lærerene sine navn og elevene sine navn og id
        """
        
        print()
        print(f"Skole: {self._skolenavn} | Klasse: {self._klassenavn}")
        print()
        print(f"Lærere: ", end="")
        for laerer in self.laerere:
            print(f"{laerer._navn:^5}", end="")
        print()
        print()
        print(f"Elever: ")
        for elev in self.elever:
            print(f"Navn: {elev._navn:^10} | ID: {elev._elev_id:^5}")



# Test-case
Max = Laerer("Max", 45, "Lektor", ["Naturfag", "Engelsk"])
Tim = Laerer("Tim", 21, "Vikar", ["Norsk", "Spansk"])
Pam = Laerer("Pam", 41, "Lektor", ["Tysk", "Biologi"])

Jim = Elev("Jim", 16, 20)
Kevin = Elev("Kevin", 17, 21)
Mike = Elev("Mike", 17, 22)

klasse = SkoleKlasse("2STB", [Max, Tim], [Jim, Kevin])
klasse.legg_til_elev(Mike)
klasse.legg_til_laerer(Pam)
klasse.hent_elevliste()
