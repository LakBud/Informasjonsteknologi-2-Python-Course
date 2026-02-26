import pygame as pg
import random as rnd
from classes import *

# ==========================
# KONSTANTER (lett å endre)
# ==========================
BREDDE = 1000
HOYDE = 700
FPS = 60

BALL_FART_X = 6
BALL_FART_Y = -6
RACKET_FART = 10

ANTALL_RADER = 6
ANTALL_KOLONNER = 12
PADDING = 8
MURSTEIN_HOYDE = 30





# ==========================
# SPILL
# ==========================
class Spill:
    def __init__(self):
        pg.init()
        self.skjerm = pg.display.set_mode((BREDDE, HOYDE))
        pg.display.set_caption("Breakout")
        self.klokke = pg.time.Clock()
        self.skrift = pg.font.SysFont(None, 40)

        self.ball = Ball(BREDDE//2, HOYDE//2, 20)
        self.racket = Racket(BREDDE//2 - 75, HOYDE - 40)

        self.murstein_liste = self.lag_vegg(BREDDE)

        self.poeng = 0
        self.game_over = False
        self.kjorer = True

    # ======================
    # LAG VEGG
    # ======================
    def lag_vegg(self, bredde_vegg):

        murstein_bredde = (bredde_vegg - PADDING*(ANTALL_KOLONNER+1)) // ANTALL_KOLONNER
        start_y = 60

        farger = [
            (255, 0, 0),
            (255, 165, 0),
            (255, 255, 0),
            (0, 255, 0),
            (0, 0, 255),
            (128, 0, 128)
        ]

        liste = []

        for i in range(ANTALL_RADER):
            for j in range(ANTALL_KOLONNER):
                x = PADDING*(j+1) + murstein_bredde*j
                y = start_y + (PADDING + MURSTEIN_HOYDE)*i

                m = Murstein(x, y, murstein_bredde, MURSTEIN_HOYDE, farger[i])
                liste.append(m)

        return liste

    # ======================
    # RESET
    # ======================
    def restart(self):
        self.ball.rect.center = (BREDDE//2, HOYDE//2)
        self.ball.stopp()
        self.murstein_liste = self.lag_vegg(BREDDE)
        self.poeng = 0
        self.game_over = False

    # ======================
    # OPPDATER
    # ======================
    def oppdater(self):
        self.ball.beveg(BREDDE)

        # Kollisjon racket
        if self.ball.rect.colliderect(self.racket.rect):
            self.ball.fart_y *= -1
            self.ball.fart_x += rnd.randint(-2, 2)

        # Kollisjon murstein
        for murstein in self.murstein_liste[:]:
            if self.ball.rect.colliderect(murstein.rect):
                self.ball.fart_y *= -1
                self.murstein_liste.remove(murstein)
                self.poeng += 1

        # Game over
        if self.ball.rect.bottom >= HOYDE:
            self.ball.stopp()
            self.game_over = True

    # ======================
    # TEGN
    # ======================
    def tegn(self):
        self.skjerm.fill((0, 0, 0))

        self.ball.tegn(self.skjerm)
        self.racket.tegn(self.skjerm)

        for m in self.murstein_liste:
            m.tegn(self.skjerm)

        poengtekst = self.skrift.render(f"Poeng: {self.poeng}", True, (255,255,255))
        self.skjerm.blit(poengtekst, (20, 20))

        if self.game_over:
            tekst = self.skrift.render("GAME OVER - Trykk X for restart", True, (255,0,0))
            self.skjerm.blit(tekst, (BREDDE//2 - 250, HOYDE//2))

        pg.display.flip()

    # ======================
    # LOOP
    # ======================
    def kjor(self):
        while self.kjorer:
            self.klokke.tick(FPS)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.kjorer = False

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE and not self.ball.i_bevegelse and not self.game_over:
                        self.ball.start(BALL_FART_X, BALL_FART_Y)

                    if event.key == pg.K_x and self.game_over:
                        self.restart()

            taster = pg.key.get_pressed()
            self.racket.beveg(taster, RACKET_FART, BREDDE)

            if not self.game_over:
                self.oppdater()

            self.tegn()

        pg.quit()


# ==========================
# START
# ==========================
if __name__ == "__main__":
    spill = Spill()
    spill.kjor()