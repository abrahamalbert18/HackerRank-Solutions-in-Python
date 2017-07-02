# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

class CartesianCoordinates(object):
    def __init__(self,A,B,C,D):
        self.A=A
        self.B=B
        self.C=C
        self.D=D
        self.Angle= None
        
    def vectorDiff(self, X,Y):
        return [Y[i]- X[i] for i in range(len(X))]
    
    def crossProduct(self, X,Y):
        vector=[]
        vector.append( X[1] * Y[2]- X[2]* Y[1])
        vector.append( X[2] * Y[0]- X[0]* Y[2])
        vector.append( X[0] * Y[1]- X[1]* Y[0])
        return vector

    
    def dotProduct(self,X,Y):
        return sum([X[i] * Y[i] for i in range(len(X))])
    
    def modulus(self, X):
        return math.sqrt(sum([i**2 for i in X]))
    
    def TorsionAngle(self,X,Y):
        self.Angle= math.degrees(math.acos( self.dotProduct(X,Y) / (self.modulus(X) * self.modulus(Y)) ) )
    
    def Program(self):
        
        AB=self.vectorDiff(self.A,self.B)
        BC=self.vectorDiff(self.B, self.C)
        CD=self.vectorDiff(self.C, self.D)
        X= self.crossProduct(AB,BC)
        Y= self.crossProduct(BC,CD)
        self.TorsionAngle(X,Y)
        print round(self.Angle,2)

A= map(float, raw_input().split())
B= map(float, raw_input().split())
C= map(float, raw_input().split())
D= map(float, raw_input().split())    
CC=CartesianCoordinates(A,B,C,D)
CC.Program()

        
     
    
                