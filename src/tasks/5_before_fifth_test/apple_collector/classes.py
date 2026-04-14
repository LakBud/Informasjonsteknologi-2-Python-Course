import pygame as pg

class GameObject:
    def __init__(self, window, coords: tuple[int, int], width_obj: int, height_obj: int, color: tuple[int, int, int], speed: int):
        self._window = window
        self._x = coords[0]
        self._y = coords[1]
        self._width = width_obj
        self._height = height_obj
        self._color = color
        self._speed = speed
        
        # Make the rectangle
        self.image = pg.Surface((self._width, self._height))
        self.image.fill(self._color)

        # Make the surface
        self.rect = self.image.get_rect(center=(coords))
    
    def draw(self) -> None:
        # Draw the rectangle
        self._window.blit(self.image, self.rect)
    
    def collides_with(self, other_obj) -> bool:
        return self.rect.colliderect(other_obj.rect)

class Player(GameObject):
    def __init__(self, window, coords, width_obj, height_obj, color, speed):
        super().__init__(window, coords, width_obj, height_obj, color, speed)
        self.draw_basket()
        
    
    def draw_basket(self):
        self.image.fill((0, 0, 0, 0))  # clear surface

        pg.draw.arc(
            self.image,
            self._color,
            (0, 0, self._width, self._height),
            3.14,
            0,
            5
        )

        pg.draw.line(
            self.image,
            self._color,
            (0, self._height // 2),
            (self._width, self._height // 2),
            5
        )
    
    
    def update(self) -> None:
        keys = pg.key.get_pressed()
        # Arrow and WD control
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.rect.centerx -= self._speed 
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.rect.centerx += self._speed
        
        # One-liner to contain the player
        self.rect.clamp_ip(self._window.get_rect())
    
    def input_color(self) -> None:
        keys = pg.key.get_pressed()
        
        if keys[pg.K_r]:
            self._color = (255, 0, 0)
            self.draw_basket()
        
        if keys[pg.K_g]:
            self._color = (0, 255, 0)
            self.draw_basket()

class Apple(GameObject):
    def __init__(self, window, coords, width_obj, height_obj, color, speed):
        super().__init__(window, coords, width_obj, height_obj, color, speed)
        
    def update(self):
        # Move downwards
        self.rect.centery += self._speed