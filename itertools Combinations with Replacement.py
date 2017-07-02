# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
s,k=raw_input().split()
for i in combinations_with_replacement(sorted(s),int(k)):
    print "".join(i)