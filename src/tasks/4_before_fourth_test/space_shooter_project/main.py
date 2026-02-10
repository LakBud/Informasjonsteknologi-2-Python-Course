import pygame as pg
import random as rnd
from classes import Player, Alien, Bullet

# Global Variables
WIDTH = 1600
HEIGHT = 1000
FPS = 60

class GameManager:
    def __init__(self):
        # Pygame setup
        pg.init()
        self._screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Space Shooter")
        self._clock = pg.time.Clock()
        self._font = pg.font.SysFont(None, 50)

        # Background
        self._background_img = pg.image.load("images/4/IT2-background.png").convert()
        self._background_img = pg.transform.scale(self._background_img, (WIDTH, HEIGHT))

        # Sprite groups
        self.all_sprites = pg.sprite.Group()
        self.aliens = pg.sprite.Group()
        self.bullets = pg.sprite.Group()

        # Player setup
        start_pos = (WIDTH // 2, HEIGHT // 2)
        self.player = Player(self._screen, start_pos, 100, 100, (0,0,255), 20)
        self.all_sprites.add(self.player)

        # Game variables
        self.active = True
        self.score = 0
        self.spawn_timer = 0
        self.spawn_interval = rnd.randint(30, 60)
        self._game_over = False

    def spawn_alien(self):
        """Spawn a single alien and add it to sprite groups."""
        
        # Alien config
        alien_height = rnd.randint(50, 100)
        alien_width = rnd.randint(60, 100)
        alien_color = (0, 255, 0)
        alien_speed = rnd.randint(3, 15)
        
        alien = Alien(self._screen, alien_height, alien_width, alien_color, alien_speed)
        self.aliens.add(alien)
        self.all_sprites.add(alien)

    def handle_events(self):
        """Handle user input and quitting."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.active = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    # Shoot a bullet
                    bullet = Bullet(self._screen, (self.player.rect.centerx, self.player.rect.top), 10, 20, (255,0,0), -15)
                    self.bullets.add(bullet)
                    self.all_sprites.add(bullet)

    def update(self):
        """Update all game objects and handle collisions."""
        
        if not self._game_over:
            # Update sprites
            self.all_sprites.update()
            self.player.activate_border_collision()

            # Spawn aliens based on timer
            self.spawn_timer += 1
            if self.spawn_timer >= self.spawn_interval:
                self.spawn_alien()
                self.spawn_timer = 0

            # Bullet → Alien collisions
            hits = pg.sprite.groupcollide(self.aliens, self.bullets, True, True)
            self.score += len(hits)

            # Player → Alien collisions
            if pg.sprite.spritecollide(self.player, self.aliens, False):
                self._game_over = True

            # Remove off-_screen aliens
            for alien in self.aliens:
                if alien.rect.top > HEIGHT:
                    alien.kill()
                    self.score -= 1

            # Remove off-_screen bullets
            for bullet in self.bullets:
                if bullet.rect.bottom < 0:
                    bullet.kill()

    def draw(self):
        """Draw everything to the _screen."""
        self._screen.blit(self._background_img, (0, 0))
        self.all_sprites.draw(self._screen)

        # Score display
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self._screen.blit(score_text, (10, 10))
        
        
        if self._game_over:
            text = self.font.render("GAME OVER", True, (255, 255, 255))
            rect = text.get_rect(center = (WIDTH // 2, HEIGHT // 2))
            self._screen.blit(text, rect)

        pg.display.flip()

    def run(self):
        """Main game loop."""
        while self.active:
                self._clock.tick(FPS)
                self.handle_events()
                if not self._game_over:
                    self.update()
                self.draw()
        pg.quit()



# Entry point
if __name__ == "__main__":
    game = GameManager()
    game.run()
