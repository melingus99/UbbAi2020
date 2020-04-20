import numpy as np
class Data:
    def __init__(self,file):
        self.trainingSet,self.trainingSetClasses,self.testSet,self.testSetClasses=self.readData(file)

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
            rawData[i]=rawData[i].split(" ")
            data.append([float(rawData[i][j]) for j in range(len(rawData[i]))])

        testSet=data[0:len(data)//5][:]
        trainingSet=data[len(data)//5:len(data)][:]

        trainingSetClasses=np.empty((len(trainingSet),1))
        testSetClasses=np.empty((len(testSet),1))

        for i in range(len(trainingSet)):
            trainingSetClasses[i]=(trainingSet[i][-1])
            trainingSet[i].pop(-1)

        for i in range(len(testSet)):
            testSetClasses[i]=(testSet[i][-1])
            testSet[i].pop(-1)


        trainingSetnp=np.empty((len(trainingSet),len(trainingSet[0])))
        for i in range(len(trainingSet)):
            trainingSetnp[i]=trainingSet[i]
        trainingSetnp=np.concatenate((np.ones((len(trainingSetnp),1)),trainingSetnp),axis=1)

        testSetnp=np.empty((len(testSet),len(testSet[0])))
        for i in range(len(testSet)):
            testSetnp[i]=testSet[i]
        testSetnp=np.concatenate((np.ones((len(testSetnp),1)),testSetnp),axis=1)

        return trainingSetnp,trainingSetClasses,testSetnp,testSetClasses

