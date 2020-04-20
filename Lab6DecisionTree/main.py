from Lab6DecisionTree.Problem import Problem
from Lab6DecisionTree.Controller import Controller
from Lab6DecisionTree.DecisionTree import *
import numpy
def main(iterations=30):
    listScores=[]
    for i in range(iterations):
        problem=Problem()
        controller=Controller()
        tree=DecisionTree(controller.GenerateTree(problem.trainingSet,problem.attributes),problem.classes)
        sum=0
        for i in problem.testSet:
            sum+=controller.evaluate(tree.root,i,problem.classes)
        percentage=sum/len(problem.testSet)
        listScores.append(percentage)

    average=numpy.average(listScores)
    std=numpy.std(listScores)
    print("average score: "+str(average))
    print("standard deviation: "+str(std))





main()
