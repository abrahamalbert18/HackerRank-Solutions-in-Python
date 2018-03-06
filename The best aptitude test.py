# Enter your code here. Read input from STDIN. Print output to STDOUT
def mean(x):
    return round(sum(x)/float(n),1)

def standardDeviation(values,mean):
    data=[(val-mean)**2 for val in values]
    return (sum(data)/float(len(data)))**0.5


def pearsonCorrelationCoefficient(x,y):
    xMean=mean(x)
    yMean=mean(y)
    xStd=standardDeviation(x,xMean)
    yStd=standardDeviation(y,yMean)
    numerator = sum( (x[i]-xMean)*(y[i]-yMean) for i in range(n))
    denominator = n*xStd*yStd
    if denominator == 0:
        return 0
    else:
        return round((numerator/denominator),3)

t = input()
for testcase in range(t):
    n = input()
    gpa = map(float, raw_input().split())
    testScores = []

    for i in range(5):
        testScores.append(map(float, raw_input().split()))

    correlationCoefficient = []

    for i in testScores:
        correlationCoefficient.append(pearsonCorrelationCoefficient(i,gpa))

    sol = correlationCoefficient.index(max(correlationCoefficient))+1
    print sol
