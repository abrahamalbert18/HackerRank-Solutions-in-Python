# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
maxWeight,n,mean,sd=input(),input(),input(),input()
def centralLimitTheorem(maxWeight,n,mean,sd):
    newMean=n*mean
    newSd=(n**0.5)*sd     
    return round(0.5 * (1 + math.erf((maxWeight - newMean) / (newSd * (2 ** 0.5)))),4)

print centralLimitTheorem(maxWeight,n,mean,sd)