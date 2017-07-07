num=input()
x=map(int,raw_input().split())
f=map(int,raw_input().split())
data=[]

for i in range(num):
    data+=[x[i]]*f[i]
        
def median(values):
    n=len(values)
    if n%2==1:
        return sorted(values)[(n+1)/2 - 1]
    else:
        return round(sum(sorted(values)[(n/2)-1:(n/2)+1])/2.0,1)
    
def quartiles(values):
    n=len(values)
    values.sort()
    Q2=median(values)
    Q1=median(values[:n/2])
    
    if n%2==0:
        Q3=median(values[n/2:]) 
    else:
        Q3=median(values[n/2+1:])
                               
    return Q1,Q2,Q3
        
Q1,Q2,Q3=quartiles(data)
print round(float(Q3-Q1),1)        
    