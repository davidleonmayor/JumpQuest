from arcade import Sprite, load_sound, load_texture
from constants.player import *

# How fast to move, and how fast to run the animation
# MOVEMENT_SPEED = 5
UPDATES_PER_FRAME = 5

# Constants used to track if the player is facing left or right
RIGHT_FACING = 0
LEFT_FACING = 1

def load_texture_pair(filename):
    """
    Load a texture pair, with the second being a mirror image.
    """
    return [
        load_texture(filename),
        load_texture(filename, flipped_horizontally=True)
    ]

class PlayerSprite(Sprite):
    def __init__(self):
        super().__init__(IMAGE_PATH, CHARACTER_SCALING)
        self.center_x = PLAYER_INITIAL_POSITION_X
        self.center_y = PLAYER_INITIAL_POSITION_Y
        self.can_jump = CAN_PLAYER_JUMP
        self.jump_speed = PLAYER_MOVEMENT_SPEED * 2.8
        self.__jump_sound = load_sound(JUMP_SOUND)
        self.__is_life = IS_LIFE
        self.__last_y_position = PLAYER_INITIAL_POSITION_Y

        # Default to face-right
        self.character_face_direction = RIGHT_FACING

        # Used for flipping between image sequences
        self.cur_texture = 0 

        # --- Load Textures ---
        # main_path = ":resources:images/animated_characters/zombie/zombie"
        main_path = ":resources:images/animated_characters/female_adventurer/femaleAdventurer"
        # Load textures for idle standing
        self.idle_texture_pair = load_texture_pair(f"{main_path}_idle.png")
        # Load textures for walking
        self.walk_textures = []
        for i in range(8):
            texture = load_texture_pair(f"{main_path}_walk{i}.png")
            self.walk_textures.append(texture)

    def is_life(self) -> bool:
        return self.__is_life

    def update_life(self) -> None:
        self.__feell_down()

    

    def update_animation(self, delta_time: float = 1 / 60):
        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING

        # Idle animation
        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.idle_texture_pair[self.character_face_direction]
            return

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture > 7 * UPDATES_PER_FRAME:
            self.cur_texture = 0
        frame = self.cur_texture // UPDATES_PER_FRAME
        direction = self.character_face_direction
        self.texture = self.walk_textures[frame][direction]

    # dead player if fell more than N pixel high
    def __feell_down(self) -> None:
        fell_height = 500
        if self.last_y_position() - self.y_position() > fell_height:
            self.__is_life = False
        else:
            self.__is_life = True

    def y_position(self) -> float:
        return self.center_y

    def last_y_position(self) -> float:
        return self.__last_y_position

    def player_can_jump(self):
        return self.can_jump

    def jump(self):
        self.__last_y_position = self.center_y # the las position then player are before jump
        self.change_y = self.jump_speed

    def jump_sound(self):
        return self.__jump_sound

    def move_right(self):
        self.change_x = PLAYER_MOVEMENT_SPEED

    def move_left(self):
        self.change_x = -PLAYER_MOVEMENT_SPEED

    def stop_move_right(self):
        self.change_x = 0 # cero because the player is not moving

    def stop_move_left(self):
        self.change_x = 0 # cero because the player is not moving
