import numpy
N,M = map(int, raw_input().split())
A = numpy.array([raw_input().split() for _ in range(N)],int)
B = numpy.array([raw_input().split() for _ in range(N)],int)
print(A + B)
print(A - B)
print(A * B)
print(A / B)
print(A % B)
print A ** B