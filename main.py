from settings import *
from car import Car
from road import Point, Segment
import sys
import pygame as pg

pg.init()
pg.font.init()
debug = False

screen = pg.display.set_mode((WIDTH,HEIGHT),0,32)
pg.display.set_caption("Self Driving Car")
clock = pg.time.Clock()

font = pg.font.SysFont(None,FONT_SIZE)

cars = pg.sprite.Group()
cars.add(Car("Player",(WIDTH //2,HEIGHT//2),0,True))

points = pg.sprite.Group()
points.add(Point((100,100),RADIUS),Point((200,200),RADIUS),Point((300,300),RADIUS))
segments = pg.sprite.Group()
segments.add(Segment((points.sprites()[0],points.sprites()[1]),SEG_WIDTH),Segment((points.sprites()[1],points.sprites()[2]),SEG_WIDTH))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                debug = not debug 

    screen.fill("white")
    points.draw(screen)
    segments.draw(screen)
    cars.update()
    cars.draw(screen)
    if debug and DEBUG:
        for sprite in cars:
            pg.draw.rect(screen,"red",sprite.rect,2)
            screen.blit(sprite.mask.to_surface(setcolor="purple",unsetcolor=None),sprite.rect)
        for sprite in points:
            pg.draw.rect(screen,"red",sprite.rect,2)
            screen.blit(sprite.mask.to_surface(setcolor="purple",unsetcolor=None),sprite.rect)
        for sprite in segments:
            pg.draw.rect(screen,"red",sprite.rect,2)
            screen.blit(sprite.mask.to_surface(setcolor="purple",unsetcolor=None),sprite.rect)
        fps = int(clock.get_fps())
        fps_surf = font.render(f"FPS: {fps}",True,"black")
        screen.blit(fps_surf,(WIDTH - 3 * FONT_SIZE,FONT_SIZE))
    pg.display.update()
    clock.tick(FPS)