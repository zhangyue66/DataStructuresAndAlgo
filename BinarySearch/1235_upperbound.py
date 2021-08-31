class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime,endTime,profit),key = lambda job:job[1])
        #print(jobs)
        dp = [[0,0]] # at time 0 profit is 0
        def binary_search(li,start):
            # binary search function to search in dp array , find the largest profit before start time
            l,r = 0,len(li)
            while l < r:
                mid = (r-l)//2 + l
                if li[mid][0] > start:
                    r = mid
                else:
                    l = mid + 1
            return l
        for s,e,p in jobs:
            index = binary_search(dp,s) - 1
            #print(index,dp)
            if dp[index][1] + p > dp[-1][1]:
                dp.append([e,dp[index][1]+p])
        return dp[-1][1]
            
            
