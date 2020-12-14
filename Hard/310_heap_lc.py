import heapq
class Solution:
    def scheduleCourse(self, courses):
        courses.sort(key=lambda x:x[1])
        ans,s=[],0
        heapq.heappush(ans,0)
        for t,d in courses:
            if s+t>d:
                if t+ans[0]<0:
                    s+=t+ans[0]
                    heapq.heappushpop(ans,-t)
            else:
                s+=t
                heapq.heappush(ans,-t)
        return len(ans)-1
