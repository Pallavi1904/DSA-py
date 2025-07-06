class Myarray:
    def __init__(self, total_size, used_size):
        self.total_size = total_size
        self.used_size = used_size
        self.ptr = [0] * total_size   

# Created ADT
def create_array(tsize, usize):
    return Myarray(tsize, usize)

# Traversal of ADT
def show(a):
    for i in range(a.used_size):
        print(a.ptr[i])
    print("...................................")

# Inserting of elements in ADT
def set_val(a):
    for i in range(a.used_size):
        n = int(input(f"Enter the element {i}: "))
        a.ptr[i] = n

# Deletion of Elements in ADT
def delete_val(a,n):
    if n < 0 or n>=a.used_size:
        print(f"The {n} is out of range")
    for i in range(n,a.used_size-1):
        a.ptr[i] = a.ptr[i+1]
    a.ptr[a.used_size-1] = 0
    a.used_size -= 1




def main():
    marks = create_array(10, 3)
    set_val(marks)
    show(marks)
    delete_val(marks,1)
    show(marks)
    

if __name__ == "__main__":
    main()