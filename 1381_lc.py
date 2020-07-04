class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            
        

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        else:
            return self.stack.pop()
        val

    def increment(self, k: int, val: int) -> None:
        if len(self.stack) == 0:
            return
        else:
            if len(self.stack) <= k and len(self.stack) != 0 :
                for i in range(len(self.stack)):
                    self.stack[i] += val
            else:
                n = len(self.stack)
                for i in range(k):
                    self.stack[i] += val

            
            
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
