import matplotlib.pyplot as plt
class View():
    def __init__(self,controller):
        self.ctrl=controller

    def compute(self):
        output=self.ctrl.compute()
        print("output:")
        for i in output:
            print(i)
        plt.show()

    def showData(self,data):
        for i in data:
            for j in i:
                print(str(j)+" ")
            print("")

    def showInput(self):
        input=self.ctrl.getInput()
        self.showData(input)


    def showProblemParams(self):
        data=self.ctrl.getProblemParams()
        self.showData(data)


    def showOptions(self):
        print("press 1 to see the problem parameters")
        print("press 2 to see the input")
        print("press 3 to set the problem parameters")
        print("press 4 to set the input")
        print("press 5 to compute and see the output")

    def setProblemParams(self):
        self.ctrl.setProblemParams()

    def setInput(self):
        self.ctrl.setInput()


    def menu(self):
        self.showOptions()
        option=input()
        while(1):
            if(option=='1'):
                self.showProblemParams()
            elif(option=='2'):
                self.showInput()
            elif(option=='3'):
                self.setProblemParams()
            elif(option=='4'):
                self.setInput()
            elif(option=='5'):
                self.compute()
            else:
                break
            self.showOptions()
            option=input()
        print("bye bye")
