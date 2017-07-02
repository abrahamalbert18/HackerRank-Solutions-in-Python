# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import *
N= input()
d= OrderedDict()
for i in range(N):
    item = raw_input().split()
    itemPrice= int(item[-1])
    itemName= " ".join(item[:-1])
    if d.get(itemName):                      # .get is used to check if itemName already exists
       d[itemName] += itemPrice
    else:
       d[itemName] = itemPrice
for i in d.keys():
    print i, d[i]
