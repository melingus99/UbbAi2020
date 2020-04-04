"""
Sa se plimbe un cal pe o tabla de sah de dimensiune n x m, odata pe fiecare casuta.
"""
import math
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
        # adauga o noua pozitie in solutia furnicii daca este posibil
        p = []
        # pozitiile ce nu sunt valide vor fi marcate cu zero
        nextSteps=deepcopy(self.expand(pos))
        # determina urmatoarele pozitii valide in nextSteps
        # daca nu avem astfel de pozitii iesim
        if (len(nextSteps) == 0):
            return False
        # punem pe pozitiile valide valoarea distantei empirice
        for i in nextSteps:
            p.append(self.fitness(i))
        # calculam produsul trace^alpha si vizibilitate^beta
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
            # adaugam cea mai buna dintre mutarile posibile
            p = [ [i, p[i]] for i in range(len(p)) ]
            p = min(p, key=lambda a: a[1])
            self.path[pos//self.size][pos%self.size]=nextSteps[p[0]][pos//self.size][pos%self.size]
        else:
            # adaugam cu o probabilitate un drum posibil (ruleta)
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


def epoca(noAnts, n,trace, alpha, beta, q0, rho,firstSet,secondSet):
    antSet=[ant(n, firstSet,secondSet) for i in range(noAnts)]
    for i in range(0,n*n):
        for x in antSet:
            x.addMove(q0, trace, alpha, beta,i)
    # actualizam trace-ul cu feromonii lasati de toate furnicile

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
    # return best ant path
    f=[ [antSet[i].fitness(antSet[i].path), i] for i in range(len(antSet))]
    f=min(f, key=lambda a: a[0])
    return antSet[f[1]].path,antSet[f[1]].fitness(antSet[f[1]].path)

def main(n = 5,noEpoch = 1000,noAnts = 10,alpha = 1.9,beta = 0.8,rho = 0.05,q0 = 0.5,firstSet=[1,2,3,4,5],secondSet=[1,2,3,4,5]):
    sol=[]
    bestSol=[]
    bestScore=math.inf
    trace=[[[1 for i in range(n*n)] for j in range(n)] for k in range (n)]
    print("Programul ruleaza! Dureaza ceva timp pana va termina!")
    for i in range(noEpoch):
        if(i%2==0):
            q0=0.8
        sol,score=epoca(noAnts, n, trace, alpha, beta, q0, rho,firstSet,secondSet)
        if score<bestScore:
            bestSol=sol.copy()
            bestScore=score
        if(bestScore==1):
            break
        q0=0.5
        print(str(sol)+" "+str(score))
    print ("valoare celei mai bune solutii depistate la aceasta rulare:",bestScore )
    print ("Drumul detectat este:", bestSol)
main()
