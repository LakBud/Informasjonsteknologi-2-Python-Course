import pygame as pg
import random as rnd

WIDTH = 1500
HEIGHT = 1000
FPS = 60

class GameManager:
    def __init__(self):
        # Pygame setup
        pg.init()
        self._screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Space Invaders")
        self._clock = pg.time.Clock()
        self._font = pg.font.SysFont(None, 50)
        
        # Lists
        self._all_sprites = []
        
        # Game variables
        self.active = True
        self._score = 0
        self._game_over = False

    def handle_events(self) -> None:
        """Handle user input and quitting."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.active = False
    
    
    def draw(self) -> None:
        """Draw everything to the _screen."""
        self._screen.fill((0, 0, 0))
        
        if not self._game_over:
            for sprites in self._all_sprites:
                sprites.draw()
            
            # Active Score Text
            score_text = self._font.render(f"Score: {self._score}", True, (255, 255, 255))
            self._screen.blit(score_text, (20, 20))
            
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

    def update(self) -> None:
        for sprites in self._all_sprites:
            sprites.update()
        
    def run(self): 
        """Main game loop."""
        while self.active:
            self._clock.tick(FPS)
            self.handle_events()
            self.draw()
            if not self._game_over:
                self.update()
        pg.quit()


# Entry point
if __name__ == "__main__":
    game = GameManager()
    game.run()
