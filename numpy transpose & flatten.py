import numpy
N, M = map(int, raw_input().split())
arr=numpy.array( [map(int, raw_input().split()) for i in range(N)])
print numpy.transpose(arr)
print arr.flatten()
    