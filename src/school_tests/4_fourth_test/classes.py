import pygame as pg

# ==========================
# BASIS KLASSE
# ==========================
class SpillObjekt:
    def __init__(self, x, y, bredde, hoyde, farge):
        self.rect = pg.Rect(x, y, bredde, hoyde)
        self.farge = farge

    def tegn(self, skjerm):
        pg.draw.rect(skjerm, self.farge, self.rect)


# ==========================
# BALL
# ==========================
class Ball(SpillObjekt):
    def __init__(self, x, y, str):
        super().__init__(x, y, str, str, (255, 255, 255))
        self.fart_x = 0
        self.fart_y = 0
        self.i_bevegelse = False

    def start(self, fart_x, fart_y):
        self.fart_x = fart_x
        self.fart_y = fart_y
        self.i_bevegelse = True

    def stopp(self):
        self.fart_x = 0
        self.fart_y = 0
        self.i_bevegelse = False

    def beveg(self, bredde):
        if self.i_bevegelse:
            self.rect.x += self.fart_x
            self.rect.y += self.fart_y

            # Vegger
            if self.rect.left <= 0 or self.rect.right >= bredde:
                self.fart_x *= -1

            if self.rect.top <= 0:
                self.fart_y *= -1


# ==========================
# RACKET
# ==========================
class Racket(SpillObjekt):
    def __init__(self, x, y):
        super().__init__(x, y, 150, 20, (180, 180, 180))

    def beveg(self, taster, fart, bredde):
        if taster[pg.K_LEFT]:
            self.rect.x -= fart
        if taster[pg.K_RIGHT]:
            self.rect.x += fart

        # Ikke utenfor skjerm
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > bredde:
            self.rect.right = bredde


# ==========================
# MURSTEIN
# ==========================
class Murstein(SpillObjekt):
    pass
