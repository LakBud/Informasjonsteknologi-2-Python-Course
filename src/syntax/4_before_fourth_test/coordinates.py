import pygame as pg
import random as rnd
# A coordinate is a point with a x which determines horizontally and y which determines vertically
# * coordinate = (x,y)

pg.init()

# Example
WIDTH, HEIGHT = 800, 600
window = pg.display.set_mode((WIDTH, HEIGHT))

clock = pg.time.Clock() 


# ? How to draw a circle with coordinates:
# * pygame.draw.circle(surface, color, center, radius, width=0)

# 	• surface: where we will draw the circle in our window
# 	• color: color to the element, used with a color tuple. (400, 600) is an example
# 	• center: where the center of the element should be. (x, y)
# 	• radius: Radius to the circle
# 	• width: The width of the round circle (default = 0)

# Ball position and speed
ball_x = 400
ball_y = 300
speed_x = 5
speed_y = 5


ball_color = (255,0,0)
active = True
radius = 20

while active:
    for action in pg.event.get(): 
        if action.type == pg.QUIT: 
            active = False
    
    # Fill the background with black to clear old frames
    window.fill((0, 0, 0))
    
    # Draw the circle at the current position
    pg.draw.circle(window, ball_color, (ball_x, ball_y), radius) 
    pg.display.flip()

    # Move the ball
    ball_x += speed_x
    ball_y += speed_y
    
    
    # Bounce off the left/right walls
    if ball_x - radius <= 0 or ball_x + radius >= WIDTH:
        speed_x = -speed_x + rnd.uniform(-1, 1)

    # Bounce off the top/bottom walls
    if ball_y - radius <= 0 or ball_y + radius >= HEIGHT:
        speed_y = -speed_y + rnd.uniform(-1, 1)
    
    
    
    # Limit FPS
    clock.tick(60)