import pygame as pg
import random as rnd
from itertools import combinations

# -----------------------------
# Global settings
# -----------------------------
WIDTH = 800
HEIGHT = 600
FPS = 60
RUNNING = True
game_over = False  # <- Legger til Game Over flagg

# -----------------------------
# Base Sprite class (Square)
# -----------------------------
class Square(pg.sprite.Sprite):
    def __init__(self, window, size, color, start_pos, speed):
        super().__init__()
        self.window = window
        self.size = size
        self.color = color
        self.speed = speed
        self.image = pg.Surface((self.size, self.size))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=start_pos)

    def update(self):
        pass

# -----------------------------
# Enemy Sprite
# -----------------------------
class Enemy(Square):
    def __init__(self, window, size, color, start_pos, speed):
        super().__init__(window, size, color, start_pos, speed)
        self.dir_x = rnd.choice([-2, -1, 1, 2])
        self.dir_y = rnd.choice([-2, -1, 1, 2])

    def update(self):
        self.rect.x += self.dir_x * self.speed
        self.rect.y += self.dir_y * self.speed

        # Bounce off window edges
        if self.rect.left <= 0 or self.rect.right >= self.window.get_width():
            self.dir_x *= -1
        if self.rect.top <= 0 or self.rect.bottom >= self.window.get_height():
            self.dir_y *= -1

# -----------------------------
# Player Sprite
# -----------------------------
class Player(Square):
    def __init__(self, window, size, color, start_pos, speed):
        super().__init__(window, size, color, start_pos, speed)

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pg.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pg.K_UP]:
            self.rect.y -= self.speed
        if keys[pg.K_DOWN]:
            self.rect.y += self.speed
        self.rect.clamp_ip(self.window.get_rect())

# -----------------------------
# Pygame setup
# -----------------------------
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
font = pg.font.SysFont(None, 72)

# -----------------------------
# Sprite Groups
# -----------------------------
all_sprites = pg.sprite.Group()
enemies = pg.sprite.Group()

# -----------------------------
# Create Enemy
# -----------------------------
for _ in range(10):
    start_pos = (rnd.randint(0, 100), rnd.randint(0, 100))
    enemy = Enemy(screen, size=25, color=(0, 0, 255), start_pos=start_pos, speed=rnd.randint(3, 6))
    all_sprites.add(enemy)
    enemies.add(enemy)

# -----------------------------
# Create Player
# -----------------------------
player = Player(screen, size=25, color=(0, 255, 0), start_pos=(WIDTH//2, HEIGHT//2), speed=4)
all_sprites.add(player)

# -----------------------------
# Game Loop
# -----------------------------
while RUNNING:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            RUNNING = False

    if not game_over:
        all_sprites.update()

        # -----------------------------
        # Player-Enemy collision
        # -----------------------------
        if pg.sprite.spritecollide(player, enemies, False):
            game_over = True

        # -----------------------------
        # Enemy-Enemy collision
        # -----------------------------
        for e1, e2 in combinations(enemies, 2):
            if e1.rect.colliderect(e2.rect):
                e1.dir_x *= -1
                e1.dir_y *= -1
                e2.dir_x *= -1
                e2.dir_y *= -1

    # -----------------------------
    # Draw
    # -----------------------------
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)

    if game_over:
        text = font.render("GAME OVER", True, (255, 0, 0))
        rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(text, rect)

    pg.display.flip()
    clock.tick(FPS)

pg.quit()
