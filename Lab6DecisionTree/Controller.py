import operator
import math
from Lab6DecisionTree.DecisionTree import *
class Controller:

    def computeEntropy(self,values):
        classes={"B":0,"L":0,"R":0}
        for i in values:
            classes[i[0]]+=1
        sum=0
        total=0
        for i in classes:
            total+=classes[i]
        for i in classes:
            if(classes[i]!=0):
                sum+=(classes[i]/total)*math.log((classes[i]/total),2)
        return -sum

    def gini(self,trainingSet,attributes):
        countAttributes={}
        classes=["L","B","R"]
        for i in attributes:
            countAttributes[i]={}
            for j in range(1,26):
                countAttributes[i][str(j)]={}
                for k in classes:
                    countAttributes[i][str(j)][k]=0

        for i in attributes:
            for j in trainingSet:
                countAttributes[i][j[i]][j[0]]+=1

        total={}
        for i in attributes:
            sum=0
            for j in range(1,26):
                for k in classes:
                    sum+=countAttributes[i][str(j)][k]
            total[i]=sum
        totalPerValue={}
        for i in attributes:
            totalPerValue[i]={}
            for j in range(1,26):
                sum=0
                for k in classes:
                    sum+=countAttributes[i][str(j)][k]
                totalPerValue[i][str(j)]=sum
                for k in classes:
                    if(sum!=0):
                        countAttributes[i][str(j)][k]=(countAttributes[i][str(j)][k]/sum)**2
                sum=0
                for k in classes:
                    sum+=countAttributes[i][str(j)][k]
                countAttributes[i][str(j)]=1-sum
        gini={}
        for i in attributes:
            sum=0
            for j in range(1,26):
                if(total[i]!=0):
                    sum+=totalPerValue[i][str(j)]/total[i]*countAttributes[i][str(j)]
            gini[i]=sum

        return min(gini.items(), key=operator.itemgetter(1))

    def AttributeSelection(self,trainingSet,attributes):
        gain={}
        E=self.computeEntropy(trainingSet)
        countAttributes={}
        exists={}
        for i in range(1,26):
            countAttributes[str(i)]=[]
        for i in attributes:
            for j in trainingSet:
                countAttributes[j[i]].append(j)

        for i in countAttributes:
            countAttributes[i]=len(countAttributes[i])/len(trainingSet)*self.computeEntropy(countAttributes[i])
        exists={}
        gain={}
        for i in attributes:
            for j in range(1,26):
                exists[str(j)]=False
            sum=0
            for j in trainingSet:
                exists[j[i]]=True
            for j in range(1,26):
                if(exists[str(j)]==True):
                    sum+=countAttributes[str(j)]
            gain[i]=1-sum
            exists.clear()


        return max(gain.items(), key=operator.itemgetter(1))



    def GenerateTree(self,trainingSet,attributes):
        node=Node()
        classes=[]
        for i in trainingSet:
            if i[0] not in classes:
                classes.append(i[0])
        if(len(classes)==1):
            node.setData(classes[0])
            return node
        else:
            countAttributes={}
            if(len(attributes)==0):
                for i in trainingSet:
                    if i[0] in countAttributes.keys():
                        countAttributes[i[0]]+=1
                    else:
                        countAttributes[i[0]]=1
                maxx=max(countAttributes.items(), key=operator.itemgetter(1))[0]
                node.setData(maxx[0])
                return node
            else:
                separationAttribute=self.AttributeSelection(trainingSet,attributes)[0]
                node.setData(separationAttribute)
                separationSet=[]
                for i in range(1,26):
                    for j in range(len(trainingSet)):
                        if(trainingSet[j][separationAttribute]==str(i)):
                            separationSet.append(trainingSet[j])
                    if(len(separationSet)==0):
                        countAttributes={}
                        node2=Node()
                        for i in trainingSet:
                            if i[0] in countAttributes.keys():
                                countAttributes[i[0]]+=1
                            else:
                                countAttributes[i[0]]=1
                        maxx=max(countAttributes.items(), key=operator.itemgetter(1))[0]
                        node2.setData(maxx)
                        node.addChild(node2)
                    else:
                        attributesWithoutSeparation=attributes[:]
                        attributesWithoutSeparation.remove(separationAttribute)
                        node.addChild(self.GenerateTree(separationSet,attributesWithoutSeparation))
                    separationSet.clear()
                return node

    def evaluate(self,node,individual,classes):
        if(node.data in classes):
            if(individual[0]==node.data):
                return 1
            else:
                return 0
        for i in range(1,26):
            if(individual[node.data]==str(i)):
                return self.evaluate(node.childs[i-1],individual,classes)
