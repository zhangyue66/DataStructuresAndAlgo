from itertools import combinations

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.ans = list(combinations(characters,combinationLength))
        print(self.ans)
        
        

    def next(self) -> str:
        if len(self.ans) != 0:
            return "".join(self.ans.pop(0))
        else:
            return
        

    def hasNext(self) -> bool:
        if len(self.ans) != 0:
            return True
        else:
            return False
        
    
    #def backtrack(self):
        
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
