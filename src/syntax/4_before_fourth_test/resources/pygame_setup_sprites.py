import pygame as pg
import random as rnd

# Globale Konstanter
SKJERM_BREDDE = 800
SKJERM_HOYDE = 600
FPS = 60

##### -- Start: KLASSER -- #####

class Spillobjekt(pg.sprite.Sprite): #Arver nå fra pg.sprite.Sprite
    """Baseklassen for alle ting i spillet."""
    def __init__(self, start_koord :tuple, bredde_obj: int, hoyde_obj :int, farge_obj: tuple, fart_obj :int = 0):
        super().__init__() #Nødvendig for at Sprite-metoder skal fungere
        
        self.image = pg.Surface((bredde_obj, hoyde_obj))
        self.image.fill(farge_obj)
        self.rect = self.image.get_rect()
        self.rect.topleft = start_koord
        
        self._fart = fart_obj

    def update(self):
        """Oppdaterer objektets posisjon eller tilstand."""
        pass


class Spiller(Spillobjekt):
    """Klassen for spilleren."""
    def __init__(self, start_koord :tuple, bredde_obj: int, hoyde_obj :int, farge_obj: tuple, fart_obj :int = 0):
        super().__init__(start_koord, bredde_obj, hoyde_obj, farge_obj, fart_obj)
        self._poeng = 0

    def update(self):
        pass


class Fiende(Spillobjekt):
    """Klassen for fiender."""
    def __init__(self, start_koord :tuple, bredde_obj: int, hoyde_obj :int, farge_obj: tuple, fart_obj :int = 0):
        super().__init__(start_koord, bredde_obj, hoyde_obj, farge_obj, fart_obj)

    def update(self):
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
        
        # Vi bruker Grupper i stedet for lister
        self._alle_sprites = pg.sprite.Group()
        self._fiender = pg.sprite.Group()
        
        # Oppretting av spiller
        spiller_start = (skjermbredde//2,skjermhoyde//2)
        spiller_bredde = 25
        spiller_hoyde = 25
        spiller_farge = (255,0,0) #rød
        spiller_fart = 5
        self._spiller = Spiller(spiller_start, spiller_bredde, spiller_hoyde, spiller_farge, spiller_fart)
        
        # Legg spilleren i gruppen som skal tegnes
        self._alle_sprites.add(self._spiller)
        
        self._score = 0

    def lag_ny_fiende(self, ny_fiende: Spillobjekt):
        """ Her kan det hende du må legge inn kode for tilfeldig tildeling av startkoodrindater og slikt"""
        fiende_start = (SKJERM_BREDDE//2,SKJERM_HOYDE//2)
        fiende_bredde = 25
        fiende_hoyde = 25
        fiende_farge = (0,255,0) #grønn
        fiende_fart = 5
        #ny_fiende = Fiende(fiende_start, fiende_bredde, fiende_hoyde, fiende_farge, fiende_fart)
        self._fiender.add(ny_fiende)
        self._alle_sprites.add(ny_fiende)

    def sjekk_kollisjoner(self):
        """Sjekker om objekter overlapper. Det er naturlig å legge dette her siden Spillkontroll 
        har listene med objekter som attributter"""
        pass

    def handter_hendelser(self):
        for hendelse in pg.event.get():
            if hendelse.type == pg.QUIT:
                self._aktiv = False # Rettet fra er_igang til _aktiv

    def oppdater(self):
        """Oppdaterer alle objekter i gruppene."""
        self._alle_sprites.update()

    def tegn_alt(self):
        self._skjerm.fill((0, 0, 0))
        
        # Tegner alle sprites med én kommando
        self._alle_sprites.draw(self._skjerm)
        
        pg.display.flip()

    def kjor(self):
        while self._aktiv:
            self.handter_hendelser()
            self.oppdater()
            self.tegn_alt()
            self._klokke.tick(self._fps)
        
        pg.quit() # Rettet fra pygame.quit() til pg.quit()

##### -- Start spillet -- #####
if __name__ == "__main__":
    spill = Spillkontroll(SKJERM_BREDDE, SKJERM_HOYDE, FPS)
    spill.kjor()