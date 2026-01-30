import pygame as pg
import random as rnd
from classes import Troll, Food, Obstacle
from utils import spawn_free_pos
from config import *

# Global Variables
WIDTH, HEIGHT = 1000, 1000
FPS = 60  # Frames per second


def main():
    # Start
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    my_font = pg.font.SysFont(None, 50)
    score: int = 0

    # Troll
    troll_player = Troll(
        screen,
        TROLL_START_COORD,
        TROLL_WIDTH,
        TROLL_HEIGHT,
        TROLL_COLOR,
        TROLL_SPEED_X,
        TROLL_SPEED_Y,
        my_font,
        TROLL_LETTER,
    )

    # Food
    foods: list[Food] = []
    for _ in range(FOOD_COUNT):
        new_food_coord = (
            rnd.randint(0, SCREEN_WIDTH - FOOD_WIDTH),
            rnd.randint(0, SCREEN_HEIGHT - FOOD_HEIGHT),
        )
        foods.append(
            Food(
                screen,
                new_food_coord,
                FOOD_WIDTH,
                FOOD_HEIGHT,
                FOOD_COLOR,
                my_font,
                FOOD_LETTER,
            )
        )


    pending_obstacles: list[tuple] = []
    obstacles: list[Obstacle] = []

    # Game Config
    screen_rect = pg.Rect(0, 0, WIDTH, HEIGHT)
    DELAY_MS = 500
    active = True

    # Game loop (Primary Loop)
    while active:
        # Check if the user wants to go out
        for action in pg.event.get():
            if action.type == pg.QUIT:
                active = False

        screen.fill((0, 0, 0))  # Black

        # Frem forth tha playah
        troll_player.handle_input()
        troll_player.move()
        troll_player.update_speed()
        troll_player.draw()

        if not screen_rect.contains(troll_player.rect):
            active = False

        # Draw the foods
        for food in foods:
            food.draw()

        for food in foods[:]:  # Create a copy for effective deleting
            if food.collides_with(troll_player):
                troll_player.update_speed()

                # Delete food
                foods.remove(food)
                score += 1

                # Create new coords for the new food
                new_food_coord = spawn_free_pos(
                    (FOOD_WIDTH, FOOD_HEIGHT), foods + obstacles, WIDTH, HEIGHT
                )
                foods.append(
                    Food(
                        screen,
                        new_food_coord,
                        FOOD_WIDTH,
                        FOOD_HEIGHT,
                        FOOD_COLOR,
                        my_font,
                        FOOD_LETTER,
                    )
                )

                # Append the obstacle within pending_obstacles for the delay
                spawn_time = pg.time.get_ticks() + DELAY_MS
                pending_obstacles.append((food.rect.center, spawn_time))

        current_time = (
            pg.time.get_ticks()
        )  # Get the number of milliseconds since pygame.init() was called

        for pos, t in pending_obstacles[:]:
            # Checks if the current time is more than the cooldown
            if current_time >= t:
                # If it is, only then spawn the obstacle
                obstacles.append(
                    Obstacle(
                        screen,
                        pos,
                        OBSTACLE_WIDTH,
                        OBSTACLE_HEIGHT,
                        OBSTACLE_COLOR,
                        my_font,
                        OBSTACLE_LETTER,
                    )
                )
                # Remove the posistion and spawn time from the previous obstacle
                pending_obstacles.remove((pos, t))

        # Draw the obstacles
        for obstacle in obstacles:
            obstacle.draw()

            if obstacle.collides_with(troll_player):
                active = False

        # Score
        score_text = my_font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        # Update
        pg.display.flip()
        clock.tick(FPS)

    pg.quit()


# This checks if the file is being run while its open
if __name__ == "__main__":
    main()
