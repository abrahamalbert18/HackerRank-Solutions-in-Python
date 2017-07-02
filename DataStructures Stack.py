# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
class Stack(object):
    def __init__(self):
        self.stack=[]
        self.maximum=-99999999
    
    def push(self,element):
        self.stack.append(element)
        if element>self.maximum:
            self.maximum=element
        
    def pop(self):
        if len(self.stack)!=0:
            self.stack.remove(self.stack[-1])
            self.maximum=max(self.stack)
        else:
            self.maximum=-99999999    
        
    def maximum(self):
        return self.maximum
            
s=Stack()            
for i in range(n):
    command=map(int,raw_input().split())
    if command[0]==1:
        s.push(command[1])
    
    elif command[0]==2:
        s.pop()
     
    elif command[0]==3:
        print s.maximum()
        
    