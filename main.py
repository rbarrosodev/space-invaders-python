from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.window import *
from main_menu import MainMenu
from diff_menu import DiffMenu
from game import Game
import globals
from ranking import Ranking

window = Window(800, 600)
window.set_title("Space Invaders")
background = GameImage("img/background.png")
spaceship = Sprite("img/spaceship.png")
bullet = Sprite("img/bullet.png")
main_menu = MainMenu()
diff_menu = DiffMenu(window)
ranking_menu = Ranking(window)
game = Game(window)

while globals.GAME_STATE != 5:
    if globals.GAME_STATE == 0:
        game.run()
    if globals.GAME_STATE == 1:
        main_menu.run()
    elif globals.GAME_STATE == 2:
        diff_menu.run()
    elif globals.GAME_STATE == 4:
        ranking_menu.run()

    window.update()
