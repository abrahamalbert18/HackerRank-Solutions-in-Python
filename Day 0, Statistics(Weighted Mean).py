#Day 0: Weighted Mean
n=input()
X=map(int,raw_input().split())
W=map(int,raw_input().split())
total=0
for i in range(n):
    total+=X[i]*W[i]

print round(total/float(sum(W)),1)    