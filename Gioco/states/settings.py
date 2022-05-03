import pygame
from typing import Tuple, Generator, List

if not pygame.font.get_init():
    pygame.font.init()
    # print(pygame.font.get_fonts())

# COLORS
BLACK: Tuple[int, int, int]     = (0, 0, 0)
WHITE: Tuple[int, int, int]     = (255, 255, 255)
RED: Tuple[int, int, int]       = (255, 0, 0)
GREEN: Tuple[int, int, int]     = (0, 255, 0)
BLUE: Tuple[int, int, int]      = (0, 0, 255)
YELLOW: Tuple[int, int, int]    = (255, 255, 0)
PURPLE: Tuple[int, int, int]    = (255, 0, 255)
CYAN: Tuple[int, int, int]      = (0, 255, 255)

LOADING_BAR_COLOR: Tuple[int, int, int] = (20, 250, 20)
GRAY: Tuple[int, int, int] = (50, 50, 50)


# FONTS
ARIAL: str = "Arial"
COMICSANS: str = "Comic Sans MS"
FREESANS: str = "FreeSans"


def import_csv_layout_gc(filename: str) -> List[List[str]]:
    """
    Import a CSV file and return a list of lists.
    """
    with open(filename, 'r') as f:
        layout = []
        for line in f:
            layout.append(line.strip().split(','))
    return layout


def import_cut_graphics(filename: str, tile_size: int) -> List[pygame.Surface]:
    surface: Surface = pygame.image.load(filename).convert_alpha()
    tile_num_x: int = int(surface.get_size()[0] // tile_size)
    tile_num_y: int = int(surface.get_size()[1] // tile_size)
    
    cut_tiles: list = []
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x: int = col * tile_size
            y: int = row * tile_size
            new_surf: Surface = pygame.Surface((tile_size, tile_size))
            new_surf.blit(surface, (0, 0), pygame.Rect(x, y, tile_size, tile_size))
            # tile = surface.subsurface((col * tile_size, row * tile_size, tile_size, tile_size))
            cut_tiles.append(new_surf)

    return cut_tiles


# Generator[YieldType, SendType, ReturnType]
def fib(n: int) -> Generator[int, None, None]:
    a: int = 0
    b: int = 1
    while n > 0:
        yield a
        b, a = a + b, b
        n -= 1
