class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class stack:
    def __init__(self, max_size=None):
        self.max_size = max_size
        self.size = 0
        self.top = None

    def isEmpty(self):
        return self.top is None

    def isFull(self):
        if self.max_size is None:
            return False
        return self.size >= self.max_size

    def Traversal(self):
        temp = self.top
        if temp is None:
            print("Stack is empty")
            return
        print("Stack (top to bottom):")
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, num):
        if self.isFull():
            print("Stack is overflow!! cannot push")
            return
        new_node = Node(num)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return None  # return None instead of raising error
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def peek(self, pos):
        temp = self.top
        index = 0
        while temp:
            if index == pos:
                print(temp.data)
                return temp.data
            temp = temp.next
            index += 1
        return None

def parenthesis(open_, close_):
    return (open_ == '[' and close_ == ']') \
        or (open_ == '(' and close_ == ')') \
        or (open_ == '{' and close_ == '}')

def parentheses_matching(expression):
    st = stack(50)
    for idx, char in enumerate(expression): # Understand this
        if char in '([{':
            st.push(char)
        elif char in ')]}':
            if st.isEmpty():
                print(f"Error at index {idx}: unmatched closing '{char}'")
                return False
            top = st.pop()

    if st.isEmpty():
        print("Parenthesis are balanced")
        return True
    else:
        print("Parenthesis are not balanced")
        return False
        

def main():
    exp = '(2+3)+23+{10+3}*[10%2]'
    exp1 = '[(10*9)%2+{1+2}'
    exp2 = '[[[[[[[[[[[[(]]]]]]]]]]]]'
    exp3 = '[[[[[[[[[[[[()]]]]]]]]]]]]'
    print("Checking:", exp)
    parentheses_matching(exp)

    print("Checking:", exp1)
    parentheses_matching(exp1)

    print("Checking:", exp2)
    parentheses_matching(exp2)

    print("Checking:", exp3)
    parentheses_matching(exp3)

if __name__ == "__main__":
    main()
