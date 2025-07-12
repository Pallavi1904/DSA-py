class Insertion_sort:
    def __init__(self, li):
        self.li = li 
    
    def insertion(self):
        for i in range(1, len(self.li)):
            key = self.li[i]
            j = i -1

            while j>=0 and self.li[j] > key:
                self.li[j+1] = self.li[j]
                j -= 1
            self.li[j+1] = key

        return self.li

def main():
    li = [10,3,4,12,35,22,12,2]
    b = Insertion_sort(li)

    print(b.insertion())
    
if __name__=="__main__":
    main()