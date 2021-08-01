import globals
from player import Player


class Game:
    def __init__(self, window):
        self.window = window
        self.fps = 0
        self.actual_fps = 0
        self.cron_fps = 0
        self.kb = window.get_keyboard()
        self.player = Player(self.window)

    def run(self):
        self.window.set_background_color([0, 0, 0])
        self.cron_fps += self.window.delta_time()
        self.fps += 1

        if self.cron_fps > 1:
            self.actual_fps = self.fps
            self.fps = 0
            self.cron_fps = 0

        self.player.run()

        if self.kb.key_pressed("esc"):
            globals.GAME_STATE = 1
