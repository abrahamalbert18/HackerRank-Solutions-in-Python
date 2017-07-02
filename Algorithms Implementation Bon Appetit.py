# Enter your code here. Read input from STDIN. Print output to STDOUT
vals=map(int,raw_input().split())
n,k=vals[0], vals[1]
cost=map(int,raw_input().split())
total=sum(cost)
aCharge=total/2
bActual=(total-(cost[k])) / 2
bCharged=input()
if bCharged!=bActual:
    print bCharged-bActual
else:
    print "Bon Appetit"