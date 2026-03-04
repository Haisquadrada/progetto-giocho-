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

        # Movement variables
        self.change_x = 0
        self.change_y = 0

    def setup(self):
        # Load the sprite
        self.player = arcade.Sprite("ethan.png", scale=0.5)
        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = SCREEN_HEIGHT // 2

    def on_draw(self):
        arcade.start_render()
        self.player.draw()

    def on_update(self, delta_time):
        # Move the player
        self.player.center_x += self.change_x
        self.player.center_y += self.change_y

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.UP:
            self.change_y = PLAYER_SPEED
        elif key == arcade.key.S or key == arcade.key.DOWN:
            self.change_y = -PLAYER_SPEED
        elif key == arcade.key.A or key == arcade.key.LEFT:
            self.change_x = -PLAYER_SPEED
        elif key == arcade.key.D or key == arcade.key.RIGHT:
            self.change_x = PLAYER_SPEED

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.W, arcade.key.S, arcade.key.UP, arcade.key.DOWN):
            self.change_y = 0
        elif key in (arcade.key.A, arcade.key.D, arcade.key.LEFT, arcade.key.RIGHT):
            self.change_x = 0


def main():
    game = Rooms()
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()



    #fix dopo