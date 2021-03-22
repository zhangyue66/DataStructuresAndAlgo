class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        # collections.Counter()
        
        dict1=collections.Counter(str(N))
        
        for i in range(33):
            dict2 = collections.Counter(str(2**i))
            if dict1 == dict2:
                return True
            
        return False
