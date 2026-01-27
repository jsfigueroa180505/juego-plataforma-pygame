import pygame as pg

import sys

from scripts.utils import load_images
from scripts.tilemap import Tilemap

RENDER_SCALE = 2.0

class Editor:
    def __init__(self): 
        pg.init()

        pg.display.set_caption('Editor') 
        self.screen = pg.display.set_mode((640, 480)) 
        self.display = pg.Surface((320, 240))

        self.clock = pg.time.Clock() 
        
        self.assets = {
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decore': load_images('tiles/large_decor'),
            'stone': load_images('tiles/stone'),
        }

        self.movement = [False, False, False, False]
        
        self.tilemap = Tilemap(self, tile_size = 16)

        self.scroll = [0, 0]

        self.tile_list = list(self.assets)
        self.tile_group = 0
        self.tile_variant = 0

        self.clicking = False
        self.right_clicking = False
        self.shift = False
        
    def run(self):      
        while True: 
            self.display.fill((0, 0, 0))

            current_tile_img = self.assets[self.tile_list[self.tile_group]][self.tile_variant].copy()
            current_tile_img.set_alpha(100)

            self.display.blit(current_tile_img, (5, 5))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.clicking = True
                    if event.button == 3:
                        self.right_clicking = True
                    if self.shift:
                        if event.button == 4:
                            self.tile_variant = (self.tile_variant - 1) % len(self.assets[self.tile_list[self.tile_group]])
                        if event.button == 5:
                            self.tile_variant = (self.tile_variant + 1) % len(self.assets[self.tile_list[self.tile_group]])
                    else:
                        if event.button == 4:
                            self.tile_group = (self.tile_group - 1) % len(self.tile_list)
                            self.tile_variant = 0
                        if event.button == 5:
                            self.tile_group = (self.tile_group + 1) % len(self.tile_list)
                            self.tile_variant = 0
                            
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        self.movement[0] = True
                    if event.key == pg.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pg.K_UP:
                        self.movement[2] = True
                    if event.key == pg.K_DOWN:
                        self.movement[3] = True  
                    if event.key == pg.K_LSHIFT:
                        self.shift = True 
                if event.type == pg.KEYUP:
                    if event.key == pg.K_LEFT:
                        self.movement[0] = False
                    if event.key == pg.K_RIGHT:
                        self.movement[1] = False
                    if event.key == pg.K_UP:
                        self.movement[2] = False
                    if event.key == pg.K_DOWN:
                        self.movement[3] = False 
                    if event.key == pg.K_LSHIFT:
                        self.shift = False 
            
            self.screen.blit(pg.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pg.display.update() 
            self.clock.tick(60) 

Editor().run() 