from lab10Fuzzy.domain import Fuzzy
from skfuzzy import control as ctrl
class Repo:
    def __init__(self,problemFile,inputFile):
        self.problemFile=problemFile
        self.inputFile=inputFile
        self.setProblemParams()
        self.setInput()

    def setProblemParams(self):
        self.data=self.readData(self.problemFile)
        self.setFuzzy()
        self.setRules()

    def setInput(self):
        self.input=self.readData(self.inputFile)

    def readData(self,textfile):
        f=open(textfile,"r")
        rawData=f.readlines()
        data=[]
        f.close()
        for i in range(0,len(rawData)):
            rawData[i]=rawData[i][0:len(rawData[i])-1]
            rawData[i]=rawData[i].split(' ')
            data.append([int(rawData[i][j]) for j in range(len(rawData[i]))])
        return data

    def setFuzzy(self):
        self.Fuzzy=Fuzzy(tempLow=self.data[0][0],tempHigh=self.data[0][1],capLow=self.data[1][0],
                         capHigh=self.data[1][1],powerLow=self.data[2][0],powerHigh=self.data[2][1])

        self.Fuzzy.setTemperature(self.data[3],self.data[4],self.data[5],self.data[6],self.data[7])

        self.Fuzzy.setCapacity(self.data[8],self.data[9],self.data[10])

        self.Fuzzy.setPower(self.data[11],self.data[12],self.data[13])

    def setRules(self):
        temperature=self.Fuzzy.getTemperature()
        capacity=self.Fuzzy.getCapacity()
        power=self.Fuzzy.getPower()

        rule1 = ctrl.Rule((temperature['Cold'] & capacity['Medium']) | (temperature['Cool'] & capacity['Medium']), power['Medium'])


        rule2= ctrl.Rule((temperature['Cold'] & capacity['High']) | (temperature['Cool'] & capacity['High']),power['High'])


        rule3=ctrl.Rule((capacity['Small']) | (capacity['Medium'] & ~temperature['Cold'] & ~temperature['Cool'])
                        | (capacity['High'] & ~temperature['Cold'] & ~temperature['Cool']),power['Small'])

        self.rules=[rule1,rule2,rule3]

    def compute(self):
        powerCtrl = ctrl.ControlSystem(self.rules)
        powering = ctrl.ControlSystemSimulation(powerCtrl)
        outputs=[]
        for i in self.input:
            powering.input['temperature'] = i[0]
            powering.input['capacity'] = i[1]

            powering.compute()

            self.Fuzzy.getPower().view(sim=powering)

            outputs.append(powering.output['power'])
        return outputs

    def getInput(self):
        return self.input

    def getProblemParams(self):
        return self.data




