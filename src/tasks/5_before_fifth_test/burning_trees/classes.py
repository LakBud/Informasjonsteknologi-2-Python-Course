import pygame as pg

class Cell:
    def __init__(self, window, coords: tuple[int, int], width_obj: int, height_obj: int):
        self._window = window
        self._x = coords[0]
        self._y = coords[1]
        self._width = width_obj
        self._height = height_obj

        # bedre tilstander enn bool
        self.state = "empty"  # "tree", "fire"

        self.image = pg.Surface((self._width, self._height))
        self.rect = self.image.get_rect(topleft=coords)

    def update(self):
        if self.state == "tree":
            self._color = (0, 200, 0)
        elif self.state == "fire":
            self._color = (255, 0, 0)
        else:
            self._color = (255, 255, 255)

        self.image.fill(self._color)

    def draw(self) -> None:
        self._window.blit(self.image, self.rect)
        pg.draw.rect(self._window, (150, 150, 150), self.rect, 1)