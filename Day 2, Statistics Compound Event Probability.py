#Compound Event Probability
import random, itertools
n=input("Number of Urns : ")
X=['R','R','R','R','B','B','B']
Y=['R','R','R','R','R','B','B','B','B']
Z=['R','R','R','R','B','B','B','B']
comboGen=[i for i in itertools.product(X,Y,Z)]
XYZ=[(x,y,z) for x,y,z in comboGen if (x,y,z)==('R','R','B') or (x,y,z)==('R','B','R') or (x,y,z)==('B','R','R')]

def findProbability(event,total):
    return float(event)/total

event=len(XYZ)
total=len(comboGen)        
print findProbability(event,total)    