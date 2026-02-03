import pygame as pg
import random as rnd
from classes import Troll, Food, Obstacle
from utils import spawn_free_pos
from config import *


def main():
    # Start
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()
    my_font = pg.font.SysFont(None, 50)

    # Game variables
    score: int = 0
    GAME_OVER: bool = False

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

    # Game setup
    screen_rect = pg.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    active = True

    # Game loop (Primary Loop)
    while active:
        # Check if the user wants to go out
        for action in pg.event.get():
            if action.type == pg.QUIT:
                active = False

        screen.fill(BLACK)

        # Frem forth tha playah
        troll_player.handle_input(GAME_OVER)
        troll_player.move(GAME_OVER)
        troll_player.update_speed()
        troll_player.draw()

        if not screen_rect.contains(troll_player.rect):
            GAME_OVER = True

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
                    (FOOD_WIDTH, FOOD_HEIGHT),
                    foods + obstacles,
                    SCREEN_WIDTH,
                    SCREEN_HEIGHT,
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
                spawn_time = pg.time.get_ticks() + OBSTACLE_DELAY_MS
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
                GAME_OVER = True

        # Score
        score_text = my_font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        # Game Over
        if GAME_OVER:
            screen.fill(BLACK)

            # Text for GAME OVER
            text = my_font.render("GAME OVER", True, (255, 0, 0))
            text_rect = text.get_rect(
                center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40)
            )
            screen.blit(text, text_rect)

            # Text for the score
            game_over_score = my_font.render(f"SCORE: {score}", True, (255, 0, 0))
            score_rect = game_over_score.get_rect(
                center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40)
            )
            screen.blit(game_over_score, score_rect)

        # Update
        pg.display.flip()
        clock.tick(FPS)

    pg.quit()


# This checks if the file is being run while its open
if __name__ == "__main__":
    main()
