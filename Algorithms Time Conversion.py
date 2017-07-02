time = raw_input().strip()

railTime=""
if time[-2:]=="PM" and time[:2]!='12':
    railTime=str(int(time[:2])+12)
if time[-2:]=="PM" and time[:2]=='12': 
    railTime+=time[:2]
if time[-2:]=="AM" and time[:2]=="12":
    railTime="00"
if time[-2:]=="AM" and time[:2]!="12":   
    railTime+=time[:2]
print railTime+time[2:-2]    