import pygame as pg
import random as rnd

# Grunnen for at meste parten er engelsk er fordi min setup var i dette språket og har ikke nok tid til å gjøre det om til norsk.


class GameBoard:
    def __init__(self, width: int, height: int):
        self.height = height
        self.width = width
        self._objects = []

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
    
    def move(self, dx: int, dy: int) -> None:
        self.rect.x += dx
        self.rect.y += dy


class Romskip(GameObject):
    def __init__(self, window, start_coord, width_obj, height_obj, color, obj_font, speed):
        super().__init__(window, start_coord, width_obj, height_obj, color, obj_font, letter="R")
        self._default_speed = speed
        self._speed = speed
    
    def move(self, keys) -> None:
        if keys[pg.K_LEFT]:
            super().move(-self._speed, 0)
        elif keys[pg.K_RIGHT]:
            super().move(self._speed, 0)
        elif keys[pg.K_UP]:
            super().move(0, -self._speed)
        elif keys[pg.K_DOWN]:
            super().move(0, self._speed)
        
    
    def expand(self, start_coord):
        self._width += 5 # 10 ble for mye
        self._height += 5 # 10 ble for mye
        
        
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




class Meteor(GameObject):
    def __init__(self, window, start_coord, width_obj, height_obj, color, obj_font, speed):
        super().__init__(window, start_coord, width_obj, height_obj, color, obj_font, letter="M")
        self._speed = speed
        
        # Random diagonal direction
        self.dx = rnd.choice([-speed, speed])
        self.dy = rnd.choice([-speed, speed])
        
    def move(self, board: GameBoard) -> None:
        self.rect.x += self.dx 
        self.rect.y += self.dy 
        
        # Border collision
        if self.rect.left <= 0:
            self.rect.left = WIDTH


        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
            
        if self.rect.top <= 0 or self.rect.bottom >= board.height:
            self.dy *= -1
            
            
# Global Variables
WIDTH = 1500
HEIGHT = 1000
FPS = 60

class GameManager:
    def __init__(self):
        # Pygame setup
        pg.init()
        self._screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Manic Mansion")
        self._clock = pg.time.Clock()
        self._font = pg.font.SysFont(None, 50)
        self._board = GameBoard(WIDTH, HEIGHT)
        
        # Lists
        self._all_sprites: list[GameObject] = []
        self._meteors: list[Meteor] = []
        
        # Game variables
        self.active = True
        self._score = 0
        self._game_over = False
        
        # Spawn Start Objects
        self._create_start_objects()

    def handle_events(self) -> None:
        """Handle user input and quitting."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.active = False
    
    def _create_start_objects(self) -> None:
        # Player
        start_x = WIDTH // 2
        start_y = HEIGHT // 2
        
        self._player: Romskip = Romskip(self._screen, (start_x, start_y), 60, 60, (120, 0, 0), self._font, 10)
        self._all_sprites.append(self._player)
        
        for _ in range(31):
            # meteors
            m_pos = self._board.random_position_in_zone(
                0, 
                HEIGHT,
                obj_width=30,
                obj_height=30
                )
            
            m_color = rnd.choice([(0, 255, 0), (255, 0, 0)])
            
            meteor = Meteor(self._screen, m_pos, 10, 10, m_color, self._font, 3)
            self._board.add_object(meteor)
            self._all_sprites.append(meteor)
            self._meteors.append(meteor)
    
    def draw(self) -> None:
        """Draw everything to the _screen."""
        self._screen.fill((0, 0, 0))
        
        if not self._game_over:
            # Draw all sprites
            for sprites in self._all_sprites:
                sprites.draw()
            
            # Active Score Text
            score_text = self._font.render(f"Score: {self._score}", True, (255, 255, 255), (0, 0, 0))
            self._screen.blit(score_text, (20, 20))
            
        else:
            # Game over Text
            game_over_text = self._font.render("GAME OVER", True, (255, 0, 0))
            text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            self._screen.blit(game_over_text, text_rect)

            # Total Score Text
            score_text = self._font.render(f"Score: {self._score}", True, (255, 255, 255))
            score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
            self._screen.blit(score_text, score_rect)
        
        pg.display.flip()

    def update(self) -> None:
        keys = pg.key.get_pressed()
        
        # Allow player movement inside the border
        self._player.move(keys)
        
        
        # Move meteors
        for meteor in self._meteors:
            meteor.move(self._board)
        
        for meteor in self._meteors[:]:
            if self._player.collides_with(meteor):
                if meteor._color == (0, 255, 0):
                    self._score += 10
                    self._meteors.remove(meteor)
                    self._all_sprites.remove(meteor)
                    self._player.expand(self._player.rect.center)
                # elif meteor._color == (255, 0, 0):
                #     self._game_over = True


    def run(self): 
        """Main game loop."""
        while self.active:
            self._clock.tick(FPS)
            self.handle_events()
            self.draw()
            if not self._game_over:
                self.update()
        pg.quit()


# Entry point
if __name__ == "__main__":
    game = GameManager()
    game.run()