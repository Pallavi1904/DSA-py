class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def Search(self,root, element):
        if root is None:
            print(f"Element {element} not in Tree!!")
            return None
        elif root.data == element:
            print(f"Element {element} found!!")
            return root
        elif root.data > element:
            return self.Search(root.left, element)
        else:
            return self.Search(root.right, element)
        
#         5
#        / \
#       3   7
#      / \  / \
#     2   4 6  8
def main():
    # leaf nodes first
    p6 = BinarySearchTree(2)
    p5 = BinarySearchTree(4)
    # p4 is null
    p3 = BinarySearchTree(6)
    p7 = BinarySearchTree(8)

    # Internal Nodes
    p2 = BinarySearchTree(3)
    p2.left = p6
    p2.right = p5

    p1 = BinarySearchTree(7)
    p1.left = p3
    p1.right = p7

    # Root node
    p = BinarySearchTree(5)
    p.left = p2
    p.right = p1
    
    # Searching 
    p.Search(p,6)
    p.Search(p,10)



if __name__=="__main__":
    main()