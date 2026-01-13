import pygame as pg

pg.init() # ! Initializes the program

window = pg.display.set_mode((800, 600)) # * Sets the dimension of the screen

# ? Color screen customization (max=255)
# window.fill((255,0,0)) # fills the window with a red color
# window.fill((0,255,0)) # fills the window with a green color
# window.fill((0,0,255)) # fiils the window with a blue color

clock = pg.time.Clock() # * This is used to set the updating frequency of the window

active = True # ! We use a boolean to hold the game

# ? We use a while loop to run the game
while active:
    for action in pg.event.get(): # This loops over every action the user can do
        # If the user closes the window, close the game too
        if action.type == pg.QUIT: 
            active = False
    
    window.fill((255,255,255)) # Creates a white color
    pg.display.flip() # ! Updates the screen
    clock.tick(20) # 20 times in a second
    
pg.quit() # Quits the program when the while loop stops