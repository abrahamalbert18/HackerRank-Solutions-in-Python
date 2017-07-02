# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
expression=r"[^aeiouAEIOU]([aeiouAEIOU]{2,})[^aeiouAEIOU]"
result=re.findall(expression,raw_input())
if len(result)!=0:
    for i in result:
        print i
else:
    print -1