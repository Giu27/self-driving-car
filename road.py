import pygame as pg
import os
from settings import *

class Track(pg.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.image = pg.image.load(os.path.join(image)).convert_alpha()
        self.image.set_colorkey("white",pg.SRCALPHA)
        self.rect = self.image.get_frect(topleft=(0,0))
        self.mask = pg.mask.from_surface(self.image)