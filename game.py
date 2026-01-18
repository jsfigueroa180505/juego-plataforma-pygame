import pygame as pg
import sys

class Game:
    def __init__(self): #Funcion de inicializacion
        pg.init()
        pg.display.set_caption('Ninja Game') 
        self.screen = pg.display.set_mode((640, 480)) 
        self.clock = pg.time.Clock() 
        self.img = pg.image.load('data/images/clouds/cloud_1.png')
        self.img.set_colorkey((0, 0, 0))
        self.img_pos = [160, 260]
        self.movement = [False, False]
        self.collision_area = pg.Rect(50, 50, 300, 50)

    def run(self): #metodo que inicia y ejecuta el programa
        while True: 
            self.screen.fill((14, 219, 248))
            img_r = pg.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())

            if img_r.colliderect(self.collision_area):
                pg.draw.rect(self.screen, (0, 100, 255), self.collision_area)
            else:
                pg.draw.rect(self.screen, (0, 50, 155), self.collision_area)
               
            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5
            self.screen.blit(self.img, self.img_pos)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        self.movement[0] = True
                    if event.key == pg.K_DOWN:
                        self.movement[1] = True
                if event.type == pg.KEYUP:
                    if event.key == pg.K_UP:
                        self.movement[0] = False
                    if event.key == pg.K_DOWN:
                        self.movement[1] = False



            pg.display.update() 
            self.clock.tick(60) 

Game().run() 