# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Stack(object):
    def __init__(self):
        self.stack=[]
        
    def push(self,element):
        self.stack.append(element)
        
    
    def pop(self):
        if len(self.stack)!=0:
            self.stack.remove(self.stack[0])       
                      
    def maxElement(self):
        if len(self.stack)!=0:
            return max(self.stack)   
'''        
    
N=input()
s=[]
for n in range(N):
    #S=Stack()
    #print S.stack
    op= raw_input().split()
    if op[0]=='1':
        print op[1]
        s.insert(0,op[1])
    if op[0]=='2':
        s.pop(s[0])
    if op[0]=='3':
        print max(s)
        
