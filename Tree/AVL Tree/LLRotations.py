class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0 # height for leaf nodes

class AVLTree:
    def find_height(self, root):
        if not root:
            return 0
        return root.height
    
    def balanced(self, root):
        if not root:
            return 0
        return self.find_height(root.right) - self.find_height(root.right)
        
    def llRotation(self, z):
        y = z.left
        t3 = y.right # None

        y.right = z
        z.left = t3

        z.height = max(self.find_height(z.right), self.find_height(z.left))
        y.height = max(self.find_height(z.right), self.find_height(z.left))

#         5         delete 3
#        / 
#       3   
#      /   
#     2     
def main():
    # leaf nodes first
    p6 = node(2)
   
    # Internal Nodes
    p2 = node(3)
    p2.left = p6

    # Root node
    p = node(5)
    p.left = p2
    
   # LL Rotation
    avl = AVLTree()
    avl.llRotation(p)
    print("If balanced factor is 0,1 and -1 then tree is balanced:")
    print(avl.balanced(p)) 

      
   
if __name__=="__main__":
    main()