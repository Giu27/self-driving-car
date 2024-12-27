from settings import *
from car import Car
import sys,os
import pygame as pg
import numpy as np

pg.init()
pg.display.init()

screen = pg.display.set_mode((WIDTH,HEIGHT),0,32)
pg.display.set_caption("Self Driving Car")
clock = pg.time.Clock()

cars = pg.sprite.Group()
cars.add(Car("player"))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.fill("white")
    cars.update()
    cars.draw(screen)
    pg.display.update()
    clock.tick(FPS)