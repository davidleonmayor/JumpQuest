import arcade
import random

from sprites.player import PlayerSprite

# Windows properties
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Jump quest"

# Scale constants
CHARACTER_SCALING = 1
TILE_SCALING = 0.5

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 8
GRAVITY = 1
PLAYER_JUMP_SPEED = 22

class Game(arcade.Window):
    def __init__(self):
        """Initializes variables and components of the game"""
        super().__init__(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE)

        # Sprites
        self.player_sprite = None
        self.player_sprite_test = None # change this to player_sprite when the player_sprite is finished
        self.scene = None
        self.next_platform_height = 200

        # Physics
        self.physics_engine = None

        # Camera for scrolling the screen
        self.camera = None
        self.center_camera_x_axi = 0

        # Camera to draw text
        self.gui_camera = None
        self.score = 0

        # Songs
        self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")
        self.puwerup_sound = arcade.load_sound(":resources:sounds/upgrade1.wav")

        arcade.set_background_color((22, 107, 193))

    def setup(self):
        # Set up the Game Scene
        self.scene = arcade.Scene()
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Walls", use_spatial_hash=True)
        self.scene.add_sprite_list("Platforms", use_spatial_hash=True)
        self.scene.add_sprite_list("Powerups", use_spatial_hash=True)

        # Set up the Game Camera
        self.camera = arcade.Camera(self.width, self.height)

        # Add player sprite
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_idle.png", CHARACTER_SCALING)
        self.player_sprite.center_x = 500
        self.player_sprite.center_y = 128
        self.scene.add_sprite("Player", self.player_sprite)

        # Add player sprite test
        self.player_sprite_test = PlayerSprite()
        self.scene.add_sprite("Player", self.player_sprite_test)
        # self.player_sprite_test.move_right()  # Mueve el sprite a la derecha a una velocidad de 5 píxeles por frame
        # self.player_sprite_test.move_right()  # Mueve el sprite a la derecha a una velocidad de 5 píxeles por frame
        # self.player_sprite_test.move_right()  # Mueve el sprite a la derecha a una velocidad de 5 píxeles por frame

        # Add walls
        for x in range(0, 1250, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.scene.add_sprite("Walls", wall)

        # Adding initial platforms from bottom to top
        for y_position in range(32, SCREEN_HEIGHT, 200):  # 32 is the height of the first platform
            quantity_x = random.randint(SCREEN_WIDTH/2-230, SCREEN_WIDTH/2+230) # random x axis position. (repeating code, fix it)
            self.create_platform(y_axis=y_position, x_axis=quantity_x, quantity=(2, 4))

        # Set up the physics engine
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            player_sprite=self.player_sprite_test, gravity_constant=GRAVITY, platforms=self.scene["Platforms"], walls=self.scene["Walls"]
        )

    def create_platform(self, y_axis: int, x_axis: int, quantity: tuple):
        x_movement_block_size = 0
        for _ in range(quantity[0], quantity[1]+1):
            platform = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
            platform.center_x = x_axis + x_movement_block_size
            platform.center_y = y_axis
            self.scene.add_sprite("Platforms", platform)
            x_movement_block_size += platform.width

    def on_draw(self):
        self.clear()
        self.scene.draw()
        self.camera.use()

    def on_update(self, delta_time):
        self.physics_engine.update()
        self.center_camera_to_player()
        self.add_platform()
        # check if player collides with powerup
        poweup_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.scene["Powerups"]
        )
        
        # Loop through each powerup we hit and remove it
        for powerup in poweup_hit_list:
            # Remove the coin
            powerup.remove_from_sprite_lists()
            # Play a sound
            arcade.play_sound(self.puwerup_sound)

    def center_camera_to_player(self):
        screen_center_y = self.player_sprite.center_y - (self.camera.viewport_height / 2)
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = self.center_camera_x_axi, screen_center_y
        self.camera.move_to(player_centered)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite_test.move_up()
                arcade.play_sound(self.jump_sound)
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite_test.move_left()
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite_test.move_right()

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite_test.stop_move_left()
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite_test.stop_move_right()

    # def on_key_press(self, key, modifiers):
    #     if key == arcade.key.UP or key == arcade.key.W:
    #         if self.physics_engine.can_jump():
    #             self.player_sprite.change_y = PLAYER_JUMP_SPEED
    #             arcade.play_sound(self.jump_sound)
    #     elif key == arcade.key.LEFT or key == arcade.key.A:
    #         self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
    #         self.player_sprite_test.move_right()
    #     elif key == arcade.key.RIGHT or key == arcade.key.D:
    #         self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
    
    # def on_key_release(self, key, modifiers):
    #     if key == arcade.key.LEFT or key == arcade.key.A:
    #         self.player_sprite.change_x = 0
    #     elif key == arcade.key.RIGHT or key == arcade.key.D:
    #         self.player_sprite.change_x = 0

    def add_platform(self):
        if self.player_sprite.center_y > self.next_platform_height: # IF player is above the next platform
            # Genere platform after the last platform
            init_x = random.randint(0, SCREEN_WIDTH/2)
            random_jump = random.randint(2, 4) * 200
            quantity_y = self.scene["Platforms"][-1].center_y + self.next_platform_height # get the last platform y axis
            for quantity_x in range(init_x, SCREEN_WIDTH, random_jump):
                self.create_platform(y_axis=quantity_y, x_axis=quantity_x, quantity=(2, 4))

            # Probability of a powerup being generated 2/10
            if random.randint(1, 10) <= 1:
                powerup = arcade.Sprite(":resources:images/items/star.png", TILE_SCALING)
                powerup.center_x = init_x+100
                powerup.center_y = quantity_y+100
                self.scene.add_sprite("Powerups", powerup)

def main():
    window = Game()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
