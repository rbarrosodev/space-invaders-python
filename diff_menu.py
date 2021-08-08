from PPlay.gameimage import *
from PPlay.mouse import *
from button import Button
import globals


class DiffMenu:
    def __init__(self, window):
        self.background = GameImage("img/background.png")
        self.easy_btn = Button("img/diff_menu/easy.png", 210, 80)
        self.medium_btn = Button("img/diff_menu/medium.png", 210, 160)
        self.hard_btn = Button("img/diff_menu/hard.png", 210, 240)
        self.back_btn = Button("img/diff_menu/back.png", 30, 80)
        self.mouse = Mouse()
        self.window = window

    def run(self):
        self.background.draw()
        self.easy_btn.draw()
        self.medium_btn.draw()
        self.hard_btn.draw()
        self.back_btn.draw()

        if self.mouse.is_over_object(self.back_btn):
            if self.mouse.is_button_pressed(1):
                globals.GAME_STATE = 1

        if self.mouse.is_over_object(self.easy_btn):
            if self.mouse.is_button_pressed(1):
                globals.shot_cooldown = 0.4
                globals.vel_enemies = 0.4
                self.window.draw_text("Dificuldade alterada para Fácil", (self.window.width / 2) - 200, 375, 30,
                                      [255, 255, 255])
        if self.mouse.is_over_object(self.medium_btn):
            if self.mouse.is_button_pressed(1):
                globals.shot_cooldown = 0.7
                globals.vel_enemies = 0.55
                self.window.draw_text("Dificuldade alterada para Médio", (self.window.width / 2) - 200, 375, 30,
                                      [255, 255, 255])
        if self.mouse.is_over_object(self.hard_btn):
            if self.mouse.is_button_pressed(1):
                globals.shot_cooldown = 1
                globals.vel_enemies = 0.65
                self.window.draw_text("Dificuldade alterada para Dificil", (self.window.width / 2) - 200, 375, 30,
                                      [255, 255, 255])

