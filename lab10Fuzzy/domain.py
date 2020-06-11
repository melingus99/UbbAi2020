from skfuzzy import control as ctrl
import numpy as np
import skfuzzy as fuzz


class Fuzzy:
    def __init__(self,tempLow,tempHigh,capLow,capHigh,powerLow,powerHigh):
        self.temperature = ctrl.Antecedent(np.arange(tempLow, tempHigh+1, 1),'temperature')
        self.capacity = ctrl.Antecedent(np.arange(capLow, capHigh+1, 1),'capacity')
        self.power  = ctrl.Consequent(np.arange(powerLow, powerHigh+1, 1),'power')
        self.temperature.automf(names=['Cold','Cool','Moderate','Hot','VeryHot'])
        self.capacity.automf(names=['Small','Medium','High'])
        self.power.automf(names=['Small','Medium','High'])


    def getTemperature(self):
        return self.temperature

    def getCapacity(self):
        return self.capacity

    def getPower(self):
        return self.power

    def setTemperature(self,Cold,Cool,Moderate,Hot,VeryHot):
        self.temperature['Cold'] = fuzz.trapmf(self.temperature.universe, Cold)
        self.temperature['Cool'] = fuzz.trimf(self.temperature.universe, Cool)
        self.temperature['Moderate'] = fuzz.trimf(self.temperature.universe, Moderate)
        self.temperature['Hot'] = fuzz.trimf(self.temperature.universe, Hot)
        self.temperature['VeryHot'] = fuzz.trapmf(self.temperature.universe, VeryHot)

    def setCapacity(self,Small,Medium,High):
        self.capacity['Small'] = fuzz.trimf(self.capacity.universe, Small)
        self.capacity['Medium'] = fuzz.trimf(self.capacity.universe, Medium)
        self.capacity['High'] = fuzz.trimf(self.capacity.universe, High)

    def setPower(self,Small,Medium,High):
        self.power['Small'] = fuzz.trimf(self.power.universe, Small)
        self.power['Medium'] = fuzz.trimf(self.power.universe, Medium)
        self.power['High'] = fuzz.trimf(self.power.universe, High)


