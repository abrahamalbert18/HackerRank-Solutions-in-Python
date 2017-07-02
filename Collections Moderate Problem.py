# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import *
N= input()
d= OrderedDict()
words= [raw_input() for i in range(N)]
counter= Counter(words)
print len(counter)
for i in words:
     d[i]= counter[i]
print " ".join(map(str,d.values()))
    