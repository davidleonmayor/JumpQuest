import arcade

# Windows properties
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Jump quest"

# Scale constants
CHARACTER_SCALING = 1
TILE_SCALING = 0.5

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 30

class Game(arcade.Window):
    def __init__(self):
        """Initializes variables and components of the game"""
        # Call the parent class and set up the window
        super().__init__(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE)
        
        # Sprites in game
        self.player_sprite = None
        self.scene = None

        self.physics_engine = None
        
        self.camera = None

        # Camera to draw text
        self.gui_camera = None

        self.score = 0

        # Background window color
        arcade.set_background_color((22, 107, 193))


    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        # initialize scene
        self.scene = arcade.Scene() 
        
        # Create the Sprite lists
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Walls", use_spatial_hash=True)

        # Adding player sprite to scene
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png", CHARACTER_SCALING)
        self.player_sprite.center_x = 500
        self.player_sprite.center_y = 128
        self.scene.add_sprite("Player", self.player_sprite)

        # Adding tile sprites to scene        
        for x in range(0, 1250, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.scene.add_sprite("Walls", wall)

        """TODO: create a function to add platforms in y axis, in random position"""
        # Platforms in y axis
        for y in range(0, 1250, 250):
            if y < 150:
                continue
            
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
            wall.center_x = 32
            wall.center_y = y
            self.scene.add_sprite("Walls", wall)


        # Initialize physics engine to sprites        
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, gravity_constant=GRAVITY, walls=self.scene["Walls"]
        )


        # self.camera = arcade.Camera(self.width, self.height)
        # self.gui_camera = arcade.Camera(self.width, self.height)
        # self.score = 0

    def on_draw(self):
        """Render the screen."""
        self.clear()

        # Draw sprites
        self.player_sprite.draw()
        self.scene.draw()

        # arcade.start_render()
        # self.camera.use()
        # self.scene.draw()
        # self.gui_camera.use()
        # arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE, 18)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
    
    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """Movement and game logic"""
        # Move the player with the physics engine
        self.physics_engine.update()



def main():
    window = Game()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
