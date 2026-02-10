import pygame
import random  # For random positions and colors

# Initialize Pygame
pygame.init()

# -----------------------------
# SETUP WINDOW
# -----------------------------
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pygame Sprite Features Example")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Clock to control FPS
clock = pygame.time.Clock()
FPS = 60

# -----------------------------
# SPRITE CLASSES
# -----------------------------

# PLAYER SPRITE
class Player(pygame.sprite.Sprite):
    """A controllable player sprite that can move with arrow keys."""
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        # Move player
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Keep inside the screen
        if self.rect.left < 0: self.rect.left = 0
        if self.rect.right > WINDOW_WIDTH: self.rect.right = WINDOW_WIDTH
        if self.rect.top < 0: self.rect.top = 0
        if self.rect.bottom > WINDOW_HEIGHT: self.rect.bottom = WINDOW_HEIGHT

# ENEMY SPRITE
class Enemy(pygame.sprite.Sprite):
    """A simple enemy sprite that moves randomly."""
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.color = random.choice([GREEN, BLUE])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WINDOW_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, WINDOW_HEIGHT - self.rect.height)
        self.speed_x = random.choice([-3, -2, -1, 1, 2, 3])
        self.speed_y = random.choice([-3, -2, -1, 1, 2, 3])

    def update(self):
        # Move enemy
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off screen edges
        if self.rect.left < 0 or self.rect.right > WINDOW_WIDTH:
            self.speed_x *= -1
        if self.rect.top < 0 or self.rect.bottom > WINDOW_HEIGHT:
            self.speed_y *= -1

# POWER-UP SPRITE
class PowerUp(pygame.sprite.Sprite):
    """A power-up sprite that changes color over time."""
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.color_index = 0
        self.colors = [RED, GREEN, BLUE]
        self.image.fill(self.colors[self.color_index])
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WINDOW_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, WINDOW_HEIGHT - self.rect.height)

    def update(self):
        # Change color every frame (animation)
        self.color_index += 1
        if self.color_index >= len(self.colors):
            self.color_index = 0
        self.image.fill(self.colors[self.color_index])

# -----------------------------
# SPRITE GROUPS
# -----------------------------
all_sprites = pygame.sprite.Group()  # All sprites
enemies = pygame.sprite.Group()      # Enemy sprites
powerups = pygame.sprite.Group()     # Power-up sprites

# Create player
player = Player()
all_sprites.add(player)

# Create multiple enemies
for _ in range(5):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# Create multiple power-ups
for _ in range(3):
    powerup = PowerUp()
    all_sprites.add(powerup)
    powerups.add(powerup)

# -----------------------------
# MAIN GAME LOOP
# -----------------------------
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speed_x = -5
            if event.key == pygame.K_RIGHT:
                player.speed_x = 5
            if event.key == pygame.K_UP:
                player.speed_y = -5
            if event.key == pygame.K_DOWN:
                player.speed_y = 5
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player.speed_x = 0
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                player.speed_y = 0

    # Update all sprites
    all_sprites.update()

    # Check for collisions
    # Player collects power-ups
    collected = pygame.sprite.spritecollide(player, powerups, True)  # True = remove collected
    if collected:
        print(f"Collected {len(collected)} power-up(s)!")

    # Player hits enemy
    hit_enemies = pygame.sprite.spritecollide(player, enemies, False)  # False = don't remove enemies
    if hit_enemies:
        print("Player hit an enemy!")

    # Draw everything
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

    # Limit frame rate
    clock.tick(FPS)

pygame.quit()
