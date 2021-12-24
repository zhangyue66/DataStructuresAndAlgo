from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        indegrees = [0]*numCourses
        graph = defaultdict(list)
        
        for course,pre_course in prerequisites:
            indegrees[course] += 1
            graph[pre_course].append(course)
        
            
        # BFS and queue to find topology sort
        queue = []
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
                
        while queue:
            cur = queue.pop(0)
            ans.append(cur)
            
            if cur in graph:
                for crs in graph[cur]:
                    indegrees[crs] -= 1
                    if indegrees[crs] == 0:
                        queue.append(crs)
        if len(ans) == numCourses:
            return ans
        return []
