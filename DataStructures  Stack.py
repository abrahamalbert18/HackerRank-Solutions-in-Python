# Enter your code here. Read input from STDIN. Print output to STDOUT
class Stack(object):
    def __init__(self):
        self.stack=[]
        self.maximum=-999999
       
    def push(self,element):
        self.stack.append(element)
        
    
    def pop(self):
        if len(self.stack)!=0:
            if self.stack[0]==self.maximum:
                self.maximum=max()
                
            self.stack.remove(self.stack[0])       
                      
    def maxElement(self):
        if len(self.stack)!=0:
            return max(self.stack)   
      
    def problem(self,N):
        for n in range(N):
            op= raw_input().split()
            if op[0]=='1':
                if op[1]> self.maximum:
                    self.maximum=op[1]   
                self.stack.insert(0,op[1])

            if op[0]=='2':
                if len(self.stack)!=0:
                    top=self.stack[0]
                    self.stack.remove(top)
                    if self.maximum==top and len(self.stack)!=0:
                        self.maximum=max(self.stack)
                    if self.maximum==top and len(self.stack)==0:
                        self.maximum=-999999
                    

            if op[0]=='3':
                print self.maximum

S=Stack()    
N=input()
S.problem(N)
