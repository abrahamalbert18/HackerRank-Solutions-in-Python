# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import *
n= input()
d= deque()
code= [raw_input().split() for i in range(n)]
for i in code:
    if len(i)> 1:
        val= i[-1]
        op= i[0] + "(" + val + ")"
        eval('d.'+ op)
    else:
        eval('d.'+ i[0] +"()")
print " ".join(map(str, d))   