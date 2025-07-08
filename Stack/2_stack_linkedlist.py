class Node:
    def __init__(self,data= None):
        self.data = data
        self.next = None

class stack:
    def __init__(self,max_size=None): # Max_size is maximum size of elements
        self.max_size = max_size
        self.size = 0 # Size of elements being pushed
        self.top = None 
        self.num = sum # as showing error thus

    def isEmpty(self):
        if(self.top == None):
            return 0
        
    def isFull(self):
        if self.max_size is None:
            return 1
        

    def Traversal(self):
        temp = self.top
        if temp is None:
            print("Stack is empty")
            return

        print("Stack (top to bottom):")
        while temp:
            print(temp.data)
            temp = temp.next

        
    def push(self,num):
        if self.isFull():
            print("Stack is overflow!! cannot push")
            return
        new_node = Node(num)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        print(f"{num} pushed!")
    
    def pop(self):
        if self.isEmpty():
            print("Stack is underflow!, cannot remove")
            return
        popped = self.top.data
        self.top = self.top.next 
        self.size -= 1
        print(f"popped!!")
        return popped
    
    def peak(self,pos):
        temp = self.top
        index = 0
        while temp:
            if index == pos:
                print(temp.data)
                return temp.data
            temp = temp.next
            index += 1
        

def main():
    stack1 = stack(4)
    stack1.push(10)
    stack1.push(11)
    stack1.push(12)
    stack1.push(13) # Top

    stack1.Traversal()

    stack1.pop()
    stack1.Traversal()

    stack1.peak(0)

if __name__ == "__main__":
    main()


