class Solution:
    def findRightInterval(self,intervals):

        if len(intervals) <= 1:
            return [-1]

        sorted_list = []

        for interval in intervals:
            sorted_list.append(interval)

        sorted_list.sort(key=lambda l:l[0]) # [[1, 2], [2, 3], [3, 4]]

        ans = []

        for interval in intervals:

            l,r = 0,len(sorted_list)-1
            while l <= r :
                mid = l+(r-l)//2

                if sorted_list[mid][0] >= interval[1]:
                    r=mid-1
                else:
                    l = mid + 1
            #print(mid)
            if l <= len(intervals)-1:
                ans.append(intervals.index(sorted_list[l]))
            else:
                ans.append(-1)

        return ans


yz = Solution()
intervals = [[3,4],[2,3],[1,2]]
print(yz.findRightInterval(intervals))
