t = int(raw_input().strip())
for a0 in xrange(t):
    n = raw_input().strip()
    
    count=0
    for digit in n:
        if int(digit)!=0:
            if (int(n) % int(digit)) == 0:
                count+=1
    print count        