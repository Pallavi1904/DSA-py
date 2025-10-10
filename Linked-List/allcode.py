class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def createNode(head,next):
    return Node(head,next)

def show(head):
    while head:
        print(head.data,end="->")
        head = head.next
    print("None")

def insertAtStart(data,head):
    new_node = Node(data)
    new_node.next = head
    return new_node

def insertAtEnd(data,last):
    new = Node(data)
    last.next = new
    new.next = None

def insertAtPosition(data,pos,head):
    new = Node(data)
    if pos == 0:
        new.next = head
        return new
    temp = head
    count = 0

    while temp is not None and count < pos-1:
        temp = temp.next
        count +=1
    
    if temp is None:
        print("Position oout of range")
        return head
    
    new.next = temp.next
    temp.next = new
    return head

def deletion_at_begin(head):
    if head is None:
        print("List is empty")
        return head
    temp = head
    head = head.next
    del temp
    return head

def delete_at_end(head):
    if head is None:
        print("List is empty")
        return head
    
    if head.next is None:
        del head
        return head
    
    temp = head
    while temp.next.next is not None:
        temp = temp.next

    del temp.next
    temp.next = None
    return head

def delete_at_position(head,pos):
    if pos == 0:
        temp = head
        head = head.next
        del temp
        return head
    
    temp = head
    count = 0

    while temp is not None and count < pos-1:
        temp = temp.next
        count += 1
    
    if temp is None or temp.next is None:
        print("Invalid position")
        return 
    
    delete_node = temp.next
    temp.next = delete_node.next
    del delete_node
    return head




def main():
    e =createNode(60,None)
    d = createNode(50,e)
    c = createNode(40,d)
    a = createNode(30,c)
    b = createNode(20,a)
    head = createNode(10,b)
    show(head)

    head = deletion_at_begin(head)
    show(head)

    delete_at_end(head)
    show(head)

    head = delete_at_position(head, 2)
    show(head)
    

if __name__ == "__main__":
    main()