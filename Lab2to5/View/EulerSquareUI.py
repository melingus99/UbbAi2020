# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eulerSquare.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThreadPool
from Lab2to5.View.Worker import Worker
from Lab2to5.Controller.controller import Controller
from Lab2to5.Problems.EulerSquare import EulerSquare
import random as rand
import copy
from Lab2to5.domain.Particle import particle


class EulerSquareUi(object):
    def setupUi(self, Form):
        self.threadpool = QThreadPool()
        self.controller=1
        Form.setObjectName("Form")
        Form.resize(1144, 554)

        self.eulerSquareMethodsList = QtWidgets.QListView(Form)
        self.eulerSquareMethodsList.setGeometry(QtCore.QRect(20, 30, 111, 192))
        self.eulerSquareMethodsList.setObjectName("eulerSquareMethodsList")
        entries = ['HillClimbing','Evolutionary algorithm','Particle Swarm Optimisation',"Ant Colony Optimisation"]

        model = QtGui.QStandardItemModel()
        self.eulerSquareMethodsList.setModel(model)

        for i in entries:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)
        self.sizeLabel = QtWidgets.QLabel(Form)
        self.sizeLabel.setGeometry(QtCore.QRect(150, 30, 55, 16))
        self.sizeLabel.setObjectName("sizeLabel")

        self.firstSetLabel = QtWidgets.QLabel(Form)
        self.firstSetLabel.setGeometry(QtCore.QRect(150, 70, 55, 16))
        self.firstSetLabel.setObjectName("firstSetLabel")

        self.secondSetLabel = QtWidgets.QLabel(Form)
        self.secondSetLabel.setGeometry(QtCore.QRect(150, 120, 71, 16))
        self.secondSetLabel.setObjectName("secondSetLabel")

        self.titleLabel = QtWidgets.QLabel(Form)
        self.titleLabel.setGeometry(QtCore.QRect(20, 10, 301, 16))
        self.titleLabel.setObjectName("titleLabel")

        self.sizeEdit = QtWidgets.QLineEdit(Form)
        self.sizeEdit.setGeometry(QtCore.QRect(280, 30, 113, 22))
        self.sizeEdit.setObjectName("sizeEdit")

        self.firstSetEdit = QtWidgets.QLineEdit(Form)
        self.firstSetEdit.setGeometry(QtCore.QRect(280, 70, 113, 22))
        self.firstSetEdit.setObjectName("firstSetEdit")

        self.secondSetEdit = QtWidgets.QLineEdit(Form)
        self.secondSetEdit.setGeometry(QtCore.QRect(280, 120, 113, 22))
        self.secondSetEdit.setObjectName("secondSetEdit")

        self.startButton = QtWidgets.QPushButton(Form)
        self.startButton.setGeometry(QtCore.QRect(30, 270, 93, 28))
        self.startButton.setObjectName("startButton")
        self.startButton.clicked.connect(self.startButtonClicked)

        self.crossoverEdit = QtWidgets.QLineEdit(Form)
        self.crossoverEdit.setGeometry(QtCore.QRect(280, 190, 113, 22))
        self.crossoverEdit.setObjectName("crossoverEdit")

        self.probabilityOfCrossover = QtWidgets.QLabel(Form)
        self.probabilityOfCrossover.setGeometry(QtCore.QRect(140, 190, 141, 16))
        self.probabilityOfCrossover.setObjectName("probabilityOfCrossover")

        self.probabilityOfMutationEdit = QtWidgets.QLineEdit(Form)
        self.probabilityOfMutationEdit.setGeometry(QtCore.QRect(280, 230, 113, 22))
        self.probabilityOfMutationEdit.setObjectName("probabilityOfMutationEdit")

        self.populationEdit = QtWidgets.QLineEdit(Form)
        self.populationEdit.setGeometry(QtCore.QRect(280, 290, 113, 22))
        self.populationEdit.setObjectName("populationEdit")

        self.populationSizeButton = QtWidgets.QLabel(Form)
        self.populationSizeButton.setGeometry(QtCore.QRect(140, 290, 121, 16))
        self.populationSizeButton.setObjectName("populationSizeButton")

        self.ProbabilityMutationButton = QtWidgets.QLabel(Form)
        self.ProbabilityMutationButton.setGeometry(QtCore.QRect(140, 230, 131, 16))
        self.ProbabilityMutationButton.setObjectName("ProbabilityMutationButton")

        self.generationEdit = QtWidgets.QLineEdit(Form)
        self.generationEdit.setGeometry(QtCore.QRect(280, 340, 113, 22))
        self.generationEdit.setObjectName("generationEdit")

        self.generationsLabel = QtWidgets.QLabel(Form)
        self.generationsLabel.setGeometry(QtCore.QRect(140, 340, 131, 16))
        self.generationsLabel.setObjectName("generationsLabel")

        self.optionalLabel = QtWidgets.QLabel(Form)
        self.optionalLabel.setGeometry(QtCore.QRect(190, 150, 141, 20))
        self.optionalLabel.setObjectName("optionalLabel")

        self.bestSolutionView = QtWidgets.QListView(Form)
        self.bestSolutionView.setGeometry(QtCore.QRect(740, 200, 311, 251))
        self.bestSolutionView.setObjectName("bestSolutionView")
        
        self.stopButton = QtWidgets.QPushButton(Form)
        self.stopButton.setGeometry(QtCore.QRect(840, 460, 93, 28))
        self.stopButton.setObjectName("stopButton")
        self.stopButton.clicked.connect(self.stopButtonClicked)


        self.solutionModel=QtGui.QStandardItemModel()
        self.bestSolutionView.setModel(self.solutionModel)


        self.bestSolutionLabel = QtWidgets.QLabel(Form)
        self.bestSolutionLabel.setGeometry(QtCore.QRect(810, 150, 161, 31))
        self.bestSolutionLabel.setObjectName("bestSolutionLabel")

        self.psoParametersLabel = QtWidgets.QLabel(Form)
        self.psoParametersLabel.setGeometry(QtCore.QRect(470, 160, 131, 16))
        self.psoParametersLabel.setObjectName("psoParametersLabel")

        self.populationPSOLabel = QtWidgets.QLabel(Form)
        self.populationPSOLabel.setGeometry(QtCore.QRect(410, 190, 71, 16))
        self.populationPSOLabel.setObjectName("populationPSOLabel")

        self.c1Label = QtWidgets.QLabel(Form)
        self.c1Label.setGeometry(QtCore.QRect(410, 230, 55, 16))
        self.c1Label.setObjectName("c1Label")

        self.c2Label = QtWidgets.QLabel(Form)
        self.c2Label.setGeometry(QtCore.QRect(410, 270, 55, 16))
        self.c2Label.setObjectName("c2Label")

        self.wLabel = QtWidgets.QLabel(Form)
        self.wLabel.setGeometry(QtCore.QRect(410, 300, 55, 16))
        self.wLabel.setObjectName("wLabel")

        self.neighborhoodLabel = QtWidgets.QLabel(Form)
        self.neighborhoodLabel.setGeometry(QtCore.QRect(410, 350, 111, 16))
        self.neighborhoodLabel.setObjectName("neighborhoodLabel")

        self.iterationLabel = QtWidgets.QLabel(Form)
        self.iterationLabel.setGeometry(QtCore.QRect(410, 390, 121, 16))
        self.iterationLabel.setObjectName("iterationLabel")

        self.populationPSOEdit = QtWidgets.QLineEdit(Form)
        self.populationPSOEdit.setGeometry(QtCore.QRect(480, 190, 113, 22))
        self.populationPSOEdit.setObjectName("populationPSOEdit")

        self.c1PSOEdit = QtWidgets.QLineEdit(Form)
        self.c1PSOEdit.setGeometry(QtCore.QRect(480, 230, 113, 22))
        self.c1PSOEdit.setObjectName("c1PSOEdit")

        self.c2PSOEdit = QtWidgets.QLineEdit(Form)
        self.c2PSOEdit.setGeometry(QtCore.QRect(480, 270, 113, 22))
        self.c2PSOEdit.setObjectName("c2PSOEdit")

        self.wPSOEdit = QtWidgets.QLineEdit(Form)
        self.wPSOEdit.setGeometry(QtCore.QRect(480, 300, 113, 22))
        self.wPSOEdit.setObjectName("wPSOEdit")

        self.neighborhoodPSOEdit = QtWidgets.QLineEdit(Form)
        self.neighborhoodPSOEdit.setGeometry(QtCore.QRect(540, 350, 113, 22))
        self.neighborhoodPSOEdit.setObjectName("neighborhoodPSOEdit")

        self.IterationsPSOEdit = QtWidgets.QLineEdit(Form)
        self.IterationsPSOEdit.setGeometry(QtCore.QRect(540, 390, 113, 22))
        self.IterationsPSOEdit.setObjectName("IterationsPSOEdit")

        self.AcoLabel = QtWidgets.QLabel(Form)
        self.AcoLabel.setGeometry(QtCore.QRect(500, 10, 131, 16))
        self.AcoLabel.setObjectName("AcoLabel")

        self.NoEpoch = QtWidgets.QLabel(Form)
        self.NoEpoch.setGeometry(QtCore.QRect(400, 30, 111, 16))
        self.NoEpoch.setObjectName("NoEpoch")

        self.AntLabel = QtWidgets.QLabel(Form)
        self.AntLabel.setGeometry(QtCore.QRect(400, 70, 101, 16))
        self.AntLabel.setObjectName("AntLabel")

        self.alphaLabel = QtWidgets.QLabel(Form)
        self.alphaLabel.setGeometry(QtCore.QRect(400, 120, 55, 16))
        self.alphaLabel.setObjectName("alphaLabel")

        self.betaLabel = QtWidgets.QLabel(Form)
        self.betaLabel.setGeometry(QtCore.QRect(630, 30, 31, 16))
        self.betaLabel.setObjectName("betaLabel")

        self.rhoLabel = QtWidgets.QLabel(Form)
        self.rhoLabel.setGeometry(QtCore.QRect(630, 70, 31, 16))
        self.rhoLabel.setObjectName("rhoLabel")

        self.q0Label = QtWidgets.QLabel(Form)
        self.q0Label.setGeometry(QtCore.QRect(630, 120, 21, 16))
        self.q0Label.setObjectName("q0Label")

        self.NoEpochEdit = QtWidgets.QLineEdit(Form)
        self.NoEpochEdit.setGeometry(QtCore.QRect(510, 30, 113, 22))
        self.NoEpochEdit.setObjectName("NoEpochEdit")

        self.NoAntsEdit = QtWidgets.QLineEdit(Form)
        self.NoAntsEdit.setGeometry(QtCore.QRect(510, 70, 113, 22))
        self.NoAntsEdit.setObjectName("NoAntsEdit")

        self.alphaEdit = QtWidgets.QLineEdit(Form)
        self.alphaEdit.setGeometry(QtCore.QRect(510, 120, 113, 22))
        self.alphaEdit.setObjectName("alphaEdit")

        self.betaEdit = QtWidgets.QLineEdit(Form)
        self.betaEdit.setGeometry(QtCore.QRect(660, 30, 113, 22))
        self.betaEdit.setObjectName("betaEdit")

        self.rhoEdit = QtWidgets.QLineEdit(Form)
        self.rhoEdit.setGeometry(QtCore.QRect(660, 70, 113, 22))
        self.rhoEdit.setObjectName("rhoEdit")

        self.q0Edit = QtWidgets.QLineEdit(Form)
        self.q0Edit.setGeometry(QtCore.QRect(660, 120, 113, 22))
        self.q0Edit.setObjectName("q0Edit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.sizeLabel.setText(_translate("Form", "Size"))
        self.firstSetLabel.setText(_translate("Form", "First Set"))
        self.secondSetLabel.setText(_translate("Form", "Second Set"))
        self.titleLabel.setText(_translate("Form", "Please fill in the parameters and select the method"))
        self.startButton.setText(_translate("Form", "Start"))
        self.probabilityOfCrossover.setText(_translate("Form", "Probability of Crossover"))
        self.populationSizeButton.setText(_translate("Form", "Population"))
        self.ProbabilityMutationButton.setText(_translate("Form", "Probability of Mutation"))
        self.generationsLabel.setText(_translate("Form", "Generations"))
        self.optionalLabel.setText(_translate("Form", "Parameters for EA:"))
        self.bestSolutionLabel.setText(_translate("Form", "Best solution found yet:"))
        self.psoParametersLabel.setText(_translate("Form", "Paremeters for PSO:"))
        self.populationPSOLabel.setText(_translate("Form", "Population:"))
        self.c1Label.setText(_translate("Form", "c1:"))
        self.c2Label.setText(_translate("Form", "c2:"))
        self.wLabel.setText(_translate("Form", "w:"))
        self.neighborhoodLabel.setText(_translate("Form", "neighborhood Size:"))
        self.iterationLabel.setText(_translate("Form", "Number of Iterations:"))
        self.stopButton.setText(_translate("Form","Stop"))
        self.AcoLabel.setText(_translate("Form", "parameters for ACO:"))
        self.NoEpoch.setText(_translate("Form", "Number of Epoch:"))
        self.AntLabel.setText(_translate("Form", "Number of Ants:"))
        self.alphaLabel.setText(_translate("Form", "Alpha:"))
        self.betaLabel.setText(_translate("Form", "Beta:"))
        self.rhoLabel.setText(_translate("Form", "Rho:"))
        self.q0Label.setText(_translate("Form", "Q0:"))

    def makePopulationEA(self,pop,n,firstSet,secondSet):
        population=[]
        for i in range(0,pop):
            matrix=[]
            for j in range(0,n):
                matrix.append([])
                for k in range(0,n):
                    first=rand.randint(0,n-1)
                    second=rand.randint(0,n-1)
                    matrix[j].append([firstSet[first],secondSet[second]])
            population.append(copy.deepcopy(matrix))
        return population

    def makePopulationPSO(self,pop,n,firstSet,secondSet):
        return [particle(n, firstSet, secondSet) for x in range(pop)]

    def startButtonClicked(self):
        itms = self.eulerSquareMethodsList.selectedIndexes()
        itm=itms[0].row()
        size=int(self.sizeEdit.text())
        firstSet=self.firstSetEdit.text().split(" ")
        secondSet=self.secondSetEdit.text().split(" ")

        if(itm==0):
            init=[]
            for i in range(0,size):
                init.append([])
                for j in range(0,size):
                    first=rand.randint(0,size-1)
                    second=rand.randint(0,size-1)
                    init[i].append([firstSet[first],secondSet[second]])
        elif(itm==1):
            PCrossover=float(self.crossoverEdit.text())
            PMutation=float(self.probabilityOfMutationEdit.text())
            population=int(self.populationEdit.text())
            generations=int(self.generationEdit.text())
            init=self.makePopulationEA(population,size,firstSet,secondSet)

        elif(itm==2):
            population=int(self.populationPSOEdit.text())
            c1=float(self.c1PSOEdit.text())
            c2=float(self.c2PSOEdit.text())
            w=float(self.wPSOEdit.text())
            neighborhoodSize=int(self.neighborhoodPSOEdit.text())
            iterations=int(self.IterationsPSOEdit.text())
            init=self.makePopulationPSO(population,size,firstSet,secondSet)
        elif(itm==3):
            noEpoch=int(self.NoEpochEdit.text())
            noAnts=int(self.NoAntsEdit.text())
            alpha=float(self.alphaEdit.text())
            beta=float(self.betaEdit.text())
            rho=float(self.rhoEdit.text())
            q0=float(self.q0Edit.text())
            init=[]

        problem=EulerSquare(init,firstSet,secondSet)
        self.controller=Controller(problem)


        if(itm==0):
            self.worker=Worker(self.controller.HillClimbing,self.populateView,2)
            self.threadpool.start(self.worker)
        elif(itm==1):
            self.worker=Worker(self.controller.EA,self.populateView,2,population,PMutation,PCrossover,generations)
            self.threadpool.start(self.worker)
        elif(itm==2):
            self.worker=Worker(self.controller.PSO,self.populateView,2,neighborhoodSize,c1,c2,w,iterations)
            self.threadpool.start(self.worker)
        elif(itm==3):
            self.worker=Worker(self.controller.ACO,self.populateView,2,noEpoch,noAnts,alpha,beta,rho,q0)
            self.threadpool.start(self.worker)
            
    def stopButtonClicked(self):
        self.worker.stop()
        self.threadpool.clear()



    def populateView(self,res,matrix,score,iteration):
        if(res==True):
            itemSucces = QtGui.QStandardItem("Finished")
        else:
            itemSucces=QtGui.QStandardItem("Not Finished Yet")
        self.solutionModel.clear()
        self.solutionModel.appendRow(itemSucces)
        itemIteration=QtGui.QStandardItem("Iteration:"+str(iteration))
        self.solutionModel.appendRow(itemIteration)
        itemScore=QtGui.QStandardItem("score: "+"-"+str(score))
        self.solutionModel.appendRow(itemScore)
        for i in range(0,len(matrix)):
            line=""
            for j in range(0,len(matrix)):
                line+="("+str(matrix[i][j][0])+","+str(matrix[i][j][1])+")"+" "
            itemLine=QtGui.QStandardItem(line)
            self.solutionModel.appendRow(itemLine)
            

    def show(self):
        Form = QtWidgets.QWidget()
        ui = EulerSquareUi()
        ui.setupUi(Form)
        Form.show()
