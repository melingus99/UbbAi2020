import random as rand

import matplotlib.pyplot as plt
import numpy as np

from Controller.controller import Controller
from Problems.EulerSquare import EulerSquare
from domain.Particle import particle


class ValidationTestsEA():
    def __init__(self):
        self.size=5
        self.firstSet=['1','2','3','4','5']
        self.secondSet=['1','2','3','4','5']
        self.PCrossover=0.8
        self.PMutate=0.2
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
            for res,matrix,score,k in controller.EA(self.population,self.PMutate,self.PCrossover,self.generation):
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
        print("average EA:"+str(avg)+" std EA:"+str(std))


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
            population.append(matrix)
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
            for res,matrix,score,k in controller.PSO(self.neighborhoodSize,self.c1,self.c2,self.w,self.iteration):
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
        print("average PSO:"+str(avg)+" std PSO:"+str(std))


    def makePopulation(self, pop, n, firstSet, secondSet):
        return [particle(n, firstSet, secondSet) for x in range(pop)]

class ValidationTestACO:
    def __init__(self):
        self.run()

    def run(self):
        listy=[]
        listx=[]
        problem=EulerSquare(4,['1','2','3','4'],['1','2','3','4'])
        for i in range(30):
            controller=Controller(problem)
            for result,matrix,score,iteration in controller.ACO(100,3,1.9,0.8,0.05,0.5):
                if(result==True):
                    listy.append(score)
                    listx.append(i)
        average=np.average(listy)
        std=np.std(listy)
        plt.plot(listx,listy)
        plt.title("Validation Tests ACO")
        plt.xlabel('number of the run')
        plt.ylabel('score of the best dude')
        plt.show()
        print("average ACO:"+str(average)+" std ACO:"+str(std))

valid=ValidationTestACO()

#validEA=ValidationTestsEA()
#validPSO=ValidationTestsPSO()
