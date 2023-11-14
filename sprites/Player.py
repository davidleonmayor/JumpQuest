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
        self.__is_life = True
        self.__last_y_position = PLAYER_INITIAL_POSITION_Y

    def is_life(self) -> bool:
        return self.__is_life

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
