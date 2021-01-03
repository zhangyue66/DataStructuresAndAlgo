import heapq
from collections import OrderedDict
# use bucket sort to count frequency 

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity =  capacity
        
        self.lru_cache = OrderedDict()
        
        self.lfu_dict = {}
        
        self.lfu_bucket = [[] for i in range(10**4+1)]
        
        self.lfu_count = {}

    def get(self, key: int) -> int:
        if key not in self.lru_cache:
            return -1
        else:
            #key exisiting -> update LRU , update frequent count , return value
            self.lru_cache.move_to_end(key)
            
            bucket = self.lfu_count[key]
            
            self.lfu_bucket[bucket].remove(key)
            
            self.lfu_bucket[bucket+1].append(key)
            
            self.lfu_count[key] += 1
            
            return self.lfu_dict[key]
            

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0 :
            return
        if key in self.lru_cache or key in self.lfu_dict:
            # update count+1 , update bucket, update LRU_cache 
            
            self.lfu_dict[key] = value
            bucket = self.lfu_count[key]
            
            self.lfu_bucket[bucket].remove(key)
            
            self.lfu_bucket[bucket+1].append(key)
            
            self.lfu_count[key] += 1
            
            self.lru_cache.move_to_end(key)
            
        else:
            
            
        
            if len(self.lfu_dict) == self.capacity or len(self.lru_cache) == self.capacity:
                #first check who is LFU key
                found = False
                for i in range(1,10**4+2):
                    if len(self.lfu_bucket[i]) >=1 :
                        for k,v in self.lru_cache.items():
                            if k in self.lfu_bucket[i]:
                                # this is the key -k which is not recently used
                                target = k
                                found = i
                                break

                        if found:
                            break

                # now remove the found key - target
                self.lru_cache.pop(target)
                self.lfu_bucket[found].remove(target)
                self.lfu_count.pop(target)
                self.lfu_dict.pop(target)



            self.lfu_dict[key] = value
            self.lru_cache[key] = value
            self.lru_cache.move_to_end(key)
            self.lfu_count[key] = 1
            self.lfu_bucket[1].append(key)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
