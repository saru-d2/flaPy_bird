import pygame
import os
from bird import *
from pipe import *
from draw_win import *
from collide import *
from base import *
pygame.font.init()

frm_ctr = 0
pygame.init()


def main():
    score = 0
    bird = Bird(200,200)
    clock = pygame.time.Clock()
    global frm_ctr
    pipes = [Pipe(500)]
    cur_pipe = pipes[0]
    # bird = Bird(200, 200)
    base = Base(730)
    run = True
    while run:
        num_alive = 1
        clock.tick(30)
        frm_ctr += 1
        if bird.alive == False:
            run = False
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird.jump()
        bird.update()
           
        if abs(cur_pipe.x + cur_pipe.width -200)<3:
            score += 1
        for pipe in pipes:
            if pipe.x < -90:
                pipes.remove(pipe)
                pipes.append(Pipe(500))
                cur_pipe = pipes[-1]
                pass
            
            if collide(pipe, bird):
                bird.alive = False                
                # print("KABOOOM")
                continue
                # print(pipe.x + pipe.width)

            pipe.update()
        base.update()
        birds = [bird]
        draw_win(birds, frm_ctr, pipes, base, score, num_alive)
main()