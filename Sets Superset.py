A,N= set(input().split()) , int(input())
ans=True
for i in range(N):
    check= set(input().split())
    ans= (ans) and ( A.issuperset(check)) and len(A)> len(check)
print (ans)    