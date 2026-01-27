import pygame as pg
import random as rnd
from classes import Player, Alien

# Global Variables
WIDTH = 1600
HEIGHT = 1000
FPS = 60


def main():
    # Game Variables
    active = True
    score = 0

    # Player settings
    start_pos: tuple[int, int] = (WIDTH // 2, HEIGHT // 2)
    player_color: tuple[int, int, int] = (0, 0, 255) 
    player_width: int = 100
    player_height: int = 100
    player_speed: int = 20 

    # Enemy configuration
    spawn_timer = 0
    spawn_interval = rnd.randint(30, 60)

    alien_height: int = rnd.randint(50, 100)
    alien_width: int = rnd.randint(60, 100)
    alien_color: tuple[int, int, int] = (0, 255, 0)
    alien_speed: int = rnd.randint(3, 15)


    # Start 
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    font = pg.font.SysFont(None, 50)
    
    # Load and scale the background image
    background_img = pg.image.load("images/4/IT2-background.png").convert()
    background_img = pg.transform.scale(background_img, (WIDTH, HEIGHT))

    player = Player(screen, start_pos, player_width, player_height, player_color, player_speed)


    aliens = []

    # Game Loop (Primary)
    while active:
        for action in pg.event.get():
            # Quit functionality
            if action.type == pg.QUIT:
                active = False
            # Checks if a key has been pressed, and if its space bar then shoot
            elif action.type == pg.KEYDOWN:
                if action.key == pg.K_SPACE:
                    player.shoot()

        
        # Black Background
        screen.blit(background_img, (0, 0))
        
        # Enter the user
        player.move()
        player.draw()
        player.activate_border_collision()
        
        # Enter the aliens
        for alien in aliens:
            alien.draw()
            alien.move()
            
            if alien.collides_with(player):
                active = False
            
        # Remove aliens that passed the screen
        for alien in aliens[:]:
            if alien.rect.bottom > HEIGHT:
                aliens.remove(alien)
                score -= 1
                
        # Enter the bullets + checking for removal
        for bullet in player.bullets[:]:
            bullet.move()
            bullet.draw()
            
            if bullet.rect.bottom < 0:
                player.bullets.remove(bullet)
                continue  # Skip to next bullet

            for alien in aliens[:]:
                if bullet.collides_with(alien):
                    player.bullets.remove(bullet)
                    aliens.remove(alien)
                    score += 1
                    break  # Stop checking this bullet

        # Score display
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        
        # Increment a frame counter and spawn a new alien when it reaches the interval then reset the counter
        spawn_timer += 1
        if spawn_timer >= spawn_interval:
            aliens.append(Alien(screen, alien_height, alien_width, alien_color, alien_speed))
            spawn_timer = 0


        # Update the screen
        pg.display.flip()
        clock.tick(FPS)

# This checks if the file is being run while its open
if __name__ == "__main__":
    main()
