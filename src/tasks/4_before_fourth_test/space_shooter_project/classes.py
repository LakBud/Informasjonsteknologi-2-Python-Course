import random as rnd
import pygame as pg

class GameObject:
    def __init__(self, window, start_coord: tuple[int, int], width_obj: int, height_obj: int, color: tuple[int, int, int], speed: int, image_path = None) -> None:
        
        """
        Docstring for __init__
        
        :param self: Description
        :param window: Description
        :param start_coord: Description
        :type start_coord: tuple[int, int]
        :param width_obj: Description
        :type width_obj: int
        :param height_obj: Description
        :type height_obj: int
        :param color: Description
        :type color: tuple[int, int, int]
        :param speed: Description
        :type speed: int
        :param image_path: Description
        """
        
        self._window = window
        self._width = width_obj
        self._height = height_obj
        self._color = color
        self._speed = speed
    
        if image_path:
            try:
                self._original_image = pg.image.load(image_path).convert_alpha()
                self._image = pg.transform.scale(self._original_image, (self._width, self._height))
            except FileNotFoundError:
                self._image = pg.Surface((self._width, self._height))
                self._image.fill(self._color)
        else:
            self._image = pg.Surface((self._width, self._height))
            self._image.fill(self._color)
        
        
        self.rect = self._image.get_rect(center=start_coord)
        
    def draw(self) -> None:
        self._window.blit(self._image, self.rect.topleft)

    def collides_with(self, other_obj) -> bool:
        return self.rect.colliderect(other_obj.rect)

class Player(GameObject):
    def __init__(self, window, start_coord: tuple[int, int], width_obj: int, height_obj: int, color: tuple[int, int, int], speed: int):        
        super().__init__(window, start_coord, width_obj, height_obj, color, speed, image_path="images/4/IT2-Spaceship1.png")
        self.bullets = []

    def move(self) -> None:
        keys = pg.key.get_pressed()
        # Arrow and WASD control
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.rect.x -= self._speed 
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.rect.x += self._speed
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.rect.y -= self._speed
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.rect.y += self._speed

    def activate_border_collision(self) -> None:
        if self.rect.bottom > self._window.get_height():
            self.rect.bottom = self._window.get_height()
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.right > self._window.get_width():
            self.rect.right = self._window.get_width()
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self) -> None:
        # Creates a bullet and appends it to its list
        bullet = Bullet(self._window, (self.rect.centerx, self.rect.top), 10, 20, (255,0,0), -15)
        self.bullets.append(bullet)


class Alien(GameObject):
    def __init__(self, window, width_obj: int, height_obj: int, color: tuple[int, int, int], speed: int):
        
        """
        Docstring for __init__
        
        :param self: Description
        :param window: Description
        :param width_obj: Description
        :type width_obj: int
        :param height_obj: Description
        :type height_obj: int
        :param color: Description
        :type color: tuple[int, int, int]
        :param speed: Description
        :type speed: int
        """
        
        start_x = rnd.randint(20, window.get_width() - width_obj)
        start_y = -height_obj 
        super().__init__(window, (start_x, start_y), width_obj, height_obj, color, speed, image_path="images/4/IT2-alien.png")
        
        self.x_speed = rnd.choice([-2, -1, 1, 2]) # Chosen speeds the enemy can have with x

    def move(self) -> None:
        self.rect.y += self._speed
        self.rect.x += self.x_speed
        
        # If it touches the left or the right border, bounce to another direction
        if self.rect.left <= 0 or self.rect.right >= self._window.get_width():
            self.x_speed *= -1  # Changes direction


class Bullet(GameObject):
    def __init__(self, window, start_coord: tuple[int, int], width_obj: int, height_obj: int, color: tuple[int, int, int], speed: int) -> None:
        super().__init__(window, start_coord, width_obj, height_obj, color, speed, image_path="images/4/IT2-bullet.png")
    
    def move(self):
        # Moves upwards
        self.rect.y += self._speed