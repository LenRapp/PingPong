import keyboard
import pygame

class Racket():
    def __init__(self, color:str, speed:float, position_x:float, key_up:str, key_down:str ) -> None:
        self.speed = speed
        self.surface = pygame.Surface((10, 50))
        self.surface.fill((255, 255, 255))
        self.rect = self.surface.get_rect()
        self.rect = self.rect.move(position_x,0)
        self.position_x = position_x
        self.key_up = key_up
        self.key_down = key_down

    def get_surface(self):
        return self.surface
    
    def get_rect(self):
        return self.rect
    
    def racket_move(self):
        if keyboard.is_pressed(self.key_up): # top rect >= 0 
            self.rect = self.rect.move(0, -self.speed)
        elif keyboard.is_pressed(self.key_down):# bottom rect <= screen heigth
            self.rect = self.rect.move(0, self.speed)