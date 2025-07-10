class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.rear = None 
        self.front = None

    def isEmpty(self):  # Not needed but still
        if self.front is None:
            return True
    
    def Enqueue(self, value): 
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    
    def Dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return
        removed = self.front
        self.front = self.front.next
        return removed.data
    
    def display(self):
        temp = self.front
        while temp:
            print(f"{temp.data} ->")
            temp = temp.next
        print("None")


def main():
    q = Queue()
    q.Enqueue(10)
    q.Enqueue(20)
    q.Enqueue(30)
    q.display()

    q.Dequeue()
    q.display()
    
    
    

if __name__=="__main__":
    main()
