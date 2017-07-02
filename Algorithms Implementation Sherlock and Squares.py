# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
t=input()
for testCase in range(t):
    count=0
    numbers=map(int,raw_input().split())
    lowerLimit=numbers[0]**(0.5)
    upperLimit=numbers[1]**(0.5)
    num=math.ceil(lowerLimit)
    while ( num>=lowerLimit and num<=upperLimit):
        if num**2 >= numbers[0] and num**2 <=numbers[1]:
            count+=1
           # print num**2
        num+=1
    print count    
    
        
        