#physicsScores=map(int,raw_input().split())
#historyScores=map(int,raw_input().split())

def KarlPearsonsCoefficient(physicsScores,historyScores):
    xValues=physicsScores
    yValues=historyScores
    xSquareValues=[i**2 for i in xValues]
    ySquareValues=[i**2 for i in yValues]
    n=len(xValues)
    xyValues=[xValues[i]*yValues[i] for i in range(n)]
    numerator=(n*sum(xyValues)- sum(xValues)*sum(yValues))
    denominator=(n*sum(xSquareValues)-(sum(xValues)**2))*(n*sum(ySquareValues)-(sum(yValues)**2))
    return round(numerator/denominator**0.5,3)
    
def SlopeOfRegressionLine(independent,dependent):
    y=dependent
    x=independent    
    xMean=float(sum(x)/len(x))
    yMean=float(sum(y)/len(y))
    n=len(x)
    xStandardDeviation=((sum([(x[i]-xMean)**2 for i in range(n)])/(n-1))**0.5)
    yStandardDeviation=((sum([(y[i]-yMean)**2 for i in range(n)])/(n-1))**0.5)
    r=KarlPearsonsCoefficient(x,y)
    return round(r*(yStandardDeviation/float(xStandardDeviation)),3)
    
def InterceptOfRegressionLine(physicsScores,historyScores):
    xValues=physicsScores
    yValues=historyScores
    xSquareValues=[i**2 for i in xValues]
    #ySquareValues=[i**2 for i in yValues]
    n=len(xValues)
    xyValues=[xValues[i]*yValues[i] for i in range(n)]    
    numerator= float((sum(yValues)*sum(xSquareValues))- (sum(xValues)*sum(xyValues)))
    denominator=(n*sum(xSquareValues)-(sum(xValues))**2)
    return round(numerator/denominator,3)