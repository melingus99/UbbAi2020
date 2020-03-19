# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 16:28:56 2020

@author: Bubu
"""

from PyQt5.QtWidgets import (QWidget, QToolTip, 
    QPushButton, QApplication,QGridLayout)
from PyQt5.QtGui import QFont
from Problems.EulerSquare import EulerSquare

from View.testUi import UiMainWindow


class GUI():
    def __init__(self):
        mainUi=UiMainWindow()
        mainUi.show()

        
gui=GUI()
