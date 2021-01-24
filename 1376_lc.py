from collections import defaultdict

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager, informTime):
        if n == 1:
            return 0

        graph = defaultdict(list)
        for i in range(n):
            graph[manager[i]].append(i)
        #->defaultdict(<class 'list'>, {2: [0, 1, 3, 4, 5], -1: [2], 0: [], 1: [], 3: [], 4: [], 5: []})
        #->defaultdict(<class 'list'>, {2: [0, 1, 3, 4, 5], -1: [2], 0: [], 1: [], 3: [], 4: [], 5: []})
        # for idx, parent in enumerate(manager):
        #     graph[parent].append(idx)




        searched = set()

        queue = [(headID,informTime[headID])]

        ans = 0

        while queue:
            cur,time = queue.pop(0)
            ans = max(time,ans)
            if cur not in searched:
                searched.add(cur)
                for node in graph[cur]:
                    queue.append([node,time+informTime[node]])

        return ans


# n = 1
# headID = 0
# manager = [-1]
# informTime = [0]

n = 6
headID = 2
manager = [2,2,-1,2,2,2]
informTime = [0,0,1,0,0,0]
yz = Solution()
print(yz.numOfMinutes(n,headID,manager,informTime))
