n,k,q = raw_input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = map(int,raw_input().strip().split(' '))
#print a    
if k%n!=0:
    k=k%n
    for i in range(k):
        last=a[-1]
        a=a[:-1]
        a.insert(0,last)
    
for a0 in xrange(q):
    m = int(raw_input().strip())
    print a[m]