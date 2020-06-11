from Lab11GP.Model import Population,Chromosome
from random import choice
import math

class Controller:
    def __init__(self,data,mutation,crossover,ind):
        self.epsilon=data.epsilon
        depth=data.depth
        self.trainingSet=data.trainingSet
        self.trainingSetClasses=data.trainingSetClasses
        self.testSet=data.testSet
        self.testSetClasses=data.testSetClasses
        self.mutation=mutation
        self.crossover=crossover
        self.ind=ind
        self.population= Population(ind, self.trainingSet, self.trainingSetClasses)

    def run(self):
        self.population.evaluate(self.trainingSet, self.trainingSetClasses)

        bestFitness = math.inf
        i = 1
        f = open("output.out", "w")

        while (bestFitness > self.epsilon):
            print("\n")
            f.write("\n")
            yield "Iteration: " + str(i)
            f.write("Iteration: " + str(i) + "\n")
            self.iteration()
            self.population.evaluate(self.trainingSet, self.trainingSetClasses)
            self.population.selection(self.ind)
            best = self.population.best(1)[0]
            bestFitness = float(best.fitness)
            yield "Best: " + str(best.root) + "\n" + "fitness: " + str(bestFitness) + "\n"
            f.write("Best: " + str(best.root) + "\n" + "fitness: " + str(bestFitness) + "\n")
            i += 1

        f.close()

    def iteration(self):
        parents = range(self.ind)
        nrChildren = len(parents) // 2
        offspring = Population(nrChildren, self.trainingSet, self.trainingSetClasses)

        for i in range(nrChildren):
            offspring.individuals[i] = Chromosome.crossover(choice(self.population.individuals),
                                                            choice(self.population.individuals),
                                                            self.trainingSet,
                                                            self.trainingSetClasses)
            offspring.individuals[i].mutate(self.mutation)
        offspring.evaluate(self.trainingSet, self.trainingSetClasses)
        self.population.reunion(offspring)
        self.population.selection(self.ind)
