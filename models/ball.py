import pygame
from models.racket import Racket

class Ball():
    def __init__(self, speed:float, size:int, width:int, height:int):
        self.speed = speed
        self.speed_vector = [speed, speed]
        self.size = size
        self.surface = pygame.Surface((size, size))
        self.surface.fill((255, 255, 255))
        self.rect = self.surface.get_rect()
        self.rect = self.rect.move(int(width/2),int(height/2))

    def touch_border(self, width, height):
        if self.rect.left < 0 or self.rect.right > width:
            self.speed_vector[0] = -self.speed_vector[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed_vector[1] = -self.speed_vector[1]
    
    def move(self):
        self.rect = self.rect.move(self.speed_vector)


    def has_collide(self, b_b, b_t, r_b, r_t):
        return (r_b <= b_t and b_t <= r_t) or (r_b <= b_b and b_b <= r_t)


    def touch_racket(self, racket1: Racket, racket2: Racket):
        b_t = self.rect.top
        b_b = self.rect.bottom
        if self.rect.left <= racket1.rect.right:
            if self.has_collide(b_b=b_b, b_t=b_t, r_b=racket1.rect.bottom, r_t=racket1.rect.top):
                # ball has collide racket 1
                print(1)
                self.speed_vector[0] = -self.speed_vector[0]

        if self.rect.right >= racket1.rect.left:
            if self.has_collide(b_b=b_b, b_t=b_t, r_b=racket2.rect.bottom, r_t=racket2.rect.top):
                # ball has collide racket 2
                print(1)
                self.speed_vector[0] = -self.speed_vector[0]
    

