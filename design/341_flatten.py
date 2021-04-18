class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack =nestedList[::-1]
    
    def next(self) -> int:
        return self.stack.pop()
    
    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            cur = self.stack.pop().getList()[::-1]
            for data in cur:
                self.stack.append(data)
            

            
        return False
