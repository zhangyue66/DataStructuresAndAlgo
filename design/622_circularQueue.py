class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1]*k
        self.capacity = k
        self.front = 0
        self.rear = 0
        self.size = 0
        

    def enQueue(self, value: int) -> bool:
        #insert after Rear
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = self.rear = 0
            self.queue[self.rear] = value
            self.size += 1
            return True
        self.rear += 1
        self.size += 1
        self.rear %= self.capacity
        self.queue[self.rear] = value
        return True
            

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        
        self.queue[self.front] = -1
        self.size -= 1
        self.front +=1
        self.front %= self.capacity
        return True
            
        

    def Front(self) -> int:
        return self.queue[self.front]

    def Rear(self) -> int:
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
