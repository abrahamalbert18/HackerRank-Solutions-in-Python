#!/bin/python
arr = []
maxVal=-9999
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().split(' '))
    arr.append(arr_temp)

#print arr

for i in range(0,4):
    for j in range(0,4):
        firstRow = arr[i][j]+arr[i][j+1]+arr[i][j+2]
        thirdRow=  arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
        secondRow= arr[i+1][j+1]
        total=firstRow+secondRow+thirdRow
        print "total = "+ str(total)
        maxVal=max(maxVal,total)
        print "maxVal= "+ str(maxVal)

print maxVal

