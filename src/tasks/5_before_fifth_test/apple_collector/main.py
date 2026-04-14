import pygame as pg
import random as rnd
from classes import Player, Apple

WIDTH, HEIGHT, FPS = 1000, 1000, 60

class GameController:
    """The brain of the program that controls the flow."""
    def __init__(self, screen_width: int, screen_height: int, fps: int):
        pg.init()
        self._screen = pg.display.set_mode((screen_width, screen_height))
        pg.display.set_caption("Apple collector")
        self._clock = pg.time.Clock()
        self._fps = fps
        self._active = True
        self._font = pg.font.SysFont("Calibri", 28, True)
        self._start_time = pg.time.get_ticks()
        
        # Game variables
        self.active = True
        self._score = 0
        self._game_over = False
        self._total_apples = 0
        
        # Sprites
        self._all_sprites = []
        self._apples = []

        # Player
        self._player = Player(self._screen, (WIDTH // 2, 970), 80, 20, (255, 0, 0), 15)
        self._all_sprites.append(self._player)


    def spawn_apple(self):
        if len(self._apples) >= 3:
            return  # dont spawn more
        
        apple_color = rnd.choice([(255, 0, 0), (0, 255, 0)])
        new_apple = Apple(self._screen, (rnd.randrange(30, WIDTH - 30), 20), 30, 30, apple_color, 10)
        
        self._all_sprites.append(new_apple)
        self._apples.append(new_apple)
        
        self._total_apples += 1

    
    def handle_events(self):
        """Check for quit, space, or mouse clicks."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self._active = False


    def update(self):
        for sprite in self._all_sprites:
            sprite.update()
        
        # Allow player to change color based on apple
        self._player.input_color()
        
        # Apple Spawner
        current_time = pg.time.get_ticks()

        if current_time - self._start_time >= rnd.randrange(1500, 3000):  #  1.5 - 3 s
            self.spawn_apple()
            
            self._start_time = current_time  # reset timer
        
        for apple in self._apples[:]:
            # Remove Apple out of border
            if apple.rect.top > HEIGHT:
                self._all_sprites.remove(apple)
                self._apples.remove(apple)
            
            # Collision - Apple and Player
            if self._player.collides_with(apple):
                # Check if apple is same color as playr
                if apple._color == self._player._color:
                    self._score += 10
                    
                    self._all_sprites.remove(apple)
                    self._apples.remove(apple)
                else:
                    self._score -= 10
                    
                    self._all_sprites.remove(apple)
                    self._apples.remove(apple)

        # Game over checker
        if self._total_apples > 10 and len(self._apples) == 0:
            self._game_over = True


    def draw(self):
        self._screen.fill((0, 0, 0))
        
        if not self._game_over:
            for sprite in self._all_sprites:
                sprite.draw()
            
            # Score display
            score_text = self._font.render(f"Score: {self._score}", True, (255, 255, 255))
            self._screen.blit(score_text, (10, 10))
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

    def run(self):
        """Main loop."""
        while self._active:
            self.handle_events()
            if not self._game_over:
                self.update()
            self.draw()
            self._clock.tick(self._fps)

        pg.quit()


if __name__ == "__main__":
    game = GameController(WIDTH,HEIGHT,FPS)
    game.run()
