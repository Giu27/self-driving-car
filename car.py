import pygame as pg
import math,random
from settings import *
class Car(pg.sprite.Sprite):
    def __init__(self,type,pos,angle,colCars):
        super().__init__()
        self.type = type
        self.original_image = pg.Surface(SIZE,pg.SRCALPHA)
        if type == "Player":
            self.original_image.fill(PLAYER_COLOR)
        else:
            self.original_image.fill(random.choice(AI_COLORS))
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.angle = angle
        self.speed = 0
        self.max_speed = MAX_SPEED
        self.acceleration = ACCELERATION
        self.deceleration = DECELERATION
        self.rotation_speed = ROTATION_SPEED
        self.live = True
        self.collide_with_cars = colCars
        if self.type == "AI":
            pass #self.brain = Network()
    
    def player_input(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.accelerate()
        elif keys[pg.K_s]:
            self.decelerate()
        else: self.slow_down()

        if keys[pg.K_a]:
            self.rotate(-1)
        if keys[pg.K_d]:
            self.rotate(1)
        
    def accelerate(self):
        self.speed = min(self.speed + self.acceleration, self.max_speed)

    def decelerate(self):
        self.speed = max(self.speed - self.deceleration, -self.max_speed / 2)

    def slow_down(self):
        if self.speed > 0:
            self.speed = max(0, self.speed - self.deceleration/2)
        elif self.speed < 0:
            self.speed = min(0, self.speed + self.deceleration / 2)

    def rotate(self,direction):
        self.angle += self.rotation_speed * direction
        self.angle %= 360

    def move(self):
        self.rect.x += self.speed * math.cos(math.radians(self.angle))
        self.rect.y += self.speed * math.sin(math.radians(self.angle))

        self.image = pg.transform.rotate(self.original_image,-self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
    
    def check_collisions(self, collide_with_other_cars):
        #Window border collisions
        if self.rect.x < 0 or self.rect.right > WIDTH:
            self.live = False
        if self.rect.y < 0 or self.rect.bottom > HEIGHT:
            self.live = False
        #collisioni con altre auto
        if collide_with_other_cars:
            collision_list = pg.sprite.spritecollide(self,self.groups()[0],False)
            for sprite in collision_list:
                if sprite != self:
                    self.live = False
                    break

    def update(self):
        if self.live:
            if self.type == "Player":
                self.player_input()
            self.check_collisions(self.collide_with_cars)
        else:
            self.original_image.fill(DEATH_COLOR)
            self.speed = 0
        self.move()