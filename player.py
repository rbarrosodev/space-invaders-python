from PPlay.sprite import *
import globals


class Player:
    def __init__(self, wd):
        self.window = wd
        self.spaceship = Sprite("img/spaceship.png")
        self.bullet_group = []
        self.kb = self.window.get_keyboard()
        self.lifes = 6 - globals.diff
        self.cooldown = 0
        self.cooldown_shot = 0
        self.shots = 0
        self.spaceship.set_position(self.window.width / 2, self.window.height - 50)

    def shot(self):
        bullet = Sprite("img/bullet.png")
        bullet.set_position(self.spaceship.x + self.spaceship.width / 2 - bullet.width / 2, self.spaceship.y)
        self.bullet_group.append(bullet)
        self.shots += 1

    def update_shots(self):
        for i in range(len(self.bullet_group)):
            self.bullet_group[i].move_y(self.window.delta_time() * globals.FRAME_PER_SECOND * -7)

    def run(self):
        if self.kb.key_pressed("a"):
            if self.spaceship.x >= 0:
                self.spaceship.x -= globals.spaceship_vel * self.window.delta_time()
        if self.kb.key_pressed("d"):
            if (self.spaceship.x + self.spaceship.width) <= self.window.width:
                self.spaceship.x += globals.spaceship_vel * self.window.delta_time()

        if self.cooldown >= globals.shot_cooldown and self.shots != 10:
            if self.kb.key_pressed("space"):
                self.shot()
                self.cooldown = 0

        self.cooldown += self.window.delta_time()

        self.update_shots()

        self.spaceship.draw()
        for i in range(len(self.bullet_group)):
            self.bullet_group[i].draw()
