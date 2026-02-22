import pygame as pg
import random as rnd

class GameBoard:
    def __init__(self, width: int, height: int):
        self.height = height
        self.width = width
        self._objects = []

        self.left_safe_zone = 150
        self.right_safe_zone = width - 150

    def add_object(self, other_obj) -> None:
        self._objects.append(other_obj)

    def remove_object(self, other_obj) -> None:
        if other_obj in self._objects:
            self._objects.remove(other_obj)

    def random_position_in_zone(self, x_min, x_max, y_min=0, y_max=None, obj_width=60, obj_height=60, max_attempts=100):
        if y_max is None:
            y_max = self.height

        for _ in range(max_attempts):
            # Ensure the RECT stays fully inside the zone
            center_x = rnd.randint(x_min + obj_width // 2, x_max - obj_width // 2)
            center_y = rnd.randint(y_min + obj_height // 2, y_max - obj_height // 2)

            rect = pg.Rect(0, 0, obj_width, obj_height)
            rect.center = (center_x, center_y)

            if not any(rect.colliderect(o.rect) for o in self._objects):
                return (center_x, center_y)

        raise RuntimeError("No free position found after max attempts")

class GameObject:
    def __init__(self, window, start_coord: tuple[int, int], width_obj: int, height_obj: int, color: tuple[int, int, int], obj_font, letter: str):
        self._window = window
        self._width = width_obj
        self._height = height_obj
        self._color = color
        self._font = obj_font
        self._letter = letter

        # Make the rectangle
        self.image = pg.Surface((self._width, self._height))
        self.image.fill(self._color)

        # Make the surface
        self.rect = self.image.get_rect(center=(start_coord))

        # Render the letter
        letter_surface = self._font.render(self._letter, True, (0, 0, 0))
        letter_square = letter_surface.get_rect(
            center=(self._width // 2, self._height // 2)
        )

        # Draw the letter
        self.image.blit(letter_surface, letter_square)

    def draw(self) -> None:
        # Draw the rectangle
        self._window.blit(self.image, self.rect)

    def collides_with(self, other_obj) -> bool:
        # Checks if the obj has collided with something else
        return self.rect.colliderect(other_obj.rect)

    def position(self, x: int, y: int) -> None:
        self.rect.center = (x, y)
    
    def move(self, dx: int, dy: int) -> None:
        self.rect.x += dx
        self.rect.y += dy


class Human(GameObject):
    def __init__(self, window, start_coord, width_obj, height_obj, color, obj_font, speed):
        super().__init__(window, start_coord, width_obj, height_obj, color, obj_font, letter="H")
        self._default_speed = speed
        self._speed = speed
        self._score = 0
        self._carrying_sheep = False
    
    def move(self, keys) -> None:
        if keys[pg.K_LEFT]:
            super().move(-self._speed, 0)
        elif keys[pg.K_RIGHT]:
            super().move(self._speed, 0)
        elif keys[pg.K_UP]:
            super().move(0, -self._speed)
        elif keys[pg.K_DOWN]:
            super().move(0, self._speed)
    
    def reduce_speed(self, s_decrease: int) -> None:
        self._speed = max(1, self._speed - s_decrease)
    
    def increase_points(self, p_increase: int) -> None:
        self._score += p_increase
    
    def pick_up_sheep(self):
        self._carrying_sheep = True
        self.reduce_speed(5)
        self._letter += "S+"  # update letter
        self._update_image()   # redraw surface

    def deliver_sheep(self):
        self._carrying_sheep = False
        self._speed = self._default_speed
        self._letter = "H"
        self._update_image()   # redraw surface

    def _update_image(self):
        # Create a new surface
        self.image = pg.Surface((self._width, self._height))
        self.image.fill(self._color)
        
        # Render the current letter
        letter_surface = self._font.render(self._letter, True, (0, 0, 0))
        letter_rect = letter_surface.get_rect(center=(self._width // 2, self._height // 2))
        self.image.blit(letter_surface, letter_rect)
    
    def block_if_outside(self, board: GameBoard) -> None:
        self.rect.clamp_ip(pg.Rect(0, 0, board.width, board.height))

class Obstacle(GameObject):
    def __init__(self, window, start_coord, width_obj, height_obj, color, obj_font):
        super().__init__(window, start_coord, width_obj, height_obj, color, obj_font, letter="O")

class Sheep(GameObject):
    def __init__(self, window, start_coord, width_obj, height_obj, color, obj_font):
        super().__init__(window, start_coord, width_obj, height_obj, color, obj_font, letter="S")
        self._is_carried = False
    
    def set_carried(self, state: bool) -> None:
        self._is_carried = state
    
    def is_carried(self) -> bool:
        return self._is_carried


class Ghost(GameObject):
    def __init__(self, window, start_coord, width_obj, height_obj, color, obj_font, speed):
        super().__init__(window, start_coord, width_obj, height_obj, color, obj_font, letter="G")
        self._speed = speed
        
        # Random diagonal direction
        self.dx = rnd.choice([-speed, speed])
        self.dy = rnd.choice([-speed, speed])
        
    def move(self, board: GameBoard) -> None:
        self.rect.x += self.dx 
        self.rect.y += self.dy 
        
        if self.rect.left <= board.left_safe_zone:
            self.rect.left = board.left_safe_zone
            self.dx *= -1

        if self.rect.right >= board.right_safe_zone:
            self.rect.right = board.right_safe_zone
            self.dx *= -1
        
        if self.rect.top <= 0 or self.rect.bottom >= board.height:
            self.dy *= -1