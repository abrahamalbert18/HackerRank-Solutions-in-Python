s = raw_input().strip()
n = long(raw_input().strip())
number=s.count('a')
if number==0:
    print 0
elif number==1 and len(s)==1:
    print n
else:
     #For Python2
     repeats=n/len(s) 
     #For Python3
     #repeats=n//len(s) 
     remainders=n%len(s)
     #s=s*repeats + s[:remainders]
     print str(number*repeats+s[:remainders].count('a'))       
        
        
