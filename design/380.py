import random
class RandomizedSet:

    def __init__(self):
        self.maps = {}
        self.nums = []
        

    def insert(self, val: int) -> bool:
        if val not in self.maps:
            self.maps[val] = len(self.nums)
            self.nums.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.maps:
            return False
        index = self.maps[val]
        self.maps[self.nums[-1]] = index
        self.maps.pop(val,None)
        self.nums[index],self.nums[-1] = self.nums[-1],self.nums[index]
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
