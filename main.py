#main.py
import pygame as pg
import random
import os
import time
from map_list import *

clock = pg.time.Clock()
pg.init()
pg.event.get()
pg.font.init()
img = intro_img
img2 = main_img

from settings import *
from sprites import *

#music
#pg.mixer.music.load('tetris.wav')
#pg.mixer.music.play(-1)


click = pg.mouse.get_pressed()
print(click)


#"game loop"             
class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('The Broken Link')
        self.background_image = pg.image.load(img2).convert()

        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

#sets up the game
    def new(self):
        print("inside new()")
        #self.screen.blit(self.background_image, [0, 0])
        self.background_image = pg.image.load(img2).convert()
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.mob = pg.sprite.Group()
        self.player = Player(self) #send Player reference to Game
        #self.health_bars = pg.sprite.Group()
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(*plat) #"exploding the list using *"
            self.all_sprites.add(p)
            self.platforms.add(p) 
        black_bar = pg.Surface((WIDTH, 35))
        #health_bars = self.player_health
        # spawn mob
        for i in range(1):
            m = Mob()
            self.all_sprites.add(m)
            self.mob.add(m)
        self.run() #<-- used to be inside the for loop

    def button(self, msg, x, y, w, h, ic, ac, action=None):
        mouse = pg.mouse.get_pos() 
        click = pg.mouse.get_pressed()
        #print(click)
        #print("click")

        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pg.draw.rect(self.screen, ac,(x,y,w,h))
            
            if click[0] == 1 and action != None:
                if action == "play":
                    self.start()
                    self.background_image = pg.image.load(img).convert()
                elif action == "quit":
                    pg.quit()
                elif action == "continue":
                    self.start()
                
        else:
            pg.draw.rect(self.screen, ic, (x,y,w,h))
        
        smallText = pg.font.Font("freesansbold.ttf",20)
        textSurf, textRect = self.text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        self.screen.blit(textSurf, textRect)

    #for words
    def text_objects(self, text, font):
        textSurface = font.render(text, True, BLACK)
        return textSurface, textSurface.get_rect()


    def message_display(self, text):
        largeText = pg.font.Font('smashfont.ttf',115)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((WIDTH / 2),( HEIGHT / 2))
        self.screen.blit(TextSurf, TextRect)
 
        pg.display.update()
 
        time.sleep(2)

    #title screen 
    def game_intro(self):
        intro = True
        
        while intro:
            for event in pg.event.get():
                #print(event)
                if event.type == pg.QUIT:
                    pg.quit
                    quit()

                    
            self.background_image = pg.image.load(img).convert()
            self.screen.blit(self.background_image, [0, 0])
            largeText = pg.font.Font('smashfont.ttf',115)
            TextSurf, TextRect = self.text_objects('THE BROKEN LINK', largeText)
            TextRect.center = (( WIDTH / 2),( HEIGHT / 2))
            self.screen.blit(TextSurf, TextRect)
            #self.screen.fill(WHITE)



            #mouse = pg.mouse.get_pos()

            #def button(msg,x,y,w,h,ic,ac)#
            self.button("PLAY!", 550, 600, 100, 50, GREEN, BRIGHTCOLOR, "play")
            self.button("QUIT", 750, 600, 100, 50, RED, BRIGHTCOLOR, "quit")

            #for the words on the play button
            smallText = pg.font.Font("freesansbold.ttf",20)
            textSurf, textRect = self.text_objects("PLAY!", smallText)
            textRect.center = ( (550+(100/2)), (600+(50/2)) )
            self.screen.blit(textSurf, textRect)

            pg.display.update()
            clock.tick(15)


            

    def pause(self):

        largeText = pg.font.Font("smashfont.ttf",115)
        TextSurf, TextRect = self.text_objects("Pawsed", largeText)
        TextRect.center = (( WIDTH / 2),( HEIGHT / 2))
        self.screen.blit(TextSurf, TextRect)
    

        while self.paused:
            for event in pg.event.get():

                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
               

            self.button("Continue", 550, 600, 100, 50, GREEN, BRIGHTCOLOR, "play")
            self.button("Quit", 750, 600, 100, 50, RED ,BRIGHTCOLOR, "quit")

            pg.display.update()
            clock.tick(15)

    def game_over(self):
        over = True
        
        while over:
            for event in pg.event.get():
                #print(event)
                if event.type == pg.QUIT:
                    pg.quit
                    quit()

                    
            self.background_image = pg.image.load(img).convert()
            self.screen.blit(self.background_image, [0, 0])
            largeText = pg.font.Font('smashfont.ttf',115)
            TextSurf, TextRect = self.text_objects('GAME OVER!', largeText)
            TextRect.center = (( WIDTH / 2),( HEIGHT / 2))
            self.screen.blit(TextSurf, TextRect)
            #self.screen.fill(WHITE)

            #mouse = pg.mouse.get_pos()

            #def button(msg,x,y,w,h,ic,ac)#
            self.button("TRY AGAIN", 550, 600, 150, 50, GREEN, BRIGHTCOLOR, "play")
            self.button("QUIT", 750, 600, 100, 50, RED, BRIGHTCOLOR, "quit")

            #for the words on the play button
            smallText = pg.font.Font("freesansbold.ttf",20)
            TextRect.center = ( (550+(100/2)), (600+(50/2)) )

            pg.display.update()
            clock.tick(15)
                        

    
