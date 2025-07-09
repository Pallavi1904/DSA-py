class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue =  [None]*capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def isEmpty(self):
        if self.size == 0:
            return True
    def isFull(self):
        if self.size == self.capacity:
            return True
    
    def Enqueue(self,data):
        if self.isFull():
            return "Queue is Full"
        self.rear = (self.rear+1) % self.capacity
        self.queue[self.rear] = data
        self.size += 1

    def Dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        remove = self.queue[self.front]
        self.front  = (self.front + 1) % self.capacity
        self.size -= 1 
        return remove

    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.queue[0]
    
    def display(self):
        print("Queue Elements: ")
        index = self.front
        for i in range(self.size):
            print(f"{self.queue[index]} ->")
            index = (index + 1) % self.capacity

def main():
    q = CircularQueue(5)
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

