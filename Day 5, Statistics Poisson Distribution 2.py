#Poisson Distribution
# Enter your code here. Read input from STDIN. Print output to STDOUT

meanOfA,meanOfB=map(float,raw_input().split())
Ca=160+40*(meanOfA+meanOfA**2)
Cb=128+40*(meanOfB+meanOfB**2)
print round(Ca,3)
print round(Cb,3)
