from PPlay.gameimage import GameImage
import globals


class Ranking(object):
    def __init__(self, wd):
        self.window = wd
        self.kb = self.window.get_keyboard()
        self.ranking = GameImage("img/ranking.png")
        self.set_pos()
        self.create()

    def set_pos(self):
        self.ranking.set_position(self.window.width / 2 - self.ranking.width / 2, 25)

    def create(self):
        self.window.set_background_color([0, 0, 0])
        self.ranking.draw()

    def run(self):
        self.create()
        file = open('ranking.txt', 'r')
        content = file.readlines()
        names = []
        pts = []
        for i in range(len(content)):
            line = content[i].split()
            names.append(line[0])
            pts.append(int(line[2].rstrip('\n')))
        file.close()
        for j in range(5):
            for i in range(len(pts) - 1):
                if pts[i] < pts[i + 1]:
                    pts[i + 1], pts[i] = pts[i], pts[i + 1]
                    names[i + 1], names[i] = names[i], names[i + 1]

        for i in range(len(names)):
            if i > 4:
                break
            self.window.draw_text("{} - {} - {} pontos".format(i + 1, names[i], pts[i]), 240, 150 + i * 50, 32,
                                  (255, 255, 255))

        if self.kb.key_pressed("esc"):
            globals.GAME_STATE = 1
