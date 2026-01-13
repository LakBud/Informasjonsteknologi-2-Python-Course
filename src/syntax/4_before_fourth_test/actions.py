import pygame as pg

# You can decide actions within the program using the library pygame


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

while active:
    for action in pg.event.get(): 
        if action.type == pg.QUIT: 
            active = False
    

    window.fill((0, 0, 0))
    

    pg.draw.circle(window, (255,0,0), (ball_x, ball_y), radius) 
    pg.display.flip()
    
    # This variable gets information if a key has been pressed
    key_pressed = pg.key.get_pressed()
    
    # ! Here it takes the key arrows, checks which one is entered and moves the ball accordingly
    if key_pressed[pg.K_LEFT]:
        ball_x -= speed_x # Left is negative x value
    if key_pressed[pg.K_RIGHT]:
        ball_x += speed_x # Right is postive x value
    if key_pressed[pg.K_UP]:
        ball_y -= speed_y # Up is negative y value
    if key_pressed[pg.K_DOWN]:
        ball_y += speed_y # Down is positive x value


    if ball_y + radius > HEIGHT:
        ball_y = HEIGHT - radius
    elif ball_y - radius < 0:
        ball_y = radius
        
        
    if ball_x + radius > WIDTH:
        ball_x = WIDTH - radius
    elif ball_x - radius < 0:
        ball_x = radius
    
    
    # Limit FPS
    clock.tick(60)