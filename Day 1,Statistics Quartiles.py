n= input()
vals= map(int,raw_input().split())

def median(values):
    n=len(values)
    print "values=",values
    if n%2==1:
        return sorted(values)[(n+1)/2 - 1]
    else:
        return sum(sorted(values)[(n/2)-1:(n/2)+1])/2
    
def quartiles(values):
    n=len(values)
    values.sort()
    Q2=median(values)
    Q1=median(values[:n/2])
    print "values=",values
    if n%2==0:
        print "values=",values[n/2:]
        Q3=median(values[n/2:]) 
    else:
        print "values=",values[n/2+1:]
        Q3=median(values[n/2+1:])
                               
    return Q1,Q2,Q3
    
Q1,Q2,Q3=quartiles(vals)
print str(Q1)+"\n"+str(Q2)+"\n"+str(Q3)     