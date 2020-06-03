import pygame
# from app import *


img1 = pygame.transform.scale2x(pygame.image.load('imgs/bird1.png'))
img2 = pygame.transform.scale2x(pygame.image.load('imgs/bird2.png'))
img3 = pygame.transform.scale2x(pygame.image.load('imgs/bird3.png'))
bird_imgs = [img1, img2, img3]
def rot_center(image, angle):
    """rotate a Surface, maintaining position."""

    loc = image.get_rect().center  #rot_image is not defined 
    rot_sprite = pygame.transform.rotate(image, angle)
    rot_sprite.get_rect().center = loc
    return rot_sprite

class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.y_vel = 0
        self.height = self.y
        self.t = 0  # time
        self.theta= 0
        self.max_tilt = 25
        self.bird_img = img1
        self.alive = True
        self.score = 0

    def jump(self):
        self.y_vel = -30
        self.t = 0
        self.height = self.y
        self.theta = self.max_tilt

    def update(self):

        # s = ut +1/2 a t^2
        self.y_vel += 1/2*self.t**2
        s = self.y_vel
        if s > 20:
            s = 20
        if s < 0:
            s -= 2
        self.y += s
        self.theta -= (1/2*self.t)
        if (self.theta < -80):
            self.theta = -80
        self.t += 1

    def draw(self, win, frm_ctr):
        ind = int((frm_ctr / 5) % 3)
        self.bird_img = bird_imgs[ind]
        self.bird_img = rot_center(self.bird_img, self.theta)
        win.blit(self.bird_img, (self.x, self.y))

    def get_mask(self):
        return pygame.mask.from_surface(self.bird_img)