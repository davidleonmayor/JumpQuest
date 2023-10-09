import arcade

# Windows properties
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Jump quest"

class Game(arcade.Window):
    def __init__(self):
        # Call the parent class and set up the window
        super().__init__(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE)
        
        # Sprites in game
        self.player_sprite = None
        self.scene = None

        self.physics_engine = None
        
        self.camera = None

        self.gui_camera = None
        self.score = 0

        # Background window color
        arcade.set_background_color((22, 107, 193))


    def setup(self):
        pass
        # self.camera = arcade.Camera(self.width, self.height)
        # self.gui_camera = arcade.Camera(self.width, self.height)
        # self.score = 0

    def on_draw(self):
        self.clear()
        # arcade.start_render()
        # self.camera.use()
        # self.scene.draw()
        # self.gui_camera.use()
        # arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE, 18)


def main():
    window = Game()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
