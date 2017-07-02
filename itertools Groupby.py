# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import *
s=raw_input()
char= [int(i) for i,j in groupby(s)]
count= [len(list(j)) for i,j in groupby(s)]

for i in range(len(char)):
    print (count[i], char[i]),
