# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 16:45:12 2020

@author: Bubu
"""

import matplotlib.pyplot as plt
import numpy as np

def B():
    option="normal"
    while(option!="exit"):
        option=input("enter your distribution: ")
        if(option=="binomial"):
            par=input("enter the number of trials, probability and number of tests \n")
            par=par.split(" ")
            n=int(par[0])
            p=float(par[1])
            test=int(par[2])
            numbers=np.random.binomial(n,p,test)
            plt.plot(numbers,'ro')
            plt.axis([0,n,0,n])
            plt.xlabel("nr test")
            plt.ylabel("number of succeses on each test")
            plt.show()
        elif(option=="Gamma"):
            par=input("enter the shape, scale and size \n")
            par=par.split(" ")
            shape=float(par[0])
            scale=float(par[1])
            size=int(par[2])
            numbers=np.random.gamma(shape,scale,size)
            plt.plot(numbers,"ro")
            plt.axis([0,10,0,10])
            plt.xlabel("nr test")
            plt.ylabel("some numbers")
            plt.show()
            
            
def sudoku(matrix,n):
    for i in range(0,n):
        for j in range(0,n):
            if(matrix[i][j]!=0):
                matrix[i][j]=np.random.randint(1,n+1)
    for i in range(0,n):
        for j in range(0,n):
            for k in range(j+1,n):
                if(matrix[i][j]==matrix[i][k]):
                    return False,matrix
            for k in range(i+1,n):
                 if(matrix[i][j]==matrix[k][j]):
                     return False,matrix

    return True,matrix
            
def crypt(s):
    s=s.split(" ")
    op=s[0][len(s[0])-1]
    s[0]=s[0].split("+")[0]
    cypher=[]
    numbers=[]
    for i in range(0,27):
        cypher.append(np.random.randint(0,16))
    for word in s:
        number=0
        for letter in range(0,len(word)):
            number=number*16+cypher[ord(word[letter])-65]
        numbers.append(number)
    if(op=="+"):
        rez=0
        for i in range(0,len(numbers)-1):
            rez+=numbers[i]
        if(rez==numbers[len(numbers)-1]):
            return True,s,cypher,numbers
        else:
            return False,s,cypher,numbers
    else:
        rez=numbers[0]
        for i in range(1,len(numbers)-1):
            rez-=numbers[i]
        if(rez==numbers[len(numbers)-1]):
            return True,s,cypher,numbers
        else:
            return False,s,cypher,numbers
        
def overlap(l,r,form,matrix):
    for i in range(0,2):
        for j in range(0,4):
            if (form[i][j]==1 and matrix[l+i][r+j]==1):
                return True
    return False

       
def forms():
    matrix=[]
    for i in range(0,5):
        matrix.append([])
        for j in range(0,6):
            matrix[i].append(0)
    form1=[[1,1,1,1],[0,0,0,0]]
    form2=[[1,0,0,0],[1,1,1,0]]
    form3=[[1,0,1,0],[1,1,1,0]]
    form4=[[1,1,1,0],[0,0,1,0]]
    form5=[[0,1,0,0],[1,1,1,0]]
    dicF={1:form1,2:form2,3:form3,4:form4,5:form5}
    dicFString={1:"form1",2:"form2",3:"form3",4:"form4",5:"form5"}
    solution=""
    failed=0
    while(failed<=1000):
        failed+=1
        l=np.random.randint(0,5)
        r=np.random.randint(0,4)
        f=np.random.randint(1,6)
        if(f!=1 and l==4):
            continue
        elif(f==1 and r==3):
            continue
        elif(overlap(l,r,dicF[f],matrix)==True):
            continue
        else:
            if(f==1):
                n=1
                m=4
            else:
                n=2
                m=3
            for i in range(0,n):
                for j in range(0,m):
                    matrix[l+i][r+j]+=dicF[f][i][j]
                    solution+=dicFString[f]+" on position: "+str(l)+" "+str(r)+"\n"
            failed=0
    for i in range(0,5):
        for j in range(0,6):
            if(matrix[i][j]==0):
                return False,solution
    return True,solution
            
        
    
    
def C():
    option=1
    while(option!=0):
        option=input("please enter the number of the problem: ")
        option=int(option)
        tests=input("choose the maximum number of attempts to find a solution: ")
        tests=int(tests)
        if(option==1):
            n=input("choose a number for the sizes of the sudoku table: ")
            n=int(n)
            rez=False
            matrix=[]
            for i in range(0,n):
                matrix.append([])
            print("write a sudoku table with values between 0 and n where 0 is a free space ")
            for i in range(0,n):
                strInput=input()
                strInput=strInput.split(" ")
                for j in range(0,n):
                    matrix[i].append(int(strInput[j]))
            while(rez==False and tests>0):
                rez,matrix=sudoku(matrix,n)
                tests-=1
            if(rez==True):
                print(matrix)
            else:
                print("no solution was found")
        elif(option==2):
            s=input("choose your words wisely ")
            rez=False
            cypher=[]
            numbers=[]
            while(rez==False and tests>0):
                rez,srez,cypher,numbers=crypt(s)
                tests-=1
            if(rez==True):
                print("the list of words are: "+srez+"their respective numbers are: "+numbers)
            else:
                print("no solution was found")
        elif(option==3):
            rez=False
            while(rez==False and tests>0):
                rez,solution=forms()
                tests-=1
            if(rez==True):
                print("solution is:\n"+solution)
            else:
                print("no solution was found")
                
C()