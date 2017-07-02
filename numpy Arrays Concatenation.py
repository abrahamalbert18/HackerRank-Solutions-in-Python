import numpy
N,M, P= map(int, raw_input().split())
A= numpy.array([ map(int, raw_input().split())  for i in range(N)] )
B= numpy.array([ map(int, raw_input().split())  for i in range(M)] )
print numpy.concatenate((A,B),axis =0)
             
