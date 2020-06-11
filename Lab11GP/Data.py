import numpy as np
from random import shuffle
class Data:
    def __init__(self,training,parameters):
        self.trainingSet,self.trainingSetClasses,self.testSet,self.testSetClasses=self.readData(training)
        self.epsilon,self.depth=self.readParameters(parameters)


    def readParameters(self,file):
        f=open(file,"r")
        epsilon=float(f.readline())
        depth=int(f.readline())
        f.close()
        return epsilon,depth


    def readData(self,file):
        f=open(file,"r")
        rawData=f.readlines()
        f.close()
        for i in rawData:
            if i=='\n':
                rawData.remove(i)
        data=[]
        for i in range(len(rawData)):
            rawData[i]=rawData[i][0:len(rawData[i])-1]
            rawData[i]=rawData[i].split(",")
            data.append([float(rawData[i][j]) for j in range(len(rawData[i])-1)])
            if rawData[i][-1]=="Sharp-Right-Turn":
                data[i].append(3)
            if rawData[i][-1] == "Slight-Right-Turn":
                data[i].append(2)
            if rawData[i][-1] == "Move-Forward":
                data[i].append(1)
            if rawData[i][-1] == "Slight-Left-Turn":
                data[i].append(0)
        shuffle(data)
        testSet=data[0:len(data)//5][:]
        trainingSet=data[len(data)//5:len(data)][:]
        trainingSetClasses=[]
        testSetClasses=[]

        for i in range(len(trainingSet)):
            trainingSetClasses.append(trainingSet[i][-1])
            trainingSet[i].pop(-1)
        for i in range(len(testSet)):
            testSetClasses.append(testSet[i][-1])
            testSet[i].pop(-1)

        return trainingSet, trainingSetClasses, testSet, testSetClasses
