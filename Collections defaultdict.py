# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import *
n, m = map(int, raw_input().split())
A= [raw_input() for i in range(n)]
B= [raw_input() for i in range(m)]
d= defaultdict(list)
index=0
for i in A:
    d[i].append( A.index(i, index) + 1)
    index+=1
for i in B:
    if i not in A:
        print -1
    else:
        print " ".join(map(str, d[i]))   # print a list of elements with uniform space/gap
        
        
