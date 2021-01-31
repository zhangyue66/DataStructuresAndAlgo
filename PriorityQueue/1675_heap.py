#results TLE 58/76 pass use maxHeap
import heapq
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        #credit to huahua
        for i in range(len(nums)):
            if nums[i] %2 == 1:#odd number
                nums[i] *= 2
        #print(nums)
        minheap = []
        for a in nums:
            heapq.heappush(minheap,-a)
            
        mini = -heapq.nlargest(1,minheap)[0]
        maxi = -heapq.nsmallest(1,minheap)[0]
        ans = abs(maxi - mini)
        #print(ans)
        
        while -heapq.nsmallest(1,minheap)[0] % 2 == 0:
            x = heapq.heappop(minheap)
            heapq.heappush(minheap,x//2)
            lo = heapq.nlargest(1,minheap)[0]
            maxi = heapq.nsmallest(1,minheap)[0]
            ans = min(ans,abs(maxi-lo))
            
            
            
        #print(minheap)   
        return ans
