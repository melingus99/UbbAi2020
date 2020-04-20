import numpy as np
from Lab7GradientDescent.Data import Data
from Lab7GradientDescent.Controller import Controller



def main():
    data=Data("Data")
    controller=Controller(data)
    controller.gradientDescent(0.001,100000)
    print("the error is: "+str(controller.evaluate()))

main()

