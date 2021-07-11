from collections import defaultdict
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.value_dict = defaultdict(list)
        self.time_dict = defaultdict(list)
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.value_dict[key].append(value)
        self.time_dict[key].append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.value_dict:
            return ""
        # now using binary_search to get the index upper bound (rightmost index) 
        n = len(self.time_dict[key])
        l,r = 0,n
        while l < r:
            mid = l + (r-l)//2
            if self.time_dict[key][mid] > timestamp:
                r = mid
            else:
                l = mid + 1
                
        # return l
        if self.time_dict[key][l-1] <= timestamp:
            return self.value_dict[key][l-1]
        return ""
