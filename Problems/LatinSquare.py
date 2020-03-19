from domain.State import State
from Problems.Problem import Problem
import numpy as np

import copy
class LatinSquare(Problem):
    def __init__(self,value):
        self.initialState=State(value)
        #self.currentState=self.initialState
        self.finalState=1
        
    def expand(self,state):
        listStates=[]
        for i in range(0,len(state.value)):
            for j in range(0,len(state.value[i])):
                if(state.value[i][j]==0):
                    state.value[i][j]=1
                    if(self.checkValid(state)):
                        listStates.append(copy.deepcopy(state))
                    state.value[i][j]=0
        return listStates
                
    def checkValid(self,state):
        sumlines=[]
        sumcols=[]
        for i in range(0,len(state.value)):
            sumline=0
            sumcol=0
            for j in range(0,len(state.value[i])):
                sumline+=state.value[i][j]
                sumcol+=state.value[j][i]
                #checks if another 1 is on the diagonal
                if(state.value[i][j]==1):
                    #checks right down diagonal
                    k=1
                    while(k+i<len(state.value) and k+j<len(state.value[i])):
                        if(state.value[i+k][j+k]==1):
                            return False
                        k+=1
                    #checks right up diagonal
                    k=1
                    while(i-k>=0 and k+j<len(state.value[i])):
                        if(state.value[i-k][j+k]==1):
                            return False
                        k+=1
                    #checks left up diagonal
                    k=1
                    while(i-k>=0 and j-k>=0):
                        if(state.value[i-k][j-k]==1):
                            return False
                        k+=1
                    #checks left down diagonal
                    k=1
                    while(k+i<len(state.value) and j-k>=0):
                        if(state.value[i+k][j-k]==1):
                            return False
                        k+=1
            sumlines.append(sumline)
            sumcols.append(sumcol)
        for i in range(0,len(sumlines)):
            if(sumlines[i]>1 or sumcols[i]>1):
                return False
        return True
                
    def heuristic(self, state1, state2):
        matrix1=copy.deepcopy(state1)
        matrix2=copy.deepcopy(state2)
        n=len(matrix1.value)
        for i in range(0,n):
            for j in range(0,n):
                if(matrix2.value[i][j]==1):
                    for k in range(0,n):
                        matrix2.value[i][k]=-1
                        matrix2.value[k][j]=-1
                    k=1
                    while(k+i<n and k+j<n):
                        matrix2.value[i + k][j + k]=-1
                        k+=1
                    #checks right up diagonal
                    k=1
                    while(i-k>=0 and k+j<n):
                        matrix2.value[i - k][j + k]=-1
                        k+=1
                    #checks left up diagonal
                    k=1
                    while(i-k>=0 and j-k>=0):
                        matrix2.value[i - k][j - k]=-1
                        k+=1
                    #checks left down diagonal
                    k=1
                    while(k+i<n and j-k>=0):
                        matrix2.value[i + k][j - k]=-1
                        k+=1
        for i in range(0,n):
            for j in range(0,n):
                if(matrix1.value[i][j]==1):
                    for k in range(0,n):
                        matrix1.value[i][k]=-1
                        matrix1.value[k][j]=-1
                    k=1
                    while(k+i<n and k+j<n):
                        matrix1.value[i + k][j + k]=-1
                        k+=1
                    #checks right up diagonal
                    k=1
                    while(i-k>=0 and k+j<n):
                        matrix1.value[i - k][j + k]=-1
                        k+=1
                    #checks left up diagonal
                    k=1
                    while(i-k>=0 and j-k>=0):
                        matrix1.value[i - k][j - k]=-1
                        k+=1
                    #checks left down diagonal
                    k=1
                    while(k+i<n and j-k>=0):
                        matrix1.value[i + k][j - k]=-1
                        k+=1
        return self.stateScore(matrix1)-self.stateScore(matrix2)
        
    
    def readFromFile(self):
        return
    
    def stateScore(self,state):
        return np.matrix(state.value).sum()
    
    def SetState(self,state):
        self.currentState=state
        
    def setFinalState(self,state):
        self.finalState=state
