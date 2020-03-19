# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LatinSquareUi.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be los

import concurrent.futures
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QRunnable, pyqtSlot
from View.Worker import Worker
from Controller.controller import Controller
from Problems.LatinSquare import LatinSquare
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
class LatinSquareUi(object):
    def setupUi(self, Form):
        self.threadpool = QThreadPool()
        self.controller=1
        Form.setObjectName("Form")
        Form.resize(549, 400)
        self.sizeLabel = QtWidgets.QLabel(Form)
        self.sizeLabel.setGeometry(QtCore.QRect(10, 30, 131, 16))
        self.sizeLabel.setObjectName("sizeLabel")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(120, 30, 51, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 351, 20))
        self.label.setObjectName("label")
        self.latinSquareMethods = QtWidgets.QListView(Form)
        self.latinSquareMethods.setGeometry(QtCore.QRect(10, 80, 111, 192))
        self.latinSquareMethods.setObjectName("latinSquareMethods")
        entries = ['Greedy','DFS']

        model = QtGui.QStandardItemModel()
        self.latinSquareMethods.setModel(model)

        for i in entries:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)
        self.latinSquareStartButton = QtWidgets.QPushButton(Form)
        self.latinSquareStartButton.setGeometry(QtCore.QRect(20, 280, 93, 28))
        self.latinSquareStartButton.setObjectName("latinSquareStartButton")
        self.latinSquareStartButton.clicked.connect(self.latinSquareStartButtonClicked)

        self.SolutionView = QtWidgets.QListView(Form)
        self.SolutionView.setGeometry(QtCore.QRect(310, 50, 221, 221))
        self.SolutionView.setObjectName("SolutionView")
        self.solutionModel = QtGui.QStandardItemModel()
        self.SolutionView.setModel(self.solutionModel)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.sizeLabel.setText(_translate("Form", "Size of the matrix"))
        self.label.setText(_translate("Form", "Type the size of the matrix and select the type of the method"))
        self.latinSquareStartButton.setText(_translate("Form", "Start"))

    def latinSquareStartButtonClicked(self):
        itms = self.latinSquareMethods.selectedIndexes()
        itm=itms[0].row()
        size = int(self.lineEdit.text())

        matrix=[]
        for i in range(0,size):
            matrix.append([])
            for j in range(0,size):
                matrix[i].append(0)
        problem=LatinSquare(matrix)
        self.controller=Controller(problem)
        if(itm==0):
            worker=Worker(self.controller.Greedy,self.populate,1)
            self.threadpool.start(worker)
        else:
            worker=Worker(self.controller.DFS,self.populate,1)
            self.threadpool.start(worker)

    def populate(self,res,matrix):
        if(res==True):
            item = QtGui.QStandardItem("Great Succes")
        else:
            item=QtGui.QStandardItem("Not Great Succes")
        self.solutionModel=QStandardItemModel()
        self.solutionModel.appendRow(item)
        for i in range(0,len(matrix)):
            line=""
            for j in range(0,len(matrix)):
                line+=str(matrix[i][j])+" "
            item=QtGui.QStandardItem(line)
            self.solutionModel.appendRow(item)
        self.SolutionView.setModel(self.solutionModel)

    def show(self):
        Form = QtWidgets.QWidget()
        ui = LatinSquareUi()
        ui.setupUi(Form)
        Form.show()
