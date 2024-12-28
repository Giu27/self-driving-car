from settings import *
from car import Car
import sys
import pygame as pg

pg.init()
pg.display.init()
debug = False

screen = pg.display.set_mode((WIDTH,HEIGHT),0,32)
pg.display.set_caption("Self Driving Car")
clock = pg.time.Clock()

cars = pg.sprite.Group()
cars.add(Car("Player",(WIDTH //2,HEIGHT//2),0,True),Car("AI",(220,300),227,True))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                debug = not debug 

    screen.fill("white")
    cars.update()
    cars.draw(screen)
    if debug:
        for sprite in cars:
            pg.draw.rect(screen,"red",sprite.rect,2)
            screen.blit(sprite.mask.to_surface(setcolor="purple",unsetcolor=None),sprite.rect)
    pg.display.update()
    clock.tick(FPS)