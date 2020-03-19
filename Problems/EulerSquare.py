# -*- coding: utf-8 -*-
from domain.Particle import particle
from domain.State import State
from Problems.Problem import Problem
from copy import deepcopy
import numpy as np
import random as rnd
class EulerSquare(Problem):
    def __init__(self,value,S,T):
        self.initialState=State(value)
        self.currentState=deepcopy(self.initialState)
        self.S=S
        self.T=T
        self.finalState=1


    def setCurrentState(self,state):
        self.currentState=deepcopy(state)

    def fitness(self,individual):
        wrongPieces=0
        n=len(self.S)
        for i in range(0,n):
            for j in range(0,n):
                for k in range(0,2):
                    for l in range(0,n):
                        if(individual[i][j][k]==individual[i][l][k] and j!=l):
                            wrongPieces+=1
                        if(individual[i][j][k]==individual[l][j][k] and i!=l):
                            wrongPieces+=1
                for k in range(0,n):
                    for l in range(0,n):
                        if(individual[i][j]==individual[k][l] and (i!=k or j!=l)):
                            wrongPieces+=2
        return wrongPieces
                

        
    def setFinalState(self,state):
        self.finalState=state
        
    def mutate(self,individual):
        n=len(individual)-1
        first=rnd.randint(0,n)
        second=rnd.randint(0,n)
        i=rnd.randint(0,n)
        j=rnd.randint(0,n)
        individual[i][j][0]=self.S[first]
        individual[i][j][1]=self.T[second]
        return individual
    
    def Crossover(self,individual1,individual2):
        newIndividual=[]
        n=len(individual1)
        for i in range(0,n):
            newIndividual.append([])
        for i in range(0,n//2):
            newIndividual[i]=(individual1[i])
        for i in range(n//2,n):
            newIndividual[i]=(individual2[i])
        return newIndividual

    def move(self,position,bestposition,bestNeighborPosition,velocity):
        newPosition=deepcopy(position)
        n=len(position)
        for i in range(0,velocity):
            randi=rnd.randint(0,n-1)
            randj=rnd.randint(0,n-1)
            if(i<=velocity//2):
                newPosition[randi][randj]=bestposition[randi][randj]
            else:
                newPosition[randi][randj]=bestNeighborPosition[randi][randj]
        return newPosition

    def reinitialize(self):
        return particle(len(self.S),self.S,self.T)

    def selectNeighbors(self, nSize):
        pop=self.currentState.value
        if (nSize>len(pop)):
            nSize=len(pop)
        neighbors=[]
        for i in range(len(pop)):
            localNeighbor=[]
            for j in range(nSize):
                x=rnd.randint(0, len(pop)-1)
                while (x in localNeighbor):
                    x=rnd.randint(0, len(pop)-1)
                localNeighbor.append(x)
            neighbors.append(localNeighbor.copy())
        return neighbors


