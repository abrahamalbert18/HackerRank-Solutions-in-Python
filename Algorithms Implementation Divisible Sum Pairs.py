n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int,raw_input().strip().split(' '))
pairs=[]
count=0
for i in range(len(a)-1):
    for j in range(1,len(a)):
        if i<j and ((a[i]+a[j]) % k ==0):
            pairs.append([a[i],a[j]])
            count+=1

#print pairs            
print count    