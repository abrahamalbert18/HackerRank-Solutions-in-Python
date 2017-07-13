#Poisson Distribution 
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
mean,k=input(),input()
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def poissonDistribution(mean,k):
    temp=((mean**k)*(math.e **(-mean)))/factorial(k)
    return temp
pd=poissonDistribution(mean,k)
print round(pd,3)