n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))
position=0
jumps=0
while position!=len(c)-1:
    print position
    if (position+2) <= (len(c)-1) and c[position+2]!=1:
        jumps+=1
        position+=2
    else:
        jumps+=1
        position+=1
print jumps        
        
