from collections import defaultdict
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return 0
        pos_map = defaultdict(list)
        n = len(arr)
        for i in range(n):
            pos_map[arr[i]].append(i)
        self.visited = set()
        self.ans = float("inf")
        #print(pos_map)
        def bfs(start,end,step):
            queue = [(start,step)]
            
            while queue:
                cur,step = queue.pop(0)
                if cur == end:
                    self.ans = min(self.ans,step)
                # three choices for next move
                if cur+1 < n and cur+1 not in self.visited:
                    queue.append((cur+1,step+1))
                if cur -1 >= 0 and cur-1 not in self.visited:
                    queue.append((cur-1,step+1))
                if len(pos_map[arr[cur]]) > 1:
                    for pos in pos_map[arr[cur]]:
                        #print(pos)
                        if pos != cur and pos not in self.visited:
                            queue.append((pos,step+1))
                    pos_map[arr[cur]] = []
                
                self.visited.add(cur)
                
        bfs(0,n-1,0)
        return self.ans
