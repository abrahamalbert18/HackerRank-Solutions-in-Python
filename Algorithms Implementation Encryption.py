import math
s=raw_input()
code=s[:]
l=len(s)
columns=int(math.ceil(l**(0.5)))
rows=int(columns)-1
if rows*columns<l:
    rows=columns
    
grid=[]
for i in range(rows):
    grid.append(code[:columns])
    code=code[columns:]

encrypted=''
for i in range(columns):
    for j in range(rows):
        if i<len(grid[j]):
            encrypted+=grid[j][i]
    encrypted+=" "    

print encrypted   
                
