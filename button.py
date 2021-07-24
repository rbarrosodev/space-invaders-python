from PPlay.sprite import *
from PPlay.gameimage import *


class Button(Sprite):
    def __init__(self, image, x, y):
        Sprite.__init__(self, image, 1)
        GameImage.set_position(self, x, y)

    def vanish(self, x, y):
        self.set_position(x, y)