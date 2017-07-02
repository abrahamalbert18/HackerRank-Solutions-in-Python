# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import *
N = int(raw_input())
assert N>=1 and N<=5
cubes=[]
for i in range(N):
    n = int(raw_input())
    assert n>=1 and n<=10**5
    cubes.append((map(int, raw_input().split())))
    
for i in cubes:
    d= deque(i)
    ans= "Yes"
    vp=[1000000000000]
    while (ans=="Yes" and len(d)>1):
        if d[0] <= d[-1]:
            k=d.pop()
            if k > vp[-1]:
                ans= "No"
        else:
            k=d.popleft()
            if k > vp[-1]:
                ans= "No"
        
        vp.append(k)    
    if len(d)==1:
        if d[0]> vp[-1]:
            ans= "No"
    print ans        
    
        
