import collections

class Solution:
    def gardenNoAdj(self, N, paths):
        graph =collections.defaultdict(list)

        for x,y in paths:
            graph[x].append(y)
            graph[y].append(x)

        #return graph
        #{1: [2, 3], 2: [1, 3], 3: [2, 1]}

        plantdict = {i:0 for i in range(1,N+1)}
        #{1: 0, 2: 0, 3: 0}
        for garden in graph:
            pick = set(range(1,5))
            for neighbor in graph[garden]:
                if plantdict[neighbor] != 0 and plantdict[neighbor] in pick:
                    pick.remove(plantdict[neighbor])

            plantdict[garden] = pick.pop()
        ans = []
        for key,value in plantdict.items():
            if value != 0:
                ans.append(plantdict[key])
            else:
                ans.append(1)

        return ans




N = 3
paths = [[1,2],[2,3],[3,1]]
yz = Solution()
print(yz.gardenNoAdj(N,paths))
