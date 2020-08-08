class ProductOfNumbers:

    def __init__(self):
        self.list = [1]
        
        

    def add(self, num: int) -> None:
        if num == 0:
            self.list = [1]
        else:
            self.list.append(self.list[-1]*num)

        

    def getProduct(self, k: int) -> int:
        if k >= len(self.list):
            return 0
        else:
            return self.list[-1]//self.list[len(self.list)-1-k]



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
