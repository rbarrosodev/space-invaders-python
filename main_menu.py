from PPlay.gameimage import *
from PPlay.mouse import *
from button import Button
import globals


class MainMenu:
    def __init__(self):
        self.background = GameImage("img/background.png")
        self.play_btn = Button("img/main_menu/play.png", 210, 80)
        self.difficulty_btn = Button("img/main_menu/difficulty.png", 210, 160)
        self.ranking_btn = Button("img/main_menu/ranking.png", 210, 240)
        self.exit_btn = Button("img/main_menu/exit.png", 210, 320)
        self.mouse = Mouse()

    def run(self):
        self.background.draw()
        self.play_btn.draw()
        self.difficulty_btn.draw()
        self.ranking_btn.draw()
        self.exit_btn.draw()

        if self.mouse.is_over_object(self.play_btn):
            if self.mouse.is_button_pressed(1):
                globals.GAME_STATE = 0
        if self.mouse.is_over_object(self.difficulty_btn):
            if self.mouse.is_button_pressed(1):
                globals.GAME_STATE = 2
        if self.mouse.is_over_object(self.ranking_btn):
            if self.mouse.is_button_pressed(1):
                globals.GAME_STATE = 4
        if self.mouse.is_over_object(self.exit_btn):
            if self.mouse.is_button_pressed(1):
                globals.GAME_STATE = 5
