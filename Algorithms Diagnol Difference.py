n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

pDiagnol= [a[i][i] for i in range(n)]

for i in range(n):
    a[i].reverse()
    
sDiagnol= [a[i][i] for i in range(n)]    

print abs( sum(pDiagnol)- sum(sDiagnol))
        
    
