# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import *
K,M= map(int, raw_input().split())
List=[]
assert K>=1 and K<=7
assert M>=1 and M <=1000

for i in range(K):
    List.append(map(int,raw_input().split()[1:]))
Sum=0
for i in product(*List):
    Sum += (i**2) 
print  Sum % M
