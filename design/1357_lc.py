class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.dict = {}
        self.n = n
        self.discount = discount
        for i in range(len(products)):
            self.dict[products[i]] = prices[i]
            
        self.cnt = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.cnt += 1
        
        total = 0
        
        for i in range(len(product)):
            total += self.dict[product[i]]*amount[i]
            
        if self.cnt % self.n == 0:
            return total - total*self.discount/100
        
        return total


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
