# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
import math

class CartesianCoordinates(object):
    def __init__(self,A,B,C,D):
        self.A=A
        self.B=B
        self.C=C
        self.D=D
        self.Angle= None
        
    def vectorDiff(self, X,Y):
        return numpy.subtract(X,Y)
    
    def crossProduct(self, X,Y):
        return numpy.cross(X,Y)
    
    def dotProduct(self,X,Y):
        return numpy.dot(X,Y)
    
    def modulus(self, X):
        return math.sqrt(sum([i**2 for i in X]))
    
    def TorsionAngle(self,X,Y):
        self.Angle= numpy.degrees(numpy.arccos( self.dotProduct(X,Y) / (self.modulus(X) * self.modulus(Y)) ) )
        print round(self.Angle,2)
        
    def Program(self):
        
        AB=self.vectorDiff(self.A,self.B)
        BC=self.vectorDiff(self.B, self.C)
        CD=self.vectorDiff(self.C, self.D)
        X= self.crossProduct(AB,BC)
        Y= self.crossProduct(BC,CD)
        self.TorsionAngle(X,Y)
        

A= map(float, raw_input().split())
B= map(float, raw_input().split())
C= map(float, raw_input().split())
D= map(float, raw_input().split())    
CC=CartesianCoordinates(A,B,C,D)
CC.Program()

        
     
    
                