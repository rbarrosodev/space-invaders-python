from PPlay.gameimage import *
from PPlay.window import *
from main_menu import MainMenu
from diff_menu import DiffMenu
import globals

window = Window(800, 600)
window.set_title("Space Invaders")
background = GameImage("img/background.png")
main_menu = MainMenu()
diff_menu = DiffMenu()

while globals.GAME_STATE != 5:
    if globals.GAME_STATE == 1:
        main_menu.run()
    elif globals.GAME_STATE == 2:
        diff_menu.run()

    window.update()
