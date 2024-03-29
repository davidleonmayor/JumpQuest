import arcade
from sprites.Player import PlayerSprite
from sprites.Platform import PlatformSprite
from constants.enviroment import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE
from constants.physics import GRAVITY

class Game(arcade.Window):
    def __init__(self):
        """Initializes variables and components of the game"""
        super().__init__(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE)

        # Sprites
        self.scene = None
        self.player_sprite = None
        self.platforms = None

        # Physics
        self.physics_engine = None

        # Camera for scrolling the screen
        self.camera = None
        self.center_camera_x_axi = 0

        # Camera to draw text
        self.gui_camera = None
        self.score = 0

        # Songs
        self.puwerup_sound = arcade.load_sound(":resources:sounds/upgrade1.wav")
        arcade.set_background_color((22, 107, 193))

    def setup(self):
        ''''''
        # Set up the Game Scene
        self.scene = arcade.Scene()
        # self.scene.add_sprite_list("Player")
        # self.scene.add_sprite_list("Walls", use_spatial_hash=True)
        # self.scene.add_sprite_list("Platforms", use_spatial_hash=True)
        # self.scene.add_sprite_list("Powerups", use_spatial_hash=True)

        # Add player sprite
        self.player_sprite = PlayerSprite()
        self.scene.add_sprite("Player", self.player_sprite)

        # TODO: Improve platform logic and performance
        # I think the mistake is that the list of sprites only ereda the class, not a list of sprites
        # Initialize platforms
        self.platforms = PlatformSprite(self.scene)
        self.scene.add_sprite_list("Platforms", self.platforms)
        self.platforms.create_wall()
        self.platforms.create_platforms() # add platforms form bottom to top

        # Set up the Game Camera
        self.camera = arcade.Camera(self.width, self.height)

        # Set up the physics engine
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            player_sprite=self.player_sprite,
            gravity_constant=GRAVITY,
            platforms=self.scene["Platforms"],
            walls=self.scene["Walls"]
        )

    def on_draw(self):
        self.clear()
        self.scene.draw()
        self.camera.use()

    def on_update(self, delta_time):
        # self.scene.update_animation(delta_time)
        self.player_sprite.update_life()
        if self.player_sprite.is_life():
            self.player_sprite.update_animation()
        else:
            arcade.close_window()

        # update map
        self.physics_engine.update()
        self.center_camera_to_player()
        self.platforms.new(self.player_sprite)

    def center_camera_to_player(self):
        screen_center_y = self.player_sprite.center_y - (self.camera.viewport_height / 2)
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = self.center_camera_x_axi, screen_center_y
        self.camera.move_to(player_centered)

        # if last platform isn't visible, remove it
        if self.scene["Platforms"][0].center_y < screen_center_y - 300: # If the last platform is at a distance of n pixels or more from the player
            self.platforms.remove(0)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.jump()
                arcade.play_sound(self.player_sprite.jump_sound())
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.move_left()
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.move_right()

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.stop_move_left()
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.stop_move_right()

def main():
    window = Game()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
