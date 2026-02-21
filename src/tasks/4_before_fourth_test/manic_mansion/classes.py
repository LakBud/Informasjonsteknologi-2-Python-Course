import pygame as pg

class GameBoard:
    def __init__(self, height: int, width: int):
        self.height = height
        self._width = width
        self._objects = []
    
    def add_object(self, other_obj) -> None:
        self._objects.append(other_obj)
    
    def remove_object(self, other_obj) -> None:
        self._objects.remove(other_obj)



class GameObject:
    def __init__(self, window, start_coord: tuple[int, int], width_obj: int, height_obj: int, color: tuple[int, int, int], obj_font, letter: str):
        self._window = window
        self._x = start_coord[0]
        self._y = start_coord[1]
        self._width = width_obj
        self._height = height_obj
        self._color = color
        self._font = obj_font
        self._letter = letter

        # Make the rectangle
        self.image = pg.Surface((self._width, self._height))
        self.image.fill(self._color)

        # Make the surface
        self.rect = self.image.get_rect(center=(self._x, self._y))

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

    def update(self) -> None:
        pass


class Human(GameObject):
    def __init__(self, window, start_coord, width_obj, height_obj, color, obj_font, letter, speed):
        super().__init__(window, start_coord, width_obj, height_obj, color, obj_font, letter)
        self._speed = speed
        self._score = 0
        self._carrying_sheep = False