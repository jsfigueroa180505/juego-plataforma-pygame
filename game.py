import pygame as pg
import sys
from scripts.entity import PhysicsEntity

class Game:
    def __init__(self): #Funcion de inicializacion
        pg.init()
        pg.display.set_caption('Ninja Game') 
        self.screen = pg.display.set_mode((640, 480)) 
        self.clock = pg.time.Clock() 
        self.movement = [False, False]
        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))
        
    def run(self): #metodo que inicia y ejecuta el programa
        while True: 
            self.screen.fill((14, 219, 248))
            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.screen)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        self.movement[0] = True
                    if event.key == pg.K_RIGHT:
                        self.movement[1] = True
                if event.type == pg.KEYUP:
                    if event.key == pg.K_LEFT:
                        self.movement[0] = False
                    if event.key == pg.K_RIGHT:
                        self.movement[1] = False

            pg.display.update() 
            self.clock.tick(60) 

Game().run() 