class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data  
        self.left = left  
        self.right = right 

    

def main():
   # Create leaf nodes first
    p4 = BinaryTree(1)
    p5 = BinaryTree(3)
    p2 = BinaryTree(16)
    
    # Then internal nodes that use the above
    p1 = BinaryTree(15, p5, p4)
    p = BinaryTree(10, p1, p2)  # Root node

    # Example traversal: Inorder
    print("Inorder Traversal:")
    # inorder(p)

# def inorder(node):
#     if node:
#         inorder(node.left)
#         print(node.data, end=' ')
#         inorder(node.right)





if __name__=="__main__":
    main()


