#Day 5, Statistics Normal Distribution
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
mean,sd=map(float,raw_input().split())
x=input()
y1,y2=map(float,raw_input().split())

def normalDistribution(x,mean,sd):
    return round(0.5 * (1 + math.erf((x - mean) / (sd * (2 ** 0.5)))),3)

print normalDistribution(x,mean,sd)
print normalDistribution(y2,mean,sd)-normalDistribution(y1,mean,sd)