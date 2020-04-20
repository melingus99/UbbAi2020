import random as rand
import copy
class particle:
    def __init__(self,size,firstSet,secondSet):
        self.position = self.makeInitPosition(size,firstSet,secondSet)
        self.evaluate()
        self.velocity =0
        self.bestPosition=self.position.copy()
        self.bestValue=self.value

    def makeInitPosition(self,n,firstSet,secondSet):
        matrix=[]
        for i in range(0,n):
            matrix.append([])
            for j in range(0,n):
                first=rand.randint(0,n-1)
                second=rand.randint(0,n-1)
                matrix[i].append([firstSet[first],secondSet[second]])
        return matrix

    def fitness(self):
        wrongPieces=0
        n=len(self.position)
        for i in range(0,n):
            for j in range(0,n):
                for k in range(0,2):
                    for l in range(0,n):
                        if(self.position[i][j][k]==self.position[i][l][k] and j!=l):
                            wrongPieces+=1
                        if(self.position[i][j][k]==self.position[l][j][k] and i!=l):
                            wrongPieces+=1
                for k in range(0,n):
                    for l in range(0,n):
                        if(self.position[i][j]==self.position[k][l] and (i!=k or j!=l)):
                            wrongPieces+=2
        return wrongPieces

    def evaluate(self):
        self.value = self.fitness()


    def setPosition(self, newPosition):
        self.position=copy.deepcopy(newPosition)
        self.evaluate()
        if (self.value<self.bestValue):
            self.bestPosition = self.position
            self.bestValue  = self.value
