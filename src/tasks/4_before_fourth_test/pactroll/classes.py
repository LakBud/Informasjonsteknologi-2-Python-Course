import pygame as pg
from abc import ABC

# ABC makes it a abstract class -> basically no direct creation, only inheritance
class GameObject(ABC):
    def __init__(
        self,
        window,
        start_coord: tuple[int, int],
        width_obj: int,
        height_obj: int,
        color: tuple[int, int, int],
        obj_font,
        letter: str,
    ):
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
        :param obj_font: Description
        :param letter: Description
        :type letter: str
        """

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


# Inheritance classes
class Troll(GameObject):
    def __init__(
        self,
        window,
        start_coord: tuple[int, int],
        width_obj: int,
        height_obj: int,
        color: tuple[int, int, int],
        speed_x: float,
        speed_y: float,
        obj_font,
        letter: str,
    ):
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
        :param speed_x: Description
        :type speed_x: float
        :param speed_y: Description
        :type speed_y: float
        :param obj_font: Description
        :param letter: Description
        :type letter: str
        """

        super().__init__(
            window, start_coord, width_obj, height_obj, color, obj_font, letter
        )
        self._speed_x = speed_x
        self._speed_y = speed_y

    def move(self) -> None:
        # Automatic movement (no keyboard input)
        self._x += self._speed_x
        self._y += self._speed_y

        # Update the surface with the new x and y
        self.rect.center = (self._x, self._y)

    def handle_input(self) -> None:
        keys = pg.key.get_pressed()

        # Use abs() to keep the speed the same size while flipping its sign to change direction
        if keys[pg.K_LEFT]:
            self._speed_x = -abs(self._speed_x)

        if keys[pg.K_RIGHT]:
            self._speed_x = abs(self._speed_x)

        if keys[pg.K_UP]:
            self._speed_y = -abs(self._speed_y)

        if keys[pg.K_DOWN]:
            self._speed_y = abs(self._speed_y)

    def update_speed(self, increment: float = 1E-4) -> None:
        # Increases the speed based on the direction
        self._speed_x += increment if self._speed_x > 0 else -increment
        self._speed_y += increment if self._speed_y > 0 else -increment


class Food(GameObject):
    def __init__(
        self,
        window,
        start_coord: tuple[int, int],
        width_obj: int,
        height_obj: int,
        color: tuple[int, int, int],
        obj_font,
        letter: str,
    ):
        super().__init__(
            window, start_coord, width_obj, height_obj, color, obj_font, letter
        )


class Obstacle(GameObject):
    def __init__(
        self,
        window,
        start_coord: tuple[int, int],
        width_obj: int,
        height_obj: int,
        color: tuple[int, int, int],
        obj_font,
        letter: str,
    ):
        super().__init__(
            window, start_coord, width_obj, height_obj, color, obj_font, letter
        )
