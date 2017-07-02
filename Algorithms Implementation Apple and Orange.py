s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))
apples=oranges=0
for i in apple:
    if (a+i)>=s and (a+i)<=t:
        apples+=1
print apples
for j in orange:
    if (b+j)>=s and (b+j)<=t:
        oranges+=1
print oranges        
