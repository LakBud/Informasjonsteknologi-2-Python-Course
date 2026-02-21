import pygame as pg
import random as rnd

class GameObject:
    def __init__(self, window, start_coord: tuple[int, int], width_obj: int, height_obj: int, default_color: tuple[int, int, int], speed: int, image_path = None):
        self._window = window
        self._x = start_coord[0]
        self._y = start_coord[1]
        self._width = width_obj
        self._height = height_obj
        self._default_color = default_color
        self._speed = speed

        if image_path:
            try:
                self.image = pg.image.load(image_path).convert_alpha()
                self.image = pg.transform.scale(self.image, (self._width, self._height))
            except FileNotFoundError:
                self.image = pg.Surface((self._width, self._height))
                self.image.fill(self._default_color)
        else:
            self.image = pg.Surface((self._width, self._height))
            self.image.fill(self._default_color)
        
        
        self.rect = self.image.get_rect(center=start_coord)
        
    def draw(self) -> None:
        # Draw the rectangle
        self._window.blit(self.image, self.rect)

    def collides_with(self, other_obj) -> bool:
        # Checks if the obj has collided with something else
        return self.rect.colliderect(other_obj.rect)

    def update(self) -> None:
        pass

class Player(GameObject):
    def __init__(self, window, start_coord: tuple[int, int], width_obj: int, height_obj: int, default_color: tuple[int, int, int], speed: int, image_path="src/tasks/4_before_fourth_test/space_invaders/images/IT2-space-invaders-player.png"):
        super().__init__(window, start_coord, width_obj, height_obj, default_color, speed, image_path)
        self._life_count = 3
    
    def update(self) -> None:
        keys = pg.key.get_pressed()
        # Arrow and WD control
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.rect.centerx -= self._speed 
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.rect.centerx += self._speed
        
        # One-liner to contain the player
        self.rect.clamp_ip(self._window.get_rect())


class Enemy(GameObject):
    direction = 1
    speed = 5

    def __init__(self, window, start_coord: tuple[int, int], width_obj: int, height_obj: int, default_color: tuple[int, int, int]):
        # Load and scale images
        self.images = [
            pg.transform.scale(pg.image.load("src/tasks/4_before_fourth_test/space_invaders/images/IT2-space-Invaders-alien1-a.png").convert_alpha(), (width_obj, height_obj)),
            pg.transform.scale(pg.image.load("src/tasks/4_before_fourth_test/space_invaders/images/IT2-space-Invaders-alien1-b.png").convert_alpha(), (width_obj, height_obj))
        ]
        
        # Call GameObject without image_path
        super().__init__(window, start_coord, width_obj, height_obj, default_color, speed=0, image_path=None)
        
        # Use self.image for draw
        self.image = self.images[0]
        self.current_image = 0
        self.anim_counter = 0

    def update(self):
        # Move horizontally
        self.rect.centerx += Enemy.speed * Enemy.direction

        # Animation
        self.anim_counter += 1
        if self.anim_counter >= 15:
            self.anim_counter = 0
            self.current_image = (self.current_image + 1) % len(self.images)
            self.image = self.images[self.current_image]  # Important: assign to self.image

class Bullet(GameObject):
    def __init__(self, window, start_coord: tuple[int, int], width_obj: int, height_obj: int, default_color: tuple[int, int, int], speed: int, image_path: str):
        super().__init__(window, start_coord, width_obj, height_obj, default_color, speed, image_path)
    
    def update(self) -> None:
        self.rect.centery += self._speed


class Fortification(GameObject):
    
    _defense_count = 5
    
    def __init__(self, window, start_coord: tuple[int, int], width_obj: int, height_obj: int, default_color: tuple[int, int, int], speed: int = 0, image_path="src/tasks/4_before_fourth_test/space_invaders/images/IT2-space-invaders-fortification.png"):
        super().__init__(window, start_coord, width_obj, height_obj, default_color, speed, image_path)

class UFO(GameObject):
    def __init__(self, window, width_obj, height_obj, default_color, speed, image_path="src/tasks/4_before_fourth_test/space_invaders/images/IT2-space-invaders-UFO.png"):
        window_width = window.get_width()
        direction = rnd.choice([-1, 1])

        super().__init__(window, (0, 50), width_obj, height_obj, default_color, speed, image_path)

        self._direction = direction

        if direction == 1:
            self.rect.left = -self.rect.width
        else:
            self.rect.right = window_width + self.rect.width
    
    def update(self) -> None:
        # Move horizontally
        self.rect.centerx += self._speed * self._direction
