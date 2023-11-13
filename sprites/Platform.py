from arcade import Sprite
# from constants import physics
from constants import plarform
from constants import enviroment
import random

class PlatformSprite(Sprite):
    row_platforms = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 0
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 1
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 2
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 3
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 4
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 5
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 6
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 7
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 8

    ]

    def __init__(self, scene):
        self.SCREEN_HEIGHT = enviroment.SCREEN_HEIGHT
        self.SCREEN_WIDTH = enviroment.SCREEN_WIDTH
        self.TILE_SCALING = plarform.TILE_SCALING
        super().__init__(":resources:images/tiles/grassMid.png", self.TILE_SCALING)
        self.sprite = None
        self.scene = scene

    # Create initial walls
    def create_wall(self):
        jump_block_size = 32
        for x_position in range(0, self.SCREEN_WIDTH, jump_block_size):
            wall = Sprite(":resources:images/tiles/grassMid.png", self.TILE_SCALING)
            wall.center_x = x_position
            wall.center_y = 32
            self.scene.add_sprite("Walls", wall)

    # Add walls
    # Adding initial platforms from bottom to top
    def create_platforms(self) -> None:
        for y_position in range(32, self.SCREEN_HEIGHT, 200):  # 32 is the height of the first platform
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
