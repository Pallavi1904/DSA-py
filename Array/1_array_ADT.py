class Myarray:
    def __init__(self, total_size, used_size):
        self.total_size = total_size
        self.used_size = used_size
        self.ptr = [0] * total_size   
        # ptr is list of [0, 0, 0, ...] till total_size
        # no need of dynamic allocation as list in python list is dynamic

def create_array(tsize, usize):
    return Myarray(tsize, usize)

def show(a):
    for i in range(a.used_size):
        print(a.ptr[i])

def set_val(a):
    for i in range(a.used_size):
        n = int(input(f"Enter the element {i}: "))
        a.ptr[i] = n

def main():
    marks = create_array(10, 3)
    set_val(marks)
    show(marks)

if __name__ == "__main__":
    main()