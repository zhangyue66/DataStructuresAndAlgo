class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # use binary search approach
        if len(arr) == k:
            return arr
        
        # find position of x in arr using binary search
        n = len(arr)
        l,r = 0,n
        #print(l)
        while l < r:
            mid = l + (r-l)//2
            if arr[mid] >= x:
                r = mid
            else:
                l = mid+1
                
        # sliding window from index
        
        low,high = l - 1,l
        
        while k > 0:
            if low == -1:
                high += 1
                k -= 1
            else:
                if high == n:
                    low -= 1
                elif abs(arr[low]-x) <= abs(arr[high]-x):
                    low -= 1           
                else:
                    high +=1
                    
                k -= 1
                
        return arr[low+1:high]
            
        
