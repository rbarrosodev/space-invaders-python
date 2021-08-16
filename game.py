import globals
from PPlay.collision import *
from enemies import Enemies
from player import Player


class Game:
    def __init__(self, window):
        self.window = window
        self.fps = 0
        self.score = 0
        self.time = 0
        self.actual_fps = 0
        self.cron_fps = 0
        self.kb = window.get_keyboard()
        self.player = Player(self.window)
        self.enemy = Enemies(self.window)
        self.alive = True

    def enemy_collision_shot(self):
        for i in range(len(self.enemy.enemies_matrix)):
            for j in range(len(self.enemy.enemies_matrix[i])):
                for k in range(len(self.player.bullet_group)):
                    if(Collision.collided(self.player.bullet_group[k], self.enemy.enemies_matrix[i][j])):
                        self.score += int(globals.SCORE / self.time)
                        self.enemy.enemies_matrix[i].pop(j)
                        self.player.bullet_group.pop(k)
                        if(len(self.enemy.enemies_matrix[i])) == 0:
                            self.enemy.enemies_matrix.pop(i)
                        self.enemy.enemy_qnty -= 1
                        return

    def game_over_y(self):
        for i in range(len(self.enemy.enemies_matrix)):
            for j in range(len(self.enemy.enemies_matrix[i])):
                if self.enemy.enemies_matrix[i][j].y + self.enemy.enemies_matrix[i][j].height >= self.player.spaceship.y:
                    return True
        return False

    def run(self):
        self.window.set_background_color([0, 0, 0])
        self.window.draw_text(f"Score: {self.score}", 300, 10, 30, (255, 255, 255))
        self.window.draw_text(f"FPS: {self.actual_fps}", 500, 10, 30, (255, 255, 255))
        self.cron_fps += self.window.delta_time()
        self.fps += 1

        if self.cron_fps > 1:
            self.actual_fps = self.fps
            self.fps = 0
            self.cron_fps = 0

        if self.alive:
            self.enemy.run()
            self.player.run()
            self.enemy_collision_shot()

        if self.game_over_y():
            self.alive = False

        self.time += self.window.delta_time()

        if self.kb.key_pressed("esc"):
            globals.GAME_STATE = 1
