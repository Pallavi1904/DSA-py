class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insertion(self, root, value):
        if root is None:
            return BinarySearchTree(value)
        elif value < root.data:
            root.left = self.insertion(root.left, value)
        elif value > root.data:
            root.right = self.insertion(root.right, value)
        return root  # Always return root to maintain the structure

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=' ')
            self.inorder(root.right)
        
#         5         insert 6
#        / \
#       3   7
#      / \   \
#     2   4   8
def main():
    # leaf nodes first
    p6 = BinarySearchTree(2)
    p5 = BinarySearchTree(4)
    p7 = BinarySearchTree(8)

    # Internal Nodes
    p2 = BinarySearchTree(3)
    p2.left = p6
    p2.right = p5

    p1 = BinarySearchTree(7)
    p1.right = p7

    # Root node
    p = BinarySearchTree(5)
    p.left = p2
    p.right = p1
    
    print("Inorder traversal before insertion:")
    p.inorder(p)
    # Insert
    p = p.insertion(p, 6)
   
    print("\nInorder traversal after insertion:")
    p.inorder(p)


if __name__=="__main__":
    main()