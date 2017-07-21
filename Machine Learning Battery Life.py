# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here
import pylab, sys
dataFile=open('Battery.txt')
batteryCharged=[]
batteryLasted=[]
for i in dataFile:
    i=i.split(',')
    batteryCharged.append(float(i[0]))
    batteryLasted.append(float(i[1]))
pylab.plot(batteryCharged,batteryLasted,'ro')
pylab.show()    
bC=pylab.array(batteryCharged)
bL=pylab.array(batteryLasted)
a,b=pylab.polyfit(bC,bL,1)
a,b=round(a,2) , round(b,2)
#print a,b


data = float(sys.stdin.readline())

# Enter your code here
if data>0 and data<=4:
    print round(data*2,2)
else:
    print 8.00  

  
