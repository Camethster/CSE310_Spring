import pygame as pg
import sys
import random
from os import path

from pygame.constants import K_ESCAPE, QUIT
from player import *
from pygame.locals import *
from settings import *




class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.map_data = []
        self.load_data()
        

    def load_data(self):
        game_folder = path.dirname(__file__)
        with open(path.join(game_folder,'mapdot.txt'),'rt') as f:
            for line in f:
                self.map_data.append(line)

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.computer = pg.sprite.Group()
        self.contestants = []
        for row,tiles in enumerate(self.map_data):
            for col,tile in enumerate(tiles):
                if tile == '1':
                    Wall(self,col,row)
                elif tile =='P':
                    self.player = Player(self, col, row)
                    self.contestants.append(self.player)
                elif tile =='C':
                   self.contestants.append(Computer(self,col,row))

    def computer_move(self):
        for i,comp in enumerate(self.contestants):
            if isinstance(comp,Player):
                continue
            rand_move = random.randint(-1,1)
            vert = random.randint(0,1)
            if vert == 0:
                comp.move(rand_move)
            else:
                comp.move(0,rand_move)

    def check_win(self):
        pass


    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.computer_move()
            self.update()
            self.draw()
            self.check_win()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key in (pg.K_LEFT, pg.K_a):
                    self.player.move(dx=-1)
                if event.key in (pg.K_RIGHT, pg.K_d):
                    self.player.move(dx=1)
                if event.key in (pg.K_UP, pg.K_w):
                    self.player.move(dy=-1)
                if event.key in (pg.K_DOWN, pg.K_s):
                    self.player.move(dy=1)
            break

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()

""" #Define Game Resolution
clock =py.time.Clock()
status =py.Rect(0,0,720,72)
player_pic =py.image.load("C:/git/CSE310_Spring/SurvivalRoyal/images/avatar.png").convert()
player_pic =py.transform.scale(player_pic,(int(res[0]/10),int(res[1]/10)))
background =py.image.load('C:/git/CSE310_Spring/SurvivalRoyal/images/bush.png').convert()
background =py.transform.scale(background,(int(res[0]/10),int(res[1]/10)))
music =py.mixer.music.load("C:/git/CSE310_Spring/SurvivalRoyal/music/Jim Hall - The Contra Chop.mp3")
avatar = Player(player_pic,0)
players = []
players.append(avatar)
computers = []
events = []py.mixer.music.set_volume(.1)py.mixer.music.play(loops=-1, start=0.0, fade_ms = 0)py.display.set_caption("Survival Royal")

game = True
while game:
    for ev inpy.event.get():
        if ev.type in (QUIT,K_ESCAPE):
        py.quit()
            sys.exit()
            quit()
    keys =py.key.
    for key in keys:
        print (key)
    for x in range(72):
        for y in range(72):
            screen.blit(background,(x*100,y*100))
    for o in players:
        screen.blit(background,o.pos,o.pos)
    for o in players:
        o.move(keys)
        screen.blit(o.img,o.pos)
    
py.display.update()
py.time.delay(5000)


if notpy.font: print('Warning, fonts disabled')
if notpy.mixer: print('Warning, sound disabled')
 """

""" def text_object(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def game_intro():
    intro = True
    while intro:
        for ev inpy.event.get():
            if ev.type ==py.QUIT():
            py.quit()
                quit()
        gameDisplay.fill(white)
        largeText =py.font.Font("comicsans",30)
        TextSurf, TextRect = text_object("Survival Royal", largeText)
        TextRect.center = ((res[0]/2),(res[1]/2))
        gameDisplay.blit(TextSurf,TextRect)
    py.display.update()
        clock.tick(15)

#Window loop
def game_loop():
    while True:
        for ev inpy.event.get():
            if ev.type ==py.QUIT():
            py.quit()
                quit()

if __name__ == "__main__":
    game_intro() """