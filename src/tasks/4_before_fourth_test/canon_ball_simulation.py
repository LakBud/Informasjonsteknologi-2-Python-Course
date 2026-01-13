import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cannonball Simulation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Clock to control frame rate
clock = pygame.time.Clock()
FPS = 60

# Cannonball properties
ball_radius = 15
x = ball_radius  # Start at bottom-left corner
y = HEIGHT - 250

velocity_x = 5       # Horizontal speed
velocity_y = -10     # Negative = moving upwards initially
a = 0.5              # Gravity (positive pulls downward)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Physics update
    velocity_y += a               # Gravity affects vertical velocity
    x += velocity_x                # Horizontal motion
    y += velocity_y                # Vertical motion

    # Check for collision with the floor
    if y >= HEIGHT - ball_radius:
        y = HEIGHT - ball_radius
        velocity_y = -velocity_y * 0.7  # Bounce with some energy loss

    # Check for collision with walls
    if x >= WIDTH - ball_radius or x <= ball_radius:
        velocity_x = -velocity_x      # Bounce horizontally

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (int(x), int(y)), ball_radius)
    pygame.display.flip()

    # Control frame rate
    clock.tick(FPS)

pygame.quit()
sys.exit()
