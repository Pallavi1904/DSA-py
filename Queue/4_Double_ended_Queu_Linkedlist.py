class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def InsertFront(self, data):
        new_node = Node(data)
        if self.front is None:
            self.front = self.rear = new_node
        else:
            self.front = self.front.next
            self.front = new_node
    
    def insertRear(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node

    def deleteFront(self):
        if self.front is None:
            print("Queue is Empty")
            return 
        removed = self.front.data
        self.front = self.front.next

        if self.front is not None:
            self.front.prev = None
        else:
            self.rear = None
        return removed
    
    def deleteRear(self):
        if self.rear is None:
            print("Queue is Empty")
            return
        removed = self.rear.data
        self.rear = self.rear.prev 
        self.rear.next = None
        return removed
    
    def display(self):
        temp = self.front
        while temp:
            print(f"{temp.data} ->")
            temp = temp.next
        print("None")

def main():
    q = Queue()
    q.InsertFront(10)
    q.display()

    q.insertRear(20)
    q.display()

    q.deleteRear()
    q.display()

    q.deleteFront()
    q.display()
    
    
    

if __name__=="__main__":
    main()
