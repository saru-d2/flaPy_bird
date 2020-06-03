import random
import math

population_size = 50
generation = 1

genomes = []
nets = []

class Net:
    def __init__(self):
        self.matrix = []
        for i in range(0, 2):
            self.matrix[i] = random.randrange(0, 100)
            self.matrix[i] /= 100

for i in range(0, 49):
    nets.append(Net)


class Genome:
    def __init__(self):
        self.fitness = 0

def sigmoid(x):
    return 1/(1+math.exp(-x))

def output(net, input):
    ret = 1
    for i in range (0, 2):
        ret +=  net[i]*input[i]
    return sigmoid(ret)



