from Problems.EulerSquare import EulerSquare
from Controller.controller import Controller
from domain.Particle import particle
from domain.State import State
import random as rand
import matplotlib.pyplot as plt
import numpy as np
class ValidationTestsEA():
    def __init__(self):
        self.size=5
        self.firstSet=['1','2','3','4','5']
        self.secondSet=['1','2','3','4','5']
        self.PCrossover=0.8
        self.Mutate=0.2
        self.population=40
        self.generation=25
        self.run()

    def run(self):
        firstGeneration=self.makePopulation(self.population,self.size,self.firstSet,self.secondSet)
        problem=EulerSquare(firstGeneration,self.firstSet,self.secondSet)
        controller=Controller(problem)
        listy=[]
        listx=[]
        for i in range(0,30):
            for res,matrix,score in controller.EA(self.population,self.PCrossover,self.PCrossover,self.generation):
                if(res==True):
                    listy.append(score)
                    listx.append(i)
        plt.plot(listx,listy)
        plt.title("Validation Tests EA")
        plt.xlabel('number of the run')
        plt.ylabel('score of the best dude')
        plt.show()
        avg=sum(listy)/len(listy)
        std=np.std(listy)
        print(str(avg)+" "+str(std))


    def makePopulation(self,pop,n,firstSet,secondSet):
        population=[]
        for i in range(0,pop):
            matrix=[]
            for j in range(0,n):
                matrix.append([])
                for k in range(0,n):
                    first=rand.randint(0,n-1)
                    second=rand.randint(0,n-1)
                    matrix[j].append([firstSet[first],secondSet[second]])
            state=State(matrix)
            population.append(state)
        return population


class ValidationTestsPSO():
    def __init__(self):
        self.size=5
        self.firstSet=['1','2','3','4','5']
        self.secondSet=['1','2','3','4','5']
        self.population=40
        self.iteration=25
        self.w=1.0
        self.c1=1.0
        self.c2=2.5
        self.neighborhoodSize=10
        self.run()

    def run(self):
        init=self.makePopulation(self.population,self.size,self.firstSet,self.secondSet)
        problem=EulerSquare(init,self.firstSet,self.secondSet)
        controller=Controller(problem)
        listy=[]
        listx=[]
        for i in range(0,30):
            for res,matrix,score in controller.PSO(self.neighborhoodSize,self.c1,self.c2,self.w,self.iteration):
                if(res==True):
                    listy.append(score)
                    listx.append(i)
        plt.plot(listx,listy)
        plt.title("Validation Tests PSO")
        plt.xlabel('number of the run')
        plt.ylabel('score of the best dude')
        plt.show()
        avg=sum(listy)/len(listy)
        std=np.std(listy)
        print(str(avg)+" "+str(std))


    def makePopulation(self, pop, n, firstSet, secondSet):
        return [particle(n, firstSet, secondSet) for x in range(pop)]


validEA=ValidationTestsEA()
validPSO=ValidationTestsPSO()
