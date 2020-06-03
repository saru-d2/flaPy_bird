import pygame
import random
from bird import *



class Pipe:
    

    gap = 240
    vel = 5
    
    def __init__(self, x):

        self.top_img = pygame.transform.flip(pygame.image.load('imgs/pipe.png'), False, True)
        self.top_img = pygame.transform.scale2x(self.top_img)
        self.bottom_img = pygame.image.load('imgs/pipe.png')
        self.bottom_img = pygame.transform.scale2x(self.bottom_img)
        self.x = x
        self.height = 0
        self.top = 0
        self.bottom = 0
        self.set_pipe()
        self.width = self.top_img.get_width()

    def set_pipe(self):
        self.height = random.randrange(50, 450)
        print(" ",self.height," ")
        self.top = self.height - self.top_img.get_height()
        self.bottom = self.height + self.gap

    def update(self):
        self.x -= self.vel
        
    def draw(self, win):
        win.blit(self.top_img, (self.x, self.top))
        win.blit(self.bottom_img, (self.x, self.bottom))
        # print (self.top, " " , self.bottom)

    def get_mask_top(self):
        return pygame.mask.from_surface(self.top_img)

    def get_mask_bottom(self):
        return pygame.mask.from_surface(self.bottom_img)