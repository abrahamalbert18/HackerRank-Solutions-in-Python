from itertools import product
k,m = map(int,input().split())
lst = []

for _ in range(k):
    lst.append(list(map(int,input().split()))[1:])
prod = list(product(*lst))
sums = []

for i in prod:
    sum = 0
    for j in i:
        sum += j**2
    sums.append(sum%m)

print(max(sums))
