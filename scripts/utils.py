import pygame as pg

BASE_IMAGE_PATH = 'data/images/'

def load_image(path):#funcion para llamar una imagen concreta  
    img = pg.image.load(BASE_IMAGE_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img  