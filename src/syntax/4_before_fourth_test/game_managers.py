import pygame
import random

# -----------------------------
# INITIAL SETUP
# -----------------------------
pygame.init()

# Window setup
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Game Manager Example")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Clock
clock = pygame.time.Clock()
FPS = 60

# -----------------------------
# SPRITE CLASSES
# -----------------------------
class Player(pygame.sprite.Sprite):
    """Player controlled sprite"""
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Keep player inside window
        if self.rect.left < 0: self.rect.left = 0
        if self.rect.right > WINDOW_WIDTH: self.rect.right = WINDOW_WIDTH
        if self.rect.top < 0: self.rect.top = 0
        if self.rect.bottom > WINDOW_HEIGHT: self.rect.bottom = WINDOW_HEIGHT

class Enemy(pygame.sprite.Sprite):
    """Enemy sprite moves randomly"""
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(random.choice([GREEN, BLUE]))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WINDOW_WIDTH-40)
        self.rect.y = random.randint(0, WINDOW_HEIGHT-40)
        self.speed_x = random.choice([-3, -2, -1, 1, 2, 3])
        self.speed_y = random.choice([-3, -2, -1, 1, 2, 3])

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off walls
        if self.rect.left < 0 or self.rect.right > WINDOW_WIDTH:
            self.speed_x *= -1
        if self.rect.top < 0 or self.rect.bottom > WINDOW_HEIGHT:
            self.speed_y *= -1

# -----------------------------
# GAME MANAGER CLASS
# -----------------------------
class GameManager:
    """
    The GameManager class handles:
    - Initializing the game objects
    - Managing sprite groups
    - Handling game logic
    - Running the main game loop
    """

    def __init__(self):
        # Sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        # Create player
        self.player = Player()
        self.all_sprites.add(self.player)

        # Create multiple enemies
        for _ in range(5):
            enemy = Enemy()
            self.all_sprites.add(enemy)
            self.enemies.add(enemy)

        # Game state
        self.running = True

    def handle_events(self):
        """Handles user input and window events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.speed_x = -5
                if event.key == pygame.K_RIGHT:
                    self.player.speed_x = 5
                if event.key == pygame.K_UP:
                    self.player.speed_y = -5
                if event.key == pygame.K_DOWN:
                    self.player.speed_y = 5
            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    self.player.speed_x = 0
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    self.player.speed_y = 0

    def update(self):
        """Updates all sprites and game logic"""
        self.all_sprites.update()

        # Check collisions with enemies
        if pygame.sprite.spritecollide(self.player, self.enemies, False):
            print("Player hit an enemy!")

    def draw(self):
        """Draws everything on the screen"""
        screen.fill(WHITE)
        self.all_sprites.draw(screen)
        pygame.display.flip()

    def run(self):
        """The main game loop"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            clock.tick(FPS)

# -----------------------------
# RUN GAME
# -----------------------------
if __name__ == "__main__":
    # Using GameManager centralizes game control and keeps main loop clean
    game = GameManager()
    game.run()
    pygame.quit()
