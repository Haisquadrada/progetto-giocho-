import arcade
import altricode

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Rooms"

PLAYER_SPEED = 5

class Rooms(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # Player sprite
        self.player = None

    def setup(self):
        # Load the sprite - ensure the path to your image is correct!
        # If you don't have the image yet, use arcade.SpriteCircle(20, arcade.color.RED) to test
        self.player = arcade.Sprite("./assets/ethan.png", scale=0.5)
        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = SCREEN_HEIGHT // 2

    def on_draw(self):
        self.clear() # Modern arcade replacement for start_render()
        self.player.draw()

    def on_update(self, delta_time):
        # This moves the sprite based on its change_x and change_y properties
        self.player.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.UP:
            self.player.change_y = PLAYER_SPEED
        elif key == arcade.key.S or key == arcade.key.DOWN:
            self.player.change_y = -PLAYER_SPEED
        elif key == arcade.key.A or key == arcade.key.LEFT:
            self.player.change_x = -PLAYER_SPEED
        elif key == arcade.key.D or key == arcade.key.RIGHT:
            self.player.change_x = PLAYER_SPEED

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.W, arcade.key.S, arcade.key.UP, arcade.key.DOWN):
            self.player.change_y = 0
        elif key in (arcade.key.A, arcade.key.D, arcade.key.LEFT, arcade.key.RIGHT):
            self.player.change_x = 0

def main():
    window = Rooms()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()



    #fix dopo