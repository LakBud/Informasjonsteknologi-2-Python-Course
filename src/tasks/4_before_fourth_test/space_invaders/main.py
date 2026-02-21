import pygame as pg
import random as rnd
from classes import Player, GameObject, Bullet, Enemy, Fortification, UFO
from config import *

class GameManager:
    def __init__(self):
        # Pygame setup
        pg.init()
        self._screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Space Invaders")
        self._clock = pg.time.Clock()
        self._font = pg.font.SysFont(None, 50)
        
        # Lists
        self._all_sprites: list[GameObject] = []
        self._all_enemies: list[Enemy] = []
        self._player_bullets: list[Bullet] = []
        self._enemy_bullets: list[Bullet] = []
        self._fortifications: list[Fortification] = []
        self._ufos: list[UFO] = []
        
        # Player
        self._player = Player(self._screen, P_START_COORD, P_WIDTH, P_HEIGHT, P_DEFAULT_COLOR, P_SPEED)
        self._all_sprites.append(self._player)
        
        
        # Enemy Bullet Cooldown
        self._last_enemy_shot = 0  # time (in seconds) when the last enemy shot
        self._enemy_shot_cooldown = 1.5  # how many seconds to wait between shots
        
        # Game variables
        self.active = True
        self._score = 0
        self._game_over = False
        
        # Spawn Enemies & Forts
        self.spawn_enemies()
        self.spawn_fortifications()

    def handle_events(self) -> None:
        """Handle user input and quitting."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.active = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    # Shoot a bullet
                    player_bullet = Bullet(self._screen, (self._player.rect.centerx, self._player.rect.top), PB_WIDTH, PB_HEIGHT, PB_DEFAULT_COLOR, PB_SPEED, PB_IMAGE_PATH)
                    self._player_bullets.append(player_bullet)
                    self._all_sprites.append(player_bullet)
    
    
    def spawn_enemies(self) -> None:
        self._enemy_columns: list[list[Enemy]] = [[] for _ in range(E_COLS)]

        for row in range(E_ROWS):
            for col in range(E_COLS):
                x = E_START_X + col * E_SPACING_X
                y = E_START_Y + row * E_SPACING_Y

                alien = Enemy(self._screen, (x, y), E_WIDTH, E_HEIGHT, E_DEFAULT_COLOR)
                self._all_sprites.append(alien)
                self._all_enemies.append(alien)
                
                # Add to Column
                self._enemy_columns[col].append(alien)
    
    def spawn_fortifications(self) -> None:
        """Spawn 4 Fortifications evenly spaced"""
        
        spacing = self._screen.get_width() // (NUM_FORTS + 1)
        y_position = self._screen.get_height() - 150   # slightly above player
        
        
        for i in range(1, NUM_FORTS + 1):
            x_position = spacing * i 
            
            fort = Fortification(self._screen, (x_position, y_position), F_WIDTH, F_HEIGHT, F_DEFAULT_COLOR)
            
            self._fortifications.append(fort)
            self._all_sprites.append(fort)
    
    
    def enemy_shoot(self) -> None:
        """Choose a random enemy at the bottom to shoot"""
        if not self._all_enemies:
            return 
        
        bottom_enemies: list[Enemy] = []

        for column in self._enemy_columns:
            if column:
                bottom_enemy = max(column, key = lambda e: e.rect.top)
                bottom_enemies.append(bottom_enemy)
            
        if not bottom_enemies:
            return 
        
        shooter = rnd.choice(bottom_enemies)
        
        enemy_bullet = Bullet(self._screen, (shooter.rect.centerx, shooter.rect.bottom), EB_WIDTH, EB_HEIGHT, EB_DEFAULT_COLOR, EB_SPEED, EB_IMAGE_PATH)
        
        self._enemy_bullets.append(enemy_bullet)
        self._all_sprites.append(enemy_bullet)

    def draw(self) -> None:
        """Draw everything to the _screen."""
        self._screen.fill((0, 0, 0))
        
    
        if not self._game_over:
            for sprites in self._all_sprites:
                sprites.draw()
            
            # Active Score Text
            score_text = self._font.render(f"Score: {self._score}", True, (255, 255, 255))
            self._screen.blit(score_text, (20, 20))
            
            # Heart
            heart_width = 20
            heart_height = 30
            spacing = 40
            top_y = 60
            bottom_y = top_y + heart_height

            for i in range(self._player._life_count):
                x = 30 + i * spacing
                points = [
                    (x, bottom_y),                 # bottom-left
                    (x + heart_width / 2, top_y),  # top
                    (x + heart_width, bottom_y)    # bottom-right
                ]
                pg.draw.polygon(self._screen, (255, 0, 0), points)
            
        else:
            # Game over Text
            game_over_text = self._font.render("GAME OVER", True, (255, 0, 0))
            text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            self._screen.blit(game_over_text, text_rect)

            # Total Score Text
            score_text = self._font.render(f"Score: {self._score}", True, (255, 255, 255))
            score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
            self._screen.blit(score_text, score_rect)
        
        pg.display.flip()

    def update(self) -> None:
        for sprites in self._all_sprites:
            sprites.update()
        
        # Spawn enemies again if all enemies are gone
        if not self._all_enemies:
            self.spawn_enemies()
        
        
        # Check Enemy Border Collision
        hit_edge = False
        
        for enemy in self._all_enemies:
            if enemy.rect.right >= WIDTH or enemy.rect.left <= 0:
                hit_edge = True
            
            if enemy.rect.bottom >= self._player.rect.top:
                self._game_over = True
        
        # Enemy Group Movement
        if hit_edge:
            Enemy.direction *= -1

            # Move all enemies down immediately
            for enemy in self._all_enemies:
                enemy.rect.y += 40
        
        # Bullet Enemy cooldown / spawn-rate
        current_time = pg.time.get_ticks() / 1000  # in seconds
        if current_time - self._last_enemy_shot > self._enemy_shot_cooldown:
            self.enemy_shoot()
            self._last_enemy_shot = current_time
        
        # Player life system
        if self._player._life_count <= 0:
            self._game_over = True
        
        # Player Bullet + Enemy Collision
        for enemy in self._all_enemies[:]:
            for p_bullet in self._player_bullets[:]:
                if enemy.collides_with(p_bullet):
                    self._score += 10
                    
                    self._all_sprites.remove(enemy)
                    self._all_sprites.remove(p_bullet)
                    self._all_enemies.remove(enemy)
                    self._player_bullets.remove(p_bullet)
                    
                    # IMPORTANT: Remove enemy from its column
                    for column in self._enemy_columns:
                        if enemy in column:
                            column.remove(enemy)
                            break
                    
                    Enemy.speed += 0.05 # Increase the speed
                    
                    break
        
        # Fortication Defense
        for fort in self._fortifications[:]:
            if fort._defense_count <= 0:
                self._all_sprites.remove(fort)
                self._fortifications.remove(fort)
        
        
        for p_bullet in self._player_bullets[:]:
            # Out of screen
            if p_bullet.rect.bottom < 0:
                self._all_sprites.remove(p_bullet)
                self._player_bullets.remove(p_bullet)
                continue
            
            # Hit UFO
            for ufo in self._ufos[:]:
                if ufo and p_bullet.collides_with(ufo):
                    self._score += 150
                    
                    self._all_sprites.remove(p_bullet)
                    self._player_bullets.remove(p_bullet)
                    
                    self._ufos.remove(ufo)
                    self._all_sprites.remove(ufo)
                    
            
            # Hit fortification
            for fort in self._fortifications[:]:
                if p_bullet.collides_with(fort):
                    fort._defense_count -= 1
                    
                    self._all_sprites.remove(p_bullet)
                    self._player_bullets.remove(p_bullet)
                    break # Stop checking other forts

        for e_bullet in self._enemy_bullets[:]:
            # Out of screen 
            if e_bullet.rect.top > HEIGHT:
                self._all_sprites.remove(e_bullet)
                self._enemy_bullets.remove(e_bullet)
                continue
            
            # Hit player
            if e_bullet.collides_with(self._player):
                self._player._life_count -= 1
                
                self._all_sprites.remove(e_bullet)
                self._enemy_bullets.remove(e_bullet)
                continue
            
            # Hit Fortification
            for fort in self._fortifications[:]:
                if e_bullet.collides_with(fort):
                    self._all_sprites.remove(e_bullet)
                    self._enemy_bullets.remove(e_bullet)
                    break
            
        # Chance for UFO to spawn
        if not self._ufos and rnd.random() < 0.002:
            new_ufo = UFO(self._screen, 60, 40, (255,0,255), 5)
            self._all_sprites.append(new_ufo)
            self._ufos.append(new_ufo)
        
        # Remove UFO when out of border
        for ufo in self._ufos[:]:
            if ufo.rect.right < 0 or ufo.rect.left > self._screen.get_width():
                self._ufos.remove(ufo)
                
                if ufo in self._all_sprites:
                    self._all_sprites.remove(ufo)
        
        
        
    def run(self): 
        """Main game loop."""
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
