import pygame, sys
from csv import reader


def import_csv_layout_gc(filename):
    """
    Import a CSV file and return a list of lists.
    """
    with open(filename, 'r') as f:
        layout = []
        for line in f:
            layout.append(line.strip().split(','))
    return layout


def import_csv_layout(filename):
    with open(filename) as map_file:
        level = reader(map_file, delimiter=',')
        layout = []
        for row in level:
            layout.append(list(row))

    return layout


def import_cut_graphics(filename, tile_size):
    surface = pygame.image.load(filename).convert_alpha()
    tile_num_x = int(surface.get_size()[0] // tile_size)
    tile_num_y = int(surface.get_size()[1] // tile_size)
    
    cut_tiles = []
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * tile_size
            y = row * tile_size
            new_surf = pygame.Surface((tile_size, tile_size))
            new_surf.blit(surface, (0, 0), pygame.rect(x, y, tile_size, tile_size))
            #tile = surface.subsurface((col * tile_size, row * tile_size, tile_size, tile_size))
            cut_tiles.append(new_surf)

    return cut_tiles


class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface([size, size])
        self.image.fill((200, 200, 100))
        self.rect = self.image.get_rect(topleft = (x, y))

    
    def update(self, shift):
        self.rect.x += shift


class StaticTile(Tile):
    def __init__(self, x, y, size, surface):
        super().__init__(x, y, size)
        self.image = surface


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.world_shift = -4

        terrain_layout = import_csv_layout(level_data['bottom floor'])
        self.terrain_sprites = self.create_tile_group(terrain_layout, 'bottom floor')


    def create_tile_group(self, layout, tile_type, tile_size=16):
        tile_group = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if type == 'bottom floor':
                        terrain_tile_list = import_cut_graphics('somepath')
                        tile_surface = terrain_tile_list[int(val)]

                        sprite = StaticTile(x, y, tile_size, tile_surface)
                        tile_group.add(sprite)

        return tile_group


    def run(self):
        self.terrain_sprites.draw(self.display_surface)
        self.terrain_sprites.update(self.world_shift)


pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Map Load Test")
clock = pygame.time.Clock()

level_data = {
    'bottom floor': "C:\Cose Nuove\Code\Mine\The p3vs game\Gioco\maps\dungeon\dungeon_Bottom floor.csv",
    'columns': "C:\Cose Nuove\Code\Mine\The p3vs game\Gioco\maps\dungeon\dungeon_Columns.csv",
    'map border': "C:\Cose Nuove\Code\Mine\The p3vs game\Gioco\maps\dungeon\dungeon_Map Border.csv",
    'walls': "C:\Cose Nuove\Code\Mine\The p3vs game\Gioco\maps\dungeon\dungeon_Walls.csv"
}

level = Level(level_data, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))
    level.run()

    pygame.display.flip()
    clock.tick(60)
