# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 16:32:24 2020

@author: Bubu
"""



from Controller.controller import Controller
from Problems.LatinSquare import LatinSquare
from Problems.EulerSquare import EulerSquare
import random as rnd
from copy import deepcopy

from domain.Particle import particle


class Ui:
    def __init__(self):
        self.controller=1
        
    def menu(self):
        f=open("EulerSquare.txt","r")
        problem=1
        while(problem!=0):
            print("avaible problems are:\n 1.Latin Square \n 2.EulerSquare")
            problem=int(input("provide the number of the problem that you want to be solved: "))
            if(problem==1):
                n=int(input("provide the size of the matrix: "))
                matrix=[]
                for i in range(0,n):
                    matrix.append([])
                    for j in range(0,n):
                        matrix[i].append(0)
                problem=LatinSquare(matrix)
                self.controller=Controller(problem)
                print("the problem can be solved in 2 ways: \n 1.Greedy \n 2.DFS ")
                option=int(input("provide the number of the method "))
                if(option==1):
                    res,matrix=self.controller.Greedy()
                    if(res==True):
                        print("Great Succes")
                        for i in range(0,len(matrix)):
                            for j in range(0, len(matrix[i])):
                                print(matrix[i][j],end=" ")
                            print()
                    elif(res==False):
                        print("Not Great Succes")
                        for i in range(0,len(matrix)):
                            for j in range(0, len(matrix[i])):
                                print(matrix[i][j],end=" ")
                            print()
                elif(option==2):
                    matrix=self.controller.DFS()
                    for i in range(0,len(matrix)):
                        for j in range(0, len(matrix[i])):
                            print(matrix[i][j],end=" ")
                        print()
            elif(problem==2):
                f1=f.read().split("\n")
                n=int(f1[0])
                firstSet=f1[1].split(" ")
                secondSet=f1[2].split(" ")
                pop=int(f1[3])
                iterations=int(f1[4])
                print("the problem can be solved in 2 ways: \n 1.HC \n 2.EA 3.PSO")
                option=int(input("provide the number of the method "))
                if(option==1):
                    matrix=[]
                    for i in range(0,n):
                        matrix.append([])
                        for j in range(0,n):
                            first=rnd.randint(0,n-1)
                            second=rnd.randint(0,n-1)
                            matrix[i].append([firstSet[first],secondSet[second]])
                    problem=EulerSquare(matrix,firstSet,secondSet)
                    self.controller=Controller(problem)
                    for res,matrix in self.controller.HillClimbing():
                        print("Great Succes")
                        for i in range(0,len(matrix)):
                            for j in range(0,len(matrix)):
                                print("("+matrix[i][j][0]+","+matrix[i][j][1]+")",end=" ")
                            print()

                elif(option==2):
                    mutation=float(f1[3])
                    crossover=float(f1[4])
                    pop=int(f1[5])
                    generations=int(f1[6])
                    population=self.populate(pop,n,firstSet,secondSet)
                    problem=EulerSquare(population,firstSet,secondSet)
                    self.controller=Controller(problem)
                    res,matrix=self.controller.EA(pop,mutation,crossover,generations)
                    if(res==True):
                        print("Great Succes")
                        for i in range(0,len(matrix)):
                            for j in range(0, len(matrix[i])):
                                print(matrix[i][j],end=" ")
                            print()
                    else:
                        print("Not Great Succes")
                        for i in range(0,len(matrix)):
                            for j in range(0, len(matrix[i])):
                                print(matrix[i][j],end=" ")
                            print()

                elif(option==3):
                    w=float(f1[5])
                    c1=float(f1[6])
                    c2=float(f1[7])
                    neighborhoodSize=int(f1[8])
                    population=self.populatePSO(pop,n,firstSet,secondSet)
                    problem=EulerSquare(population,firstSet,secondSet)
                    self.controller=Controller(problem)
                    for res,matrix,score in self.controller.PSO(neighborhoodSize,c1,c2,w,iterations):
                        if(res==True):
                            print("Finished")
                        else:
                            print("Not Finished Yet")
                        print("score is: -"+str(score))
                        for i in range(0,len(matrix)):
                            for j in range(0, len(matrix[i])):
                                print(matrix[i][j],end=" ")
                            print()
        
    def populate(self,pop,n,firstSet,secondSet):
        population=[]
        for i in range(0,pop):
            matrix=[]
            for j in range(0,n):
                matrix.append([])
                for k in range(0,n):
                    first=rnd.randint(0,n-1)
                    second=rnd.randint(0,n-1)
                    matrix[j].append([firstSet[first],secondSet[second]])
            population.append(deepcopy(matrix))
        return population

    def populatePSO(self, pop, n, firstSet, secondSet):
        return [particle(n, firstSet, secondSet) for x in range(pop)]




class Main():
    def __init__(self,ui):
        self.ui=ui
    def run(self):
        self.ui.menu()

ui=Ui()
main=Main(ui)
main.run()
