# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N= input()
emails =[]
for i in range(N):
    emails.append(raw_input())

pattern= re.compile('(^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{0,3}$)')    
print sorted(filter(pattern.match,emails))    

    


   