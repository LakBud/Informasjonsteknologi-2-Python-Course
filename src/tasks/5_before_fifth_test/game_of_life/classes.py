import pygame as pg

class Organism:
    def __init__(self, window, coords: tuple[int, int], width_obj: int, height_obj: int):
        self._window = window
        self._x = coords[0]
        self._y = coords[1]
        self._width = width_obj
        self._height = height_obj
        self.is_alive = False
        self._color = (0,0,0)
        
        
        # Make the rectangle
        self.image = pg.Surface((self._width, self._height))
        self.image.fill(self._color)

        # Make the surface
        self.rect = self.image.get_rect(center=(coords))
    
    def draw(self) -> None:
        # Draw the rectangle
        self._window.blit(self.image, self.rect)
        
        # Grey outline
        pg.draw.rect(self._window, (150, 150, 150), self.rect, 1)
    
    def update(self) -> None:
        if self.is_alive:
            self._color = (0, 0, 0)
        else:
            self._color = (255, 255, 255)
        
        self.image.fill(self._color)