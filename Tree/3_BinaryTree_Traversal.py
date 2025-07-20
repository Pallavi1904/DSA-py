class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=' ')
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data ,end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=' ')

#         5
#        / \
#       8   7
#      / \   \
#     6   4   3

def main():
    # leaf nodes first
    p6 = BinaryTree(6)
    p5 = BinaryTree(4)
    # p4 is null
    p3 = BinaryTree(3)

    # Internal Nodes
    p2 = BinaryTree(8)
    p2.left = p6
    p2.right = p5

    p1 = BinaryTree(7)
    p1.right = p3

    # Root node
    p = BinaryTree(5)
    p.left = p2
    p.right = p1


    #Inoder:  Left->Root->Right
    print("InOrder Traversal:")
    p.inorder(p)

    #Preorder:  Root->Left->Right
    print("\nPreOrder Traversal:")
    p.preorder(p)

    #Postorder:  Left->Right->Root
    print("\nPostOrder Traversal:")
    p.postorder(p)

if __name__=="__main__":
    main()