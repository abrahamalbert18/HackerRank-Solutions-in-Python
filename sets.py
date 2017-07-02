numOfEng= raw_input()
rollOfEng=set(raw_input().split())
numOfFre= raw_input()
rollOfFre=set(raw_input().split())

total= numOfEng+numOfFre

studentsTakingPaper= list(rollOfEng.union(rollOfFre)) #converting set into list
print len(studentsTakingPaper)

