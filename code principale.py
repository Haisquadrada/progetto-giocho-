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

        # 1. Create a SpriteList to hold the player
        self.player_list = arcade.SpriteList()
        self.player = None
        
        # --- NEW: Variable for the background texture ---
        self.background = None

    def setup(self):
        # --- NEW: Load the background image ---
        # Replace "path/to/your/background.png" with your actual file path
        self.background = arcade.load_texture("assets/room.png")

        # 2. Initialize the sprite
        self.player = arcade.Sprite("./assets/ethan.png", scale=0.1)
        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = SCREEN_HEIGHT // 2
        
        # 3. Add the player to the list
        self.player_list.append(self.player)

    def on_draw(self):
        self.clear()
        
        # --- NEW: Draw the background ---
        # This draws the texture scaled to fill the entire screen
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        
        # 4. Draw the list, not the individual sprite
        self.player_list.draw()

    def on_update(self, delta_time):
        # 5. Update the list (this calls update() on all sprites inside)
        self.player_list.update()

        # Check the Left edge
        if self.player.left < 0:
            self.player.left = 0
        
        # Check the Right edge
        elif self.player.right > SCREEN_WIDTH:
            self.player.right = SCREEN_WIDTH

        # Check the Bottom edge
        if self.player.bottom < 0:
            self.player.bottom = 0
            
        # Check the Top edge 
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


    #fix dopo