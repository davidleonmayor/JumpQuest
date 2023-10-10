import arcade
import random

# Windows properties
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Jump quest"

# Scale constants
CHARACTER_SCALING = 1
TILE_SCALING = 0.5

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 8
GRAVITY = 3
PLAYER_JUMP_SPEED = 40

class Game(arcade.Window):
    def __init__(self):
        """Initializes variables and components of the game"""
        super().__init__(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE)
        
        # Sprites
        self.player_sprite = None
        self.scene = None

        # Physics
        self.physics_engine = None
        
        # Camera for scrolling the screen
        self.camera = None
        self.center_camera_x_axi = 0

        # Camera to draw text
        self.gui_camera = None
        self.score = 0

        self.next_platform_height = 268
        self.last_platform_y = 0

        arcade.set_background_color((22, 107, 193))

    def setup(self):
        self.scene = arcade.Scene()
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Walls", use_spatial_hash=True)

        self.camera = arcade.Camera(self.width, self.height)

        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png", CHARACTER_SCALING)
        self.player_sprite.center_x = 500
        self.player_sprite.center_y = 128
        self.scene.add_sprite("Player", self.player_sprite)

        for x in range(0, 1250, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.scene.add_sprite("Walls", wall)

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, gravity_constant=GRAVITY, walls=self.scene["Walls"]
        )

    def on_draw(self):
        self.clear()
        self.player_sprite.draw()
        self.scene.draw()
        self.camera.use()

    def on_update(self, delta_time):
        self.physics_engine.update()
        self.center_camera_to_player()
        self.add_platform()

    def center_camera_to_player(self):
        screen_center_y = self.player_sprite.center_y - (self.camera.viewport_height / 2)
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = self.center_camera_x_axi, screen_center_y
        self.camera.move_to(player_centered)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
    
    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def add_platform(self):
        if self.player_sprite.center_y > self.last_platform_y:
            # Determina cuántos bloques compondrán la plataforma (2 o 3)
            num_blocks = random.randint(2, 3)

            # Ancho total de la plataforma (considerando 64 píxeles por bloque)
            total_width = num_blocks * 64

            # Posición inicial de la plataforma
            start_x = random.randint(100, SCREEN_WIDTH - total_width)
            platform_y = self.last_platform_y + self.next_platform_height

            # Crea los bloques de la plataforma
            for _ in range(num_blocks):
                platform = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
                platform.center_x = start_x + (64 / 2)  # Centra el bloque
                platform.center_y = platform_y
                self.scene.add_sprite("Walls", platform)
                start_x += 64  # Mueve la posición X para el siguiente bloque

            # Ajusta la altura de la plataforma para que sea alcanzable por el jugador
            platform_y += self.player_sprite.height + 10

            self.last_platform_y = platform_y


def main():
    window = Game()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
