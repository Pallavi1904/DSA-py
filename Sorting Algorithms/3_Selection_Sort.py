class Selection_Sort:
    def __init__(self, arr):
        self.arr = arr

    def selection(self):
        n = len(self.arr)
        for i in range(n):
            index = i
            for j in range(i+1, n):
                if self.arr[j] < self.arr[index]:
                    index = j

            self.arr[i], self.arr[index] = self.arr[index],self.arr[i]
        return self.arr

def main():
    li = [10,3,4,12,35,22,12,2]
    q = Selection_Sort(li)
    print(f"Sorted array : {q.selection()}")
    
if __name__=="__main__":
    main() 