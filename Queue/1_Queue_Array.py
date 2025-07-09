class Queue:
    def __init__(self,max_size=0):
        self.max_size = max_size
        self.queue = []
    
    def isEmpty(self):
        if len(self.queue) == 0:
            return True

    def isFull(self):
        if len(self.queue) == self.max_size:
            return True    
    
    def Enqueue(self,data):
        if self.isFull():
            return "Queue is Full"
        self.queue.append(data) #Append directly append at last node
        return True
    
    def Dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.queue.pop(0)  # delete from front

    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.queue[0]
    
    def display(self):
        print(self.queue)
        
    

def main():
    q = Queue(6)
    q.Enqueue(10)
    q.Enqueue(20)
    q.Enqueue(30)
    q.Enqueue(40)
    q.display()

    q.Dequeue()
    q.display()

    print(q.peek())
    


if __name__ == "__main__":
    main()    
        

        