class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # bfs idea
        self.visited = set()
        n = len(arr)
        def bfs(start,end):
            queue = [start]
            
            while queue:
                cur = queue.pop(0)
                if cur in end:
                    return True
                self.visited.add(cur)
                far,close = 0,0
                if cur + arr[cur] < n and cur+arr[cur] not in self.visited:
                    far = cur+arr[cur]
                    queue.append(far)
                if cur - arr[cur] >= 0 and cur - arr[cur] not in self.visited:
                    close = cur - arr[cur]
                    queue.append(close)
            
            return False
        end = []
        for i in range(n):
            if arr[i] == 0:
                end.append(i)
        
        return bfs(start,end)
