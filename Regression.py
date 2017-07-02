import pylab

vals=map(int,raw_input().split())
f,n=vals[0],vals[1]
data=[]
factors=[]
R=[]
pricePerSqFeet=[]
results=[]


for observations in range(n):
    data.append(map(float,raw_input().split()))
    pricePerSqFeet.append(data[observations][-1])
    
    result=1
    for factor in range(f):
        result*=data[observations][factor]
    factors.append(result)    

def problemSolving(xValue):
    bestFit=R.index(max(R))
    if (bestFit+1)==1:
        ans=fit1(factors,pricePerSqFeet)
        print ans[0]*xValue+ans[1]
        
    elif (bestFit+1)==2:
        ans=fit2(factors,pricePerSqFeet)
        print ans[0]*(xValue**2)+ans[1]*xValue+ans[2]
        
    elif (bestFit+1)==3:
        ans=fit3(factors,pricePerSqFeet)    
        print ans[0]*(xValue**3)+ans[1]*(xValue**2)+ans[2]*xValue+ans[3]
    return

    
        
#print factors,pricePerSqFeet,data            

def rSquare(measured, estimated):
    SEE = ((estimated - measured)**2).sum()
    mMean = sum(measured)/float(len(measured))
    MV = sum(((mMean - measured)**2))
    return 1 - SEE/MV
    
def fit1(factors,pricePerSqFeet):
    xVals,yVals=pylab.array(factors), pylab.array(pricePerSqFeet)    
    a,b=pylab.polyfit(xVals,yVals,1)
    estVals=a*xVals+b
    results=[]
    results.append(a)
    results.append(b)
    R.append(rSquare(factors,estVals))
    return results
    
def fit2(factors,pricePerSqFeet):
    xVals,yVals=pylab.array(factors), pylab.array(pricePerSqFeet)    
    a,b,c=pylab.polyfit(xVals,yVals,2)
    estVals=a*(xVals**2)+b*xVals+c
    results=[]
    results.append(a)
    results.append(b)
    results.append(c)
    R.append(rSquare(factors,estVals))
    return results    

def fit3(factors,pricePerSqFeet):
    xVals,yVals=pylab.array(factors), pylab.array(pricePerSqFeet)    
    a,b,c,d=pylab.polyfit(xVals,yVals,3)
    estVals=a*(xVals**3)+b*(xVals**2)+c*xVals+d
    results=[]
    results.append(a)
    results.append(b)
    results.append(c)
    results.append(d)
    R.append(rSquare(factors,estVals))
    return results           

fit1(factors,pricePerSqFeet)
fit2(factors,pricePerSqFeet)
fit3(factors,pricePerSqFeet)

newFactors=[]        
t=input()
for testCase in range(t):
    newFactors.append(map(float,raw_input().split()))
    result=1
    for factor in range(f):
        result*=newFactors[testCase][factor]   
    
    problemSolving(result)
