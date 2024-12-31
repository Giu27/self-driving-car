import pygame as pg
from settings import *
import math

class Point(pg.sprite.Sprite):
    def __init__(self,pos,radius):
        super().__init__()
        self.x = pos[0]
        self.y = pos[1]
        self.radius = radius
        self.image = pg.Surface((radius * 2,radius *2),pg.SRCALPHA)
        pg.draw.circle(self.image,POINT_COLOR,(radius,radius),radius)
        self.rect = self.image.get_frect(center=(self.x,self.y))
        self.mask = pg.mask.from_surface(self.image)

class Segment(pg.sprite.Sprite):
    def __init__(self,points,width):
        super().__init__()
        self.points = points
        self.width = width
        self.dx = self.points[1].x - self.points[0].x
        self.dy = self.points[1].y - self.points[0].y
        self.lenght = math.sqrt(self.dx**2 + self.dy**2)
        self.angle = math.degrees(math.atan2(self.dy,self.dx))
        self.image = pg.Surface((self.lenght,self.width),pg.SRCALPHA)
        pg.draw.line(self.image,SEGMENT_COLOR,(0,self.width // 2),(self.lenght,self.width//2),self.width)
        self.image = pg.transform.rotate(self.image,-self.angle)
        self.rect = self.image.get_frect(center=((self.points[1].x + self.points[0].x)/2,(self.points[1].y + self.points[0].y)/2))
        self.mask = pg.mask.from_surface(self.image)