import pygame as pg
import random as rnd

# OOP is important for pygame

class Ball:
    def __init__(self, window, start_x: int, start_y: int, radius: int, color: tuple, speed_x: float, speed_y: float):
        self._window = window
        self._x = start_x
        self._y = start_y
        self._radius = radius
        self._color = color
        self._speed_x = speed_x
        self._speed_y = speed_y
    
    def draw(self):
        pg.draw.circle(self._window, self._color, (int(self._x), (self._y)), self._radius)
    
    def move(self, key_pressed):
        if key_pressed[pg.K_LEFT]:
            self._x -= self._speed_x
        
        if key_pressed[pg.K_RIGHT]:
            self._x += self._speed_x
        
        if key_pressed[pg.K_UP]:
            self._y -= self._speed_y
        
        if key_pressed[pg.K_DOWN]:
            self._y += self._speed_y
        
        width, height = self._window.get_size()

        if self._y + self._radius > height:
            self._y = height - self._radius
        elif self._y - self._radius < 0:
            self._y = self._radius

        if self._x + self._radius > width:
            self._x = width - self._radius
        elif self._x - self._radius < 0:
            self._x = self._radius

class MovingBall(Ball):
    def __init__(self, window, start_x, start_y, radius, color, speed_x, speed_y):
        super().__init__(window, start_x, start_y, radius, color, speed_x, speed_y)
    
    def move(self):
        self._x += self._speed_x
        self._y += self._speed_y
        
        width, height = self._window.get_size()
        
        # Bounce off the left/right walls
        if self._x - self._radius <= 0 or self._x + self._radius >= width:
            self._speed_x = -self._speed_x + rnd.uniform(-1, 1)

        # Bounce off the top/bottom walls
        if self._y - self._radius <= 0 or self._y + self._radius >= height:
            self._speed_y = -self._speed_y + rnd.uniform(-1, 1)


# Start the Program
pg.init()

WIDTH, HEIGHT = 800, 600
window = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock() 


# Ball position and speed
ball_x = WIDTH / 2
ball_y = HEIGHT / 2
speed_x = 5
speed_y = 5

active = True
radius = 20

ball1 = Ball(window, ball_x, ball_y, radius, (255, 0, 0), speed_x, speed_y)
ball2 = Ball(window, ball_x + 10, ball_y + 100, 30, (255, 255, 0), speed_x + 25, speed_y + 20)

ball3 = MovingBall(window, ball_x + 40, ball_y + 100, 30, (120, 255, 20), speed_x, speed_y)

while active:
    for action in pg.event.get(): 
        if action.type == pg.QUIT: 
            active = False
            
    window.fill((255, 255, 255))
    
    ball1.draw()
    ball2.draw()
    ball1.move(pg.key.get_pressed())
    ball2.move(pg.key.get_pressed())
    
    ball3.draw()
    ball3.move()
    
    pg.display.flip()
    
    
    # Limit FPS
    clock.tick(60)

pg.quit()