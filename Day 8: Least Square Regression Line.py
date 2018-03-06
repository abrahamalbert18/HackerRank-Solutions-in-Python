maths, stats = [],[]

for i in range(5):
    m, s= map(int,raw_input().split())
    maths.append(m)
    stats.append(s)

def b_value(x,y):
    n = len(x)
    xy =[x[i]*y[i] for i in range(n) ]
    x_square = [i**2 for i in x]
    # y_square = [i**2 for i in y]
    
    b = (n*(sum(xy))-((sum(x)*sum(y))))/float(((n*sum(x_square))-sum(x)**2))
    return b
    
def ab_values(x,y):
    x_mean = sum(x)/float(len(x))    
    y_mean = sum(y)/float(len(y))
    b = b_value(x,y)
    a = y_mean - b*x_mean
    return a,b
    
a,b = ab_values(maths,stats)
print a + b*80
