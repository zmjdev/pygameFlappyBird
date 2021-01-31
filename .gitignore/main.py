import pygame as pg
from settings import *
import sprites
import random

vec = pg.math.Vector2


class Game:
    def __init__(self):
        self.running = True
        self.playing = True
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("FlappyBird")
        self.all_sprites = pg.sprite.Group()
        self.pillars = pg.sprite.Group()

    def new(self):
        dist_bet_Pillars = 0
        space = 110
        self.bird = sprites.Bird(self)
        self.all_sprites.add(self.bird)
        self.all_sprites.add(self.pillars)
        for i in range(0, 10):
            height = int(random.randrange(0, HEIGHT / 2))
            for j in range(2):
                if j % 2 == 0:
                    pillar = sprites.Pillar(60, height, vec(WIDTH + dist_bet_Pillars, 0))
                    self.pillars.add(pillar)
                    self.all_sprites.add(pillar)
                    print(height)
                else:
                    pillar = sprites.Pillar(60, HEIGHT - (height + space),
                                            vec(WIDTH + dist_bet_Pillars, height + space))
                    self.pillars.add(pillar)
                    self.all_sprites.add(pillar)
                    dist_bet_Pillars += 200
                    print(height)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False
        # dist_bet_Pillars = 140
        # space = 120
        # while len(self.pillars.sprites()) < 8:
        #     height = int(random.randrange(0, 3 * HEIGHT / 4))
        #     for j in range(2):
        #         if j % 2 == 0:
        #             pillar = sprites.Pillar(60, height, vec(WIDTH + dist_bet_Pillars, 0))
        #             self.pillars.add(pillar)
        #             self.all_sprites.add(pillar)
        #             print(height)
        #         else:
        #             pillar = sprites.Pillar(60, HEIGHT - (height + space),
        #                                     vec(WIDTH + dist_bet_Pillars, height + space))
        #             self.pillars.add(pillar)
        #             self.all_sprites.add(pillar)
        #             dist_bet_Pillars += 200

    def update(self):
        dist_bet_Pillars = 140
        space = 120
        while len(self.pillars.sprites()) < 8:
            height = int(random.randrange(0, 3 * HEIGHT / 4))
            for j in range(2):
                if j % 2 == 0:
                    pillar = sprites.Pillar(60, height, vec(WIDTH + dist_bet_Pillars, 0))
                    self.pillars.add(pillar)
                    self.all_sprites.add( pillar)
                    print(height)
                else:
                    pillar = sprites.Pillar(60, HEIGHT - (height + space),
                                            vec(WIDTH + dist_bet_Pillars, height + space))
                    self.pillars.add(pillar)
                    self.all_sprites.add(pillar)
                    dist_bet_Pillars += 200
        pg.display.update()
        self.all_sprites.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)

    def run(self):
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()
            self.update()


game = Game()

while game.running:
    game.new()
    game.run()
pg.quit()
