# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N= input()
for i in range(N):
    ans=True
    try:
        reg= re.compile(raw_input())
    except re.error:
        ans= False
    print ans    