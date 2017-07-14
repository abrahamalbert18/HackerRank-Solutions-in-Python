import math
mean,sd=map(float,raw_input().split())
x,y=input(),input()

def normalDistribution(x, mean, sd):
    return round(0.5 * 100 * (1 + math.erf((x - mean)/ (sd * math.sqrt(2)))), 3)

print round(100 - normalDistribution(x, mean, sd), 2)
print round(100 - normalDistribution(y, mean, sd), 2)
print round(normalDistribution(60, 70, 10), 2)