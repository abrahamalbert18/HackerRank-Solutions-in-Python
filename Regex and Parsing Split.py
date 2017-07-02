# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
expression=r"[,|.]*"
for i in re.split(expression,raw_input().strip()):
    if i!='':
        print i
