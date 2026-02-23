import pygame as pg
from classes import GameBoard, Human, Obstacle, Sheep, Ghost, GameObject

# Global Variables
WIDTH = 1500
HEIGHT = 1000
FPS = 60

class GameManager:
    def __init__(self):
        # Pygame setup
        pg.init()
        self._screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Manic Mansion")
        self._clock = pg.time.Clock()
        self._font = pg.font.SysFont(None, 50)
        self._board = GameBoard(WIDTH, HEIGHT)
        
        # Lists
        self._all_sprites: list[GameObject] = []
        self._ghosts: list[Ghost] = []
        self._sheeps: list[Sheep] = []
        self._obstacles: list[Obstacle] = []
        
        # Game variables
        self.active = True
        self._score = 0
        self._game_over = False
        
        # Spawn Start Objects
        self._create_start_objects()

    def handle_events(self) -> None:
        """Handle user input and quitting."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.active = False
    
    def _create_start_objects(self) -> None:
        # Player
        start_x = self._board.left_safe_zone // 2
        start_y = HEIGHT // 2
        
        self._player: Human = Human(self._screen, (start_x, start_y), 60, 60, (120, 0, 0), self._font, 10)
        self._all_sprites.append(self._player)
        
        # Obstacles
        for _ in range(3):
            o_pos = self._board.random_position_in_zone(
            self._board.left_safe_zone, 
            self._board.right_safe_zone,
            obj_width=60,
            obj_height=60
            )
            
            obstacle = Obstacle(self._screen, o_pos, 60, 60, (100, 100, 100), self._font)
            self._board.add_object(obstacle)
            self._all_sprites.append(obstacle)
            self._obstacles.append(obstacle)
        
        # Ghosts
        g_pos = self._board.random_position_in_zone(
            self._board.left_safe_zone, 
            self._board.right_safe_zone,
            obj_width=60,
            obj_height=60
            )
        
        ghost = Ghost(self._screen, g_pos, 60, 60, (0, 100, 200), self._font, 3)
        self._board.add_object(ghost)
        self._all_sprites.append(ghost)
        self._ghosts.append(ghost)
        
        # Sheeps
        for _ in range(3):
            s_pos = self._board.random_position_in_zone(
            self._board.right_safe_zone,
            self._board.width,
            obj_width=60,
            obj_height=60
            )
            
            sheep = Sheep(self._screen, s_pos, 60, 60, (255, 255, 255), self._font)
            self._board.add_object(sheep)
            self._all_sprites.append(sheep)
            self._sheeps.append(sheep)
    
    def draw(self) -> None:
        """Draw everything to the _screen."""
        self._screen.fill((0, 0, 0))
        
        if not self._game_over:
            # Draw left zone
            left_zone_rect = pg.Rect(0, 0, self._board.left_safe_zone, HEIGHT)
            pg.draw.rect(self._screen, (0, 250, 0, 100), left_zone_rect)
            
            # Draw right zone
            right_zone_rect = pg.Rect(self._board.right_safe_zone, 0, WIDTH - self._board.right_safe_zone, HEIGHT)
            pg.draw.rect(self._screen, (0, 0, 150, 100), right_zone_rect)  # blue shade
            
            # Draw all sprites
            for sprites in self._all_sprites:
                sprites.draw()
            
            # Active Score Text
            score_text = self._font.render(f"Score: {self._score}", True, (255, 255, 255), (0, 0, 0))
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
        keys = pg.key.get_pressed()
        
        # Retain position
        old_pos = self._player.rect.copy()
        
        # Allow player movement inside the border
        self._player.move(keys)
        self._player.block_if_outside(self._board)
        
        # Block obstacles
        for obstacle in self._obstacles:
            if self._player.collides_with(obstacle):
                self._player.rect = old_pos
        
        # Move ghosts
        for ghost in self._ghosts:
            ghost.move(self._board)
        
        # Ghost collision
        for ghost in self._ghosts:
            if self._player.collides_with(ghost):
                self._game_over = True
        
        # Sheep collision
        for sheep in self._sheeps[:]:
            # If not carrying -> Carry 
            if self._player.collides_with(sheep) and not self._player._carrying_sheep:
                self._player.pick_up_sheep()
                sheep.set_carried(True)
                
                self._all_sprites.remove(sheep)
                self._sheeps.remove(sheep)
                break
            
            # If carrying and collides -> game over
            if self._player.collides_with(sheep) and self._player._carrying_sheep:
                self._game_over = True
        
        # Check if player is carrying a sheep and reached left zone
        if self._player._carrying_sheep and self._player.rect.left <= self._board.left_safe_zone:
            self._player.deliver_sheep()
            self._score += 10                       # give a point
            
            # Spawn a new sheep on the right
            s_pos = self._board.random_position_in_zone(
            self._board.right_safe_zone,
            self._board.width,
            obj_width=60,
            obj_height=60
            )
            
            new_sheep = Sheep(self._screen, s_pos, 60, 60, (255,255,255), self._font)
            
            self._sheeps.append(new_sheep)
            self._all_sprites.append(new_sheep)
            self._board.add_object(new_sheep)
            
            # Spawn new obstacle
            o_pos = self._board.random_position_in_zone(
            self._board.left_safe_zone, 
            self._board.right_safe_zone,
            obj_width=60,
            obj_height=60
            )
            
            obstacle = Obstacle(self._screen, o_pos, 60, 60, (100, 100, 100), self._font)
            
            self._board.add_object(obstacle)
            self._all_sprites.append(obstacle)
            self._obstacles.append(obstacle)
            
            # Spawn new ghost
            g_pos = self._board.random_position_in_zone(
            self._board.left_safe_zone, 
            self._board.right_safe_zone,
            obj_width=60,
            obj_height=60
            )

            ghost = Ghost(self._screen, g_pos, 60, 60, (0, 100, 200), self._font, 3)
            self._board.add_object(ghost)
            self._all_sprites.append(ghost)
            self._ghosts.append(ghost)
            
            self._board.add_object(ghost)
            self._all_sprites.append(ghost)
            self._ghosts.append(ghost)
            

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