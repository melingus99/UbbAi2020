from random import randint,random
from numpy.random.mtrand import choice
from math import *

f = open("input.in", "r")
f.readline()
DEPTH_MAX = int(f.readline())
f.close()

T = ['-165', '-150', '-135', '-120', '-105', '-90', '-75',
     '-60', '-45', '-30', '-15', '0', '15', '30', '45', '60', '75',
     '90', '105', '120', '135', '150', '165'] + \
    ["c" + str(x) for x in range(10)]
P = [0.332, 0.332, 0.332, 0.002, 0.002]
F = ['+', '-', '*', 'sin', 'cos']
C = [random() for _ in range(10)]


class Node:
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None
        self.size = 1

    def deepcopy(self):
        copy = Node()
        copy.val = self.val
        copy.size = self.size
        if self.left:
            copy.left = self.left.deepcopy()
        if self.right:
            copy.right = self.right.deepcopy()
        return copy

    def init(self, d):
        if d == 0:
            self.val = choice(T)
            return

        self.val = choice(F, p=P)
        self.left = Node()
        self.left.init(d - 1)
        self.size += self.left.size
        if self.val != 'sin' and self.val != 'cos':
            self.right = Node()
            self.right.init(d - 1)
            self.size += self.right.size

    def mutate(self, pos, prob):
        if pos <= 0:
            assert False
        if pos > self.size:
            assert False
        if self.left and pos <= self.left.size:
            self.left.mutate(pos, prob)
        else:
            leftSize = 0
            if self.left:
                leftSize = self.left.size
            if leftSize + 1 == pos:
                if random() < prob:
                    if self.val in T:
                        self.val = choice(T)
                    else:
                        if self.val == 'sin':
                            self.val = 'cos'
                        elif self.val == 'cos':
                            self.val = 'sin'
                        else:
                            self.val = choice(F[:3])
            else:
                self.right.mutate(pos - leftSize - 1, prob)

    def change(self, root, node1, node2):
        self.val = root.val
        if root.left:
            if root.left == node1:
                self.left = node2.deepcopy()
            else:
                self.left = Node()
                self.left.change(root.left, node1, node2)
        if root.right:
            if root.right == node1:
                self.right = node2.deepcopy()
            else:
                self.right = Node()
                self.right.change(root.right, node1, node2)
        self.size = 1
        if self.left:
            self.size += self.left.size
        if self.right:
            self.size += self.right.size

    def getNodes(self):
        ret = []
        if self.left:
            ret += self.left.getNodes()
        ret.append(self)
        if self.right:
            ret += self.right.getNodes()
        return ret

    def __str__(self):
        if self.val in T:
            return str(C[int(self.val[1])]) if self.val[0] == 'c' else str(self.val)
        if self.val == "sin" or self.val == "cos":
            return self.val + "(" + str(self.left) + ")"
        return str(self.left) + self.val + str(self.right)

    def __repr__(self):
        return self.__str__()

class Chromosome:
    def __init__(self, trainingSet, trainingSetClasses, d=DEPTH_MAX):
        self.trainingSet = trainingSet
        self.trainingSetClasses = trainingSetClasses
        self.root = Node()
        self.root.init(d)
        self.maxDepth = d
        self.fitness = self.evaluate(self.trainingSet, self.trainingSetClasses)

    def __str__(self):
        return str(self.root)

    def evaluate(self, input, output):
        self.fitness = 0
        nr = 0
        exp = str(self.root)
        for (x, y) in zip(input, output):

            res = eval(exp)

            new_res = abs(float(res) - float(y))

            self.fitness += new_res
            nr += 1
        self.fitness = self.fitness / nr
        return self.fitness

    @staticmethod
    def crossover(ch1, ch2, input, output):
        node1 = choice(ch1.root.getNodes())
        node2 = choice(ch2.root.getNodes())
        c = Chromosome(input, output,)
        if ch1.root == node1:  # if we must change the whole tree
            c.root = node2.deepcopy()
        else:
            c.root = Node()
            c.root.change(ch1.root, node1, node2)
        return c

    def mutate(self, prob):
        pos = randint(1, self.root.size)
        self.root.mutate(pos, prob)



class Population:
    def __init__(self, nrIndividuals, input, output):
        self.nrIndividuals = nrIndividuals
        self.individuals = [Chromosome(input, output) for _ in range(nrIndividuals)]

    def __str__(self):
        result = []
        for elem in self.individuals:
            result.append(str(elem.fitness))
        return str(result)

    def evaluate(self, inputTrain, outputTrain):
        for chromosome in self.individuals:
            chromosome.evaluate(inputTrain, outputTrain)

    def selection(self, nrInd):
        if nrInd < self.nrIndividuals:
            self.nrIndividuals = nrInd
            self.individuals = sorted(self.individuals, key=lambda x: x.fitness)
            self.individuals = self.individuals[:nrInd]

    def best(self, maxInd):
        self.individuals = sorted(self.individuals, key=lambda x: x.fitness)
        return self.individuals[:maxInd]

    def reunion(self, other):
        self.nrIndividuals += other.nrIndividuals
        self.individuals = self.individuals + other.individuals
