# Global Variables
WIDTH: int = 1600
HEIGHT: int = 1000
FPS: int = 60

# Player
P_START_COORD: tuple[int, int] = (WIDTH // 2, HEIGHT - 50)
P_WIDTH: int = 60
P_HEIGHT: int = 60
P_DEFAULT_COLOR: tuple[int, int, int] = (100, 100, 100)
P_SPEED: int = 10

# Player Bullet
PB_WIDTH: int = 10
PB_HEIGHT: int = 20
PB_DEFAULT_COLOR: tuple[int, int, int] = (255, 0, 0)
PB_SPEED: int = -15
PB_IMAGE_PATH: str = "src/tasks/4_before_fourth_test/space_invaders/images/IT2-space-invaders-playerbullet.png"

# Enemy Amount & Position
E_ROWS: int = 5
E_COLS: int = 10
E_SPACING_X: int = 100
E_SPACING_Y: int = 80
E_START_X: int = 100
E_START_Y: int = 90

# Enemy
E_WIDTH: int = 60
E_HEIGHT: int = 60
E_DEFAULT_COLOR: tuple[int, int, int] = (100, 100, 100)
E_SPEED: int = 10

# Enemy Bullet
EB_WIDTH: int = 10
EB_HEIGHT: int = 20
EB_DEFAULT_COLOR: tuple[int, int, int] = (0, 255, 0)
EB_SPEED: int = 10
EB_IMAGE_PATH: str = "src/tasks/4_before_fourth_test/space_invaders/images/IT2-space-invaders-alienbullet.png"

# Fortification
NUM_FORTS: int = 4
F_WIDTH: int = 120
F_HEIGHT: int = 60
F_DEFAULT_COLOR: tuple[int, int, int] = (0, 255, 0)

