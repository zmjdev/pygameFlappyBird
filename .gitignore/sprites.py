import pygame as pg
from settings import *

vec = pg.math.Vector2


class Bird(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.width = 30
        self.height = 30
        self.pos = vec(WIDTH / 3, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.image = pg.Surface((self.width, self.height))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 3, HEIGHT / 2)

    def update(self):
        self.acc = vec(self.acc.x, GRAVITY)
        keys = pg.key.get_pressed()
        if self.is_hit():
            print('hit')

        if keys[pg.K_SPACE]:
            self.move_up()
        self.fall()

    def fall(self):
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.center = self.pos

    def move_up(self):
        self.vel.y = FLAPPY_SPEED

    def is_hit(self):
        hits = pg.sprite.spritecollide(self, self.game.pillars, False)
        if hits:
            hits[0].image.fill((255,0,0))
            return True
        else:
            return False


class Pillar(pg.sprite.Sprite):
    def __init__(self, width, height, pos=vec()):
        pg.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.pos = pos
        self.vel = vec(0, 0)
        # self.acc = vec(0, 0)
        self.image = pg.Surface((self.width, self.height))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.midtop = (self.pos.x, self.pos.y)

    def update(self):
        self.move()
        if self.is_boundary_hit():
            self.remove()

    def move(self):
        self.vel.x = -2
        self.pos.x += self.vel.x
        self.rect.midtop = (self.pos.x, self.pos.y)
    def is_boundary_hit(self):
        if self.pos.x<=0:
            return True
        else:
            return False
    def remove(self):
        self.kill()