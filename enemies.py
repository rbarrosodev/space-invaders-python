import random

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

        self.bullet_group = []
        self.shot_cron = 0
        self.adv_cron = 0
        self.shot_vel = 2 + (70 / self.enemy_qnty) * 0.2 + (1 * 0.5)

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

    def shoot(self):
        if self.shot_cron > 4 / (globals.diff + (1 * 0.5)):
            selected = random.randint(0, self.enemy_qnty)
            aux = 0
            for i in range(len(self.enemies_matrix)):
                for j in range(len(self.enemies_matrix[i])):
                    aux += 1
                    if aux == selected:
                        shot = Sprite("img/bullet.png")
                        shot.set_position(self.enemies_matrix[i][j].x + self.enemies_matrix[i][j].width/2 - shot.width/2, self.enemies_matrix[i][j].y)
                        self.bullet_group.append(shot)
                        self.shot_cron = 0
                        return
        else:
            self.shot_cron += self.window.delta_time()

    def update_shots(self):
        self.shot_vel = 2 + (70 / self.enemy_qnty) * 0.2 + (1 * 0.5)
        for i in range(len(self.bullet_group)):
            self.bullet_group[i].move_y(self.window.delta_time() * globals.FRAME_PER_SECOND * self.shot_vel)
            if self.bullet_group[i].y <= 0:
                self.bullet_group.pop(i)
                break

    def draw_enemies(self):
        for i in range(len(self.enemies_matrix)):
            for j in range(len(self.enemies_matrix[i])):
                self.enemies_matrix[i][j].draw()
        for i in range(len(self.bullet_group)):
            self.bullet_group[i].draw()

    def run(self):
        self.move_enemies_x()
        self.move_enemies_y()
        self.shoot()
        self.update_shots()
        self.draw_enemies()
