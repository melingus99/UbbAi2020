from Problems.Problem import Problem
from Problems.LatinSquare import LatinSquare
from Problems.EulerSquare import EulerSquare
from copy import deepcopy
import math
import numpy as np
import random as rand
from domain.State import State
from PyQt5.QtCore import QRunnable, pyqtSlot
from domain.Ant import ant

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
            if(k%100==0):
                yield False,state.value,scoreState,k
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
                state=self.problem.reinitialize(state.value)
                #state=self.problem.mutate(state.value)
            Scores=[]
            minScore=math.inf
            k+=1
        yield True,state.value,scoreState,k
    
    def EA(self,population,PMutate,PCrossover,maxGeneration):
        generation=self.problem.initialState
        kGeneration=0
        newGeneration=State([])
        generation.value.sort(key=self.problem.fitness)
        bestScoreState=self.problem.fitness(generation.value[0])
        
        while(kGeneration<maxGeneration and bestScoreState!=0):
            if kGeneration%50==0:
                yield False,generation.value[0],bestScoreState,kGeneration
                
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

        yield True,generation.value[0],bestScoreState,kGeneration


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
                yield False,population[best].position,population[best].value,k

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

            '''
            reinitialization
            if(k%10==0):
                for i in range(0,len(population)):
                    randomDude=rand.randint(0,len(population)-1)
                    population[randomDude]=self.problem.reinitializeParticle()
                    neighbors=self.problem.selectNeighbors(neighborhoodSize)
            '''

            k+=1
            #w=w-0.0001
            best=0
            for i in range(1, len(population)):
                if (population[i].value<population[best].value):
                    best = i
            bestScoreParticle=population[best].value

        yield True,population[best].position,population[best].value,k

    def epoca(self,trace,noAnts,alpha,beta,rho,q0):
        n=len(self.problem.S)
        firstSet=self.problem.S
        secondSet=self.problem.T
        antSet=[ant(n, firstSet,secondSet) for i in range(noAnts)]
        for i in range(0,n*n):
            for x in antSet:
                x.addMove(q0, trace, alpha, beta,i)

        dTrace=[ 1.0 / antSet[i].fitness(antSet[i].path) for i in range(len(antSet))]
        for i in range(n):
            for j in range (n):
                for k in range(n*n):
                    trace[i][j][k] = (1 - rho) * trace[i][j][k]

        for i in range(len(antSet)):
            x = antSet[i].path
            for k in range(len(x)):
                for l in range(len(x)):
                    if(x[k][l][0]!=-1 and x[k][l][1]!=-1):
                        pos0=firstSet.index(x[k][l][0])
                        pos1=secondSet.index(x[k][l][1])
                        trace[k][l][pos0*n+pos1]+=dTrace[i]
        f=[ [antSet[i].fitness(antSet[i].path), i] for i in range(len(antSet))]
        f=min(f, key=lambda a: a[0])
        return antSet[f[1]].path,antSet[f[1]].fitness(antSet[f[1]].path)

    def ACO(self,noEpoch,noAnts,alpha,beta,rho,q0):
        bestSol=[]
        bestScore=math.inf
        succes=False
        n=len(self.problem.S)
        trace=[[[1 for i in range(n*n)] for j in range(n)] for k in range (n)]
        for i in range(noEpoch):
            sol,score=self.epoca(trace,noAnts,alpha,beta,rho,q0)
            if score<bestScore:
                bestSol=sol.copy()
                bestScore=score
            if(bestScore==1):
                succes=True
                break
            if(i%25==0):
                yield succes,bestSol,bestScore,i
        yield True,bestSol,bestScore,noEpoch
    
    
