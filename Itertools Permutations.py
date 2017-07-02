# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
ip=raw_input().split()
s=ip[0]
k=int(ip[1])
ans= list(permutations(s,k))
for i in sorted(ans):
    print "".join(i)