#runs the game
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events() 
            self.update()
            self.draw()
            #self.over()

    def health_bars(self, player_health):

        if self.player.health > 75:
            self.player_health_color = GREEN
        elif self.player.health > 50:
            self.player_health_color = YELLOW
        else:
            self.player_health_colro = RED
        
        pg.draw.rect(gameDisplay, self.player_health_color, (680, 25, self.player_health, 25))


    clock.tick(40)
    '''
    def shield_bar(surface, player_shield):
        #display the graphic and track shield for the player
        if player_shield > 100:
            player_shield_color = GREEN
            player_shield = 100
        elif player_shield > 75:
            player_shield_color = GREEN
        elif player_shield > 50:
            player_shield_color = YELLOW
        else:
            player_shield_color= RED

        pg.draw.rect(screen, ROAD, (5, 5, 104, 24), 3)
        pg.draw.rect(screen, player_shield_color, (7, 7, player_shield, 20))
'''
    

            
    def update(self):
        #print("running update()")
        self.all_sprites.update()

        #check to see if a mob hit the player
        hits = pg.sprite.spritecollide(self.player, self.mob, False, pg.sprite.collide_circle)
        if hits:
            self.game_over() 
            self.playing = False
            self.running = False
            self.over = True

            self.player_health = 100


        #check if player hits platform - only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top + 1
                self.player.vel.y = 0

        # scroll if player reaches top 1/4 of screen
        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()

        # spawn new platforms
        while len(self.platforms) < 6:
            width = random.randrange(50, 100)
            p = Platform(random.randrange(0, WIDTH - width),
                         random.randrange(-75, -30),
                         width,
                         20)
            self.platforms.add(p)
            self.all_sprites.add(p)

    def events(self):
        for event in pg.event.get():
            #check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                if self.playing == False:
                    self.over = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
                if event.key == pg.K_p:
                    self.paused = True
                    self.pause()
                #if event.key == pg.K_q:
                   #self.background_image = pg.image.load(img2).convert()

                
    def draw(self):    
        self.screen.blit(self.background_image, [0, 0])
        self.health_bars(self.player_health)
        self.all_sprites.draw(self.screen)
        black_bar = pg.Surface((WIDTH, 35))
        self.screen.blit(black_bar, (0,0))
        pg.draw.rect(self.screen, ROAD, (0, 0, WIDTH, 35), 5)
        self.draw
        #self.shield_bar(self.screen, self.player.shield)

        # *after* drawing everything flip the display
        pg.display.flip()

    def start(self):
        self.new()

g = Game()
g.game_intro()
while g.running:
    g.new()
pg.quit()
