import arcade
import random
import arcade.math

# Costanti
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Rooms"
PLAYER_SPEED = 5

PAPER_X, PAPER_Y = 745, 525
RIGHT_DOOR_X = 1200

# Domande e risposte
QUESTIONS = [
    {"text": "Did you get slimed?", "answer": "Y"},
    {"text": "Are you going to keep doomscrolling if you get a second chance?", "answer": "N"},
    {"text": "Did you see it coming, or was it John Cena?", "answer": "N"},
    {"text": "Is 'In Rainbows' the best Radiohead album?", "answer": "N"},
    {"text": "So is it 'The Bends'?", "answer": "Y"},
    {"text": "Is Mohammad Saif a good person?", "answer": "N"},
    {"text": "Are you racist?", "answer": "N"},
    {"text": "You lied, didn't you brochacho?", "answer": "Y"},
    {"text": "Is John Frusciante the goat?", "answer": "Y"},
    {"text": "x(x + 1) + 2(x² - 1) = x(x - 1) - 3(x² - 1) + 2x : il risultato è +-2?", "answer": "N"},
]

class Rooms(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)

        # Sprite List
        self.background_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.ui_box_list = arcade.SpriteList()
        self.jumpscare_list = arcade.SpriteList()
        
        self.player = None
        self.background_sprite = None
        self.ui_box = None
        self.jumpscare_sprite = None
        
        # Variabili di suoni
        self.bgm = None
        self.jumpscare_sfx = None 
        
        # Variabili di logica del gioco
        self.room_number = 1
        self.answered_correctly = False
        self.state = "PLAYING" 
        
        # Logica Jumpscare
        self.show_jumpscare = False
        self.jumpscare_timer = 0

    def setup(self):
        # 1. Setup Background
        self.background_sprite = arcade.Sprite("assets/room.png")
        self.background_sprite.center_x = SCREEN_WIDTH // 2
        self.background_sprite.center_y = SCREEN_HEIGHT // 2
        self.background_sprite.width = SCREEN_WIDTH
        self.background_sprite.height = SCREEN_HEIGHT
        self.background_list.append(self.background_sprite)

        # 2. Setup giocatore
        self.player = arcade.Sprite("assets/ethan.png", scale=0.1)
        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = SCREEN_HEIGHT // 2
        self.player_list.append(self.player)
        
        # 3. Setup UI Box
        self.ui_box = arcade.SpriteSolidColor(700, 300, color=(0, 0, 0, 230))
        self.ui_box.center_x = SCREEN_WIDTH // 2
        self.ui_box.center_y = SCREEN_HEIGHT // 2
        self.ui_box_list.append(self.ui_box)
        
        #Setup jumpscare
        self.jumpscare_sprite = arcade.Sprite("assets/jumpscareimage.png", scale=4.2) 
        self.jumpscare_sprite.center_x = SCREEN_WIDTH // 2
        self.jumpscare_sprite.center_y = SCREEN_HEIGHT // 2
        self.jumpscare_list.append(self.jumpscare_sprite)

        #Suoni
        try:
            # Radiohead
            self.bgm = arcade.load_sound("assets/Hunting Bears.mp3")
            arcade.play_sound(self.bgm, volume=0.02, loop=True)
            
          
            self.jumpscare_sfx = arcade.load_sound("assets/jumpscare.mp3") 
        except Exception as e:
            print(f"Audio failed to load: {e}")

    def on_draw(self):
        self.clear()

        if self.state == "FREE":
            arcade.draw_text("You scaped the ", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 
                             arcade.color.RED, 50, anchor_x="center")
            return

        self.background_list.draw()
        self.player_list.draw()

        arcade.draw_text(f"Room: {self.room_number}", 20, SCREEN_HEIGHT - 40, 
                         arcade.color.WHITE, 20, bold=True)

        if self.state == "ASKING_QUESTION":
            self.ui_box_list.draw()
            
            q_text = QUESTIONS[self.room_number - 1]["text"]
            arcade.draw_text(q_text, SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50, 
                             arcade.color.WHITE, 18, anchor_x="center")
            
            arcade.draw_text("[Y] YES", SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT/2 - 50, 
                             arcade.color.GREEN, 20, anchor_x="center")
            arcade.draw_text("[N] NO", SCREEN_WIDTH/2 + 100, SCREEN_HEIGHT/2 - 50, 
                             arcade.color.RED, 20, anchor_x="center")
            arcade.draw_text("Press [ESC] to Close", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 130, 
                             arcade.color.GRAY, 12, anchor_x="center")

        if self.show_jumpscare:
            self.jumpscare_list.draw()
        
    def on_update(self, delta_time):
        if self.state == "FREE":
            return

        if self.state == "PLAYING":
            self.player_list.update()

            if self.player.left < 0: self.player.left = 0
            if self.player.right > SCREEN_WIDTH: self.player.right = SCREEN_WIDTH
            if self.player.bottom < 0: self.player.bottom = 0
            if self.player.top > SCREEN_HEIGHT: self.player.top = SCREEN_HEIGHT

            dist = arcade.math.get_distance(self.player.center_x, self.player.center_y, PAPER_X, PAPER_Y)
            if dist < 50:
                self.state = "ASKING_QUESTION"
                self.player.change_x = 0
                self.player.change_y = 0

            if self.answered_correctly and self.player.center_x > RIGHT_DOOR_X:
                self.next_room()

        if self.show_jumpscare:
            self.jumpscare_timer -= delta_time
            if self.jumpscare_timer <= 0:
                self.show_jumpscare = False

    def next_room(self):
        self.room_number += 1
        if self.room_number > 10:
            self.state = "FREE"
        else:
            self.player.center_x = 150 
            self.answered_correctly = False
            
            # 29% di probabilità di jumpscare ad ogni nuova stanza
            if random.random() < 0.29:
                self.show_jumpscare = True
                self.jumpscare_timer = 2
                
                
                if self.jumpscare_sfx:
                    arcade.play_sound(self.jumpscare_sfx, volume=0.085)

    def reset_to_start(self):
        self.room_number = 1
        # Dopo una risposta sbagliata, riportiamo il giocatore al centro
        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = SCREEN_HEIGHT // 2
        self.answered_correctly = False
        self.state = "PLAYING"

    def on_key_press(self, key, modifiers):
        if self.state == "PLAYING":
            if key == arcade.key.W or key == arcade.key.UP: self.player.change_y = PLAYER_SPEED
            elif key == arcade.key.S or key == arcade.key.DOWN: self.player.change_y = -PLAYER_SPEED
            elif key == arcade.key.A or key == arcade.key.LEFT: self.player.change_x = -PLAYER_SPEED
            elif key == arcade.key.D or key == arcade.key.RIGHT: self.player.change_x = PLAYER_SPEED
        
        elif self.state == "ASKING_QUESTION":
            correct_ans = QUESTIONS[self.room_number - 1]["answer"]
            
            if key == arcade.key.Y:
                if correct_ans == "Y":
                    self.answered_correctly = True
                    self.state = "PLAYING"
                else:
                    self.reset_to_start()
            elif key == arcade.key.N:
                if correct_ans == "N":
                    self.answered_correctly = True
                    self.state = "PLAYING"
                else:
                    self.reset_to_start()
            elif key == arcade.key.ESCAPE:
                self.state = "PLAYING"
                # Dopo una risposta giusta, riportiamo il giocatore al centro
                self.player.center_x = SCREEN_WIDTH // 2
                self.player.center_y = SCREEN_HEIGHT // 2

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