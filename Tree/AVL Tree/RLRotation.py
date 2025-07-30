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
        
    def rlRotation(self, z): # z is 5
        y = z.right
        t3 = y.left 
        t4 = y.right

        temp = y #swap
        y = t3
        t3 = temp
        
        
        y.left = z
        z.left = t4
    

        z.height = max(self.find_height(z.right), self.find_height(z.left))
        y.height = max(self.find_height(z.right), self.find_height(z.left))

#         5         
#          \          5
#           9        / (before)
#          /        7
#         7 
def main():
    # leaf nodes first
    p6 = node(7)
   
    # Internal Nodes
    p2 = node(9)
    p2.left = p6

    # Root node
    p = node(5)
    p.right = p2
    
   # RR Rotation
    avl = AVLTree()
    avl.rlRotation(p)
    print("If balanced factor is 0,1 and -1 then tree is balanced:")
    print(avl.balanced(p)) 

      
   
if __name__=="__main__":
    main()