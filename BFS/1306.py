class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        self.visited = set()        
        def bfs(start,target):  
            queue = [start]
            
            while queue:
                cur = queue.pop(0)
                self.visited.add(cur)
                if cur in target:
                    return True
                left,right = "NA","NA"
                if cur-arr[cur] >= 0:
                    left = cur-arr[cur]
                if cur+arr[cur] < n:
                    right = cur+arr[cur]
                if left != "NA" and left not in self.visited:
                    queue.append(left)
                if right != "NA" and right not in self.visited:
                    queue.append(right)
            # print(self.visited) 
            # print(target)
            return False
                    
        n = len(arr)
        target = []
        
        for i in range(n):
            if arr[i] == 0:
                target.append(i)
                
        return bfs(start,target)
