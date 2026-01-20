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

        # You use a try to load the pictures.
        try:
            # Where is where you load it and should convert to alpha ()
            self._original_picture = pg.image.load("src/syntax/4_before_fourth_test/images/IT2-Spaceship1.png").convert_alpha()
            # ? You use tranform.scale(image, (width, heigth)) to determine the size and which picture you are gonna use
            self._picture = pg.transform.scale(self._original_picture, (self._width, self._height))
            
        except FileNotFoundError:
            self._picture = pg.Surface((self._width, self._height))
            self._picture.fill(self._color)
        
        
        # Rect is the outline of the picture, in this case it is a square
        # Rect is useful for access to every side and center to the shapes 
        self._picture_square = self._picture.get_rect()
        self._picture_square.center = start_coord # This makes the center of the picture shape as the start coords

    def draw(self):
        self._window.blit(self._picture, (self._picture_square.x, self._picture_square.y))

    
    def move(self) -> None:
        key_pressed = pg.key.get_pressed()
        
        if key_pressed[pg.K_LEFT]:
            self._picture_square.x -= self._speed
            
        if key_pressed[pg.K_RIGHT]:
            self._picture_square.x += self._speed
        
        if key_pressed[pg.K_UP]:
            self._picture_square.y -= self._speed
            
        if key_pressed[pg.K_DOWN]:
            self._picture_square.y += self._speed
    
    def activate_border_collision(self) -> None:
        if self._picture_square.bottom > self._window.get_height():
            self._picture_square.bottom = self._window.get_height()
        elif self._picture_square.top < 0:
            self._picture_square.top = 0
        

        if self._picture_square.right > self._window.get_width():
            self._picture_square.right = self._window.get_width()
        elif self._picture_square.left < 0:
            self._picture_square.left = 0



# Global Variables
WIDTH = 800
HEIGHT = 600
FPS = 60
active = True

# Player settings
start_pos: tuple[int] = (WIDTH // 2, HEIGHT // 2)
player_color: tuple[int] = (0, 0, 255) # Blue
player_width: int = 100
player_height: int = 100



# Start
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

test_player = Player(screen, start_pos, player_width, player_height, player_color, 10)

# Game Loop (Primary)
while active:
    # Checks if the user wants to end the program
    for action in pg.event.get():
        if action.type == pg.QUIT:
            active = False
    
    # my_font = pg.font.SysFont("Arial", 26)
    # text = my_font.render("Hello", True, (0,0,0))
    # screen.blit(text, (10, 10))
    
    # Draw background
    screen.fill((255, 255, 255))
    
    # Enter the user
    test_player.move()
    test_player.draw()
    test_player.activate_border_collision()
    

    
    # Update the screen
    pg.display.flip()
    clock.tick(FPS)
