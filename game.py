import globals
from PPlay.animation import *
from PPlay.collision import *
from enemies import Enemies
from player import Player


class Game:
    def __init__(self, window):
        self.window = window
        self.score = 0
        self.time = 0
        self.fps = 0
        self.actual_fps = 0
        self.cron_fps = 0
        self.kb = window.get_keyboard()
        self.player = Player(self.window)
        self.enemy = Enemies(self.window)
        self.alive = True

        self.dead_player = Animation("img/spaceship-respawn.png", 12)
        self.dead_player.set_total_duration(1000)
        self.death_cron = 1

        self.cooldown_player = Animation("img/spaceship-frozen.png", 1)
        self.cooldown_player.set_total_duration(3000)
        self.cooldown_cron = 1

    def reset(self):
        self.score = 0
        self.alive = True
        self.enemy = Enemies(self.window)
        self.player = Player(self.window)
        self.death_cron = 1
        globals.level = 1

    def next_level(self):
        self.enemy = Enemies(self.window)
        self.player = Player(self.window)
        self.death_cron = 1
        globals.level += 1
        self.time = 0

    def enemy_collision_shot(self):
        for i in range(len(self.enemy.enemies_matrix)):
            for j in range(len(self.enemy.enemies_matrix[i])):
                for k in range(len(self.player.bullet_group)):
                    if Collision.collided(self.player.bullet_group[k], self.enemy.enemies_matrix[i][j]):
                        self.score += int(globals.SCORE / self.time)
                        self.enemy.enemies_matrix[i].pop(j)
                        self.player.bullet_group.pop(k)
                        if (len(self.enemy.enemies_matrix[i])) == 0:
                            self.enemy.enemies_matrix.pop(i)
                        self.enemy.enemy_qnty -= 1
                        return

    def game_over_y(self):
        for i in range(len(self.enemy.enemies_matrix)):
            for j in range(len(self.enemy.enemies_matrix[i])):
                if self.enemy.enemies_matrix[i][j].y + self.enemy.enemies_matrix[i][j].height >= self.player.spaceship.y:
                    return True
        return False

    def player_collision_shot(self):
        for i in range(len(self.enemy.bullet_group)):
            if Collision.collided(self.enemy.bullet_group[i], self.player.spaceship):
                self.player.lifes -= 1
                self.enemy.bullet_group.pop(i)
                self.death_cron = 0
                self.dead_player.set_curr_frame(0)
                self.dead_player.set_position(self.player.spaceship.x, self.player.spaceship.y)
                if self.player.lifes != 0:
                    self.respawn()
                break

    def respawn(self):
        self.player.spaceship.set_position(self.window.width / 2 - self.player.spaceship.width / 2,
                                           self.window.height - 50)

    def game_over(self):
        file = open('ranking.txt', 'r')
        content = file.readlines()
        name = str(input('Digite seu nome: '))
        line = name + ' ' + str(globals.diff) + ' ' + str(int(self.score)) + '\n'
        content.append(line)
        file.close()
        file = open('ranking.txt', 'w')
        file.writelines(content)
        file.close()
        print('Ranking atualizado com sucesso')
        self.enemy = Enemies(self.window)
        self.player = Player(self.window)
        self.reset()
        globals.GAME_STATE = 1

    def run(self):
        print(self.player.shots)
        self.window.set_background_color([0, 0, 0])
        self.window.draw_text("Vidas: " + str(self.player.lifes), 50, 10, 28, (255, 255, 255))
        self.window.draw_text(f"Score: {self.score}", 200, 10, 30, (255, 255, 255))
        self.window.draw_text(f"FPS: {self.actual_fps}", 400, 10, 30, (255, 255, 255))
        self.window.draw_text(f"Level: {globals.level}", 600, 10, 30, (255, 255, 255))
        self.cron_fps += self.window.delta_time()
        self.fps += 1

        if self.cron_fps > 1:
            self.actual_fps = self.fps
            self.fps = 0
            self.cron_fps = 0

        if self.alive:
            self.enemy.run()
            self.player.run()
            self.player_collision_shot()
            self.enemy_collision_shot()

            if self.game_over_y() or self.player.lifes == 0:
                self.game_over()
                self.alive = False
                globals.GAME_STATE = 1
                self.reset()

            if self.enemy.enemy_qnty == 0:
                self.next_level()

            self.time += self.window.delta_time()

            if self.kb.key_pressed("esc"):
                globals.GAME_STATE = 1
                self.reset()

        else:
            self.game_over()

        if self.player.shots == 10:
            self.cooldown_player.set_position(self.player.spaceship.x, self.player.spaceship.y)
            self.cooldown_player.draw()
            self.cooldown_cron += self.window.delta_time()
            if self.cooldown_cron >= 3:
                self.cooldown_cron = 0
                self.player.shots = 0
                self.player.spaceship.draw()


        if self.death_cron < 0.9:
            self.dead_player.draw()
            self.dead_player.update()
            self.death_cron += self.window.delta_time()
