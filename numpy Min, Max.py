import numpy
N,M = map(int, raw_input().split())
array= numpy.array( [map(int, raw_input().split()) for i in range(N)])
Min= numpy.min(array, axis=1)
print numpy.max(Min)
