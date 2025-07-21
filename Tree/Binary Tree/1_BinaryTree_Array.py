class BinaryTree:
    def __init__(self,size):
        self.tree = [None]* size
        self.size = size
        self.last_index = -1  # tree is empty

    def insert(self, value):
        if self.last_index + 1 >= self.size:
            print("Tree is empty!!")
            return 
        self.last_index += 1
        self.tree[self.last_index] = value

    def display(self):
        for i, val in enumerate(self.tree):
            if val is not None:
                print(f"Index {i}: {val}")

    def get_left_child(self, index):
        left_child = 2 * index + 1
        if left_child <= self.last_index:
            return self.tree[left_child]
        return None
    
    def get_right_child(self, index):
        right_child = 2 * index + 2
        if right_child <= self.last_index:
            return self.tree[right_child]
        return None

    def get_parents(self, index):
        if index == 0:
            print("Root Node has no parents!!")
            return 
        parents = (index - 1 )// 2
        return self.tree[parents]
    


def main():
    b = BinaryTree(7)
    b.insert(2)
    b.insert(3)
    b.insert(4)
    b.insert(7)
    b.insert(8)
    b.insert(None)
    b.insert(9)
    b.display()

    print(b.get_left_child(1))
    print(b.get_right_child(2))
    print(b.get_parents(4))
    
if __name__=="__main__":
    main() 