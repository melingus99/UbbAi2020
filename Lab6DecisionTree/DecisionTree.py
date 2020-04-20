class Node():
    def __init__(self):
        self.childs=[]
        self.data=0

    def addChild(self,child):
        self.childs.append(child)

    def setData(self,data):
        self.data=data

class DecisionTree:
    def __init__(self,root,classes):
        self.root=root
        self.classes=classes


