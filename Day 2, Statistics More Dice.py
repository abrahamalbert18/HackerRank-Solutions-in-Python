#Dice Probability evenly weighed
import random
import itertools
dice=[1,2,3,4,5,6]
n=input("Please enter the number of Dices: ")

def diceRolls(dice):
    a=itertools.product(dice,dice)
    diceCombos=[i for i in a]
    return diceCombos

def sumProbability(rs,dices):
    requiredSum=rs
    result= [(i,j) for i,j in diceCombinations if i!=j and i+j==requiredSum ]
    print "result ="+str(result)
    return result
    
def findProbability(event,total):
    return float(event)/total
    
diceCombinations=diceRolls(dice)
rs=input("Please enter required sum : ")
event=sumProbability(rs,diceCombinations)
eventLen=len(event)
totalLen=len(diceCombinations)
print findProbability(eventLen,totalLen)
          
                                                                              
    
