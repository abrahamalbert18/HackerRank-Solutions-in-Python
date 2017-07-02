from collections import *
n=input()
array=map(int,raw_input().split())
values=Counter(array)

print str(len(array)-max(values.viewvalues())) 