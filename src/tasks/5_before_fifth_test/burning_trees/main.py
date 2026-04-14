import pygame as pg
import random as rnd
from classes import Cell

WIDTH, HEIGHT, FPS = 1000, 1000, 5

class GameController:
    """The brain of the program that controls the flow."""
    def __init__(self, screen_width: int, screen_height: int, fps: int):
        pg.init()
        self._screen_width = screen_width
        self._screen_height = screen_height
        self._screen = pg.display.set_mode((screen_width, screen_height))
        pg.display.set_caption("Burning trees")
        self._clock = pg.time.Clock()
        self._fps = fps
        self._active = True
        self._font = pg.font.SysFont("Calibri", 28, True)
        self._clicked_coords = None
        
        self._rows = 60
        self._cols = 60
        self._cell_width = self._screen_width // self._cols
        self._cell_height = self._screen_height // self._rows

        self._cells: list[list[Cell]] = []
        

        for row in range(self._rows):
            grid_row = []
            for col in range(self._cols):
                x = col * self._cell_width + self._cell_width // 2
                y = row * self._cell_height + self._cell_height // 2

                cell = Cell(self._screen, (x, y), self._cell_width, self._cell_height)

                grid_row.append(cell)

            self._cells.append(grid_row)

    def handle_events(self):
        """Check for quit, space, or mouse clicks."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self._active = False


    def update(self):
        # 1. start copy for next grid
        next_states = [[cell.state for cell in row] for row in self._cells]

        fire_exists = False

        for row in self._cells:
            for cell in row:
                if cell.state == "fire":
                    fire_exists = True


        # 2. Tree chance
        if not fire_exists:
            for r in range(self._rows):
                for c in range(self._cols):
                    if self._cells[r][c].state == "empty":
                        if rnd.random() < 0.03:
                            next_states[r][c] = "tree"

        # 3. Fire chance
        if rnd.random() < 0.2:
            r = rnd.randint(0, self._rows - 1)
            c = rnd.randint(0, self._cols - 1)

            if self._cells[r][c].state == "tree":
                next_states[r][c] = "fire"


        
        # 4. Fire spreading
        for r in range(self._rows):
            for c in range(self._cols):

                if self._cells[r][c].state == "fire":
                    next_states[r][c] = "empty"

                elif self._cells[r][c].state == "tree":
                    if self.has_neighbor(r, c):
                        next_states[r][c] = "fire"

        # 5. intiakuze cioy
        for r in range(self._rows):
            for c in range(self._cols):
                self._cells[r][c].state = next_states[r][c]
        
        # VISUAL UPDATE
        for row in self._cells:
            for cell in row:
                cell.update()
    

    def has_neighbor(self, row, col):
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue

                new_row = row + dy
                new_col = col + dx

                if 0 <= new_row < self._rows and 0 <= new_col < self._cols:
                    if self._cells[new_row][new_col].state == "fire":
                        return True
        return False

    def draw_all(self):
        self._screen.fill((200, 200, 200))

        for row in self._cells:
            for cell in row:
                cell.draw()

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
