n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
length=min(arr)
while len(arr)!=0:
    print len(arr)
    length=min(arr)
    #print "length="+ str(length)
    arr=[i-length for i in arr if (i-length)!=0]
    #print arr
    
    
