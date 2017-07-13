#Day 4, Geometric Distribution during few inspections
#Enter your code here. Read input from STDIN. Print output to STDOUT
numerator,denominator=map(float,raw_input().split())
n=input()
p=numerator/denominator
q=1-p
gd=0
for i in range(1,n+1):
    gd+= (q**(n-i))*p           #geometric distribution
    
print round(gd,3)
