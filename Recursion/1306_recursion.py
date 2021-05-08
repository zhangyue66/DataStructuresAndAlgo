class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # use recursion method
        visited = set()
        def helper(start):
            if start in visited:
                return
            if start is None:
                return
            if arr[start] == 0:
                return True
            visited.add(start)
            left = start-arr[start] if start-arr[start] >= 0 else None
            right = start + arr[start] if start+arr[start] < len(arr) else None
            #print(visited)
            return helper(left) or helper(right)
        
        return helper(start)
            
