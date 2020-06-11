import numpy as np
from Lab8ANN.Data import Data
import matplotlib.pyplot as plt

class NeuralNetwork():
    def __init__(self,X,Y,hiddenSize,noFeatures,Lambda,alpha):
        self.theta1 = self.randInitializeWeights(5,hiddenSize)
        self.theta2=self.randInitializeWeights(hiddenSize,1)
        self.X=X
        self.Y=Y
        self.noFeatures=noFeatures
        self.Lambda=Lambda
        self.alpha=alpha

    def feedForward(self,X):
        m= X.shape[0]
        a1 = X @ self.theta1.T
        a1 = np.hstack((np.ones((m,1)), a1)) # hidden layer
        a2 = a1 @ self.theta2.T # output layer

        return a2


    def evaluate(self,testSet,testSetClasses):
        error=0
        prediction=self.feedForward(testSet)
        for i in range(len(testSet)):
            error+=abs(testSetClasses[i][0]-prediction[i])
        error=error/len(testSet)
        return error[0]

    def randInitializeWeights(self,l_in, l_out):
        epi = (6**1/2) / (l_in + l_out)**1/2

        W = np.random.rand(l_out,l_in +1) *(2*epi) -epi

        return W

    def nnCostFunction(self):
        m = self.X.shape[0]
        a1 = self.X @ self.theta1.T
        a1 = np.hstack((np.ones((m,1)), a1)) # hidden layer
        a2 = a1 @ self.theta2.T #output layer

        cost=(1/m)*(a2-self.Y).T@(a2-self.Y)
        cost = cost + self.Lambda/(2*m) * (np.sum(self.theta1[:,1:]**2) + np.sum(self.theta2[:,1:]**2))


        grad1 = np.zeros((self.theta1.shape))
        grad2 = np.zeros((self.theta2.shape))

        for i in range(m):
            xi= self.X[i,:]
            a1i = a1[i,:]
            a2i =a2[i,:]
            d2 = (a2i - self.Y[i,:])*self.alpha
            d1 = self.theta2.T @ d2.T *self.alpha
            grad1= grad1 + d1[1:][:,np.newaxis] @ xi[:,np.newaxis].T
            grad2 = grad2 + d2.T[:,np.newaxis] @ a1i[:,np.newaxis].T

        grad1 = 1/m * grad1
        grad2 = 1/m*grad2

        grad1_reg = grad1 + (self.Lambda/m) * np.hstack((np.zeros((self.theta1.shape[0],1)),self.theta1[:,1:]))
        grad2_reg = grad2 + (self.Lambda/m) * np.hstack((np.zeros((self.theta2.shape[0],1)),self.theta2[:,1:]))

        return cost,grad1_reg,grad2_reg

    def gradientDescentnn(self,num_iters):
        m=len(self.Y)
        cost_history =[]

        for i in range(num_iters):
            cost,grad1,grad2 = self.nnCostFunction()
            self.theta1 = self.theta1 - (self.alpha * grad1)
            self.theta2 = self.theta2 - (self.alpha * grad2)
            cost_history.append(cost)

        return cost_history

def main():
    data=Data("Data")
    trainingset=data.trainingSet
    trainingsetClasses=data.trainingSetClasses
    testSet=data.testSet
    testSetClasses=data.testSetClasses
    nn=NeuralNetwork(trainingset,trainingsetClasses,3,trainingset[0],5,0.01)
    iter=10000
    cost=nn.gradientDescentnn(iter)

    iterations=[]
    for i in range(iter):
        iterations.append(i)
    predictionTest=nn.feedForward(testSet)
    accuracy=nn.evaluate(testSet,testSetClasses)
    error=[]
    for i in cost:
        error.append(i[0][0])
    print("Prediction for test Set:")
    print("Difference between real output and expected output is aproximatively:"+str(accuracy))
    for i in range(len(testSet)):
        print(testSet[i], testSetClasses[i], predictionTest[i])
    plt.plot(iterations, error, label='loss value vs iteration')
    plt.xlabel('Iterations')
    plt.ylabel('loss function')
    plt.legend()
    plt.show()
main()
