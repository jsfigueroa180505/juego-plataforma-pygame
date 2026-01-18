import pygame as pg
import sys

class Game:
    def __init__(self): #Funcion de inicializacion
        pg.init()
        pg.display.set_caption('Ninja Game') #cambia el nombre de la ventana del juego
        self.screen = pg.display.set_mode((640,480)) #crea la ventana del juego
        self.clock = pg.time.Clock() #crea un objeto reloj que permite controlar la velocidad de los FPS

    def run(self): #metodo que inicia y ejecuta el programa
        while True: #loop infinito para la generacion de FPS 
            for event in pg.event.get():
                if event.type() == pg.QUIT: #si el usuario presiona la X en la ventana cierra el juego
                    pg.quit()
                    sys.exit()

            pg.display.update() #muestra el fotograma dibujado 
            self.clock.tick(60) #limita el juego a 60FPS por maximo

Game().run() #crea el objeto Game para iniciar el juego