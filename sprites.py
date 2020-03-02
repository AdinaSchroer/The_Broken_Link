#sprite classes for platform game
import pygame as pg
from settings import *
from settings import BLACK
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.image.load("thicc.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 46
        pg.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.center = (WIDTH / 2, HEIGHT / 1)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        #self.shield = 100
        #self.lives = 3

    def jump(self):
        #jump only if standing on platform
        self.rect.y += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 1
        if hits:
            self.vel.y = -21.5

    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION

        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc #equation of motion

        # wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 1395
        if self.pos.x < 0:
            self.pos.x = 5

        # calculated position of the player
        self.rect.midbottom = self.pos

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(ROAD)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Mob(pg.sprite.Sprite):
    
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(1):
            img = pg.image.load("car.png").convert()
            self.images.append(img)
            self.image = self.images[0]
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.radius = 100
            pg.draw.circle(self.image, RED, self.rect.center, self.radius)
            self.rect.center = (WIDTH / 3, HEIGHT / 1.17)
            self.Mob_speed = 20
            self.center = float(self.Mob_speed)
            print("self.images has this many elements:", len(self.images))

            self.index = 0
            self.image = self.images[self.index]

    def update(self):
        self.rect.x -= 15
        if self.rect.right < 0:
            self.rect.right = 0
            self.rect.left = 2000
            self.speedx = 15

class Shield(pg.sprite.Sprite):
    '''create Shield class'''
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        super().__init__()
        img = pg.image.load("test.jpg").convert()
        self.center = center
        self.rect = self.image.get_rect(center=(self.center))
        self.player = player
    
    def update(self):
        '''update shield location'''
        self.rect.centerx = self.player.rect.centerx
        self.rect.centery = self.player.rect.centery

        if self.player.shield <= 30:
            self.rect.center = (WIDTH/2, HEIGHT + 115)
        elif self.player.shield > 30:
            self.rect.centerx = self.player.rect.centerx
            self.rect.centery = self.player.rect.centery
