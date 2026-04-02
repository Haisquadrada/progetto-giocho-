import arcade
import altricode

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Rooms"
PLAYER_SPEED = 5

class Rooms(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.GRAY)

        # Create SpriteLists for organization and performance
        self.background_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        
        self.player = None
        self.background_sprite = None

    def setup(self):
        # 1. Setup Background as a Sprite
        self.background_sprite = arcade.Sprite("assets/room.png")
        
        # Position the background in the center
        self.background_sprite.center_x = SCREEN_WIDTH // 2
        self.background_sprite.center_y = SCREEN_HEIGHT // 2
        
        # Scale the background to fit the screen size exactly
        self.background_sprite.width = SCREEN_WIDTH
        self.background_sprite.height = SCREEN_HEIGHT
        
        self.background_list.append(self.background_sprite)

        # 2. Setup Player
        self.player = arcade.Sprite("assets/ethan.png", scale=0.1)
        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = SCREEN_HEIGHT // 2
        
        self.player_list.append(self.player)

    def on_draw(self):
        self.clear()
        
        # Draw the background list first
        self.background_list.draw()
        
        # Draw the player list second (so they stay on top)
        self.player_list.draw()

    def on_update(self, delta_time):
        self.player_list.update()

        # Simple Boundary Checking
        if self.player.left < 0:
            self.player.left = 0
        elif self.player.right > SCREEN_WIDTH:
            self.player.right = SCREEN_WIDTH

        if self.player.bottom < 0:
            self.player.bottom = 0
        elif self.player.top > SCREEN_HEIGHT:
            self.player.top = SCREEN_HEIGHT

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