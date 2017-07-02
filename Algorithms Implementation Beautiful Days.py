# Enter your code here. Read input from STDIN. Print output to STDOUT
vals=raw_input().split()
i,j,k=vals[0],vals[1],int(vals[2])
def beautiful(day,k):
    if ( int(day)- int(day[::-1]) ) % k == 0:
        return True
    else:
        return False
count=0
for days in range(int(i),int(j)+1):
    #print days, type(days)
    
    if beautiful(str(days),k)==True:
        count+=1
print count        
    
