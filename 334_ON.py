class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 , min2 = float("inf"),float("inf")
        
        for num in nums:
            if num < min1 :
                min1 = num
            elif num > min1 and num < min2 :
                min2 = num
                
            if min1 != float("inf") and min2 != float("inf"):
                if num > min2:
                    return True
                
        return False
