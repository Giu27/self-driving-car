import pygame as pg
from settings import *
class Car(pg.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        self.type = type
        self.image = pg.Surface(SIZE)
        self.image.fill("blue")
        self.rect = self.image.get_rect()
        self.max_speed = MAX_SPEED
        if self.type == "AI":
            pass #self.brain = Network()
    
    def update(self):
        pass