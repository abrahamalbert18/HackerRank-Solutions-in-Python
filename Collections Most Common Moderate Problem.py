# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import *
s= raw_input()
string= [i for i in s]
counter= Counter(string)
string= sorted(set(string))
for i in range(3):
    for j in string:
        if counter[j]== max(counter.values()):
            print j+" "+ str(max(counter.values()))
            counter.pop(j) 
            break
            print counter
        
