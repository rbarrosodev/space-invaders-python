import globals


class Game:
    def __init__(self, window):
        self.window = window

    def run(self):
        self.window.set_background_color([0, 0, 0])
        kb = self.window.get_keyboard()

        if kb.key_pressed("esc"):
            globals.GAME_STATE = 1
