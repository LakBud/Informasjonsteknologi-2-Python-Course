import pygame as pg
import math as m


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
        pg.draw.circle(self._window, self._color, (int(self._x), int(self._y)), self._radius)
    
    def move(self, key_pressed = None):
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

    # AI-generated code meant for the task
    def detect_collision(self, other):
        dx = other._x - self._x
        dy = other._y - self._y
        distance = m.hypot(dx, dy)

        # Check collision
        if distance <= self._radius + other._radius and distance != 0:
            # Normal vector
            nx = dx / distance
            ny = dy / distance

            # Tangent vector
            tx = -ny
            ty = nx

            # Dot product tangent
            dpTan1 = self._speed_x * tx + self._speed_y * ty
            dpTan2 = other._speed_x * tx + other._speed_y * ty

            # Dot product normal
            dpNorm1 = self._speed_x * nx + self._speed_y * ny
            dpNorm2 = other._speed_x * nx + other._speed_y * ny

            # Swap normal velocities (equal mass, elastic)
            self._speed_x = tx * dpTan1 + nx * dpNorm2
            self._speed_y = ty * dpTan1 + ny * dpNorm2
            other._speed_x = tx * dpTan2 + nx * dpNorm1
            other._speed_y = ty * dpTan2 + ny * dpNorm1

            # Prevent overlap
            overlap = 0.5 * (self._radius + other._radius - distance + 1)
            self._x -= overlap * nx
            self._y -= overlap * ny
            other._x += overlap * nx
            other._y += overlap * ny



class MovingBall(Ball):
    def __init__(self, window, start_x, start_y, radius, color, speed_x, speed_y):
        super().__init__(window, start_x, start_y, radius, color, speed_x, speed_y)
    
    def move(self):
        self._x += self._speed_x
        self._y += self._speed_y
        
        width, height = self._window.get_size()
        
        if self._x - self._radius <= 0 or self._x + self._radius >= width:
            self._speed_x = -self._speed_x

        if self._y - self._radius <= 0 or self._y + self._radius >= height:
            self._speed_y = -self._speed_y 





pg.init()

WIDTH, HEIGHT = 800, 600
window = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()


ball_x = WIDTH / 2
ball_y = HEIGHT / 2
speed_x = 5
speed_y = 5
radius = 20

active = True

# Create ball objects
ball1 = Ball(window, ball_x, ball_y, radius, (54, 0, 122), speed_x, speed_y)
ball2 = Ball(window, ball_x - 30, ball_y + 40, radius, (255, 15, 0), speed_x + 30, speed_y)
ball3 = Ball(window, ball_x + 10, ball_y + 100, 30, (122, 100, 40), speed_x + 10, speed_y + 10)

ball4 = MovingBall(window, ball_x + 40, ball_y + 100, 30, (120, 10, 20), speed_x, speed_y)
ball5 = MovingBall(window, ball_x + 10, ball_y + 5, 30, (120, 255, 20), speed_x, speed_y)



balls: list[Ball] = [ball1, ball2, ball3, ball4, ball5]

while active:
    for action in pg.event.get():
        if action.type == pg.QUIT:
            active = False
            
    window.fill((255, 255, 255))
    
    
    for b in balls:
        b.draw()
        if isinstance(b, MovingBall):
            b.move()
        else:
            b.move(pg.key.get_pressed())  

    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            balls[i].detect_collision(balls[j])


    pg.display.flip()
    
    clock.tick(60)

pg.quit()
