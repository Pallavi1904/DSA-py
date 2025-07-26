class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def find_minimum(self, root):
        while root.left:
            root = root.left
        return root
    

    def deletion(self, root, value):
        if root is None:
            return None
        elif value < root.data:
            root.left = self.deletion(root.left, value)
        elif value > root.data:
            root.right = self.deletion(root.right, value)
        else:
            # Root is leaf node
            if root.left is None and root.right is None:
                print(f"Leaf node deleted: {value}")
                return None
            
            # Root with non-leaf node
            if root.left is None:
                print(f"Deleting node with only right child:{value}")
                return root.right
            elif root.right is None:
                print(f"Deleting node with only left child:{value}")
                return root.left
            
            # Root node or node with two child
            min_larger = self.find_minimum(self.right)
            root.data = min_larger.data
            root.right = self.deletion(root.right, min_larger.data)

        return root
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=' ')
            self.inorder(root.right) 

        
#         5         delete 3
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
    
    print("Before deletion")
    p.inorder(p)
    # deletion
    print("Before deletion")
    p.deletion(p,3)
    p.inorder(p)

      
   
if __name__=="__main__":
    main()