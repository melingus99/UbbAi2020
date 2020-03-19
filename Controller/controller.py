from Problems.Problem import Problem
from Problems.LatinSquare import LatinSquare
from Problems.EulerSquare import EulerSquare
from copy import deepcopy
import math
import numpy as np
import random as rand
from domain.State import State
from PyQt5.QtCore import QRunnable, pyqtSlot


class Controller():
    def __init__(self,problem):
        self.problem=problem

    def Greedy(self):
        state=self.problem.initialState
        validStates=[1]
        listScores=[]
        maxScore=-1
        listMaxScores=[]
        #if problem is not solved and can still be solved go a State deeper
        while(self.problem.stateScore(state)<len(state.value) and len(validStates)!=0):
            validStates=self.problem.expand(state)
            if(len(validStates)==0):
                continue
            for i in range(0,len(validStates)):
                listScores.append(self.problem.heuristic(state,validStates[i]))
            maxScore=max(listScores)
            for i in range(0,len(listScores)):
                if(listScores[i]==maxScore):
                    listMaxScores.append(i)
            idx=np.random.randint(0,len(listMaxScores))
            state=validStates[idx]
            listScores=[]
            listMaxScores=[]
        self.problem.setFinalState(state)
        if(self.problem.stateScore(state)==len(state.value) and self.problem.checkValid(state)==True):
            return True,state.value
        return False,state.value
            
            
            
    def DFSRecursive(self,state):
        if(self.problem.stateScore(state)==len(state.value) and self.problem.checkValid(state)==True):
            return True,state
        validStates=self.problem.expand(state)
        for i in range(0,len(validStates)):
            res,state=self.DFSRecursive(validStates[i])
            if(res==True):
                return res,state
        return False,state
        
    
    def DFS(self):
        state=self.problem.initialState
        res,state=self.DFSRecursive(state)
        matrix=deepcopy(state.value)
        return res,matrix
    
    def HillClimbing(self):
        state=self.problem.initialState
        Scores=[]
        minScore=math.inf
        k=0
        scoreState=self.problem.fitness(state.value)
        while(scoreState!=0):
            scoreState=self.problem.fitness(state.value)
            if(k%25==0):
                yield False,state.value,scoreState
            validStates=self.problem.expand(state)
            for i in range(0,len(validStates)):
                Scores.append(self.problem.fitness(validStates[i].value))
            for i in range(0,len(Scores)):
                if(Scores[i]<minScore):
                    idxScore=i
                    minScore=Scores[i]
            if(minScore<scoreState):
                state=deepcopy(validStates[idxScore])
            else:
                state=self.problem.mutate(state)
            Scores=[]
            minScore=math.inf
            k+=1
        yield True,state.value
    
    def EA(self,population,PMutate,PCrossover,maxGeneration):
        generation=self.problem.initialState
        kGeneration=0
        newGeneration=State([])
        generation.value.sort(key=self.problem.fitness)
        bestScoreState=self.problem.fitness(generation.value[0])
        
        while(kGeneration<maxGeneration and bestScoreState!=0):
            if kGeneration%25==0:
                yield False,generation.value[0],bestScoreState
            randCrossover=rand.random()
            randMutate=rand.random()
            newGeneration=deepcopy(generation)
            
            if(randMutate<=PMutate):
                idx=rand.randint(0,population-1)
                mutant=self.problem.mutate(generation.value[idx])
                newGeneration.value[idx]=deepcopy(mutant)
                
            
            if(randCrossover<=PCrossover):
                for i in range(1,population//4):
                    newGeneration.value[i+population//2]=deepcopy(self.problem.Crossover(generation.value[0],generation.value[i]))
                for i in range(1,population//4):
                    newGeneration.value[i+population//2+population//4]=deepcopy(self.problem.Crossover(generation.value[i],generation.value[i+population//2+population//4]))
                newGeneration.value[population-1]=deepcopy(self.problem.Crossover(generation.value[1],generation.value[0]))

            kGeneration+=1
            generation=deepcopy(newGeneration)
            generation.value.sort(key=self.problem.fitness)
            bestScoreState=self.problem.fitness(generation.value[0])

        yield True,generation.value[0],bestScoreState


    def PSO(self,neighborhoodSize, c1, c2, w,iterations):

        population=deepcopy(self.problem.initialState.value)
        neighbors=self.problem.selectNeighbors(neighborhoodSize)
        self.problem.setCurrentState(State(population))

        best = 0
        for i in range(1, len(population)):
            if (population[i].value<population[best].value):
                best = i

        bestScoreParticle=population[best].value
        k=0

        while(k<iterations and bestScoreParticle!=0):
            if(k%20==0):
                yield False,population[best].position,population[best].value

            bestNeighbors=[]
            for i in range(len(population)):
                bestNeighbors.append(neighbors[i][0])
                for j in range(1,len(neighbors[i])):
                    if (population[bestNeighbors[i]].value>population[neighbors[i][j]].value):
                        bestNeighbors[i]=neighbors[i][j]


            for i in range(len(population)):
                newVelocity = w * population[i].velocity
                newVelocity = newVelocity + c1*rand.random()*abs(self.problem.fitness(population[bestNeighbors[i]].position)-self.problem.fitness(population[i].position))
                newVelocity = newVelocity + c2*rand.random()*abs(self.problem.fitness(population[i].bestPosition)-self.problem.fitness(population[i].position))

                population[i].velocity=round(newVelocity)

            for i in range(len(population)):
                newPosition=self.problem.move(population[i].position,population[i].bestPosition,population[bestNeighbors[i]].bestPosition,population[i].velocity)
                population[i].setPosition(newPosition)
                #population[i].position=deepcopy(newPosition)

            if(k%10==0):
                for i in range(0,len(population)):
                    randomDude=rand.randint(0,len(population)-1)
                    population[randomDude]=self.problem.reinitialize()
                    neighbors=self.problem.selectNeighbors(neighborhoodSize)

            k+=1
            #w=w-0.0001
            best=0
            for i in range(1, len(population)):
                if (population[i].value<population[best].value):
                    best = i
            bestScoreParticle=population[best].value

        yield True,population[best].position,population[best].value

        
    
    
