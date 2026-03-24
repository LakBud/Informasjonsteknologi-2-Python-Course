import pygame as pg
import random as rnd
from classes import Organism

WIDTH, HEIGHT, FPS = 1000, 1000, 5

class GameController:
    """The brain of the program that controls the flow."""
    def __init__(self, screen_width: int, screen_height: int, fps: int):
        pg.init()
        self._screen_width = screen_width
        self._screen_height = screen_height
        self._screen = pg.display.set_mode((screen_width, screen_height))
        pg.display.set_caption("Game of life")
        self._clock = pg.time.Clock()
        self._fps = fps
        self._active = True
        self._font = pg.font.SysFont("Calibri", 28, True)
        self._clicked_coords = None
        
        self._rows = 50
        self._cols = 50
        self._cell_width = self._screen_width // self._cols
        self._cell_height = self._screen_height // self._rows

        self._organisms: list[list[Organism]] = []
        

        for row in range(self._rows):
            grid_row = []
            for col in range(self._cols):
                x = col * self._cell_width + self._cell_width // 2
                y = row * self._cell_height + self._cell_height // 2

                organism = Organism(self._screen, (x, y), self._cell_width, self._cell_height)

                # Random chance that it is alive
                if rnd.random() < (1/3):
                    organism.is_alive = True

                grid_row.append(organism)

            self._organisms.append(grid_row)

    def handle_events(self):
        """Check for quit, space, or mouse clicks."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self._active = False
            
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.kill_all_organisms()
            
            elif event.type == pg.MOUSEBUTTONDOWN:
                self._clicked_coords = pg.mouse.get_pos()

    def update_organism(self, mouse_coords: tuple[int, int], next_states: list[list[bool]]):
        for row_idx, row in enumerate(self._organisms):
            for col_idx, organism in enumerate(row):
                if organism.rect.collidepoint(mouse_coords):
                    next_states[row_idx][col_idx] = not organism.is_alive

    def update(self):
        next_states = []

        for row in range(self._rows):
            next_row = []
            for col in range(self._cols):
                organism = self._organisms[row][col]
                live_neighbors = self.count_neighbors(row, col)

                # Apply Game of Life rules
                if organism.is_alive:
                    if live_neighbors < 2 or live_neighbors > 3:
                        next_row.append(False)
                    else:
                        next_row.append(True)
                else:
                    if live_neighbors == 3:
                        next_row.append(True)
                    else:
                        next_row.append(False)

                # Handle mouse click toggle
                if self._clicked_coords and organism.rect.collidepoint(self._clicked_coords):
                    next_row[-1] = not organism.is_alive

            next_states.append(next_row)

        # Reset click after applying
        self._clicked_coords = None

        # Apply next states
        for row in range(self._rows):
            for col in range(self._cols):
                self._organisms[row][col].is_alive = next_states[row][col]
        
        # Update organism visuals
        for row in self._organisms:
            for organism in row:
                organism.update()
    
    
    def count_neighbors(self, row, col):
        count = 0

        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue

                new_row = row + dy
                new_col = col + dx

                if 0 <= new_row < self._rows and 0 <= new_col < self._cols:
                    if self._organisms[new_row][new_col].is_alive:
                        count += 1

        return count
    
    def kill_all_organisms(self):
        for row in self._organisms:
            for organism in row:
                organism.is_alive = False

    def draw_all(self):
        self._screen.fill((200, 200, 200))

        for row in self._organisms:
            for organism in row:
                organism.draw()

        pg.display.flip()

    def run(self):
        """Main loop."""
        while self._active:
            self.handle_events()
            self.update()
            self.draw_all()
            self._clock.tick(self._fps)

        pg.quit()


if __name__ == "__main__":
    game = GameController(WIDTH,HEIGHT,FPS)
    game.run()
