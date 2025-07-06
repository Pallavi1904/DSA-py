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

# Linear Search
def linear_search(a,n):
    for i in range(a.used_size):
        if(a.ptr[i] == n):
            print(f"{n} is found at index {i}")
            return #Imp just remove return and see output
    print("Element not in array")

# # Sorting array 
# def Sort(a):
#     a.ptr[:a.used_size].sort()
#     print("Array Sorted")


# Binary Search
def Binary_search(a,n):
    a.ptr[:a.used_size].sort() # Sorting array
    low = 0
    high = a.used_size-1

    while(low <= high):
        mid = (low+high)//2       
        # // is called integer division (also known as floor division).
        # It divides and then rounds down to the nearest integer.

        if(a.ptr[mid] == n):
            print(f"Element {n} found at index {mid}")
            return
        elif(a.ptr[mid] > n):
            low = mid+1
        else:
            high = mid-1
    
    print("Element is not in Array")
    
        

def main():
    marks = create_array(10, 3)
    set_val(marks)
    show(marks)
    linear_search(marks,10)

    Binary_search(marks,1)
    show(marks)
    
    
    

if __name__ == "__main__":
    main()