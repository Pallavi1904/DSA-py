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


    # Deletion at beginning
def deletion_at_beginning(head):
    if head is None:
        print("List is empty")
        return head
    temp = head
    head = head.next
    del temp
    return head


# Deletion at end
def deletion_at_end(head):
    # if list is empty
    if head is None:
        print("List is empty")
        return head
    
    # if only one node exist
    if head.next is None:
        del head
        return None
    
    #If more than one node exist
    temp = head
    while temp.next.next is not None:
        temp = temp.next
    
    del temp.next
    temp.next = None
    return head

# Deletion at position
def deletion_at_position(head,pos):
    if(pos == 0):
        temp = head
        head = head.next
        del temp
        return head
    
    temp =head
    i = 0
    # Traverse to the node before the one to delete
    while temp is not None and i < pos-1:
        temp = temp.next
        i += 1
    
    # Check if position is invalid
    if temp is None or temp.next is None:
        print("Position out of range")
        return head

    # Delete node at position 
    node_to_delete = temp.next
    temp.next = node_to_delete.next
    del node_to_delete
    return head




        

 

def main():
    d = create_list(27,None)
    c = create_list(20,d)
    b = create_list(34,c)
    head = create_list(2,b)
    Traversal(head)

    head = deletion_at_beginning(head)
    Traversal(head)

    deletion_at_end(head)
    Traversal(head)

    deletion_at_position(head, 1)
    Traversal(head)





if __name__ == "__main__":
    main()