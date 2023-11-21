from arcade import Sprite
# from constants import physics
from constants import plarform
from constants import enviroment
import random

class PlatformSprite(Sprite):
    # n columns = SCREEN_WIDTH/64 "64 is the width of the block" n rows = SCREEN_HEIGHT/space_between_platforms
    row_platforms = [
        [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1],
        [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
        [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1],
        # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
    ]

    def __init__(self, scene):
        self.SCREEN_HEIGHT = enviroment.SCREEN_HEIGHT
        self.SCREEN_WIDTH = enviroment.SCREEN_WIDTH
        self.TILE_SCALING = plarform.TILE_SCALING
        self.space_between_platforms = 200
        super().__init__(":resources:images/tiles/grassMid.png", self.TILE_SCALING)
        self.sprite = None
        self.scene = scene

    # Create initial walls
    def create_wall(self) -> None:
        for x_position in range(32, self.SCREEN_WIDTH, 64): # 32 because it shows from the middle of the block, 64 is each width of the wall
            wall = Sprite(":resources:images/tiles/grassMid.png", self.TILE_SCALING)
            wall.center_x = x_position
            wall.center_y = 32
            self.scene.add_sprite("Walls", wall)

    # test new plarform
    def new(self, player_sprite) -> None:
        posicion_y = player_sprite.center_y
        if posicion_y > self.space_between_platforms: # IF player is above the next platform
            random_row = self.row_platforms[random.randint(0, len(self.row_platforms)-1)]
            spacer = 32
            y = self.scene["Platforms"][-1].center_y + self.space_between_platforms # get the last platform y axis
            for cell in random_row:
                if cell == 1:
                    bloque = Sprite(":resources:images/tiles/grassMid.png", self.TILE_SCALING)
                    bloque.center_x = spacer
                    bloque.center_y = y # self.scene["Platforms"][-1].center_y + self.space_between_platforms # get the last platform y axis
                    self.scene.add_sprite("Platforms", bloque)

                spacer += 64

    def remove(self, index: int = None) -> None:
        # validate if index is diferent an integrer
        if not isinstance(index, int):
            raise ValueError("index must be an integer")
        elif index < 0 or index > len(self.scene["Platforms"])-1:
            raise ValueError("index must be between 0 and {}".format(len(self.scene["Platforms"])-1))

        self.scene["Platforms"].pop(index)

    # Add walls
    # Adding initial platforms from bottom to top
    def create_platforms(self) -> None:
        for y_position in range(32, self.SCREEN_HEIGHT, self.space_between_platforms):  # 32 is the height of the first platform
            quantity_x = random.randint(self.SCREEN_WIDTH/2-230, self.SCREEN_WIDTH/2+230) # random x axis position. (repeating code, fix it)
            self.create_platform(y_axis=y_position, x_axis=quantity_x, quantity=(2, 4))

    def new_row_plarforms(self, player_sprite) -> None:
        posicion_y = player_sprite.center_y
        next_platform_height = 200
        if posicion_y > next_platform_height: # IF player is above the next platform
            # Genere platform after the last platform
            init_x = random.randint(0, self.SCREEN_WIDTH/2)
            random_jump = random.randint(2, 4) * next_platform_height
            quantity_y = self.scene["Platforms"][-1].center_y + next_platform_height # get the last platform y axis
            for quantity_x in range(init_x, self.SCREEN_WIDTH, random_jump):
                self.create_platform(y_axis=quantity_y, x_axis=quantity_x, quantity=(2, 4))

    def create_platform(self, y_axis: int, x_axis: int, quantity: tuple) -> None:
        x_movement_block_size = 0
        for _ in range(quantity[0], quantity[1]+1):
            platform = Sprite(":resources:images/tiles/grassMid.png", self.TILE_SCALING)
            platform.center_x = x_axis + x_movement_block_size
            platform.center_y = y_axis
            self.scene.add_sprite("Platforms", platform)
            x_movement_block_size += platform.width
