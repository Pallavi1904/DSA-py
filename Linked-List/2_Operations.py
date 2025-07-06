class Node:
    def __init__(self,data,next=None):
        self.next = next
        self.data = data
    

# Creation 
def create_list(data,next):
    return Node(data,next)

# Traversal
def Traversal(a):
    while a:
        print(a.data,end="->")
        a = a.next
    print("None")

    # Insertion at beginning
def insert_at_beginning(data,head):
    new_node = Node(data)
    new_node.next = head
    return new_node
  
     # Insertion at end
def insert_at_end(data,last):
    new_node = Node(data)
    last.next = new_node
    new_node.next = None

def insert_at_position(data,pos,head):
    new_node = Node(data)
    if(pos == 0):
        new_node.next = head
        return new_node
    
    temp = head
    count = 0
    
    # Traverse until you reach the node just before the desired position.
    while temp is not None and count < pos-1:
        temp = temp.next
        count += 1
    
    # Check if the position is valid (temp must not be None).
    if temp is None:
        print("Position out of range")
        return head
        
    new_node.next = temp.next
    temp.next = new_node
    return head

def main():
    d = create_list(27,None)
    c = create_list(20,d)
    b = create_list(34,c)
    head = create_list(2,b)
    Traversal(head)

    head = insert_at_beginning(23,head)
    Traversal(head)

    insert_at_end(30,d)
    Traversal(head)

    head = insert_at_position(30000,5,head)
    Traversal(head)






if __name__ == "__main__":
    main()