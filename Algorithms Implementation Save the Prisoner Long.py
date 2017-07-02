t=input()
for testCases in range(t):
    vals=map(int,raw_input().split())
    n,m,s=vals[0],vals[1],vals[2]
    prisoners=range(1,n+1)
    while m!=1:
        if s==n:
            s=1
        else:
            s+=1
        m-=1
    print s    
 