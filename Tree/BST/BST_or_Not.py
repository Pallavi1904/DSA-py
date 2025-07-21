class BinarySearchTree:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

    def inorder(self, root):
        if root is None:
            return []
        return self.inorder(root.left) + [root.data] + self.inorder(root.right)

    def BST_Or_Not(self, root):
        values = self.inorder(root)
        print("\nInOrder Traversal:")
        print(*values) # * iterate for all values
        if values == sorted(values):
            print("It is BST!!!")
        else:
            print("It is not BST!!")


#         5
#        / \
#       8   7
#      / \   \
#     6   4   3
def main():
    # leaf nodes first
    p6 = BinarySearchTree(6)
    p5 = BinarySearchTree(4)
    # p4 is null
    p3 = BinarySearchTree(3)

    # Internal Nodes
    p2 = BinarySearchTree(8)
    p2.left = p6
    p2.right = p5

    p1 = BinarySearchTree(7)
    p1.right = p3

    # Root node
    p = BinarySearchTree(5)
    p.left = p2
    p.right = p1


    #Inoder:  Left->Root->Right
    print("InOrder Traversal:")
    p.inorder(p)

    # BST or not 
    p.BST_Or_Not(p)

if __name__=="__main__":
    main()