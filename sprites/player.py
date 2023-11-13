from arcade import Sprite, load_sound
from constants.player import *

class PlayerSprite(Sprite):
    def __init__(self):
        super().__init__(IMAGE_PATH, CHARACTER_SCALING)
        self.center_x = PLAYER_INITIAL_POSITION_X
        self.center_y = PLAYER_INITIAL_POSITION_Y
        self.can_jump = CAN_PLAYER_JUMP
        self.jump_speed = PLAYER_MOVEMENT_SPEED*2.8
        self.__jump_sound = load_sound(JUMP_SOUND)

    def player_can_jump(self):
        return self.can_jump
    
    def jump(self):
        self.change_y = self.jump_speed

    def move_right(self):
        self.change_x = PLAYER_MOVEMENT_SPEED

    def stop_move_right(self):
        self.change_x = 0 # cero because the player is not moving

    def move_left(self):
        self.change_x = -PLAYER_MOVEMENT_SPEED

    def stop_move_left(self):
        self.change_x = 0 # cero because the player is not moving

    def jump_sound(self):
        return self.__jump_sound

