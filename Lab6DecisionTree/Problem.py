import random

class Problem:
    def __init__(self):
        self.data=self.readData()
        self.testSet,self.trainingSet,self.classes,self.attributes=self.processData()

    def readData(self):
        f= open("balance-scale.data","r")
        data=f.readlines()
        for i in range(len(data)):
            data[i]=data[i].split(",")
            data[i][4]=data[i][4][0]
        f.close()
        return data

    def processData(self):
        random.shuffle(self.data)
        classes=[]
        for i in range(0,len(self.data)):
            self.data[i][1]=str(int (self.data[i][1])*int(self.data[i][2]))
            self.data[i][2]=str(int (self.data[i][3])*int(self.data[i][4]))
            self.data[i].pop(3)
            self.data[i].pop(3)
            if(self.data[i][0] not in classes):
                classes.append(self.data[i][0])

        attributes=[i for i in range(len(self.data[0]))]
        attributes.pop(0)
        testSet=self.data[0:(len(self.data)//5)]
        trainingSet=self.data[len(self.data)//5:len(self.data)]
        return testSet,trainingSet,classes,attributes


