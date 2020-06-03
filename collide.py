import pygame
from pipe import *
from bird import *

def collide(pipe, bird):
    bird_mask = bird.get_mask()

    if bird.bird_img.get_height() + bird.y > 730 : 
        return True

    if bird.y + bird.bird_img.get_height() < 0 :
        return True
    top_pipe_mask = pipe.get_mask_top()
    bottom_pipe_mask = pipe.get_mask_bottom()

    top_offset = (pipe.x - bird.x, pipe.top - round(bird.y))
    bottom_offset = (pipe.x - bird.x, pipe.bottom - round(bird.y))

    b_pt = bird_mask.overlap(bottom_pipe_mask, bottom_offset)
    t_pt = bird_mask.overlap(top_pipe_mask, top_offset)

    if b_pt or t_pt:
        return True
    return False