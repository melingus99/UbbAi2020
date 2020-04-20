from Lab7GradientDescent.Data import Data
import numpy as np
class Controller:
    def __init__(self,data):
        self.data=data
        self.theta = np.ones((len(self.data.trainingSet[0]),1))

    def evaluate(self):
        error=0
        for i in range(len(self.data.testSet)):
            #print(str(self.data.testSet[i]@self.theta)+","+str(self.data.testSetClasses[i]))
            error+=abs(self.data.testSetClasses[i][0]-self.data.testSet[i]@self.theta)
        error=error/len(self.data.testSet)
        return error

    def gradientDescent(self,alpha, iterations):
        m=len(self.data.trainingSetClasses)
        for i in range(iterations):
            self.theta = self.theta - alpha*(1/m)*self.data.trainingSet.T@(self.data.trainingSet@self.theta - self.data.trainingSetClasses)

    def computeCost(self):

        m=len(self.data.trainingSetClasses)
        cost=(1/(2*m))*(self.data.trainingSet@self.theta-self.data.trainingSetClasses).T@(self.data.trainingSet@self.theta-self.data.trainingSetClasses)
        return cost

