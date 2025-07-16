class Count_Sort:
    def __init__(self, arr):
        self.arr = arr

    def CountSort(self):
        if len(self.arr) == 0:
            return self.arr
        
        max_ele = max(self.arr)
        count = [0]*(max_ele + 1)

        for num in self.arr:
            count[num] += 1
        
        sorted_array =[]
        for i in range(len(count)):
            sorted_array.extend([i] * count[i])

        return sorted_array
def main():
    li = [10, 7, 8, 9, 1, 5]
    co = Count_Sort(li)
    print(f"Sorted array: {co.CountSort()}")


if __name__=="__main__":
    main()