import pygame as pg
from abc import ABC

# Globale Variabler
BREDDE, HOYDE = 800, 600
aktiv = True
FPS = 60 # Frames per second

# Klasse definisjoner
class SpillObjekt(ABC):
    
    """
    Docstring for SpillObjekt
    
    SpillObjekt er en abstrakt klasse.
    Betyr at det skal bare bli arvet og ikke kan bli brukt direkte
    ABC blir brukt for å indikere en abstrakt klasse
    """
    
    
    def __init__(self, vindu, start_koord: tuple[int, int], bredde_obj: int, hoyde_obj: int, farge: tuple[int, int, int], fart: int, obj_font, bokstav: str):
        self._vindu = vindu
        self._x = start_koord[0]
        self._y = start_koord[1]
        self._bredde = bredde_obj
        self._hoyde = hoyde_obj
        self._farge = farge
        self._fart = fart
        self._font = obj_font
        self._bokstav = bokstav
        
        # Vi lager en firkant (Vår "bilde") ... med farge
        self.image = pg.Surface((self._bredde, self._hoyde))
        self.image.fill(self._farge)
        
        # Vi lager et rect-objekt som skal håndtere plassering osv
        self.rect = self.image.get_rect(center=(self._x, self._y))
        
        bokstav_flate = self._font.render(self._bokstav, True, (0,0,0))
        bokstav_firkant = bokstav_flate.get_rect(center=(self._bredde // 2, self._hoyde // 2))
        
        # Tegn bokstaven på firkanten / "bildet"
        self.image.blit(bokstav_flate, bokstav_firkant)
    

    def tegn(self) -> None:
        # Tegner firkanten / "bildet" med sitt overflate (rect)
        self._vindu.blit(self.image, self.rect)

    def kolliderer_med(self, other_obj) -> bool:
        # Sjekker hvis sitt overflate truffer en annen objekt sitt overflate
        return self.rect.colliderect(other_obj.rect)


class Spiller(SpillObjekt):
    def __init__(self, vindu, start_koord: tuple[int, int], bredde_obj: int, hoyde_obj: int, farge: tuple[int, int, int], fart: int, obj_font, bokstav: str):
        super().__init__(vindu, start_koord, bredde_obj, hoyde_obj, farge, fart, obj_font, bokstav)
    
    def beveg(self) -> None:
        # Finner hvilken tast har blitt trykket på
        tast = pg.key.get_pressed()
        
        # Sjekker hvis den tasten tilsvarer en retning (WASD og pil kontrol)
        if tast[pg.K_LEFT] or tast[pg.K_a]:
            self.rect.x -= self._fart
            
        if tast[pg.K_RIGHT] or tast[pg.K_d]:
            self.rect.x += self._fart
        
        if tast[pg.K_UP] or tast[pg.K_w]:
            self.rect.y -= self._fart
        
        if tast[pg.K_DOWN] or tast[pg.K_s]:
            self.rect.y += self._fart
        
    def aktiver_grense_kontroll(self) -> None:
        # Sørger for at self.rect alltid holder seg innenfor vinduets grenser ved å “klemme” rektangelet inn i vinduets rektangel.
        self.rect.clamp_ip(self._vindu.get_rect())



# Oppsett
pg.init()
skjerm = pg.display.set_mode((BREDDE, HOYDE))
klokke = pg.time.Clock()
min_font = pg.font.SysFont(None, 50)

# Lage spillobject
spiller_start_koord: tuple[int, int] = (BREDDE // 2, HOYDE // 2)
spiller_bredde: int = 50
spiller_hoyde: int = 50
spiller_farge: tuple[int, int, int] = (123, 90, 203)
spiller_fart: int = 10
spiller_bokstav: str = "T"

spiller = Spiller(skjerm, spiller_start_koord, spiller_bredde, spiller_hoyde, spiller_farge, spiller_fart, min_font, spiller_bokstav)

# Game loop (Hovedløkken)
while aktiv:
    # Sjekk om brukeren vi lukke vinduet
    for hendelse in pg.event.get():
        if hendelse.type == pg.QUIT:
            aktiv = False
    
    
    # Tegn bakgrunn før objektene
    skjerm.fill((255, 255, 255)) # Hvit
    
    # Hente objektene
    spiller.tegn()
    spiller.beveg()
    spiller.aktiver_grense_kontroll()
    
    
    # Oppdater skjermen
    pg.display.flip()
    klokke.tick(FPS)
    
pg.quit()