import pygame


class Base:
    vel = 5
    base_img = pygame.image.load('imgs/base.png')
    base_img = pygame.transform.scale2x(base_img)
    width = base_img.get_width()

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.width

    def update(self):
        self.x1 -= self.vel
        self.x2 -= self.vel
        
        if self.x1 + self.width < 0:
            self.x1 = self.x2 + self.width
        
        if self.x2 + self.width < 0:
            self.x2 = self.x1 + self.width

    def draw(self, win):
        win.blit(self.base_img, (self.x1, self.y))
        win.blit(self.base_img, (self.x2, self.y))

