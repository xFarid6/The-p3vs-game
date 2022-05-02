import pygame
from typing import Tuple, Generator

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

# Generator[YieldType, SendType, ReturnType]
def fib(n: int) -> Generator[int, None, None]:
    a: int = 0
    b: int = 1
    while n > 0:
        yield a
        b, a = a + b, b
        n -= 1
