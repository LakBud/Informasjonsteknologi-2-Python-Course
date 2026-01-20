import pygame as pg

class Player:
    def __init__(self, window: object, start_coord: tuple[float], width_obj: int, height_obj: int, color: tuple[int], speed: int):
        self._window = window
        self._x = start_coord[0]
        self._y = start_coord[1]
        self._width = width_obj
        self._height = height_obj
        self._color = color
        self._speed = speed
    
    
    def draw(self):
        square = pg.Surface((self._width, self._height)) # This draws a square with its width and height
        square.fill(self._color) # Fills the shape with a color
        self._window.blit(square, (self._x, self._y)) # This updates the pixels of the square with its x and y coords
    
    def move(self):
        key_pressed = pg.key.get_pressed()
        
        if key_pressed[pg.K_LEFT]:
            self._x -= self._speed
            
        if key_pressed[pg.K_RIGHT]:
            self._x += self._speed
        
        if key_pressed[pg.K_UP]:
            self._y -= self._speed
            
        if key_pressed[pg.K_DOWN]:
            self._y += self._speed


# Global Variables
WIDTH = 800
HEIGHT = 600
FPS = 60
active = True

# Player settings
start_pos: tuple[int] = (WIDTH // 2, HEIGHT // 2)
player_color: tuple[int] = (0, 0, 255) # Blue
player_width: int = 20
player_height: int = 20



# Start
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

test_player = Player(screen, start_pos, player_width, player_height, player_color, 10)

# Game Loop (Primary)
while active:
    # Checks if the user wants to end the program
    for hendelse in pg.event.get():
        if hendelse.type == pg.QUIT:
            active = False
            
    # Draw background and users
    screen.fill((255, 255, 255))
    test_player.draw()
    test_player.move()
    
    
    
    # Keep the player's x position within the screen width
    test_player._x = max(0, min(test_player._x, WIDTH - test_player._width))

    # Keep the player's y position within the screen height
    test_player._y = max(0, min(test_player._y, HEIGHT - test_player._height))

    
    # Update the screen
    pg.display.flip()
    clock.tick(FPS)
