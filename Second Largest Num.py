# Enter your code here. Read input from STDIN. Print output to STDOUT
N= input()
L= raw_input().split()
I=[]
assert N>=2 and N<=10
#print type(L[0])
for i in L:
    I.append(int(i))
I.sort()
#print L
largest=max(I)
#print "Large=" + str(largest)
count=I.count(largest)
for i in range(count):
    I.remove(largest)
print max(I)


        

5
-7 -7 -7 -7 -6
