import pygame
import os
import neat
from bird import *
from pipe import *
from draw_win import *
from collide import *
from base import *
pygame.font.init()

frm_ctr = 0
pygame.init()


def main(genomes, config):
    score = 0
    nets = []
    birds = []
    ge = []

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        birds.append(Bird(200, 200))
        g.fitness = 0
        ge.append(g)

    clock = pygame.time.Clock()
    global frm_ctr
    pipes = [Pipe(500)]
    cur_pipe = pipes[0]
    # bird = Bird(200, 200)
    base = Base(730)
    run = True
    while run:

        # clock.tick(30)
        frm_ctr += 1
        if len(birds) <= 0:
            run = False
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                for bird in birds:
                    bird.jump()
        for x, bird in enumerate(birds):
            bird.update()
            ge[x].fitness += 0.01
            output = nets[x].activate(
                (bird.y, abs(bird.y - cur_pipe.height), abs(bird.y - cur_pipe.bottom), cur_pipe.x))
            if output[0] > 0.5:
                bird.jump()
        num_alive = len(birds)
        if abs(cur_pipe.x + cur_pipe.width -200)<3:
            score += 1
        for pipe in pipes:
            if pipe.x < -90:
                pipes.remove(pipe)
                pipes.append(Pipe(500))
                cur_pipe = pipes[-1]
                pass
            for x, bird in enumerate(birds):
                if collide(pipe, bird):
                    bird.alive = False
                    ge[x].fitness -= 1
                    birds.pop(x)
                    ge.pop(x)
                    nets.pop(x)
                    # print("KABOOOM")
                    continue
                # print(pipe.x + pipe.width)
                if pipe.x + pipe.width - bird.x < 5 and pipe.x + pipe.width - bird.x > 0:
                    ge[x].fitness += 5

            pipe.update()
        base.update()
        draw_win(birds, frm_ctr, pipes, base, score, num_alive)


def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    winner = p.run(main, 50)


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    run(config_path)
