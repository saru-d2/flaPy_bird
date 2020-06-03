import pygame
from bird import *
from pipe import *
pygame.font.init()

win = pygame.display.set_mode((500, 800))
bg = pygame.image.load('./imgs/bg.png')
bg = pygame.transform.scale2x(bg)

font = pygame.font.SysFont("comicsans", 50)

def draw_win(birds, frm_ctr, pipes, base, score, num_alive):
    win.blit(bg, (0, 0))
    for bird in birds:
        bird.draw(win, frm_ctr)
    for pipe in pipes:
        pipe.draw(win)
    base.draw(win)
    text = font.render("SCORE: "+ str(score), 1, (255, 255, 255))
    text2 = font.render("No. ALIVE: "+ str(num_alive), 1, (255, 255, 255))
    win.blit(text, (500 - 10 - text.get_width(), 10))
    win.blit(text2, (10,10))
    pygame.display.update()
