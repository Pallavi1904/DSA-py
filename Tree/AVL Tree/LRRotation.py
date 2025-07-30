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
        
    def lrRotation(self, z): # z is 5
        y = z.left
        t3 = y.right 
        t4 = y.left

        temp = y #swap
        y = t3
        t3 = temp

        y.left = t3
        y.right = z

    
        z.height = max(self.find_height(z.right), self.find_height(z.left))
        y.height = max(self.find_height(z.right), self.find_height(z.left))

#      8
#     /
#    6
#     \
#      7

def main():
    # leaf nodes first
    p6 = node(7)
   
    # Internal Nodes
    p2 = node(6)
    p2.right = p6

    # Root node
    p = node(8)
    p.left = p2
    
   # RR Rotation
    avl = AVLTree()
    avl.lrRotation(p)
    print("If balanced factor is 0,1 and -1 then tree is balanced:")
    print(avl.balanced(p)) 

      
   
if __name__=="__main__":
    main()