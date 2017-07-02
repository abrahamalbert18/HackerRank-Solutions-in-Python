t=input()
for testCases in range(t):
    vals=map(int,raw_input().split())
    n,m,s=vals[0],vals[1],vals[2]
    if ((m+s)%n-1) == 0:
        print n
    else:
        print ((m+s)%n-1)      
 