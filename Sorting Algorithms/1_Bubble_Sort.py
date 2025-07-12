class Bubble_Sort:
    def __init__(self,li):
        self.li = li

    def Bubble(self):
        n = len(self.li)
        for i in range(n):
            if self.li == self.li.sort():
                print("Array is already sorted!!")
                return 
            for j in range(n - i -1):
                if self.li[j] > self.li[j+1]:
                    self.li[j], self.li[j + 1] = self.li[j + 1], self.li[j]
                    return True
                else:
                    print(f"No swap in iteration {j}")
        
        

def main():
    li = [10,3,4,12,35,67]
    b = Bubble_Sort(li)

    b.Bubble()
    print(f"List is: {b.li}")

    
    
    

if __name__=="__main__":
    main()
