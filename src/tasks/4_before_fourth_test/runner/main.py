import pygame as pg
import random as rnd
from classes import Player, Enemy

# Global Variables
WIDTH = 1600
HEIGHT = 800
FPS = 60


class GameManager:
    def __init__(self):
        # PyGame setup
        pg.init()
        self._screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Runner")
        self._clock = pg.time.Clock()
        self._font = pg.font.SysFont(None, 50)
        
        # Ground settings
        self._ground_height = 300
        self._ground_rect = pg.Rect(0, HEIGHT - self._ground_height, WIDTH, self._ground_height)
        
        # Lists
        self._all_sprites = []
        self._enemies = []
        
        # Player
        p_height = 60
        p_width = 60
        self._player = Player(self._screen, (WIDTH // 7, HEIGHT - p_height // 2 - self._ground_height), p_width, p_height, (255, 0, 0), self._font)
        self._all_sprites.append(self._player)
        
        # Spawn timer
        self.SPAWN_ENEMY = pg.USEREVENT + 1
        pg.time.set_timer(self.SPAWN_ENEMY, 1500)  # spawn every 1.5 seconds
        
        
        # Game variables
        self.active = True
        self._score = 0
        self._game_over = False
    
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.active = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self._player.jump()
                if event.key == pg.K_DOWN:
                    self._player.crouch()

            if event.type == pg.KEYUP:
                if event.key == pg.K_DOWN:
                    self._player.stand()
            
            if event.type == self.SPAWN_ENEMY and not self._game_over:
                self.spawn_enemy()
    
    
    def spawn_enemy(self):
        enemy_width = 50
        enemy_height = 50

        enemy = Enemy(
            self._screen,
            (WIDTH + enemy_width, HEIGHT - self._ground_height - enemy_height // 2 + rnd.randint(-100, 0)),
            enemy_width,
            enemy_height,
            (0, 0, 255),
            self._font,
            speed=6
        )

        self._enemies.append(enemy)
        self._all_sprites.append(enemy)
    
    def draw(self):
        self._screen.fill((0, 0, 0))
        
        if not self._game_over:
            # Ground
            pg.draw.rect(self._screen, (0, 200, 0, 0), self._ground_rect)
            
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
            
            # Final Score Text
            score_text = self._font.render(f"Score: {self._score}", True, (255, 255, 255), (0, 0, 0))
            score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
            self._screen.blit(score_text, score_rect)
        
        pg.display.flip()
    
    def update(self):
        self._player.update(self._ground_rect)
        self._score += 1
        
        for enemy in self._enemies:
            enemy.update()
            
            if self._player.collides_with(enemy):
                self._game_over = True
            
            # Score when enemy passes player
            if not enemy.passed and enemy.rect.right < self._player.rect.left:
                enemy.passed = True
                enemy.increase_speed(1)  # if you have this method
        
        for enemy in self._enemies[:]:
            if enemy.off_screen():
                self._enemies.remove(enemy)
    
    def run(self):
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