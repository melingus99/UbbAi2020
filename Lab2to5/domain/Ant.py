from random import *
from copy import deepcopy
class ant:
    def __init__(self, n, firstSet,secondSet):
        self.size = n
        self.firstSet=firstSet
        self.secondSet=secondSet
        self.path=[[ [-1,-1] for i in range(n)] for j in range(n)]
        self.makeInitPosition()

    def makeInitPosition(self):
        for i in range(self.size):
            nrset1=randint(0,self.size-1)
            nrset2=randint(0,self.size-1)
            self.path[0][i]=[self.firstSet[nrset1],self.secondSet[nrset2]]


    def expand(self,pos):
        list=[]
        i=pos//self.size
        j=pos%self.size
        init=[deepcopy(self.path[i][j][0]),deepcopy(self.path[i][j][1])]
        for k in range(self.size):
            for l in range(self.size):
                self.path[i][j]=[self.firstSet[k],self.secondSet[l]]
                list.append(deepcopy(self.path))
        self.path[i][j]=init
        return list

    def addMove(self, q0, trace, alpha, beta,pos):
        p = []
        nextSteps=deepcopy(self.expand(pos))
        if (len(nextSteps) == 0):
            return False
        for i in nextSteps:
            p.append(self.fitness(i))
        for i in range(len(p)):
            score=0
            for j in range(self.size):
                for k in range(self.size):
                    if(self.path[j][k][0]!=-1 and self.path[j][k][1]!=-1):
                        pos0=self.firstSet.index(self.path[j][k][0])
                        pos1=self.secondSet.index(self.path[j][k][1])
                        score+=trace[j][k][pos0*self.size+pos1]
            p[i]=(p[i]**beta)*(score**alpha)
        if (random()<q0):
            p = [ [i, p[i]] for i in range(len(p)) ]
            p = min(p, key=lambda a: a[1])
            self.path[pos//self.size][pos%self.size]=nextSteps[p[0]][pos//self.size][pos%self.size]
        else:
            s = sum(p)
            if (s==0):
                return choice(nextSteps)
            p = [ p[i]/s for i in range(len(p)) ]
            p = [ sum(p[0:i+1]) for i in range(len(p)) ]
            r=random()
            i=0
            while (r > p[i]):
                i=i+1
            self.path[pos//self.size][pos%self.size]=nextSteps[i][pos//self.size][pos%self.size]
        return True

    def fitness(self,individual):
        wrongPieces=0
        n=len(self.secondSet)
        for i in range(0,n):
            for j in range(0,n):
                for k in range(0,2):
                    for l in range(0,n):
                        if((individual[i][j][k]==individual[i][l][k] and j!=l) or individual[i][j][k]==-1):
                            wrongPieces+=1
                        if((individual[i][j][k]==individual[l][j][k] and i!=l) or individual[i][j][k]==-1):
                            wrongPieces+=1
                for k in range(0,n):
                    for l in range(0,n):
                        if(individual[i][j]==individual[k][l] and (i!=k or j!=l)):
                            wrongPieces+=2
        return wrongPieces+1
