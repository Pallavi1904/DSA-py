def precedence(op):
    if op == '+' or op =='-':
        return 1
    if op == '/' or op == '*' or op == '%':
        return 2
    return 0
   
def Infix_to_postfix(exp):
    stack = []
    result = ''

    for char in exp:
        if char.isalnum(): # for (A, V, B, 1, 2, 3)
            result += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        
        else:
            while stack and precedence(stack[-1]) >= precedence(char):
                result += stack.pop()
            
            stack.append(char)

    while stack:
        result += stack.pop()
    
    return result

def main():
    exp = 'x+y*z-r'
    print(Infix_to_postfix(exp))
    
    

if __name__=="__main__":
    main()