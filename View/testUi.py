# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testUi.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from View.LatinSquareUi import LatinSquareUi
from View.EulerSquareUI import EulerSquareUi
class UiMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)
        self.latinSquareWindow=QtWidgets.QMainWindow()
        self.latinSquareUi=LatinSquareUi()
        self.latinSquareUi.setupUi(self.latinSquareWindow)
        self.eulerSquareWindow=QtWidgets.QMainWindow()
        self.eulerSquareUi=EulerSquareUi()
        self.eulerSquareUi.setupUi(self.eulerSquareWindow)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SelectButton = QtWidgets.QPushButton(self.centralwidget)
        self.SelectButton.setGeometry(QtCore.QRect(120, 410, 93, 28))
        self.SelectButton.setObjectName("SelectButton")
        self.SelectButton.clicked.connect(self.SelectButtonClicked)
        self.problemsList = QtWidgets.QListView(self.centralwidget)
        self.problemsList.setGeometry(QtCore.QRect(40, 210, 256, 192))
        self.problemsList.setObjectName("problemsList")
        entries = ['Latin Square','Euler Square']

        model = QtGui.QStandardItemModel()
        self.problemsList.setModel(model)

        for i in entries:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SelectButton.setText(_translate("MainWindow", "Select"))
        
    def SelectButtonClicked(self):
        itms = self.problemsList.selectedIndexes()
        itm=itms[0]

        if(itm.row()==0):
            self.latinSquareWindow.show()
        else:
            self.eulerSquareWindow.show()
        #self.close()


    def show(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = UiMainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
