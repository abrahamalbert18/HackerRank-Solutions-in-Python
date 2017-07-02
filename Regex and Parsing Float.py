# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=input()
for number in range(n):
    expression=r'^[+|-]?[0-9]*\.[0-9]+$'
    print bool(re.match(expression,raw_input()))