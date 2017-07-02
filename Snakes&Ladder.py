# Enter your code here. Read input from STDIN. Print output to STDOUT
T=input()
def gamePlay(dice,position,ladders,snakes):
    ladders.sort()
    snakes.sort()
    ladderLow=[ladders[i][0] for i in range(len(ladders))]
    snakesHead=[snakes[i][0] for i in range(len(snakes))]
    count=0
    while (position<=98):
        roll=max(dice)
        position+=roll
        if position in snakesHead and roll!=1:
            roll-=1
        if position in snakesHead and roll==1:
            position = snakes[snakesHead.index(position)][1]   
            
        
        if position in ladderLow:
            position= ladders[ladderLow.index(position)][1]
        count+=1    
        print snakesHead
        print ladderLow
        print "count ="+str(count) 
        print "position="+str(position)   
    print "position="+str(position)    
    return count    
    
for testCase in range(T):
    N=input()
    ladders=[raw_input().split() for n in range(N)]
    M=input()
    snakes=[raw_input().split() for m in range(M)]
    position=1
    dice=[1,2,3,4,5,6]
    #Select the higher number
    #Check if there's a snake head
    #if there's a snake head go for the next highest number
    #if there's no snake head go for another roll and make a count of the step.
    #if there's a ladder bottom in the position, change the position and make a count
    #make sure the position reaches till 98.
    #steps=0
    maxCount=gamePlay(dice,position,ladders,snakes)
    print maxCount
    

            
        
        
        
    
    
