import pygame as pg
import random as rnd

# Globale Konstanter (vanlig å angi med bare store bokstaver for lesbarhetens skyld)
SKJERM_BREDDE = 800
SKJERM_HOYDE = 600
FPS = 60

##### -- Start: KLASSER -- #####

class Spillobjekt:
    """Baseklassen for alle ting i spillet."""
    def __init__(self, start_koord :tuple, bredde_obj: int, hoyde_obj :int, farge_obj: tuple, fart_obj :int = 0):
        # Vi beholder disse engelske navnene for kompatibilitet med Pygame-logikk
        self.image = pg.Surface((bredde_obj, hoyde_obj))
        self.image.fill(farge_obj)
        self.rect = self.image.get_rect()
        self.rect.topleft = start_koord
        
        self._fart = fart_obj

    def update(self):
        """Oppdaterer objektets posisjon eller tilstand."""
        pass

    def tegn(self, skjerm):
        """Tegner objektet på skjermen."""
        pass


class Spiller(Spillobjekt):
    """Klassen for spilleren."""
    def __init__(self, start_koord :tuple, bredde_obj: int, hoyde_obj :int, farge_obj: tuple, fart_obj :int = 0):
        super().__init__(start_koord, bredde_obj, hoyde_obj, farge_obj, fart_obj)
        self._poeng = 0

    def update(self):
        """Spiller-spesifikk logikk. F.eks. sjekk input og flytt spiller i henhold til dette"""
        pass


class Fiende(Spillobjekt):
    """Klassen for fiender."""
    def __init__(self, start_koord :tuple, bredde_obj: int, hoyde_obj :int, farge_obj: tuple, fart_obj :int = 0):
        super().__init__(start_koord, bredde_obj, hoyde_obj, farge_obj, fart_obj)

    def update(self):
        """Fiende-spesifikk logikk (f.eks. automatisk bevegelse)."""
        pass


class Spillkontroll:
    """Hjernen i programmet som styrer flyten."""
    def __init__(self, skjermbredde :int, skjermhoyde :int, fps :int):
        pg.init()
        self._skjerm = pg.display.set_mode((skjermbredde, skjermhoyde))
        pg.display.set_caption("Mitt fantastiske spill")
        self._klokke = pg.time.Clock()
        self._fps = fps
        self._aktiv = True
        self._font = pg.font.SysFont("Calibri", 28, True)
        
        # Oppretting av objekter
        spiller_start = (skjermbredde//2,skjermhoyde//2)
        spiller_bredde = 25
        spiller_hoyde = 25
        spiller_farge = (255,0,0) #rød
        spiller_fart = 5
        self._spiller = Spiller(spiller_start, spiller_bredde, spiller_hoyde, spiller_farge, spiller_fart)
        
        #Dersom det er mange "fiender"
        self._fiender = [] # En liste som holder på alle fiende-objektene
        
        self._score = 0

    def lag_ny_fiende(self):
        """ Her kan det hende du må legge inn kode for tilfeldig tildeling av startkoodrindater og slikt"""
        fiende_start = (SKJERM_BREDDE // 2, SKJERM_HOYDE // 2)
        fiende_bredde = 25
        fiende_hoyde = 25
        fiende_farge = (0,255,0) #grønn
        fiende_fart = 5
        """Oppretter en ny fiende og legger den i listen."""
        pass

    def sjekk_kollisjoner(self):
        """Sjekker om objekter overlapper. Naturlig å lage metoder for dette i spiller og/eller fiende klassene"""
        pass

    def handter_hendelser(self):
        """Sjekker om brukeren f.eks. trykker på X for å avslutte."""
        for hendelse in pg.event.get():
            if hendelse.type == pg.QUIT:
                self._aktiv = False

    def oppdater(self):
        """Kjører update-metoden, f.eks. flytting av spiller, på alle objekter."""
        pass

    def tegn_alt(self):
        """Tegner bakgrunn og alle objekter."""
        self._skjerm.fill((0, 0, 0)) # Sort bakgrunn
        
        """Tegn alle objektene i spillet. Typisk kalle på tegn-metoden"""
        
        pg.display.flip()

    def kjor(self):
        """Hovedløkken."""
        while self._aktiv:
            self.handter_hendelser()
            self.oppdater()
            self.tegn_alt()
            self._klokke.tick(self._fps)
        
        pg.quit()


##### -- Slutt: KLASSER -- #####


##### -- Start spillet -- #####
if __name__ == "__main__":
    spill = Spillkontroll(SKJERM_BREDDE,SKJERM_HOYDE,FPS)
    spill.kjor()
