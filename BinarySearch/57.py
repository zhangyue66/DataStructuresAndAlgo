from bisect import bisect_left
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        
        index = bisect_left(intervals,newInterval)
        
        intervals.insert(index,newInterval)
        
        # then start to merge the interval
        
        for interval in intervals:
            if len(ans) == 0:
                ans.append(interval)
            elif interval[0] > ans[-1][1]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1],interval[1])
                
        return ans
