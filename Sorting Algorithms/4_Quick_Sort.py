class Quick_Sort:
    def __init__(self, li):
        self.li = li

    def quick(self, arr=None):  # optional argument for recursion
        if arr is None:
            arr = self.li

        if len(arr) <= 1:
            return arr

        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot] # j
        right = [x for x in arr[1:] if x > pivot] # i

        return self.quick(left) + [pivot] + self.quick(right)


def main():
    li = [10, 7, 8, 9, 1, 5]
    q = Quick_Sort(li)
    print("Sorted List:", q.quick())
    
if __name__=="__main__":
    main()