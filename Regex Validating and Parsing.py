# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n=input()
for i in range(n):
    line=raw_input()
    name,email=line.split(' ')
    pattern="<[a-z][a-zA-Z0-9\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>"
    if bool(re.match(pattern,email)):
        print name,email
        