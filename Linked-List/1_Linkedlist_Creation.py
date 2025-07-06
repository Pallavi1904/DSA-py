class Node:
    def __init__(self,data,next=None):
        self.data = data 
        self.next = next

# Creation 
def create_list(head,next):
    return Node(head,next)

# Traversal
def Traversal(a):
    while a:
        print(a.data,end="->")
        a = a.next
    print("None")

# Insertion done in main function itself
def main():
    c = create_list(30,None)
    b = create_list(20,c)
    a = create_list(10,b)

    Traversal(a)
    
    




if __name__ == "__main__":
    main()