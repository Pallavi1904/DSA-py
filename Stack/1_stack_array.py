class stack:
    def __init__(self,max_size):
        self.stack = []
        self.max_size = max_size
    
    # IsEmpty function
    def isEmpty(self):
        if len(self.stack) == 0:
            return 0
    
    #TsFull function
    def isFull(self):
        if len(self.stack) == self.max_size:
            return 1
    
    # Push function
    def push(self,item):
        if self.isFull():
            print("Stack is Overflow")
            return 
        
        self.stack.append(item)
        print(f"pushed {item} into stack")
    
    # Pop function
    def pop(self):
        if self.isEmpty():
            print("Stack is underflow")
            return None
        
        return self.stack.pop()
    
    #peak function
    def peak(self,pos):
        if self.isEmpty():
            print("Stack is underflow")
            return None
        
        return self.stack[pos]
    
    # Display function
    def display(self):
        for i in range(len(self.stack)):
            print(self.stack[i])
        print("***********************")    

    

def main():
    stack1 = stack(8)
    stack1.push(5)
    stack1.push(12)
    stack1.push(10)
    stack1.push(13)
    stack1.push(50)
    stack1.push(14)
    stack1.push(17)
    stack1.display()

    stack1.pop()
    stack1.display()

    c = stack1.peak(2)
    print(c)


if __name__=="__main__":
    main()