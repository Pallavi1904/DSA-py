class Myarray:
    def __init__(self, total_size, used_size):
        self.total_size = total_size
        self.used_size = used_size
        self.ptr = [0] * total_size   


# Create array
def create_array(tsize, usize):
    return Myarray(tsize, usize)


# Display array
def show(a):
    print("Array elements:")
    for i in range(a.used_size):
        print(a.ptr[i])
    print("...................................")


# Insert elements
def set_val(a):
    for i in range(a.used_size):
        n = int(input(f"Enter element {i}: "))
        a.ptr[i] = n


# Linear Search
def linear_search(a, n):
    for i in range(a.used_size):
        if a.ptr[i] == n:
            print(f"{n} is found at index {i}")
            return
    print(f"{n} is not in the array.")


# Binary Search (without modifying original order)
def binary_search(a, n):
    # Create a sorted copy of the used part
    sorted_part = sorted(a.ptr[:a.used_size])
    low = 0
    high = len(sorted_part) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_part[mid] == n:
            print(f"Element {n} found at sorted index {mid}")
            return
        elif sorted_part[mid] > n:
            high = mid - 1
        else:
            low = mid + 1

    print(f"{n} is not in the array.")


# Main function
def main():
    marks = create_array(10, 5)
    set_val(marks)
    print("\nOriginal Array:")
    show(marks)

    # Linear search example
    linear_search(marks, 3)

    # Binary search example
    binary_search(marks, 3)


if __name__ == "__main__":
    main()
