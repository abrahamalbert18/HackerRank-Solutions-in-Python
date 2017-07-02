import numpy
N= input()
arr= numpy.array( [(map(float, raw_input().split())) for i in range(N)])
print numpy.linalg.det(arr)    #computes the determinent value of a matrix

#numpy.linalg.eig(array)   --- computes the eigen values of the matrix
#numpy.linalg.inv(array)   --- computes the inverse of a matrix
