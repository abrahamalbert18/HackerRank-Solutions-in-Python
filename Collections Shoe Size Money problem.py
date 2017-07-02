# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import *
X=input()
shoeSizes=map(int, raw_input().split())
shoeSizes=Counter(shoeSizes)
N= input()
customer= [ map(int, raw_input().split())  for i in range(N)]
money=0
for i in customer:
    if (i[0] in shoeSizes) and ( shoeSizes[i[0]] > 0) :
        money+=i[1]
        shoeSizes[i[0]]-=1 
        
print money
