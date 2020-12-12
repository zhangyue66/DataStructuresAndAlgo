class Solution:
    def canFinish(self, numCourses: int, prerequisites):
        # Kahn's algorthim - find all vertx with 0 indegree
        if len(prerequisites) == 0:
            return True
        indegree = [0]*numCourses
        for pre in prerequisites:
            indegree[pre[0]] += 1

        queue = []

        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
                
        cnt = 0
        
        visited = set()
        
        while queue :
            v = queue.pop()
            #print(v)
            cnt += 1
            #visited.add(v)

            for prereq in prerequisites:
                if prereq[1] == v:
                    indegree[prereq[0]] -= 1
                    #print(indegree)
                    if indegree[prereq[0]] == 0:
                        queue.append(prereq[0])

            #print(indegree,cnt)
        if cnt < numCourses:
            return False
        return True
