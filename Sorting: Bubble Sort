n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

count = 0
for i in range(len(a)):
    for j in range(len(a)-1):
        #Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]):
            s = a[j]
            a[j] = a[j+1]
            a[j + 1] = s
            count += 1
print "Array is sorted in",str(count),"swaps."
print "First Element:",a[0]
print "Last Element:",a[-1]
    
