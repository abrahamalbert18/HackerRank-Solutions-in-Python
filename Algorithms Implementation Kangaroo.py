x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

if v1>v2:
    posDiff=x2-x1 
    velDiff=v1-v2
    if posDiff%velDiff ==0:
        print "YES"
    else:
        print "NO"    
else:
    print "NO"    
    