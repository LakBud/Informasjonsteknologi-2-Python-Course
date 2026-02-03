import pygame as pg
import random as rnd

# -----------------------------
# Global settings
# -----------------------------
WIDTH = 800
HEIGHT = 600
FPS = 60
RUNNING = True


# -----------------------------
# Base Sprite class (Square)
# -----------------------------
class Square(pg.sprite.Sprite):
    def __init__(self, window, size, color, start_pos, speed):
        """
        ? All sprites must inherit from pg.sprite.Sprite.
        This allows them to be added to Sprite Groups and
        use built-in functions like update() and draw().
        """
        super().__init__()  # ! IMPORTANT: initializes the Sprite system

        self.window = window
        self.size = size
        self.color = color
        self.speed = speed

        # image = the visual appearance of the sprite
        self.image = pg.Surface((self.size, self.size))
        self.image.fill(self.color)

        # rect = position, collision, and movement handling
        # Sprite Groups rely heavily on rect
        self.rect = self.image.get_rect(topleft=start_pos)

    def update(self):
        """
        ? Base update method.
        Sprite Groups call update() automatically every frame.
        Child classes override this.
        """
        pass



# -----------------------------
# Enemy Sprite
# -----------------------------
class Enemy(Square):
    def __init__(self, window, size, color, start_pos, speed):
        super().__init__(window, size, color, start_pos, speed)

        # Random movement direction
        self.dir_x = rnd.choice([-2, -1, 1, 2])
        self.dir_y = rnd.choice([-2, -1, 1, 2])

    def update(self):
        """
        update() is automatically called when:
        group.update() is used.
        """
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
        """
        Player movement belongs in update(),
        so Sprite Groups can control it.
        """
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pg.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pg.K_UP]:
            self.rect.y -= self.speed
        if keys[pg.K_DOWN]:
            self.rect.y += self.speed

        # Keep player inside the screen
        self.rect.clamp_ip(self.window.get_rect())


# -----------------------------
# Pygame setup
# -----------------------------
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

# -----------------------------
# Sprite Groups
# -----------------------------
"""
? Sprite Groups:
- store sprites
- call update() automatically
- draw all sprites in one line
"""
all_sprites = pg.sprite.Group()
enemies = pg.sprite.Group()

# -----------------------------
# Create Enemy
# -----------------------------

for _ in range(10):
    start_pos = (rnd.randint(0, 100), rnd.randint(0, 100))
    enemy = Enemy(
        screen,
        size=25,
        color=(0, 0, 255),
        start_pos=start_pos,
        speed=rnd.randint(5, 10)
    )
    
    all_sprites.add(enemy)
    enemies.add(enemy)


# -----------------------------
# Create Player
# -----------------------------
player = Player(
    screen,
    size=25,
    color=(0, 255, 0),
    start_pos=(WIDTH // 2, HEIGHT // 2),
    speed=4
)

all_sprites.add(player)

# -----------------------------
# Game Loop
# -----------------------------
while RUNNING:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            RUNNING = False

    # Update all sprites
    all_sprites.update()

    # Draw
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)  # Sprite magic ✨

    pg.display.flip()
    clock.tick(FPS)

pg.quit()
