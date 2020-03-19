# -*- coding: utf-8 -*-

from domain.State import State

class Problem:
    def __init__(self,value):
        pass
        
    def expand(self,state):
        pass
                
    def checkValid(self,state):
        pass
                
    def heuristic(self,state1,state2):
        pass
        
    def fitness(self,state):
        pass
    def readFromFile(self):
        pass
    
    def stateScore(self,state):
        pass
    
    def mutate(self,state):
        pass
    
    def setFinalState(self,state):
        pass
