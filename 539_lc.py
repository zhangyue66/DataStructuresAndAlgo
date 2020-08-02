class Solution:
    def findMinDifference(self, timePoints):
        #sort and compare
        timePoints.sort()
        #['00:00', '23:50', '23:59']
        ans = float("inf")
        new_time = []
        for _ in timePoints:
            yz = _.split(":")
            time = int(yz[0])*60+int(yz[1])
            new_time.append(time)
        #new time format [0, 1430, 1439]

        for i in range(len(new_time)):
            if i+1 <= len(new_time)-1:
                delta = new_time[i+1]-new_time[i]
                ans = min(delta,ans)

        last = new_time[0]+1440-new_time[-1]

        ans  = min(last,ans)


        return ans

yz = Solution()
timePoints = ["23:59","00:00","23:50"]
print(yz.findMinDifference(timePoints))
