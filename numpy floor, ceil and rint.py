import numpy
numpy.set_printoptions(sign=' ')
array= numpy.array( map(float, raw_input().split()))
print numpy.floor(array)
print numpy.ceil(array)
print numpy.rint(array)
