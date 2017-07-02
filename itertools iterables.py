# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import *
N=input()
alpha=raw_input().split()
k=input()
possibilities= list(combinations(sorted(alpha),k))
count=0
for i in possibilities:
    if 'a' in i:
        count+=1
print count / float(len(possibilities))           
    

