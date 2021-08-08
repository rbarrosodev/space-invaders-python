from PPlay.sprite import *
import globals


class Enemies(object):
    def __init__(self, wd):
        self.window = wd
        self.enemies_matrix = []
        self.col_size = 3 + globals.diff
        self.lin_size = 3 + globals.diff
        self.enemy_qnty = self.col_size * self.lin_size
        self.enemy_vel = (5 * globals.diff * self.window.delta_time() * 1) / self.enemy_qnty
        self.enemies_direction = 1

        self.cronometer = 0
        self.create()

    def create(self):
        for i in range(self.lin_size):
            self.enemies_matrix.append([])
            for j in range(self.col_size):
                if j % 4 == 0:
                    self.enemies_matrix[i].append(Sprite("img/yellowenemy.png"))
                elif j % 3 == 0:
                    self.enemies_matrix[i].append(Sprite("img/greenenemy.png"))
                elif j % 2 == 0:
                    self.enemies_matrix[i].append(Sprite("img/blueenemy.png"))
                else:
                    self.enemies_matrix[i].append(Sprite("img/redenemy.png"))
                self.enemies_matrix[i][j].set_position((j+1) * (self.window.width/(self.window.width / 60)), (i+1) * 50)

    def move_enemies_x(self):
        if self.enemy_qnty > 0:
            self.enemy_vel = (self.window.delta_time() * globals.FRAME_PER_SECOND) * self.enemies_direction + self.enemies_direction * globals.vel_enemies/2 + self.enemies_direction * 3 / self.enemy_qnty
        for i in range(len(self.enemies_matrix)):
            for j in range(len(self.enemies_matrix[i])):
                self.enemies_matrix[i][j].move_x(self.enemy_vel)

    def check_limits(self):
        for i in range(len(self.enemies_matrix)):
            for j in range(len(self.enemies_matrix[i])):
                if (self.enemies_matrix[i][j].x <= 0) or (self.enemies_matrix[i][j].x >= (self.window.width - self.enemies_matrix[i][j].width)):
                    return True
        return False

    def move_enemies_y(self):
        if self.cronometer > 0.15:
            if self.check_limits():
                self.enemies_direction = -self.enemies_direction
                for i in range(len(self.enemies_matrix)):
                    for j in range(len(self.enemies_matrix[i])):
                        self.enemies_matrix[i][j].y += 20
                self.cronometer = 0
        else:
            self.cronometer += self.window.delta_time()

    def draw_enemies(self):
        for i in range(len(self.enemies_matrix)):
            for j in range(len(self.enemies_matrix[i])):
                self.enemies_matrix[i][j].draw()

    def run(self):
        self.move_enemies_x()
        self.move_enemies_y()
        self.draw_enemies()
