import pygame as pg
import random as rnd


def spawn_free_pos(size, blocked, width: int, height: int):
    while True:
        # Pick a random x and y position within the screen bounds
        x = rnd.randint(size[0], width - size[0])
        y = rnd.randint(size[1], height - size[1])

        # Create a temporary rectangle for the new object at this position
        rect = pg.Rect(0, 0, *size)
        rect.center = (x, y)

        # Check if this rectangle collides with any blocked objects
        if not any(rect.colliderect(obj.rect) for obj in blocked):
            # If no collisions, return this position
            return x, y
