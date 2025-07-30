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
        
    def rrRotation(self, z): # z is 5
        y = z.right
        t3 = y.left # None

        y.left = z
        z.right = t3

        z.height = max(self.find_height(z.right), self.find_height(z.left))
        y.height = max(self.find_height(z.right), self.find_height(z.left))

#         5         
#          \         
#           9          
#            \
#             11
def main():
    # leaf nodes first
    p6 = node(11)
   
    # Internal Nodes
    p2 = node(9)
    p2.right = p6

    # Root node
    p = node(5)
    p.right = p2
    
   # RR Rotation
    avl = AVLTree()
    avl.rrRotation(p)
    print("If balanced factor is 0,1 and -1 then tree is balanced:")
    print(avl.balanced(p)) 

      
   
if __name__=="__main__":
    main()