import pygame as pg
from classes import Troll, Food, Obstacle
from utils import spawn_free_pos
from config import *


class GameManager:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Troll Game")
        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont(None, 50)

        # Sprite groups
        self.all_sprites = pg.sprite.Group()
        self.foods = pg.sprite.Group()
        self.obstacles = pg.sprite.Group()

        # Game variables
        self.score = 0
        self.game_over = False
        self.active = True

        # Player
        self.player = Troll(
            self.screen,
            TROLL_START_COORD,
            TROLL_WIDTH,
            TROLL_HEIGHT,
            TROLL_COLOR,
            TROLL_SPEED_X,
            TROLL_SPEED_Y,
            self.font,
            TROLL_LETTER
        )
        self.all_sprites.add(self.player)

        # Spawn initial foods
        for _ in range(FOOD_COUNT):
            self.spawn_food()

        # Pending obstacles (delayed spawn)
        self.pending_obstacles = []

    def spawn_food(self):
        new_food_coord = spawn_free_pos(
            (FOOD_WIDTH, FOOD_HEIGHT),
            list(self.foods) + list(self.obstacles) + [self.player],
            SCREEN_WIDTH,
            SCREEN_HEIGHT
        )
        food = Food(
            self.screen,
            new_food_coord,
            FOOD_WIDTH,
            FOOD_HEIGHT,
            FOOD_COLOR,
            self.font,
            FOOD_LETTER
        )
        self.foods.add(food)
        self.all_sprites.add(food)

    def spawn_obstacle(self, pos):
        obstacle = Obstacle(
            self.screen,
            pos,
            OBSTACLE_WIDTH,
            OBSTACLE_HEIGHT,
            OBSTACLE_COLOR,
            self.font,
            OBSTACLE_LETTER
        )
        self.obstacles.add(obstacle)
        self.all_sprites.add(obstacle)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.active = False

    def update(self):
        # Update all sprites
        self.all_sprites.update(self.game_over)

        # Check player out-of-bounds
        if not self.screen.get_rect().contains(self.player.rect):
            self.game_over = True

        # Check collisions with foods
        hit_foods = pg.sprite.spritecollide(self.player, self.foods, True)
        for food in hit_foods:
            self.player.update_speed()
            self.score += 1
            self.spawn_food()
            spawn_time = pg.time.get_ticks() + OBSTACLE_DELAY_MS
            self.pending_obstacles.append((food.rect.center, spawn_time))

        # Spawn pending obstacles
        current_time = pg.time.get_ticks()
        for pos, t in self.pending_obstacles[:]:
            if current_time >= t:
                self.spawn_obstacle(pos)
                self.pending_obstacles.remove((pos, t))

        # Check collisions with obstacles
        if pg.sprite.spritecollideany(self.player, self.obstacles):
            self.game_over = True

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)

        # Score
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

        # Game Over screen
        if self.game_over:
            self.screen.fill(BLACK)
            text = self.font.render("GAME OVER", True, (255, 0, 0))
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40))
            self.screen.blit(text, text_rect)

            game_over_score = self.font.render(f"SCORE: {self.score}", True, (255, 0, 0))
            score_rect = game_over_score.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40))
            self.screen.blit(game_over_score, score_rect)

    def run(self):
        while self.active:
            self.handle_events()
            if not self.game_over:
                self.update()
            self.draw()
            pg.display.flip()
            self.clock.tick(FPS)

        pg.quit()


if __name__ == "__main__":
    GameManager().run()
