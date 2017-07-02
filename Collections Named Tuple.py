# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import *
N,students= input(), namedtuple('students',raw_input().split())
stud=  [students(*raw_input().split()) for i in range(N)]                 #passed string of input as a single key
print sum([float (i.MARKS) for i in stud]) /N

   
'''    
Code 01

>>> from collections import namedtuple
>>> Point = namedtuple('Point','x,y')
>>> pt1 = Point(1,2)
>>> pt2 = Point(3,4)
>>> dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
>>> print dot_product
11
Code 02

>>> from collections import namedtuple
>>> Car = namedtuple('Car','Price Mileage Colour Class')
>>> xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
>>> print xyz
Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
>>> print xyz.Class
Y


'''