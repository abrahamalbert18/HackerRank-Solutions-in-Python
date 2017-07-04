# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
expression=raw_input()
pattern="[^aeiouAEIOU]?([aeiouAEIOU]{2,})[^aeiouAEIOU]"
values=re.findall(pattern,expression)
if len(values)>0:
    for i in values:
        print i
else:
    print -1