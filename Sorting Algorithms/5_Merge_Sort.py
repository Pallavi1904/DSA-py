class Merge_Sort:
    def __init__(self,arr1,arr2):
        self.arr1 = arr1
        self.arr2 = arr2

    def merge(self):
        m = len(self.arr1) # arr1 and i
        n = len(self.arr2) # arr2 and j
        arr3 = []
        i = j = 0

        while i<m and j<n:
            if(self.arr1[i] > self.arr2[j]):
                arr3.append(self.arr2[j])
                j +=1

            else:
                arr3.append(self.arr1[i])
                i += 1
        
        while i < m:
            arr3.append(self.arr1[i])
            i += 1

        while j < n:
            arr3.append(self.arr2[j])
            j += 1
    
        return arr3

def main():
    li1 = [1, 2, 3, 4, 5]
    li2 = [6, 7, 8, 9, 10]

    mer = Merge_Sort(li1, li2)
    print(f"Merged array is: {mer.merge()}")
    
if __name__=="__main__":
    main()


