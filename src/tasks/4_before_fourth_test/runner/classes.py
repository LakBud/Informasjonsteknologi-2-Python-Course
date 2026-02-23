import pygame as pg

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
        self.rect = self.image.get_rect(center=(start_coord))
        
        # Render the letter
        letter_surface = self._font.render(self._letter, True, (0, 0, 0))
        letter_square = letter_surface.get_rect(center=(self._width // 2, self._height // 2))
        
        # Draw the letter
        self.image.blit(letter_surface, letter_square)
    
    def draw(self) -> None:
        self._window.blit(self.image, self.rect)
    
    def collides_with(self, other_obj) -> bool:
        return self.rect.colliderect(other_obj.rect)
    

class Player(GameObject):
    def __init__(self, window, start_coord, width_obj, height_obj, color, obj_font):
        super().__init__(window, start_coord, width_obj, height_obj, color, obj_font, letter="P")
        
        # Jump physics
        self.velocity_y = 0
        self.gravity = 0.6
        self.jump_strength = -15
        self.on_ground = False

        # Crouch settings
        self.normal_height = height_obj
        self.crouch_height = height_obj // 2
        self.is_crouching = False

    def jump(self):
        if self.on_ground and not self.is_crouching:
            self.velocity_y = self.jump_strength
            self.on_ground = False

    def rebuild_image(self, height):
        bottom = self.rect.bottom

        self.image = pg.Surface((self.rect.width, height))
        self.image.fill(self._color)

        # Re-center letter using CURRENT image size
        letter_surface = self._font.render(self._letter, True, (0, 0, 0))
        letter_square = letter_surface.get_rect(
            center=(self.image.get_width() // 2, self.image.get_height() // 2)
        )
        self.image.blit(letter_surface, letter_square)

        self.rect = self.image.get_rect(midbottom=(self.rect.centerx, bottom))


    def crouch(self):
        if not self.is_crouching and self.on_ground:
            self.is_crouching = True
            self.rebuild_image(self.crouch_height)


    def stand(self):
        if self.is_crouching:
            self.is_crouching = False
            self.rebuild_image(self.normal_height)

    def update(self, ground_rect):
        # Apply gravity
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        # Ground collision
        if self.rect.bottom >= ground_rect.top:
            self.rect.bottom = ground_rect.top
            self.velocity_y = 0
            self.on_ground = True


class Enemy(GameObject):
    def __init__(self, window, start_coord, width_obj, height_obj, color, obj_font, speed):
        super().__init__(window, start_coord, width_obj, height_obj, color, obj_font, letter="E")
        self._speed = speed
        self.passed = False

    def update(self):
        # Move left
        self.rect.x -= self._speed
    
    def increase_speed(self, increase: int) -> None:
        self._speed -= increase

    def off_screen(self):
        return self.rect.right < 0