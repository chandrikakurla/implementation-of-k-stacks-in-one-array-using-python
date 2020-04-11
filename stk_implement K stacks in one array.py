class kstacks:
    def __init__(self,k,n):
        #total no.of stacks
        self.k=k
        #size of array holding k stacks
        self.n=n
        self.free=0
        self.arr=[0]*self.n
        self.top=[-1]*self.k
        self.next = [i + 1 for i in range(self.n)] 
        self.next[self.n - 1] = -1
    def isEmpty(self,stack_no):
        return self.top[stack_no]==-1
    def isFull(self):
        return self.free==-1
    def push(self,data,stack_no):
        if self.isFull():
            print("stack is full")
            return
        insert_at=self.free
        self.free=self.next[self.free]
        self.arr[insert_at]=data
        self.next[insert_at]=self.top[stack_no]
        self.top[stack_no]=insert_at
    def pop(self,stack_no):
        if self.top[stack_no]==-1:
            print("stack underflow")
            return
        top_stack=self.top[stack_no]
        self.top[stack_no]=self.next[top_stack]
        self.next[top_stack]=self.free
        self.free=top_stack
        return self.arr[top_stack]
    def print_stack(self,stack_no):
        top=self.top[stack_no]
        while(top!=-1):
            print(self.arr[top])
            top=self.next[top]
if __name__ == "__main__": 
      
    # Create 3 stacks using an  
    # array of size 10. 
    stacks = kstacks(3, 10) 
    stacks.push(13,1)
    stacks.push(2,2)
    stacks.push(10,0)
    stacks.push(9,0)
    stacks.push(1,2)
    stacks.push(12,1)
    print("Popped element from stack 2 is " + str(stacks.pop(2))) 
    print("Popped element from stack 1 is " + str(stacks.pop(1))) 
    print("Popped element from stack 0 is " + str(stacks.pop(0))) 
    print("Popped element from stack 0 is " + str(stacks.pop(0))) 
    stacks.print_stack(0) 
  
