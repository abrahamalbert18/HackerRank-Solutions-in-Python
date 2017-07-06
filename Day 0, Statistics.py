#day 0, Statistics (Mean, Median, Mode)
from collections import *
n= input()
vals= map(int,raw_input().split())
total=0
modeVals=Counter(vals)
maxVal=max(modeVals.values())
modes=[]
for i in modeVals.keys():
    if modeVals[i]==maxVal:
        modes.append(i)
                        
mean=round(sum(vals)/float(n),1)

if n%2==1:
    median=sorted(vals)[(n+1)/2 - 1]
    
else:
    median=sum(sorted(vals)[(n/2)-1:(n/2)+1])/2.0
                    
if len(modes)==1: 
    mode= modes[0]
    
else:
    mode=min(modes)
    
print str(mean)+'\n'+str(median)+'\n'+str(mode)                                            