#Day 4, Geometric Distribution at a particular position
# Enter your code here. Read input from STDIN. Print output to STDOUT
numerator,denominator=map(float,raw_input().split())
n=input()
p=numerator/denominator
q=1-p
gd= (q**(n-1))*p           #geometric distribution
print round(gd,3)
