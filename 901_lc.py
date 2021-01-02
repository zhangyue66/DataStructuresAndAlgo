class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        #print(self.stack)
        if not self.stack:
            self.stack.append([price,1])
            return 1
        else:
            if price < self.stack[-1][0]:
                self.stack.append([price,1])
                return 1
            else:
                ans = 1
                while self.stack and  self.stack[-1][0] <= price:
                    target = self.stack.pop()
                    ans += target[1]

                self.stack.append([price,ans])

                return ans
